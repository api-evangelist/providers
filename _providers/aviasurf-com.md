---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
  score: 20.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aviasurf Com Agentic Access
  operation_count: 8
  slug: aviasurf-com-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- baseURL: https://api.aviasurf.com
  baseurl_source: declared
  description: The Health API from Aviasurf — 1 operation(s) for health.
  name: Aviasurf Health API
  slug: aviasurf-com-health-api
- baseURL: https://api.aviasurf.com
  baseurl_source: declared
  description: The Prices API from Aviasurf — 7 operation(s) for prices.
  name: Aviasurf Prices API
  slug: aviasurf-com-prices-api
artifact_total: 13
common:
- group: design
  href: https://artifacts.apis.io/aviasurf-com/data-model/aviasurf-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aviasurf-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/aviasurf-com/agentic-access/aviasurf-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aviasurf-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/aviasurf-com/rules/aviasurf-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aviasurf-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aviasurf-com/vocabulary/aviasurf-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aviasurf-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aviasurf-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/aviasurf-com/cli/aviasurf-com-cli.yml
  title: ''
  type: CLI
  url: cli/aviasurf-com-cli.yml
- group: design
  href: https://artifacts.apis.io/aviasurf-com/errors/aviasurf-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aviasurf-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aviasurf-com/conformance/aviasurf-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aviasurf-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/aviasurf-com/hosts/aviasurf-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aviasurf-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aviasurf-com/vendors/aviasurf-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aviasurf-com-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://aviasurf.com/help
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aviasurf
- group: auth
  href: https://artifacts.apis.io/aviasurf-com/security/aviasurf-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aviasurf-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aviasurf.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aviasurf.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aviasurf.com/privacy
created: '2026-11-02'
description: Aviasurf is a flight metasearch service. We compare flight options from airlines and travel agencies and redirect travelers to the selected provider to complete their booking. Aviasurf does not sell airline tickets directly.
image: https://aviasurf.com/local/templates/aviasurf_2026/images/logo-schema.png
json_schemas:
- name: CalendarEnvelope
  property_count: 0
  slug: aviasurf-com-calendar-envelope
- name: CheapestFromEnvelope
  property_count: 0
  slug: aviasurf-com-cheapest-from-envelope
- name: PopularFromEnvelope
  property_count: 0
  slug: aviasurf-com-popular-from-envelope
- name: PopularToEnvelope
  property_count: 0
  slug: aviasurf-com-popular-to-envelope
- name: RoutePricesEnvelope
  property_count: 0
  slug: aviasurf-com-route-prices-envelope
layout: provider
modified: '2026-11-02'
name: Aviasurf
nav: Providers
network: true
overview: 'Aviasurf publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Health API and Prices API. Tagged areas include Flights, Travel, Metasearch, Booking, and Airlines.


  The Aviasurf catalog on APIs.io includes 1 Spectral governance ruleset.


  Aviasurf''s developer surface includes CLI, support, and 14 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: Aviasurf API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: aviasurf-com-rules
scopes:
- name: Aviasurf Com Scopes
  scope_count: 0
  slug: aviasurf-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 26
    catalog_earned: 51.8
    catalog_earned_first_party: 0.0
    catalog_gap: 63.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 45.3
    developer_ergonomics: 16.0
    discoverability: 66.1
    operational_transparency: 2.6
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aviasurf Com Authentication
  slug: aviasurf-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aviasurf Com Domain Security
  slug: aviasurf-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: aviasurf-com-search-price-skill
  slug: aviasurf-com-search-price-skill
slug: aviasurf-com
tags:
- Flights
- Travel
- Metasearch
- Booking
- Airlines
website: https://aviasurf.com/
---
