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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 45.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Coro's REST API (v1) for managing workspaces, subscriptions, tickets, devices, protected users, portal users, usage, audit logs, and webhooks across the Coro cybersecurity platform. OAuth 2.0 client-c
  name: Coro Public REST API
  slug: coro-public-rest-api
artifact_total: 6
asyncapis:
- description: ''
  name: Coro Webhooks
  slug: coro-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.coro.net/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.coro.net/developer-portal/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coro.net/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.coro.net/developer-portal/authentication/
- group: auth
  title: ''
  type: Authentication
  url: authentication/coro-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coro-mcp.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/coro-webhooks.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coro-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coro-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coro-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coro-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coro-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.coro.net/compliance
- group: auth
  title: ''
  type: TrustCenter
  url: security/coro-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coro-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/coro-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coro-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://docs.coro.net/
- group: company
  title: ''
  type: Blog
  url: https://www.coro.net/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coro.net/platform/pricing
- group: start
  title: ''
  type: SignUp
  url: https://secure.coro.net/login
- group: start
  title: ''
  type: Login
  url: https://secure.coro.net/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coro.net/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coro.net/legal/privacy
created: '2026-07-17'
description: Coro is a cybersecurity company that consolidates endpoint protection, email security, network protection (ZTNA, VPN, encryption), cloud app security, data protection, and security awareness training into a single AI-driven platform built for lean IT teams, growing organizations, and managed service providers (MSPs). Coro's public REST API (v1) exposes the same workspace security data through region-specific hosts (US, Canada, Germany), organized around workspaces as tenant containers with subscriptions, tickets, devices, protected users, portal users, usage metrics, audit logs, and webhook configurations. It authenticates with OAuth 2.0 client credentials and offers real-time webhooks and an official MCP server so AI tools can query Coro securely. Coro was surfaced as a portfolio company of Balderton Capital.
image: https://www.coro.net/wp-content/uploads/coro-opengraph.png
layout: provider
mcp_servers:
- description: ''
  name: coro-mcp.yml
  slug: coro-mcpyml
modified: '2026-07-18'
name: Coro
nav: Providers
network: true
overview: 'Coro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Security, Endpoint Protection, and Email Security.


  The Coro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Coro''s developer surface includes documentation, getting-started guide, authentication, changelog, support, engineering blog, pricing, and 17 more developer resources.'
random_paper: 40
score:
  band: developing
  composite: 49.1
  delta: 8.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 51.6
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 23.7
  previous_composite: 40.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/coro/refs/heads/main/screenshots/coro-2026-07-25T210437.png
security:
- kind: authentication
  name: Coro Authentication
  slug: coro-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Coro Domain Security
  slug: coro-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Coro Trust Center
  slug: coro-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: coro
tags:
- Company
- Cybersecurity
- Security
- Endpoint Protection
- Email Security
- Cloud Security
- Data Protection
- MSP
- Webhooks
- MCP
website: https://www.coro.net/
---
