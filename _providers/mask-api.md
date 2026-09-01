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
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Mask API is a powerful and flexible tool designed to help programmers and companies customize the response format of endpoint APIs, providing control over which fields are returned in API responses.
  name: Mask API
  slug: mask-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mask-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Mask-API
- group: company
  title: ''
  type: Website
  url: https://maskapi.dev/
created: '2025-02-12'
description: Mask API is a powerful and flexible tool designed to help programmers and companies customize the response format of endpoint APIs, enabling selective field filtering and data transformation in API responses.
finops:
- name: Mask Api Finops
  service_category: API
  slug: mask-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mask-api.png
layout: provider
modified: '2026-04-28'
name: Mask API
nav: Providers
network: true
overview: Mask API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Tools, Developer Tools, and Response Filtering.
plans:
- name: Mask Api Plans Pricing
  plan_count: 3
  slug: mask-api-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Mask Api Rate Limits
  slug: mask-api-rate-limits
score:
  band: emerging
  composite: 11.4
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
    operational_transparency: 10.5
  previous_composite: 11.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mask-api/refs/heads/main/screenshots/mask-api-2026-06-20T185015.png
security:
- kind: domain-security
  name: Mask Api Domain Security
  slug: mask-api-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mask-api
tags:
- API Tools
- Developer Tools
- Response Filtering
website: https://maskapi.dev/
---
