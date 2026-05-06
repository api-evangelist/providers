---
aid: lennox-international
name: Lennox International
description: Lennox International is a global leader in the heating, air conditioning, and refrigeration markets, providing climate control solutions for residential and commercial applications. Lennox does not publish a general developer portal for HVAC system access. Smart-home integrations with the iComfort S30, E30, and M30 thermostat product lines are delivered through partnerships (Control4, Amazon Alexa, Apple HomeKit, Google Assistant, IFTTT) and through community-maintained, reverse-engineered Python and TypeScript libraries.
type: Contract
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: Partner
tags:
  - HVAC
  - Smart Home
  - Thermostat
  - IoT
  - Climate Control
url: https://raw.githubusercontent.com/api-evangelist/lennox-international/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: lennox-international:lennox-icomfort-smart-home-integrations
    name: Lennox iComfort Smart Home Integrations
    description: Official partner integrations for the Lennox iComfort S30, E30, and M30 smart thermostats. Connectivity is provided through Control4, Amazon Alexa, Apple HomeKit, Google Assistant, and IFTTT rather than a public developer API. Control4 drivers are distributed through authorized Control4 dealers.
    humanURL: https://www.lennoxpros.com/news/icomfort-smart-home-integration
    tags:
      - Smart Home
      - Thermostat
      - Integrations
    properties:
      - url: https://www.lennoxpros.com/news/icomfort-smart-home-integration
        type: Documentation
      - url: https://www.support.lennoxicomfort.com/help/lennox-control4/lennox-control4.html
        type: Documentation
  - aid: lennox-international:lennox-s30-community-api
    name: Lennox S30 Community API
    description: Community-maintained, reverse-engineered Python library for communicating with Lennox S30, S40, E30, and M30 climate controls via the Lennox cloud or local LAN. Powers the popular Home Assistant integration. Not an official Lennox product.
    humanURL: https://github.com/PeteRager/lennoxs30api
    tags:
      - Community
      - Python
      - Reverse Engineered
    properties:
      - url: https://github.com/PeteRager/lennoxs30api
        type: SourceCode
      - url: https://github.com/PeteRager/lennoxs30
        type: HomeAssistantIntegration
  - aid: lennox-international:lennoxapi-typescript
    name: lennoxapi (TypeScript)
    description: TypeScript port of the community Python library for controlling Lennox S30, S40, E30, and M30 thermostats over a local LAN connection. No cloud required.
    humanURL: https://github.com/lukealonso/lennoxapi
    tags:
      - Community
      - TypeScript
      - Local LAN
    properties:
      - url: https://github.com/lukealonso/lennoxapi
        type: SourceCode
common:
  - url: https://www.lennox.com/
    type: Website
  - url: https://www.lennoxinternational.com/
    type: CorporateWebsite
  - url: https://www.lennoxpros.com/
    type: PartnerPortal
  - url: https://www.support.lennoxicomfort.com/
    type: Support
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
