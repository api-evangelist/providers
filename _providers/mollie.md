---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 70.3
  scored_at: '2026-08-11'
api_count: 2
apis:
- description: The Mollie API is a REST API using HAL (application/hal+json) over HTTPS at api.mollie.com. It covers 124 documented operations across 33 API groups — Payments, Payment Links, Refunds, Chargebacks, Ca
  name: Mollie API
  slug: mollie-api
- description: Mollie's official hosted Model Context Protocol server at mcp.mollie.com/mcp. It exposes Mollie API capabilities to AI agents over streamable HTTP, authenticated with an OAuth 2.0 advanced access toke
  name: Mollie MCP Server
  slug: mollie-mcp
artifact_total: 9
asyncapis:
- description: ''
  name: Mollie Webhooks
  slug: mollie-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mollie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mollie.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.mollie.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mollie.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.mollie.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mollie.com/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://help.mollie.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.mollie.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mollie
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mollie.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.mollie.com/dashboard/signup
- group: start
  title: ''
  type: Login
  url: https://my.mollie.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mollie.com/legal/user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mollie.com/legal/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/molliedev/mollie-api/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mollie.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mollie-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/mollie-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/mollie-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/mollie-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mollie-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/mollie-security.txt
- group: auth
  title: ''
  type: Security
  url: https://www.mollie.com/legal/responsible-disclosure
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/mollie-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/mollie-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.mollie.com/security
- group: design
  title: ''
  type: Conformance
  url: conformance/mollie-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mollie-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/mollie-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mollie-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.mollie.com/changelog
- group: auth
  title: ''
  type: Authentication
  url: authentication/mollie-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/mollie-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mollie-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/mollie-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mollie-problem-types.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/mollie-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/mollie-webhooks.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mollie-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mollie-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/mollie-tool-crosswalk.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/mollie-openapi-original.yml
created: '2026-08-01'
description: Mollie B.V. is a Dutch payment service provider headquartered in Amsterdam that lets businesses across Europe accept online, point-of-sale and recurring payments through a single REST API and hosted checkout. The Mollie API is an HTTP+HAL (application/hal+json) interface at api.mollie.com covering Payments, Payment Links, Refunds, Chargebacks, Captures, Customers, Mandates, Subscriptions, Methods, Sessions, Terminals, Balances, Settlements, Payouts, Invoices, Sales Invoices, Business Accounts, Transfers, Onboarding, Capabilities, Clients, Client Links, Profiles, Organizations, Permissions, Delayed Routing, Verify Payee, Wallets, Webhooks and Webhook Events. Mollie supports European payment methods including iDEAL, Bancontact, SEPA Direct Debit, Klarna, PayPal, Apple Pay, Google Pay, BLIK, Przelewy24, TWINT, Vipps, MobilePay, Swish and cards. Mollie publishes an OpenAPI 3.1 specification, official SDKs for PHP, Node/TypeScript, Python, Ruby, Go, Java and C#/.NET, an OAuth 2.0
  Connect platform for marketplaces, next-gen webhook subscriptions, and a hosted Model Context Protocol server plus an official agent toolkit and Agent Skill for AI-driven integrations.
image: https://www.mollie.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: mollie-mcp.yml
  slug: mollie-mcpyml
modified: '2026-08-01'
name: Mollie
nav: Providers
network: true
overview: 'Mollie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, Financial Services, and Checkout.


  The Mollie catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Mollie''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
random_paper: 62
scopes:
- name: Mollie Scopes
  scope_count: 61
  slug: mollie-scopes
  summary_line: 61 scopes · authorizationCode
score:
  band: strong
  composite: 64.7
  delta: -4.8
  facets:
    commercial_clarity: 60.5
    contract_quality: 68.5
    developer_ergonomics: 84.8
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 55.3
  previous_composite: 69.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 71.9
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mollie/refs/heads/main/screenshots/mollie-2026-08-07T184112.png
security:
- kind: authentication
  name: Mollie Authentication
  slug: mollie-authentication
  summary_line: http/oauth2 · 4 schemes
- kind: domain-security
  name: Mollie Domain Security
  slug: mollie-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Mollie Vulnerability Disclosure
  slug: mollie-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Mollie Trust Center
  slug: mollie-trust-center
  summary_line: SOC 2 Type 2, PCI-DSS Level 1, ISAE 3402 Type 2, GDPR
slug: mollie
tags:
- Company
- Payments
- Fintech
- Financial Services
- Checkout
- Ecommerce
- Subscriptions
- Point of Sale
- Europe
- Netherlands
website: https://www.mollie.com/
---
