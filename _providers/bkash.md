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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: 'REST API for accepting bKash payments — token-based auth (Grant/Refresh Token), Checkout and Tokenized Checkout (create/execute/query payment, create/execute agreement), Refund, Instant Payout (B2C), '
  name: bKash Payment Gateway (PGW)
  slug: bkash-payment-gateway-pgw
artifact_total: 5
asyncapis:
- description: ''
  name: Bkash Webhooks
  slug: bkash-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bkash-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.bka.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.bka.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.bka.sh/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.bka.sh/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bKash-developer
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/bkash-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bkash-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/bkash-authentication.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bkash-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/bkash-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/bkash-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bkash-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/bkash-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bkash-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/bkash-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bkash-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/bkash-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/bkash-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bkash-mcp.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.bka.sh/usage-plan
- group: operate
  title: ''
  type: Support
  url: https://www.bkash.com/en/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bkash.com/en/page/tokenized_checkout
created: '2026-07-17'
description: bKash is Bangladesh's largest mobile financial services (MFS) provider, offering a Payment Gateway (PGW) that lets online and mobile merchants accept bKash wallet payments through secure REST APIs. The developer platform (developer.bka.sh, public beta "Inferno Dragon") documents Checkout (hosted iframe/URL), Tokenized Checkout (agreement-based PIN-only payments), Instant Payout (B2C disbursement), Add Wallet, Auth and Capture, Subscriptions, and real-time webhook Instant Payment Notifications. Integration follows a token-based flow — Grant Token, Create Payment, Execute Payment, Query, Refund — with a self-service sandbox (service-name.sandbox.bka.sh) and production (service-name.pay.bka.sh) environments. bKash is a portfolio company associated with the SoftBank Vision Fund and is majority owned by BRAC Bank, with investment from Ant Group, the Bill & Melinda Gates Foundation, and IFC.
image: https://developer.bka.sh/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: bkash-mcp.yml
  slug: bkash-mcpyml
modified: '2026-07-18'
name: bKash
nav: Providers
network: true
overview: 'bKash publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Payment Gateway, and Mobile Financial Services.


  The bKash catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  bKash''s developer surface includes documentation, API reference, getting-started guide, changelog, authentication, sandbox, pricing, and 16 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 40.4
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 51.6
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 28.9
  previous_composite: 40.4
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bkash/refs/heads/main/screenshots/bkash-2026-07-25T203226.png
security:
- kind: authentication
  name: Bkash Authentication
  slug: bkash-authentication
  summary_line: token/apiKey · 2 schemes
- kind: domain-security
  name: Bkash Domain Security
  slug: bkash-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bkash
tags:
- Company
- Fintech
- Payments
- Payment Gateway
- Mobile Financial Services
- Digital Wallet
- Bangladesh
- Checkout
- Webhooks
website: https://developer.bka.sh/
---
