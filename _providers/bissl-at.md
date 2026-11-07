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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bissl At Agentic Access
  operation_count: 4
  slug: bissl-at-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://api.bissl.at
  baseurl_source: declared
  description: The Dishes API from bissl-at — 1 operation(s) for dishes.
  name: bissl-at Dishes API
  slug: bissl-at-dishes-api
- baseURL: https://api.bissl.at
  baseurl_source: declared
  description: The Lunch API from bissl-at — 1 operation(s) for lunch.
  name: bissl-at Lunch API
  slug: bissl-at-lunch-api
- baseURL: https://api.bissl.at
  baseurl_source: declared
  description: The Venues API from bissl-at — 2 operation(s) for venues.
  name: bissl-at Venues API
  slug: bissl-at-venues-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/bissl-at/agentic-access/bissl-at-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bissl-at-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bissl-at/rules/bissl-at-rules.yml
  title: ''
  type: Spectral
  url: rules/bissl-at-rules.yml
- group: design
  href: https://artifacts.apis.io/bissl-at/json-ld/bissl-at-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bissl-at-context.jsonld
- group: design
  href: https://artifacts.apis.io/bissl-at/vocabulary/bissl-at-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bissl-at-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bissl-at/data-model/bissl-at-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bissl-at-data-model.yml
- group: design
  href: https://artifacts.apis.io/bissl-at/errors/bissl-at-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bissl-at-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bissl-at/conformance/bissl-at-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bissl-at-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bissl-at/well-known/bissl-at-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bissl-at-well-known.yml
- group: other
  href: https://artifacts.apis.io/bissl-at/hosts/bissl-at-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bissl-at-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bissl-at/security/bissl-at-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bissl-at-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bissl.at/
created: '2026-11-02'
description: 'bissl-at is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
json_schemas:
- name: DishesAnswer
  property_count: 11
  slug: bissl-at-dishes-answer
- name: LunchAnswer
  property_count: 11
  slug: bissl-at-lunch-answer
- name: VenueAnswer
  property_count: 9
  slug: bissl-at-venue-answer
- name: VenuesAnswer
  property_count: 5
  slug: bissl-at-venues-answer
jsonld:
- class_count: 12
  name: Bissl At Context
  property_count: 49
  slug: bissl-at-context
layout: provider
modified: '2026-11-02'
name: bissl-at
nav: Providers
network: true
overview: 'bissl-at publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Dishes API, Lunch API, and Venues API. Tagged areas include Company.


  The bissl-at catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 78
  extends:
  - spectral:oas
  name: bissl-at API Rules
  rule_count: 37
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 2
  slug: bissl-at-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
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
  name: Bissl At Domain Security
  slug: bissl-at-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bissl-at
tags:
- Company
website: https://bissl.at/
---
