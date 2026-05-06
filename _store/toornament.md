---
aid: toornament
name: Toornament
description: Toornament is an esports tournament management platform providing a comprehensive API for creating, managing, and viewing tournaments across 100+ esports disciplines. The API supports full tournament lifecycle management including participant registration, bracket generation, match reporting, and real-time standings. Used by game publishers, esports organizers, broadcasters, and gaming communities worldwide.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Esports
  - Gaming
  - Tournaments
  - Brackets
  - Competition
created: '2025-02-06'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/toornament/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: toornament:organizer-api
    name: Toornament Organizer API
    description: Full-featured tournament management API for tournament organizers. Provides complete CRUD operations for tournaments, participant management, stage and bracket configuration, match reporting, registration management, and webhook subscriptions. Requires API key authentication plus OAuth2 access tokens with organizer:view or organizer:admin scopes.
    humanURL: https://developer.toornament.com/v2/overview/get-started
    baseURL: https://api.toornament.com/organizer/v2
    tags:
      - Brackets
      - Esports
      - Gaming
      - Matches
      - Organizer
      - Participants
      - Tournaments
    properties:
      - type: Documentation
        url: https://developer.toornament.com/v2/overview/get-started
      - type: OpenAPI
        url: openapi/toornament-openapi.yml
      - type: SpectralRules
        url: rules/toornament-rules.yml
      - type: NaftikoCapability
        url: capabilities/shared/toornament-organizer.yaml
  - aid: toornament:viewer-api
    name: Toornament Viewer API
    description: Read-only public API for accessing tournament information without full organizer authentication. Ideal for embedding tournament brackets, leaderboards, and match schedules in applications, streaming overlays, and fan sites. Supports disciplines, tournaments, participants, stages, matches, and rankings.
    humanURL: https://developer.toornament.com/v2/doc/viewer_overview
    baseURL: https://api.toornament.com/viewer/v2
    tags:
      - Brackets
      - Esports
      - Gaming
      - Read-Only
      - Tournaments
      - Viewer
    properties:
      - type: Documentation
        url: https://developer.toornament.com/v2/doc/viewer_overview
common:
  - type: Website
    url: https://www.toornament.com/
    name: Toornament Website
    description: 'null'
  - type: Documentation
    url: https://developer.toornament.com/
    name: Toornament Developer Documentation
    description: 'null'
  - type: Getting Started
    url: https://developer.toornament.com/v2/overview/get-started
    name: Getting Started Guide
    description: 'null'
  - type: Sign Up
    url: https://www.toornament.com/signup/
    name: Toornament Sign Up
    description: 'null'
  - type: Login
    url: https://app.toornament.com/
    name: Toornament Login
    description: 'null'
  - type: Pricing
    url: https://www.toornament.com/en_US/p/tournament-api
    name: API Pricing
    description: 'null'
  - type: JSON-LD
    url: json-ld/toornament-context.jsonld
    name: Toornament JSON-LD Context
    description: JSON-LD context defining Toornament tournament domain vocabulary.
  - type: JSON-Schema
    url: json-schema/toornament-tournament-schema.json
    name: Toornament Tournament Schema
    description: JSON Schema for the Toornament Tournament entity.
  - type: JSONStructure
    url: json-structure/toornament-tournament-structure.json
    name: Toornament Tournament Structure
    description: Structured documentation of the Toornament Tournament object model.
  - type: SpectralRules
    url: rules/toornament-rules.yml
    name: Toornament Spectral Rules
    description: Spectral ruleset for Toornament API conventions.
  - type: NaftikoCapability
    url: capabilities/tournament-management.yaml
    name: Toornament Tournament Management Capability
    description: Naftiko workflow capability for esports tournament management.
  - type: Vocabulary
    url: vocabulary/toornament-vocabulary.yml
    name: Toornament Vocabulary
    description: Domain vocabulary for the Toornament esports platform.
  - name: Features
    type: Features
    data:
      - name: Tournament Creation and Management
      - name: Participant Registration
      - name: Bracket Generation (Single/Double Elimination)
      - name: Group Stage Management
      - name: Match Reporting
      - name: Live Rankings and Standings
      - name: Custom Registration Fields
      - name: Check-in Management
      - name: Webhook Event Notifications
      - name: Multi-discipline Support (100+ games)
      - name: Team and Player Support
      - name: Public Tournament Viewer API
  - name: Use Cases
    type: UseCases
    data:
      - name: Esports Tournament Platform
      - name: Game Publisher Tournament Integration
      - name: Streaming Overlay Bracket Display
      - name: Community Tournament Management
      - name: Fan Site Tournament Viewer
      - name: Circuit and League Management
  - name: Integrations
    type: Integrations
    data:
      - name: Postman
      - name: Insomnia
      - name: OAuth2 Identity Providers
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
