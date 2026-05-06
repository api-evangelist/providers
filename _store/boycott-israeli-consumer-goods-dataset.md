---
aid: boycott-israeli-consumer-goods-dataset
url: https://raw.githubusercontent.com/api-evangelist/boycott-israeli-consumer-goods-dataset/refs/heads/main/apis.yml
name: Boycott Israeli Consumer Goods Dataset
tags:
  - Boycotts
  - Consumers
  - Datasets
  - Palestine
  - BDS Movement
  - Open Data
  - YAML
type: Index
x-type: topic
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-04-21'
position: Consumer
description: The Boycott Israeli Consumer Goods Dataset, maintained by TechForPalestine, is a version-controlled, golden-source repository collating consumer boycott and alternative product data into a single consumable dataset. The project aggregates data from authoritative sources including the Who Profits Research Center, the BDS Movement boycott guide, and the AFSC profiteering company list. Data is stored as YAML and exported in CSV and JSON formats for integration into software products and services.
apis:
  - aid: boycott-israeli-consumer-goods-dataset:boycott-israeli-consumer-goods-dataset
    name: Boycott Israeli Consumer Goods Dataset
    tags:
      - Boycotts
      - Consumers
      - Datasets
      - Palestine
      - BDS
    humanURL: https://github.com/TechForPalestine/boycott-israeli-consumer-goods-dataset
    properties:
      - url: https://github.com/TechForPalestine/boycott-israeli-consumer-goods-dataset
        type: Documentation
      - url: https://raw.githubusercontent.com/TechForPalestine/boycott-israeli-consumer-goods-dataset/main/output/brands.json
        type: DataFeed
    description: Collating all consumer boycott and alternatives data into a single, golden-source, version-controlled repository consumable by software products and services. Data sourced from Who Profits Research Center, BDS Movement, and AFSC.
common:
  - type: Website
    url: https://github.com/TechForPalestine/boycott-israeli-consumer-goods-dataset
  - type: Organization
    url: https://techforpalestine.org
properties:
  - type: x-domain
    value: github.com/TechForPalestine
  - type: x-maintainer
    value: TechForPalestine
  - type: x-license
    value: Open Source
  - type: x-data-format
    value: YAML input, CSV and JSON output
  - type: x-repository-structure
    value: data/ (YAML source files), schemas/ (JSON Schema definitions in YAML), output/ (generated CSV and JSON), raw/ (source materials), .github/workflows/ (automation scripts)
  - type: x-validation
    value: Python validation script (scripts/validate_yaml.py) checks brands against JSON Schema
  - type: x-data-sources
    value: Who Profits Research Center, BDS Movement Boycott Guide, AFSC Profiteering Company List
  - type: x-related-datasets
    value: TechForPalestine boycott-israeli-tech-companies-dataset (SaaS products)
  - type: x-use-cases
    value: Consumer boycott apps, barcode scanner integrations, browser extensions, shopping comparison tools, advocacy platforms, open data research
  - type: x-topics
    value: BDS Movement, Palestine solidarity, consumer advocacy, ethical consumption
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'
---
