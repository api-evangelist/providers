---
aid: us-space-comman
url: https://raw.githubusercontent.com/api-evangelist/us-space-comman/refs/heads/main/apis.yml
apis:
  - aid: us-space-comman:space-track-api
    name: Space-Track.org REST API
    tags:
      - Space Situational Awareness
      - Orbital Data
      - Satellite Tracking
      - Federal Government
      - Open Data
    humanURL: https://www.space-track.org/documentation
    properties:
      - url: https://www.space-track.org/documentation
        type: Documentation
      - url: https://www.space-track.org
        type: Portal
      - url: https://raw.githubusercontent.com/api-evangelist/us-space-comman/refs/heads/main/openapi/us-space-command-space-track-openapi.yml
        type: OpenAPI
    description: Space-Track.org is the official public source for US Space Command's satellite catalog and space situational awareness data, maintained by the 18th Space Defense Squadron. The REST API provides access to orbital element sets (GP/TLEs), the satellite catalog (SATCAT), conjunction data messages (CDMs), decay predictions (TIP), and space object history. Requires a free Space-Track.org account for authentication.
name: US Space Command
tags:
  - Federal Government
  - Space
  - Space Situational Awareness
  - Satellite Tracking
  - Open Data
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-03'
modified: '2026-05-03'
position: Consuming
description: US Space Command (USSPACECOM) is a unified combatant command in the United States Department of Defense responsible for conducting operations in, from, and through space to deter conflict and, if necessary, defeat aggressors. The command provides space situational awareness (SSA) data through Space-Track.org, including the official satellite catalog with orbital element sets, conjunction warnings, and reentry predictions for all tracked objects.
features:
  - Orbital Element Sets (GP / TLE)
  - Satellite Catalog (SATCAT)
  - Conjunction Data Messages (CDM)
  - Tracking and Impact Prediction (TIP)
  - Historical Orbital Ephemerides
  - Space Object Decay Data
useCases:
  - Satellite operations and collision avoidance
  - Space debris monitoring
  - Orbital mechanics research
  - Satellite tracking and identification
  - Space traffic management
  - Launch planning and collision risk assessment
integrations:
  - TraCSS (Traffic Coordination System for Space)
solutions:
  - Space Situational Awareness
  - Space Traffic Management
  - Orbital Debris Research
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
