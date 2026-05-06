---
aid: rush-enterprises
name: Rush Enterprises
description: Rush Enterprises is the largest network of commercial vehicle dealerships in North America, operating Rush Truck Centers with more than 200 locations across the United States. The company offers new and used commercial vehicles, all-makes parts, vehicle technology solutions, collision repair, alternative fuel systems, vehicle and equipment leasing, and financial services. Rush Enterprises provides fleet technology through RushCare, including Service Connect (integrated with OEMs like Peterbilt, International, Hino, and Cummins), Parts Connect, and telematics solutions powered by Geotab.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Commercial Vehicles
  - Fleet Management
  - Telematics
  - Truck Dealerships
  - Transportation
url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/apis.yml
created: '2026-03-21'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: rush-enterprises:rushcare-service-connect
    name: RushCare Service Connect
    description: RushCare Service Connect is a technology platform that provides a single portal integrated with OEMs, third-party repair software systems, and real-time telematics providers. It integrates with Peterbilt, International, Hino, Cummins, Decisiv, and Geotab to enable fleet managers to schedule service, view telematics faults, and manage vehicle maintenance across Rush Truck Centers locations.
    humanURL: https://serviceconnect.rushcare.com/
    tags:
      - Fleet Management
      - Service Management
      - Telematics
      - Vehicle Maintenance
    properties:
      - type: Website
        url: https://serviceconnect.rushcare.com/
      - type: Documentation
        url: https://rushcare.rushtruckcenters.com/
  - aid: rush-enterprises:rushcare-parts-connect
    name: RushCare Parts Connect
    description: RushCare Parts Connect is a technology platform for managing commercial vehicle parts procurement and supply chain operations across Rush Truck Centers locations.
    humanURL: https://rushcare.rushtruckcenters.com/
    tags:
      - Parts Management
      - Supply Chain
      - Commercial Vehicles
    properties:
      - type: Website
        url: https://rushcare.rushtruckcenters.com/
  - aid: rush-enterprises:rushcare-telematics
    name: RushCare Telematics
    description: RushCare Telematics provides fleet visibility and vehicle data monitoring powered by Geotab, the world's largest provider of premium quality telematics hardware. The platform offers an open SDK for integration with third-party solutions and enables data sharing with fleet management systems.
    humanURL: https://www.rushtruckcenters.com/service/programs/telematics-solutions
    tags:
      - Telematics
      - Fleet Visibility
      - Vehicle Data
      - Geotab
      - IoT
    properties:
      - type: Website
        url: https://www.rushtruckcenters.com/service/programs/telematics-solutions
      - type: Documentation
        url: https://www.rushtruckcenters.com/service/programs/telematics-solutions/hardware
common:
  - type: Website
    url: https://www.rushenterprises.com
  - type: Website
    url: https://www.rushtruckcenters.com
  - type: Technology
    url: https://rushcare.rushtruckcenters.com/
  - type: About
    url: https://www.rushenterprises.com/our-story
  - type: Investors
    url: https://investors.rushenterprises.com
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/vocabulary/rush-enterprises-vocabulary.yml
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-ld/rush-enterprises-context.jsonld
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-schema/rush-enterprises-vehicle-schema.json
  - type: JSONSchema
    url: https://raw.githubusercontent.com/api-evangelist/rush-enterprises/refs/heads/main/json-schema/rush-enterprises-service-event-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
