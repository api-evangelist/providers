---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Dunamu Agentic Access
  operation_count: 40
  slug: dunamu-agentic-access
  summary_line: 40 operations · 11 acting
api_count: 2
apis:
- baseURL_template: https://{region}-api.upbit.com
  baseurl_source: spec_template
  description: The Exchange API from Dunamu — 24 operation(s) for exchange.
  name: Dunamu Exchange API
  slug: dunamu-exchange-api
- baseURL_template: https://{region}-api.upbit.com
  baseurl_source: spec_template
  description: The Quotation API from Dunamu — 12 operation(s) for quotation.
  name: Dunamu Quotation API
  slug: dunamu-quotation-api
artifact_total: 24
common:
- group: other
  href: https://artifacts.apis.io/dunamu/capabilities/dunamu-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dunamu-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/dunamu/agentic-access/dunamu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dunamu-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dunamu/rules/dunamu-rules.yml
  title: ''
  type: Spectral
  url: rules/dunamu-rules.yml
- group: design
  href: https://artifacts.apis.io/dunamu/json-ld/dunamu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dunamu-context.jsonld
- group: design
  href: https://artifacts.apis.io/dunamu/vocabulary/dunamu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dunamu-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dunamu/data-model/dunamu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dunamu-data-model.yml
- group: operate
  href: https://artifacts.apis.io/dunamu/lifecycle/dunamu-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/dunamu-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/dunamu/mcp/dunamu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dunamu-mcp.yml
- group: other
  href: https://artifacts.apis.io/dunamu/hosts/dunamu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dunamu-hosts.yml
- group: other
  href: https://artifacts.apis.io/dunamu/vendors/dunamu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dunamu-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://dunamu.com/esg/management
- group: commercial
  title: ''
  type: Pricing
  url: https://global-docs.upbit.com/docs/api-key
- group: auth
  href: https://artifacts.apis.io/dunamu/security/dunamu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dunamu-domain-security.yml
- group: build
  href: https://artifacts.apis.io/dunamu/packages/dunamu-packages.yml
  title: ''
  type: Packages
  url: packages/dunamu-packages.yml
- group: build
  href: https://artifacts.apis.io/dunamu/packages/dunamu-packages.yml
  title: ''
  type: SDKs
  url: packages/dunamu-packages.yml
- group: build
  href: https://artifacts.apis.io/dunamu/cli/dunamu-cli.yml
  title: ''
  type: CLI
  url: cli/dunamu-cli.yml
- group: agent
  href: https://artifacts.apis.io/dunamu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/dunamu/changelog/dunamu-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/dunamu-changelog.yml
- group: design
  href: https://artifacts.apis.io/dunamu/lifecycle/dunamu-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dunamu-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dunamu/conformance/dunamu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dunamu-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.dunamu.com/en/about/company
- group: auth
  href: https://artifacts.apis.io/dunamu/authentication/dunamu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dunamu-authentication.yml
- group: design
  href: https://artifacts.apis.io/dunamu/conventions/dunamu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dunamu-conventions.yml
- group: design
  href: https://artifacts.apis.io/dunamu/conventions/dunamu-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/dunamu-conventions.yml
- group: design
  href: https://artifacts.apis.io/dunamu/errors/dunamu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dunamu-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/dunamu/rate-limits/dunamu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dunamu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dunamu/plans/dunamu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dunamu-plans-pricing.yml
- group: company
  title: ''
  type: Website
  url: https://dunamu.com/
- group: company
  title: ''
  type: About
  url: https://dunamu.com/about/company
- group: start
  title: ''
  type: DeveloperPortal
  url: https://global-docs.upbit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://global-docs.upbit.com/reference
- group: docs
  title: ''
  type: APIReference
  url: https://global-docs.upbit.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://global-docs.upbit.com/docs/first-exchange-api-call
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/upbit-official
- group: company
  title: ''
  type: Blog
  url: https://blog.naver.com/dunamupr
- group: company
  title: ''
  type: News
  url: https://dunamu.com/news
- group: operate
  title: ''
  type: Support
  url: https://upbitcare.com
- group: company
  title: ''
  type: Careers
  url: https://dunamu.com/careers/jobs
