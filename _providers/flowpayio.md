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
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: Flowpay's REST partner API for the Fully Embedded (Native) lending flow - customer onboarding and service activation, open-banking account and transaction ingestion, offer request/recalculation/retrie
  name: Flowpay Partner API
  slug: flowpay-partner-api
- description: Partner-implemented endpoint (GET /v1/sales) that supplies Flowpay with a merchant's paginated sales/order history (status, delivery, payment, currency, totals, line items) so Flowpay can score and pe
  name: Flowpay Sales Transactions API
  slug: flowpay-sales-transactions-api
artifact_total: 6
asyncapis:
- description: 'Flowpay notifies partner applications of asynchronous events via HTTPS POST webhooks. Each delivery is signed with an HMAC-SHA256 signature in the `x-flowpay-sig` header and carries an `x-flowpay-ts` '
  name: Flowpay Webhooks
  slug: flowpayio-webhooks-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flowpayio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://flowpay.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.flowpay.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.flowpay.io/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.flowpay.io/specifications/fully-embedded-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.flowpay.io/
- group: company
  title: ''
  type: Blog
  url: https://www.flowpay.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.flowpay.io/contact
- group: start
  title: ''
  type: SignUp
  url: https://my.flowpay.io/signup
- group: start
  title: ''
  type: Login
  url: https://my.flowpay.io/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.flowpay.io/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.flowpay.io/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/flowpay-io
- group: auth
  title: ''
  type: Authentication
  url: authentication/flowpayio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/flowpayio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/flowpayio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/flowpayio-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/flowpayio-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/flowpayio-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/flowpayio-webhooks-asyncapi.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/flowpayio-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/flowpayio-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/flowpayio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/flowpayio-packages.yml
- group: design
  title: ''
  type: Components
  url: components/flowpayio-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/flowpayio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flowpayio-llms.txt
created: '2026-07-17'
description: Flowpay is an embedded-lending fintech that provides fast, flexible, non-purpose financing of up to EUR 100,000 to small and medium-sized businesses across the Czech Republic, Slovakia, and the Netherlands. Its AI-driven platform lets e-commerce, point-of-sale, accounting, and banking partners embed an end-to-end lending journey - customer onboarding and identity verification, open-banking and sales-transaction data ingestion, personalized offer generation, and financing origination, document signing, and repayment - directly into their own products via a REST partner API, hosted iframe/linkout surfaces, and a modular JavaScript/React embed SDK. Authentication is OAuth 2.0 client-credentials (Auth0), with HMAC-SHA256 signed webhooks for customer-scoring and financing-state events. Flowpay is a Techstars-backed company.
image: https://cdn.prod.website-files.com/67f67c483b46bf33a3c28b20/688a66eddaf45373ea01c930_OG%20(2).png
layout: provider
mcp_servers:
- description: ''
  name: flowpayio-mcp.yml
  slug: flowpayio-mcpyml
modified: '2026-07-19'
name: flowpay.io
nav: Providers
network: true
overview: 'flowpay.io publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financing, Lending, Embedded Finance, and Fintech.


  The flowpay.io catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  flowpay.io''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 58
score:
  band: developing
  composite: 42.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 67.4
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 13.2
  previous_composite: 42.1
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/flowpayio/refs/heads/main/screenshots/flowpayio-2026-07-25T214838.png
security:
- kind: authentication
  name: Flowpayio Authentication
  slug: flowpayio-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Flowpayio Domain Security
  slug: flowpayio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: flowpayio
tags:
- Company
- Financing
- Lending
- Embedded Finance
- Fintech
- SME
- Open Banking
- Payments
website: https://flowpay.io/
---
