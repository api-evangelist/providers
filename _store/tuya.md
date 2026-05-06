---
aid: tuya
name: Tuya
description: 'Tuya Smart is a global leading AI cloud platform service provider (NYSE: TUYA; HKEX: 2391) that enables IoT device manufacturers, solution providers, and app developers to build smart home and industrial IoT applications. The platform provides APIs for device management, smart home management, scene automation, data analytics, and industry-specific integrations across smart home, energy, security, and industrial verticals. Tuya operates six global data centers and handles over 100 million concurrent requests.'
type: Contract
access: 3rd-Party
image: https://images.tuya.com/smart/tuya-logo.png
tags:
  - IoT
  - Smart Home
  - Devices
  - Cloud Platform
  - Automation
  - Industrial IoT
  - Device Management
created: '2025-03-01'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tuya/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tuya:device-management
    name: Tuya Device Management API
    description: The Tuya Device Management API provides endpoints to query, control, and manage IoT devices registered to a Tuya cloud project. Capabilities include device information retrieval, factory reset, device renaming, sub-device listing, operation log queries, and user-device association management.
    humanURL: https://developer.tuya.com/en/docs/cloud/device-management?id=K9g6rfntdz78a
    baseURL: https://openapi.tuyaus.com
    tags:
      - Devices
      - IoT
      - Device Management
    properties:
      - type: Documentation
        url: https://developer.tuya.com/en/docs/cloud/device-management?id=K9g6rfntdz78a
      - type: Getting Started
        url: https://developer.tuya.com/en/docs/iot/quick-start1?id=K95ztz9u9t89n
  - aid: tuya:smart-home
    name: Tuya Smart Home API
    description: The Tuya Smart Home API provides management capabilities for smart home deployments, including home and room management, device grouping, scene automation (tap-to-run and automation rules), member management, and data services. Enables developers to build full-featured smart home applications.
    humanURL: https://developer.tuya.com/en/docs/cloud/smart_home_paas?id=Kakujwbddm7fv
    baseURL: https://openapi.tuyaus.com
    tags:
      - Smart Home
      - IoT
      - Automation
      - Scene Management
    properties:
      - type: Documentation
        url: https://developer.tuya.com/en/docs/cloud/smart_home_paas?id=Kakujwbddm7fv
  - aid: tuya:authorization
    name: Tuya Authorization API
    description: The Tuya Authorization API handles authentication for cloud-to-cloud integrations. Supports HMAC-SHA256 request signing using Access ID and Access Secret credentials. Provides token management endpoints for obtaining, refreshing, and revoking access tokens. Supports both cloud authorization (server-to-server) and app authorization (user-scoped) modes.
    humanURL: https://developer.tuya.com/en/docs/iot/guide-explanation?id=Ke0wpiw0dwxun
    baseURL: https://openapi.tuyaus.com
    tags:
      - Authentication
      - Authorization
      - Tokens
    properties:
      - type: Documentation
        url: https://developer.tuya.com/en/docs/iot/guide-explanation?id=Ke0wpiw0dwxun
      - type: API Reference
        url: https://developer.tuya.com/en/docs/iot/api-reference?id=Ka7qb7vhber64
  - aid: tuya:industry
    name: Tuya Industry API
    description: The Tuya Industry API provides enterprise IoT capabilities for non-consumer deployments including industrial device registration, device management, status queries, device control, user management, and asset management. Designed for B2B scenarios in real estate, energy, manufacturing, and facilities management.
    humanURL: https://developer.tuya.com/en/docs/cloud
    baseURL: https://openapi.tuyaus.com
    tags:
      - Industrial IoT
      - Enterprise
      - Asset Management
    properties:
      - type: Documentation
        url: https://developer.tuya.com/en/docs/cloud
common:
  - type: Website
    url: https://developer.tuya.com/en/
  - type: Documentation
    url: https://developer.tuya.com/en/docs/cloud/
  - type: Sign Up
    url: https://auth.tuya.com/
  - type: Getting Started
    url: https://developer.tuya.com/en/docs/iot/quick-start1?id=K95ztz9u9t89n
  - type: API Explorer
    url: https://developer.tuya.com/en/docs/cloud
  - type: GitHub Organization
    url: https://github.com/tuya
  - type: Authentication
    url: https://developer.tuya.com/en/docs/iot/guide-explanation?id=Ke0wpiw0dwxun
  - type: Terms of Service
    url: https://developer.tuya.com/en/docs/iot/compliance?id=Ka9t0qa3qihn3
  - type: Portal
    url: https://iot.tuya.com/
  - type: OpenAPI
    url: openapi/tuya-device-management-openapi.yml
  - type: JSONSchema
    url: json-schema/tuya-device-schema.json
  - type: JSONSchema
    url: json-schema/tuya-command-schema.json
  - type: JSONLD
    url: json-ld/tuya-context.jsonld
  - type: Spectral Rules
    url: rules/tuya-rules.yml
  - type: Vocabulary
    url: vocabulary/tuya-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
