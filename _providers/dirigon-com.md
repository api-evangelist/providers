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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Dirigon API as documented publicly: 9 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: Dirigon API
  slug: dirigon-com-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/dirigon-com/plans/dirigon-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dirigon-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dirigon-com/rules/dirigon-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dirigon-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dirigon-com/json-ld/dirigon-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dirigon-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dirigon-com/vocabulary/dirigon-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dirigon-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dirigon-com/data-model/dirigon-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dirigon-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dirigon-com/authentication/dirigon-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dirigon-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dirigon-com/conformance/dirigon-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dirigon-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dirigon-com/llms/dirigon-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dirigon-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dirigon-com/well-known/dirigon-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dirigon-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dirigon-com/hosts/dirigon-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dirigon-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dirigon-com/vendors/dirigon-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dirigon-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dirigon.com/docs/terms.md
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dirigon.com/docs/privacy.md
- group: start
  title: ''
  type: Login
  url: https://dirigon.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://dirigon.com/docs/mcp
- group: start
  title: ''
  type: GettingStarted
  url: https://dirigon.com/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/dirigon-com/security/dirigon-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dirigon-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dirigon.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://dirigon.com/pricing
- group: other
  title: ''
  type: RequestAccess
  url: https://dirigon.com/request-access
- group: other
  title: ''
  type: Agents
  url: https://dirigon.com/agents.md
coverage:
  checked: '2026-11-05'
  detail: The provider's documentation is public but does not publish any machine‑readable OpenAPI, GraphQL SDL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://dirigon.com/docs/mcp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: Dirigon provides a private credit look‑through platform that aggregates SEC EDGAR filings to show what major investment firms such as Blackstone, Blue Owl, Ares and others hold and how they mark the same loan. The service offers searchable data on credit holdings, BDC marks, and detailed manager information, helping analysts and investors understand credit exposure across the market.
image: https://dirigon.com/assets/social/dirigon-card-wide.png?v=20261006
json_schemas:
- name: GetV1FilersFileridResponse
  property_count: 8
  slug: dirigon-com-get-v1-filers-filerid-response
- name: GetV1IssuersIss002537MarksResponse
  property_count: 1
  slug: dirigon-com-get-v1-issuers-iss002537-marks-response
- name: GetV1NonAccrualResponse
  property_count: 1
  slug: dirigon-com-get-v1-non-accrual-response
- name: PostV1McpRequest
  property_count: 3
  slug: dirigon-com-post-v1-mcp-request
jsonld:
- class_count: 4
  name: Dirigon Com Context
  property_count: 13
  slug: dirigon-com-context
layout: provider
modified: '2026-11-05'
name: Dirigon
nav: Providers
network: true
overview: 'Dirigon is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Credit, Data, and SEC.


  The Dirigon catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dirigon''s developer surface includes authentication, documentation, getting-started guide, pricing, and 17 more developer resources.'
plans:
- name: Dirigon Com Plans Pricing
  plan_count: 5
  slug: dirigon-com-plans-pricing
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Dirigon API Rules
  rule_count: 42
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 1
  slug: dirigon-com-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 66.8
    catalog_earned_first_party: 12.0
    catalog_gap: 48.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 33.3
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 28.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dirigon Com Authentication
  slug: dirigon-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Dirigon Com Domain Security
  slug: dirigon-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dirigon-com
tags:
- Company
- Finance
- Credit
- Data
- SEC
website: https://dirigon.com/
---
