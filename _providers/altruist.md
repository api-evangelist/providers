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
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 18.9
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: OAuth 2.0 authorization-code API giving partners full access to Altruist custody data — accounts, households, positions, transactions, and cost basis — for advisor tools, reporting, and reconciliation
  name: Altruist Open API
  slug: altruist-open-api
- description: OAuth 2.0 password-grant API for account onboarding, funding, transfers, contacts, households, bank-link, user management, and time-weighted return performance reporting.
  name: Altruist Realtime API
  slug: altruist-realtime-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://altruist.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.altruist.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.altruist.com/docs/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developer.altruist.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.altruist.com/docs/getting-started-with-open-api
- group: auth
  title: ''
  type: Authentication
  url: authentication/altruist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/altruist-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/altruist-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/altruist-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.altruist.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.altruist.com/docs/deprecation-policy
- group: design
  title: ''
  type: Conventions
  url: conventions/altruist-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/altruist-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.altruist.com/
- group: auth
  title: ''
  type: TrustCenter
  url: security/altruist-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/altruist-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://altruist.com/legal/security/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/altruist-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/altruist-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/altruist-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/altruist-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/altruist-llms.txt
- group: operate
  title: ''
  type: Support
  url: https://developer.altruist.com/docs/support-policy
- group: company
  title: ''
  type: Blog
  url: https://altruist.com/engineering-blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://hazel.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.altruist.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://altruist.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altruist.com/legal/privacy-policy/
created: '2026-07-17'
description: Altruist is a modern, vertically integrated RIA custodian and technology platform for independent financial advisors. It combines self-clearing custody infrastructure with software for digital account opening, fractional model-based trading, rebalancing, tax management, fee billing, and performance reporting in a single workspace. Altruist runs a developer program with an OAuth 2.0 Open API (accounts, households, positions, transactions, cost basis), a Realtime API (account onboarding, funding, transfers, contacts, bank-link, time-weighted return), and custodial flat-file (SFTP) data feeds, so advisor tools and fintech partners such as Orion, Tamarac, Black Diamond, and Advyzon can integrate directly with the custodian. Backed by ICONIQ Capital and Insight Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/altruist.png
layout: provider
mcp_servers:
- description: ''
  name: altruist-mcp.yml
  slug: altruist-mcpyml
modified: '2026-07-17'
name: Altruist
nav: Providers
network: true
overview: 'Altruist publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Custody, Wealth Management, and Financial Advisors.


  Altruist''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 21 more developer resources.'
random_paper: 19
scopes:
- name: Altruist Scopes
  scope_count: 1
  slug: altruist-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 41.0
  delta: -0.3
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 60.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 50.0
  previous_composite: 41.3
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/altruist/refs/heads/main/screenshots/altruist-2026-07-25T195845.png
security:
- kind: authentication
  name: Altruist Authentication
  slug: altruist-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Altruist Domain Security
  slug: altruist-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: trust-center
  name: Altruist Trust Center
  slug: altruist-trust-center
  summary_line: SOC 2
slug: altruist
tags:
- Company
- Fintech
- Custody
- Wealth Management
- Financial Advisors
- RIA
- Investing
- OAuth
website: https://altruist.com/
---
