---
aid: sound-transit
name: Sound Transit
description: Sound Transit is a regional transit authority serving the Seattle-Puget Sound area of Washington State, operating light rail, commuter rail, and express bus services. The Sound Transit Open Transit Data (OTD) program provides GTFS static and real-time data feeds, OneBusAway API access, and GTFS-RT service alerts for transit application developers and researchers.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Transit
  - Transportation
  - GTFS
  - Real-Time
  - Public Transit
  - Government
  - Seattle
created: '2026-03-16'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/sound-transit/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: sound-transit:sound-transit-onebusaway-api
    name: Sound Transit OneBusAway API
    description: The Sound Transit OneBusAway API provides access to real-time and scheduled transit data for the Puget Sound region. Supports route information, stop locations, real-time arrivals and departures, vehicle positions, and trip details for 1 Line, 2 Line, T Line, and ST Express routes.
    humanURL: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
    baseURL: https://api.pugetsound.onebusaway.org/api/where
    tags:
      - Transit
      - GTFS
      - Real-Time
      - Routes
      - Stops
      - Vehicles
    properties:
      - type: Documentation
        url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
      - type: Reference
        url: http://developer.onebusaway.org/
      - type: GTFS Downloads
        url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/otd-downloads
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/sound-transit/refs/heads/main/openapi/sound-transit-onebusaway-openapi.yml
    contact:
      - FN: Sound Transit Open Transit Data
        url: https://www.soundtransit.org/
        email: open_transit_data@soundtransit.org
common:
  - type: Portal
    url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
  - type: Website
    url: https://www.soundtransit.org/
  - type: GTFS Static Feeds
    url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/otd-downloads
  - type: GTFS-RT Service Alerts (Protocol Buffers)
    url: https://s3.amazonaws.com/st-service-alerts-prod/alerts.pb
  - type: GTFS-RT Service Alerts (JSON)
    url: https://s3.amazonaws.com/st-service-alerts-prod/alerts_pb.json
  - type: Transitland Feed
    url: https://www.transit.land/feeds/f-c23-soundtransit
  - type: OneBusAway
    url: https://onebusaway.org/
  - type: Terms of Use
    url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd/transit-data-terms-use
  - type: API Key Request
    url: mailto:oba_api_key@soundtransit.org
  - type: Support
    url: mailto:open_transit_data@soundtransit.org
  - type: Trip Planner
    url: https://tripplanner.kingcounty.gov/
  - type: Real-Time Coverage
    url: https://www.soundtransit.org/help-contacts/business-information/open-transit-data-otd
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
