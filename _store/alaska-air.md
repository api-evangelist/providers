---
aid: alaska-air
url: https://raw.githubusercontent.com/api-evangelist/alaska-air/refs/heads/main/apis.yml
name: Alaska Airlines
tags:
  - Airlines
  - Aviation
  - Travel
  - Cargo
  - Loyalty
  - Flight Status
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
description: Alaska Air Group is the parent company of Alaska Airlines and Horizon Air, providing passenger and cargo air transportation throughout the United States, Mexico, Canada, Costa Rica, and Belize. Alaska Airlines offers a developer portal at developers.alaskaair.com for accessing flight status, schedules, and other APIs, and operates Alaska Air Cargo serving 115+ destinations worldwide with dedicated cargo aircraft.
created: '2024-01-01'
modified: '2026-04-19'
specificationVersion: '0.19'
apis:
  - aid: alaska-air:flight-status-api
    name: Alaska Airlines Flight Status API
    tags:
      - Flight Status
      - Aviation
      - Real-Time Data
    properties:
      - url: https://developers.alaskaair.com/
        type: Documentation
      - url: https://developers.alaskaair.com/
        type: APIReference
      - url: openapi/alaska-air-flight-status-openapi.yaml
        type: OpenAPI
    humanURL: https://developers.alaskaair.com/
    baseURL: https://api.alaskaair.com
    description: The Alaska Airlines Flight Status API provides real-time flight status, departure and arrival information, gate assignments, and delay details for Alaska Airlines (AS) and Horizon Air (QX) flights.
  - aid: alaska-air:flight-schedules-api
    name: Alaska Airlines Flight Schedules API
    tags:
      - Schedules
      - Aviation
      - Itinerary
    properties:
      - url: https://developers.alaskaair.com/
        type: Documentation
      - url: openapi/alaska-air-flight-schedules-openapi.yaml
        type: OpenAPI
    humanURL: https://developers.alaskaair.com/
    baseURL: https://api.alaskaair.com
    description: The Alaska Airlines Flight Schedules API provides access to flight schedule data including route information, operating days, departure and arrival times, and equipment information across the Alaska Airlines and Horizon Air networks.
  - aid: alaska-air:cargo-api
    name: Alaska Air Cargo API
    tags:
      - Cargo
      - Freight
      - Shipping
      - Tracking
    properties:
      - url: https://www.alaskacargo.com/
        type: Documentation
      - url: https://www.alaskacargo.com/
        type: Portal
      - url: openapi/alaska-air-cargo-openapi.yaml
        type: OpenAPI
    humanURL: https://www.alaskacargo.com/
    baseURL: https://api.alaskacargo.com
    description: Alaska Air Cargo APIs enable partners to book shipments, track cargo, get rate estimates, and access schedules across 115+ cargo destinations worldwide. Alaska Airlines operates the only U.S. passenger airline with dedicated cargo aircraft including Airbus A330s and Boeing 787s.
  - aid: alaska-air:mileage-plan-api
    name: Alaska Airlines Mileage Plan API
    tags:
      - Loyalty
      - Mileage Plan
      - Rewards
      - Partners
    properties:
      - url: https://www.alaskaair.com/content/mileage-plan
        type: Documentation
      - url: openapi/alaska-air-mileage-plan-openapi.yaml
        type: OpenAPI
    humanURL: https://www.alaskaair.com/content/mileage-plan
    baseURL: https://api.alaskaair.com
    description: The Alaska Mileage Plan partner API enables airline partners, hotel chains, car rental companies, and other loyalty partners to report and redeem miles for members. Alaska's Mileage Plan is consistently rated among the top frequent flyer programs.
common:
  - url: https://www.alaskaair.com
    type: Website
  - url: https://developers.alaskaair.com/
    type: Portal
  - url: https://www.alaskaair.com/content/about-us/news-and-events
    type: Blog
  - url: https://www.alaskaair.com/content/about-us/investor-relations
    type: Support
  - url: api.support@alaskaair.com
    type: Support
    title: API Support Email
  - url: https://www.alaskacargo.com/
    type: Documentation
    title: Alaska Air Cargo Portal
  - url: rules/alaska-air-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/alaska-air-vocabulary.yaml
    type: Vocabulary
  - url: json-ld/alaska-air-context.jsonld
    type: JSONLD
  - url: capabilities/shared/flight-status-api.yaml
    type: NaftikoCapability
    title: Flight Status API Shared Capability
  - url: capabilities/shared/cargo-api.yaml
    type: NaftikoCapability
    title: Cargo API Shared Capability
  - url: capabilities/travel-operations.yaml
    type: NaftikoCapability
    title: Travel Operations Workflow
  - type: Features
    data:
      - name: Real-Time Flight Status
        description: Track live flight status, departure and arrival times, gate assignments, and delay information for Alaska Airlines and Horizon Air flights.
      - name: Flight Schedules
        description: Access flight schedule data including routes, operating days, departure/arrival times, and equipment across the Alaska network.
      - name: Cargo Booking and Tracking
        description: Book shipments and track cargo across 115+ destinations worldwide via Alaska Air Cargo's network, including dedicated widebody aircraft.
      - name: Cargo Rate Estimates
        description: Get real-time rate estimates for cargo shipments based on origin, destination, weight, dimensions, and special handling requirements.
      - name: Mileage Plan Partner Integration
        description: Enable partner mile accrual and redemption for Alaska's Mileage Plan loyalty program across airline, hotel, car rental, and retail partners.
      - name: Dedicated Cargo Aircraft
        description: Alaska Air Cargo operates the only U.S. passenger airline with dedicated cargo aircraft (Airbus A330s and Boeing 787s) for increased capacity on key routes.
      - name: Specialized Cargo Services
        description: Support for dangerous goods transport, live animal shipments via Pet Connect, and international cargo across Asia, Pacific, Canada, and Mexico.
      - name: API Management via Azure
        description: Developer portal powered by Microsoft Azure API Management with subscription-based key management, interactive API console, and automatic API documentation generation.
  - type: UseCases
    data:
      - name: Travel Agent and OTA Integration
        description: Integrate Alaska Airlines flight schedules and status into online travel agencies and booking platforms for real-time availability and status updates.
      - name: Cargo Partner Booking
        description: Enable freight forwarders and cargo brokers to book shipments, get rate quotes, and track Alaska Air Cargo shipments programmatically.
      - name: Loyalty Partner Mile Reporting
        description: Integrate Mileage Plan mile accrual into partner platforms (hotels, car rentals, credit cards) to automatically report earned miles.
      - name: Airport Operations Display
        description: Power airport operations systems and display boards with real-time Alaska Airlines flight status and gate assignment data.
      - name: Corporate Travel Management
        description: Integrate Alaska Airlines flight data into corporate travel management systems for booking, tracking, and expense reporting.
      - name: Mobile App Integration
        description: Embed Alaska Airlines flight status and schedule data into third-party mobile applications for travelers.
  - type: Integrations
    data:
      - name: Microsoft Azure API Management
        description: Developer portal and API gateway powered by Azure API Management with subscription key management and interactive testing console.
      - name: Hawaiian Airlines
        description: Alaska Air Cargo partnerships including connections with Hawaiian Airlines cargo network for Pacific and inter-island routes.
      - name: One World Alliance
        description: Member of the oneworld airline alliance enabling Mileage Plan accrual and redemption across 13 member airlines.
      - name: Duffel
        description: Third-party travel API provider enabling search, booking, and ticket issuance for Alaska Airlines flights.
      - name: Five9
        description: Customer service platform integration for Alaska Air Cargo live chat and support operations.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
