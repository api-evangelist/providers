---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Auraspay Com Agentic Access
  operation_count: 10
  slug: auraspay-com-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 2
apis:
- baseURL: https://auraspay.com
  baseurl_source: declared
  description: The Account API from AurasPay — 1 operation(s) for account.
  name: AurasPay Account API
  slug: auraspay-com-account-api
- baseURL: https://auraspay.com
  baseurl_source: declared
  description: The Agent Checkout API from AurasPay — 4 operation(s) for agent checkout.
  name: AurasPay Agent Checkout API
  slug: auraspay-com-agent-checkout-api
- baseURL: https://auraspay.com
  baseurl_source: declared
  description: The Payment Links API from AurasPay — 3 operation(s) for payment links.
  name: AurasPay Payment Links API
  slug: auraspay-com-payment-links-api
- baseURL: https://auraspay.com
  baseurl_source: declared
  description: The Supported Tokens API from AurasPay — 1 operation(s) for supported tokens.
  name: AurasPay Supported Tokens API
  slug: auraspay-com-supported-tokens-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/auraspay-com/agentic-access/auraspay-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/auraspay-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/auraspay-com/plans/auraspay-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auraspay-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/auraspay-com/rules/auraspay-com-rules.yml
  title: ''
  type: Spectral
  url: rules/auraspay-com-rules.yml
- group: design
  href: https://artifacts.apis.io/auraspay-com/json-ld/auraspay-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auraspay-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/auraspay-com/vocabulary/auraspay-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auraspay-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/auraspay-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/auraspay-com/data-model/auraspay-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auraspay-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/auraspay-com/errors/auraspay-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auraspay-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auraspay-com/conformance/auraspay-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auraspay-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auraspay-com/llms/auraspay-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auraspay-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/auraspay-com/well-known/auraspay-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/auraspay-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/auraspay-com/hosts/auraspay-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auraspay-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/auraspay-com/vendors/auraspay-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auraspay-com-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://auraspay.com/trust/about
- group: operate
  title: ''
  type: Support
  url: https://auraspay.com/support
- group: auth
  title: ''
  type: Security
  url: https://auraspay.com/security
- group: start
  title: ''
  type: Login
  url: https://auraspay.com/en/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://auraspay.com/trust/release-notes
- group: auth
  href: https://artifacts.apis.io/auraspay-com/authentication/auraspay-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auraspay-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/auraspay-com/security/auraspay-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auraspay-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auraspay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://auraspay.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://auraspay.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://auraspay.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://auraspay.com/developers#quick-start
- group: commercial
  title: ''
  type: Pricing
  url: https://auraspay.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auraspay.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auraspay.com/privacy-policy
created: '2026-11-02'
description: AurasPay provides a stablecoin and crypto payment gateway allowing individuals and businesses to hold, send, and approve crypto assets via self‑custody wallets. It offers payment links, QR payments, POS, invoicing, payroll payouts, and integrations for online stores, plus AI‑agentic payment capabilities. Developers can access a REST API to integrate crypto payments into applications, supporting multiple networks such as USDC, USDT, SOL, ETH, BTC, TRX, BNB, and EURC.
image: https://auraspay.com/og.png
json_schemas:
- name: AccountResponse
  property_count: 3
  slug: auraspay-com-account-response
- name: CreatePaymentLinkRequest
  property_count: 14
  slug: auraspay-com-create-payment-link-request
- name: PaymentListResponse
  property_count: 3
  slug: auraspay-com-payment-list-response
- name: PaymentResponse
  property_count: 3
  slug: auraspay-com-payment-response
- name: SupportedTokensResponse
  property_count: 3
  slug: auraspay-com-supported-tokens-response
jsonld:
- class_count: 20
  name: Auraspay Com Context
  property_count: 71
  slug: auraspay-com-context
layout: provider
modified: '2026-11-02'
name: AurasPay
nav: Providers
network: true
overview: 'AurasPay publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Agent Checkout API, Payment Links API, and 1 more. Tagged areas include Company, Payments, Cryptocurrency, and Stablecoins.


  The AurasPay catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AurasPay''s developer surface includes support, changelog, authentication, documentation, API reference, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Auraspay Com Plans Pricing
  plan_count: 1
  slug: auraspay-com-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: AurasPay API Rules
  rule_count: 50
  severity_counts:
    error: 47
    hint: 0
    info: 1
    warn: 2
  slug: auraspay-com-rules
score:
  band: developing
  composite: 42.9
  coverage:
    artifact_dirs: 21
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -13.0
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 39.8
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auraspay Com Authentication
  slug: auraspay-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Auraspay Com Domain Security
  slug: auraspay-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: auraspay-com
tags:
- Company
- Payments
- Cryptocurrency
- Stablecoins
website: https://auraspay.com/
---
