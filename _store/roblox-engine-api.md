---
aid: roblox-engine-api
name: Roblox Engine API
description: Roblox provides a suite of developer APIs for building experiences on the Roblox platform. The Engine API documents all classes, data types, enumerations, functions, events, callbacks, and properties for in-experience scripting in Luau. The Open Cloud REST API provides external programmatic access to Roblox platform resources including experiences, places, data stores, users, groups, assets, messaging, and more. In March 2026 Roblox launched new unified Open Cloud reference documentation.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Gaming
  - Game Development
  - Metaverse
  - Roblox
  - Open Cloud
url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/apis.yml
created: '2024-11-07'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: roblox-engine-api:roblox-engine-api
    name: Roblox Engine API
    description: The Roblox Engine API documents all classes, data types, enumerations, global functions, variables, and libraries available when scripting Roblox experiences in Luau. This is the primary reference for in-engine development covering services, instances, and platform behaviors.
    humanURL: https://create.roblox.com/docs/reference/engine
    tags:
      - Gaming
      - Luau
      - Scripting
      - Engine
    properties:
      - type: Documentation
        url: https://create.roblox.com/docs/reference/engine
  - aid: roblox-engine-api:roblox-open-cloud-api
    name: Roblox Open Cloud API
    description: The Roblox Open Cloud API is a REST API providing external programmatic access to Roblox platform resources. It supports experiences (universes), places, data stores, memory stores, users, groups, assets, messaging, badges, game passes, and subscriptions. Authentication uses API keys scoped to specific resources. The API is organized into Open Cloud v2, v1, and Legacy tiers.
    humanURL: https://create.roblox.com/docs/cloud/reference
    baseURL: https://apis.roblox.com
    tags:
      - Gaming
      - Open Cloud
      - REST API
      - Data Stores
      - Experiences
      - Users
      - Groups
    properties:
      - url: https://create.roblox.com/docs/cloud/reference
        type: Documentation
      - url: https://create.roblox.com/docs/cloud/reference/openapi
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/openapi/roblox-open-cloud-openapi.yml
        type: OpenAPI
      - url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/rules/roblox-open-cloud-rules.yml
        type: SpectralRules
      - url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/capabilities/experience-management.yaml
        type: NaftikoCapabilities
      - url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/json-schema/roblox-universe-schema.json
        type: JSONSchema
      - url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/json-schema/roblox-user-schema.json
        type: JSONSchema
    contact:
      - FN: Roblox Developer Relations
        url: https://devforum.roblox.com
    features:
      - Experience Management
      - Place Publishing
      - Data Store Access
      - Memory Store Operations
      - User Management
      - Group Management
      - Asset Management
      - Messaging Service
      - Badge Management
      - Game Pass Management
      - Subscription Management
      - Inventory Access
    useCases:
      - External automation of Roblox experiences
      - Player data management
      - Server-side economy and inventory
      - Moderation tooling
      - Community management
      - Analytics integration
    solutions:
      - Game Development Platform
      - Creator Tooling
      - Developer Platform
common:
  - type: Website
    url: https://www.roblox.com
  - type: DeveloperPortal
    url: https://create.roblox.com
  - type: Documentation
    url: https://create.roblox.com/docs
  - type: DevForum
    url: https://devforum.roblox.com
  - type: GitHub
    url: https://github.com/Roblox
  - type: Blog
    url: https://blog.roblox.com
  - type: PrivacyPolicy
    url: https://www.roblox.com/info/privacy
  - type: TermsOfService
    url: https://en.help.roblox.com/hc/en-us/articles/115004647846
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/json-ld/roblox-engine-api-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/roblox-engine-api/refs/heads/main/vocabulary/roblox-engine-api-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
