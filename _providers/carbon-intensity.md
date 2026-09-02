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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Carbon Intensity Agentic Access
  operation_count: 27
  slug: carbon-intensity-agentic-access
  summary_line: 27 operations
api_count: 1
apis:
- description: Carbon intensity factors by fuel type
  name: Carbon Intensity API Factors API
  slug: carbon-intensity-factors-api
- description: Electricity generation mix data (beta)
  name: Carbon Intensity API Generation Mix API
  slug: carbon-intensity-generation-mix-api
- description: National carbon intensity data for Great Britain
  name: Carbon Intensity API National Intensity API
  slug: carbon-intensity-national-intensity-api
- description: Regional carbon intensity and generation mix data (beta)
  name: Carbon Intensity API Regional API
  slug: carbon-intensity-regional-api
- description: Carbon intensity statistics and aggregations
  name: Carbon Intensity API Statistics API
  slug: carbon-intensity-statistics-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Carbon Intensity Factors API
  slug: open-carbon-intensity-factors-api
- collection_type: open
  name: Carbon Intensity Factors Generation Mix API
  slug: open-carbon-intensity-generation-mix-api
- collection_type: open
  name: Carbon Intensity Factors National Intensity API
  slug: open-carbon-intensity-national-intensity-api
- collection_type: open
  name: Carbon Intensity Factors Regional API
  slug: open-carbon-intensity-regional-api
- collection_type: open
  name: Carbon Intensity Factors Statistics API
  slug: open-carbon-intensity-statistics-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/carbon-intensity/api-definitions/issues
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/carbon-intensity-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carbon-intensity-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://carbonintensity.org.uk/
- group: docs
  title: ''
  type: Documentation
  url: https://carbon-intensity.github.io/api-definitions/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/carbon-intensity
- group: commercial
  title: ''
  type: TermsOfService
  url: https://github.com/carbon-intensity/terms
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by/4.0/
- group: other
  title: ''
  type: X
  url: https://x.com/carbonintensity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-energy-system-operator
created: '2026-06-13'
description: The Carbon Intensity API is the official carbon intensity forecasting service for Great Britain, developed by the National Energy System Operator (NESO) in partnership with EDF, the University of Oxford, and WWF. It provides real-time, forecast, and historical carbon intensity data alongside generation mix information for GB electricity, with 96+ hour forecasts and 30-minute temporal resolution across 14 regional DNO boundaries. The API is publicly accessible with no authentication required and is licensed under CC BY 4.0.
examples:
- key_count: 4
  name: Get Current Intensity
  slug: get-current-intensity
- key_count: 4
  name: Get Generation Mix
  slug: get-generation-mix
- key_count: 4
  name: Get Intensity Factors
  slug: get-intensity-factors
- key_count: 4
  name: Get Intensity Stats
  slug: get-intensity-stats
- key_count: 4
  name: Get Regional Intensity
  slug: get-regional-intensity
finops:
- name: Carbon Intensity Finops
  service_category: API
  slug: carbon-intensity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carbon-intensity.png
json_schemas:
- name: Generation Mix
  property_count: 3
  slug: generation-mix
- name: Carbon Intensity Factors
  property_count: 14
  slug: intensity-factors
- name: Intensity Period
  property_count: 3
  slug: intensity-period
- name: Regional Intensity
  property_count: 7
  slug: regional-intensity
jsonld:
- class_count: 0
  name: Carbon Intensity Context
  property_count: 35
  slug: carbon-intensity-context
layout: provider
modified: '2026-06-13'
name: Carbon Intensity API
nav: Providers
network: true
overview: 'Carbon Intensity API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Factors API, Generation Mix API, National Intensity API, and 2 more. Tagged areas include Carbon Intensity, Environment, Energy, Electricity, and Climate.


  The Carbon Intensity API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Carbon Intensity API''s developer surface includes documentation and 9 more developer resources.'
plans:
- name: Carbon Intensity Plans
  plan_count: 1
  slug: carbon-intensity-plans
random_paper: 14
rate_limits:
- limit_count: 3
  name: Carbon Intensity Rate Limits
  slug: carbon-intensity-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Carbon Intensity API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: carbon-intensity-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 13
    catalog_gap: 28.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 25.0
    contract_quality: 66.2
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 34.2
  previous_composite: 40.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 20.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carbon-intensity/refs/heads/main/screenshots/carbon-intensity-2026-06-20T173949.png
security:
- kind: domain-security
  name: Carbon Intensity Domain Security
  slug: carbon-intensity-domain-security
  summary_line: TLSv1.3
slug: carbon-intensity
tags:
- Carbon Intensity
- Environment
- Energy
- Electricity
- Climate
- Great Britain
- National Grid
website: https://carbonintensity.org.uk/
---
