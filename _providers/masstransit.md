---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: MassTransit provides a consistent abstraction on top of message transports like RabbitMQ, Azure Service Bus, and Amazon SQS, with support for sagas, state machines, routing slip activities, and a stan
  name: MassTransit Messaging Framework
  slug: masstransit-messaging
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/masstransit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://masstransit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://masstransit.io/documentation/concepts
- group: start
  title: ''
  type: GettingStarted
  url: https://masstransit.io/quick-starts
- group: build
  title: ''
  type: GitHub
  url: https://github.com/MassTransit/MassTransit
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/rNpQgYn
- group: other
  title: ''
  type: NuGet
  url: https://www.nuget.org/packages/MassTransit
created: '2026-03-26'
description: MassTransit is a free, open source distributed application framework for .NET that makes it easy to create applications and services that leverage message-based, loosely-coupled asynchronous communication for higher availability, reliability, and scalability.
finops:
- name: Masstransit Finops
  service_category: API
  slug: masstransit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/masstransit.png
json_schemas:
- name: MassTransit Message Envelope
  property_count: 15
  slug: masstransit-message-envelope
- name: MassTransit Saga State
  property_count: 8
  slug: masstransit-saga-state
layout: provider
modified: '2026-04-28'
name: MassTransit
nav: Providers
network: true
overview: 'MassTransit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, Event-Driven, Message Bus, Messaging, and Open Source.


  The MassTransit catalog on APIs.io includes 1 Spectral governance ruleset.


  MassTransit''s developer surface includes documentation, getting-started guide, GitHub presence, and 4 more developer resources.'
plans:
- name: Masstransit Plans Pricing
  plan_count: 3
  slug: masstransit-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Masstransit Rate Limits
  slug: masstransit-rate-limits
rules:
- name: MassTransit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: masstransit-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.8
  delta: -8.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 16.1
    developer_ergonomics: 19.6
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 38.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 8.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/masstransit/refs/heads/main/screenshots/masstransit-2026-06-20T185019.png
security:
- kind: domain-security
  name: Masstransit Domain Security
  slug: masstransit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: masstransit
tags:
- .NET
- Event-Driven
- Message Bus
- Messaging
- Open Source
- Sagas
website: https://masstransit.io/
---
