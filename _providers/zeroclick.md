---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.7
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://zeroclick.ai
- group: docs
  title: ''
  type: Documentation
  url: https://zeroclick.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://zeroclick.ai/docs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zeroclick.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zeroclick.ai/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/piedotorg
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/piedotorg/zeroclick
- group: build
  title: ''
  type: Packages
  url: packages/zeroclick-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zeroclick-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zeroclick-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zeroclick-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/zeroclick-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zeroclick-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zeroclick-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zeroclick-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zeroclick-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zeroclick-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zeroclick-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zeroclick-llms.txt
created: '2026-07-17'
description: ZeroClick is the agent-first storefront and transaction layer that lets businesses sell directly to AI agents. It turns any existing API or offering into an agent-purchasable service, publishing a machine-readable storefront so agents can discover it and adding agent identity, agent-native payment rails (x402 and MPP, the Machine Payments Protocol), signed proxying, and per-transaction analytics in front of the seller's unchanged upstream API. Sellers keep their product, pricing, and customer experience, add a small guard to billed endpoints via the @zeroclickai/sellers SDK, and settle revenue to their own connected Stripe account. ZeroClick launched in July 2026, raised $55M, is backed by Forerunner Ventures, and is a product of the People's Internet Experiment.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zeroclick.png
layout: provider
modified: '2026-07-21'
name: Zeroclick
nav: Providers
network: true
overview: 'Zeroclick is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Agent Commerce, Agentic Payments, and API Monetization.


  Zeroclick''s developer surface includes documentation, API reference, authentication, and 16 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 21.7
  delta: 1.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 32.6
    discoverability: 57.4
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 19.8
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zeroclick Authentication
  slug: zeroclick-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Zeroclick Domain Security
  slug: zeroclick-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zeroclick
tags:
- Company
- Ai
- Agent Commerce
- Agentic Payments
- API Monetization
- x402
- Machine Payments Protocol
- Agent Identity
- Stripe
website: https://zeroclick.ai
---
