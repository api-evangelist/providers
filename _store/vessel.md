---
aid: vessel
name: Vessel
description: 'Vessel is a developer-first embedded integrations platform that enables product teams to add native integrations to their applications. It provides unified API abstractions, actions APIs, and passthrough APIs to connect with CRM, sales engagement, marketing automation, chat, and dialer tools while managing authentication, rate limits, and data normalization. The platform supports OAuth and API-key authentication via a drop-in React UI component (Vessel Link), with two API surfaces: api.vessel.dev for the newer GTM integrations platform and api.vessel.land for the CRM-focused platform.'
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CRM
  - Embedded Integrations
  - GTM
  - Integrations
  - iPaaS
  - Sales Engagement
  - Unified API
url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/apis.yml
created: '2026-05-03'
modified: '2026-05-03'
specificationVersion: '0.19'
apis:
  - aid: vessel:platform-api
    name: Vessel Platform API
    description: The Vessel Platform API (api.vessel.dev) provides the core integration platform capabilities including authentication session management, access token exchange, connection lifecycle management, integration listing, passthrough API calls, and webhook management. Authentication uses the x-vessel-api-token header for server-side requests plus x-vessel-access-token for user connection scoped operations.
    humanURL: https://www.vessel.dev/
    tags:
      - Authentication
      - Connections
      - Integrations
      - Passthrough
      - Webhooks
    properties:
      - type: Documentation
        url: https://docs.vessel.dev/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/openapi/vessel-platform-openapi.yml
      - type: NaftikoCapability
        url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/capabilities/crm-integration.yaml
      - type: SpectralRuleset
        url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/rules/vessel-api-rules.yml
      - type: GitHubRepository
        url: https://github.com/vesselapi/all-api-docs
  - aid: vessel:crm-api
    name: Vessel CRM API
    description: The Vessel CRM API (api.vessel.land) provides unified CRM operations across Salesforce, HubSpot, Zoho, Pipedrive, Close, Freshsales, Microsoft Dynamics, Affinity, monday.com, and Freshdesk. The API normalizes contacts, deals, accounts, leads, notes, tasks, emails, calls, events, event attendees, users, and lists. Authentication uses vessel-api-token header and accessToken query parameter.
    humanURL: https://www.vessel.dev/unified-apis/crm
    tags:
      - Accounts
      - CRM
      - Contacts
      - Deals
      - Leads
      - Unified API
    properties:
      - type: Documentation
        url: https://docs.vessel.dev/
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/openapi/vessel-crm-openapi.yml
      - type: JSONSchema
        url: https://raw.githubusercontent.com/api-evangelist/vessel/refs/heads/main/json-schema/vessel-contact-schema.json
      - type: GitHubRepository
        url: https://github.com/vesselapi/all-api-docs
  - aid: vessel:actions-api
    name: Vessel Actions API
    description: The Vessel Actions API provides pre-built, validated actions for common integration operations across CRM, sales engagement, marketing automation, chat, and dialer systems. Actions validate API responses and request inputs, standardize data types (ISO dates, string IDs), and abstract downstream provider quirks.
    humanURL: https://www.vessel.dev/
    tags:
      - Actions
      - Automation
      - Integrations
      - Validation
    properties:
      - type: Documentation
        url: https://www.vessel.dev/
      - type: GitHubRepository
        url: https://github.com/vesselapi/integrations
  - aid: vessel:unified-api
    name: Vessel Unified API
    description: The Vessel Unified API provides a standardized interface across integrations, abstracting away the differences between third-party APIs to provide a consistent developer experience. Supports CRM, sales engagement, chat, marketing automation, and dialer categories.
    humanURL: https://www.vessel.dev/
    tags:
      - CRM
      - Chat
      - Dialers
      - Marketing Automation
      - Normalized
      - Sales Engagement
      - Unified API
    properties:
      - type: Documentation
        url: https://www.vessel.dev/
common:
  - url: https://www.vessel.dev/
    name: Vessel - Embedded Integrations Platform
    type: Website
    description: Vessel's main website for the developer-first embedded integrations platform.
  - url: https://docs.vessel.dev/
    name: Vessel API Documentation
    type: Documentation
    description: Full documentation for the Vessel APIs, SDKs, and integrations.
  - url: https://www.vessel.dev/integrations
    name: Vessel Integrations
    type: Integrations
    description: Full catalog of supported integrations across CRM, engagement, chat, dialer, and marketing automation.
  - url: https://github.com/vesselapi
    name: Vessel GitHub Organization
    type: GitHubOrganization
    description: Vessel's GitHub organization hosting the integrations library, documentation, client SDK, and example applications.
  - url: https://github.com/vesselapi/integrations
    name: Vessel Integrations Library
    type: GitHubRepository
    description: Open-source integrations library defining actions, authentication, and passthrough APIs for all supported integrations.
  - url: https://github.com/vesselapi/client-sdk
    name: Vessel Client SDK
    type: SDK
    description: Client-side SDK providing the Vessel Link modal for user authentication with third-party integrations.
  - url: https://www.npmjs.com/package/@vesselapi/sdk
    name: Vessel Node.js SDK (npm)
    type: SDK
    description: Official Vessel Node.js SDK for server-side API calls.
  - url: https://www.npmjs.com/package/@vesselapi/react-vessel-link
    name: Vessel React Link Component (npm)
    type: SDK
    description: React component for embedding the Vessel authentication modal.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
