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
    mcp_server: documented
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
  score: 20.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Free REST API providing DayZ item data as documented on the DZPage developer page.
  name: DZPage Item API
  slug: dzpage-item-api
- description: 'DZPage API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-11-06); not the provider''s own document.'
  name: DZPage API
  slug: dzpage-com-api
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/dzpage-com/rules/dzpage-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dzpage-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dzpage-com/json-ld/dzpage-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dzpage-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dzpage-com/vocabulary/dzpage-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dzpage-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dzpage-com/data-model/dzpage-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dzpage-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dzpage-com/conformance/dzpage-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dzpage-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dzpage-com/llms/dzpage-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dzpage-com-llms.txt
- group: other
  href: https://artifacts.apis.io/dzpage-com/hosts/dzpage-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dzpage-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dzpage-com/vendors/dzpage-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dzpage-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dzpage-com/security/dzpage-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dzpage-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dzpage.com/
coverage:
  checked: '2026-11-06'
  detail: The provider documents a free REST API but no OpenAPI or other machine‑readable contract is publicly available.
  evidence:
  - status: 200
    url: https://dzpage.com/en/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-06'
description: DZPage provides a comprehensive DayZ item database, interactive loot maps, a 3D map, and tools such as XML editors. All data is sourced directly from the real game files, offering over 4,700 items with detailed weapon stats, loot locations, and server tools. The platform also offers a free open REST API for developers to integrate DayZ data into their applications, without requiring accounts or paywalls.
image: https://dzpage.com/api/og?t=DayZ+item+database%2C+loot+maps+and+server+tools&s=Everything+generated+straight+from+the+game+files%3A+4%2C700%2B+items+with+real+stats%2C+interactive+loot+maps%2C+a+real+3D+map+and+editors+for+every+mission+file.+No+account%2C+no+paywall.&tag=100%25+free
json_schemas:
- name: GetApiV1CategoriesResponse
  property_count: 1
  slug: dzpage-com-get-api-v1-categories-response
- name: GetApiV1ItemsClassnameResponse
  property_count: 1
  slug: dzpage-com-get-api-v1-items-classname-response
jsonld:
- class_count: 2
  name: Dzpage Com Context
  property_count: 2
  slug: dzpage-com-context
layout: provider
modified: '2026-11-06'
name: DZPage
nav: Providers
network: true
overview: 'DZPage is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Gaming, DayZ, Database, and Tools.


  The DZPage catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 75
  extends:
  - spectral:oas
  name: DZPage API Rules
  rule_count: 34
  severity_counts:
    error: 32
    hint: 0
    info: 1
    warn: 1
  slug: dzpage-com-rules
score:
  band: emerging
  composite: 11.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.8
    catalog_earned_first_party: 0.0
    catalog_gap: 68.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
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
  name: Dzpage Com Domain Security
  slug: dzpage-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: dzpage-com
tags:
- Gaming
- DayZ
- Database
- Tools
website: https://dzpage.com/
---
