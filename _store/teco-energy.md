---
aid: teco-energy
name: TECO Energy
description: TECO Energy is an energy holding company and subsidiary of Emera Inc., operating Tampa Electric (electric utility serving west central Florida) and Peoples Gas (natural gas utility serving Florida). TECO Energy provides a developer portal powered by Azure API Management at developer.tecoenergy.com, exposing APIs for outage management, account services, energy usage, billing, and grid operations. Tampa Electric serves approximately 800,000 customers across the Tampa Bay area and parts of central Florida.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Utilities
  - Electric
  - Natural Gas
  - Smart Grid
  - Tampa Bay
url: https://raw.githubusercontent.com/api-evangelist/teco-energy/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: teco-energy:developer-api
    name: Tampa Electric API Management
    description: Tampa Electric provides a developer portal powered by Azure API Management at developer.tecoenergy.com. The portal enables developers to discover APIs, review documentation, try APIs interactively, and sign up for API keys. APIs likely include outage management, account services, energy usage data, billing, and grid operations. Authentication is required to access the full API catalog.
    humanURL: https://developer.tecoenergy.com/
    baseURL: https://developer.tecoenergy.com
    tags:
      - Electric Utility
      - Energy
      - API Management
      - Azure
      - Tampa Electric
    properties:
      - type: Documentation
        url: https://developer.tecoenergy.com/
      - type: DeveloperPortal
        url: https://developer.tecoenergy.com/
  - aid: teco-energy:outage-api
    name: Tampa Electric Outage API
    description: Tampa Electric exposes outage reporting and outage map data through its customer portal and API infrastructure. The outage map at account.tecoenergy.com/Outage/Outagemap enables customers to report and track power outages, serving as the foundation for utility outage management APIs covering outage creation, status, restoration times, and affected customer counts.
    humanURL: https://account.tecoenergy.com/Outage/Outagemap
    baseURL: https://account.tecoenergy.com
    tags:
      - Outage
      - Electric Utility
      - Grid Operations
      - Reliability
    properties:
      - type: Documentation
        url: https://account.tecoenergy.com/Outage/Outagemap
      - type: OpenAPI
        url: openapi/teco-energy-outage-openapi.yml
      - type: JSONSchema
        url: json-schema/teco-energy-outage-schema.json
  - aid: teco-energy:account-api
    name: Tampa Electric Account API
    description: Tampa Electric provides customer account management services including bill payment, usage history, paperless billing enrollment, service transfers, and energy audit tools. These customer-facing services are backed by account APIs enabling programmatic access to billing data, account status, payment history, and energy efficiency recommendations for residential and commercial customers.
    humanURL: https://account.tecoenergy.com/
    baseURL: https://account.tecoenergy.com
    tags:
      - Account Management
      - Billing
      - Energy Usage
      - Customer Service
    properties:
      - type: Documentation
        url: https://account.tecoenergy.com/
      - type: OpenAPI
        url: openapi/teco-energy-account-openapi.yml
      - type: JSONSchema
        url: json-schema/teco-energy-account-schema.json
common:
  - url: https://www.tecoenergy.com
    name: TECO Energy
    type: Website
    description: Main corporate website for TECO Energy.
  - url: https://developer.tecoenergy.com/
    name: Tampa Electric API Developer Portal
    type: DeveloperPortal
    description: Azure API Management developer portal for Tampa Electric APIs.
  - url: https://www.tampaelectric.com/
    name: Tampa Electric
    type: Website
    description: Tampa Electric subsidiary website.
  - url: https://account.tecoenergy.com/
    name: TECO Account Portal
    type: Portal
    description: Customer account management portal for billing and usage.
  - url: https://account.tecoenergy.com/Outage/Outagemap
    name: Tampa Electric Outage Map
    type: Status
    description: Real-time outage map for Tampa Electric service territory.
  - url: https://www.linkedin.com/company/teco-energy
    name: TECO Energy on LinkedIn
    type: LinkedIn
    description: TECO Energy LinkedIn company page.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
