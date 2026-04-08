---
aid: basetrip
url: https://raw.githubusercontent.com/api-search/basetrip/refs/heads/main/apis.yml
apis:
- aid: basetrip:basetrip-countries-api
  name: Basetrip Countries API
  tags:
  - Countries
  - Travel
  humanURL: https://www.thebasetrip.com/en/documentation/v3/countries
  properties:
  - url: ' https://www.thebasetrip.com/en/documentation/v3/countries'
    type: Documentation
  description: Get all the countries' names, slugs and codes. Use slug or alpha-2 code for a country's details endpoint as a {id} path parameter.
- aid: basetrip:basetrip-cities-api
  name: Basetrip Cities API
  tags:
  - Cities
  - Travel
  humanURL: https://www.thebasetrip.com/en/documentation/v3/cities
  properties:
  - url: https://www.thebasetrip.com/en/documentation/v3/cities
    type: Documentation
  description: Get all the cities from particular country, including their names and slugs. Use a slug or alpha-2 code for a {id} path parameter.
- aid: basetrip:basetrip-phrases-api
  name: Basetrip Phrases API
  tags:
  - Language
  - Phrases
  - Travel
  humanURL: https://www.thebasetrip.com/en/documentation/v3/phrases
  properties:
  - url: ' https://www.thebasetrip.com/en/documentation/v3/phrases'
    type: Documentation
  description: Get all language (travel) phrases for specific languages. Currently supported languages are English, French, German, Italian and Spanish.
name: Basetrip
tags:
- Travel
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-13'
modified: '2026-04-07'
position: Consuming
description: The Basetrip enables you to differentiate your travel products and improve conversion, brand awareness, and customer satisfaction.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

