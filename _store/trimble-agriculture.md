---
aid: trimble-agriculture
name: Trimble Agriculture
description: The Trimble Agriculture Cloud is an independent, brand-agnostic platform that connects infield devices and operational workflows to more efficiently execute crop production plans and collect robust agricultural datasets. The Trimble Agriculture API (now operating as PTxAg FarmENGAGE) provides REST APIs for farm setup, field boundaries, task records, work orders, prescriptions, equipment activities, crop zones, materials, and telematics. It enables third-party integrators to exchange as-applied data, send prescriptions to Trimble displays, and align field resources across precision agriculture systems. The platform serves over 180 million customer acres globally.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Agriculture
  - Farming
  - IoT
  - Precision Agriculture
  - Field Management
  - Prescriptions
  - Telematics
url: https://raw.githubusercontent.com/api-evangelist/trimble-agriculture/refs/heads/main/apis.yml
created: '2025-02-06'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: trimble-agriculture:trimble-agriculture-data
    name: Trimble Agriculture Data API
    description: 'The Trimble Agriculture Data API (PTxAg FarmENGAGE API) provides REST endpoints for managing farms, fields, crop zones, boundaries, equipment activities, work orders, prescriptions, materials, and imagery. Enables third-party integrators to exchange precision agriculture data between field devices and farm management platforms. Base URL: https://cloud.api.trimble.com/Trimble-Ag-Software/externalApi/3.0'
    humanURL: https://agdeveloper.trimble.com/api-docs
    tags:
      - Agriculture
      - Farming
      - Field Management
      - Prescriptions
      - Equipment Activities
      - Work Orders
      - Crop Zones
      - Boundaries
    properties:
      - type: Documentation
        url: https://agdeveloper.trimble.com/api-docs
      - type: GettingStarted
        url: https://agdeveloper.trimble.com/
      - type: OpenAPI
        url: openapi/trimble-agriculture-openapi.yml
  - aid: trimble-agriculture:trimble-agriculture-telematics
    name: Trimble Agriculture Telematics API
    description: The Trimble Agriculture Telematics API provides access to real-time and historical equipment telematics data from connected Trimble displays and precision agriculture devices. Includes equipment location, status, and operational metrics.
    humanURL: https://agdeveloper.trimble.com/api-docs
    tags:
      - Agriculture
      - Telematics
      - IoT
      - Equipment
      - GPS
    properties:
      - type: Documentation
        url: https://agdeveloper.trimble.com/api-docs
features:
  - Farm, field, and crop zone management
  - Equipment activity data from precision ag displays
  - As-applied data for regulatory compliance and productivity analysis
  - Prescription management (send to and receive from Trimble displays)
  - Field boundary, guidance line, and landmark synchronization
  - Work order creation and assignment to farm operators
  - Materials management for inputs (seeds, fertilizers, chemicals)
  - GeoTIFF imagery upload and processing for crop zones
  - Equipment telematics and real-time positioning
  - Multi-tenant organization support for agronomists and consultants
useCases:
  - Access as-applied data from Trimble displays for compliance reporting
  - Send variable-rate prescriptions to in-field Trimble displays
  - Align field boundaries and landmarks with farm management software
  - Plan and assign work orders to farm equipment operators
  - Integrate harvest data with third-party yield analysis platforms
  - Monitor equipment telematics for fleet management
  - Build agronomist portals accessing farmer data with consent
integrations:
  - Trimble Precision-IQ display field application
  - Trimble Ag Software and Trimble Ag Mobile
  - PTxAg FarmENGAGE platform
  - Third-party precision agriculture software systems
solutions:
  - Third-party software vendors integrating with Trimble precision ag ecosystem
  - Custom applicators and agronomists accessing farm data APIs
  - Large production farms building multi-vendor data workflows
  - Regulatory compliance and farm management platforms
common:
  - type: Website
    url: https://agriculture.trimble.com/
  - type: DeveloperPortal
    url: https://agdeveloper.trimble.com/
  - type: Documentation
    url: https://agdeveloper.trimble.com/api-docs
  - type: SignUp
    url: https://agdeveloper.trimble.com/
  - type: Contact
    url: mailto:ag_api@trimble.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
