# coding: utf-8

"""
    VCell API

    VCell API

    The version of the OpenAPI document: 1.0.1
    Contact: vcell_support@uchc.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from vcell_api_client.models.biomodel_ref import BiomodelRef
from vcell_api_client.models.mathmodel_ref import MathmodelRef
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Publication(BaseModel):
    """
    Publication
    """ # noqa: E501
    pub_key: Optional[StrictInt] = Field(default=None, alias="pubKey")
    title: Optional[StrictStr] = None
    authors: Optional[List[StrictStr]] = None
    year: Optional[StrictInt] = None
    citation: Optional[StrictStr] = None
    pubmedid: Optional[StrictStr] = None
    doi: Optional[StrictStr] = None
    endnoteid: Optional[StrictInt] = None
    url: Optional[StrictStr] = None
    wittid: Optional[StrictInt] = None
    biomodel_refs: Optional[List[BiomodelRef]] = Field(default=None, alias="biomodelRefs")
    mathmodel_refs: Optional[List[MathmodelRef]] = Field(default=None, alias="mathmodelRefs")
    var_date: Optional[date] = Field(default=None, alias="date")
    __properties: ClassVar[List[str]] = ["pubKey", "title", "authors", "year", "citation", "pubmedid", "doi", "endnoteid", "url", "wittid", "biomodelRefs", "mathmodelRefs", "date"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of Publication from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in biomodel_refs (list)
        _items = []
        if self.biomodel_refs:
            for _item in self.biomodel_refs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['biomodelRefs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in mathmodel_refs (list)
        _items = []
        if self.mathmodel_refs:
            for _item in self.mathmodel_refs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['mathmodelRefs'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Publication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        # raise errors for additional fields in the input
        for _key in obj.keys():
            if _key not in cls.__properties:
                raise ValueError("Error due to additional fields (not defined in Publication) in the input: " + _key)

        _obj = cls.model_validate({
            "pubKey": obj.get("pubKey"),
            "title": obj.get("title"),
            "authors": obj.get("authors"),
            "year": obj.get("year"),
            "citation": obj.get("citation"),
            "pubmedid": obj.get("pubmedid"),
            "doi": obj.get("doi"),
            "endnoteid": obj.get("endnoteid"),
            "url": obj.get("url"),
            "wittid": obj.get("wittid"),
            "biomodelRefs": [BiomodelRef.from_dict(_item) for _item in obj.get("biomodelRefs")] if obj.get("biomodelRefs") is not None else None,
            "mathmodelRefs": [MathmodelRef.from_dict(_item) for _item in obj.get("mathmodelRefs")] if obj.get("mathmodelRefs") is not None else None,
            "date": obj.get("date")
        })
        return _obj


