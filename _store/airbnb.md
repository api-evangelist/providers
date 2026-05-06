---
aid: airbnb
url: https://raw.githubusercontent.com/api-evangelist/airbnb/refs/heads/main/apis.yml
apis:
  - aid: airbnb:homes-api
    name: Airbnb Homes API
    tags:
      - Airbnb
      - Calendar
      - Channel Manager
      - Hospitality
      - Host
      - Listings
      - Lodging
      - Photos
      - Property Management
      - Reservations
      - Short-Term Rental
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
    features:
      - Listing creation and management with full property details
      - Photo upload and management for listings
      - Calendar and availability management
      - Dynamic pricing and availability rules
      - Reservation management (accept, decline, modify)
      - Guest messaging within reservation threads
      - Review retrieval and response
      - Multi-unit and room-type support
    use_cases:
      - Property management systems syncing Airbnb listings
      - Channel managers distributing inventory across platforms
      - Vacation rental software managing guest communications
      - Revenue management tools adjusting pricing dynamically
  - aid: airbnb:activities-api
    name: Airbnb Activities API
    tags:
      - Activities
      - Airbnb
      - Bookings
      - Experiences
      - Hospitality
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
    features:
      - Experience listing creation and management
      - Activity scheduling and availability management
      - Booking management for hosted experiences
      - Guest communication for experience bookings
      - Photo management for experience listings
      - Host profile and capacity management
    use_cases:
      - Tour operators managing Airbnb Experiences listings
      - Activity booking platforms syncing availability
      - Experience management software integrating with Airbnb
  - aid: airbnb:webhooks-api
    name: Airbnb Webhooks API
    tags:
      - Airbnb
      - Events
      - Hospitality
      - Notifications
      - Real-Time
      - Reservations
      - Travel
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
    features:
      - Real-time reservation status change notifications
      - Guest message event notifications
      - Review submission notifications
      - Calendar update event notifications
      - Listing status change notifications
    use_cases:
      - Property management systems reacting to booking events in real time
      - Guest communication automation triggered by reservation changes
      - Inventory sync systems responding to availability changes
common:
  - type: Website
    url: https://www.airbnb.com/
  - type: Portal
    url: https://developer.withairbnb.com/
  - type: JSON-LD
    url: json-ld/airbnb-context.jsonld
  - type: JSONSchema
    url: json-schema/airbnb-listing-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-reservation-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-webhook-event-schema.json
  - type: Blog
    url: https://www.airbnb.com/resources/hosting-homes/a/airbnb-newsroom
  - type: GitHub
    url: https://github.com/airbnb
  - type: LinkedIn
    url: https://www.linkedin.com/company/airbnb
  - type: Twitter
    url: https://twitter.com/airbnb
  - type: TermsOfService
    url: https://www.airbnb.com/terms
  - type: PrivacyPolicy
    url: https://www.airbnb.com/privacy
  - type: Status
    url: https://airbnb.statuspage.io/
  - type: JSONSchema
    url: json-schema/airbnb-address-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-booking-guest-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-booking-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-calendar-day-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-calendar-operation-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-create-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-host-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-location-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-message-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-photo-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-pricing-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-experience-update-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-guest-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-listing-create-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-listing-update-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-message-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-photo-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-pricing-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-review-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-schedule-create-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-schedule-schema.json
  - type: JSONSchema
    url: json-schema/airbnb-schedule-update-schema.json
  - type: JSONStructure
    url: json-structure/airbnb-address-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-booking-guest-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-booking-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-calendar-day-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-calendar-operation-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-create-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-host-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-location-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-message-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-photo-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-pricing-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-experience-update-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-guest-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-listing-create-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-listing-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-listing-update-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-message-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-photo-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-pricing-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-reservation-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-review-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-schedule-create-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-schedule-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-schedule-update-structure.json
  - type: JSONStructure
    url: json-structure/airbnb-webhook-event-structure.json
  - type: Example
    url: examples/airbnb-address-example.json
  - type: Example
    url: examples/airbnb-booking-example.json
  - type: Example
    url: examples/airbnb-booking-guest-example.json
  - type: Example
    url: examples/airbnb-calendar-day-example.json
  - type: Example
    url: examples/airbnb-calendar-operation-example.json
  - type: Example
    url: examples/airbnb-experience-create-example.json
  - type: Example
    url: examples/airbnb-experience-example.json
  - type: Example
    url: examples/airbnb-experience-host-example.json
  - type: Example
    url: examples/airbnb-experience-location-example.json
  - type: Example
    url: examples/airbnb-experience-message-example.json
  - type: Example
    url: examples/airbnb-experience-photo-example.json
  - type: Example
    url: examples/airbnb-experience-pricing-example.json
  - type: Example
    url: examples/airbnb-experience-update-example.json
  - type: Example
    url: examples/airbnb-guest-example.json
  - type: Example
    url: examples/airbnb-listing-create-example.json
  - type: Example
    url: examples/airbnb-listing-example.json
  - type: Example
    url: examples/airbnb-listing-update-example.json
  - type: Example
    url: examples/airbnb-message-example.json
  - type: Example
    url: examples/airbnb-photo-example.json
  - type: Example
    url: examples/airbnb-pricing-example.json
  - type: Example
    url: examples/airbnb-reservation-example.json
  - type: Example
    url: examples/airbnb-review-example.json
  - type: Example
    url: examples/airbnb-schedule-create-example.json
  - type: Example
    url: examples/airbnb-schedule-example.json
  - type: Example
    url: examples/airbnb-schedule-update-example.json
  - type: Example
    url: examples/airbnb-webhook-event-example.json
  - type: SpectralRules
    url: rules/airbnb-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/shared/airbnb-api.yaml
  - type: NaftikoCapability
    url: capabilities/airbnb-listing-management.yaml
  - type: Vocabulary
    url: vocabulary/airbnb-vocabulary.yaml
modified: '2026-04-19'
description: Airbnb is the world's leading home-sharing and short-term rental marketplace, connecting hosts who offer accommodations and experiences with guests worldwide. The Airbnb developer platform provides connectivity partners — property management systems, channel managers, and experience operators — with APIs to manage listings, reservations, calendars, messaging, reviews, and webhook-based event notifications. Access is restricted to approved partners.
---
