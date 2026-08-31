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
- description: The Pulse API enables direct management of your Pulse devices and organisation. Update device settings, create new rooms and locations, access device sensor data and more.
  name: Neat Pulse API
  slug: neat-pulse-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/neat-pulse-api-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Neat-Community-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/neatmeetings
- group: company
  title: ''
  type: Blog
  url: https://neat.no/news/
created: '2025-02-24'
description: The Pulse API enables direct management of your Pulse devices and organisation. Update device settings, create new rooms and locations, access device sensor data and more.
finops:
- name: Neat Pulse Api Finops
  service_category: API
  slug: neat-pulse-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/neat-pulse-api.png
layout: provider
modified: '2026-04-28'
name: Neat Pulse API
nav: Providers
network: true
overview: 'Neat Pulse API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Video Conferencing, Devices, and Hardware.


  Neat Pulse API''s developer surface includes engineering blog and 3 more developer resources.'
plans:
- name: Neat Pulse Api Plans Pricing
  plan_count: 3
  slug: neat-pulse-api-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Neat Pulse Api Rate Limits
  slug: neat-pulse-api-rate-limits
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 6
    catalog_gap: 84.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 9.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/neat-pulse-api/refs/heads/main/screenshots/neat-pulse-api-2026-06-20T190123.png
security:
- kind: domain-security
  name: Neat Pulse Api Domain Security
  slug: neat-pulse-api-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: neat-pulse-api
tags:
- Video Conferencing
- Devices
- Hardware
---
