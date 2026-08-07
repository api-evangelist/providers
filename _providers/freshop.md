---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Live REST API serving grocery store and product data to Freshop-powered storefronts. Numeric path versioning (/1/, /2/); app_key query-parameter authentication; flat JSON error envelope.
  name: Freshop API
  slug: freshop-api
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://freshop.com
- group: operate
  title: ''
  type: Support
  url: https://freshop.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ncr.com/privacy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/freshop-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freshop-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freshop-llms.txt
created: '2026-07-17'
description: Freshop is an eCommerce platform purpose-built for grocery and specialty retail, now part of NCR Voyix. It powers branded online storefronts, mobile shopping, order fulfillment, pickup, and delivery for independent and regional grocers, and integrates third-party services for loyalty, coupons, email, SMS, and fulfillment. Freshop exposes a live REST API at api.freshop.com that serves store and product data to Freshop-powered storefronts and apps, authenticated with an application key (app_key) query-string parameter and versioned by a numeric path segment.
image: https://freshop.com/favicon.ico
layout: provider
modified: '2026-07-19'
name: Freshop
nav: Providers
network: true
overview: 'Freshop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Grocery, eCommerce, Retail, and Online Shopping.


  Freshop''s developer surface includes support and 5 more developer resources.'
random_paper: 81
score:
  band: minimal
  composite: 11.7
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 4.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/freshop/refs/heads/main/screenshots/freshop-2026-07-25T215203.png
security:
- kind: authentication
  name: Freshop Authentication
  slug: freshop-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Freshop Domain Security
  slug: freshop-domain-security
  summary_line: TLSv1.3 · HSTS
slug: freshop
tags:
- Company
- Grocery
- eCommerce
- Retail
- Online Shopping
- Fulfillment
- Delivery
- NCR Voyix
website: https://freshop.com
---
