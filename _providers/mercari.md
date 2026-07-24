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
  band: human-only
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
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: Partner-only API access for shipping, payment, and integration partners. Not self-serve; access granted under partnership agreements.
  name: Mercari Partner API
  slug: partner-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mercari-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mercari
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mercari-inc-
- group: company
  title: ''
  type: Website
  url: https://www.mercari.com/
- group: other
  title: ''
  type: Developer
  url: https://about.mercari.com/en/business/
- group: commercial
  title: ''
  type: Plans
  url: plans/mercari-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mercari-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mercari-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://about.mercari.com/en/press/news/
created: '2026-05-08'
description: Mercari is a peer-to-peer marketplace for new and used goods, operating in Japan and the United States. Mercari does not maintain a public developer API; integration is restricted to approved partners (e.g., shipping carriers, payment partners) under direct agreements.
finops:
- name: Mercari Finops
  service_category: Marketplace
  slug: mercari-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mercari.png
layout: provider
modified: '2026-05-08'
name: Mercari
nav: Providers
network: true
overview: 'Mercari publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Marketplace, Resale, P2P, and Ecommerce.


  Mercari''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Mercari Plans Pricing
  plan_count: 1
  slug: mercari-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 1
  name: Mercari Rate Limits
  slug: mercari-rate-limits
score:
  band: emerging
  composite: 16.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 16.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mercari/refs/heads/main/screenshots/mercari-2026-06-20T185213.png
security:
- kind: domain-security
  name: Mercari Domain Security
  slug: mercari-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mercari
tags:
- Marketplace
- Resale
- P2P
- Ecommerce
website: https://www.mercari.com/
---
