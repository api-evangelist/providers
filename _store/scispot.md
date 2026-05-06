---
aid: scispot
name: Scispot
description: Scispot is a cloud-native laboratory data platform and operating system for modern life science labs. It provides an API-first architecture combining Electronic Lab Notebook (ELN) and Laboratory Information Management System (LIMS) capabilities with over 250 pre-built instrument connectors and 7,000+ application integrations via its GLUE layer. Labs use Scispot to centralize and activate their data, automate experiment workflows, manage samples, sequences, and chemical structures programmatically, and integrate with clinical data standards including HL7 FHIR, HL7 v2, and ASTM protocols.
url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/apis.yml
created: '2026-05-02'
modified: '2026-05-02'
specificationVersion: '0.19'
tags:
  - Laboratory
  - Life Science
  - LIMS
  - ELN
  - Biotech
  - API First
  - Scientific Data
  - Healthcare
apis:
  - aid: scispot:scispot-api
    name: Scispot API
    description: The Scispot REST API provides programmatic access to all laboratory data management features including Labsheets (LIMS), Electronic Lab Notebooks (ELN), Manifests (plates, boxes, racks), and Sequences. Authenticated via personal API tokens, the API supports creating, reading, updating, and searching lab records, samples, barcodes, experimental results, and biological sequences. The API follows a flat, consistent schema designed for computational biology and dry-lab automation.
    humanURL: https://www.scispot.com/
    baseURL: https://api.scispot.com/v1
    tags:
      - Laboratory
      - LIMS
      - ELN
      - Life Science
      - Biotech
      - Samples
      - Sequences
    properties:
      - type: Documentation
        url: https://docs.scispot.com/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/openapi/scispot-openapi.yml
      - type: Developer Portal
        url: https://www.scispot.com/compbio
      - type: SpectralRules
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/rules/scispot-rules.yml
      - type: NaftikoCapabilities
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/capabilities/lab-data-management.yaml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/json-schema/scispot-labsheet-schema.json
      - type: JSONLDContext
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/json-ld/scispot-context.jsonld
      - type: Vocabulary
        url: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/vocabulary/scispot-vocabulary.yml
common:
  - type: Website
    url: https://www.scispot.com/
  - type: Documentation
    url: https://docs.scispot.com/
  - type: Developer Portal
    url: https://www.scispot.com/compbio
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
