---
aid: flightaware
name: FlightAware
description: FlightAware is a global flight tracking and data platform that provides real-time flight tracking, mapping, and predictive technology to both individual users and commercial aviation companies. The platform collects data from a variety of sources including air traffic control systems, radar, ADS-B, and satellite data, and exposes that data to developers and commercial customers through its AeroAPI query-based REST API and its Firehose streaming feed.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
position: Consumer
created: '2025-02-24'
modified: '2026-04-28'
tags:
  - Aviation
  - Flights
  - Flight Tracking
  - Mapping
  - Radar
  - Satellites
  - Traffic Control
url: https://raw.githubusercontent.com/api-evangelist/flightaware/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: flightaware:aeroapi
    name: FlightAware AeroAPI
    description: AeroAPI is FlightAware's query-based REST API for accessing aviation data on demand. It exposes 60+ endpoints across flights, airports, operators, alerts, history, and Foresight predictive analytics, and supports both real-time and historical flight tracking, status, positions, routes, and notifications.
    humanURL: https://www.flightaware.com/aeroapi/portal/
    baseURL: https://aeroapi.flightaware.com/aeroapi
    tags:
      - Airports
      - Alerts
      - Aviation
      - Flights
      - Flight Tracking
      - Foresight
      - History
      - Operators
      - Predictive Analytics
    properties:
      - type: Documentation
        url: https://www.flightaware.com/aeroapi/portal/documentation
      - type: Portal
        url: https://www.flightaware.com/aeroapi/portal/
      - type: Pricing
        url: https://www.flightaware.com/commercial/aeroapi/
  - aid: flightaware:firehose
    name: FlightAware Firehose
    description: Firehose is FlightAware's real-time streaming feed of global flight data, delivering ADS-B, radar, and ATC-derived position, status, and event messages over a persistent TLS connection for enterprise-grade flight tracking, situational awareness, and operations analytics.
    humanURL: https://www.flightaware.com/commercial/firehose/
    tags:
      - ADS-B
      - Aviation
      - Flight Tracking
      - Real-Time
      - Streaming
    properties:
      - type: Documentation
        url: https://www.flightaware.com/commercial/firehose/documentation
      - type: ProductPage
        url: https://www.flightaware.com/commercial/firehose/
common:
  - type: Website
    url: https://www.flightaware.com/
  - type: CommercialData
    url: https://www.flightaware.com/commercial/data/
  - type: AeroAPIPortal
    url: https://www.flightaware.com/aeroapi/portal/
  - type: Documentation
    url: https://www.flightaware.com/aeroapi/portal/documentation
  - type: Pricing
    url: https://www.flightaware.com/commercial/aeroapi/
  - type: Blog
    url: https://blog.flightaware.com/
  - type: Support
    url: https://www.flightaware.com/about/contact/
  - type: PrivacyPolicy
    url: https://www.flightaware.com/about/privacy
  - type: TermsOfService
    url: https://www.flightaware.com/about/termsofuse
  - type: GitHub
    url: https://github.com/flightaware
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
