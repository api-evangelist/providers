---
aid: united-states-fire-administration
url: https://raw.githubusercontent.com/api-evangelist/united-states-fire-administration/refs/heads/main/apis.yml
apis:
  - aid: united-states-fire-administration:openfema-fire-data-api
    name: OpenFEMA Fire Data API
    tags:
      - Fire Safety
      - Incident Reporting
      - Emergency Management
      - NFIRS
      - Federal Government
    humanURL: https://www.fema.gov/about/openfema/api
    baseURL: https://www.fema.gov/api/open
    properties:
      - url: https://www.fema.gov/about/openfema/api
        type: Documentation
      - url: https://www.fema.gov/about/openfema/developer-resources
        type: Portal
      - url: https://www.fema.gov/about/openfema/data-sets
        type: DataSets
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-fire-administration/refs/heads/main/openapi/openfema-fire-data-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-fire-administration/refs/heads/main/rules/openfema-fire-data-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/united-states-fire-administration/refs/heads/main/capabilities/fire-incident-data.yaml
        type: NaftikoCapability
    description: The OpenFEMA API provides free, read-only REST access to FEMA and USFA datasets including the National Fire Incident Reporting System (NFIRS) annual public data, disaster declarations, and other emergency management data. No API key is required. The API supports filtering, sorting, pagination, and field selection for all available datasets.
name: United States Fire Administration
tags:
  - Federal Government
  - Fire Safety
  - Emergency Management
  - Public Safety
  - FEMA
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consumer
description: The United States Fire Administration (USFA) is a government agency under the Federal Emergency Management Agency (FEMA) that is responsible for providing leadership and support to fire departments across the country. The USFA works to improve fire prevention and safety by disseminating training and education programs, conducting research on fire-related issues, and developing national fire prevention initiatives. USFA manages the National Fire Incident Reporting System (NFIRS) and the National Fire Academy (NFA). Fire incident data is accessible through the OpenFEMA API platform at www.fema.gov/api/open.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
