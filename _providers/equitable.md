---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: An API capability that acts as a digital bridge between systems, enabling automatic creation and configuration of employee benefits plans for small and medium-sized businesses. Integrated with Employe
  name: Equitable Benefits Plan Setup API
  slug: benefits-plan-setup
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/equitable-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Equitable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/equitable-financial
- group: company
  title: ''
  type: Website
  url: https://equitable.com/
- group: operate
  title: ''
  type: Technical Support
  url: https://equitable.com/support/technical-support
created: '2025-03-01'
description: Equitable Holdings, Inc. is a financial services holding company offering individual retirement, group retirement, life insurance, and employee benefits solutions. In 2025, Equitable launched API capabilities for benefits plan setup integration, partnering with platforms such as Employee Navigator to streamline broker workflows.
finops:
- name: Equitable Finops
  service_category: API
  slug: equitable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/equitable.png
layout: provider
modified: '2026-07-25'
name: Equitable
nav: Providers
network: true
overview: Equitable publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Benefits, Financial Services, Insurance, Retirement, and Employee Benefits.
plans:
- name: Equitable Plans Pricing
  plan_count: 3
  slug: equitable-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Equitable Rate Limits
  slug: equitable-rate-limits
score:
  band: minimal
  composite: 8.7
  delta: -2.6
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 11.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 9.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/equitable/refs/heads/main/screenshots/equitable-2026-06-20T180805.png
security:
- kind: domain-security
  name: Equitable Domain Security
  slug: equitable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: equitable
tags:
- Benefits
- Financial Services
- Insurance
- Retirement
- Employee Benefits
website: https://equitable.com/
---
