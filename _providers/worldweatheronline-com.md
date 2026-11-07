---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: WorldWeatherOnline provides weather data APIs (current, forecast, historical, marine, ski, etc.)
  name: Weather API
  slug: weather-api
- baseURL: https://api.worldweatheronline.com
  baseurl_source: declared
  description: 'worldweatheronline-com API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: worldweatheronline-com API
  slug: worldweatheronline-com-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/worldweatheronline-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/worldweatheronline-com/rate-limits/worldweatheronline-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/worldweatheronline-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/worldweatheronline-com/plans/worldweatheronline-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/worldweatheronline-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/worldweatheronline-com/rules/worldweatheronline-com-rules.yml
  title: ''
  type: Spectral
  url: rules/worldweatheronline-com-rules.yml
- group: design
  href: https://artifacts.apis.io/worldweatheronline-com/json-ld/worldweatheronline-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/worldweatheronline-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/worldweatheronline-com/vocabulary/worldweatheronline-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/worldweatheronline-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/worldweatheronline-com/data-model/worldweatheronline-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/worldweatheronline-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/worldweatheronline-com/authentication/worldweatheronline-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/worldweatheronline-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/worldweatheronline-com/conformance/worldweatheronline-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/worldweatheronline-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/worldweatheronline-com/hosts/worldweatheronline-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/worldweatheronline-com-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.worldweatheronline.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WorldWeatherOnline
- group: auth
  href: https://artifacts.apis.io/worldweatheronline-com/security/worldweatheronline-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/worldweatheronline-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://worldweatheronline.com/
coverage:
  checked: '2026-10-31'
  detail: API documentation pages are rendered via JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://www.worldweatheronline.com/weather-api/api/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-31'
description: 'worldweatheronline-com is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: GetAstronomyAshxResponse
  property_count: 16
  slug: worldweatheronline-com-get-astronomy-ashx-response
- name: GetPremiumV1PastMarineAshxResponse
  property_count: 19
  slug: worldweatheronline-com-get-premium-v1-past-marine-ashx-response
- name: GetPremiumV1PastWeatherAshxResponse
  property_count: 32
  slug: worldweatheronline-com-get-premium-v1-past-weather-ashx-response
- name: GetPremiumV1SkiAshxResponse
  property_count: 34
  slug: worldweatheronline-com-get-premium-v1-ski-ashx-response
jsonld:
- class_count: 4
  name: Worldweatheronline Com Context
  property_count: 97
  slug: worldweatheronline-com-context
layout: provider
modified: '2026-10-31'
name: worldweatheronline-com
nav: Providers
network: true
overview: 'worldweatheronline-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The worldweatheronline-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  worldweatheronline-com''s developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: Worldweatheronline Com Plans Pricing
  plan_count: 3
  slug: worldweatheronline-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Worldweatheronline Com Rate Limits
  slug: worldweatheronline-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: worldweatheronline-com API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: worldweatheronline-com-rules
scopes:
- name: Worldweatheronline Com Scopes
  scope_count: 0
  slug: worldweatheronline-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 23.5
    developer_ergonomics: 23.1
    discoverability: 44.6
    operational_transparency: 23.7
  previous_composite: 30.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Worldweatheronline Com Authentication
  slug: worldweatheronline-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Worldweatheronline Com Domain Security
  slug: worldweatheronline-com-domain-security
  summary_line: DMARC
slug: worldweatheronline-com
tags:
- Company
website: https://worldweatheronline.com/
---
