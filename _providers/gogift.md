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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Do you need a technology solution to easily order and send digital gift cards? GoGift has a gift card API for that. Instantly send gift cards with a simple API integration!
  name: GoGift
  slug: gogift
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gogift-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GoGift
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gogift
- group: company
  title: ''
  type: Website
  url: https://www.global.gogift.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.global.gogift.com/gift-card-api
- group: company
  title: ''
  type: Blog
  url: https://www.global.gogift.com/blog-feed.xml
created: '2025-02-08'
description: Do you need a technology solution to easily order and send digital gift cards? GoGift has a gift card API for that. Instantly send gift cards with a simple API integration!
finops:
- name: Gogift Finops
  service_category: API
  slug: gogift-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gogift.png
layout: provider
modified: '2026-04-28'
name: GoGift
nav: Providers
network: true
overview: 'GoGift publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Gift Cards.


  GoGift''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
plans:
- name: Gogift Plans Pricing
  plan_count: 3
  slug: gogift-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 5
  name: Gogift Rate Limits
  slug: gogift-rate-limits
score:
  band: minimal
  composite: 10.9
  delta: -8.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 18.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/gogift/refs/heads/main/screenshots/gogift-2026-06-20T181946.png
security:
- kind: domain-security
  name: Gogift Domain Security
  slug: gogift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gogift
tags:
- Gift Cards
website: https://www.global.gogift.com/
---
