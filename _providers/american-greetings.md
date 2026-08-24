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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: The American Greetings API provides access to platform services and data for enterprise integration and automation.
  name: American Greetings API
  slug: american-greetings-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/american-greetings-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/american-greetings
- group: company
  title: ''
  type: Website
  url: https://www.americangreetings.com
created: '2026-04-19'
description: American Greetings is a major US corporation and Fortune 1000 company. The American Greetings API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: American Greetings Finops
  service_category: Consumer Goods / Retail
  slug: american-greetings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/american-greetings.png
layout: provider
modified: '2026-04-19'
name: American Greetings
nav: Providers
network: true
overview: American Greetings publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Greeting Cards, Gift Wrap, and Celebration.
plans:
- name: American Greetings Plans Pricing
  plan_count: 1
  slug: american-greetings-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 1
  name: American Greetings Rate Limits
  slug: american-greetings-rate-limits
score:
  band: minimal
  composite: 5.8
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/american-greetings/refs/heads/main/screenshots/american-greetings-2026-06-20T171917.png
security:
- kind: domain-security
  name: American Greetings Domain Security
  slug: american-greetings-domain-security
  summary_line: TLSv1.3 · DMARC
slug: american-greetings
tags:
- Greeting Cards
- Gift Wrap
- Celebration
website: https://www.americangreetings.com
---
