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
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dhamma Gift Agentic Access
  operation_count: 16
  slug: dhamma-gift-agentic-access
  summary_line: 16 operations · 3 acting
api_count: 1
apis:
- baseURL: /
  baseurl_source: spec
  description: MCP-сервер для ИИ-агентов
  name: Dhamma.Gift MCP API
  slug: dhamma-gift-mcp-api
- baseURL: /
  baseurl_source: spec
  description: Поиск по ключевому слову
  name: Dhamma.Gift Search API
  slug: dhamma-gift-search-api
- baseURL: /
  baseurl_source: spec
  description: Полный текст сутты для ридера
  name: Dhamma.Gift Text API
  slug: dhamma-gift-text-api
- baseURL: /
  baseurl_source: spec
  description: Оглавление и структура текстов
  name: Dhamma.Gift Toc API
  slug: dhamma-gift-toc-api
- baseURL: /
  baseurl_source: spec
  description: Озвучка (Voice API) — api.dhamma.gift
  name: Dhamma.Gift Tts API
  slug: dhamma-gift-tts-api
- baseURL: /
  baseurl_source: spec
  description: Календарь упосатх
  name: Dhamma.Gift Uposatha API
  slug: dhamma-gift-uposatha-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/dhamma-gift/agentic-access/dhamma-gift-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dhamma-gift-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dhamma-gift/rules/dhamma-gift-rules.yml
  title: ''
  type: Spectral
  url: rules/dhamma-gift-rules.yml
- group: design
  href: https://artifacts.apis.io/dhamma-gift/json-ld/dhamma-gift-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dhamma-gift-context.jsonld
- group: design
  href: https://artifacts.apis.io/dhamma-gift/vocabulary/dhamma-gift-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dhamma-gift-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dhamma-gift/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dhamma-gift/data-model/dhamma-gift-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dhamma-gift-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dhamma-gift/security/dhamma-gift-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/dhamma-gift-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/dhamma-gift/errors/dhamma-gift-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dhamma-gift-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dhamma-gift/conformance/dhamma-gift-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dhamma-gift-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dhamma-gift/llms/dhamma-gift-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dhamma-gift-llms.txt
- group: other
  href: https://artifacts.apis.io/dhamma-gift/hosts/dhamma-gift-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dhamma-gift-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://dhamma.gift/login
- group: docs
  title: ''
  type: Documentation
  url: https://dhamma.gift/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://dhamma.gift/api-docs/
- group: auth
  href: https://artifacts.apis.io/dhamma-gift/security/dhamma-gift-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dhamma-gift-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dhamma-gift/security/dhamma-gift-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dhamma-gift-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dhamma.gift/
created: '2026-11-05'
description: Dhamma.Gift provides an online platform for searching, reading, and listening to the Pali Canon texts. The site offers access to over 600 suttas with translations and audio, organized by collections such as An, Sn, Dn, and Mn. Users can explore the scriptures via a searchable interface, view contextual translations, and listen to recitations, supporting study and practice of Buddhist teachings.
image: https://dhamma.gift/assets/img/og-dhamma-gift-v3.png
json_schemas:
- name: SearchResponse
  property_count: 4
  slug: dhamma-gift-search-response
- name: Segment
  property_count: 7
  slug: dhamma-gift-segment
jsonld:
- class_count: 7
  name: Dhamma Gift Context
  property_count: 36
  slug: dhamma-gift-context
layout: provider
modified: '2026-11-05'
name: Dhamma.Gift
nav: Providers
network: true
overview: 'Dhamma.Gift publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including MCP API, Search API, Text API, and 3 more. Tagged areas include Buddhism, Pali Canon, Texts, Search, and Audio.


  The Dhamma.Gift catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dhamma.Gift''s developer surface includes documentation, API reference, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 81
  extends:
  - spectral:oas
  name: Dhamma.Gift API Rules
  rule_count: 40
  severity_counts:
    error: 35
    hint: 0
    info: 4
    warn: 1
  slug: dhamma-gift-rules
score:
  band: thin
  composite: 30.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 22.0
    contract_quality: 54.1
    developer_ergonomics: 23.1
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: unknown
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
  name: Dhamma Gift Domain Security
  slug: dhamma-gift-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dhamma Gift Vulnerability Disclosure
  slug: dhamma-gift-vulnerability-disclosure
  summary_line: no policy recorded
slug: dhamma-gift
tags:
- Buddhism
- Pali Canon
- Texts
- Search
- Audio
website: https://dhamma.gift/
---
