---
aid: food-safety-and-inspection-service
name: Food Safety and Inspection Service
description: The Food Safety and Inspection Service (FSIS) is a branch of the United States Department of Agriculture (USDA) responsible for ensuring the safety of the nation's commercial supply of meat, poultry, and egg products. FSIS publishes a Recall API that provides machine-readable access to recall and public health alert records.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-04-28'
position: Consumer
tags:
  - Federal Government
  - Food
  - Food Safety
  - Inspections
  - Recalls
  - Meat
  - Poultry
  - Eggs
url: https://raw.githubusercontent.com/api-evangelist/food-safety-and-inspection-service/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: food-safety-and-inspection-service:fsis-recall
    name: FSIS Recall API
    tags:
      - Recalls
      - Food Safety
      - Public Health Alerts
    humanURL: https://www.fsis.usda.gov/science-data/developer-resources/recall-api
    baseURL: https://www.fsis.usda.gov/fsis/api
    description: The FSIS Recall API returns a JSON list of recall and public health alert records for meat, poultry, and egg products. The endpoint is open and unauthenticated; the full dataset is returned on each request.
    properties:
      - type: Documentation
        url: https://www.fsis.usda.gov/science-data/developer-resources/recall-api
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/food-safety-and-inspection-service/refs/heads/main/openapi/fsis-recall-openapi.yml
      - type: Capabilities
        url: https://raw.githubusercontent.com/api-evangelist/food-safety-and-inspection-service/refs/heads/main/capabilities/fsis-recall-capabilities.yml
      - type: Rules
        url: https://raw.githubusercontent.com/api-evangelist/food-safety-and-inspection-service/refs/heads/main/rules/fsis-recall-rules.yml
common:
  - type: Website
    url: https://www.fsis.usda.gov/
  - type: Documentation
    url: https://www.fsis.usda.gov/science-data/developer-resources/recall-api
  - type: Recalls
    url: https://www.fsis.usda.gov/recalls
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
