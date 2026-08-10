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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Eventuate Agentic Access
  operation_count: 10
  slug: eventuate-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- description: The Entities API from Eventuate — 2 operation(s) for entities.
  name: Eventuate Entities API
  slug: eventuate-entities-api
- description: The Events API from Eventuate — 1 operation(s) for events.
  name: Eventuate Events API
  slug: eventuate-events-api
- description: The Subscriptions API from Eventuate — 4 operation(s) for subscriptions.
  name: Eventuate Subscriptions API
  slug: eventuate-subscriptions-api
- description: The System API from Eventuate — 1 operation(s) for system.
  name: Eventuate System API
  slug: eventuate-system-api
artifact_total: 10
collections:
- collection_type: open
  name: Eventuate REST API
  slug: open-eventuate-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eventuate-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eventuate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://eventuate.io/
- group: docs
  title: ''
  type: Documentation
  url: https://eventuate.io/docs/general/getting-started.html
- group: start
  title: ''
  type: GettingStarted
  url: https://eventuate.io/exampleapps.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/eventuate-tram
- group: company
  title: ''
  type: Blog
  url: https://eventuate.io/news.html
created: '2026-03-26'
description: Eventuate is a platform for developing transactional microservices using event sourcing and CQRS patterns, providing frameworks for managing distributed data consistency across services without two-phase commit.
finops:
- name: Eventuate Finops
  service_category: API
  slug: eventuate-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/eventuate.png
layout: provider
modified: '2026-05-19'
name: Eventuate
nav: Providers
network: true
overview: 'Eventuate publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Entities API, Events API, Subscriptions API, and 1 more. Tagged areas include CQRS, Distributed Data, Event Sourcing, Event-Driven, and Microservices.


  Eventuate''s developer surface includes documentation, getting-started guide, GitHub presence, engineering blog, and 3 more developer resources.'
plans:
- name: Eventuate Plans Pricing
  plan_count: 3
  slug: eventuate-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Eventuate Rate Limits
  slug: eventuate-rate-limits
score:
  band: thin
  composite: 36.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 36.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eventuate/refs/heads/main/screenshots/eventuate-2026-06-20T180901.png
security:
- kind: domain-security
  name: Eventuate Domain Security
  slug: eventuate-domain-security
  summary_line: TLSv1.3
slug: eventuate
tags:
- CQRS
- Distributed Data
- Event Sourcing
- Event-Driven
- Microservices
- Sagas
website: https://eventuate.io/
---
