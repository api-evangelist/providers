---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The LiquidTrust API lets platform partners embed conditional payment logic - Micro Escrow(R) holds, milestone approvals, and rule-based release - directly into their own product, with LiquidTrust hand
  name: LiquidTrust API
  slug: api
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/liquidtrust-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/liquidtrust-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.liquidtrust.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.liquidtrust.io/knowledge-base
- group: operate
  title: ''
  type: Support
  url: https://www.liquidtrust.io/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.liquidtrust.io/knowledge-base
- group: company
  title: ''
  type: Blog
  url: https://liquidtrust.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liquidtrust.io/pricing
- group: start
  title: ''
  type: Login
  url: https://www.liquidtrust.io/login
- group: start
  title: ''
  type: SignUp
  url: https://www.liquidtrust.io/talk-to-sales
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquidtrust.io/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquidtrust.io/privacy
- group: auth
  title: ''
  type: Security
  url: https://www.liquidtrust.io/security
- group: operate
  title: ''
  type: StatusPage
  url: https://status.liquidtrust.io/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.liquidtrust.io/
- group: auth
  title: ''
  type: Compliance
  url: https://www.liquidtrust.io/security
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/liquidtrust-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/liquidtrust-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/liquidtrust-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/liquidtrust-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/liquidtrust-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/liquidtrust-llms.txt
created: '2026-07-17'
description: LiquidTrust, operated by Liquid Global, Inc., is a B2B payments platform that embeds trust and conditionality directly into the payment flow. Its core product, Micro Escrow(R), holds funds and releases them against defined conditions such as milestones, approvals, and deliveries, giving buyers and sellers recourse without a traditional escrow agent. The platform bundles KYC/KYB, AML and sanctions screening into the payment rails and settles to 200+ countries, with J.P. Morgan named as a payment-rails partner. LiquidTrust is sold to marketplaces, banks, and platform partners through three integration models - referral, white-label, and a direct API integration that embeds conditional payment logic into a partner platform. Pricing is a flat 1% all-in per protected transaction, with a $10 flat Simple Pay option for lower-risk transfers. The API surface at api.liquidtrust.io is live but access-gated behind sales onboarding; no public developer portal, OpenAPI description, SDKs,
  or sandbox documentation is published at this time.
image: https://liquidtrust.io/lt-social-card.png
layout: provider
modified: '2026-07-19'
name: LiquidTrust
nav: Providers
network: true
overview: 'LiquidTrust publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, B2B Payments, Escrow, and Fintech.


  LiquidTrust''s developer surface includes documentation, support, engineering blog, pricing, signup flow, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 34.3
  delta: 5.5
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 28.8
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 65.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: rising
security:
- kind: domain-security
  name: Liquidtrust Domain Security
  slug: liquidtrust-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Liquidtrust Vulnerability Disclosure
  slug: liquidtrust-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Liquidtrust Trust Center
  slug: liquidtrust-trust-center
  summary_line: SOC 2 Type II, ISO 27001, PCI DSS, GDPR, CCPA
slug: liquidtrust
tags:
- Company
- Payments
- B2B Payments
- Escrow
- Fintech
- Cross-Border Payments
- Marketplaces
- Compliance
- KYC
- Trust and Safety
website: https://www.liquidtrust.io/
---
