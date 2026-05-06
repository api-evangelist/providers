---
aid: bookingcom
name: Booking.com
description: Booking.com is the world's leading online travel platform for accommodations, offering over 28 million listings including hotels, apartments, villas, homes, and unique places to stay. Part of Booking Holdings, Booking.com provides APIs for affiliate partners and connectivity partners to integrate its extensive travel inventory into third-party applications and property management systems.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/bookingcom/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Accommodations
  - Affiliates
  - Connectivity
  - Hospitality
  - Hotels
  - Reservations
  - Travel
apis:
  - aid: bookingcom:booking-api
    name: Booking.com API
    tags:
      - Hospitality
      - Hotels
      - Reservations
      - Travel
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.booking.com
    humanURL: https://developers.booking.com/
    properties:
      - url: https://developers.booking.com/
        type: Documentation
      - url: openapi/bookingcom-booking-api-openapi.yml
        type: OpenAPI
    description: Booking.com provides APIs for hotel search, availability, rates, reservations, and property management. The Connectivity APIs enable partners to distribute and manage accommodation inventory.
common:
  - type: Website
    url: https://www.booking.com
  - type: DeveloperPortal
    url: https://developers.booking.com/
  - type: Documentation
    url: https://developers.booking.com/demand/docs/getting-started/overview
  - type: AffiliateProgram
    url: https://www.booking.com/affiliate-program/v2/
  - type: ConnectivityPartners
    url: https://developers.booking.com/connectivity/docs
  - type: About
    url: https://www.booking.com/content/about.html
  - type: PrivacyPolicy
    url: https://www.booking.com/content/privacy.html
  - type: TermsOfService
    url: https://www.booking.com/content/terms.html
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
