---
aid: rockwell-collins
name: Rockwell Collins
description: Rockwell Collins was a major American company providing avionics and information technology systems and services to government agencies and aircraft manufacturers. In 2018, Rockwell Collins was acquired by United Technologies and became part of Collins Aerospace, a subsidiary of RTX Corporation (formerly Raytheon Technologies). Collins Aerospace provides flight deck systems, cabin electronics, mission systems, communications, and advanced data services including FlightAware AeroAPI for aviation data. The Collins Digital Exchange offers API products for aerospace and defense integration.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/rockwell-collins/refs/heads/main/apis.yml
tags:
  - Avionics
  - Aerospace
  - Defense
  - Aviation
  - Flight Deck
created: '2026-03-24'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rockwell-collins:flightaware-aeroapi
    name: FlightAware AeroAPI
    description: FlightAware AeroAPI (formerly FlightXML) is a RESTful aviation data API acquired by Collins Aerospace in 2021. It provides access to real-time and historical flight tracking data, airport activity, flight positions, predictive ETAs powered by machine learning (FlightAware Foresight), and configurable alerting on flight events. With over 60 distinct endpoints organized into 7 functional families, AeroAPI supports aviation operations, maintenance scheduling, flight planning, and resource management.
    tags:
      - Aviation
      - Flight Tracking
      - Aerospace
      - REST
      - Real-Time Data
    humanURL: https://www.flightaware.com/commercial/aeroapi/
    baseURL: https://aeroapi.flightaware.com/aeroapi
    properties:
      - url: https://www.flightaware.com/commercial/aeroapi/
        type: Documentation
      - url: https://www.flightaware.com/aeroapi/portal
        type: Portal
      - url: openapi/flightaware-aeroapi-openapi.yml
        type: OpenAPI
      - url: https://github.com/flightaware/aeroapps
        type: GitHubRepository
    solutions:
      - Flight Planning
      - Resource Management
      - Maintenance Scheduling
      - Competitive Analysis
      - Real-Time Alerting
    features:
      - Real-Time Flight Tracking
      - Historical Flight Data (from 2011)
      - Predictive ETAs (Foresight)
      - Flight Event Alerts
      - Airport Activity
      - Aircraft Position
      - 60+ API Endpoints
  - aid: rockwell-collins:collins-digital-exchange-apis
    name: Collins Digital Exchange APIs
    description: The Collins Digital Exchange is a developer portal operated by Collins Aerospace providing API products for aerospace integration. The portal provides quick-start guides and authenticated access to Collins Aerospace API products for authorized partners, customers, and suppliers.
    tags:
      - Aerospace
      - Defense
      - Integration
      - Partner APIs
    humanURL: https://developer.collins.com/api-products
    baseURL: https://developer.collins.com
    properties:
      - url: https://developer.collins.com/api-products
        type: Portal
common:
  - url: https://www.rockwellcollins.com
    type: Website
  - url: https://www.rtx.com/collinsaerospace/
    type: Website
  - url: https://developer.collins.com/api-products
    type: Portal
  - url: https://portal.rockwellcollins.com/
    type: Portal
  - url: https://customers.collinsaerospace.com/
    type: Portal
  - url: https://www.flightaware.com/commercial/aeroapi/
    type: Documentation
  - url: https://www.rtx.com/collinsaerospace/what-we-do/service-and-support/support/support-lookup
    type: Support
  - url: openapi/flightaware-aeroapi-openapi.yml
    type: OpenAPI
  - url: json-schema/rockwell-collins-flight-schema.json
    type: JSONSchema
  - url: json-structure/rockwell-collins-flight-structure.json
    type: JSONStructure
  - url: json-ld/rockwell-collins-context.jsonld
    type: JSONLDContext
  - url: vocabulary/rockwell-collins-vocabulary.yml
    type: Vocabulary
  - url: rules/rockwell-collins-rules.yml
    type: SpectralRuleset
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
