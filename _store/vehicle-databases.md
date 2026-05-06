---
aid: vehicle-databases
name: Vehicle Databases
description: Vehicle Databases provides automotive maintenance schedule APIs with OEM-compliant service schedules for vehicles up to 200,000 miles. Delivers maintenance intervals, service items, fluids, and recall data for automotive service platforms, fleet management systems, and consumer maintenance reminder applications.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Automotive
  - Fleet Management
  - Maintenance
  - Recalls
  - Vehicles
url: https://raw.githubusercontent.com/api-evangelist/vehicle-databases/refs/heads/main/apis.yml
specificationVersion: '0.19'
created: '2025-02-12'
modified: '2026-05-03'
apis:
  - aid: vehicle-databases:vehicle-databases
    name: Vehicle Databases Maintenance API
    description: The Vehicle Databases Maintenance API delivers OEM-compliant maintenance schedules for vehicles up to 200,000 miles. Provides service intervals by mileage and time, service item descriptions, fluid specifications, part numbers, labor time estimates, recall notices, technical service bulletins, and vehicle decoder (VIN) information for fleet operators, repair shops, and consumer-facing automotive applications.
    humanURL: https://vehicledatabases.com/vehicle-maintenance-api
    tags:
      - Automotive
      - Fleet Management
      - Maintenance
      - Recalls
      - Vehicles
    properties:
      - type: Documentation
        url: https://vehicledatabases.com/vehicle-maintenance-api
      - type: Portal
        url: https://vehicledatabases.com/
      - type: OpenAPI
        url: openapi/vehicle-databases-openapi.yml
      - type: JSONSchema
        url: json-schema/vehicle-databases-maintenance-schedule-schema.json
        title: Maintenance Schedule Schema
      - type: JSONSchema
        url: json-schema/vehicle-databases-service-item-schema.json
        title: Service Item Schema
      - type: JSONSchema
        url: json-schema/vehicle-databases-vehicle-schema.json
        title: Vehicle Schema
      - type: JSONStructure
        url: json-structure/vehicle-databases-maintenance-schedule-structure.json
        title: Maintenance Schedule Structure
      - type: JSONStructure
        url: json-structure/vehicle-databases-service-item-structure.json
        title: Service Item Structure
      - type: Example
        url: examples/vehicle-databases-maintenance-schedule-example.json
        title: Maintenance Schedule Example
      - type: Example
        url: examples/vehicle-databases-vehicle-example.json
        title: Vehicle Example
common:
  - type: Website
    url: https://vehicledatabases.com/
  - type: Portal
    url: https://vehicledatabases.com/
  - type: Documentation
    url: https://vehicledatabases.com/vehicle-maintenance-api
  - type: Pricing
    url: https://vehicledatabases.com/pricing
  - type: SpectralRules
    url: rules/vehicle-databases-spectral-rules.yml
    title: Vehicle Databases Spectral Rules
  - type: Vocabulary
    url: vocabulary/vehicle-databases-vocabulary.yml
    title: Vehicle Databases Vocabulary
  - type: NaftikoCapability
    url: capabilities/vehicle-maintenance.yaml
    title: Vehicle Maintenance
  - type: Features
    data:
      - name: OEM-Compliant Maintenance Schedules
        description: Factory maintenance schedules matching OEM specifications for vehicles up to 200,000 miles with mileage and time-based service intervals.
      - name: Service Item Details
        description: Detailed service item data including fluid specifications, part numbers, labor time estimates, and OEM-required procedures for each service.
      - name: VIN Decoder
        description: Decode 17-character VINs to extract make, model, year, engine, trim, and manufacturing details for vehicle identification.
      - name: Recall Data
        description: NHTSA recall information linked to specific vehicles including recall dates, component affected, risk description, and remedy status.
      - name: Technical Service Bulletins
        description: OEM technical service bulletins (TSBs) for specific vehicle issues including symptom description, diagnosis, and corrective action.
  - type: UseCases
    data:
      - name: Fleet Maintenance Management
        description: Automate maintenance scheduling for commercial and enterprise fleets using OEM-compliant service intervals and mileage-based triggers.
      - name: Auto Repair Shop Management
        description: Integrate maintenance schedules and TSBs into shop management systems to provide accurate service recommendations and labor estimates.
      - name: Consumer Maintenance Reminders
        description: Power maintenance reminder apps and connected car services with personalized OEM service schedules based on vehicle and mileage.
      - name: Insurance Telematics
        description: Combine telematics mileage data with maintenance schedules to provide proactive service alerts in usage-based insurance applications.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
