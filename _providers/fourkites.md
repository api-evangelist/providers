---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: FourKites Tracking API provides shipment creation, status, and ETA updates plus carrier integrations across modes (TL, LTL, ocean, rail, parcel) for real-time supply chain visibility.
  name: FourKites Tracking API
  slug: fourkites-tracking-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fourkites-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FourKites
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fourkites-inc
- group: company
  title: ''
  type: Website
  url: https://www.fourkites.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fourkites.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/fourkites-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fourkites-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fourkites-finops.yml
created: '2026-05-08'
description: FourKites is a real-time supply chain visibility platform that tracks shipments and assets across road, rail, ocean, and yard modes worldwide.
finops:
- name: Fourkites Finops
  service_category: Logistics
  slug: fourkites-finops
graphqls:
- description: FourKites is a real-time supply chain visibility platform that tracks shipments and assets across road, rail, ocean, and yard modes worldwide. The GraphQL schema below is a conceptual representation o
  name: FourKites GraphQL Schema
  slug: fourkites-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fourkites.png
layout: provider
modified: '2026-05-08'
name: FourKites
nav: Providers
network: true
overview: 'FourKites publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Logistics, Supply Chain Visibility, Tracking, Freight, and ETA.


  FourKites'' developer surface includes documentation and 7 more developer resources.'
plans:
- name: Fourkites Plans Pricing
  plan_count: 1
  slug: fourkites-plans-pricing
random_paper: 64
rate_limits:
- limit_count: 1
  name: Fourkites Rate Limits
  slug: fourkites-rate-limits
score:
  band: thin
  composite: 28.9
  delta: 10.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 48.1
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 18.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/fourkites/refs/heads/main/screenshots/fourkites-2026-06-20T181456.png
security:
- kind: domain-security
  name: Fourkites Domain Security
  slug: fourkites-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fourkites
tags:
- Logistics
- Supply Chain Visibility
- Tracking
- Freight
- ETA
website: https://www.fourkites.com/
---
