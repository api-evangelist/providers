---
aid: oecd
name: OECD
description: The OECD provides programmatic access to OECD data through an application programming interface (API) based on the SDMX standard. These APIs are free of charge and are offered subject to your acceptance of OECD Terms and Conditions.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Data
  - Statistics
  - Economics
  - SDMX
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/oecd/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: oecd:oecd
    name: OECD Data API
    description: The OECD provides programmatic access to OECD data through an application programming interface (API) based on the SDMX standard. These APIs are free of charge and are offered subject to your acceptance of OECD Terms and Conditions.
    humanURL: https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html
    baseURL: https://sdmx.oecd.org/public/rest
    tags:
      - Data
      - Statistics
      - SDMX
    properties:
      - type: Documentation
        url: https://www.oecd.org/en/data/insights/data-explainers/2024/09/api.html
      - type: Developer
        url: https://data-explorer.oecd.org/
common:
  - type: Website
    url: https://www.oecd.org/
  - type: Terms of Service
    url: https://www.oecd.org/termsandconditions/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
