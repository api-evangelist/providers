---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Farm Machinery And Equipment Api Agentic Access
  operation_count: 1
  slug: farm-machinery-and-equipment-api-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Farm Machinery and Equipment API is a vast repository of farm machinery data, technical details, specifications, usage guidelines, operating manuals, maintenance recommendations and more for Agricultu
  name: Farm Machinery and Equipment API
  slug: farm-machinery-and-equipment-api
- baseURL: https://apifarmer.com/
  baseurl_source: declared
  description: The Farm Machinery API from Farm Machinery and Equipment API — 1 operation(s) for farm machinery.
  name: Farm Machinery and Equipment API Farm Machinery API
  slug: farm-machinery-and-equipment-api-farm-machinery-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: APIFarmer and Equipment Farm Machinery API
  slug: open-farm-machinery-and-equipment-api-farm-machinery-api
- collection_type: open
  name: APIFarmer Farm Machinery and Equipment API
  slug: open-farm-machinery-and-equipment-api
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/plans/farm-machinery-and-equipment-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/farm-machinery-and-equipment-api-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/rate-limits/farm-machinery-and-equipment-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/farm-machinery-and-equipment-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/finops/farm-machinery-and-equipment-api-finops.yml
  title: ''
  type: FinOps
  url: finops/farm-machinery-and-equipment-api-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/agentic-access/farm-machinery-and-equipment-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/farm-machinery-and-equipment-api-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/security/farm-machinery-and-equipment-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/farm-machinery-and-equipment-api-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/authentication/farm-machinery-and-equipment-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/farm-machinery-and-equipment-api-authentication.yml
created: '2025-02-12'
description: The Farm Machinery and Equipment API is a software solution that provides developers with access to a database of information related to various types of farm machinery and equipment. This API allows users to retrieve detailed specifications, usage instructions, maintenance tips, and other relevant data for a wide range of agricultural tools and devices.
finops:
- has_sources: false
  method: generated
  name: Farm Machinery And Equipment Api Finops
  primary_unit: ''
  service_category: API
  slug: farm-machinery-and-equipment-api-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/farm-machinery-and-equipment-api.png
layout: provider
modified: '2026-04-28'
name: Farm Machinery and Equipment API
nav: Providers
network: true
overview: 'Farm Machinery and Equipment API publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Farm Machinery API, and 1 more. Tagged areas include Equipment, Farms, and Machinery.


  Farm Machinery and Equipment API''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Farm Machinery And Equipment Api Plans Pricing
  plan_count: 3
  slug: farm-machinery-and-equipment-api-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Farm Machinery And Equipment Api Rate Limits
  slug: farm-machinery-and-equipment-api-rate-limits
score:
  band: emerging
  composite: 25.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.5
  facets:
    access_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 46.5
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 27.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/farm-machinery-and-equipment-api/refs/heads/main/screenshots/farm-machinery-and-equipment-api-2026-06-20T181042.png
security:
- kind: authentication
  name: Farm Machinery And Equipment Api Authentication
  slug: farm-machinery-and-equipment-api-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Farm Machinery And Equipment Api Domain Security
  slug: farm-machinery-and-equipment-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: farm-machinery-and-equipment-api
tags:
- Equipment
- Farms
- Machinery
---
