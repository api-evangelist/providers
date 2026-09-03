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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-02'
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
overview: 'MassTransit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include .NET, Event-Driven, Message Bus, Messaging, and Open-Source.


  The MassTransit catalog on APIs.io includes 1 Spectral governance ruleset.


  MassTransit''s developer surface includes documentation, getting-started guide, GitHub presence, and 4 more developer resources.'
plans:
- name: Masstransit Plans Pricing
  plan_count: 3
  slug: masstransit-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Masstransit Rate Limits
  slug: masstransit-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: MassTransit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: masstransit-jsonschema-spectral-rules
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 7
    catalog_gap: 60.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 13.3
    developer_ergonomics: 26.2
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 13.2
  previous_composite: 20.5
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
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
- Open-Source
- Sagas
website: https://masstransit.io/
---
