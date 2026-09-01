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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: The Forward Air API provides access to platform services and data for enterprise integration and automation.
  name: Forward Air API
  slug: forward-air-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/forward-air-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/forward-air
- group: company
  title: ''
  type: Website
  url: https://www.forwardair.com
created: '2026-04-19'
description: Forward Air is a major US corporation and Fortune 1000 company. The Forward Air API provides programmatic access to its platform services, data, and integrations for enterprise customers and partners.
finops:
- name: Forward Air Finops
  service_category: Freight & Logistics
  slug: forward-air-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/forward-air.png
layout: provider
modified: '2026-04-19'
name: Forward Air
nav: Providers
network: true
overview: Forward Air publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Freight, Air Cargo, and Logistics.
plans:
- name: Forward Air Plans Pricing
  plan_count: 1
  slug: forward-air-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 1
  name: Forward Air Rate Limits
  slug: forward-air-rate-limits
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.2
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/forward-air/refs/heads/main/screenshots/forward-air-2026-06-20T181450.png
security:
- kind: domain-security
  name: Forward Air Domain Security
  slug: forward-air-domain-security
  summary_line: TLSv1.3 · DMARC
slug: forward-air
tags:
- Freight
- Air Cargo
- Logistics
website: https://www.forwardair.com
---
