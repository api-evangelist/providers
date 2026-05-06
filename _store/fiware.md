---
aid: fiware
name: FIWARE
description: FIWARE is an open-source framework that provides a curated set of standards and components for context information management. The cornerstone is the NGSI-LD API standardized by ETSI ISG CIM, which allows applications to provide, consume, and subscribe to context information in smart cities, smart industry, smart agriculture, and smart energy scenarios.
type: Standard
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-07-02'
modified: '2026-04-28'
position: Consumer
tags:
  - Context Information
  - Devices
  - Internet of Things
  - Linked Data
  - NGSI
  - Smart Cities
  - Standards
url: https://raw.githubusercontent.com/api-evangelist/fiware/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: fiware:ngsi-ld
    name: FIWARE NGSI-LD API
    description: The NGSI-LD API defined by ETSI ISG CIM is a Cross-domain Context Information Management API that allows applications to provide, consume, and subscribe to context information in multiple scenarios and involving multiple stakeholders. It is the linked-data evolution of the NGSI specification and forms the foundation of FIWARE-based smart solutions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/FIWARE/specifications/tree/master/OpenAPI/ngsi-ld
    tags:
      - Context Information
      - Linked Data
      - NGSI-LD
      - Standards
    properties:
      - type: Documentation
        url: https://fiware-orion.readthedocs.io/
      - type: Specification
        url: https://github.com/FIWARE/specifications/tree/master/OpenAPI/ngsi-ld
      - type: OpenAPI
        url: openapi/fiware-ngsi-ld-openapi.yml
  - aid: fiware:ngsi-v2
    name: FIWARE NGSI v2 API
    description: The NGSI v2 API is the previous generation context broker specification that established the patterns later evolved into NGSI-LD. It is widely implemented by Orion Context Broker and is still in use across many FIWARE-based deployments for managing entities, attributes, and subscriptions.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://github.com/FIWARE/specifications/tree/master/OpenAPI/ngsiv2
    tags:
      - Context Information
      - NGSI
      - Standards
    properties:
      - type: Documentation
        url: https://fiware-orion.readthedocs.io/
      - type: Specification
        url: https://github.com/FIWARE/specifications/tree/master/OpenAPI/ngsiv2
      - type: OpenAPI
        url: openapi/fiware-ngsiv2-openapi.yml
common:
  - type: Website
    url: https://www.fiware.org/
  - type: GitHub Organization
    url: https://github.com/FIWARE
  - type: Documentation
    url: https://fiware-orion.readthedocs.io/
  - type: Specifications
    url: https://github.com/FIWARE/specifications
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
