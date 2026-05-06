---
aid: maryland-transit-administration
name: Maryland Transit Administration
description: The Maryland Transit Administration (MDOT MTA) supports open transit data initiatives and makes resources available to developers and applications. It primarily uses the General Transit Feed Specification (GTFS) and GTFS-RT to convey schedule, geographic, fare, vehicle position, and trip update data for Local Bus, Light Rail, Metro Subway, MARC Train, and Commuter Bus services in a standardized format.
type: Index
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Government
  - GTFS
  - GTFS-RT
  - Public Transportation
  - Transit
  - Bus
  - Rail
  - Subway
url: https://raw.githubusercontent.com/api-evangelist/maryland-transit-administration/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: maryland-transit-administration:mta-local-bus-gtfs
    name: MDOT MTA Local Bus GTFS
    description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Local Bus service. Includes GTFS-Fares V2 fare data.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/gtfs/local-bus
    tags:
      - GTFS
      - Bus
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS
        url: https://feeds.mta.maryland.gov/gtfs/local-bus
  - aid: maryland-transit-administration:mta-light-rail-gtfs
    name: MDOT MTA Light Rail GTFS
    description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Light Rail service. Includes GTFS-Fares V2 fare data.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/gtfs/light-rail
    tags:
      - GTFS
      - Light Rail
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS
        url: https://feeds.mta.maryland.gov/gtfs/light-rail
  - aid: maryland-transit-administration:mta-metro-subway-gtfs
    name: MDOT MTA Metro Subway GTFS
    description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Metro Subway service. Includes GTFS-Fares V2 fare data.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/gtfs/metro
    tags:
      - GTFS
      - Subway
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS
        url: https://feeds.mta.maryland.gov/gtfs/metro
  - aid: maryland-transit-administration:mta-marc-train-gtfs
    name: MDOT MTA MARC Train GTFS
    description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA MARC commuter rail service.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/gtfs/marc
    tags:
      - GTFS
      - Rail
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS
        url: https://feeds.mta.maryland.gov/gtfs/marc
      - type: GTFS-RT Trip Updates
        url: https://mdotmta-gtfs-rt.s3.amazonaws.com/MARC+RT/marc-tu.pb
      - type: GTFS-RT Vehicle Positions
        url: https://mdotmta-gtfs-rt.s3.amazonaws.com/MARC+RT/marc-vp.pb
  - aid: maryland-transit-administration:mta-commuter-bus-gtfs
    name: MDOT MTA Commuter Bus GTFS
    description: Static GTFS feed and GTFS-RT vehicle positions and trip updates for MDOT MTA Commuter Bus service.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/gtfs/commuter-bus
    tags:
      - GTFS
      - Bus
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS
        url: https://feeds.mta.maryland.gov/gtfs/commuter-bus
  - aid: maryland-transit-administration:mta-service-alerts
    name: MDOT MTA Service Alerts
    description: System-wide GTFS-RT service alerts feed for all MDOT MTA modes.
    humanURL: https://www.mta.maryland.gov/developer-resources
    baseURL: https://feeds.mta.maryland.gov/alerts.pb
    tags:
      - GTFS-RT
      - Alerts
      - Public Transportation
    properties:
      - type: Documentation
        url: https://www.mta.maryland.gov/developer-resources
      - type: GTFS-RT Alerts
        url: https://feeds.mta.maryland.gov/alerts.pb
common:
  - type: Portal
    url: https://www.mta.maryland.gov/developer-resources
  - type: Website
    url: https://www.mta.maryland.gov/
  - type: GTFS Specification
    url: https://gtfs.org/
  - type: Swiftly Documentation
    url: https://swiftly-inc.stoplight.io/docs/realtime-standalone/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
