---
aid: visteon
name: Visteon
description: Visteon Corporation is a global automotive electronics supplier providing innovative cockpit electronics products and connected car solutions to vehicle manufacturers worldwide. The Visteon Phoenix platform offers a JavaScript API for building HTML5-based automotive infotainment applications covering audio control, phone integration, media playback, navigation, screen management, remote UI, and vehicle data access. Phoenix Studio enables third-party app development targeting Visteon's SmartCore and display audio infotainment systems.
image: https://www.visteon.com/wp-content/themes/visteon/images/visteon-logo.png
type: Index
tags:
  - Automotive
  - Connected Car
  - Infotainment
  - IoT
url: https://raw.githubusercontent.com/api-evangelist/visteon/refs/heads/main/apis.yml
created: '2026-03-24'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: visteon:phoenix-api
    name: Visteon Phoenix API
    description: The Phoenix API is an automotive-oriented JavaScript interface for building HTML5 applications on Visteon's Phoenix infotainment platform. The API provides access to vehicle cockpit domains including audio playback and volume control, phone call management, media library browsing, navigation routing, screen and display management, remote UI rendering, and vehicle data such as speed, fuel level, and HVAC status. Applications written with the Phoenix API can run across multiple Visteon infotainment hardware platforms including SmartCore and display audio units.
    humanURL: https://developer.visteon.com/phoenix/api.html
    baseURL: https://developer.visteon.com/phoenix
    tags:
      - Audio
      - Automotive
      - Connected Car
      - HMI
      - HTML5
      - Infotainment
      - JavaScript
      - Navigation
      - Vehicle Data
    properties:
      - type: Documentation
        url: https://developer.visteon.com/phoenix/api.html
      - type: SDK
        url: https://developer.visteon.com/phoenix/sdk.html
      - type: Developer Portal
        url: https://developer.visteon.com/phoenix/
      - type: OpenAPI
        url: openapi/visteon-phoenix-openapi.yml
    contact:
      - FN: Visteon Developer Network
        url: https://developer.visteon.com/phoenix/
  - aid: visteon:phoenix-sdk
    name: Visteon Phoenix SDK
    description: The Phoenix Software Development Kit provides development tools for building automotive infotainment applications targeting Visteon hardware. Phoenix Studio 2.0 is a PC-based IDE that enables app development with hardware simulation, device emulation, and the Phoenix API reference integrated into the development environment. Apps can be developed once and deployed to any supported Visteon infotainment platform.
    humanURL: https://developer.visteon.com/phoenix/sdk.html
    baseURL: https://developer.visteon.com/phoenix
    tags:
      - Automotive
      - Development Tools
      - HTML5
      - Infotainment
      - JavaScript
      - SDK
    properties:
      - type: Documentation
        url: https://developer.visteon.com/phoenix/sdk.html
      - type: Getting Started
        url: https://developer.visteon.com/phoenix/
    contact:
      - FN: Visteon Developer Network
        url: https://developer.visteon.com/phoenix/
common:
  - type: Website
    url: https://www.visteon.com
  - type: Developer Portal
    url: https://developer.visteon.com/phoenix/
  - type: OpenAPI
    url: openapi/visteon-phoenix-openapi.yml
  - type: JSONSchema
    url: json-schema/visteon-vehicle-data-schema.json
  - type: JSONSchema
    url: json-schema/visteon-audio-schema.json
  - type: JSONLD
    url: json-ld/visteon-context.jsonld
  - type: Vocabulary
    url: vocabulary/visteon-vocabulary.yml
  - type: SpectralRules
    url: rules/visteon-rules.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
