---
aid: cloudrf
url: https://raw.githubusercontent.com/api-evangelist/cloudrf/refs/heads/main/apis.yml
name: CloudRF
tags:
  - Coverage Modeling
  - HF Propagation
  - Mesh Network
  - Radio Frequency
  - RF
  - Satellite
  - Signal Analysis
  - Telecommunications
  - Wireless Planning
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-07-02'
modified: '2026-04-26'
position: Consumer
x-type: company
x-company: CloudRF (Farrant Consulting Ltd.)
description: CloudRF is a radio frequency (RF) propagation, coverage modeling, and wireless network planning service. The HTTPS REST API at api.cloudrf.com offers point-to-multipoint coverage heatmaps, point-to-point path analysis, mesh networks, multisite, HF point-to-multipoint and point-to-point analysis, 3D coverage, satellite modeling, interference detection, geo-location of signals, archive and export of calculations, clutter and noise data management, account metrics, and reusable templates. Authentication is by API key passed as the `key` HTTP header.
apis:
  - aid: cloudrf:cloudrf-api
    name: CloudRF API
    tags:
      - Coverage Modeling
      - RF
      - Signal Analysis
    humanURL: https://cloudrf.com/documentation/developer/
    properties:
      - url: https://cloudrf.com/documentation/developer/
        type: Documentation
      - url: https://cloudrf.com/documentation/developer/swagger-ui/
        type: Reference
      - url: openapi/cloudrf-openapi.yml
        type: OpenAPI
      - url: https://github.com/Cloud-RF/CloudRF-API-clients
        type: Code Samples
    description: Public REST API for RF propagation, coverage modeling, mesh and multisite analysis, HF analysis, 3D and satellite modeling, interference detection, signal geo-location, archive/export, clutter and noise data, and reusable templates. Authentication is via the `key` HTTP header.
common:
  - type: Website
    url: https://cloudrf.com/
  - type: Documentation
    url: https://cloudrf.com/documentation/
  - type: Developer Documentation
    url: https://cloudrf.com/documentation/developer/
  - type: API Reference
    url: https://cloudrf.com/documentation/developer/swagger-ui/
  - type: Code Samples
    url: https://github.com/Cloud-RF/CloudRF-API-clients
  - type: Privacy Policy
    url: https://cloudrf.com/privacy
  - type: OpenAPI
    url: openapi/cloudrf-openapi.yml
  - type: JSON-LD
    url: json-ld/cloudrf-context.jsonld
  - type: Spectral
    url: rules/cloudrf-rules.yml
  - type: Naftiko Capabilities
    url: capabilities/cloudrf-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
