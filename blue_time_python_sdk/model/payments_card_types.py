# coding: utf-8

"""
    Orchestra API

    Code Version 1.0.7.15

    The version of the OpenAPI document: Prod
    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from blue_time_python_sdk import schemas  # noqa: F401


class PaymentsCardTypes(
    schemas.EnumBase,
    schemas.StrSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            "Visa": "VISA",
            "AMEX": "AMEX",
            "BC": "BC",
            "MasterCard": "MASTER_CARD",
            "MC_Alaska": "MC_ALASKA",
            "MC_Canada": "MC_CANADA",
            "CarteBlanche": "CARTE_BLANCHE",
            "UnionPay": "UNION_PAY",
            "Discover": "DISCOVER",
            "DinersClub": "DINERS_CLUB",
            "CartaSi": "CARTA_SI",
            "CarteBleue": "CARTE_BLEUE",
            "Dankort": "DANKORT",
            "Delta": "DELTA",
            "Electron": "ELECTRON",
            "JCB": "JCB",
            "Maestro": "MAESTRO",
            "Switch": "SWITCH",
            "Solo": "SOLO",
            "Lazer": "LAZER",
            "Elo": "ELO",
            "Hipercard": "HIPERCARD",
            "enRoute": "EN_ROUTE",
            "UATP": "UATP",
        }
    
    @schemas.classproperty
    def VISA(cls):
        return cls("Visa")
    
    @schemas.classproperty
    def AMEX(cls):
        return cls("AMEX")
    
    @schemas.classproperty
    def BC(cls):
        return cls("BC")
    
    @schemas.classproperty
    def MASTER_CARD(cls):
        return cls("MasterCard")
    
    @schemas.classproperty
    def MC_ALASKA(cls):
        return cls("MC_Alaska")
    
    @schemas.classproperty
    def MC_CANADA(cls):
        return cls("MC_Canada")
    
    @schemas.classproperty
    def CARTE_BLANCHE(cls):
        return cls("CarteBlanche")
    
    @schemas.classproperty
    def UNION_PAY(cls):
        return cls("UnionPay")
    
    @schemas.classproperty
    def DISCOVER(cls):
        return cls("Discover")
    
    @schemas.classproperty
    def DINERS_CLUB(cls):
        return cls("DinersClub")
    
    @schemas.classproperty
    def CARTA_SI(cls):
        return cls("CartaSi")
    
    @schemas.classproperty
    def CARTE_BLEUE(cls):
        return cls("CarteBleue")
    
    @schemas.classproperty
    def DANKORT(cls):
        return cls("Dankort")
    
    @schemas.classproperty
    def DELTA(cls):
        return cls("Delta")
    
    @schemas.classproperty
    def ELECTRON(cls):
        return cls("Electron")
    
    @schemas.classproperty
    def JCB(cls):
        return cls("JCB")
    
    @schemas.classproperty
    def MAESTRO(cls):
        return cls("Maestro")
    
    @schemas.classproperty
    def SWITCH(cls):
        return cls("Switch")
    
    @schemas.classproperty
    def SOLO(cls):
        return cls("Solo")
    
    @schemas.classproperty
    def LAZER(cls):
        return cls("Lazer")
    
    @schemas.classproperty
    def ELO(cls):
        return cls("Elo")
    
    @schemas.classproperty
    def HIPERCARD(cls):
        return cls("Hipercard")
    
    @schemas.classproperty
    def EN_ROUTE(cls):
        return cls("enRoute")
    
    @schemas.classproperty
    def UATP(cls):
        return cls("UATP")
