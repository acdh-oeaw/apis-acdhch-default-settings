import os

from apis_core.utils.autocomplete import (
    ExternalAutocomplete,
    TypeSenseAutocompleteAdapter,
    LobidAutocompleteAdapter,
)


class E74_GroupExternalAutocomplete(ExternalAutocomplete):
    adapters = [
        LobidAutocompleteAdapter(
            params={
                "filter": "type:CorporateBody",
                "format": "json:preferredName,geographicAreaCode,dateOfEstablishment,broaderTermInstantial",
            },
            data_mapping={"label": "label"},
        ),
    ]


class E53_PlaceExternalAutocomplete(ExternalAutocomplete):
    adapters = [
        TypeSenseAutocompleteAdapter(
            collections=[
                "prosnet-wikidata-place-index",
                "prosnet-geonames-place-index",
            ],
            template="e53_place_from_typesense_autocomplete_result.html",
            token=os.getenv("TYPESENSE_TOKEN", None),
            server=os.getenv("TYPESENSE_SERVER", None),
            data_mapping={"label": ["document", "label"]},
        ),
        LobidAutocompleteAdapter(
            params={
                "filter": "type:PlaceOrGeographicName",
                "format": "json:preferredName",
            },
            data_mapping={"label": "label"},
        ),
    ]


class E21_PersonExternalAutocomplete(ExternalAutocomplete):
    adapters = [
        TypeSenseAutocompleteAdapter(
            collections="prosnet-wikidata-person-index",
            token=os.getenv("TYPESENSE_TOKEN", None),
            server=os.getenv("TYPESENSE_SERVER", None),
            data_mapping={"surname": ["document", "label"]},
        ),
        LobidAutocompleteAdapter(
            params={
                "filter": "type:Person",
                "format": "json:preferredName,professionOrOccupation",
            },
            data_mapping={"surname": "label"},
        ),
    ]
