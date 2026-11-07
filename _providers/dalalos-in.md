---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Reference for the DalalOS REST API providing read‑only Indian stock‑market data via MCP tools.
  name: DalalOS REST API
  slug: dalalos-rest-api
- baseURL: https://mcp.dalalos.in
  baseurl_source: declared
  description: 'DalalOS API as documented publicly: 47 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: DalalOS API
  slug: dalalos-in-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/dalalos-in/plans/dalalos-in-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dalalos-in-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dalalos-in/rules/dalalos-in-rules.yml
  title: ''
  type: Spectral
  url: rules/dalalos-in-rules.yml
- group: design
  href: https://artifacts.apis.io/dalalos-in/json-ld/dalalos-in-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dalalos-in-context.jsonld
- group: design
  href: https://artifacts.apis.io/dalalos-in/vocabulary/dalalos-in-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dalalos-in-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dalalos-in/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dalalos-in/data-model/dalalos-in-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dalalos-in-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dalalos-in/authentication/dalalos-in-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dalalos-in-authentication.yml
- group: design
  href: https://artifacts.apis.io/dalalos-in/conformance/dalalos-in-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dalalos-in-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dalalos-in/llms/dalalos-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dalalos-in-llms.txt
- group: agent
  href: https://artifacts.apis.io/dalalos-in/well-known/dalalos-in-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dalalos-in-well-known.yml
- group: other
  href: https://artifacts.apis.io/dalalos-in/hosts/dalalos-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dalalos-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/dalalos-in/vendors/dalalos-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dalalos-in-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dalalos.in/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dalalos.in/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://dalalos.in/pricing
- group: start
  title: ''
  type: Login
  url: https://dalalos.in/sign-in
- group: docs
  title: ''
  type: Documentation
  url: https://dalalos.in/docs
- group: company
  title: ''
  type: Blog
  url: https://dalalos.in/blog
- group: auth
  href: https://artifacts.apis.io/dalalos-in/security/dalalos-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dalalos-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dalalos.in/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages are JavaScript‑rendered and no OpenAPI or other machine‑readable contract was found.
  evidence:
  - status: 200
    url: https://dalalos.in/docs/rest-api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: DalalOS provides source‑backed Indian stock‑market data for AI assistants. It offers real‑time and historical quotes, financials, shareholding, filings and analytics from NSE/BSE, with free starter tier and paid plans from ₹199/month. The service is MCP‑compatible, enabling AI tools to query market data for research, not investment advice.
image: https://dalalos.in/opengraph-image?1afa43a5a17f900e
json_schemas:
- name: DeleteV1AccountWatchlistSymbolResponse
  property_count: 2
  slug: dalalos-in-delete-v1-account-watchlist-symbol-response
- name: GetV1AccountWatchlistResponse
  property_count: 5
  slug: dalalos-in-get-v1-account-watchlist-response
- name: PostV1AccountWatchlistRequest
  property_count: 1
  slug: dalalos-in-post-v1-account-watchlist-request
- name: PostV1AccountWatchlistResponse
  property_count: 2
  slug: dalalos-in-post-v1-account-watchlist-response
jsonld:
- class_count: 4
  name: Dalalos In Context
  property_count: 8
  slug: dalalos-in-context
layout: provider
modified: '2026-11-04'
name: DalalOS
nav: Providers
network: true
overview: 'DalalOS is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Data, Artificial Intelligence, and Stock Market.


  The DalalOS catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DalalOS''s developer surface includes authentication, pricing, documentation, engineering blog, and 16 more developer resources.'
plans:
- name: Dalalos In Plans Pricing
  plan_count: 3
  slug: dalalos-in-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: DalalOS API Rules
  rule_count: 45
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 2
  slug: dalalos-in-rules
score:
  band: thin
  composite: 36.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 30.2
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dalalos In Authentication
  slug: dalalos-in-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dalalos In Domain Security
  slug: dalalos-in-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dalalos-in
tags:
- Company
- Finance
- Data
- Artificial Intelligence
- Stock Market
- MCP
website: https://dalalos.in/
---
