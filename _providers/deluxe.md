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
- description: The Deluxe Corporation API provides access to platform services and data for enterprise integration and automation.
  name: Deluxe Corporation API
  slug: deluxe-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deluxe-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deluxe
- group: company
  title: ''
  type: Website
  url: https://www.deluxe.com
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.deluxe.com/llms.txt
created: '2026-04-19'
description: Deluxe Corporation is a major US corporation and Fortune 1000 company. The Deluxe Corporation API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Deluxe Finops
  service_category: Payments / Treasury / Business Services
  slug: deluxe-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deluxe.png
layout: provider
modified: '2026-04-19'
name: Deluxe Corporation
nav: Providers
network: true
overview: Deluxe Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Data Analytics, and Marketing.
plans:
- name: Deluxe Plans Pricing
  plan_count: 1
  slug: deluxe-plans-pricing
random_paper: 31
rate_limits:
- limit_count: 1
  name: Deluxe Rate Limits
  slug: deluxe-rate-limits
score:
  band: emerging
  composite: 13.7
  delta: -2.3
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 9.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deluxe/refs/heads/main/screenshots/deluxe-2026-06-20T175905.png
security:
- kind: domain-security
  name: Deluxe Domain Security
  slug: deluxe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: deluxe
tags:
- Payments
- Data Analytics
- Marketing
website: https://www.deluxe.com
---
