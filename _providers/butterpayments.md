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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Source-agnostic payment-event ingestion API for payment recovery. Merchants POST standardized successful and failed payment events and payment-method updates; Recover optimizes retry timing and report
  name: Recover Enterprise API
  slug: recover-enterprise-api
artifact_total: 6
asyncapis:
- description: ''
  name: Butterpayments Webhooks
  slug: butterpayments-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://butterpayments.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.services.butterpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.services.butterpayments.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.services.butterpayments.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.services.butterpayments.com/integration-guide
- group: company
  title: ''
  type: Blog
  url: https://butterpayments.com/blog
- group: operate
  title: ''
  type: Support
  url: https://butterpayments.com/faq
- group: commercial
  title: ''
  type: Pricing
  url: https://butterpayments.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://butterpayments.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://butterpayments.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/butterpayments-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/butterpayments-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/butterpayments-webhooks.yml
- group: design
  title: ''
  type: Components
  url: components/butterpayments-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/butterpayments-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/butterpayments-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/butterpayments-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/butterpayments-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/butterpayments-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.butterpayments.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/butterpayments-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/butterpayments-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/butterpayments-well-known.yml
created: '2026-07-17'
description: Butter Payments is a payment recovery and involuntary-churn platform that uses machine learning to recover revenue from failed subscription payments. Its Recover product ingests real-time transaction and payment-method events, optimizes retry timing, and reports outcomes back to merchants via HMAC-SHA256 signed webhooks; Dispute (powered by Verifi) intercepts chargebacks and runs Rapid Dispute Resolution; PaymentScore identifies recoverable failed payments; and a PCI DSS Level 2 Card Vault secures card data behind a secure-iframe element. Butter integrates turnkey with Stripe Billing, Braintree, and Recharge, or directly through the Recover Enterprise API.
image: https://cdn.prod.website-files.com/6570760e6e7b5aa59f8f2452/657b7105d992d17f87a2d0e2_hero-img-m.avif
layout: provider
mcp_servers:
- description: ''
  name: Butterpayments MCP Server
  slug: butterpayments-mcp-server
modified: '2026-07-18'
name: Butterpayments
nav: Providers
network: true
overview: 'Butterpayments publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Payment Recovery, Subscription, and Dunning.


  The Butterpayments catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Butterpayments'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, authentication, and 16 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 46.8
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 18.2
    contract_quality: 45.1
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 46.8
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/butterpayments/refs/heads/main/screenshots/butterpayments-2026-07-25T204125.png
security:
- kind: authentication
  name: Butterpayments Authentication
  slug: butterpayments-authentication
  summary_line: apiKey/http/hmac · 5 schemes
- kind: domain-security
  name: Butterpayments Domain Security
  slug: butterpayments-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: trust-center
  name: Butterpayments Trust Center
  slug: butterpayments-trust-center
  summary_line: SOC 2 Type 2, HIPAA, PCI DSS Level 2
slug: butterpayments
tags:
- Company
- Payments
- Payment Recovery
- Subscription
- Dunning
- Involuntary Churn
- Dispute Prevention
- Chargebacks
- Card Vault
- Fintech
- Machine-Learning
website: https://butterpayments.com
---
