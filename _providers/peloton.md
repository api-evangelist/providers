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
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.4
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Conceptual GraphQL schema for the Peloton connected fitness platform, derived from community reverse-engineering of the internal REST API. Covers authentication, users, subscriptions, hardware devices
  name: Peloton API
  slug: peloton-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/peloton-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/peloton-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/peloton
- group: company
  title: ''
  type: Website
  url: https://www.onepeloton.com/
created: '2026-05-05'
description: A connected fitness company offering stationary bikes, treadmills, rowers, and a digital platform for live and on-demand fitness classes. Peloton pioneered the premium at-home fitness category, blending hardware, software, and instructor-led content into an interactive workout experience available across Peloton equipment and a standalone Peloton App on iOS, Android, web, and connected TV. Peloton does not publish a public developer API, partner portal, or third-party integration program; all API surfaces are internal and only reachable through the consumer apps. Reverse-engineered community libraries exist on GitHub but are unsupported by Peloton.
graphqls:
- description: This is a conceptual GraphQL schema for the Peloton connected fitness platform. Peloton does not publish a public developer API or official GraphQL endpoint. This schema is derived from community reve
  name: Peloton GraphQL Schema
  slug: peloton-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/peloton.png
layout: provider
modified: '2026-05-09'
name: Peloton
nav: Providers
network: true
overview: Peloton publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fitness, Wellness, Connected Fitness, Subscription, and Hardware.
random_paper: 24
score:
  band: emerging
  composite: 17.7
  delta: -1.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 43.3
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.9
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/peloton/refs/heads/main/screenshots/peloton-2026-06-20T191533.png
security:
- kind: domain-security
  name: Peloton Domain Security
  slug: peloton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Peloton Vulnerability Disclosure
  slug: peloton-vulnerability-disclosure
  summary_line: Hackerone
slug: peloton
tags:
- Fitness
- Wellness
- Connected Fitness
- Subscription
- Hardware
- Streaming
- Consumer
website: https://www.onepeloton.com/
---
