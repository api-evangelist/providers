---
aid: carrier-global
name: Carrier Global
description: Carrier Global Corporation is a global provider of healthy, safe, sustainable, and intelligent building and cold-chain solutions, spanning HVAC, refrigeration, fire, security, and building automation technologies. Its digital ecosystem includes the Lynx Fleet telematics platform (Lynx APIs for transport refrigeration units), the Abound building management platform, i-Vu and Carrier Comfort Network for commercial building automation, and the Carrier SmartHome app for residential smart thermostats.
type: Index
position: Provider
access: Partner
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - HVAC
  - Cold Chain
  - Telematics
  - Building Automation
  - IoT
  - Refrigeration
  - Fortune 500
created: '2026-03-21'
modified: '2026-04-23'
url: https://raw.githubusercontent.com/api-evangelist/carrier-global/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: carrier-global:lynx-fleet-api
    name: Carrier Lynx Fleet API
    description: REST API surface exposing Lynx Fleet telematics and control data for diesel and electric transport refrigeration units (TRUs). Enables systems integrators to pull asset inventory, setpoints, temperatures, alarms, and GPS location, and to issue two-way commands to connected refrigeration units directly from existing transport-management systems.
    humanURL: https://doc-api.fleet.lynx.carrier.io/
    baseURL: https://doc-api.fleet.lynx.carrier.io/
    tags:
      - Cold Chain
      - Telematics
      - Fleet
      - Refrigeration
      - IoT
    properties:
      - type: Documentation
        url: https://doc-api.fleet.lynx.carrier.io/api-documentation
      - type: Portal
        url: https://api.tta.lynxfleet.carrier.com/
      - type: Reference
        url: https://doc-api.fleet.lynx.carrier.io/docs/lynx-prod-api/1/routes/v1/assets/get
      - type: Products
        url: https://api.tta.lynxfleet.carrier.com/products
  - aid: carrier-global:i-vu-building-automation
    name: Carrier i-Vu Building Automation
    description: i-Vu is Carrier's web-based commercial building automation system for monitoring and controlling HVAC, lighting, and related building systems. It integrates with BACnet and other standard building protocols rather than a public REST API surface.
    humanURL: https://www.carrier.com/commercial/en/us/software/building-automation/i-vu-building-automation/
    tags:
      - Building Automation
      - BACnet
      - HVAC
    properties:
      - type: Documentation
        url: https://www.carrier.com/commercial/en/us/software/building-automation/i-vu-building-automation/
  - aid: carrier-global:carrier-comfort-network
    name: Carrier Comfort Network
    description: Carrier Comfort Network (CCN) is Carrier's proprietary control and communication network for tying together chillers, air handlers, and related HVAC equipment, typically integrated into BMS/BAS deployments.
    humanURL: https://www.carrier.com/commercial/en/us/carrier-comfort-network/
    tags:
      - Building Automation
      - HVAC
      - Chillers
    properties:
      - type: Documentation
        url: https://www.carrier.com/commercial/en/us/carrier-comfort-network/
  - aid: carrier-global:abound-building-platform
    name: Carrier Abound
    description: Abound is Carrier's cloud-based building intelligence platform that aggregates data from HVAC, IAQ sensors, and occupancy systems to provide indoor-environmental-quality analytics, energy insights, and healthy-building dashboards for commercial real estate operators.
    humanURL: https://www.carrier.com/commercial/en/us/software/abound/
    tags:
      - Building Intelligence
      - IAQ
      - Analytics
    properties:
      - type: Documentation
        url: https://www.carrier.com/commercial/en/us/software/abound/
  - aid: carrier-global:carrier-smarthome
    name: Carrier SmartHome App
    description: The Carrier SmartHome app lets homeowners remotely control Carrier connected smart thermostats and residential HVAC equipment. No public developer API is currently published; integration is via the consumer mobile app and connected thermostat web portals.
    humanURL: https://www.carrier.com/residential/en/us/smart-thermostats/smarthome-app/
    tags:
      - Smart Home
      - Thermostats
      - Residential
    properties:
      - type: Documentation
        url: https://www.carrier.com/residential/en/us/smart-thermostats/smarthome-app/
common:
  - type: Website
    url: https://www.corporate.carrier.com
  - type: ConsumerSite
    url: https://www.carrier.com/us/en/
  - type: Documentation
    name: Lynx Fleet API Documentation
    url: https://doc-api.fleet.lynx.carrier.io/
  - type: Portal
    name: Lynx Fleet Developer Portal
    url: https://api.tta.lynxfleet.carrier.com/
  - type: GettingStarted
    url: https://doc-api.fleet.lynx.carrier.io/api-documentation
  - type: Abound
    url: https://www.carrier.com/commercial/en/us/software/abound/
  - type: BuildingAutomation
    url: https://www.carrier.com/commercial/en/us/software/building-automation/i-vu-building-automation/
  - type: SmartHome
    url: https://www.carrier.com/residential/en/us/smart-thermostats/smarthome-app/
  - type: InvestorRelations
    url: https://ir.carrier.com
  - type: Careers
    url: https://careers.corporate.carrier.com
  - type: Contact
    url: https://www.corporate.carrier.com/contact-us/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
