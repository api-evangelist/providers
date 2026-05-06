---
aid: chicago-transit-authority
name: Chicago Transit Authority
x-type: government
description: The Chicago Transit Authority (CTA) is the public transit operator for the City of Chicago and 35 surrounding suburbs, operating the second largest public transit system in the United States with bus and rapid-transit (L) train services. The CTA Developer Center publishes open transit data feeds and APIs for developers building rider-facing applications, including the Train Tracker API for real-time L-train arrivals, the Bus Tracker API for real-time bus arrivals and vehicle locations, the Customer Alerts API for service status and disruptions, and GTFS schedule data feeds for the entire CTA bus and rail network.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/chicago-transit-authority/refs/heads/main/apis.yml
tags:
  - Bus
  - Bus Tracker
  - Chicago
  - CTA
  - Customer Alerts
  - GTFS
  - L Train
  - Open Data
  - Public Transit
  - Real-Time
  - Train
  - Train Tracker
  - Transit
  - Transportation
created: '2025-05-02'
modified: '2026-04-23'
specificationVersion: '0.20'
apis:
  - aid: chicago-transit-authority:train-tracker-api
    name: CTA Train Tracker API
    description: The Train Tracker API provides real-time train arrival predictions and run/location information for all CTA L train lines. Endpoints include arrival predictions by station or stop, follow-this-train run tracking, and a locations service exposing the current latitude/longitude of in-service trains. Authentication requires a developer API key issued through the CTA Developer Center.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.transitchicago.com/developers/traintracker/
    baseURL: http://lapi.transitchicago.com/api/1.0
    tags:
      - L Train
      - Real-Time
      - Train Tracker
      - Transit
    properties:
      - type: Documentation
        url: https://www.transitchicago.com/developers/traintracker/
      - type: APIDocs
        url: https://www.transitchicago.com/developers/ttdocs/
      - type: APIKeyApplication
        url: https://www.transitchicago.com/developers/traintrackerapply/
      - type: TermsOfUse
        url: https://www.transitchicago.com/developers/terms/
      - type: OpenAPI
        url: openapi/cta-train-tracker-openapi.yml
      - type: Spectral
        url: spectral/chicago-transit-authority-spectral.yml
  - aid: chicago-transit-authority:bus-tracker-api
    name: CTA Bus Tracker API
    description: The Bus Tracker API series provides real-time bus arrival predictions, vehicle locations, route patterns, route lists, and stop directories for the CTA bus network. Endpoints support route, stop, and vehicle-based queries returning JSON or XML. Authentication requires a developer API key issued through the CTA Developer Center.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.transitchicago.com/developers/bustracker/
    baseURL: http://www.ctabustracker.com/bustime/api/v2
    tags:
      - Bus
      - Bus Tracker
      - Real-Time
      - Transit
    properties:
      - type: Documentation
        url: https://www.transitchicago.com/developers/bustracker/
      - type: TermsOfUse
        url: https://www.transitchicago.com/developers/terms/
      - type: OpenAPI
        url: openapi/cta-bus-tracker-openapi.yml
  - aid: chicago-transit-authority:customer-alerts-api
    name: CTA Customer Alerts API
    description: The Customer Alerts API delivers real-time service status, planned outages, and disruption information for CTA bus and rail services. It provides both a route-level status feed and per-route or per-station detail. Authentication is not required for the public Customer Alerts feeds.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.transitchicago.com/developers/alerts/
    baseURL: http://www.transitchicago.com/api/1.0
    tags:
      - Customer Alerts
      - Real-Time
      - Service Status
      - Transit
    properties:
      - type: Documentation
        url: https://www.transitchicago.com/developers/alerts/
  - aid: chicago-transit-authority:gtfs-feed
    name: CTA GTFS Schedule Feed
    description: CTA publishes a GTFS (General Transit Feed Specification) schedule feed covering the physical layout, stop locations, and static schedules for the entire CTA bus and L train system. The feed is a downloadable ZIP archive that conforms to the GTFS reference and is updated when CTA service changes.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.transitchicago.com/developers/gtfs/
    baseURL: https://www.transitchicago.com/downloads/sch_data/google_transit.zip
    tags:
      - GTFS
      - Schedule
      - Static
      - Transit
    properties:
      - type: Documentation
        url: https://www.transitchicago.com/developers/gtfs/
      - type: Feed
        url: https://www.transitchicago.com/downloads/sch_data/google_transit.zip
      - type: DataGov
        url: https://catalog.data.gov/dataset/cta-system-information-developer-tool-gtfs-data
      - type: Transitland
        url: https://www.transit.land/feeds/f-dp3-cta
      - type: ChicagoDataPortal
        url: https://data.cityofchicago.org/Transportation/CTA-System-Information-Developer-Tool-GTFS-Data/sp6w-yusg
common:
  - type: Website
    url: https://www.transitchicago.com/
  - type: Portal
    name: CTA Developer Center
    url: https://www.transitchicago.com/developers/
  - type: TermsOfUse
    url: https://www.transitchicago.com/developers/terms/
  - type: PrivacyPolicy
    url: https://www.transitchicago.com/privacy/
  - type: APIKeyApplication
    url: https://www.transitchicago.com/developers/traintrackerapply/
  - type: ChicagoDataPortal
    url: https://data.cityofchicago.org
  - type: SystemMap
    url: https://www.transitchicago.com/maps/
  - type: Newsroom
    url: https://www.transitchicago.com/news/
  - type: ContactUs
    url: https://www.transitchicago.com/contactus/
  - type: JSONLD
    url: json-ld/chicago-transit-authority-context.jsonld
  - type: NaftikoCapabilities
    url: naftiko/chicago-transit-authority-capabilities.yml
  - type: Spectral
    url: spectral/chicago-transit-authority-spectral.yml
  - name: Features
    type: Features
    data:
      - name: Real-Time Train Arrivals
      - name: Real-Time Bus Arrivals
      - name: Train Run Locations
      - name: Bus Vehicle Locations
      - name: Route and Stop Directories
      - name: Customer Alerts and Service Status
      - name: Planned Outage Notifications
      - name: GTFS Static Schedule Feed
      - name: API Key Issuance
      - name: Open Chicago Transit Data
  - name: UseCases
    type: UseCases
    data:
      - name: Rider-Facing Mobile Apps
      - name: Trip Planners and Routing
      - name: Real-Time Arrival Displays
      - name: Service Disruption Notifications
      - name: Schedule Visualizations
      - name: Accessibility Tooling
      - name: Smart City Dashboards
      - name: Multimodal Transit Apps
      - name: Research and Open Data Analysis
  - name: Standards
    type: Standards
    data:
      - name: GTFS
      - name: GTFS-Realtime (consumed via partners)
      - name: REST
      - name: JSON
      - name: XML
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
