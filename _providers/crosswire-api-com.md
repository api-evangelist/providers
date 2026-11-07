---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Crosswire Api Com Agentic Access
  operation_count: 5
  slug: crosswire-api-com-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.crosswire-api.com
  baseurl_source: declared
  description: The Adoption API from Crosswire — 1 operation(s) for adoption.
  name: Crosswire Adoption API
  slug: crosswire-api-com-adoption-api
- baseURL: https://api.crosswire-api.com
  baseurl_source: declared
  description: The Audit API from Crosswire — 1 operation(s) for audit.
  name: Crosswire Audit API
  slug: crosswire-api-com-audit-api
- baseURL: https://api.crosswire-api.com
  baseurl_source: declared
  description: The Events API from Crosswire — 1 operation(s) for events.
  name: Crosswire Events API
  slug: crosswire-api-com-events-api
- baseURL: https://api.crosswire-api.com
  baseurl_source: declared
  description: The Health API from Crosswire — 1 operation(s) for health.
  name: Crosswire Health API
  slug: crosswire-api-com-health-api
- baseURL: https://api.crosswire-api.com
  baseurl_source: declared
  description: The Live API from Crosswire — 1 operation(s) for live.
  name: Crosswire Live API
  slug: crosswire-api-com-live-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/crosswire-api-com/agentic-access/crosswire-api-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/crosswire-api-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/rules/crosswire-api-com-rules.yml
  title: ''
  type: Spectral
  url: rules/crosswire-api-com-rules.yml
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/json-ld/crosswire-api-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/crosswire-api-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/vocabulary/crosswire-api-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/crosswire-api-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/data-model/crosswire-api-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/crosswire-api-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/errors/crosswire-api-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/crosswire-api-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/crosswire-api-com/conformance/crosswire-api-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/crosswire-api-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/crosswire-api-com/hosts/crosswire-api-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crosswire-api-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/crosswire-api-com/vendors/crosswire-api-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crosswire-api-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/crosswire-api-com/security/crosswire-api-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crosswire-api-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://crosswire-api.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.crosswire-api.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.crosswire-api.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://api.crosswire-api.com/docs#/default/health_v1_health_get
created: '2026-11-04'
description: Crosswire provides a pre‑trade resolution‑truth gate for cross‑venue trading agents. It audits event markets across platforms like Polymarket and Kalshi, returning SAFE, CAUTION, or BLOCK verdicts with detailed rule divergences. The service operates statelessly, machine‑to‑machine, at a low cost per call, helping users avoid settlement mismatches and protect hedged positions.
json_schemas:
- name: EventInfo
  property_count: 6
  slug: crosswire-api-com-event-info
- name: HealthResponse
  property_count: 9
  slug: crosswire-api-com-health-response
- name: LivenessResponse
  property_count: 7
  slug: crosswire-api-com-liveness-response
- name: VenueMarketRef
  property_count: 0
  slug: crosswire-api-com-venue-market-ref
- name: Venue
  property_count: 0
  slug: crosswire-api-com-venue
jsonld:
- class_count: 7
  name: Crosswire Api Com Context
  property_count: 34
  slug: crosswire-api-com-context
layout: provider
modified: '2026-11-04'
name: Crosswire
nav: Providers
network: true
overview: 'Crosswire publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Adoption API, Audit API, Events API, and 2 more. Tagged areas include Finance, Trading, Cryptocurrency, and Risk Management.


  The Crosswire catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Crosswire''s developer surface includes documentation, API reference, getting-started guide, and 11 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 74
  extends:
  - spectral:oas
  name: Crosswire API Rules
  rule_count: 33
  severity_counts:
    error: 31
    hint: 0
    info: 1
    warn: 1
  slug: crosswire-api-com-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 48.6
    developer_ergonomics: 28.6
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 10.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crosswire Api Com Domain Security
  slug: crosswire-api-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: crosswire-api-com
tags:
- Finance
- Trading
- Cryptocurrency
- Risk Management
website: https://crosswire-api.com/
---
