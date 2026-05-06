---
aid: united-airlines
url: https://raw.githubusercontent.com/api-evangelist/united-airlines/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-03'
name: United Airlines
description: United Airlines is a major American airline headquartered in Chicago, Illinois. It operates one of the largest route networks in the world with hubs in Chicago, Denver, Houston, Los Angeles, New York, San Francisco, and Washington, D.C. United provides NDC (New Distribution Capability) APIs for flight shopping, booking, and servicing, as well as corporate travel integration capabilities.
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Airlines
  - Travel
  - Flight Booking
  - NDC
  - Loyalty
  - Fortune 100
apis:
  - name: United Airlines NDC API
    description: United Airlines NDC (New Distribution Capability) API enables travel agencies, online booking tools, and corporate travel platforms to search, book, and service United flights with full access to continuous pricing, dynamic bundled fares, ancillary products, hold bookings, exchanges, refunds, cancellations, schedule change alerts, and ARC/BSP reporting. Supports 30+ bundle combinations.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://united.business/NDC-corporate
    baseURL: https://api.united.com/v1
    tags:
      - Airlines
      - Flight Booking
      - NDC
      - Travel
      - Shopping
      - Booking
      - Servicing
    properties:
      - type: Documentation
        url: https://united.business/NDC-corporate
      - type: NDC Capabilities
        url: https://united.business/NDC-capabilities
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/openapi/united-airlines-ndc-openapi.yml
    contact:
      - FN: United Airlines NDC Support
        email: ndcagency@united.com
  - name: United Airlines Flight Status API
    description: United Airlines Flight Status API providing real-time flight status including estimated and actual departure and arrival times, gate information, delays, and flight tracking for United-operated flights.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://api.developer.iata.org/united-airlines-united-airlines-default/api/flight-status2
    baseURL: https://api.united.com/v1
    tags:
      - Airlines
      - Flight Status
      - Real-Time
      - IATA
    properties:
      - type: Documentation
        url: https://api.developer.iata.org/united-airlines-united-airlines-default/api/flight-status2
common:
  - type: Website
    url: https://www.united.com
  - type: Developer Portal
    url: https://united.business/NDC-corporate
  - type: NDC Capabilities
    url: https://united.business/NDC-capabilities
  - type: Contact
    url: https://united.business/contact-form.html
  - type: IATA Developer Portal
    url: https://api.developer.iata.org/united-airlines-united-airlines-default/api/flight-status2
  - type: LinkedIn
    url: https://www.linkedin.com/company/united-airlines
  - type: X
    url: https://twitter.com/united
  - type: MileagePlus
    url: https://www.united.com/en/us/fly/mileageplus.html
  - type: OpenAPI
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/openapi/united-airlines-ndc-openapi.yml
  - type: SpectralRules
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/rules/united-airlines-rules.yml
  - type: NaftikoCapabilities
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/capabilities/flight-booking.yaml
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-booking-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-schema/united-airlines-flight-status-schema.json
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/json-ld/united-airlines-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/united-airlines/main/vocabulary/united-airlines-vocabulary.yml
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
---
