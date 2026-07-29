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
- description: Hobart's API integration helps automate the work order workflow process and streamline the exchange of data between partner systems and Hobart's service operations. Implementation requires the Web Ser
  name: Hobart Work Order Web Service
  slug: work-order-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hobart-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hobart
- group: company
  title: ''
  type: Website
  url: https://www.hobartcorp.com
created: '2024-01-15'
description: Hobart is a leading commercial food service equipment manufacturer that offers an API integration to automate work order workflow and streamline the exchange of data between partner systems and Hobart service operations.
finops:
- name: Hobart Finops
  service_category: API
  slug: hobart-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hobart.png
layout: provider
modified: '2026-04-28'
name: Hobart
nav: Providers
network: true
overview: Hobart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Equipment, Food Service, Work Orders, and Service.
plans:
- name: Hobart Plans Pricing
  plan_count: 3
  slug: hobart-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Hobart Rate Limits
  slug: hobart-rate-limits
score:
  band: emerging
  composite: 17.0
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 18.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hobart/refs/heads/main/screenshots/hobart-2026-06-20T182807.png
security:
- kind: domain-security
  name: Hobart Domain Security
  slug: hobart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hobart
tags:
- Equipment
- Food Service
- Work Orders
- Service
website: https://www.hobartcorp.com
---
