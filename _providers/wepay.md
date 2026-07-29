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
  url: security/wepay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wepay.com
created: '2026-07-17'
description: WePay is a payments platform, founded in 2008 and backed by 500 Global and Y Combinator, that provided integrated payments (payment processing, merchant onboarding, and payouts) embedded inside software platforms and online marketplaces. WePay was acquired by JPMorgan Chase in 2017 and its capabilities were folded into Chase Integrated Payments (WePay Clear and WePay Link). As of this enrichment pass the standalone WePay developer platform has been decommissioned. developer.wepay.com serves a deleted storage bucket, api.wepay.com is unreachable, www.wepay.com redirects to a dead landing page, and all wepay.com TLS certificates have expired, so no live public API surface remains.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wepay.png
layout: provider
modified: '2026-07-21'
name: WePay
nav: Providers
network: true
overview: WePay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Payment Processing, Platform Payments, Marketplaces, and Fintech.
random_paper: 64
score:
  band: minimal
  composite: 5.7
  delta: -2.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Wepay Domain Security
  slug: wepay-domain-security
  summary_line: DMARC
slug: wepay
tags:
- Payments
- Payment Processing
- Platform Payments
- Marketplaces
- Fintech
- Merchant Onboarding
- Payouts
- Company
website: https://wepay.com
---
