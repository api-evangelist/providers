---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Chargetrip Agentic Access
  operation_count: 1
  slug: chargetrip-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Chargetrip — 1 operation(s) for graphql.
  name: Chargetrip GraphQL API
  slug: chargetrip-graphql-api
artifact_total: 12
asyncapis:
- description: AsyncAPI 2.6 description of Chargetrip's **real-time route updates** surface. Unlike the synchronous query/mutation surface (HTTP POST to `https://api.chargetrip.io/graphql`, modeled in `openapi/charg
  name: Chargetrip Route Updates (GraphQL Subscriptions over WebSocket)
  slug: chargetrip-asyncapi
collections:
- collection_type: open
  name: Chargetrip GraphQL API
  slug: open-chargetrip
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/chargetrip-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chargetrip-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chargetrip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/chargetrip-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chargetrip
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/chargetrip
- group: company
  title: ''
  type: Website
  url: https://www.chargetrip.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chargetrip.com
- group: commercial
  title: ''
  type: Plans
  url: plans/chargetrip-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/chargetrip-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chargetrip-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/chargetrip
created: '2026-06-21'
description: Chargetrip provides an EV routing GraphQL API used by automakers and e-mobility services. It plans range-aware routes with charging stops, exposes a curated charge station database, an EV vehicle/consumption database, isolines (reachability), and operator data, with real-time route updates delivered over WebSocket subscriptions.
finops:
- name: Chargetrip Finops
  service_category: Maps and Routing
  slug: chargetrip-finops
graphqls:
- description: The [Chargetrip](https://www.chargetrip.com) API is a **native GraphQL API** for
  name: Chargetrip GraphQL API
  slug: chargetrip-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chargetrip.png
layout: provider
modified: '2026-06-21'
name: Chargetrip
nav: Providers
network: true
overview: 'Chargetrip publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include EV, Routing, Charging Stations, GraphQL, and Mobility.


  The Chargetrip catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Chargetrip''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Chargetrip Plans Pricing
  plan_count: 3
  slug: chargetrip-plans-pricing
random_paper: 81
rate_limits:
- limit_count: 4
  name: Chargetrip Rate Limits
  slug: chargetrip-rate-limits
rules:
- name: Chargetrip API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: chargetrip-asyncapi-spectral-rules
score:
  band: developing
  composite: 46.6
  delta: -4.1
  facets:
    commercial_clarity: 39.5
    contract_quality: 70.8
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 41.7
    operational_transparency: 36.8
  previous_composite: 50.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chargetrip/refs/heads/main/screenshots/chargetrip-2026-07-25T205058.png
security:
- kind: authentication
  name: Chargetrip Authentication
  slug: chargetrip-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Chargetrip Domain Security
  slug: chargetrip-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chargetrip Vulnerability Disclosure
  slug: chargetrip-vulnerability-disclosure
  summary_line: disclosure policy published
slug: chargetrip
tags:
- EV
- Routing
- Charging Stations
- GraphQL
- Mobility
website: https://www.chargetrip.com
---
