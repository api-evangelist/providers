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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/event-sourcing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://martinfowler.com/eaaDev/EventSourcing.html
created: '2025-01-01'
description: Event sourcing is an architectural pattern where state changes are stored as a sequence of immutable events rather than just the current state. Instead of storing only the current state of data, event sourcing stores all changes as a log of events, enabling complete audit trails, temporal queries, and event-driven projections.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/event-sourcing.png
layout: provider
modified: '2026-03-16'
name: Event Sourcing
nav: Providers
network: true
overview: Event Sourcing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Architecture, CQRS, Distributed Systems, and Event Sourcing.
random_paper: 25
score:
  band: minimal
  composite: 4.8
  delta: -0.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/event-sourcing/refs/heads/main/screenshots/event-sourcing-2026-06-20T180857.png
security:
- kind: domain-security
  name: Event Sourcing Domain Security
  slug: event-sourcing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: event-sourcing
tags:
- Architecture
- CQRS
- Distributed Systems
- Event Sourcing
website: https://martinfowler.com/eaaDev/EventSourcing.html
---
