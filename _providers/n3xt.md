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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
api_count: 11
apis:
- description: The Approvals API from N3XT — 2 operation(s) for approvals.
  name: N3XT Approvals API
  slug: n3xt-approvals-api
- description: The AuditTrail API from N3XT — 1 operation(s) for audittrail.
  name: N3XT AuditTrail API
  slug: n3xt-audittrail-api
- description: The Businesses API from N3XT — 2 operation(s) for businesses.
  name: N3XT Businesses API
  slug: n3xt-businesses-api
- description: The Contacts API from N3XT — 2 operation(s) for contacts.
  name: N3XT Contacts API
  slug: n3xt-contacts-api
- description: The Ndd Routes API from N3XT — 2 operation(s) for ndd routes.
  name: N3XT Ndd Routes API
  slug: n3xt-ndd-routes-api
- description: The Payments API from N3XT — 5 operation(s) for payments.
  name: N3XT Payments API
  slug: n3xt-payments-api
- description: The Programmable API from N3XT — 5 operation(s) for programmable.
  name: N3XT Programmable API
  slug: n3xt-programmable-api
- description: The System API from N3XT — 2 operation(s) for system.
  name: N3XT System API
  slug: n3xt-system-api
- description: The Transfers API from N3XT — 1 operation(s) for transfers.
  name: N3XT Transfers API
  slug: n3xt-transfers-api
- description: The Users API from N3XT — 2 operation(s) for users.
  name: N3XT Users API
  slug: n3xt-users-api
- description: The Wallets API from N3XT — 6 operation(s) for wallets.
  name: N3XT Wallets API
  slug: n3xt-wallets-api
artifact_total: 17
common:
- group: company
  title: ''
  type: Website
  url: https://n3xt.io
- group: start
  title: ''
  type: DeveloperPortal
  url: https://helpcenter.n3xt.io/
- group: docs
  title: ''
  type: Documentation
  url: https://helpcenter.n3xt.io/
- group: docs
  title: ''
  type: APIReference
  url: https://openapi.n3xt.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://helpcenter.n3xt.io/en/articles/12118191-api-getting-started
- group: operate
  title: ''
  type: Support
  url: https://helpcenter.n3xt.io/en/
- group: company
  title: ''
  type: Blog
  url: https://n3xt.io/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.n3xt.io/application
- group: start
  title: ''
  type: Login
  url: https://app.n3xt.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://n3xt.io/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.n3xt.io/resources?s=igp2bvcb2ox3cjeerru9qs&name=privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.n3xt.io/
- group: auth
  title: ''
  type: TrustCenter
  url: security/n3xt-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://n3xt.io/security
- group: auth
  title: ''
  type: Security
  url: https://trust.n3xt.io/resources?s=a3mbqw7jbnczlhbn9hfm16&name=vulnerability-disclosure-program
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/n3xt-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/n3xt-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/n3xt-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/n3xt-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/n3xt-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/n3xt-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/n3xt-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/n3xt-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/n3xt-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/n3xt-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/n3xt-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/n3xt-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/n3xt-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/n3xt-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/n3xt-data-model.yml
created: '2026-07-17'
description: N3XT is a Wyoming state-chartered Special Purpose Depository Institution (SPDI) offering instant, 24/7/365 USD payment settlement for business-to-business transactions on blockchain rails. Its full-reserve narrow-bank model backs every deposit 1:1 with cash and short-term U.S. Treasuries (no lending), and it issues the N3XT Digital Dollar (NDD) — a bank-regulated tokenized deposit with an on-chain KYC/KYB Identity Passport (NDDID). The N3XT API is a holistic banking API for businesses covering wallets and public-wallet onboarding, instant and programmable payments, payment requests, internal transfers, NDD mint/redeem, contacts, approvals and audit trail. It ships OAuth 2.0 authentication, Beta/Omega test environments, and a first-party hosted MCP server for AI/agent access.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/n3xt.png
layout: provider
mcp_servers:
- description: ''
  name: n3xt-mcp.yml
  slug: n3xt-mcpyml
modified: '2026-07-20'
name: N3XT
nav: Providers
network: true
overview: 'N3XT publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Approvals API, AuditTrail API, Businesses API, and 8 more. Tagged areas include Company, Crypto, Banking, Payments, and Stablecoin.


  N3XT''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 24 more developer resources.'
random_paper: 57
scopes:
- name: N3Xt Scopes
  scope_count: 8
  slug: n3xt-scopes
  summary_line: 8 scopes
score:
  band: strong
  composite: 60.0
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.9
    developer_ergonomics: 73.9
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 60.0
  regulatory:
    applies: true
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 100.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: N3Xt Authentication
  slug: n3xt-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: N3Xt Domain Security
  slug: n3xt-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: N3Xt Vulnerability Disclosure
  slug: n3xt-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: N3Xt Trust Center
  slug: n3xt-trust-center
  summary_line: SOC 2, ISO 27001
slug: n3xt
tags:
- Company
- Crypto
- Banking
- Payments
- Stablecoin
- Fintech
- Blockchain
- API
- MCP
website: https://n3xt.io
---
