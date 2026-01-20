import logging
from os import environ

from user.v1.user_connect import UserService, UserServiceASGIApplication
from user.v1.user_pb2 import User, CreateRequest, CreateResponse, ReadRequest, ReadResponse, UpdateRequest, UpdateResponse, DeleteRequest, DeleteResponse
from surrealdb import Surreal, RecordID

logging.basicConfig(
    level=environ.get("LOGLEVEL", "INFO"),
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)
logger = logging.getLogger(__name__)

class Users(UserService):
    def __init__(self):
        surreal_host = environ.get("SURREALDB_HOST", "localhost")
        surreal_port = environ.get("SURREALDB_PORT", "8080")
        surreal_user = environ.get("SURREALDB_USER", "root")
        surreal_pass = environ.get("SURREALDB_PASS", "root")
        sureral_ns = environ.get("SURREALDB_NS", "ironclad")
        surreal_db = environ.get("SURREALDB_DB", "test")
        self.db = Surreal(f"ws://{surreal_host}:{surreal_port}/rpc")
        self.db.signin({"username": surreal_user, "password": surreal_pass})
        self.db.use(sureral_ns, surreal_db)

    async def create(self, request: CreateRequest, ctx):
        user_req = request.user
        # Error if email is empty
        if not user_req.email:
            return CreateResponse(success=False)
        logger.debug("Creating user: %s", user_req)
        user_db = self.db.create('user', {
            'firstname': user_req.firstname,
            'middlename': user_req.middlename,
            'lastname': user_req.lastname,
            'email': user_req.email,
            'phone': user_req.phone,
            'dob': user_req.dob
        })
        logger.debug("User created in DB: %s", user_db['id'])
        response = CreateResponse(id=user_db['id'].id, success=True)
        ctx.response_headers()["user-version"] = "v1"
        return response

    async def read(self, request: ReadRequest, ctx):
        rid = RecordID('user', request.id)
        logger.debug("Reading user with ID: %s", rid)
        result = self.db.select(rid)
        logger.debug("User read from DB: %s", result)
        user = result[0]
        logger.debug("User data: %s", user)
        response = ReadResponse(
            user=User(
                email=user['email'],
                firstname=user['firstname'],
                middlename=user['middlename'],
                lastname=user['lastname'],
                phone=user['phone'],
                dob=user['dob']
            ),
            success=True
        )
        ctx.response_headers()["user-version"] = "v1"
        return response
    
    async def update(self, request: UpdateRequest, ctx):
        rid = RecordID('user', request.id)
        logger.debug("Updating user with ID: %s", rid)
        try:
            user_db = self.db.update(rid, {
                'firstname': request.user.firstname,
                'middlename': request.user.middlename,
                'lastname': request.user.lastname,
                'email': request.user.email,
                'phone': request.user.phone,
                'dob': request.user.dob
            })
            user = user_db
            response = UpdateResponse(
                user=User(
                    email=user['email'],
                    firstname=user['firstname'],
                    middlename=user['middlename'],
                    lastname=user['lastname'],
                    phone=user['phone'],
                    dob=user['dob']
                ),
                success=True
            )
        except Exception as e:
            logger.exception("User update failed")
            response = UpdateResponse(success=False)
        ctx.response_headers()["user-version"] = "v1"
        return response
    
    async def delete(self, request: DeleteRequest, ctx):
        rid = RecordID('user', request.id)
        logger.debug("Deleting user with ID: %s", rid)
        try:
            self.db.delete(rid)
            response = DeleteResponse(success=True)
        except Exception as e:
            logger.exception("User deletion failed")
            response = DeleteResponse(success=False)
        ctx.response_headers()["user-version"] = "v1"
        return response

app = UserServiceASGIApplication(Users())
