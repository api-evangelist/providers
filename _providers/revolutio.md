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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Revolutio Agentic Access
  operation_count: 8
  slug: revolutio-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://api.revolutio.com.au
  baseurl_source: declared
  description: Multi-hazard combined analysis returning all available parameters for a site
  name: Revolutio Combined Hazard API
  slug: revolutio-combined-hazard-api
- baseURL: https://api.revolutio.com.au
  baseurl_source: declared
  description: Seismic hazard parameters
  name: Revolutio Seismic API
  slug: revolutio-seismic-api
- baseURL: https://api.revolutio.com.au
  baseurl_source: declared
  description: Snow and ice loading parameters per applicable standards
  name: Revolutio Snow And Ice API
  slug: revolutio-snow-and-ice-api
- baseURL: https://api.revolutio.com.au
  baseurl_source: declared
  description: Site-specific wind hazard analysis per AS/NZS 1170.2 and ASCE 7 standards
  name: Revolutio Wind API
  slug: revolutio-wind-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Revolutio Hazard Combined Hazard API
  slug: open-revolutio-combined-hazard-api
- collection_type: open
  name: Revolutio Hazard API
  slug: open-revolutio-hazard-api
- collection_type: open
  name: Revolutio Hazard Combined Hazard Seismic API
  slug: open-revolutio-seismic-api
- collection_type: open
  name: Revolutio Hazard Combined Hazard Snow And Ice API
  slug: open-revolutio-snow-and-ice-api
- collection_type: open
  name: Revolutio Hazard Combined Hazard Wind API
  slug: open-revolutio-wind-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/revolutio-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/revolutio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/revolutio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/revolutio-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revolutio
- group: company
  title: ''
  type: Website
  url: https://www.revolutio.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://www.revolutio.com.au/support/hazardapi/
- group: docs
  title: ''
  type: Swagger
  url: https://api.revolutio.com.au/swagger/index.html
created: '2025-02-17'
description: Revolutio provides smart structural engineering software and a Hazard API (formerly CHECKWIND.API) that delivers site-specific wind, snow, ice, and seismic load parameters for structural engineering and construction projects. The API is trusted by over 750 companies and 5000 users worldwide across construction, fabrication, power distribution, signage, structural engineering, and telecommunications. It covers 40+ countries and supports standards including AS/NZS 1170.2, AS 4055, and ASCE 7.
examples:
- key_count: 2
  name: Revolutio Combined Hazard Example
  slug: revolutio-combined-hazard-example
- key_count: 2
  name: Revolutio Get Wind Hazard Example
  slug: revolutio-get-wind-hazard-example
finops:
- name: Revolutio Finops
  service_category: API
  slug: revolutio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/revolutio.png
json_schemas:
- name: Revolutio Wind Hazard Analysis Result
  property_count: 8
  slug: revolutio-wind-result
json_structures:
- name: Revolutio Wind Result Structure
  property_count: 0
  slug: revolutio-wind-result-structure
jsonld:
- class_count: 29
  name: Revolutio Context
  property_count: 0
  slug: revolutio-context
layout: provider
modified: '2026-05-19'
name: Revolutio
nav: Providers
network: true
overview: 'Revolutio publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Combined Hazard API, Seismic API, Snow And Ice API, and 1 more. Tagged areas include Engineering, Hazard, Weather, Structural Engineering, and Wind Analysis.


  The Revolutio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Revolutio''s developer surface includes authentication, documentation, and 6 more developer resources.'
plans:
- name: Revolutio Plans Pricing
  plan_count: 3
  slug: revolutio-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Revolutio Rate Limits
  slug: revolutio-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Revolutio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: revolutio-jsonschema-spectral-rules
- effective_rule_count: 8
  extends: []
  name: Revolutio API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: revolutio-rules
score:
  band: thin
  composite: 29.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.3
    catalog_earned_first_party: 0.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 59.7
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 29.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/revolutio/refs/heads/main/screenshots/revolutio-2026-06-20T193102.png
security:
- kind: authentication
  name: Revolutio Authentication
  slug: revolutio-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Revolutio Domain Security
  slug: revolutio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: revolutio
tags:
- Engineering
- Hazard
- Weather
- Structural Engineering
- Wind Analysis
- Construction
website: https://www.revolutio.com.au/
---
