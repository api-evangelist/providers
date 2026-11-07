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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bvicrewed Com Agentic Access
  operation_count: 2
  slug: bvicrewed-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- description: Public API for the Islands & Sails BVI crewed catamaran charter fleet. All rates are in USD per week and are all‑inclusive.
  name: Islands & Sails — BVI Charter API
  slug: islands-sails-bvi-charter-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/bvicrewed-com/agentic-access/bvicrewed-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bvicrewed-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/rules/bvicrewed-com-rules.yml
  title: ''
  type: Spectral
  url: rules/bvicrewed-com-rules.yml
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/json-ld/bvicrewed-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bvicrewed-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/vocabulary/bvicrewed-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bvicrewed-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bvicrewed-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/data-model/bvicrewed-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bvicrewed-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/errors/bvicrewed-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bvicrewed-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bvicrewed-com/conformance/bvicrewed-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bvicrewed-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bvicrewed-com/llms/bvicrewed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bvicrewed-com-llms.txt
- group: other
  href: https://artifacts.apis.io/bvicrewed-com/hosts/bvicrewed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bvicrewed-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bvicrewed-com/security/bvicrewed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bvicrewed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bvicrewed.com/
created: '2026-11-03'
description: BVI Crewed offers luxury crewed catamaran charters in the British Virgin Islands. Customers can book hand‑picked yachts with professional crews, sailing to Tortola, Virgin Gorda, Jost Van Dyke and the full BVI. The service provides expert concierge matching, seamless booking, and a premium Caribbean sailing experience for leisure travelers seeking effortless island hopping and bespoke itineraries.
image: https://bvicrewed.com/opengraph.jpg
jsonld:
- class_count: 1
  name: Bvicrewed Com Context
  property_count: 18
  slug: bvicrewed-com-context
layout: provider
modified: '2026-11-03'
name: BVI Crewed
nav: Providers
network: true
overview: 'BVI Crewed is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Yacht Charter, Luxury Travel, Caribbean, BVI, and Sailing.


  The BVI Crewed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: BVI Crewed API Rules
  rule_count: 40
  severity_counts:
    error: 38
    hint: 0
    info: 1
    warn: 1
  slug: bvicrewed-com-rules
score:
  band: emerging
  composite: 12.6
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
    contract_quality: 10.7
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
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
  name: Bvicrewed Com Domain Security
  slug: bvicrewed-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bvicrewed-com
tags:
- Yacht Charter
- Luxury Travel
- Caribbean
- BVI
- Sailing
website: https://bvicrewed.com/
---
