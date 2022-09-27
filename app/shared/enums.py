from enum import Enum


class NationalIdType(str, Enum):
    CIUDADANIA = "CCI"
    TARJETA = "TDI"
    PASAPORTE = "PPT"
    VISA = "VIS"
    EXTRANJERIA = "CEX"
    NIT = "NIT"
    TAXID = "TAXID"


class PersonType(str, Enum):
    JURIDICAL = "J"
    NATURAL = "N"