---
aid: aerodatabox
url: https://raw.githubusercontent.com/api-evangelist/aerodatabox/refs/heads/main/apis.yml
name: AeroDataBox
tags:
  - Aviation
  - Flights
  - Aerospace
  - Flight Data
  - Airport Data
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2025-02-24'
modified: '2026-04-19'
description: AeroDataBox is an affordable aviation and flight data API platform tailored for small and medium businesses, individual developers, researchers, and students. Founded in 2019, the platform provides real-time and historical flight status, aircraft information, airport data, delay statistics, and flight alert webhooks through a RESTful API available on RapidAPI and API.Market. AeroDataBox covers global aviation data across airlines, aircraft, airports, and flight operations.
specificationVersion: '0.16'
maintainers:
  - FN: API Evangelist
    url: http://apievangelist.com
    email: info@apievangelist.com
apis:
  - aid: aerodatabox:aerodatabox-flight-api
    name: AeroDataBox Flight API
    tags:
      - Flights
      - Flight Status
      - FIDS
      - Real-Time
      - Aviation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://prod.api.market/api/v1/aedbx/aerodatabox
    humanURL: https://doc.aerodatabox.com/
    description: Provides real-time and historical flight status information including departure and arrival times, delays, codeshares, and flight number lookups. Supports FIDS (Flight Information Display System) data for airports and individual flight tracking by flight number, IATA/ICAO codes, and date ranges.
    properties:
      - url: https://doc.aerodatabox.com/
        type: Documentation
      - url: openapi/aerodatabox-openapi.yml
        type: OpenAPI
  - aid: aerodatabox:aerodatabox-aircraft-api
    name: AeroDataBox Aircraft API
    tags:
      - Aircraft
      - Tail Numbers
      - Fleet
      - Airlines
      - Aviation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://prod.api.market/api/v1/aedbx/aerodatabox
    humanURL: https://doc.aerodatabox.com/
    description: Search and retrieve aircraft information by tail number, registration, or ICAO24 hex code. Includes airline fleet lookups, aircraft registration history, and aircraft images. Supports searches by term for active aircraft registrations.
    properties:
      - url: https://doc.aerodatabox.com/
        type: Documentation
      - url: openapi/aerodatabox-openapi.yml
        type: OpenAPI
  - aid: aerodatabox:aerodatabox-airport-api
    name: AeroDataBox Airport API
    tags:
      - Airports
      - Runways
      - Location Search
      - Aviation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://prod.api.market/api/v1/aedbx/aerodatabox
    humanURL: https://doc.aerodatabox.com/
    description: Retrieve airport information by IATA/ICAO code including runway data, local time, solar time, and distance calculations between airports. Search airports by geographic location, IP address geolocation, or free-text term.
    properties:
      - url: https://doc.aerodatabox.com/
        type: Documentation
      - url: openapi/aerodatabox-openapi.yml
        type: OpenAPI
  - aid: aerodatabox:aerodatabox-statistical-api
    name: AeroDataBox Statistical API
    tags:
      - Delays
      - Statistics
      - Routes
      - Historical Data
      - Aviation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://prod.api.market/api/v1/aedbx/aerodatabox
    humanURL: https://doc.aerodatabox.com/
    description: Access current and historical airport delay statistics, global delay summaries, daily route statistics, and flight delay data by flight number. Supports date range queries for trend analysis and performance benchmarking.
    properties:
      - url: https://doc.aerodatabox.com/
        type: Documentation
      - url: openapi/aerodatabox-openapi.yml
        type: OpenAPI
  - aid: aerodatabox:aerodatabox-flight-alert-api
    name: AeroDataBox Flight Alert API
    tags:
      - Webhooks
      - Alerts
      - Subscriptions
      - Real-Time
      - Aviation
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://prod.api.market/api/v1/aedbx/aerodatabox
    humanURL: https://doc.aerodatabox.com/
    description: Create, manage, and monitor webhook subscriptions for real-time flight status alerts. Subscribe to flight events by flight number or airport and receive push notifications to your endpoint when flight status changes occur.
    properties:
      - url: https://doc.aerodatabox.com/
        type: Documentation
      - url: openapi/aerodatabox-openapi.yml
        type: OpenAPI
