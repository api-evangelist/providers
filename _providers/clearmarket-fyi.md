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
    agent_card: conformant
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Clearmarket Fyi Agentic Access
  operation_count: 12
  slug: clearmarket-fyi-agentic-access
  summary_line: 12 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Catalysts API from ClearMarket — 1 operation(s) for catalysts.
  name: ClearMarket Catalysts API
  slug: clearmarket-fyi-catalysts-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The ClearMarket API API from ClearMarket — 1 operation(s) for clearmarket api.
  name: ClearMarket ClearMarket API
  slug: clearmarket-fyi-clearmarket-api-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Events API from ClearMarket — 2 operation(s) for events.
  name: ClearMarket Events API
  slug: clearmarket-fyi-events-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Keys API from ClearMarket — 1 operation(s) for keys.
  name: ClearMarket Keys API
  slug: clearmarket-fyi-keys-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Markets API from ClearMarket — 2 operation(s) for markets.
  name: ClearMarket Markets API
  slug: clearmarket-fyi-markets-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Marks API from ClearMarket — 1 operation(s) for marks.
  name: ClearMarket Marks API
  slug: clearmarket-fyi-marks-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Signals API from ClearMarket — 2 operation(s) for signals.
  name: ClearMarket Signals API
  slug: clearmarket-fyi-signals-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Spot API from ClearMarket — 1 operation(s) for spot.
  name: ClearMarket Spot API
  slug: clearmarket-fyi-spot-api
- baseURL: https://api.clearmarket.fyi
  baseurl_source: declared
  description: The Status API from ClearMarket — 1 operation(s) for status.
  name: ClearMarket Status API
  slug: clearmarket-fyi-status-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/clearmarket-fyi/agentic-access/clearmarket-fyi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clearmarket-fyi-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/rules/clearmarket-fyi-rules.yml
  title: ''
  type: Spectral
  url: rules/clearmarket-fyi-rules.yml
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/json-ld/clearmarket-fyi-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clearmarket-fyi-context.jsonld
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/vocabulary/clearmarket-fyi-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clearmarket-fyi-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/data-model/clearmarket-fyi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clearmarket-fyi-data-model.yml
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/errors/clearmarket-fyi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clearmarket-fyi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clearmarket-fyi/conformance/clearmarket-fyi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clearmarket-fyi-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clearmarket-fyi/llms/clearmarket-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clearmarket-fyi-llms.txt
- group: other
  href: https://artifacts.apis.io/clearmarket-fyi/a2a/clearmarket-fyi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/clearmarket-fyi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/clearmarket-fyi/well-known/clearmarket-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clearmarket-fyi-well-known.yml
- group: other
  href: https://artifacts.apis.io/clearmarket-fyi/hosts/clearmarket-fyi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clearmarket-fyi-hosts.yml
- group: other
  href: https://artifacts.apis.io/clearmarket-fyi/vendors/clearmarket-fyi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clearmarket-fyi-vendors.yml
- group: auth
  href: https://artifacts.apis.io/clearmarket-fyi/security/clearmarket-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clearmarket-fyi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clearmarket.fyi/
created: '2026-11-03'
description: ClearMarket provides an institutional reference layer for prediction market data, offering graded resolution clarity, regulatory eligibility screens, and cross‑venue linking across Kalshi and Polymarket. The platform serves daily API and MCP feeds for analysts, desks, and agents to query events, signals, and methodology, supporting open access to market intelligence.
image: https://clearmarket.fyi/og.png
json_schemas:
- name: ClearMarket Event
  property_count: 18
  slug: clearmarket-fyi-event
- name: ClearMarket Market
  property_count: 46
  slug: clearmarket-fyi-market
- name: ClearMarket Resolution Log Entry
  property_count: 12
  slug: clearmarket-fyi-resolution-log-entry
jsonld:
- class_count: 4
  name: Clearmarket Fyi Context
  property_count: 97
  slug: clearmarket-fyi-context
layout: provider
modified: '2026-11-03'
name: ClearMarket
nav: Providers
network: true
overview: 'ClearMarket publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalysts API, ClearMarket API, Events API, and 6 more. Tagged areas include Prediction Markets, Market Data API, Signal Feed, Daily Wire, and Market Intelligence.


  The ClearMarket catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: ClearMarket API Rules
  rule_count: 45
  severity_counts:
    error: 43
    hint: 0
    info: 1
    warn: 1
  slug: clearmarket-fyi-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 18
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 55.2
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clearmarket Fyi Domain Security
  slug: clearmarket-fyi-domain-security
  summary_line: TLSv1.3
slug: clearmarket-fyi
tags:
- Prediction Markets
- Market Data API
- Signal Feed
- Daily Wire
- Market Intelligence
website: https://clearmarket.fyi/
---
