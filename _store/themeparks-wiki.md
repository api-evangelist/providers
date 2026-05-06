---
aid: themeparks-wiki
name: ThemeParks.wiki
description: An ever-growing database of real-time data for the world's best theme parks, including wait times, schedules, and park information.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Entertainment
  - Real-Time
  - Theme Parks
  - Wait Times
  - Travel
created: '2025-02-24'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/themeparks-wiki/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: themeparks-wiki:themeparks-wiki
    name: ThemeParks.wiki API
    description: An ever-growing database of real-time data for the world's best theme parks, including wait times, schedules, and park information. Provides live wait times, operational status, park schedules, and entity metadata for 75+ destinations worldwide including Disney, Universal, Cedar Fair, and Six Flags. No authentication required.
    humanURL: https://themeparks.wiki/
    baseURL: https://api.themeparks.wiki/v1
    tags:
      - Entertainment
      - Real-Time
      - Theme Parks
      - Wait Times
      - Travel
    properties:
      - type: Documentation
        url: https://api.themeparks.wiki/docs/v1/
      - type: OpenAPI
        url: openapi/themeparks-wiki-openapi.yml
      - type: JSONSchema
        url: json-schema/themeparks-wiki-destination-schema.json
        title: Destination Schema
      - type: JSONStructure
        url: json-structure/themeparks-wiki-destination-structure.json
        title: Destination Structure
      - type: JSON-LD
        url: json-ld/themeparks-wiki-context.jsonld
        title: ThemeParks.wiki JSON-LD Context
common:
  - type: Website
    url: https://themeparks.wiki/
  - type: Documentation
    url: https://api.themeparks.wiki/docs/v1/
  - type: GitHub Organization
    url: https://github.com/ThemeParks
  - type: SpectralRules
    url: rules/themeparks-wiki-spectral-rules.yml
    title: ThemeParks.wiki Spectral Rules
  - type: Vocabulary
    url: vocabulary/themeparks-wiki-vocabulary.yml
    title: ThemeParks.wiki Vocabulary
  - type: NaftikoCapability
    url: capabilities/theme-park-planning.yaml
    title: Theme Park Planning
  - type: Authentication
    data:
      - name: No Authentication Required
        description: ThemeParks.wiki API is publicly accessible with no API key or authentication required
  - type: Features
    data:
      - name: Real-Time Wait Times
        description: Live queue wait times and operational status for attractions at 75+ destinations
      - name: Park Schedules
        description: Operating hours, special event schedules, and monthly calendar views for parks
      - name: Destination Catalog
        description: Complete listing of all supported theme park resort destinations worldwide
      - name: Entity Metadata
        description: Detailed information for parks, attractions, shows, and restaurants
      - name: Live Operational Status
        description: Real-time OPERATING, DOWN, CLOSED, and REFURBISHMENT status for all entities
      - name: Monthly Schedule Lookup
        description: Historical and future operating schedules by specific month and year
  - type: UseCases
    data:
      - name: Trip Planning
        description: Research park schedules and wait time patterns before visiting
      - name: Real-Time Monitoring
        description: Monitor live wait times and attraction availability during a park visit
      - name: Media Centers
        description: Power home media center displays with live park data and wait times
      - name: AI Park Assistant
        description: Power AI agents that help users plan and navigate theme park visits
  - type: Integrations
    data:
      - name: EmulationStation/RetroPie
        description: Community integrations for theme park data displays
      - name: Home Assistant
        description: Smart home integrations for displaying live park data on dashboards
      - name: Kodi
        description: Media center plugin integrations for theme park information
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
