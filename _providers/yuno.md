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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Core Yuno Payments API — customers, checkout sessions, payments, refunds, captures, subscriptions, payouts, disputes, reports, banking connectivity and PCI Proxy. Header API-key auth with X-Idempotenc
  name: Yuno Payments API
  slug: yuno-payments-api
artifact_total: 7
asyncapis:
- description: ''
  name: Yuno Webhooks
  slug: yuno-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yuno-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://y.uno
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.y.uno/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.y.uno/docs/your-payment-operative-system
- group: docs
  title: ''
  type: APIReference
  url: https://docs.y.uno/reference/getting-started/api-reference-overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.y.uno/reference/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.y.uno
- group: company
  title: ''
  type: Blog
  url: https://y.uno/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yuno-payments
- group: operate
  title: ''
  type: StatusPage
  url: https://status.y.uno
- group: commercial
  title: ''
  type: TermsOfService
  url: https://y.uno/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://y.uno/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://security.y.uno/
- group: auth
  title: ''
  type: Compliance
  url: https://security.y.uno/
- group: auth
  title: ''
  type: Security
  url: https://security.y.uno/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.y.uno/changelog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/yuno-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yuno-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/yuno-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/yuno-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/yuno-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/yuno-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/yuno-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/yuno-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/yuno-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/yuno-decline-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/yuno-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/yuno-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/yuno-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yuno-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Components
  url: components/yuno-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/yuno-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/yuno-webhooks.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/yuno-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/yuno-changelog.yml
created: '2026-07-17'
description: Yuno is a global payment orchestration platform that lets merchants connect to 1,000+ payment methods, PSPs, anti-fraud, and payout providers through a single API and SDK. Its unified checkout, smart routing, and no-code workflows consolidate a company's payment stack, reduce processing fees, and improve approval rates across markets. Yuno exposes payments, checkout sessions, customers, subscriptions, payouts, disputes, reports, banking connectivity, and a PCI Proxy, plus Web/iOS/Android/React Native/Flutter checkout SDKs, an official MCP server, and an agent toolkit for building agentic payment flows. Yuno is certified to PCI DSS v4.0, SOC 2 Type 2, ISO/IEC 27001, ISO/IEC 27701, GDPR, and is a recognized Visa Service Provider.
image: https://y.uno/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: yuno-mcp.yml
  slug: yuno-mcpyml
modified: '2026-07-21'
name: Yuno
nav: Providers
network: true
overview: 'Yuno publishes 1 API on the [APIs.io](https://apis.io/) network: Payments API. Tagged areas include Company, Payments, Payment Orchestration, Fintech, and Checkout.


  The Yuno catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Yuno''s developer surface includes documentation, API reference, getting-started guide, signup flow, engineering blog, changelog, authentication, and 29 more developer resources.'
random_paper: 7
score:
  band: strong
  composite: 57.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 51.6
    developer_ergonomics: 71.2
    discoverability: 87.0
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 57.0
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 65.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Yuno Authentication
  slug: yuno-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Yuno Domain Security
  slug: yuno-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yuno Vulnerability Disclosure
  slug: yuno-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Yuno Trust Center
  slug: yuno-trust-center
  summary_line: GDPR, ISO/IEC 27001, ISO/IEC 27701, PCI DSS, SOC 2 Type 2, Visa Service Provider
slug: yuno
tags:
- Company
- Payments
- Payment Orchestration
- Fintech
- Checkout
- Payouts
- Subscriptions
- API
website: https://y.uno
---
