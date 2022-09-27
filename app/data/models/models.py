from tortoise import Model as DBModel, fields as db_fields

from app.shared.enums import NationalIdType, PersonType


class TimeStampedModel(DBModel):
    created_at = db_fields.DatetimeField(auto_now_add=True)
    updated_at = db_fields.DatetimeField(auto_now_add=True)

    class Meta:
        abstract = True


class CityTortoise(DBModel):
    id = db_fields.IntField(pk=True)
    name = db_fields.CharField(max_length=50, unique=True)
    timezone = db_fields.CharField(max_length=50)


class TablePersons(DBModel):
    person_id = db_fields.IntField(pk=True)
    national_id_type: NationalIdType = db_fields.CharEnumField(NationalIdType, max_length=3)
    national_id = db_fields.CharField(max_length=50, unique=True)
    person_type: PersonType = db_fields.CharEnumField(PersonType, max_length=1)

    def __str__(self):
        return f"person  national_id_type: {self.national_id_type} national_id: {self.national_id}"

