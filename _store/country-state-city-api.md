---
aid: country-state-city-api
name: Country State City API
x-type: company
description: The Country State City API is a global geographic reference dataset and REST API published by countrystatecity.in. It exposes 247+ countries, 5,000+ states / provinces, and 150,000+ cities with ISO 3166 codes, phone codes, capitals, currencies, native names, regions, sub-regions, coordinates, time zones, and flag emoji. The data is also distributed as downloadable JSON, SQL, PostgreSQL, SQLite, XML, YAML, and CSV bundles for offline use, and the live API is authenticated with the X-CSCAPI-KEY header from a free developer plan.
url: https://raw.githubusercontent.com/api-evangelist/country-state-city-api/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/country-state-city-api.png
type: Index
access: Public
position: Provider
tags:
  - Capitals
  - Cities
  - Countries
  - Currencies
  - Geography
  - Geolocation
  - ISO 3166
  - JSON
  - Phone Codes
  - Provinces
  - Reference Data
  - Regions
  - States
  - Time Zones
created: '2024-03-30'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: country-state-city-api:country-state-city-api
    name: Country State City API
    description: REST API exposing world countries, states, regions, provinces, and cities with ISO2 / ISO3 codes, country code, phone code, capital, native language, time zones, latitude, longitude, region, subregion, flag emoji, and currency. Authentication is via the X-CSCAPI-KEY header.
    humanURL: https://docs.countrystatecity.in/
    baseURL: https://api.countrystatecity.in/v1
    properties:
      - type: Documentation
        url: https://docs.countrystatecity.in/
      - type: APIIntroduction
        url: https://docs.countrystatecity.in/api/introduction
      - type: SignUp
        url: https://app.countrystatecity.in/
      - type: OpenAPI
        url: openapi/country-state-city-api-openapi.yml
      - type: Rules
        url: rules/country-state-city-api-rules.yml
      - type: Capabilities
        url: capabilities/country-state-city-api-capabilities.yml
    tags:
      - Cities
      - Countries
      - ISO 3166
      - REST
      - States
common:
  - type: Website
    url: https://countrystatecity.in/
  - type: Documentation
    url: https://docs.countrystatecity.in/
  - type: APIIntroduction
    url: https://docs.countrystatecity.in/api/introduction
  - type: Console
    url: https://app.countrystatecity.in/
  - type: Pricing
    url: https://countrystatecity.in/pricing/
  - type: Downloads
    url: https://countrystatecity.in/downloads/
  - type: GitHubRepository
    url: https://github.com/dr5hn/countries-states-cities-database
  - type: Contact
    url: https://countrystatecity.in/contact/
  - type: PrivacyPolicy
    url: https://countrystatecity.in/privacy-policy/
  - type: TermsOfService
    url: https://countrystatecity.in/terms/
  - type: Vocabulary
    url: vocabulary/country-state-city-api-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
