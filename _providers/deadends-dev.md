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
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Deadends Dev Agentic Access
  operation_count: 7
  slug: deadends-dev-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Countries.json API from deadends.dev — 1 operation(s) for countries.json.
  name: deadends.dev Countries.json API
  slug: deadends-dev-countries-json-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Country API from deadends.dev — 1 operation(s) for country.
  name: deadends.dev Country API
  slug: deadends-dev-country-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Deadends.dev API API from deadends.dev — 1 operation(s) for deadends.dev api.
  name: deadends.dev Deadends.dev API
  slug: deadends-dev-deadends-dev-api-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Errors.ndjson API from deadends.dev — 1 operation(s) for errors.ndjson.
  name: deadends.dev Errors.ndjson API
  slug: deadends-dev-errors-ndjson-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Index.json API from deadends.dev — 1 operation(s) for index.json.
  name: deadends.dev Index.json API
  slug: deadends-dev-index-json-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Match.json API from deadends.dev — 1 operation(s) for match.json.
  name: deadends.dev Match.json API
  slug: deadends-dev-match-json-api
- baseURL: https://deadends.dev/api/v1
  baseurl_source: declared
  description: The Stats.json API from deadends.dev — 1 operation(s) for stats.json.
  name: deadends.dev Stats.json API
  slug: deadends-dev-stats-json-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/deadends-dev/agentic-access/deadends-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/deadends-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/deadends-dev/rules/deadends-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/deadends-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/deadends-dev/json-ld/deadends-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/deadends-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/deadends-dev/vocabulary/deadends-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/deadends-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/deadends-dev/data-model/deadends-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/deadends-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/deadends-dev/conformance/deadends-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/deadends-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/deadends-dev/llms/deadends-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/deadends-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/deadends-dev/a2a/deadends-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/deadends-dev-a2a.yml
- group: auth
  href: https://artifacts.apis.io/deadends-dev/well-known/deadends-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/deadends-dev-security.txt
- group: agent
  href: https://artifacts.apis.io/deadends-dev/well-known/deadends-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/deadends-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/deadends-dev/hosts/deadends-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/deadends-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/deadends-dev/vendors/deadends-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/deadends-dev-vendors.yml
- group: build
  href: https://artifacts.apis.io/deadends-dev/packages/deadends-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/deadends-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/deadends-dev/packages/deadends-dev-packages.yml
  title: ''
  type: Packages
  url: packages/deadends-dev-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://deadends.dev/security/
- group: auth
  href: https://artifacts.apis.io/deadends-dev/security/deadends-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/deadends-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/deadends-dev/security/deadends-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/deadends-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://deadends.dev/
created: '2026-11-05'
description: 'deadends-dev is a company surfaced via the API Evangelist harvest backlog (source: mcp-registry) and added to the network as a stub for full-pipeline profiling.'
image: https://deadends.dev/og-image.png
json_schemas:
- name: CountryAggregate
  property_count: 8
  slug: deadends-dev-country-aggregate
- name: CountrySummary
  property_count: 6
  slug: deadends-dev-country-summary
- name: ErrorCanon
  property_count: 7
  slug: deadends-dev-error-canon
- name: ErrorSummary
  property_count: 8
  slug: deadends-dev-error-summary
jsonld:
- class_count: 4
  name: Deadends Dev Context
  property_count: 21
  slug: deadends-dev-context
layout: provider
modified: '2026-11-05'
name: deadends.dev
nav: Providers
network: true
overview: 'deadends.dev publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Countries.json API, Country API, Deadends.dev API, and 4 more. Tagged areas include Error Database, Debugging, and Open Source.


  The deadends.dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: deadends.dev API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: deadends-dev-rules
score:
  band: emerging
  composite: 24.6
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.8
    catalog_earned_first_party: 0.0
    catalog_gap: 65.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Deadends Dev Domain Security
  slug: deadends-dev-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Deadends Dev Vulnerability Disclosure
  slug: deadends-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: deadends-dev
tags:
- Error Database
- Debugging
- Open Source
website: https://deadends.dev/
---
