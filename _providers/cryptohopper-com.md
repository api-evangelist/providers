---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API documentation for Cryptohopper platform
  name: Cryptohopper API
  slug: cryptohopper-api
- baseURL: https://api.cryptohopper.com
  baseurl_source: declared
  description: 'Cryptohopper API as documented publicly: 10 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Cryptohopper API
  slug: cryptohopper-com-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/cryptohopper-com/plans/cryptohopper-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptohopper-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cryptohopper-com/rules/cryptohopper-com-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptohopper-com-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptohopper-com/json-ld/cryptohopper-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptohopper-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptohopper-com/vocabulary/cryptohopper-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptohopper-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptohopper-com/data-model/cryptohopper-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptohopper-com-data-model.yml
- group: build
  href: https://artifacts.apis.io/cryptohopper-com/cli/cryptohopper-com-cli.yml
  title: ''
  type: CLI
  url: cli/cryptohopper-com-cli.yml
- group: design
  href: https://artifacts.apis.io/cryptohopper-com/conformance/cryptohopper-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptohopper-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cryptohopper-com/llms/cryptohopper-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptohopper-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/cryptohopper-com/well-known/cryptohopper-com-support-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cryptohopper-com-support-security.txt
- group: agent
  href: https://artifacts.apis.io/cryptohopper-com/well-known/cryptohopper-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cryptohopper-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/cryptohopper-com/hosts/cryptohopper-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptohopper-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptohopper-com/vendors/cryptohopper-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptohopper-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/cryptohopper-com/packages/cryptohopper-com-packages.yml
  title: ''
  type: SDKs
  url: packages/cryptohopper-com-packages.yml
- group: build
  href: https://artifacts.apis.io/cryptohopper-com/packages/cryptohopper-com-packages.yml
  title: ''
  type: Packages
  url: packages/cryptohopper-com-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.cryptohopper.com/api-documentation/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cryptohopper.com/terms
- group: operate
  title: ''
  type: Support
  url: https://support.cryptohopper.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cryptohopper.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cryptohopper.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.cryptohopper.com/news
- group: start
  title: ''
  type: Login
  url: https://www.cryptohopper.com/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cryptohopper.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.cryptohopper.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.cryptohopper.com/api-documentation/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cryptohopper.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cryptohopper
- group: auth
  href: https://artifacts.apis.io/cryptohopper-com/security/cryptohopper-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptohopper-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptohopper.com/
coverage:
  checked: '2026-11-04'
  detail: Documentation is markdown without a published OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://docs.cryptohopper.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Cryptohopper is the world’s leading cryptocurrency trading bot platform, enabling automated trading across 10 exchanges with AI‑powered strategies, copy trading, DCA, and advanced tools for traders of all levels. Founded in 2017 in Amsterdam, it serves worldwide users.
image: https://cdn.sanity.io/images/oxjt6901/production/a98f54631cf3114cc407140890e1e208cb850873-2400x1260.jpg?w=1200&h=630
json_schemas:
- name: GetHopperIdResponse
  property_count: 2
  slug: cryptohopper-com-get-hopper-id-response
- name: GetV1HopperResponse
  property_count: 2
  slug: cryptohopper-com-get-v1-hopper-response
- name: PostV1HopperRequest
  property_count: 6
  slug: cryptohopper-com-post-v1-hopper-request
- name: PostV1HopperResponse
  property_count: 1
  slug: cryptohopper-com-post-v1-hopper-response
jsonld:
- class_count: 4
  name: Cryptohopper Com Context
  property_count: 11
  slug: cryptohopper-com-context
layout: provider
modified: '2026-11-04'
name: Cryptohopper
nav: Providers
network: true
overview: 'Cryptohopper is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Crypto Trading Bot, Automated Trading, Social Trading, and AI Trading.


  The Cryptohopper catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cryptohopper''s developer surface includes CLI, support, pricing, engineering blog, API reference, documentation, and 22 more developer resources.'
plans:
- name: Cryptohopper Com Plans Pricing
  plan_count: 3
  slug: cryptohopper-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Cryptohopper API Rules
  rule_count: 39
  severity_counts:
    error: 35
    hint: 0
    info: 1
    warn: 3
  slug: cryptohopper-com-rules
score:
  band: developing
  composite: 42.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 22.1
    developer_ergonomics: 47.6
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
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
- kind: domain-security
  name: Cryptohopper Com Domain Security
  slug: cryptohopper-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cryptohopper-com
tags:
- Crypto Trading Bot
- Automated Trading
- Social Trading
- AI Trading
website: https://cryptohopper.com/
---
