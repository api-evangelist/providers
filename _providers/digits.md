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
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.7
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: The Llms.txt API from Digits — 1 operation(s) for llms.txt.
  name: Digits Llms.txt API
  slug: digits-llms-txt-api
- description: The Sitemap.xml API from Digits — 1 operation(s) for sitemap.xml.
  name: Digits Sitemap.xml API
  slug: digits-sitemap-xml-api
- description: The .well Known API from Digits — 2 operation(s) for .well known.
  name: Digits .well Known API
  slug: digits-well-known-api
artifact_total: 11
asyncapis:
- description: ''
  name: Digits Webhooks
  slug: digits-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/digits-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://digits.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.digits.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.digits.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.digits.com/reference/companyservice_get
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.digits.com/docs/app-creation
- group: commercial
  title: ''
  type: Pricing
  url: https://digits.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://my.digits.com
- group: start
  title: ''
  type: Login
  url: https://my.digits.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://my.digits.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://my.digits.com/legal/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://help.digits.com
- group: company
  title: ''
  type: Blog
  url: https://digits.com/blog/
- group: auth
  title: ''
  type: Security
  url: https://digits.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.digits.com
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/digits-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/digits-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/digits-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/digits-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/digits-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/digits-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/digits-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/digits-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/digits-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/digits-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/digits-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/digits-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/digits-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/digits-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/digits-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/digits-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/digits-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/digits-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/digits-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/digits-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Digits is an AI-native accounting software company founded in 2018 and based in San Francisco, building what it calls the world's first Agentic General Ledger (AGL) — a suite of custom-trained models and agents that auto-book 95%+ of business transactions in real time to deliver always up-to-date, verified financials. The platform automates bookkeeping, reconciliation, financial reporting, dashboards, bill pay, invoicing, automated schedules, and the month-end close for small businesses, startups, and accounting firms, and connects to 12,000+ financial institutions. Digits exposes the Digits Connect API (OAuth 2.0), a hosted MCP server, published llms.txt, and an OpenAPI specification for developers integrating source data and reading ledger and financial-statement data.
image: https://digits.com/favicon/favicon.svg
layout: provider
mcp_servers:
- description: ''
  name: digits-mcp.yml
  slug: digits-mcpyml
modified: '2026-07-18'
name: Digits
nav: Providers
network: true
overview: 'Digits publishes 3 APIs on the [APIs.io](https://apis.io/) network: Llms.txt API, Sitemap.xml API, and .well Known API. Tagged areas include Accounting, Bookkeeping, Financial Reporting, General Ledger, and AI.


  The Digits catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Digits'' developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, engineering blog, and 29 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Digits Rate Limits
  slug: digits-rate-limits
scopes:
- name: Digits Scopes
  scope_count: 6
  slug: digits-scopes
  summary_line: 6 scopes · authorizationCode
score:
  band: strong
  composite: 56.8
  delta: 1.2
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.7
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 20.8
    operational_transparency: 26.3
  previous_composite: 55.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digits/refs/heads/main/screenshots/digits-2026-07-25T212030.png
security:
- kind: authentication
  name: Digits Authentication
  slug: digits-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Digits Domain Security
  slug: digits-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Digits Vulnerability Disclosure
  slug: digits-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Digits Trust Center
  slug: digits-trust-center
  summary_line: SOC 2
slug: digits
tags:
- Accounting
- Bookkeeping
- Financial Reporting
- General Ledger
- AI
- Fintech
- Accountants
- Bill Pay
- Invoicing
website: https://digits.com
---
