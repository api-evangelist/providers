---
aid: federal-emergency-management-agency
name: Federal Emergency Management Agency
description: The Federal Emergency Management Agency (FEMA) coordinates the federal government's role in preparing for, preventing, mitigating, responding to, and recovering from disasters. The OpenFEMA program provides programmatic access to disaster declarations, public assistance, individual assistance, hazard mitigation, and National Flood Insurance Program (NFIP) data.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Disasters
  - Emergencies
  - Federal Government
  - Flood Insurance
  - Hazard Mitigation
url: https://raw.githubusercontent.com/api-evangelist/federal-emergency-management-agency/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: federal-emergency-management-agency:openfema
    name: OpenFEMA API
    description: The OpenFEMA API provides programmatic access to FEMA's public datasets including disaster declarations, public assistance, individual assistance, hazard mitigation grants, and the National Flood Insurance Program.
    humanURL: https://www.fema.gov/about/openfema/api
    baseURL: https://www.fema.gov/api/open
    tags:
      - Disasters
      - Emergencies
      - Flood Insurance
      - Hazard Mitigation
    properties:
      - type: Documentation
        url: https://www.fema.gov/about/openfema/api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/federal-emergency-management-agency/refs/heads/main/openapi/openfema.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/federal-emergency-management-agency/refs/heads/main/rules/openfema-rules.yml
common:
  - type: Website
    url: https://www.fema.gov/
  - type: Documentation
    url: https://www.fema.gov/about/openfema/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
