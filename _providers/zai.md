---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 54
  human_in_the_loop: 0
  name: Zai Agentic Access
  operation_count: 128
  slug: zai-agentic-access
  summary_line: 128 operations · 54 acting
api_count: 4
apis:
- description: Zai's core payments platform API. Onboard users, create and manage wallet accounts, items (transaction records), bank and card accounts, companies, fees, tokens, callbacks and batch transactions to co
  name: Zai Assembly API
  slug: zai-assembly-api
- description: Create and manage Virtual Accounts and PayIDs on the New Payments Platform (NPP), letting platforms receive real-time account-to-account pay-ins to uniquely addressable virtual accounts. OpenAPI 3.0.0
  name: Zai Virtual Accounts and PayIDs API
  slug: zai-virtual-accounts-payid-api
- description: Create and manage PayTo agreements (mandated real-time debits) and initiate payments against them over the New Payments Platform. OpenAPI 3.0.1, version 1.4-external, 10 documented paths, secured with
  name: Zai PayTo API
  slug: zai-payto-api
- description: Asynchronous API for submitting long-running operations and retrieving their results without blocking, complementing the synchronous Assembly API. OpenAPI 3.0.0, version 1.0.0, 3 documented paths, sup
  name: Zai Asynchronous API
  slug: zai-async-api
artifact_total: 14
asyncapis:
- description: ''
  name: Zai Webhooks
  slug: zai-webhooks
collections:
- collection_type: postman
  name: Assembly API
  slug: postman-zai-assembly-api
- collection_type: postman
  name: Asynchronous API
  slug: postman-zai-async-api
- collection_type: postman
  name: PayTo
  slug: postman-zai-payto
- collection_type: postman
  name: Virtual Accounts and PayIDs
  slug: postman-zai-virtual-accounts-payid
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/zai/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zai-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zai-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zai-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hellozai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.hellozai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.hellozai.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.hellozai.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.hellozai.com/docs/developer-checklist
- group: auth
  title: ''
  type: Authentication
  url: https://developer.hellozai.com/reference/token
- group: design
  title: ''
  type: Webhooks
  url: https://developer.hellozai.com/docs/webhooks
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hellozai.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.hellozai.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.hellozai.com/
- group: operate
  title: ''
  type: Support
  url: https://support.hellozai.com/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.hellozai.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hellozai.com/company/policies/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.hellozai.com/company/policies/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.hellozai.com/company/compliance
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hellozai/
- group: build
  title: ''
  type: Packages
  url: packages/zai-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/zai-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zai-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/zai-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/zai-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/zai-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zai-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zai-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zai-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zai-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/zai-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/zai-data-model.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AssemblyPayments
created: '2026-07-24'
description: 'Zai (hellozai.com, formerly Assembly Payments / Assembly) is an Australian payments and Payments-as-a-Service provider headquartered in Melbourne. Zai gives platforms, marketplaces and vertical software companies a programmable way to onboard users, hold funds in managed wallet accounts, collect pay-ins (card, direct debit, BPAY, PayID), and disburse pay-outs across many parties in a single transaction flow. It is API-first: the Assembly API exposes wallet accounts, users, items, transactions, bank accounts, card accounts, fees, callbacks and batch disbursements, layered with Australia''s New Payments Platform rails through dedicated Virtual Accounts / PayID and PayTo APIs, plus an Asynchronous API for long-running operations. Authentication is OAuth2 client-credentials (bearer tokens on PayTo), with a Live and Pre-live (sandbox) environment, webhooks with signature verification, and a developer dashboard. Positioned as the embedded-payments and marketplace-money-movement layer
  for the Australian market and platforms operating there.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: zai-mcp.yml
  slug: zai-mcpyml
modified: '2026-07-24'
name: Zai
nav: Providers
network: true
overview: 'Zai publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assembly API, Virtual Accounts and PayIDs API, PayTo API, and 1 more. Tagged areas include Payments, Australia, Payment Gateway, Payment Processing, and Marketplace Payments.


  The Zai catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zai''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 29 more developer resources.'
random_paper: 92
scopes:
- name: Zai Scopes
  scope_count: 0
  slug: zai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.8
  delta: -2.4
  facets:
    commercial_clarity: 52.6
    contract_quality: 65.1
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 28.9
  previous_composite: 61.2
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 68.8
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: Zai Authentication
  slug: zai-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Zai Domain Security
  slug: zai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zai
tags:
- Payments
- Australia
- Payment Gateway
- Payment Processing
- Marketplace Payments
- Payments-as-a-Service
- Real-Time Payments
- Account-to-Account
- Open Banking
- PayTo
- PayID
- NPP
- Direct Debit
- Digital Wallets
- Payouts
website: https://www.hellozai.com/
---