- group: company
  title: ''
  type: InvestorRelations
  url: https://dunamu.com/ir/announcement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://upbit.com/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://upbit.com/privacy_policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://global-docs.upbit.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: https://global-docs.upbit.com/reference/auth
- group: operate
  title: ''
  type: RateLimits
  url: https://global-docs.upbit.com/reference/rate-limits
- group: start
  title: ''
  type: SignUp
  url: https://sg.upbit.com/signup
- group: agent
  title: ''
  type: LLMsTxt
  url: https://global-docs.upbit.com/llms.txt
created: '2026-08-12'
description: Dunamu Inc. (두나무 주식회사) is a South Korean fintech and blockchain company founded in April 2012 and headquartered at 369 Gangnam-daero, Seocho-gu, Seoul. Dunamu operates Upbit, Korea's largest digital asset exchange (launched 2017, the country's first registered VASP), and Stockplus, a securities trading application launched in 2014, alongside Stockplus Unlisted for pre-IPO share trading. The group also spun out Lambda256 (blockchain infrastructure, now trading as Nodit) in 2019 and runs the Dunamu & Partners venture arm. Dunamu itself publishes no developer program at dunamu.com — its entire public API surface is served under the Upbit brand through the Upbit Developer Center, which offers REST and WebSocket APIs for market data, orders, accounts, deposits, withdrawals and Travel Rule compliance, plus first-party Python, TypeScript and Go SDKs, a CLI and packaged agent skills published from the upbit-official GitHub organization. That API surface is catalogued separately at the
  Upbit provider profile; this record profiles the corporate parent.
finops:
- has_sources: true
  method: derived
  name: Dunamu Finops
  primary_unit: ''
  service_category: ''
  slug: dunamu-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
json_schemas:
- name: CandleDay
  property_count: 13
  slug: dunamu-candle-day
- name: Candle
  property_count: 9
  slug: dunamu-candle
- name: Deposit
  property_count: 11
  slug: dunamu-deposit
- name: Market
  property_count: 3
  slug: dunamu-market
- name: OrderChance
  property_count: 7
  slug: dunamu-order-chance
- name: Order
  property_count: 21
  slug: dunamu-order
- name: Orderbook
  property_count: 6
  slug: dunamu-orderbook
- name: Ticker
  property_count: 24
  slug: dunamu-ticker
- name: Trade
  property_count: 10
  slug: dunamu-trade
- name: WithdrawAddress
  property_count: 10
  slug: dunamu-withdraw-address
- name: WithdrawChance
  property_count: 4
  slug: dunamu-withdraw-chance
- name: Withdraw
  property_count: 12
  slug: dunamu-withdraw
jsonld:
- class_count: 27
  name: Dunamu Context
  property_count: 111
  slug: dunamu-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.upbit.com over HTTP.
  name: Dunamu MCP Server
  slug: dunamu
modified: '2026-08-12'
name: Dunamu
nav: Providers
network: true
overview: 'Dunamu publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Exchange API and Quotation API. Tagged areas include Fintech, Cryptocurrency, Digital Assets, Exchange, and Securities.


  The Dunamu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dunamu''s developer surface includes pricing, CLI, changelog, authentication, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: Dunamu Plans Pricing
  plan_count: 1
  slug: dunamu-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 11
  name: Dunamu Rate Limits
  slug: dunamu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Dunamu API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: dunamu-rules
score:
  band: strong
  composite: 57.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 72.8
    catalog_earned_first_party: 20.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 6.3
  facets:
    access_clarity: 39.5
    contract_governance: 35.6
    contract_quality: 66.7
    developer_ergonomics: 78.6
    discoverability: 60.0
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 50.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dunamu/dunamu-2026-08-17T080906.png
security:
- kind: authentication
  name: Dunamu Authentication
  slug: dunamu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dunamu Domain Security
  slug: dunamu-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: upbit
  slug: dunamu-upbit-skill
slug: dunamu
tags:
- Fintech
- Cryptocurrency
- Digital Assets
- Exchange
- Securities
- Trading
- Blockchain
- South Korea
- Company
website: https://dunamu.com/
---
