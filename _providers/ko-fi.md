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
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.7
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: Outbound webhook that Ko-fi HTTP POSTs to a URL you configure whenever a payment happens on your Ko-fi page. The single POST body is form-encoded with a "data" field containing a JSON payload; a "type
  name: Ko-fi Webhook
  slug: ko-fi-webhook
artifact_total: 7
asyncapis:
- description: 'AsyncAPI 2.6 description of Ko-fi''s **only** documented developer surface: an **outbound payment webhook**. Ko-fi does **not** publish a public REST API. There is no request/response endpoint to read,'
  name: Ko-fi Payment Webhook (Outbound HTTP POST)
  slug: ko-fi-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ko-fi-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ko-fi
- group: company
  title: ''
  type: Website
  url: https://ko-fi.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.ko-fi.com/hc/en-us/articles/360004162298-Does-Ko-fi-have-an-API-or-webhook
- group: commercial
  title: ''
  type: Plans
  url: plans/ko-fi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ko-fi-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ko-fi-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.ko-fi.com
created: '2026-07-05'
description: 'Ko-fi is a creator monetization platform where fans support creators through one-off tips ("buy me a coffee"), recurring memberships, digital and physical shop products, and paid commissions. Ko-fi charges 0% platform fee on tips and donations. Its developer surface is intentionally narrow and integration-only: Ko-fi does not publish a public REST API. Instead it offers an outbound WEBHOOK that HTTP POSTs payment notifications (donations, subscription / membership payments, shop orders, and commissions) to a URL you configure on your Ko-fi webhooks page. Each POST is application/x-www-form-urlencoded with a single "data" field carrying a JSON payload, and includes a verification_token so you can confirm the request originated from Ko-fi. The webhook is one-way (Ko-fi to your endpoint) and fires only when a payment happens - there is no request/response API to read, create, or manage donations, members, or orders.'
finops:
- name: Ko Fi Finops
  service_category: Creator Monetization and Payments
  slug: ko-fi-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ko-fi.png
layout: provider
modified: '2026-07-05'
name: Ko-fi
nav: Providers
network: true
overview: 'Ko-fi publishes 1 API on the [APIs.io](https://apis.io/) network: Webhook. Tagged areas include Creator Economy, Donations, Tips, Memberships, and Shop.


  The Ko-fi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Ko-fi''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
plans:
- name: Ko Fi Plans Pricing
  plan_count: 2
  slug: ko-fi-plans-pricing
random_paper: 110
rate_limits:
- limit_count: 2
  name: Ko Fi Rate Limits
  slug: ko-fi-rate-limits
rules:
- name: Ko-fi API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: ko-fi-asyncapi-spectral-rules
score:
  band: thin
  composite: 30.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.6
    developer_ergonomics: 10.9
    discoverability: 59.3
    governance: 41.7
    operational_transparency: 21.1
  previous_composite: 30.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ko-fi/refs/heads/main/screenshots/ko-fi-2026-07-25T224019.png
security:
- kind: domain-security
  name: Ko Fi Domain Security
  slug: ko-fi-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: ko-fi
tags:
- Creator Economy
- Donations
- Tips
- Memberships
- Shop
- Payments
- Webhooks
- Creator Monetization
website: https://ko-fi.com
---
