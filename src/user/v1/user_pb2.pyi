from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class User(_message.Message):
    __slots__ = ("firstname", "middlename", "lastname", "email", "phone", "dob")
    FIRSTNAME_FIELD_NUMBER: _ClassVar[int]
    MIDDLENAME_FIELD_NUMBER: _ClassVar[int]
    LASTNAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    DOB_FIELD_NUMBER: _ClassVar[int]
    firstname: str
    middlename: str
    lastname: str
    email: str
    phone: str
    dob: str
    def __init__(self, firstname: _Optional[str] = ..., middlename: _Optional[str] = ..., lastname: _Optional[str] = ..., email: _Optional[str] = ..., phone: _Optional[str] = ..., dob: _Optional[str] = ...) -> None: ...

class CreateRequest(_message.Message):
    __slots__ = ("user",)
    USER_FIELD_NUMBER: _ClassVar[int]
    user: User
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class CreateResponse(_message.Message):
    __slots__ = ("id", "success")
    ID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    id: str
    success: bool
    def __init__(self, id: _Optional[str] = ..., success: _Optional[bool] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ("user", "success")
    USER_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    user: User
    success: bool
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., success: _Optional[bool] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("id", "user")
    ID_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    id: str
    user: User
    def __init__(self, id: _Optional[str] = ..., user: _Optional[_Union[User, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("user", "success")
    USER_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    user: User
    success: bool
    def __init__(self, user: _Optional[_Union[User, _Mapping]] = ..., success: _Optional[bool] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: str
    def __init__(self, id: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: _Optional[bool] = ...) -> None: ...
