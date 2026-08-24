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
- description: The Piper Sandler Companies API provides access to platform services and data for enterprise integration and automation.
  name: Piper Sandler Companies API
  slug: piper-sandler-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/piper-sandler-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pipersandler
- group: company
  title: ''
  type: Website
  url: https://www.pipersandler.com
created: '2026-04-19'
description: Piper Sandler Companies is a major US corporation and Fortune 1000 company. The Piper Sandler Companies API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Piper Sandler Finops
  service_category: Capital Markets
  slug: piper-sandler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/piper-sandler.png
layout: provider
modified: '2026-04-19'
name: Piper Sandler Companies
nav: Providers
network: true
overview: Piper Sandler Companies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Investment Banking and Institutional Brokerage.
plans:
- name: Piper Sandler Plans Pricing
  plan_count: 1
  slug: piper-sandler-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 1
  name: Piper Sandler Rate Limits
  slug: piper-sandler-rate-limits
score:
  band: minimal
  composite: 5.7
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
  previous_composite: 5.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/piper-sandler/refs/heads/main/screenshots/piper-sandler-2026-06-20T191727.png
security:
- kind: domain-security
  name: Piper Sandler Domain Security
  slug: piper-sandler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: piper-sandler
tags:
- Investment Banking
- Institutional Brokerage
website: https://www.pipersandler.com
---
