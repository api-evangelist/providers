---
aid: airbnb
url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/apis.yml
apis:
- aid: airbnb:homes-api
  name: Airbnb Homes API
  tags:
  - Listings
  - Lodging
  - Property Management
  - Reservations
  - Travel
  - Vacation Rentals
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.airbnb.com
  humanURL: https://developer.withairbnb.com/
  properties:
  - url: https://developer.withairbnb.com/
    type: Documentation
  - type: OpenAPI
    url: openapi/airbnb-homes-api-openapi.yml
  description: The Airbnb Homes API provides partner developers with programmatic access to manage vacation rental listings on the Airbnb platform. It supports creating and updating property listings, managing descriptions, amenities, photos, pricing, and availability rules. The API also enables reservation management, calendar synchronization, guest messaging, and review handling.
- aid: airbnb:activities-api
  name: Airbnb Activities API
  tags:
  - Activities
  - Bookings
  - Experiences
  - Tourism
  - Travel
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.airbnb.com
  humanURL: https://developer.withairbnb.com/
  properties:
  - url: https://developer.withairbnb.com/
    type: Documentation
  - type: OpenAPI
    url: openapi/airbnb-activities-api-openapi.yml
  description: The Airbnb Activities API allows approved partners to integrate with Airbnb Experiences, the platform's marketplace for hosted activities and tours. It provides endpoints for managing experience listings, handling bookings, and synchronizing availability for activities offered by local hosts.
- aid: airbnb:webhooks-api
  name: Airbnb Webhooks API
  tags:
  - Events
  - Notifications
  - Real-Time
  - Reservations
  - Webhooks
  image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
  baseURL: https://api.airbnb.com
  humanURL: https://developer.withairbnb.com/
  properties:
  - url: https://developer.withairbnb.com/
    type: Documentation
  - type: AsyncAPI
    url: asyncapi/airbnb-webhooks-asyncapi.yml
  description: The Airbnb Webhooks API enables connectivity partners to receive real-time notifications when events occur on the Airbnb platform. It supports webhook subscriptions for reservation changes, message creation, review submissions, listing calendar updates, and other key events.
name: Airbnb
tags:
- API
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Airbnb's developer documentation offers everything you need to know to seamlessly integrate your applications with our Homes and Activities APIs, empowering you to manage listings, bookings, reviews and messages, and enhance user experiences for Hosts.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

