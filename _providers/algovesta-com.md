---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for AlgoVesta services, providing endpoints for analytics, webhooks and trading automation.
  name: AlgoVesta API
  slug: algovesta-api
- baseURL: https://api.algovesta.com
  baseurl_source: declared
  description: 'AlgoVesta API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AlgoVesta API
  slug: algovesta-com-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/algovesta-com/plans/algovesta-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/algovesta-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/algovesta-com/rules/algovesta-com-rules.yml
  title: ''
  type: Spectral
  url: rules/algovesta-com-rules.yml
- group: design
  href: https://artifacts.apis.io/algovesta-com/json-ld/algovesta-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/algovesta-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/algovesta-com/vocabulary/algovesta-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/algovesta-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/algovesta-com/data-model/algovesta-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/algovesta-com-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://algovesta.com/security.html#disclosure
- group: auth
  href: https://artifacts.apis.io/algovesta-com/authentication/algovesta-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/algovesta-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/algovesta-com/conformance/algovesta-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/algovesta-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/algovesta-com/llms/algovesta-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/algovesta-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/algovesta-com/well-known/algovesta-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/algovesta-com-security.txt
- group: agent
  href: https://artifacts.apis.io/algovesta-com/well-known/algovesta-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/algovesta-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/algovesta-com/hosts/algovesta-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/algovesta-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/algovesta-com/vendors/algovesta-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/algovesta-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://algovesta.com/terms-of-service.html
- group: operate
  title: ''
  type: Support
  url: https://algovesta.com/help/
- group: start
  title: ''
  type: SignUp
  url: https://algovesta.com/register.html
- group: commercial
  title: ''
  type: Pricing
  url: https://algovesta.com/pricing.html
- group: start
  title: ''
  type: GettingStarted
  url: https://algovesta.com/mcp-trading-server.html
- group: auth
  href: https://artifacts.apis.io/algovesta-com/security/algovesta-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/algovesta-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/algovesta-com/security/algovesta-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/algovesta-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://algovesta.com/
- group: company
  title: ''
  type: Blog
  url: https://algovesta.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AlgoVesta
coverage:
  checked: '2026-11-01'
  detail: Documentation lists API endpoints but provides no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://algovesta.com/docs.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AlgoVesta is a BYOS (Bring Your Own Signal) crypto & forex signal execution/automation SaaS that routes Telegram and TradingView signals to 16 crypto exchanges and MetaTrader 5, available in 13 languages. Pure technical middleware — no financial advice.
image: https://algovesta.com/img/av-metallic.png
json_schemas:
- name: GetApiMcpReceiptsReceiptidVerifyResponse
  property_count: 3
  slug: algovesta-com-get-api-mcp-receipts-receiptid-verify-response
- name: PostApiMcpPoliciesCompileRequest
  property_count: 1
  slug: algovesta-com-post-api-mcp-policies-compile-request
- name: PostExchangeOrderRequest
  property_count: 5
  slug: algovesta-com-post-exchange-order-request
- name: PostWebhookYourtokenRequest
  property_count: 14
  slug: algovesta-com-post-webhook-yourtoken-request
jsonld:
- class_count: 4
  name: Algovesta Com Context
  property_count: 20
  slug: algovesta-com-context
layout: provider
modified: '2026-11-01'
name: AlgoVesta
nav: Providers
network: true
overview: 'AlgoVesta is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Trading, Automation, Cryptocurrency, and Software-as-a-Service.


  The AlgoVesta catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AlgoVesta''s developer surface includes authentication, support, signup flow, pricing, getting-started guide, engineering blog, and 17 more developer resources.'
plans:
- name: Algovesta Com Plans Pricing
  plan_count: 5
  slug: algovesta-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Algovesta Com Rate Limits
  slug: algovesta-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AlgoVesta API Rules
  rule_count: 11
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 2
  slug: algovesta-com-rules
scopes:
- name: Algovesta Com Scopes
  scope_count: 0
  slug: algovesta-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 25
    catalog_earned: 71.8
    catalog_earned_first_party: 12.0
    catalog_gap: 43.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 21.9
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 7.9
  previous_composite: 39.0
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
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 38.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Algovesta Com Authentication
  slug: algovesta-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Algovesta Com Domain Security
  slug: algovesta-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Algovesta Com Vulnerability Disclosure
  slug: algovesta-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: algovesta-com
tags:
- Fintech
- Trading
- Automation
- Cryptocurrency
- Software-as-a-Service
website: https://algovesta.com/
---
