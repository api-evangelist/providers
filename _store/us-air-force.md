---
aid: us-air-force
url: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/apis.yml
apis:
  - aid: us-air-force:us-air-force-open-data
    name: US Air Force Open Data
    tags:
      - Air Force
      - Open Data
      - Federal Government
      - Military
      - Defense
    humanURL: https://www.data.af.mil/
    properties:
      - url: https://www.data.af.mil/
        type: Documentation
      - url: https://www.data.af.mil/Data-Catalog/
        type: DataCatalog
      - url: https://catalog.data.gov/dataset/?tags=air-force
        type: DataGov
      - url: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/json-schema/us-air-force-dataset-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/json-structure/us-air-force-dataset-structure.json
        type: JSONStructure
      - url: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/json-ld/us-air-force-context.jsonld
        type: JSONLDContext
      - url: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/examples/us-air-force-open-data-dataset-example.json
        type: Example
    description: The Air Force OPEN Data Program provides public access to Department of the Air Force datasets, covering military installations, personnel data, research findings, and operational information. The program supports the DAF's API-first architecture initiative and makes government data accessible to the public through structured data downloads in CSV and JSON formats.
  - aid: us-air-force:us-air-force-developer-api
    name: US Air Force DAF API Program
    tags:
      - Air Force
      - Developer API
      - Federal Government
      - Military
      - Defense
      - API-First
    humanURL: https://www.dafcio.af.mil/
    properties:
      - url: https://www.dafcio.af.mil/
        type: Documentation
      - url: https://www.dafcio.af.mil/Portals/64/Documents/Strategy/DAF%20API%20Roadmap%202.0_25OCT.pdf
        type: RoadMap
      - url: https://www.dafcio.af.mil/Portals/64/Documents/Strategy/DAF%20API%20Reference%20Architecture%202.0.pdf
        type: ReferenceArchitecture
      - url: https://software.af.mil/
        type: DeveloperPortal
    description: The Department of the Air Force API program provides a strategic framework for standardized APIs across the DAF enterprise. The DAF API Roadmap 2.0 and API Reference Architecture 2.0 guide the implementation of a modern API ecosystem, enabling seamless integration across command-and-control systems, intelligence systems, and partner organizations. The API-first approach covers FY2024 through FY2026 implementation phases.
name: US Air Force
tags:
  - Air Force
  - Federal Government
  - Military
  - Defense
  - Open Data
  - Government API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-21'
modified: '2026-05-03'
position: Consuming
description: The United States Air Force is responsible for providing air and space power to protect the United States and its interests. As part of the Department of the Air Force, the USAF has adopted an API-first architecture strategy to improve data sharing, software interoperability, and integration across military systems. The DAF publishes open datasets through data.af.mil and provides developer resources through software.af.mil.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
