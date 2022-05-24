from datetime import datetime
from mongoengine import (
    Document,
    StringField,
    DateTimeField,
    ListField
)


class User(Document):
    username = StringField(required=True, max_length=200, unique=True)
    created_at = DateTimeField(default=datetime.utcnow)
    tags = ListField(StringField(max_length=50))
