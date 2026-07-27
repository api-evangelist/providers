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
  scored_at: '2026-07-27'
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
random_paper: 35
rate_limits:
- limit_count: 1
  name: Deluxe Rate Limits
  slug: deluxe-rate-limits
score:
  band: emerging
  composite: 16.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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
