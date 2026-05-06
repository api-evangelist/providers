---
aid: foreign-agricultural-service
name: Foreign Agricultural Service
description: The Foreign Agricultural Service (FAS) is a branch of the United States Department of Agriculture (USDA) that works to promote U.S. agricultural exports and expand global markets for American agricultural products.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-04-28'
position: Consumer
tags:
  - Agriculture
  - Federal Government
url: https://raw.githubusercontent.com/api-evangelist/foreign-agricultural-service/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: foreign-agricultural-service:fas-open-data
    name: USDA FAS Open Data API
    tags:
      - Agriculture
      - Trade
      - Federal Government
      - Open Data
    humanURL: https://apps.fas.usda.gov/opendataweb/home
    properties:
      - url: https://apps.fas.usda.gov/opendataweb/home
        type: Documentation
    description: The USDA Foreign Agricultural Service Open Data API provides programmatic access to U.S. agricultural trade data, including the Global Agricultural Trade System (GATS), Export Sales Reporting (ESR), and Production, Supply and Distribution (PSD) Online datasets.
common:
  - type: Website
    url: https://www.fas.usda.gov/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
