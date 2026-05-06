---
aid: steelcase
name: Steelcase
description: Steelcase is a global leader in the office furniture and workplace design industry, providing furniture, technology, and research-based insights to help organizations create effective work environments. Steelcase offers the RoomWizard API for integrating room scheduling and conference room reservation systems with enterprise calendaring platforms. The API enables developers to manage room bookings, retrieve availability, and synchronize reservations with Microsoft Exchange, Office 365, and Google Calendar.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Office Furniture
  - Workplace
  - Room Scheduling
  - Facilities Management
  - IoT
  - Smart Office
created: '2025-03-01'
modified: '2026-05-02'
url: https://raw.githubusercontent.com/api-evangelist/steelcase/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: steelcase:roomwizard-api
    name: Steelcase RoomWizard API
    description: The Steelcase RoomWizard API provides programmatic access to conference room scheduling and reservation management. Using HTTP GET and POST requests, developers can retrieve room bookings, create reservations, check room availability, and synchronize with enterprise calendaring systems including Microsoft Exchange, Office 365, and Google Calendar. The API returns XML-structured responses and supports webhook-style synchronization for keeping room status current.
    humanURL: https://www.steelcase.com/products/scheduling-systems/roomwizard/
    baseURL: https://roomwizard.local/api
    tags:
      - Room Scheduling
      - Conference Rooms
      - Calendaring
      - Facilities Management
      - Workplace
    properties:
      - type: Documentation
        url: https://www.steelcase.com/techsupport/types/spec-guide/
      - type: OpenAPI
        url: openapi/steelcase-roomwizard-api-openapi.yml
    contact:
      - FN: Steelcase Tech Support
        url: https://www.steelcase.com/techsupport/
common:
  - type: Website
    url: https://www.steelcase.com
  - type: TechSupport
    url: https://www.steelcase.com/techsupport/
  - type: Downloads
    url: https://www.steelcase.com/techsupport/downloads/
  - type: JSONSchema
    url: json-schema/steelcase-booking-schema.json
  - type: JSONSchema
    url: json-schema/steelcase-room-schema.json
  - type: JSONStructure
    url: json-structure/steelcase-booking-structure.json
  - type: JSONStructure
    url: json-structure/steelcase-room-structure.json
  - type: JSON-LD
    url: json-ld/steelcase-context.jsonld
  - type: SpectralRules
    url: rules/steelcase-rules.yml
  - type: NaftikoCapabilities
    url: capabilities/room-scheduling.yaml
  - type: Vocabulary
    url: vocabulary/steelcase-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
