---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public company filing data API as described in the developer reference.
  name: Financial Filings API
  slug: financial-filings-api
artifact_total: 11
asyncapis:
- description: ''
  name: Financialfilings Com Webhooks
  slug: financialfilings-com-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/financialfilings-com/plans/financialfilings-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/financialfilings-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/rules/financialfilings-com-rules.yml
  title: ''
  type: Spectral
  url: rules/financialfilings-com-rules.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/json-ld/financialfilings-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/financialfilings-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/financialfilings-com/vocabulary/financialfilings-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/financialfilings-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/asyncapi/financialfilings-com-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/financialfilings-com-webhooks.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/data-model/financialfilings-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/financialfilings-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/financialfilings-com-vulnerability-disclosure.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/errors/financialfilings-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/financialfilings-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/financialfilings-com/conformance/financialfilings-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/financialfilings-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/financialfilings-com/llms/financialfilings-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/financialfilings-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/financialfilings-com-security.txt
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-chatgpt-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/financialfilings-com-chatgpt-security.txt
- group: agent
  href: https://artifacts.apis.io/financialfilings-com/well-known/financialfilings-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/financialfilings-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/financialfilings-com/hosts/financialfilings-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/financialfilings-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/financialfilings-com/vendors/financialfilings-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/financialfilings-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://financialfilings.com/accounts/login/?next=%2Faccounts%2Fapi-dashboard%2F%3Fsource%3Dnavbar&source=navbar
- group: operate
  title: ''
  type: ChangeLog
  url: https://financialfilings.com/developers/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://financialfilings.com/mcp/
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/financialfilings-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/financialfilings-com/security/financialfilings-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/financialfilings-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://financialfilings.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://financialfilings.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://financialfilings.com/developers/reference/
- group: docs
  title: ''
  type: APIReference
  url: https://financialfilings.com/api-solutions/
- group: commercial
  title: ''
  type: Pricing
  url: https://financialfilings.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://financialfilings.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://financialfilings.com/data-privacy/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.financialfilings.com/mcp
  - status: 200
    url: https://financialfilings.com/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: FinancialFilings provides a comprehensive index of public-company filings worldwide, offering both a free web interface and a typed REST API. Users can search companies, explore filings across 60 markets, and access datasets via JSON, Markdown, or PDF. The platform aggregates data from over 113 sources, supporting analytics, research, and compliance use cases.
image: https://financialfilings.com/og/general.png?title=Everything+public+companies+file%2C&subtitle=in+one+place.&v=2
jsonld:
- class_count: 88
  name: Financialfilings Com Context
  property_count: 224
  slug: financialfilings-com-context
layout: provider
modified: '2026-10-31'
name: FinancialFilings
nav: Providers
network: true
overview: 'FinancialFilings publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Financial Filings API. Tagged areas include Company, Financial Data, Filings, Market Data, and Research.


  The FinancialFilings catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  FinancialFilings'' developer surface includes changelog, getting-started guide, documentation, API reference, pricing, and 22 more developer resources.'
plans:
- name: Financialfilings Com Plans Pricing
  plan_count: 1
  slug: financialfilings-com-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 2
  name: Financialfilings Com Rate Limits
  slug: financialfilings-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: FinancialFilings API Rules
  rule_count: 15
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 3
  slug: financialfilings-com-rules
scopes:
- name: Financialfilings Com Scopes
  scope_count: 0
  slug: financialfilings-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 29
    catalog_earned: 64.8
    catalog_earned_first_party: 16.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 51.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 47.4
  previous_composite: 52.5
  provenance:
    conformance: derived
    contracts:
      callable: 93.8
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 39.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/financialfilings-com/financialfilings-com-2026-11-03T132014.png
security:
- kind: authentication
  name: Financialfilings Com Authentication
  slug: financialfilings-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Financialfilings Com Domain Security
  slug: financialfilings-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Financialfilings Com Vulnerability Disclosure
  slug: financialfilings-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: companies-list
  slug: financialfilings-com-companies-list
slug: financialfilings-com
tags:
- Company
- Financial Data
- Filings
- Market Data
- Research
website: https://financialfilings.com/
---
