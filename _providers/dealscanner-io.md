---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
  score: 5.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Dealscanner Io Agentic Access
  operation_count: 7
  slug: dealscanner-io-agentic-access
  summary_line: 7 operations · 1 acting
api_count: 1
apis:
- description: Programmatic access to DealScanner property deals, investment analysis (BRRRR), sold comps, and area-level investment intelligence.
  name: DealScanner API
  slug: dealscanner-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/dealscanner-io/agentic-access/dealscanner-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dealscanner-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dealscanner-io/rules/dealscanner-io-rules.yml
  title: ''
  type: Spectral
  url: rules/dealscanner-io-rules.yml
- group: design
  href: https://artifacts.apis.io/dealscanner-io/json-ld/dealscanner-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dealscanner-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/dealscanner-io/vocabulary/dealscanner-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dealscanner-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dealscanner-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dealscanner-io/data-model/dealscanner-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dealscanner-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/dealscanner-io/errors/dealscanner-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dealscanner-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dealscanner-io/conformance/dealscanner-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dealscanner-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dealscanner-io/llms/dealscanner-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dealscanner-io-llms.txt
- group: other
  href: https://artifacts.apis.io/dealscanner-io/hosts/dealscanner-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dealscanner-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/dealscanner-io/vendors/dealscanner-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dealscanner-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dealscanner.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dealscanner.io/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://www.dealscanner.io/login
- group: docs
  title: ''
  type: Documentation
  url: https://dev.dealscanner.io/
- group: docs
  title: ''
  type: APIReference
  url: https://www.dealscanner.io/developers
- group: auth
  href: https://artifacts.apis.io/dealscanner-io/authentication/dealscanner-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dealscanner-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dealscanner-io/security/dealscanner-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dealscanner-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dealscanner.io/
created: '2026-11-05'
description: DealScanner analyzes every on‑market single‑family home in Allegheny County against your investment targets. When a property is worth pursuing, we help you assess its condition, refine rehab assumptions and returns, and take you from offer through closing with confidence. The platform provides investors with data‑driven insights to make better real‑estate decisions.
image: https://www.dealscanner.io/static/img/logo/app_logo.png
jsonld:
- class_count: 1
  name: Dealscanner Io Context
  property_count: 1
  slug: dealscanner-io-context
layout: provider
modified: '2026-11-05'
name: DealScanner
nav: Providers
network: true
overview: 'DealScanner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, Investment, Brokerage, and Analytics.


  The DealScanner catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DealScanner''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: DealScanner API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: dealscanner-io-rules
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.8
    catalog_earned_first_party: 0.0
    catalog_gap: 67.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 6.7
    developer_ergonomics: 30.4
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dealscanner Io Authentication
  slug: dealscanner-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Dealscanner Io Domain Security
  slug: dealscanner-io-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: dealscanner-io-api
  slug: dealscanner-io-api
slug: dealscanner-io
tags:
- Company
- Real Estate
- Investment
- Brokerage
- Analytics
website: https://dealscanner.io/
---