common:
  - url: https://doc.aerodatabox.com/
    type: Documentation
  - url: https://www.aerodatabox.com/
    type: Portal
  - url: https://rapidapi.com/aerodatabox/api/aerodatabox
    type: Marketplace
    title: RapidAPI
  - url: https://api.market/store/aedbx/aerodatabox
    type: Marketplace
    title: API.Market
  - url: https://www.aerodatabox.com/pricing
    type: Pricing
  - url: https://www.aerodatabox.com/terms-of-service
    type: TermsOfService
  - url: https://www.aerodatabox.com/privacy-policy
    type: PrivacyPolicy
  - url: https://www.aerodatabox.com/contact
    type: Contact
  - type: Features
    data:
      - name: Real-Time Flight Status
        description: Live flight tracking with departure and arrival times, current status, and delay information for flights worldwide.
      - name: FIDS Airport Departures and Arrivals
        description: Flight Information Display System data showing all departures and arrivals at any airport for a given time window.
      - name: Aircraft Search and Profiles
        description: Lookup aircraft by tail number, registration, or ICAO24 hex code with fleet data, registration history, and images.
      - name: Airport Search by Location
        description: Find airports by geographic coordinates, IP address geolocation, or free-text search with runway data included.
      - name: Flight Delay Statistics
        description: Current and historical delay data for airports and specific flight numbers enabling trend analysis and SLA monitoring.
      - name: Webhook Flight Alerts
        description: Push notification subscriptions for real-time flight status changes, supporting event-driven application architectures.
      - name: FAA LADD Status
        description: FAA Limiting Aircraft Data Displayed (LADD) status lookup to determine if an aircraft is opted out of public tracking.
      - name: Solar Time Calculations
        description: Sunrise, sunset, and solar position data for any airport and date, useful for scheduling and operations planning.
      - name: Route Statistics
        description: Daily route statistics for airports showing which routes operate and their frequency.
  - type: UseCases
    data:
      - name: Flight Tracking Applications
        description: Build consumer or enterprise flight tracking apps using real-time status data for specific flights or all flights at an airport.
      - name: Travel Booking Notifications
        description: Send flight status alerts to travelers by integrating webhook subscriptions for departure and arrival updates.
      - name: Airport Operations Intelligence
        description: Monitor airport performance, delay patterns, and route activity for operations research and capacity planning.
      - name: Airline Research and Analysis
        description: Analyze fleet composition, route networks, and on-time performance for competitive intelligence and market research.
      - name: Aviation Data Journalism
        description: Access historical delay and route statistics for data-driven journalism and research on aviation trends.
      - name: Aircraft Valuation and Tracking
        description: Track aircraft registrations and history for aviation finance, insurance, and asset management applications.
      - name: Trip Planning Tools
        description: Integrate airport search, local time, and solar data into travel planning applications to enhance itinerary building.
  - url: rules/aerodatabox-spectral-rules.yml
    type: SpectralRules
  - url: vocabulary/aerodatabox-vocabulary.yaml
    type: Vocabulary
  - url: capabilities/flight-tracking.yaml
    type: NaftikoCapability
    title: Flight Tracking
  - url: json-ld/aerodatabox-context.jsonld
    type: JSON-LD
  - type: Integrations
    data:
      - name: RapidAPI
        description: Available on RapidAPI Hub with interactive API playground and usage metering for easy developer onboarding.
      - name: API.Market
        description: Available on API.Market marketplace with official OpenAPI v3 specifications for download and code generation.
      - name: Webhook Endpoints
        description: Integrates with any webhook-capable endpoint for real-time flight status push notifications.
---
