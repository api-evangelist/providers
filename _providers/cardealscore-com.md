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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Cardealscore Com Agentic Access
  operation_count: 5
  slug: cardealscore-com-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://cardealscore.com
  baseurl_source: declared
  description: The Explain API from DealScore — 1 operation(s) for explain.
  name: DealScore Explain API
  slug: cardealscore-com-explain-api
- baseURL: https://cardealscore.com
  baseurl_source: declared
  description: The Health API from DealScore — 1 operation(s) for health.
  name: DealScore Health API
  slug: cardealscore-com-health-api
- baseURL: https://cardealscore.com
  baseurl_source: declared
  description: The Quote Check API from DealScore — 1 operation(s) for quote check.
  name: DealScore Quote Check API
  slug: cardealscore-com-quote-check-api
- baseURL: https://cardealscore.com
  baseurl_source: declared
  description: The Score API from DealScore — 1 operation(s) for score.
  name: DealScore Score API
  slug: cardealscore-com-score-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/cardealscore-com/agentic-access/cardealscore-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cardealscore-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cardealscore-com/plans/cardealscore-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardealscore-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cardealscore-com/rules/cardealscore-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cardealscore-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cardealscore-com/json-ld/cardealscore-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cardealscore-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cardealscore-com/vocabulary/cardealscore-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cardealscore-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cardealscore-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cardealscore-com/data-model/cardealscore-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cardealscore-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/cardealscore-com/authentication/cardealscore-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cardealscore-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/cardealscore-com/errors/cardealscore-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cardealscore-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cardealscore-com/conformance/cardealscore-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cardealscore-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cardealscore-com/llms/cardealscore-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardealscore-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/cardealscore-com/well-known/cardealscore-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cardealscore-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cardealscore-com/hosts/cardealscore-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardealscore-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardealscore-com/vendors/cardealscore-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardealscore-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://cardealscore.com/login
- group: auth
  href: https://artifacts.apis.io/cardealscore-com/security/cardealscore-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardealscore-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardealscore.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cardealscore.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://cardealscore.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://cardealscore.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardealscore.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardealscore.com/privacy
created: '2026-11-03'
description: DealScore provides a used‑car price checking MCP tool for AI agents. It grades an asking price against live dealer listings, returning a score from 0 to 100 and a price band. The service is operated by DealScore and offers a REST API for scoring deals, with documentation, pricing, and integration guides for popular AI coding assistants.
image: https://cardealscore.com/opengraph-image.jpg?opengraph-image.0-_4hdth94do2.jpg
json_schemas:
- name: QuoteReport
  property_count: 5
  slug: cardealscore-com-quote-report
jsonld:
- class_count: 9
  name: Cardealscore Com Context
  property_count: 13
  slug: cardealscore-com-context
layout: provider
modified: '2026-11-03'
name: DealScore
nav: Providers
network: true
overview: 'DealScore publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Explain API, Health API, Quote Check API, and 1 more. Tagged areas include Company, UsedCar, Artificial Intelligence, Pricing, and MCP.


  The DealScore catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DealScore''s developer surface includes authentication, documentation, API reference, pricing, and 18 more developer resources.'
plans:
- name: Cardealscore Com Plans Pricing
  plan_count: 2
  slug: cardealscore-com-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: DealScore API Rules
  rule_count: 54
  severity_counts:
    error: 50
    hint: 0
    info: 3
    warn: 1
  slug: cardealscore-com-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 67.2
    catalog_earned_first_party: 8.0
    catalog_gap: 47.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 59.5
    developer_ergonomics: 22.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Cardealscore Com Authentication
  slug: cardealscore-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Cardealscore Com Domain Security
  slug: cardealscore-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: cardealscore-com-score-and-explain
  slug: cardealscore-com-score-and-explain
slug: cardealscore-com
tags:
- Company
- UsedCar
- Artificial Intelligence
- Pricing
- MCP
website: https://cardealscore.com/
---
