---
aid: realestateapi
name: RealEstateAPI
description: RealEstateAPI.com offers expressive property data APIs designed for building prop-tech applications. The platform exposes nationwide US property records including ownership, valuations, MLS listings, comparables, parcel boundary data, skip tracing, and involuntary liens through a unified JSON REST API.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Real Estate
  - Property Data
  - MLS
  - Valuation
  - Geospatial
  - Skip Tracing
  - Prop-Tech
url: https://raw.githubusercontent.com/api-evangelist/realestateapi/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: realestateapi:realestateapi
    name: RealEstateAPI
    description: A unified property data API offering property search, detail records, comparables, automated valuations (AVM), parcel boundaries, MLS data, skip tracing, and involuntary lien records. Authenticates with an x-api-key header. The Property Search endpoint supports list building, counts, and rich filtering across location, property characteristics, financial criteria, and special-status flags such as pre-foreclosure, foreclosure, REO, auction, tax delinquent, cash buyer, and investor owned.
    humanURL: https://www.realestateapi.com/
    baseURL: https://api.realestateapi.com
    tags:
      - Real Estate
      - Property Data
      - MLS
      - Valuation
    properties:
      - type: Documentation
        url: https://developer.realestateapi.com/reference/getting-started
      - type: PropertySearch
        url: https://developer.realestateapi.com/reference/property-search-api
      - type: SignUp
        url: https://app.realestateapi.com/signup
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/realestateapi/refs/heads/main/openapi/realestateapi-openapi.yml
common:
  - type: Portal
    url: https://www.realestateapi.com/
  - type: Documentation
    url: https://developer.realestateapi.com/
  - type: Pricing
    url: https://www.realestateapi.com/pricing/
  - type: SignUp
    url: https://app.realestateapi.com/signup
  - type: Login
    url: https://app.realestateapi.com/login
  - type: Blog
    url: https://www.realestateapi.com/blog/
  - type: Contact
    url: https://www.realestateapi.com/contact/
  - type: TermsOfService
    url: https://www.realestateapi.com/terms-of-service/
  - type: PrivacyPolicy
    url: https://www.realestateapi.com/privacy-policy/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
