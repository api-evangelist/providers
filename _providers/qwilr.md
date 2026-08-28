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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.4
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: REST API for programmatically creating and managing Qwilr pages (proposals, quotes, contracts, reports) from templates and saved blocks, managing quote taxes, listing payment gateways and users, and s
  name: Qwilr API
  slug: qwilr-api
artifact_total: 8
asyncapis:
- description: ''
  name: Qwilr Webhooks
  slug: qwilr-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://qwilr.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.qwilr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qwilr.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.qwilr.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.qwilr.com/docs/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://help.qwilr.com/
- group: company
  title: ''
  type: Blog
  url: https://qwilr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://qwilr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.qwilr.com/#/signup
- group: start
  title: ''
  type: Login
  url: https://app.qwilr.com/#/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://qwilr.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://qwilr.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.qwilr.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://product.qwilr.com/Qwilr-Product-Updates-2025-ZmP5Cml2THGA
- group: auth
  title: ''
  type: Authentication
  url: authentication/qwilr-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/qwilr-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/qwilr-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/qwilr-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/qwilr-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qwilr-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/qwilr-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://qwilr.com/vulnerability-disclosure/
- group: auth
  title: ''
  type: TrustCenter
  url: security/qwilr-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.qwilr.com/
- group: design
  title: ''
  type: Conformance
  url: conformance/qwilr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/qwilr-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/qwilr-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/qwilr-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/qwilr-webhooks.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/qwilr-llms.txt
created: '2026-07-17'
description: Qwilr is a document-experience platform for creating interactive, web-based sales proposals, quotes, contracts, and reports that replace static PDFs. Beyond the editor, Qwilr exposes a REST API (https://api.qwilr.com/v1) and a hosted, OAuth-protected Model Context Protocol (MCP) server that let teams generate branded pages from templates and reusable saved blocks, manage quote tax definitions and Qwilr Pay payment gateways, subscribe to page-lifecycle webhook events (viewed, accepted, set-live), and automate the sales workflow programmatically. API access is an Enterprise capability authenticated with bearer JWT access tokens. Qwilr is backed by Point Nine and maintains a public trust portal with SOC 2 Type 2, PCI DSS, and GDPR posture.
image: https://qwilr.com/apple-touch-icon.png
layout: provider
mcp_servers:
- description: ''
  name: Qwilr MCP Server
  slug: qwilr-mcp-server
modified: '2026-07-20'
name: Qwilr
nav: Providers
network: true
overview: 'Qwilr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Proposals, Documents, Sales, and Quotes.


  The Qwilr catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Qwilr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 23 more developer resources.'
random_paper: 13
scopes:
- name: Qwilr Scopes
  scope_count: 1
  slug: qwilr-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.6
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 57.1
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 50.0
  previous_composite: 51.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/qwilr/refs/heads/main/screenshots/qwilr-2026-08-17T081434.png
security:
- kind: authentication
  name: Qwilr Authentication
  slug: qwilr-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Qwilr Domain Security
  slug: qwilr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Qwilr Vulnerability Disclosure
  slug: qwilr-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Qwilr Trust Center
  slug: qwilr-trust-center
  summary_line: SOC 2 Type 2, PCI DSS (Level 1, via Stripe), GDPR, UETA, eIDAS, E-SIGN Act
slug: qwilr
tags:
- Company
- Proposals
- Documents
- Sales
- Quotes
- Contracts
- E-Signature
- Webhook
- MCP
- Software-as-a-Service
website: https://qwilr.com
---
