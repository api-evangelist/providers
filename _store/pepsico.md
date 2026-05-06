---
aid: pepsico
name: PepsiCo
description: PepsiCo is one of the world's largest food and beverage companies, with a portfolio of brands including Pepsi-Cola, Mountain Dew, Frito-Lay, Quaker, Tropicana, and Gatorade.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Beverages
  - Food
  - Retail
  - Supply Chain
url: https://raw.githubusercontent.com/api-evangelist/pepsico/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: pepsico:pepsico-api
    name: PepsiCo API
    tags:
      - Beverages
      - Food
      - Retail
      - Supply Chain
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.pepsico.com
    humanURL: https://www.pepsico.com/our-stories/digital-innovation
    properties:
      - url: https://www.pepsico.com/our-stories/digital-innovation
        type: Documentation
      - url: openapi/pepsico-pepsico-api-openapi.yml
        type: OpenAPI
    description: PepsiCo provides partner APIs for supply chain integration, product data, and retail analytics. These APIs support distribution partners and retail customers in managing PepsiCo product operations.
common:
  - type: Website
    url: https://www.pepsico.com
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
