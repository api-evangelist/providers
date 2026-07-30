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
- description: Podchaser's GraphQL API provides programmatic access to podcasts, episodes, creators, credits, reviews, and lists across the Podchaser database. Authentication is handled via OAuth-style API tokens an
  name: Podchaser GraphQL API
  slug: podchaser
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podchaser-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podchaser
- group: company
  title: ''
  type: Website
  url: https://www.podchaser.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.podchaser.com/
- group: start
  title: ''
  type: APIPortal
  url: https://www.podchaser.com/api
created: '2025-05-02'
description: Podchaser provides one of the most comprehensive podcast databases, exposed through a GraphQL API designed to drive podcast discovery for listeners, podcasters, brands, and platform partners. The API surface is GraphQL-only and is therefore not represented as an OpenAPI specification in this index.
finops:
- name: Podchaser Finops
  service_category: API
  slug: podchaser-finops
graphqls:
- description: Podchaser's GraphQL API provides programmatic access to podcasts, episodes, creators, credits, reviews, and lists across the Podchaser database. Authentication is handled via OAuth-style API tokens an
  name: Podchaser GraphQL API
  slug: podchaser-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podchaser.png
layout: provider
modified: '2026-04-28'
name: Podchaser
nav: Providers
network: true
overview: 'Podchaser publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Podcasting, Discovery, GraphQL, and Database.


  Podchaser''s developer surface includes documentation and 4 more developer resources.'
plans:
- name: Podchaser Plans Pricing
  plan_count: 3
  slug: podchaser-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 5
  name: Podchaser Rate Limits
  slug: podchaser-rate-limits
score:
  band: emerging
  composite: 19.7
  delta: -2.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Podchaser Domain Security
  slug: podchaser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: podchaser
tags:
- Podcasting
- Discovery
- GraphQL
- Database
website: https://www.podchaser.com/
---
