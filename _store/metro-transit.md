---
aid: metro-transit
name: Metro Transit
description: Metro Transit provides real-time departure information, service alerts, trip planning, and schedule data APIs for the Minneapolis-Saint Paul metropolitan transit system. The APIs support creating transit departure displays and accessing real-time bus and train arrival data for the Twin Cities.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Minneapolis
  - Minnesota
  - Public Transportation
  - Real-Time
  - Transit
url: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/apis.yml
created: '2025-05-02'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: metro-transit:nextrip-api
    name: Metro Transit NexTrip API
    description: The NexTrip API provides real-time departure information for creating transit departure displays. It offers endpoints for routes, stops, and real-time departure data for the Twin Cities metro area.
    humanURL: https://svc.metrotransit.org/swagger/index.html
    baseURL: https://svc.metrotransit.org/nextripv2
    tags:
      - Departures
      - Real-Time
      - Transit
    properties:
      - type: Documentation
        url: https://svc.metrotransit.org/swagger/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/openapi/metro-transit-nextrip-openapi.json
  - aid: metro-transit:alerts-api
    name: Metro Transit Service Alerts API
    description: The Service Alerts API provides current service alerts for routes and stops across the Twin Cities Metro Transit network.
    humanURL: https://svc.metrotransit.org/swagger/index.html
    baseURL: https://svc.metrotransit.org/alerts
    tags:
      - Alerts
      - Real-Time
      - Transit
    properties:
      - type: Documentation
        url: https://svc.metrotransit.org/swagger/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/openapi/metro-transit-alerts-openapi.json
  - aid: metro-transit:trip-planner-api
    name: Metro Transit Trip Planner API
    description: The Trip Planner API supports building itineraries and routing trips across the Twin Cities Metro Transit system using stops, places, and schedules.
    humanURL: https://svc.metrotransit.org/swagger/index.html
    baseURL: https://svc.metrotransit.org/tripplanner
    tags:
      - Trip Planner
      - Routing
      - Transit
    properties:
      - type: Documentation
        url: https://svc.metrotransit.org/swagger/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/openapi/metro-transit-tripplanner-openapi.json
  - aid: metro-transit:schedule-api
    name: Metro Transit Schedule API
    description: The Schedule API provides published timetable data including routes, directions, stops, and schedule details for the Twin Cities Metro Transit system.
    humanURL: https://svc.metrotransit.org/swagger/index.html
    baseURL: https://svc.metrotransit.org/schedule
    tags:
      - Schedule
      - Timetable
      - Transit
    properties:
      - type: Documentation
        url: https://svc.metrotransit.org/swagger/index.html
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/metro-transit/refs/heads/main/openapi/metro-transit-schedule-openapi.json
common:
  - type: Portal
    url: https://www.metrotransit.org/developer-resources
  - type: Documentation
    url: https://svc.metrotransit.org/swagger/index.html
  - type: Website
    url: https://www.metrotransit.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
