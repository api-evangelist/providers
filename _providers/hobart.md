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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
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
random_paper: 10
rate_limits:
- limit_count: 5
  name: Hobart Rate Limits
  slug: hobart-rate-limits
score:
  band: emerging
  composite: 11.1
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
