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
  name: Danseici Fr Agentic Access
  operation_count: 2
  slug: danseici-fr-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- baseURL: https://www.danseici.fr
  baseurl_source: declared
  description: The Events API from Danse Ici — 2 operation(s) for events.
  name: Danse Ici Events API
  slug: danseici-fr-events-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/danseici-fr/agentic-access/danseici-fr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/danseici-fr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/danseici-fr/rules/danseici-fr-rules.yml
  title: ''
  type: Spectral
  url: rules/danseici-fr-rules.yml
- group: design
  href: https://artifacts.apis.io/danseici-fr/json-ld/danseici-fr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/danseici-fr-context.jsonld
- group: design
  href: https://artifacts.apis.io/danseici-fr/vocabulary/danseici-fr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/danseici-fr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/danseici-fr/data-model/danseici-fr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/danseici-fr-data-model.yml
- group: design
  href: https://artifacts.apis.io/danseici-fr/errors/danseici-fr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/danseici-fr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/danseici-fr/conformance/danseici-fr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/danseici-fr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/danseici-fr/llms/danseici-fr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/danseici-fr-llms.txt
- group: other
  href: https://artifacts.apis.io/danseici-fr/hosts/danseici-fr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/danseici-fr-hosts.yml
- group: other
  href: https://artifacts.apis.io/danseici-fr/vendors/danseici-fr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/danseici-fr-vendors.yml
- group: auth
  href: https://artifacts.apis.io/danseici-fr/security/danseici-fr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/danseici-fr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://danseici.fr/
created: '2026-11-04'
description: Danse Ici is a Paris‑based platform that aggregates and promotes dance events, classes, workshops and social dancing opportunities across the city. It provides a searchable calendar of salsa, bachata, kizomba and other Latin dance activities, offering details on venues, times, prices and instructors, helping dancers discover where to practice and enjoy dance in Paris.
image: https://www.danseici.fr/opengraph-image?4f100ff0f53e282b
jsonld:
- class_count: 1
  name: Danseici Fr Context
  property_count: 20
  slug: danseici-fr-context
layout: provider
modified: '2026-11-04'
name: Danse Ici
nav: Providers
network: true
overview: 'Danse Ici publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Events API. Tagged areas include Dance, Event, Paris, Community, and Platform.


  The Danse Ici catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 76
  extends:
  - spectral:oas
  name: Danse Ici API Rules
  rule_count: 35
  severity_counts:
    error: 33
    hint: 0
    info: 1
    warn: 1
  slug: danseici-fr-rules
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 16
    catalog_earned: 50.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 46.5
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
  name: Danseici Fr Domain Security
  slug: danseici-fr-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: danseici-fr
tags:
- Dance
- Event
- Paris
- Community
- Platform
website: https://danseici.fr/
---
