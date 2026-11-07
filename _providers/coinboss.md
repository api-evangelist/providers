---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.coinboss.com
  baseurl_source: declared
  description: 'Coin Boss API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Coin Boss API
  slug: coinboss-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/coinboss/rules/coinboss-rules.yml
  title: ''
  type: Spectral
  url: rules/coinboss-rules.yml
- group: design
  href: https://artifacts.apis.io/coinboss/json-ld/coinboss-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/coinboss-context.jsonld
- group: design
  href: https://artifacts.apis.io/coinboss/vocabulary/coinboss-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/coinboss-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/coinboss/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/coinboss/data-model/coinboss-data-model.yml
  title: ''
  type: DataModel
  url: data-model/coinboss-data-model.yml
- group: design
  href: https://artifacts.apis.io/coinboss/conformance/coinboss-conformance.yml
  title: ''
  type: Conformance
  url: conformance/coinboss-conformance.yml
- group: agent
  href: https://artifacts.apis.io/coinboss/llms/coinboss-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/coinboss-llms.txt
- group: other
  href: https://artifacts.apis.io/coinboss/hosts/coinboss-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coinboss-hosts.yml
- group: other
  href: https://artifacts.apis.io/coinboss/vendors/coinboss-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coinboss-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.coinboss.com/liquidations/TRUST
- group: other
  title: ''
  type: Leadership
  url: https://www.coinboss.com/currencies/TEAM
- group: auth
  href: https://artifacts.apis.io/coinboss/security/coinboss-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coinboss-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coinboss.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.coinboss.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.coinboss.com/api-docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coinboss.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.coinboss.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinboss
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coinboss.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coinboss.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.coinboss.com/api-docs
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://www.coinboss.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: CoinBoss provides real-time crypto derivatives market data, including liquidations, funding rates, open interest, long/short ratios, and spot ETF flows across 25 major exchanges. The platform offers free access to comprehensive analytics and tools for traders and analysts.
image: https://www.coinboss.com/icon.svg
json_schemas:
- name: GetApiLiquidationsOverviewResponse
  property_count: 2
  slug: coinboss-get-api-liquidations-overview-response
jsonld:
- class_count: 1
  name: Coinboss Context
  property_count: 2
  slug: coinboss-context
layout: provider
modified: '2026-11-02'
name: Coin Boss
nav: Providers
network: true
overview: 'Coin Boss is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency, Derivatives, Market Data, and Finance.


  The Coin Boss catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Coin Boss'' developer surface includes documentation, API reference, pricing, support, and 17 more developer resources.'
random_paper: 0
rules:
- authorship: generated
  effective_rule_count: 70
  extends:
  - spectral:oas
  name: Coin Boss API Rules
  rule_count: 29
  severity_counts:
    error: 27
    hint: 0
    info: 1
    warn: 1
  slug: coinboss-rules
scopes:
- name: Coinboss Scopes
  scope_count: 0
  slug: coinboss-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.8
  coverage:
    artifact_dirs: 28
    catalog_earned: 48.2
    catalog_earned_first_party: 0.0
    catalog_gap: 66.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 18.5
    developer_ergonomics: 17.1
    discoverability: 58.0
    operational_transparency: 2.6
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
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Coinboss Authentication
  slug: coinboss-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Coinboss Domain Security
  slug: coinboss-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-liquidations-overview
  slug: coinboss-get-liquidations-overview
slug: coinboss
tags:
- Cryptocurrency
- Derivatives
- Market Data
- Finance
website: https://www.coinboss.com
---
