---
aid: lufthansa
name: Lufthansa
url: https://raw.githubusercontent.com/api-evangelist/lufthansa/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Contract
position: Consuming
access: 3rd-Party
tags:
  - Airlines
  - Travel
  - Aviation
  - Flights
created: '2024-07-02'
modified: '2026-04-28'
specificationVersion: '0.19'
description: The Lufthansa Group is a global aviation group that plays a leading role in its European home market. The Lufthansa Open API developer portal exposes reference data, flight operations, offers, notifications, and cargo APIs secured with OAuth2 for partner and public consumers.
apis:
  - aid: lufthansa:public-api
    name: Lufthansa Public API
    description: The Lufthansa Public API provides reference data for countries, cities, airports, airlines, and aircraft, plus flight schedules and real-time flight status by route, arrival airport, or departure airport, customer flight information, seat maps, and lounge data.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.lufthansa.com
    baseURL: https://api.lufthansa.com/v1
    tags:
      - Airlines
      - Flights
      - Reference Data
      - Flight Status
      - Seat Maps
      - Lounges
    properties:
      - type: Documentation
        url: https://developer.lufthansa.com/docs/read/api_details
      - type: Portal
        url: https://developer.lufthansa.com
      - type: Authentication
        url: https://developer.lufthansa.com/docs/read/Authentication
      - type: OpenAPI
        url: openapi/lufthansa-openapi.yml
  - aid: lufthansa:partner-api
    name: Lufthansa Partner API
    description: The Lufthansa Partner API exposes deeplinks, fares, pricing offers, and seat details for integration partners. NDC capabilities including Smart Offer, NDC Bonus, Servicing, and Technology are part of the partner program.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.lufthansa.com
    baseURL: https://api.lufthansa.com/v1
    tags:
      - Partner
      - NDC
      - Fares
      - Pricing
      - Offers
    properties:
      - type: Documentation
        url: https://developer.lufthansa.com/docs/read/api_details
      - type: Portal
        url: https://developer.lufthansa.com
  - aid: lufthansa:flightops-crew
    name: Lufthansa FlightOps and Crew API
    description: The FlightOps and Crew API provides crew-specific services including check-in times, duty events, and weather information for operational use cases.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.lufthansa.com
    baseURL: https://api.lufthansa.com/v1
    tags:
      - Crew
      - Flight Operations
      - Weather
    properties:
      - type: Documentation
        url: https://developer.lufthansa.com/docs/read/api_details
      - type: Portal
        url: https://developer.lufthansa.com
  - aid: lufthansa:cargo
    name: Lufthansa Cargo API
    description: The Lufthansa Cargo API provides shipment tracking and LH CARGO flight routings.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.lufthansa.com
    baseURL: https://api.lufthansa.com/v1
    tags:
      - Cargo
      - Shipment Tracking
      - Logistics
    properties:
      - type: Documentation
        url: https://developer.lufthansa.com/docs/read/api_details
      - type: Portal
        url: https://developer.lufthansa.com
  - aid: lufthansa:notifications
    name: Lufthansa Notifications API
    description: The Notifications API delivers FlightUpdate notifications and JWT-based authentication tokens for streaming flight events.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://developer.lufthansa.com
    baseURL: https://api.lufthansa.com/v1
    tags:
      - Notifications
      - JWT
      - Webhooks
      - Flight Updates
    properties:
      - type: Documentation
        url: https://developer.lufthansa.com/docs/read/api_details
      - type: Portal
        url: https://developer.lufthansa.com
common:
  - type: Website
    url: https://www.lufthansagroup.com
  - type: Portal
    url: https://developer.lufthansa.com
  - type: Documentation
    url: https://developer.lufthansa.com/docs/read/api_details
  - type: Authentication
    url: https://developer.lufthansa.com/docs/read/Authentication
  - type: SignUp
    url: https://developer.lufthansa.com/user/register
  - type: TermsOfService
    url: https://developer.lufthansa.com/docs/read/General_Terms_and_Conditions
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
