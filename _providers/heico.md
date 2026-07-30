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
- description: The HEICO Corporation API provides access to platform services and data for enterprise integration and automation.
  name: HEICO Corporation API
  slug: heico-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/heico-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/heico-corporation
- group: company
  title: ''
  type: Website
  url: https://www.heico.com
created: '2026-04-19'
description: HEICO Corporation is a major US corporation and Fortune 1000 company. The HEICO Corporation API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Heico Finops
  service_category: Aerospace / Defense
  slug: heico-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/heico.png
layout: provider
modified: '2026-04-19'
name: HEICO Corporation
nav: Providers
network: true
overview: HEICO Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Aerospace, Aviation, and Defense.
plans:
- name: Heico Plans Pricing
  plan_count: 1
  slug: heico-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 1
  name: Heico Rate Limits
  slug: heico-rate-limits
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
screenshot: https://raw.githubusercontent.com/api-evangelist/heico/refs/heads/main/screenshots/heico-2026-06-20T182623.png
security:
- kind: domain-security
  name: Heico Domain Security
  slug: heico-domain-security
  summary_line: TLSv1.3 · DMARC
slug: heico
tags:
- Aerospace
- Aviation
- Defense
website: https://www.heico.com
---
