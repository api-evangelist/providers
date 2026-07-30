---
access_model:
  confidence: medium
  label: Enterprise · Requires approval
  onboarding: approval
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
- description: The TPG Inc API provides access to platform services and data for enterprise integration and automation.
  name: TPG Inc API
  slug: tpg-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tpg-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tpginc
- group: company
  title: ''
  type: Website
  url: https://www.tpg.com
- group: company
  title: ''
  type: Blog
  url: https://www.tpg.com/news-and-insights
created: '2026-04-19'
description: TPG Inc is a major US corporation and Fortune 1000 company. The TPG Inc API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Tpg Finops
  service_category: Alternative Asset Management
  slug: tpg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tpg.png
layout: provider
modified: '2026-04-19'
name: TPG Inc
nav: Providers
network: true
overview: 'TPG Inc publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Private Equity, Alternative Assets, and Investment.


  TPG Inc''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Tpg Plans Pricing
  plan_count: 1
  slug: tpg-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 1
  name: Tpg Rate Limits
  slug: tpg-rate-limits
score:
  band: emerging
  composite: 14.0
  delta: -1.7
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 15.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tpg/refs/heads/main/screenshots/tpg-2026-06-20T195511.png
security:
- kind: domain-security
  name: Tpg Domain Security
  slug: tpg-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tpg
tags:
- Private Equity
- Alternative Assets
- Investment
website: https://www.tpg.com
---
