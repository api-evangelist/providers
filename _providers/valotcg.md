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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Valotcg Agentic Access
  operation_count: 20
  slug: valotcg-agentic-access
  summary_line: 20 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: 'Ready-to-display answers: identification, recommended price and changes, top movers, most valuable products, comparison, edition overview.'
  name: Valo.Data Analysis API
  slug: valotcg-analysis-api
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: Card search, card sheets, current prices, batches and price history.
  name: Valo.Data Cards API
  slug: valotcg-cards-api
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: Sets and expansions of a game.
  name: Valo.Data Editions API
  slug: valotcg-editions-api
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: Games, card languages, per source coverage and rarity codes. Free.
  name: Valo.Data Games API
  slug: valotcg-games-api
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: Sealed products (boosters, displays, ETB…), prices and history.
  name: Valo.Data Sealed API
  slug: valotcg-sealed-api
- baseURL: https://api.valotcg.com
  baseurl_source: declared
  description: Credits used in the current month. Free; accepts an API key.
  name: Valo.Data Usage API
  slug: valotcg-usage-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/valotcg/agentic-access/valotcg-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/valotcg-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/valotcg/plans/valotcg-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/valotcg-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/valotcg/rules/valotcg-rules.yml
  title: ''
  type: Spectral
  url: rules/valotcg-rules.yml
- group: design
  href: https://artifacts.apis.io/valotcg/json-ld/valotcg-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/valotcg-context.jsonld
- group: design
  href: https://artifacts.apis.io/valotcg/vocabulary/valotcg-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/valotcg-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/valotcg/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/valotcg/data-model/valotcg-data-model.yml
  title: ''
  type: DataModel
  url: data-model/valotcg-data-model.yml
- group: design
  href: https://artifacts.apis.io/valotcg/errors/valotcg-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/valotcg-problem-types.yml
- group: design
  href: https://artifacts.apis.io/valotcg/conformance/valotcg-conformance.yml
  title: ''
  type: Conformance
  url: conformance/valotcg-conformance.yml
- group: agent
  href: https://artifacts.apis.io/valotcg/llms/valotcg-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/valotcg-llms.txt
- group: other
  href: https://artifacts.apis.io/valotcg/hosts/valotcg-hosts.yml
  title: ''
  type: Hosts
  url: hosts/valotcg-hosts.yml
- group: other
  href: https://artifacts.apis.io/valotcg/vendors/valotcg-vendors.yml
  title: ''
  type: Vendors
  url: vendors/valotcg-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://valotcg.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://valotcg.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://valotcg.com/developers/pricing
- group: company
  title: ''
  type: Blog
  url: https://valotcg.com/blog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.valotcg.com\
- group: auth
  href: https://artifacts.apis.io/valotcg/authentication/valotcg-authentication.yml
  title: ''
  type: Authentication
  url: authentication/valotcg-authentication.yml
- group: auth
  href: https://artifacts.apis.io/valotcg/security/valotcg-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/valotcg-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://valotcg.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://valotcg.com/developers/docs
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://api.valotcg.com/mcp
  - status: 200
    url: https://valotcg.com/developers
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: 'Valo.Data is a company surfaced via the API Evangelist harvest backlog (source: new-submission) and added to the network as a stub for full-pipeline profiling.'
image: https://valotcg.com/og-valotcg.png
json_schemas:
- name: CardDetail
  property_count: 19
  slug: valotcg-card-detail
- name: PriceSummary
  property_count: 9
  slug: valotcg-price-summary
- name: SealedDetail
  property_count: 15
  slug: valotcg-sealed-detail
- name: SealedPriceHistory
  property_count: 7
  slug: valotcg-sealed-price-history
- name: TopPriced
  property_count: 7
  slug: valotcg-top-priced
- name: UsageResponse
  property_count: 12
  slug: valotcg-usage-response
jsonld:
- class_count: 48
  name: Valotcg Context
  property_count: 121
  slug: valotcg-context
layout: provider
modified: '2026-11-03'
name: Valo.Data
nav: Providers
network: true
overview: 'Valo.Data publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Analysis API, Cards API, Editions API, and 3 more. Tagged areas include Trading Card Games, Pricing Data, and Vision.


  The Valo.Data catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Valo.Data''s developer surface includes pricing, engineering blog, authentication, documentation, and 17 more developer resources.'
plans:
- name: Valotcg Plans Pricing
  plan_count: 4
  slug: valotcg-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 108
  extends:
  - spectral:oas
  name: Valo.Data API Rules
  rule_count: 67
  severity_counts:
    error: 63
    hint: 0
    info: 1
    warn: 3
  slug: valotcg-rules
score:
  band: thin
  composite: 37.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 24.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Valotcg Authentication
  slug: valotcg-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Valotcg Domain Security
  slug: valotcg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: valotcg-analyze-card-price
  slug: valotcg-analyze-card-price
- name: valotcg-get-card-price-history
  slug: valotcg-get-card-price-history
slug: valotcg
tags:
- Trading Card Games
- Pricing Data
- Vision
website: https://valotcg.com/developers
---
