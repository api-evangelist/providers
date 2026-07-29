---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
- description: The Trex Company API provides access to platform services and data for enterprise integration and automation.
  name: Trex Company API
  slug: trex-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trex-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trex-company
- group: company
  title: ''
  type: Website
  url: https://www.trex.com
created: '2026-04-19'
description: Trex Company is a major US corporation and Fortune 1000 company. The Trex Company API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Trex Finops
  service_category: Building Products
  slug: trex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trex.png
layout: provider
modified: '2026-04-19'
name: Trex Company
nav: Providers
network: true
overview: Trex Company publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Composite Decking, Outdoor, and Building Products.
plans:
- name: Trex Plans Pricing
  plan_count: 1
  slug: trex-plans-pricing
random_paper: 51
rate_limits:
- limit_count: 1
  name: Trex Rate Limits
  slug: trex-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: -2.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 16.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/trex/refs/heads/main/screenshots/trex-2026-06-20T195701.png
security:
- kind: domain-security
  name: Trex Domain Security
  slug: trex-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trex
tags:
- Composite Decking
- Outdoor
- Building Products
website: https://www.trex.com
---
