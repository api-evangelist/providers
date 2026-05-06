---
aid: pg-and-e
url: https://raw.githubusercontent.com/api-evangelist/pg-and-e/refs/heads/main/apis.yml
modified: '2026-04-28'
apis:
  - aid: pg-and-e:share-my-data-api
    name: PG&E Share My Data API
    tags:
      - Energy
      - Utilities
      - Smart Meters
      - Green Button
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.pge.com
    humanURL: https://www.pge.com/en/save-energy-and-money/energy-usage-and-tips/understand-my-usage/share-my-data.html
    properties:
      - url: https://www.pge.com/en/save-energy-and-money/energy-usage-and-tips/understand-my-usage/share-my-data.html
        type: Documentation
      - url: openapi/pg-and-e-share-my-data-api-openapi.yml
        type: OpenAPI
    description: The PG&E Share My Data API provides customer-authorized access to energy usage data following the Energy Service Provider Interface (ESPI) standard and Green Button Connect My Data specification. Third-party companies can access interval data for both electricity and gas usage through RESTful web services with OAuth 2.0 authorization.
common:
  - type: Share My Data
    url: https://www.pge.com/en/save-energy-and-money/energy-usage-and-tips/understand-my-usage/share-my-data.html
  - type: Website
    url: https://www.pge.com/
description: Pacific Gas and Electric Company (PG&E) is one of the largest combined natural gas and electric energy companies in the United States, serving approximately 16 million people in northern and central California. PG&E offers the Share My Data API, a Green Button Connect My Data implementation providing customer- authorized access to energy usage interval data for both electricity and gas through RESTful web services.
---
