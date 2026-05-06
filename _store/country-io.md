---
aid: country-io
name: Country.io
x-type: company
description: 'Country.io is a small open data project that publishes a set of static JSON files mapping ISO 3166-1 alpha-2 country codes to common reference data: country names, capital cities, ISO 3166-1 alpha-3 codes, continent codes, international telephone dialing prefixes, and ISO 4217 currency codes. The files are commonly consumed as a lightweight country-data dataset for forms, country pickers, and analytics enrichment.'
url: https://raw.githubusercontent.com/api-evangelist/country-io/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
access: Public
position: Provider
tags:
  - Capitals
  - Continents
  - Countries
  - Currencies
  - Currency Codes
  - Dialing Codes
  - Geography
  - ISO 3166
  - JSON
  - Open Data
  - Phone Codes
  - Reference Data
created: '2025-02-21'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: country-io:country-io-data-api
    name: Country.io Data API
    description: 'Country.io exposes six static JSON files under https://country.io. Each file is a flat object keyed by ISO 3166-1 alpha-2 country code and maps to a single reference value: country name, capital city, continent code, ISO3 code, dialing prefix, or currency code. The endpoints are open and unauthenticated.'
    humanURL: https://country.io/data/
    baseURL: https://country.io
    properties:
      - type: Documentation
        url: https://country.io/data/
      - type: OpenAPI
        url: openapi/country-io-data-openapi.yml
      - type: Rules
        url: rules/country-io-data-rules.yml
      - type: Capabilities
        url: capabilities/country-io-data-capabilities.yml
    tags:
      - Capitals
      - Countries
      - Currencies
      - ISO 3166
      - Open Data
      - Phone Codes
      - Reference Data
common:
  - type: Website
    url: https://country.io/
  - type: Data
    url: https://country.io/data/
  - type: Countries
    url: https://country.io/countries/
  - type: Rankings
    url: https://country.io/rankings/
  - type: Contact
    url: https://country.io/contact/
  - type: Vocabulary
    url: vocabulary/country-io-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
