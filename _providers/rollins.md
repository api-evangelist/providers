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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: The Rollins API provides access to platform services and data for enterprise integration and automation.
  name: Rollins API
  slug: rollins-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rollins-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.rollins.com/investors/press-releases/rss
- group: company
  title: ''
  type: Website
  url: https://www.rollins.com
created: '2026-04-19'
description: Rollins is a major US corporation and Fortune 1000 company. The Rollins API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Rollins Finops
  service_category: Pest Control Services
  slug: rollins-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rollins.png
layout: provider
modified: '2026-04-19'
name: Rollins
nav: Providers
network: true
overview: 'Rollins publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Pest Control and Services.


  Rollins'' developer surface includes engineering blog and 2 more developer resources.'
plans:
- name: Rollins Plans Pricing
  plan_count: 1
  slug: rollins-plans-pricing
random_paper: 75
rate_limits:
- limit_count: 1
  name: Rollins Rate Limits
  slug: rollins-rate-limits
score:
  band: minimal
  composite: 8.8
  delta: -5.2
  facets:
    commercial_clarity: 13.2
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 14.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/rollins/refs/heads/main/screenshots/rollins-2026-06-20T193207.png
security:
- kind: domain-security
  name: Rollins Domain Security
  slug: rollins-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rollins
tags:
- Pest Control
- Services
website: https://www.rollins.com
---
