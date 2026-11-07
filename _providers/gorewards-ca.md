---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: documented
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'GoRewards API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: GoRewards API
  slug: gorewards-ca-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/gorewards-ca/plans/gorewards-ca-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gorewards-ca-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/gorewards-ca/rules/gorewards-ca-rules.yml
  title: ''
  type: Spectral
  url: rules/gorewards-ca-rules.yml
- group: design
  href: https://artifacts.apis.io/gorewards-ca/json-ld/gorewards-ca-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gorewards-ca-context.jsonld
- group: design
  href: https://artifacts.apis.io/gorewards-ca/vocabulary/gorewards-ca-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gorewards-ca-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/gorewards-ca/data-model/gorewards-ca-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gorewards-ca-data-model.yml
- group: design
  href: https://artifacts.apis.io/gorewards-ca/conformance/gorewards-ca-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gorewards-ca-conformance.yml
- group: agent
  href: https://artifacts.apis.io/gorewards-ca/llms/gorewards-ca-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gorewards-ca-llms.txt
- group: other
  href: https://artifacts.apis.io/gorewards-ca/a2a/gorewards-ca-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/gorewards-ca-a2a.yml
- group: agent
  href: https://artifacts.apis.io/gorewards-ca/well-known/gorewards-ca-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gorewards-ca-well-known.yml
- group: other
  href: https://artifacts.apis.io/gorewards-ca/hosts/gorewards-ca-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gorewards-ca-hosts.yml
- group: other
  href: https://artifacts.apis.io/gorewards-ca/vendors/gorewards-ca-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gorewards-ca-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gorewards.ca/terms
- group: start
  title: ''
  type: SignUp
  url: https://gorewards.ca/cards/best-for/signup-bonus
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gorewards.ca/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://gorewards.ca/pricing
- group: company
  title: ''
  type: Blog
  url: https://gorewards.ca/blog
- group: auth
  href: https://artifacts.apis.io/gorewards-ca/security/gorewards-ca-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gorewards-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gorewards.ca
- group: docs
  title: ''
  type: Documentation
  url: https://gorewards.ca/data
coverage:
  checked: '2026-11-04'
  detail: Documentation provides a field dictionary but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL spec.
  evidence:
  - status: 200
    url: https://gorewards.ca/data
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: GoRewards provides a Canadian credit‑card rewards calculator that helps users compare cards based on spending habits, caps, bonuses and fees. The service is independent, free to use and does not require an account. It aggregates publicly available card terms to let consumers see which card maximizes their rewards under real‑world limits. The platform also shares details on how it is funded and its data sources, aiming for transparency in the Canadian financial‑services space.
image: https://gorewards.ca/api/og?title=Which+Card+Earns+You+the+Most%3F&subtitle=Canadian+credit+card+rewards+calculator
json_schemas:
- name: GetApiV1CardsResponse
  property_count: 23
  slug: gorewards-ca-get-api-v1-cards-response
jsonld:
- class_count: 1
  name: Gorewards Ca Context
  property_count: 23
  slug: gorewards-ca-context
layout: provider
modified: '2026-11-04'
name: GoRewards
nav: Providers
network: true
overview: 'GoRewards is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Credit Cards, Canada, and Rewards.


  The GoRewards catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GoRewards'' developer surface includes signup flow, pricing, engineering blog, documentation, and 15 more developer resources.'
plans:
- name: Gorewards Ca Plans Pricing
  plan_count: 3
  slug: gorewards-ca-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: GoRewards API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: gorewards-ca-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 63.2
    catalog_earned_first_party: 12.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 19.5
    developer_ergonomics: 11.9
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 29.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gorewards Ca Domain Security
  slug: gorewards-ca-domain-security
  summary_line: TLSv1.3 · HSTS
slug: gorewards-ca
tags:
- Company
- Finance
- Credit Cards
- Canada
- Rewards
website: https://gorewards.ca
---
