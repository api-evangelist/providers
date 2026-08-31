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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.1
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Invoicing, payments and credit-control API — customers, invoices, payment requests, direct-debit mandates, payments and signed webhooks.
  name: Adfin API
  slug: adfin-api
artifact_total: 5
asyncapis:
- description: ''
  name: Adfin Webhooks
  slug: adfin-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://adfin.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adfin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adfin.com/docs/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adfin.com/reference/welcome-1
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adfin.com/products/direct-integration/guides/get-started/1_get-access
- group: operate
  title: ''
  type: Support
  url: https://support.adfin.com/en/
- group: company
  title: ''
  type: Blog
  url: https://adfin.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adfin.com/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Adfin-Engineering
- group: commercial
  title: ''
  type: Pricing
  url: https://adfin.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.adfin.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://console.adfin.com/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adfin.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adfin.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/adfin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adfin-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/adfin-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/adfin-webhooks.yml
- group: build
  title: ''
  type: Packages
  url: packages/adfin-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/adfin-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adfin-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adfin-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adfin-well-known.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/adfin-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adfin-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/adfin-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adfin-domain-security.yml
created: '2026-07-17'
description: Adfin is a London-based fintech that combines payment collection and AI-powered credit control so businesses get paid faster. Its developer platform exposes invoicing, payments and credit-control APIs — create and activate invoices, issue payment requests with hosted payment pages, set up direct-debit mandates, and reconcile payments — plus signed webhooks for real-time invoice, mandate and payment events. Authentication is OAuth 2.0 (client-credentials for platforms, authorization-code for biller authorization), with an official Node.js SDK and a first-party MCP server for agent-driven invoicing. Adfin is a portfolio company of Index Ventures.
image: https://assets.adfin.com/frontend-resources/favicon/web-app-manifest-512x512.png
layout: provider
mcp_servers:
- description: ''
  name: Adfin MCP Server
  slug: adfin-mcp-server
modified: '2026-07-17'
name: Adfin
nav: Providers
network: true
overview: 'Adfin publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Payments, Invoicing, and Credit Control.


  The Adfin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Adfin''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, pricing, and 20 more developer resources.'
random_paper: 10
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 38.2
    commercial_clarity: 38.2
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 54.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 45.3
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 51.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adfin/refs/heads/main/screenshots/adfin-2026-07-25T181629.png
security:
- kind: authentication
  name: Adfin Authentication
  slug: adfin-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Adfin Domain Security
  slug: adfin-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: adfin
tags:
- Company
- Fintech
- Payments
- Invoicing
- Credit Control
- Direct Debit
- Billing
- Accounts Receivable
- United Kingdom
website: https://adfin.com
---
