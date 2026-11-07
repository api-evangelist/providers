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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Meld Agentic Access
  operation_count: 9
  slug: meld-agentic-access
  summary_line: 9 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api-sb.meld.io
  baseurl_source: spec
  description: The Headless API from Meld.io — 4 operation(s) for headless.
  name: Meld.io Headless API
  slug: meld-headless-api
- baseURL: https://api-sb.meld.io
  baseurl_source: spec
  description: The Retail Ramp API from Meld.io — 5 operation(s) for retail ramp.
  name: Meld.io Retail Ramp API
  slug: meld-retail-ramp-api
artifact_total: 20
asyncapis:
- description: ''
  name: Meld Webhooks
  slug: meld-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/meld/agentic-access/meld-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/meld-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/meld/rules/meld-rules.yml
  title: ''
  type: Spectral
  url: rules/meld-rules.yml
- group: design
  href: https://artifacts.apis.io/meld/json-ld/meld-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/meld-context.jsonld
- group: design
  href: https://artifacts.apis.io/meld/vocabulary/meld-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/meld-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/meld/asyncapi/meld-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/meld-webhooks.yml
- group: design
  href: https://artifacts.apis.io/meld/data-model/meld-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meld-data-model.yml
- group: design
  href: https://artifacts.apis.io/meld/conventions/meld-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/meld-conventions.yml
- group: design
  href: https://artifacts.apis.io/meld/conventions/meld-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meld-conventions.yml
- group: start
  href: https://artifacts.apis.io/meld/sandbox/meld-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/meld-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/meld/authentication/meld-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meld-authentication.yml
- group: design
  href: https://artifacts.apis.io/meld/lifecycle/meld-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meld-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/meld/errors/meld-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meld-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meld/conformance/meld-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meld-conformance.yml
- group: agent
  href: https://artifacts.apis.io/meld/llms/meld-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meld-llms.txt
- group: other
  href: https://artifacts.apis.io/meld/a2a/meld-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/meld-a2a.yml
- group: agent
  href: https://artifacts.apis.io/meld/well-known/meld-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/meld-well-known.yml
- group: other
  href: https://artifacts.apis.io/meld/hosts/meld-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meld-hosts.yml
- group: other
  href: https://artifacts.apis.io/meld/vendors/meld-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meld-vendors.yml
- group: auth
  href: https://artifacts.apis.io/meld/security/meld-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meld-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.meld.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meld.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meld.io/docs/meld-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meld.io/docs/meld-api/getting-started
- group: operate
  title: ''
  type: Support
  url: https://www.meld.io/contact?type=general
- group: company
  title: ''
  type: Blog
  url: https://www.meld.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meld.io/policy/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meld.io/policy/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meld.io/partner-application
created: '2026-10-21'
description: Meld.io provides a modern data integration platform that enables businesses to connect, transform, and orchestrate data flows across a wide variety of sources and destinations. The platform offers real-time streaming, batch processing, and powerful transformation capabilities, all accessible via a robust RESTful API. Meld.io focuses on security, scalability, and ease of use, allowing developers to build data pipelines quickly while maintaining compliance with industry standards. With extensive documentation, SDKs, and support, Meld.io aims to simplify complex data integration challenges for enterprises of all sizes.
image: https://meld.io/images/meld-icon-wordmark.png
json_schemas:
- name: CryptoQuoteRequest
  property_count: 10
  slug: meld-crypto-quote-request
- name: CryptoQuoteResponse20260203
  property_count: 1
  slug: meld-crypto-quote-response20260203
- name: HeadlessOrderOfframpRequest
  property_count: 9
  slug: meld-headless-order-offramp-request
- name: HeadlessOrderOfframpResponse
  property_count: 3
  slug: meld-headless-order-offramp-response
- name: HeadlessOrderOnrampRequest
  property_count: 14
  slug: meld-headless-order-onramp-request
- name: HeadlessOrderOnrampResponse
  property_count: 8
  slug: meld-headless-order-onramp-response
- name: PaymentTransactionListResponse20250304
  property_count: 4
  slug: meld-payment-transaction-list-response20250304
- name: PaymentTransactionResponse20250304
  property_count: 1
  slug: meld-payment-transaction-response20250304
- name: SessionTokenForWidgetRequestV20231219
  property_count: 8
  slug: meld-session-token-for-widget-request-v20231219
- name: SessionTokenResponse
  property_count: 7
  slug: meld-session-token-response
- name: VirtualAccountDepositInstructionsRequest
  property_count: 7
  slug: meld-virtual-account-deposit-instructions-request
- name: VirtualAccountDepositInstructionsResponse
  property_count: 9
  slug: meld-virtual-account-deposit-instructions-response
jsonld:
- class_count: 118
  name: Meld Context
  property_count: 219
  slug: meld-context
layout: provider
modified: '2026-10-21'
name: Meld.io
nav: Providers
network: true
overview: 'Meld.io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Headless API and Retail Ramp API. Tagged areas include Data Integration, Fintech, API Platform, Stablecoins, and Digital Assets.


  The Meld.io catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Meld.io''s developer surface includes sandbox, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 21 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: Meld.io API Rules
  rule_count: 58
  severity_counts:
    error: 54
    hint: 0
    info: 1
    warn: 3
  slug: meld-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 73.7
    developer_ergonomics: 36.9
    discoverability: 55.4
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/meld/meld-2026-11-03T135443.png
security:
- kind: authentication
  name: Meld Authentication
  slug: meld-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Meld Domain Security
  slug: meld-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meld
tags:
- Data Integration
- Fintech
- API Platform
- Stablecoins
- Digital Assets
- Enterprise
website: https://www.meld.io/
---
