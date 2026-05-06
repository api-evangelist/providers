---
aid: national-energy-system-operator
name: National Energy System Operator
description: The National Energy System Operator (NESO) is the independent operator responsible for planning and operating Great Britain's electricity and gas networks. NESO publishes operational, market, and forecasting datasets through its Data Portal, which exposes a CKAN v3 API for programmatic access to energy system data including wind forecasts, demand predictions, balancing services, and transmission constraints.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/national-energy-system-operator/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
tags:
  - Energy
  - Electricity
  - Grid
  - Open Data
  - United Kingdom
apis:
  - aid: national-energy-system-operator:data-portal-api
    name: NESO Data Portal API
    description: CKAN v3 API for the NESO Data Portal providing programmatic access to datasets, resources, and tabular data through search, metadata, and datastore endpoints.
    humanURL: https://www.neso.energy/data-portal
    baseURL: https://api.neso.energy/api/3/action/
    tags:
      - Energy
      - CKAN
      - Open Data
      - Datasets
    properties:
      - type: Documentation
        url: https://www.neso.energy/data-portal/api-guidance
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/national-energy-system-operator/main/openapi/national-energy-system-operator-openapi.json
      - type: Portal
        url: https://www.neso.energy/data-portal
common:
  - type: Website
    url: https://www.neso.energy/
  - type: Portal
    url: https://www.neso.energy/data-portal
  - type: Documentation
    url: https://www.neso.energy/data-portal/api-guidance
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
