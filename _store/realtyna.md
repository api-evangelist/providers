---
aid: realtyna
name: Realtyna
description: Realtyna provides real estate technology including IDX, RESO Web API integrations, MLS data routing, and a WordPress-based property platform (WPL). Their API Plugin exposes the WPL platform via a RESTful, JSON-based HTTP interface for building custom front-ends and mobile applications. Realtyna also offers MLS API, Organic RESO API, and the MLS Router API for enterprise MLS integration.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Real Estate
  - MLS
  - IDX
  - RESO
  - WordPress
url: https://raw.githubusercontent.com/api-evangelist/realtyna/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: realtyna:wpl-api
    name: Realtyna WPL API Plugin
    description: The WPL API Plugin is a RESTful HTTP/JSON interface for the Realtyna WPL WordPress platform. It supports user account registration and management, authentication, retrieving active listing types, loading property data, filter parameters (property type, bedrooms, bathrooms, price, neighborhood), managing favorites, saved searches, password reset via SMS, and listing details.
    humanURL: https://realtyna.com/api
    tags:
      - WPL
      - Property Listings
      - WordPress
    properties:
      - type: Documentation
        url: https://realtyna.com/API_Documentation_V2.pdf
      - type: Pricing
        url: https://realtyna.com/api
  - aid: realtyna:mls-router-api
    name: Realtyna MLS Router API
    description: MLS Router API is an enterprise solution that aggregates and routes data across multiple MLS feeds, providing a single integration point for accessing normalized MLS listing data through a RESO-compliant interface.
    humanURL: https://realtyna.com/mls-router-api
    tags:
      - MLS
      - RESO
      - Enterprise
    properties:
      - type: Documentation
        url: https://realtyna.com/mls-router-api
  - aid: realtyna:organic-reso-api
    name: Realtyna Organic RESO API
    description: Organic RESO API provides standards-based access to real estate listing data using the RESO Web API specification, enabling developers to build applications consuming MLS data through a RESO-compliant interface.
    humanURL: https://realtyna.com/organic-mls-integration/
    tags:
      - MLS
      - RESO
    properties:
      - type: Documentation
        url: https://realtyna.com/organic-mls-integration/
common:
  - type: Website
    url: https://realtyna.com
  - type: Documentation
    url: https://realtyna.com/api
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
