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
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Chalet Montagne Com Agentic Access
  operation_count: 7
  slug: chalet-montagne-com-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- baseURL: https://mcp.chalet-montagne.com
  baseurl_source: declared
  description: The Public Front API from Chalet Montagne — 7 operation(s) for public front.
  name: Chalet Montagne Public Front API
  slug: chalet-montagne-com-public-front-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/chalet-montagne-com/agentic-access/chalet-montagne-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/chalet-montagne-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/rules/chalet-montagne-com-rules.yml
  title: ''
  type: Spectral
  url: rules/chalet-montagne-com-rules.yml
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/json-ld/chalet-montagne-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chalet-montagne-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/vocabulary/chalet-montagne-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chalet-montagne-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/data-model/chalet-montagne-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chalet-montagne-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/errors/chalet-montagne-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/chalet-montagne-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/chalet-montagne-com/conformance/chalet-montagne-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chalet-montagne-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chalet-montagne-com/llms/chalet-montagne-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chalet-montagne-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/chalet-montagne-com/well-known/chalet-montagne-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chalet-montagne-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/chalet-montagne-com/hosts/chalet-montagne-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chalet-montagne-com-hosts.yml
- group: docs
  title: ''
  type: Documentation
  url: https://dev.chalet-montagne.com/
- group: auth
  href: https://artifacts.apis.io/chalet-montagne-com/security/chalet-montagne-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chalet-montagne-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chalet-montagne.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.chalet-montagne.com/
- group: docs
  title: ''
  type: APIReference
  url: https://mcp.chalet-montagne.com/openapi
- group: company
  title: ''
  type: Blog
  url: https://www.chalet-montagne.com/blog
created: '2026-11-03'
description: Chalet Montagne is a French vacation rental platform offering seasonal mountain accommodations across the Alps, Pyrenees, Jura, Vosges, and Massif Central. It connects travelers directly with property owners or agencies, providing thousands of listings in hundreds of stations, available in six languages, with detailed descriptions, capacities, pricing, and availability calendars.
image: https://www.chalet-montagne.com/images/hero/chalet-automne-1.jpg?v=1782497310
json_schemas:
- name: Envelope
  property_count: 3
  slug: chalet-montagne-com-envelope
- name: SearchResponse
  property_count: 2
  slug: chalet-montagne-com-search-response
jsonld:
- class_count: 2
  name: Chalet Montagne Com Context
  property_count: 3
  slug: chalet-montagne-com-context
layout: provider
modified: '2026-11-03'
name: Chalet Montagne
nav: Providers
network: true
overview: 'Chalet Montagne publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Public Front API. Tagged areas include Vacation Rentals, France, Mountain, Travel, and Accommodation.


  The Chalet Montagne catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Chalet Montagne''s developer surface includes documentation, API reference, engineering blog, and 13 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Chalet Montagne API Rules
  rule_count: 42
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 3
  slug: chalet-montagne-com-rules
score:
  band: emerging
  composite: 24.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 56.8
    catalog_earned_first_party: 0.0
    catalog_gap: 58.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 51.8
    developer_ergonomics: 14.3
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Chalet Montagne Com Domain Security
  slug: chalet-montagne-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: chalet-montagne-com
tags:
- Vacation Rentals
- France
- Mountain
- Travel
- Accommodation
website: https://chalet-montagne.com/
---
