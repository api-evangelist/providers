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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 50.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: RESTful API for crypto and stablecoin platforms to onboard end users (KYC/AML), open named and virtual fiat accounts, receive pay-ins and send payouts across GBP, EUR and USD schemes, run FX conversio
  name: Fiat Republic API
  slug: fiat-republic-api
artifact_total: 8
asyncapis:
- description: ''
  name: Fiat Republic Webhooks
  slug: fiat-republic-webhooks
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fiat-republic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/fiat-republic-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiat-republic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fiatrepublic.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fiatrepublic.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.fiatrepublic.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.fiatrepublic.com/reference/create-api-token
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.fiatrepublic.com/docs/authentication-webhook-setup
- group: company
  title: ''
  type: Blog
  url: https://fiatrepublic.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://member.fiatrepublic.com/dashboard
- group: start
  title: ''
  type: Login
  url: https://member.fiatrepublic.com/dashboard
- group: operate
  title: ''
  type: Support
  url: https://fiatrepublic.atlassian.net/servicedesk/customer/portal/4
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fiatrepublic.com/privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fiatrepublic.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.fiatrepublic.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fiat-republic-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://fiatrepublic.com/compliance
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/fiatrepublicdev/fiat-republic-developers/overview
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fiat-republic-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/fiat-republic-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fiat-republic-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fiat-republic-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/fiat-republic-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fiat-republic-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fiat-republic-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fiat-republic-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/fiat-republic-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fiat-republic-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fiat-republic-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fiat-republic-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fiat-republic-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fiat-republic-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fiat-republic-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/fiat-republic-security.txt
created: '2026-07-17'
description: Fiat Republic is a UK- and EU-regulated Banking-as-a-Service provider that gives crypto platforms, exchanges and stablecoin issuers a single API and single liability contract for local fiat rails. Its RESTful API automates end-user onboarding with embedded KYC/AML, named and virtual fiat accounts, pay-ins and payouts across GBP (Faster Payments / CHAPS), EUR (SEPA / SEPA Instant) and USD schemes, FX conversion, Verification of Payee (VoP), returns and recalls, and its Oxygen transaction-monitoring product. Access is via OAuth 2.0 client-credentials with PAYMENTS and OXYGEN scopes, HMAC-SHA256-signed webhooks using the HTTP Message Signatures standard, idempotency keys, and separate sandbox and production environments. Fiat Republic operates as an Electronic Money Institution regulated by the FCA (UK) and De Nederlandsche Bank (NL), with MSB registrations in the US and Canada.
image: https://fiatrepublic.com/images/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: fiat-republic-mcp.yml
  slug: fiat-republic-mcpyml
modified: '2026-07-19'
name: Fiat Republic
nav: Providers
network: true
overview: 'Fiat Republic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Banking, Payments, Fintech, and Cryptocurrency.


  The Fiat Republic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fiat Republic''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, changelog, and 27 more developer resources.'
random_paper: 76
rate_limits:
- limit_count: 7
  name: Fiat Republic Rate Limits
  slug: fiat-republic-rate-limits
scopes:
- name: Fiat Republic Scopes
  scope_count: 2
  slug: fiat-republic-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 55.3
  delta: 0.0
  facets:
    commercial_clarity: 31.6
    contract_quality: 51.6
    developer_ergonomics: 65.2
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 89.5
  previous_composite: 55.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 62.0
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiat-republic/refs/heads/main/screenshots/fiat-republic-2026-07-25T214357.png
security:
- kind: authentication
  name: Fiat Republic Authentication
  slug: fiat-republic-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fiat Republic Domain Security
  slug: fiat-republic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fiat Republic Vulnerability Disclosure
  slug: fiat-republic-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: fiat-republic
tags:
- Company
- Banking
- Payments
- Fintech
- Cryptocurrency
- Stablecoins
- Banking-as-a-Service
- Embedded Finance
- Compliance
- KYC
- SEPA
- Faster Payments
website: https://fiatrepublic.com
---
