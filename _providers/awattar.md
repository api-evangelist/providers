---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Awattar Agentic Access
  operation_count: 1
  slug: awattar-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.awattar.at
  baseurl_source: declared
  description: EPEX Spot electricity market price data
  name: aWATTar Market Data API
  slug: awattar-market-data-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: aWATTar Market Data API
  slug: open-awattar-market-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/awattar-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/awattar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.awattar.at
- group: docs
  title: ''
  type: Documentation
  url: https://www.awattar.at/services/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/awattarenergy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/awattar
- group: company
  title: ''
  type: Blog
  url: https://www.awattar.at/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.awattar.at/tariffs/hourly
- group: commercial
  title: ''
  type: Plans
  url: plans/awattar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/awattar-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/awattar-finops.yml
created: '2026-06-13'
description: aWATTar provides a free, public REST API delivering real-time and next-day hourly electricity spot prices sourced from the EPEX Spot market exchange for both Austria and Germany. The API enables developers, smart home integrators, and commercial operators to build dynamic energy pricing applications that respond to market conditions. Prices are updated daily at 14:00 CET covering the following day, and the API returns JSON data including start/end timestamps and market price per MWh. No authentication token is required, making integration straightforward for any developer. The service is offered free of charge under a fair-use policy of 100 requests per day per client, supporting use cases such as EV charging optimization, smart heating control, and automated energy management systems.
examples:
- key_count: 2
  name: Awattar Market Data Example
  slug: awattar-market-data-example
finops:
- name: Awattar Finops
  service_category: ''
  slug: awattar-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/awattar.png
json_schemas:
- name: aWATTar Market Data Response
  property_count: 2
  slug: awattar-market-data-response
jsonld:
- class_count: 5
  name: Awattar Context
  property_count: 8
  slug: awattar-context
layout: provider
modified: '2026-06-13'
name: aWATTar
nav: Providers
network: true
overview: 'aWATTar publishes 1 API on the [APIs.io](https://apis.io/) network: Market Data API. Tagged areas include Electricity, Energy, Spot Price, EPEX Spot, and Dynamic Pricing.


  The aWATTar catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aWATTar''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Awattar Plans Pricing
  plan_count: 1
  slug: awattar-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Awattar Rate Limits
  slug: awattar-rate-limits
rules:
- effective_rule_count: 4
  extends: []
  name: aWATTar API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: awattar-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 14
    catalog_earned: 67.3
    catalog_earned_first_party: 0.0
    catalog_gap: 47.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 59.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 14.9
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/awattar/refs/heads/main/screenshots/awattar-2026-06-20T172732.png
security:
- kind: domain-security
  name: Awattar Domain Security
  slug: awattar-domain-security
  summary_line: TLSv1.3 · DMARC
slug: awattar
tags:
- Electricity
- Energy
- Spot Price
- EPEX Spot
- Dynamic Pricing
- Austria
- Germany
- Smart Energy
- IoT
website: https://www.awattar.at
---
