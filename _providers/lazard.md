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
- description: The Lazard API provides access to platform services and data for enterprise integration and automation.
  name: Lazard API
  slug: lazard-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lazard-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lazard
- group: company
  title: ''
  type: Website
  url: https://www.lazard.com
created: '2026-04-19'
description: Lazard is a major US corporation and Fortune 1000 company. The Lazard API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Lazard Finops
  service_category: Financial Services / Advisory
  slug: lazard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lazard.png
layout: provider
modified: '2026-04-19'
name: Lazard
nav: Providers
network: true
overview: Lazard publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Investment Banking, Asset Management, and Financial Advisory.
plans:
- name: Lazard Plans Pricing
  plan_count: 1
  slug: lazard-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 1
  name: Lazard Rate Limits
  slug: lazard-rate-limits
score:
  band: emerging
  composite: 13.5
  delta: -1.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lazard/refs/heads/main/screenshots/lazard-2026-06-20T184339.png
security:
- kind: domain-security
  name: Lazard Domain Security
  slug: lazard-domain-security
  summary_line: TLSv1.2 · DMARC
slug: lazard
tags:
- Investment Banking
- Asset Management
- Financial Advisory
website: https://www.lazard.com
---
