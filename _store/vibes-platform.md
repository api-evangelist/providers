---
aid: vibes-platform
url: https://raw.githubusercontent.com/api-evangelist/vibes-platform/refs/heads/main/apis.yml
apis:
  - aid: vibes-platform:vibes-platform-api
    name: Vibes Platform API
    tags:
      - Mobile Marketing
      - Push Notifications
      - SMS
      - Broadcast
      - Acquisition
      - Subscription Management
      - Wallet Passes
    humanURL: https://developer-platform.vibes.com/
    baseURL: https://public-api.vibescm.com
    properties:
      - url: https://developer-platform.vibes.com/reference/our-apis
        type: Documentation
      - url: https://developer-platform.vibes.com/reference/broadcast-api-1
        type: Reference
      - url: https://developer-platform.vibes.com/reference/acquisition-campaign-api-1
        type: Reference
      - url: https://developer-platform.vibes.com/reference/subscription-list-api
        type: Reference
      - url: https://developer-platform.vibes.com/reference/callbacks
        type: Reference
      - url: https://developer-platform.vibes.com/reference/technical-details
        type: Reference
      - url: openapi/vibes-platform-openapi.yml
        type: OpenAPI
      - url: rules/vibes-platform-rules.yml
        type: SpectralRuleset
    description: The Vibes Platform API provides programmatic access to broadcast messaging (SMS and push notifications), acquisition workflows, subscription list management, wallet pass management, and event-triggered message capabilities. Broadcasts are delivered to subscribers within your mobile contact book. Authentication uses HTTP Basic Auth with Base64-encoded credentials. The US environment base URL is https://public-api.vibescm.com and the EU environment base URL is https://public-api.eu.vibes.com.
  - aid: vibes-platform:vibes-connect-api
    name: Vibes Connect API
    tags:
      - SMS
      - MMS
      - Aggregation
      - Messaging
      - Mobile
    humanURL: https://developer-aggregation.vibes.com
    baseURL: https://messageapi.vibesapps.com
    properties:
      - url: https://developer-aggregation.vibes.com
        type: Documentation
      - url: https://developer-aggregation.vibes.com/reference/http-message-api
        type: Reference
      - url: openapi/vibes-connect-openapi.yml
        type: OpenAPI
    description: 'Vibes Connect provides aggregation-layer APIs for sending and receiving SMS and MMS messages via HTTP calls. Three APIs are offered: the HTTP Message API for SMS, the SMPP Gateway API for persistent SMPP bindings, and the MMS Message API using MM7 Protocol. Vibes is a Tier 1 provider with direct connections to Verizon, AT&T, T-Mobile, and regional carriers. US SMS endpoint: https://messageapi.vibesapps.com; US MMS endpoint: https://messageapi-mms.vibesapps.com.'
name: Vibes Platform
tags:
  - Mobile Marketing
  - Mobile Messaging
  - Push Notifications
  - SMS
  - MMS
  - Broadcast Messaging
  - Acquisition Campaigns
  - Subscription Management
  - Wallet Passes
  - RCS
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-11-14'
modified: '2026-05-03'
position: Consuming
description: Vibes is a mobile engagement platform that provides APIs for SMS messaging, push notifications, RCS for Business, and mobile marketing campaigns. The platform APIs support broadcast messaging, event-triggered messages, acquisition workflows, subscription list management, wallet pass management, and callback notifications for opt-ins and delivery status. Vibes operates as a Tier 1 provider with direct carrier connections in the US and Canada.
common:
  - url: https://developer-platform.vibes.com/
    name: Vibes Platform Developer Portal
    type: Portal
    description: Primary developer portal for Vibes Platform APIs.
  - url: https://developer-platform.vibes.com/reference/our-apis
    name: Our APIs - Vibes Platform
    type: Documentation
    description: Overview of all Vibes Platform APIs.
  - url: https://developer-aggregation.vibes.com
    name: Vibes Connect Developer Portal
    type: Portal
    description: Developer portal for Vibes Connect aggregation APIs (SMS/MMS).
  - url: https://developer-rbm.vibes.com/
    name: Vibes RCS for Business Developer Portal
    type: Portal
    description: Developer portal for Vibes RCS for Business (Rich Communication Services).
  - url: https://www.vibes.com/
    name: Vibes - Mobile Engagement Platform
    type: Website
    description: Official website for Vibes mobile engagement platform.
  - url: https://www.vibes.com/platform/integrations
    name: Vibes Platform Integrations
    type: Integrations
    description: Integration partners and connectors for the Vibes platform.
features:
  - Broadcast SMS and MMS messaging
  - Push notification delivery
  - Acquisition campaign management
  - Subscription list management
  - Wallet pass creation and management
  - Event-triggered messages
  - File-triggered messages
  - Callback registrations for opt-in and delivery status
  - RCS for Business (Rich Communication Services)
  - Rate limiting with 429 Too Many Requests responses
  - US and EU environment support
  - HTTP Basic Authentication
  - Direct Tier 1 carrier connections (AT&T, Verizon, T-Mobile)
integrations:
  - Salesforce Marketing Cloud
  - Adobe Campaign
  - Oracle Eloqua
  - Marketo
artifacts:
  - url: openapi/vibes-platform-openapi.yml
    type: OpenAPI
    name: Vibes Platform OpenAPI
  - url: openapi/vibes-connect-openapi.yml
    type: OpenAPI
    name: Vibes Connect OpenAPI
  - url: rules/vibes-platform-rules.yml
    type: SpectralRuleset
    name: Vibes Platform Spectral Rules
  - url: capabilities/mobile-messaging.yaml
    type: NaftikoCapability
    name: Vibes Mobile Messaging Capability
  - url: capabilities/shared/vibes-platform.yaml
    type: NaftikoCapability
    name: Vibes Platform Shared Capability
  - url: capabilities/shared/vibes-connect.yaml
    type: NaftikoCapability
    name: Vibes Connect Shared Capability
  - url: json-schema/vibes-platform-broadcast-schema.json
    type: JSONSchema
    name: Broadcast Schema
  - url: json-schema/vibes-platform-person-schema.json
    type: JSONSchema
    name: Person Schema
  - url: json-schema/vibes-platform-subscription-list-schema.json
    type: JSONSchema
    name: Subscription List Schema
  - url: json-ld/vibes-platform-context.jsonld
    type: JSONLDContext
    name: Vibes Platform JSON-LD Context
  - url: vocabulary/vibes-platform-vocabulary.yml
    type: Vocabulary
    name: Vibes Platform Vocabulary
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
