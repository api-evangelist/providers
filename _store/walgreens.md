---
aid: walgreens
name: Walgreens
description: Walgreens is one of the largest pharmacy-led health and wellbeing companies in the United States, operating over 8,000 locations nationwide. The Walgreens Developer Program provides APIs enabling third-party applications to integrate pharmacy prescription management, vaccine scheduling, retail shopping, store locations, and product inventory. The APIs support seamless healthcare delivery, prescription refills, immunization appointments, and retail e-commerce integrations for mobile and web applications.
type: Index
position: Producer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Pharmacy
  - Healthcare
  - Retail
  - Prescriptions
  - Vaccines
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: walgreens:walgreens-store-locator
    name: Walgreens Store Locator API
    description: Returns dynamic store location data and service information for 8,000+ Walgreens and Duane Reade locations across the United States. Supports search by geolocation, address, or zip code with filtering by store services such as 24-hour pharmacy, drive-thru, healthcare clinic, photo lab, flu shots, and immunization services.
    humanURL: https://developer.walgreens.com/api/storelocator/rest
    baseURL: https://services.walgreens.com
    tags:
      - Store Locator
      - Retail
      - Pharmacy
      - Geolocation
    properties:
      - type: Documentation
        url: https://developer.walgreens.com/api/storelocator/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/openapi/walgreens-store-locator-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/json-schema/walgreens-store-schema.json
  - aid: walgreens:walgreens-prescription-refill
    name: Walgreens Prescription Refill API
    description: Enables medication management application developers to process prescription refills or transfers to any Walgreens pharmacy location. Supports both barcode scanning for refill initiation and image-based prescription transfers. Processes refills from 8,200+ Walgreens pharmacies with mobile-optimized WebView checkout flows.
    humanURL: https://developer.walgreens.com/api/rx/rest
    baseURL: https://services.walgreens.com
    tags:
      - Pharmacy
      - Prescriptions
      - Healthcare
      - Mobile
    properties:
      - type: Documentation
        url: https://developer.walgreens.com/api/rx/rest
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/openapi/walgreens-prescription-refill-openapi.yml
  - aid: walgreens:walgreens-vaccine-scheduling
    name: Walgreens Vaccine Scheduling API
    description: Allows developers to integrate vaccine and immunization appointment booking capabilities including eligibility checking, timeslot availability, appointment holds, patient registration, and booking confirmation across all Walgreens locations in the United States and Puerto Rico. Supports 19+ vaccine types including COVID-19, influenza, RSV, and travel immunizations.
    humanURL: https://developer.walgreens.com/api/scheduling/v1
    baseURL: https://services.walgreens.com
    tags:
      - Vaccines
      - Healthcare
      - Scheduling
      - Immunizations
    properties:
      - type: Documentation
        url: https://developer.walgreens.com/api/scheduling/v1
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/openapi/walgreens-vaccine-scheduling-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/walgreens/refs/heads/main/json-schema/walgreens-vaccine-appointment-schema.json
  - aid: walgreens:walgreens-photo-prints
    name: Walgreens Photo Prints API
    description: Enables developers to offer photo printing services at 8,000+ Walgreens and Duane Reade stores for same-day pickup. Supports native JSON API integration with potential revenue share commissions for qualifying partners. Prints can be ordered from mobile and web applications.
    humanURL: https://developer.walgreens.com/api/photoprints/native
    baseURL: https://services.walgreens.com
    tags:
      - Photo Printing
      - Retail
      - Mobile
    properties:
      - type: Documentation
        url: https://developer.walgreens.com/api/photoprints/native
common:
  - type: Website
    url: https://www.walgreens.com
  - type: Portal
    url: https://developer.walgreens.com
  - type: Documentation
    url: https://developer.walgreens.com/apis
  - type: Blog
    url: https://developer.walgreens.com/blog
  - type: SignUp
    url: https://developer.walgreens.com/user/register
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
