---
aid: boeing
name: Boeing
description: Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, and telecommunications equipment. Boeing Developer Tools provides aviation data APIs powered by Jeppesen aeronautical databases, covering aircraft models, airport data, airspace information, NOTAMs, flight events, and runway operations.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/boeing/refs/heads/main/apis.yml
created: '2025-02-24'
modified: '2026-04-21'
specificationVersion: '0.19'
tags:
  - Aviation
  - Airplanes
  - Aerospace
  - Flight
  - Aeronautical
apis:
  - aid: boeing:boeing-aircraft-models-api
    name: Boeing Aircraft Models API
    description: The Boeing Aircraft Models API provides model characteristics of commercial and business aviation aircraft including ICAO/IATA codes, engine specifications, wingspan, weight, and height. Data sourced from Jeppesen aeronautical database updated on the 28-day AIRAC cycle.
    humanURL: https://developer.boeing.com/apis/aircraft-models/
    tags:
      - Aviation
      - Aircraft
      - Models
      - Jeppesen
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/aircraft-models/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-airports-aerodromes-api
    name: Boeing Airports and Aerodromes API
    description: The Boeing Airports and Aerodromes API provides current, worldwide aerodrome data from Jeppesen's aeronautical database, including airport identifiers, location data, and operational information for global flight operations.
    humanURL: https://developer.boeing.com/apis/airports-aerodromes/
    tags:
      - Aviation
      - Airports
      - Aerodromes
      - Jeppesen
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/airports-aerodromes/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-airspaces-api
    name: Boeing Airspaces API
    description: The Boeing Airspaces API provides detailed, current information about airspace classifications and boundaries around the globe to support flight planning and air traffic management applications.
    humanURL: https://developer.boeing.com/apis/airspaces/
    tags:
      - Aviation
      - Airspace
      - Flight Planning
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/airspaces/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-parts-api
    name: Boeing Parts API
    description: The Boeing Parts API enables searching and requesting price and availability information for specific Boeing aircraft parts, supporting maintenance, repair, and overhaul operations.
    humanURL: https://developer.boeing.com/apis/boeing-parts/
    tags:
      - Aviation
      - Parts
      - MRO
      - Maintenance
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/boeing-parts/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-flight-events-api
    name: Boeing Flight Events API
    description: The Boeing Flight Events API (Beta) provides real-time insights into worldwide flight events, enabling flight tracking applications and operational control systems to monitor global air traffic activity.
    humanURL: https://developer.boeing.com/apis/boeing-flight-events-beta/
    tags:
      - Aviation
      - Flight
      - Events
      - Real-Time
      - Tracking
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/boeing-flight-events-beta/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-notams-api
    name: Boeing NOTAMs API
    description: The Boeing NOTAMs API provides access to Jeppesen's global Notices to Air Missions (NOTAMs) database, enabling flight planning systems to retrieve current airspace restrictions and safety information.
    humanURL: https://developer.boeing.com/apis/notams-3/
    tags:
      - Aviation
      - NOTAMs
      - Safety
      - Flight Planning
      - Jeppesen
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/notams-3/
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-runway-monitor-api
    name: Boeing Runway Monitor API
    description: The Boeing Runway Monitor API provides active runway information for arrivals and departures at airports around the world, supporting dispatch and operations control center workflows.
    humanURL: https://developer.boeing.com/apis/runway-monitor
    tags:
      - Aviation
      - Runway
      - Airports
      - Operations
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/runway-monitor
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-standard-minimums-api
    name: Boeing Standard Minimums API
    description: The Boeing Standard Minimums API provides worldwide, detailed, and current information about instrument approach standard minimums for airports globally, supporting flight dispatch and operations planning.
    humanURL: https://developer.boeing.com/apis/standard-minimums
    tags:
      - Aviation
      - Minimums
      - Instrument
      - Flight Planning
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/standard-minimums
      - type: Portal
        url: https://developer.boeing.com/
  - aid: boeing:boeing-taxi-time-api
    name: Boeing Taxi Time API
    description: The Boeing Taxi Time API provides current taxi time information at airports around the world, enabling airline operations and flight planning systems to optimize departure timing and gate scheduling.
    humanURL: https://developer.boeing.com/apis/taxi-time-3
    tags:
      - Aviation
      - Taxi
      - Airports
      - Operations
      - Flight Planning
    properties:
      - type: Documentation
        url: https://developer.boeing.com/apis/taxi-time-3
      - type: Portal
        url: https://developer.boeing.com/
common:
  - type: Website
    url: https://www.boeing.com
  - type: Portal
    url: https://developer.boeing.com/
  - type: APIDirectory
    url: https://developer.boeing.com/apis
maintainers:
  - FN: Kin Lane
    email: kinlane@gmail.com
---
