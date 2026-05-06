---
aid: centerpoint-energy
url: https://raw.githubusercontent.com/api-evangelist/centerpoint-energy/refs/heads/main/apis.yml
name: CenterPoint Energy
tags:
  - Electricity
  - Energy
  - Fortune 500
  - Green Button
  - Natural Gas
  - Smart Meter
  - Usage Data
  - Utility
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-21'
modified: '2026-04-23'
position: Consumer
specificationVersion: '0.19'
description: CenterPoint Energy is a domestic energy delivery company that provides electric transmission and distribution, natural gas distribution, and energy services operations serving residential, commercial, and industrial customers across multiple U.S. states. Developer-facing interfaces include the Smart Meter Texas (SMT) Usage History Inquiry API, Green Button Connect My Data exports for authorized third-party access to customer interval usage, and the Centerpoint Connect service API at api-portal.centerpointconnect.io used by contractor and field-service integrations.
apis:
  - aid: centerpoint-energy:usage-history-inquiry
    name: CenterPoint Energy Usage History Inquiry API
    tags:
      - Billing History
      - Interval Data
      - Smart Meter Texas
      - Usage
    humanURL: https://www.smartmetertexas.com/
    properties:
      - url: https://www.smartmetertexas.com/
        type: Website
      - url: https://www.smartmetertexas.com/home
        type: Documentation
      - url: https://www.smartmetertexas.com/developers
        type: Developer
    description: Automated access to residential and commercial billing history and electricity usage as measured by CenterPoint's Interval Data Recorders (IDRs), exposed through the Smart Meter Texas platform that CenterPoint participates in as a Texas Transmission and Distribution Service Provider. Intended for third-party information providers acting on customer authorization with API methods for account validation, provider account management, and retrieval of interval usage.
  - aid: centerpoint-energy:green-button-connect-my-data
    name: CenterPoint Energy Green Button Connect My Data
    tags:
      - Energy Usage
      - Green Button
      - Interval Data
      - Open Data
    humanURL: https://www.energy.gov/data/green-button
    properties:
      - url: https://www.energy.gov/data/green-button
        type: Website
      - url: https://www.greenbuttonalliance.org/
        type: Alliance
      - url: https://www.naesb.org/ESPI_Standards.asp
        type: Specification
    description: CenterPoint Energy has committed to the Green Button initiative, providing customers and authorized third parties with secure download and Connect My Data API access to detailed interval energy usage in the NAESB ESPI (Energy Services Provider Interface) standard XML / Atom format.
  - aid: centerpoint-energy:centerpoint-connect-services-api
    name: Centerpoint Connect Services API
    tags:
      - Field Service
      - Integration
      - Partner
    humanURL: https://api-portal.centerpointconnect.io/
    properties:
      - url: https://api-portal.centerpointconnect.io/
        type: Developer
      - url: https://centerpointconnect.zendesk.com/hc/en-us/sections/16652143336855-API-Integrations
        type: Documentation
    description: The Centerpoint API Developer Portal publishes Services API references, examples, and troubleshooting for partners integrating with the Centerpoint Connect field-service and workflow platform used by contractor teams, including Automated Leads integrations and webhook flows.
common:
  - type: Website
    url: https://www.centerpointenergy.com
  - type: Builder Developer Resources
    url: https://www.centerpointenergy.com/en-us/Services/Pages/builder-developer-resources.aspx
  - type: Energy Data Portal
    url: https://energydataportal.centerpointenergy.com/
  - type: Green Button
    url: https://www.energy.gov/data/green-button
  - type: Smart Meter Texas
    url: https://www.smartmetertexas.com/
  - type: Privacy Policy
    url: https://www.centerpointenergy.com/en-us/utility/pages/privacy-policy.aspx
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
