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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 34.6
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: 'Embed B2B payment and financing into a platform: onboard buyers and sellers, create payment requests financed by a finmid loan, create payouts, upload documents, and track repayment. JSON over HTTPS, '
  name: finmid B2B Payments API
  slug: finmid-b2b-payments-api
- description: 'Offer pre-approved, customizable financing to businesses on a platform: real-time offer generation, an embeddable acceptance widget (iframe), business onboarding and KYB, fundings, and business paymen'
  name: finmid Capital API
  slug: finmid-capital-api
artifact_total: 6
asyncapis:
- description: ''
  name: Finmid Webhooks
  slug: finmid-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/finmid-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.finmid.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.finmid.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.finmid.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.finmid.com/reference/api-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.finmid.com/docs/finmid-products
- group: company
  title: ''
  type: Blog
  url: https://finmid.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/finmid
- group: start
  title: ''
  type: SignUp
  url: https://platform.finmid.com
- group: start
  title: ''
  type: Login
  url: https://platform.finmid.com
- group: operate
  title: ''
  type: Support
  url: mailto:support@finmid.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://finmid.com/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://finmid.com/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://finmid.statuspage.io
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/finmid-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/finmid-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/finmid-authentication.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/finmid-sandbox.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/finmid-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/finmid-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/finmid-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/finmid-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/finmid-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/finmid-mcp.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/finmid-data-model.yml
created: '2026-07-17'
description: 'finmid is a Berlin-based embedded lending and B2B payments infrastructure provider that lets software platforms and marketplaces offer financing — cash advances, term loans, and business loans — to their customers across 30+ European markets without becoming a lender or handling the regulatory complexity themselves. finmid exposes two REST APIs: the B2B Payments API (buyer/seller onboarding, payment requests, payouts, and repayment) and the Capital API (pre-approved offer generation, an embeddable acceptance widget, business onboarding/KYB, fundings, and payments). Both APIs are JSON over HTTPS, authenticated with an environment-scoped X-API-Key header, with a separate sandbox environment, HMAC-signed webhooks for asynchronous events, and HTTP Message Signatures (RFC 9421, Ed25519) for platform-provided capital payout execution.'
image: https://finmid.com/icon-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: finmid-mcp.yml
  slug: finmid-mcpyml
modified: '2026-07-19'
name: Finmid
nav: Providers
network: true
overview: 'Finmid publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Embedded Finance, Embedded Lending, B2B Payments, and Fintech.


  The Finmid catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Finmid''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, support, authentication, and 18 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 41.3
  delta: 2.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 22.6
    developer_ergonomics: 67.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 39.0
  regulatory:
    applies: true
    regime: Payments
    regime_id: payments
    score: 54.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Finmid Authentication
  slug: finmid-authentication
  summary_line: apiKey/httpMessageSignatures · 2 schemes
- kind: domain-security
  name: Finmid Domain Security
  slug: finmid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: finmid
tags:
- Company
- Embedded Finance
- Embedded Lending
- B2B Payments
- Fintech
- Lending
- Capital
- Financing
- Payments
- Marketplaces
website: https://www.finmid.com
---
