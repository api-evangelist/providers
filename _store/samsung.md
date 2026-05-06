---
aid: samsung
name: Samsung
description: Samsung Electronics is a global technology leader offering developer platforms for building applications and services across mobile devices, IoT, smart home, enterprise security, and entertainment. The Samsung Developer ecosystem spans SmartThings (IoT and smart home platform), Knox (enterprise device security and management), Galaxy mobile SDKs, Smart TV, and Tizen cross-platform development. Samsung provides REST APIs, SDKs, and tools that enable developers to create connected experiences for hundreds of millions of Galaxy devices and Samsung smart home products worldwide.
url: https://developer.samsung.com/
tags:
  - Consumer Electronics
  - Developer Platform
  - IoT
  - Mobile
  - Smart Home
  - Smart TV
  - Wearables
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
created: '2025-02-08'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: samsung:smartthings
    name: SmartThings API
    description: 'The SmartThings REST API provides programmatic access to the SmartThings platform for controlling connected devices, creating automations, managing locations, and building smart home integrations. Supports OAuth 2.0 and personal access tokens. Base URL: https://api.smartthings.com/v1.'
    humanURL: https://developer.smartthings.com/
    baseURL: https://api.smartthings.com/v1
    tags:
      - Automations
      - Connected Devices
      - IoT
      - Locations
      - Rules
      - Scenes
      - Smart Home
      - SmartThings
    properties:
      - type: Documentation
        url: https://developer.smartthings.com/docs/
      - type: Documentation
        url: https://developer.smartthings.com/docs/api/public
      - type: OpenAPI
        url: openapi/samsung-smartthings-openapi.yml
  - aid: samsung:knox-cloud
    name: Knox Cloud APIs
    description: Samsung Knox provides enterprise-grade device management and security APIs. Knox Cloud APIs enable programmatic access to Knox Deployment Program, Knox Mobile Enrollment, Knox Configure, Knox Manage, Knox E-FOTA, Knox Guard, Knox Asset Intelligence, and Knox MSP Portal for enterprise device lifecycle management.
    humanURL: https://docs.samsungknox.com/dev/
    tags:
      - Device Management
      - Enterprise
      - Knox
      - MDM
      - Mobile Device Management
      - Security
    properties:
      - type: Documentation
        url: https://docs.samsungknox.com/dev/
      - type: Documentation
        url: https://developer.samsungknox.com/develop
  - aid: samsung:health-sdk
    name: Samsung Health SDK
    description: The Samsung Health SDK enables developers to create health and fitness applications for Galaxy Watch and smartphones, providing access to health data including steps, heart rate, sleep, workouts, and body measurements.
    humanURL: https://developer.samsung.com/health
    tags:
      - Fitness
      - Galaxy Watch
      - Health
      - Wearables
    properties:
      - type: Documentation
        url: https://developer.samsung.com/health
  - aid: samsung:galaxy-mobile
    name: Galaxy Mobile SDKs
    description: Samsung Galaxy mobile SDKs provide access to device-specific hardware and software features including S Pen Remote, DeX desktop mode, AR Emoji, foldable device optimization, Samsung Blockchain, eSE (embedded secure element), TEEGRIS trusted execution environment, and Galaxy Performance SDK.
    humanURL: https://developer.samsung.com/
    tags:
      - Android
      - Foldable
      - Galaxy
      - Mobile
      - S Pen
      - Samsung DeX
    properties:
      - type: Documentation
        url: https://developer.samsung.com/
  - aid: samsung:smart-tv
    name: Samsung Smart TV SDK
    description: The Samsung Smart TV developer platform enables development of Tizen-based applications for Samsung Smart TVs, including access to TV-specific APIs for media playback, user interface, smart signage, hospitality displays, and TV input management.
    humanURL: https://developer.samsung.com/smarttv
    tags:
      - Media
      - Smart TV
      - Streaming
      - Tizen
      - TV
    properties:
      - type: Documentation
        url: https://developer.samsung.com/smarttv
  - aid: samsung:bixby
    name: Bixby Developer API
    description: The Bixby developer platform allows developers to integrate Samsung's voice assistant into their applications and create custom Bixby capsules (skills) that respond to natural language commands across Galaxy devices, Smart TVs, and appliances.
    humanURL: https://bixby.developer.samsung.com/
    tags:
      - AI
      - Bixby
      - Natural Language Processing
      - Voice Assistant
    properties:
      - type: Documentation
        url: https://bixby.developer.samsung.com/
  - aid: samsung:samsung-wallet
    name: Samsung Wallet API
    description: Samsung Wallet API allows developers to add digital passes, tickets, boarding passes, loyalty cards, coupons, and payment cards to the Samsung Wallet app on Galaxy devices.
    humanURL: https://developer.samsung.com/wallet
    tags:
      - Digital Wallet
      - Loyalty
      - Passes
      - Payments
      - Wallet
    properties:
      - type: Documentation
        url: https://developer.samsung.com/wallet
common:
  - type: Documentation
    url: https://developer.samsung.com/
    title: Samsung Developer Portal
  - type: Documentation
    url: https://docs.samsungknox.com/dev/
    title: Samsung Knox Developer Documentation
  - type: Documentation
    url: https://developer.smartthings.com/docs/
    title: SmartThings Developer Documentation
  - type: GitHubOrganization
    url: https://github.com/SmartThingsCommunity
    title: SmartThings Community GitHub
  - type: GitHubOrganization
    url: https://github.com/samsung
    title: Samsung GitHub Organization
  - type: SpectralRules
    url: rules/samsung-rules.yml
    title: Samsung API Spectral Rules
  - type: NaftikoCapability
    url: capabilities/smart-home-control.yaml
    title: Samsung SmartThings Smart Home Control Capability
  - type: JSONSchema
    url: json-schema/samsung-smartthings-device-schema.json
    title: Samsung SmartThings Device Schema
  - type: JSONStructure
    url: json-structure/samsung-smartthings-device-structure.json
    title: Samsung SmartThings Device Structure
  - type: JSONLDContext
    url: json-ld/samsung-context.jsonld
    title: Samsung JSON-LD Context
  - type: Example
    url: examples/samsung-list-devices-example.json
    title: Samsung SmartThings List Devices Example
  - type: Example
    url: examples/samsung-execute-device-command-example.json
    title: Samsung SmartThings Execute Device Command Example
  - type: Vocabulary
    url: vocabulary/samsung-vocabulary.yml
    title: Samsung Developer Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
