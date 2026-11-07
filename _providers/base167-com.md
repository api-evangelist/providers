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
    agent_card: conformant
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
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Base167 Com Agentic Access
  operation_count: 9
  slug: base167-com-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://base167.com
  baseurl_source: declared
  description: The Check API from BASE167 — 1 operation(s) for check.
  name: BASE167 Check API
  slug: base167-com-check-api
- baseURL: https://base167.com
  baseurl_source: declared
  description: The Games API from BASE167 — 8 operation(s) for games.
  name: BASE167 Games API
  slug: base167-com-games-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/base167-com/agentic-access/base167-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/base167-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/base167-com/rules/base167-com-rules.yml
  title: ''
  type: Spectral
  url: rules/base167-com-rules.yml
- group: design
  href: https://artifacts.apis.io/base167-com/json-ld/base167-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/base167-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/base167-com/vocabulary/base167-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/base167-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/base167-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/base167-com/data-model/base167-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/base167-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://base167.com/terms
- group: design
  href: https://artifacts.apis.io/base167-com/errors/base167-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/base167-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/base167-com/conformance/base167-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/base167-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/base167-com/llms/base167-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/base167-com-llms.txt
- group: other
  href: https://artifacts.apis.io/base167-com/a2a/base167-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/base167-com-a2a.yml
- group: auth
  href: https://artifacts.apis.io/base167-com/well-known/base167-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/base167-com-security.txt
- group: agent
  href: https://artifacts.apis.io/base167-com/well-known/base167-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/base167-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/base167-com/hosts/base167-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/base167-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/base167-com/vendors/base167-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/base167-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://base167.com/terms
- group: auth
  href: https://artifacts.apis.io/base167-com/security/base167-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/base167-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/base167-com/security/base167-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/base167-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://base167.com/
created: '2026-11-02'
description: BASE167 is a blockchain‑based gaming platform that lets users claim free BASE167 tokens and participate in high‑stakes Degen Games. The site offers a claim terminal, token wallet integration, and a prize pool of 300 million BASE167. It provides API endpoints for token transactions, game actions, and user balances, targeting developers building on the Base blockchain ecosystem.
image: https://base167.com/og.png
json_schemas:
- name: Address
  property_count: 0
  slug: base167-com-address
- name: BoardRow
  property_count: 2
  slug: base167-com-board-row
- name: Hex
  property_count: 0
  slug: base167-com-hex
- name: PreparedCall
  property_count: 4
  slug: base167-com-prepared-call
- name: SeasonConfig
  property_count: 29
  slug: base167-com-season-config
- name: SignatureExpiry
  property_count: 0
  slug: base167-com-signature-expiry
jsonld:
- class_count: 4
  name: Base167 Com Context
  property_count: 34
  slug: base167-com-context
layout: provider
modified: '2026-11-02'
name: BASE167
nav: Providers
network: true
overview: 'BASE167 publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Check API and Games API. Tagged areas include Blockchain, Gaming, Cryptocurrency, Tokens, and DegenGames.


  The BASE167 catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: BASE167 API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: base167-com-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 57.2
    developer_ergonomics: 6.4
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Base167 Com Domain Security
  slug: base167-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Base167 Com Vulnerability Disclosure
  slug: base167-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: base167-com
tags:
- Blockchain
- Gaming
- Cryptocurrency
- Tokens
- DegenGames
website: https://base167.com/
---
