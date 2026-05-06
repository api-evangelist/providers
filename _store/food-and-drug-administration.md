---
aid: food-and-drug-administration
name: Food and Drug Administration
description: openFDA is an Elasticsearch-based public API that serves FDA data on drugs, devices, foods, animal/veterinary products, and tobacco. Each noun exposes one or more datasets including adverse events, recall enforcement reports, product labeling, classifications, registrations, and approvals.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Drugs
  - Devices
  - Federal Government
  - Food Safety
  - Public Data
  - Recalls
  - Adverse Events
url: https://raw.githubusercontent.com/api-evangelist/food-and-drug-administration/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: food-and-drug-administration:openfda
    name: openFDA
    tags:
      - Drugs
      - Devices
      - Food
      - Animal & Veterinary
      - Tobacco
    humanURL: https://open.fda.gov/apis
    baseURL: https://api.fda.gov
    description: openFDA provides public APIs for drug adverse events (FAERS), drug labeling (SPL), drug recall enforcement, NDC directory, Drugs@FDA, drug shortages, device adverse events (MAUDE), 510(k), PMA, UDI, device classification, food recall enforcement, food adverse events (CAERS), animal/veterinary adverse events, and tobacco problem reports.
    properties:
      - type: Documentation
        url: https://open.fda.gov/apis
      - type: Authentication
        url: https://open.fda.gov/apis/authentication/
      - type: TermsOfService
        url: https://open.fda.gov/terms/
      - type: StatusPage
        url: https://open.fda.gov/about/status/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/food-and-drug-administration/refs/heads/main/openapi/openfda-openapi.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/food-and-drug-administration/refs/heads/main/capabilities/openfda-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/food-and-drug-administration/refs/heads/main/rules/openfda-rules.yml
common:
  - type: Website
    url: https://www.fda.gov/
  - type: Documentation
    url: https://open.fda.gov/apis
  - type: Authentication
    url: https://open.fda.gov/apis/authentication/
  - type: TermsOfService
    url: https://open.fda.gov/terms/
  - type: GitHub
    url: https://github.com/FDA/openfda
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
