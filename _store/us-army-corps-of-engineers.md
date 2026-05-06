---
aid: us-army-corps-of-engineers
url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/apis.yml
apis:
  - aid: us-army-corps-of-engineers:usace-cwms-data
    name: USACE CWMS Data API
    tags:
      - Water Resources
      - Federal Government
      - Water Data
      - Hydrological Data
      - Open Data
      - Timeseries
      - REST API
    humanURL: https://cwms-data.usace.army.mil/cwms-data/
    baseURL: https://cwms-data.usace.army.mil/cwms-data
    properties:
      - url: https://cwms-data.usace.army.mil/cwms-data/
        type: Documentation
      - url: https://cwms-data.usace.army.mil/cwms-data/swagger-ui.html
        type: SwaggerUI
      - url: https://github.com/USACE/cwms-data-api
        type: GitHubRepository
      - url: https://cwms-data-api.readthedocs.io/latest/
        type: APIDocumentation
      - url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/openapi/usace-cwms-data-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/rules/usace-cwms-data-rules.yml
        type: SpectralRuleset
      - url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/capabilities/water-data.yaml
        type: NaftikoCapability
      - url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/json-schema/usace-timeseries-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/us-army-corps-of-engineers/refs/heads/main/json-ld/us-army-corps-of-engineers-context.jsonld
        type: JSONLDContext
    description: The Corps Water Management System Data API (CDA) is a RESTful API providing public access to USACE water management data. It supports retrieval of timeseries data (stream flow, reservoir levels, precipitation), location information, rating tables, location levels, reservoirs, and a full data catalog. The API supports pagination, unit conversion, and multiple date/time formats (ISO 8601 or epoch milliseconds). Data is publicly available without authentication for reading.
  - aid: us-army-corps-of-engineers:usace-national-inventory-of-dams
    name: USACE National Inventory of Dams API
    tags:
      - Dams
      - Federal Government
      - Water Infrastructure
      - Safety
      - Geospatial Data
    humanURL: https://nid.sec.usace.army.mil/
    properties:
      - url: https://nid.sec.usace.army.mil/
        type: Documentation
      - url: https://nid.sec.usace.army.mil/api/developer
        type: SwaggerUI
      - url: https://geospatial-usace.opendata.arcgis.com/datasets/1632cb2bb23046569fbf2bc144f06764_0
        type: GISData
    description: The National Inventory of Dams (NID) API provides access to the comprehensive database of US dams maintained by the US Army Corps of Engineers. The database contains information on over 70 data fields for each dam including location, size, type, purpose, hazard classification, last inspection date, and owner information. The API supports searching and filtering dam records.
  - aid: us-army-corps-of-engineers:usace-open-data
    name: USACE Open Data
    tags:
      - Open Data
      - Federal Government
      - Geospatial Data
      - Water Resources
      - Infrastructure
    humanURL: https://www.usace.army.mil/open/
    properties:
      - url: https://www.usace.army.mil/open/
        type: Documentation
      - url: https://geospatial-usace.opendata.arcgis.com/
        type: GeoSpatialPortal
      - url: https://catalog.data.gov/dataset?publisher=US+Army+Corps+of+Engineers
        type: DataGov
      - url: https://permits.ops.usace.army.mil/
        type: PermitsPortal
    description: The USACE Open Data program provides public access to geospatial data, regulatory permit information, and other datasets maintained by the US Army Corps of Engineers. Data is available through ArcGIS Open Data, data.gov, and the USACE Regulatory portal.
name: US Army Corps of Engineers
tags:
  - Water Resources
  - Federal Government
  - Military Engineering
  - Infrastructure
  - Open Data
  - Geospatial Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-03'
position: Consuming
description: The US Army Corps of Engineers is a federal agency that plays a critical role in managing the nation's water resources and infrastructure. They are responsible for building and maintaining dams, levees, and flood control systems, overseeing construction of ports, harbors, and waterways, and providing engineering support to military operations. USACE publishes open APIs including the CWMS Data API for water management timeseries data, the National Inventory of Dams API, and open geospatial datasets.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
