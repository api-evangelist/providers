---
aid: danish-meteorological-institutes
url: https://raw.githubusercontent.com/api-evangelist/danish-meteorological-institutes/refs/heads/main/apis.yml
apis:
  - aid: danish-meteorological-institutes:dmi-open-data-api
    name: DMI Open Data API
    tags:
      - Climate
      - Environment
      - Lightning
      - Meteorological
      - Ocean
      - Open Data
      - Weather
    humanURL: https://opendatadocs.dmi.govcloud.dk/
    baseURL: https://opendataapi.dmi.dk/v2
    properties:
      - url: https://opendatadocs.dmi.govcloud.dk/
        type: Documentation
      - url: https://opendatadocs.dmi.govcloud.dk/Authentication
        type: Authentication
      - url: openapi/dmi-open-data-api-openapi.yml
        type: OpenAPI
      - url: json-schema/observation.json
        type: JSONSchema
      - url: json-schema/station.json
        type: JSONSchema
      - url: rules/dmi-open-data-api-rules.yml
        type: Rules
      - url: capabilities/dmi-open-data-api-capabilities.yml
        type: Capabilities
    description: The DMI Open Data API provides access to four core public services - meteorological observations (metObs), climate data (climateData), ocean observations (oceanObs), and lightning data (lightningData) - via OGC API compatible feature collections. Each service requires a per-service API key obtained through the DMI Open Data portal.
name: Danish Meteorological Institutes
tags:
  - Climate
  - Environment
  - Lightning
  - Meteorological
  - Ocean
  - Open Data
  - Weather
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2025-02-06'
modified: '2026-04-28'
position: Consumer
description: The Danish Meteorological Institute is a government agency responsible for providing meteorological and climate services in Denmark. DMI publishes weather observations, climate data, ocean observations, and lightning data through its Open Data API and supplies forecast products via the AWS Open Data registry. The agency operates weather stations, radar systems, and satellites to monitor and forecast weather across Denmark, Greenland, and the Faroe Islands.
common:
  - type: Website
    url: https://www.dmi.dk/
  - type: Open Data Portal
    url: https://opendatadocs.dmi.govcloud.dk/
  - type: Open Data FAQ
    url: https://opendatadocs.dmi.govcloud.dk/en/FAQ
  - type: AWS Open Data
    url: https://registry.opendata.aws/dmi-opendata/
  - type: GitHub Organization
    url: https://github.com/dmidk
  - type: JSON-LD
    url: json-ld/dmi-context.jsonld
  - type: Vocabulary
    url: vocabulary/dmi-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
xType: company
---
