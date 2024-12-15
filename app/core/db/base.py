from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, declared_attr

from core import settings


class Base(DeclarativeBase):
    __abstract__ = True

    metadata = MetaData(naming_convention=settings.db.naming_convention)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f'{cls.__name__.lower()}s'