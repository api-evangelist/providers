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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: The Waters Corporation API provides access to platform services and data for enterprise integration and automation.
  name: Waters Corporation API
  slug: waters-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/waters-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/waters
- group: company
  title: ''
  type: Website
  url: https://www.waters.com
created: '2026-04-19'
description: Waters Corporation is a major US corporation and Fortune 1000 company. The Waters Corporation API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Waters Finops
  service_category: Laboratory Informatics
  slug: waters-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/waters.png
layout: provider
modified: '2026-04-19'
name: Waters Corporation
nav: Providers
network: true
overview: Waters Corporation publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Laboratory, Instruments, and Analytics.
plans:
- name: Waters Plans Pricing
  plan_count: 1
  slug: waters-plans-pricing
random_paper: 82
rate_limits:
- limit_count: 1
  name: Waters Rate Limits
  slug: waters-rate-limits
score:
  band: emerging
  composite: 14.5
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 14.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/waters/refs/heads/main/screenshots/waters-2026-06-20T201251.png
security:
- kind: domain-security
  name: Waters Domain Security
  slug: waters-domain-security
  summary_line: TLSv1.3 · DMARC
slug: waters
tags:
- Laboratory
- Instruments
- Analytics
website: https://www.waters.com
---
