---
aid: iata
name: IATA
description: The International Air Transport Association (IATA) is the global trade association representing and serving the airline industry. IATA sets standards for the aviation industry, promotes cooperation among airlines, and operates an Open API Hub providing access to airline-published APIs for flight status, destinations, baggage, ticket validation, cargo, digital identity, and related aviation data services.
url: https://raw.githubusercontent.com/api-evangelist/iata/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Airlines
  - Airports
  - Aviation
  - Cargo
  - Standards
  - Travel
created: '2025-03-01'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: iata:iata-open-api-hub
    name: IATA Open API Hub
    description: The IATA Open API Hub aggregates airline-published APIs covering flight status, customer flight info, destinations, port lists, ticket validation, baggage claims, pet travel, and verifiable credential revocation lists from carriers including Lufthansa, Air France, Qantas, Singapore Airlines, Turkish Airlines, China Southern, United, Avianca, and IATA itself.
    humanURL: https://api.developer.iata.org/hub/
    tags:
      - Airlines
      - Aviation
      - Flight Status
    properties:
      - type: Documentation
        url: https://api.developer.iata.org/hub/
      - type: Portal
        url: https://developer.iata.org/en/
  - aid: iata:one-record
    name: IATA ONE Record
    description: ONE Record is IATA's standard for data sharing in air cargo, defining a single record view of shipments accessible across stakeholders via standardized APIs and a shared data model.
    humanURL: https://onerecord.iata.org/
    tags:
      - Cargo
      - Logistics
      - Standards
    properties:
      - type: Documentation
        url: https://onerecord.iata.org/
  - aid: iata:ndc
    name: IATA New Distribution Capability (NDC)
    description: NDC is an XML-based data transmission standard that enhances the capability of communications between airlines and travel agents, enabling rich content and personalized offers across the airline distribution channel.
    humanURL: https://www.iata.org/en/programs/airline-distribution/ndc/
    tags:
      - Airlines
      - Distribution
      - Standards
    properties:
      - type: Documentation
        url: https://www.iata.org/en/programs/airline-distribution/ndc/
common:
  - type: Portal
    url: https://developer.iata.org/en/
  - type: Hub
    url: https://api.developer.iata.org/hub/
  - type: Website
    url: https://www.iata.org/
  - type: Support
    url: https://www.iata.org/en/contact-us/
  - type: Code Samples
    url: https://github.com/airtechzone
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
