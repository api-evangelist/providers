---
aid: united-technologies
name: United Technologies
url: https://raw.githubusercontent.com/api-evangelist/united-technologies/refs/heads/main/apis.yml
description: United Technologies Corporation (UTC) was an American multinational conglomerate that merged with Raytheon Company in 2020 to form Raytheon Technologies, later renamed RTX Corporation in 2023. Prior to the merger, UTC's major subsidiaries included Otis Elevator (now independent), Carrier Global (now independent), Pratt & Whitney, and Collins Aerospace. Today, Collins Aerospace (formerly UTC Aerospace Systems and Rockwell Collins) provides aviation connectivity and data exchange services through the ARINC Digital Exchange platform, including messaging, flight operations, and weather data APIs for commercial aviation.
modified: '2026-05-03'
tags:
  - Aerospace
  - Defense
  - Aviation
  - Manufacturing
  - Connectivity
apis:
  - name: Collins Aerospace ARINC Messaging API
    description: The Collins Aerospace ARINC Messaging API provides access to the ARINC Global Network for aviation messaging and data exchange. Supports ACARS, OOOI flight events, aviation weather, and operational communications between aircraft, airlines, airports, and ground operations. Part of the Collins Aerospace ARINC Digital Exchange platform.
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.rtx.com/collinsaerospace/what-we-do/industries/commercial-aviation/ground-operations/messaging-data-exchange
    baseURL: https://api.arinconline.collinsaerospace.com
    tags:
      - Aviation
      - Messaging
      - ACARS
      - OOOI
      - Aerospace
    properties:
      - type: Documentation
        url: https://www.rtx.com/collinsaerospace/what-we-do/industries/commercial-aviation/ground-operations/messaging-data-exchange/arinc-messaging
      - type: OpenAPI
        url: openapi/united-technologies-arinc-messaging-openapi.yml
      - type: JSONSchema
        url: json-schema/arinc-messaging-message-schema.json
        title: Message Schema
      - type: JSONSchema
        url: json-schema/arinc-messaging-flight-schema.json
        title: Flight Schema
      - type: JSONStructure
        url: json-structure/arinc-messaging-message-structure.json
        title: Message Structure
      - type: JSON-LD
        url: json-ld/united-technologies-arinc-messaging-context.jsonld
      - type: Example
        url: examples/arinc-messaging-message-example.json
        title: Message Example
    aid: united-technologies:arinc-messaging-api
common:
  - type: Website
    url: https://www.rtx.com/collinsaerospace
  - type: Portal
    url: https://arinconline.collinsaerospace.com
  - type: Documentation
    url: https://www.rtx.com/collinsaerospace/what-we-do/industries/commercial-aviation/ground-operations/messaging-data-exchange
  - type: SpectralRules
    url: rules/united-technologies-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/aviation-operations.yaml
    title: Aviation Operations
  - type: Vocabulary
    url: vocabulary/united-technologies-vocabulary.yaml
  - type: Features
    data:
      - name: ARINC Global Network
        description: Industry-standard aviation communications network connecting aircraft, airlines, airports, and ground operations worldwide.
      - name: ACARS Messaging
        description: Aircraft Communications Addressing and Reporting System messaging for digital communications between aircraft and ground.
      - name: OOOI Flight Events
        description: Real-time Out, Off, On, In flight event tracking for operational efficiency and on-time performance monitoring.
      - name: Aviation Weather Data
        description: METARs, TAFs, SIGMETs, PIREPs, and graphical weather services for flight operations and dispatch.
      - name: ARINC Integrator Platform
        description: Flexible integration platform deployable on-premise, SaaS, or in customer cloud for managing aviation data exchange.
      - name: Connected Aircraft Solutions
        description: InteliSight, GlobalConnect, and FlightHub platforms for comprehensive connected aircraft and ground operations.
      - name: Airport Network Connectivity
        description: AviNet Airport and GLOBALink network infrastructure for airport ground operations and avionics connectivity.
  - type: UseCases
    data:
      - name: Airline Operations Control
        description: Monitor real-time flight status, OOOI events, and aircraft communications for dispatch and operations center workflows.
      - name: Ground Operations Automation
        description: Automate gate assignments, crew notifications, and turnaround communications using ACARS uplink messaging.
      - name: Flight Dispatch
        description: Access METARs, TAFs, and SIGMETs for pre-flight weather briefings and in-flight weather monitoring.
      - name: Maintenance MRO Integration
        description: Receive ACARS maintenance messages and fault codes from aircraft for predictive maintenance workflows.
      - name: Passenger Service Messaging
        description: Send gate change and operational update messages to aircraft for cabin crew announcements.
      - name: Airport Operations Management
        description: Integrate OOOI flight data into airport management systems for terminal planning and resource allocation.
  - type: Integrations
    data:
      - name: Airbus Skywise
        description: Collins Aerospace joined the Digital Alliance for Aviation powered by Airbus Skywise for predictive maintenance and health monitoring.
      - name: SAP Aviation
        description: ARINC flight operations data integrates with SAP IS-A for airline operations and financial management.
      - name: Amadeus
        description: OOOI and flight status data integrates with Amadeus Altea CM for airline departure control and passenger services.
      - name: SITA
        description: Complementary aviation communications network for shared messaging and airport data exchange services.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
