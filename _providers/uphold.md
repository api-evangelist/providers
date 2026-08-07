---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 65.3
  scored_at: '2026-08-06'
api_count: 7
apis:
- description: The primary Uphold Enterprise REST API — users, KYC/KYB processes, capabilities, terms of service, files, countries, assets, networks and rails, accounts, external accounts (bank/card/APM), quotes and
  name: Uphold Enterprise Core API
  slug: uphold-enterprise-core-api
- description: Session API behind the embeddable Uphold Widgets — creates Payment Widget, KYC Widget and Travel Rule Widget sessions that the browser/native SDKs consume to collect payment methods, KYC data and FATF
  name: Uphold Enterprise Widgets API
  slug: uphold-enterprise-widgets-api
- description: Market data API returning descriptive asset information, real-time asset market statistics, per-asset news and general market news for the assets supported on the Uphold platform.
  name: Uphold Market Pulse API
  slug: uphold-market-pulse-api
- description: Ingests verifications performed in third-party identity providers — Sumsub Reusable KYC and Veriff — and maps their payloads onto Uphold KYC processes, so a partner that already verifies users elsewhe
  name: Uphold KYC Connector API
  slug: uphold-kyc-connector-api
- description: KYC-sharing API for Topper, Uphold's fiat-to-crypto onramp widget — identifies a user and creates a KYC sharing session so an existing Uphold verification can be reused inside a Topper integration.
  name: Uphold Topper API
  slug: uphold-topper-api
- description: The long-standing public Uphold API at api.uphold.com/v0 — tickers and exchange rates, supported currencies and assets, plus OAuth 2.0 authenticated access to a member's cards, transactions and accoun
  name: Uphold Public API (v0)
  slug: uphold-public-api-v0
- description: Anonymous, read-only Model Context Protocol server published by Uphold at developer.uphold.com/mcp over streamable HTTP. Exposes three tools (documentation search, a virtualized read-only docs filesys
  name: Uphold Documentation MCP Server
  slug: uphold-documentation-mcp-server
artifact_total: 14
asyncapis:
- description: ''
  name: Uphold Core Webhooks
  slug: uphold-core-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://uphold.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uphold.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uphold.com/rest-apis/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uphold.com/rest-apis/core-api/concepts
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uphold.com/get-started/overview
- group: start
  title: ''
  type: Quickstart
  url: https://developer.uphold.com/get-started/make-your-first-api-call
- group: operate
  title: ''
  type: Support
  url: https://support.uphold.com/
- group: company
  title: ''
  type: Blog
  url: https://uphold.com/en-us/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uphold
- group: commercial
  title: ''
  type: Pricing
  url: https://uphold.com/en-us/get-started/service-fees
- group: start
  title: ''
  type: SignUp
  url: https://portal.enterprise.uphold.com/
- group: start
  title: ''
  type: Login
  url: https://portal.enterprise.uphold.com/
- group: commercial
  title: ''
  type: DeveloperAgreement
  url: https://uphold.com/en-us/legal/developer-agreement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uphold.com/en-us/legal/membership-agreement/usa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uphold.com/en-us/legal/privacy-policy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/uphold/workspace/enterprise-api
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uphold.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.uphold.com/rest-apis/versioning
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/uphold-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uphold-lifecycle.yml
- group: auth
  title: ''
  type: Security
  url: https://uphold.com/en-us/get-started/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uphold-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/uphold-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://uphold.com/en-us/get-started/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uphold-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/uphold-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uphold-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uphold-llms.txt
- group: other
  title: ''
  type: AgentCard
  url: a2a/uphold-a2a.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uphold-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uphold-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uphold-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uphold-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uphold-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uphold-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/uphold-decline-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uphold-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/uphold-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uphold-packages.yml
- group: design
  title: ''
  type: Components
  url: components/uphold-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uphold-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uphold-core-webhooks.yml
created: '2026-08-05'
description: Uphold is a multi-asset digital money platform and regulated crypto exchange that lets consumers and businesses hold, trade, send and spend more than 300 cryptocurrencies, national currencies and precious metals from a single account. Its Enterprise API Suite ("Move on chain") is a modular set of OpenAPI 3.1 REST APIs — Core, Widgets, Topper, Market Pulse and KYC Connector — that partners embed to onboard and KYC/KYB-verify users, move value across bank rails (ACH, FedNow/RTP, Wire, FPS, SEPA), debit and credit cards, alternative payment methods (Apple Pay, PayPal) and 50+ blockchain networks, and to run buy/sell, trade, send, portfolio, statements and FATF Travel Rule flows. Uphold also runs a public legacy market-data and wallet API at api.uphold.com/v0, publishes embeddable Payment, KYC and Travel Rule widgets, a Svix-backed webhook event surface, a full Sandbox with test helpers, a public Postman workspace, an llms.txt, an A2A agent card and a documentation MCP server.
image: https://cdn.prod.website-files.com/65116a8935747aeda81c6865/65a8ffa13ea101b31a905d2f_UPHOLD%20LOGO-2.png
layout: provider
mcp_servers:
- description: ''
  name: uphold-mcp.yml
  slug: uphold-mcpyml
modified: '2026-08-05'
name: Uphold
nav: Providers
network: true
overview: 'Uphold publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Enterprise Core API, Enterprise Widgets API, Market Pulse API, and 2 more. Tagged areas include Company, cryptocurrency, digital-assets, payments, and banking.


  The Uphold catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Uphold''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 36 more developer resources.'
random_paper: 87
scopes:
- name: Uphold Scopes
  scope_count: 64
  slug: uphold-scopes
  summary_line: 64 scopes · clientCredentials
score:
  band: exemplar
  composite: 68.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 75.0
    developer_ergonomics: 84.8
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 63.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 74.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
security:
- kind: authentication
  name: Uphold Authentication
  slug: uphold-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Uphold Domain Security
  slug: uphold-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Uphold Vulnerability Disclosure
  slug: uphold-vulnerability-disclosure
  summary_line: Intigriti · security.txt · contact published
- kind: trust-center
  name: Uphold Trust Center
  slug: uphold-trust-center
  summary_line: SOC 2 Type 2, ISO 27001, PCI DSS
slug: uphold
tags:
- Company
- cryptocurrency
- digital-assets
- payments
- banking
- fintech
- kyc
- compliance
- crypto-exchange
- market-data
- embedded-finance
- travel-rule
- webhooks
- agent-native
website: https://uphold.com/
---
