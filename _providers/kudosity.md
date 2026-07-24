---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 17.3
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Current v2 REST API covering SMS, MMS, RCS and Webhooks. Authenticated via x-api-key header.
  name: Transmit Message API
  slug: transmit-message-api
- description: Legacy/classic REST API for SMS. Authenticated via HTTP Basic Authentication (API key + secret).
  name: Transmit SMS API
  slug: transmit-sms-api
artifact_total: 2
created: '2026-07-11'
description: Business messaging platform for SMS, MMS, RCS and WhatsApp (formerly Burst SMS / TransmitSMS). Exposes two public REST APIs, OpenAPI contracts, a hosted MCP server, llms.txt files, and published agent plugins.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kudosity.png
layout: provider
modified: '2026-07-11'
name: Kudosity
nav: Providers
network: true
overview: 'Kudosity publishes 2 APIs on the [APIs.io](https://apis.io/) network: Transmit Message API and Transmit SMS API. Tagged areas include Messaging, SMS, MMS, RCS, and WhatsApp.'
random_paper: 25
score:
  band: emerging
  composite: 17.9
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 37.7
    developer_ergonomics: 0.0
    discoverability: 85.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
slug: kudosity
tags:
- Messaging
- SMS
- MMS
- RCS
- WhatsApp
- Communications
- CPaaS
- Webhooks
- MCP
- Agent-native
---
