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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Safello Agentic Access
  operation_count: 52
  slug: safello-agentic-access
  summary_line: 52 operations · 21 acting
api_count: 2
apis:
- description: Account management
  name: Safello account API
  slug: safello-account-api
- description: Authentication flow
  name: Safello auth API
  slug: safello-auth-api
- description: User's compliance information/status
  name: Safello compliance API
  slug: safello-compliance-api
- description: Market endpoints
  name: Safello market API
  slug: safello-market-api
- description: Buy and sell crypto
  name: Safello orders API
  slug: safello-orders-api
- description: Price endpoints
  name: Safello prices API
  slug: safello-prices-api
- description: User's wallet
  name: Safello wallet API
  slug: safello-wallet-api
arazzos:
- description: Verify buy compliance, quote fees, create a buy order, and poll it to completion.
  name: Safello — buy cryptocurrency
  slug: safello-buy-crypto
- description: BankID auth, email verification, terms acceptance, and KYC to reach a trade-ready customer.
  name: Safello — onboard a customer with BankID
  slug: safello-onboard-customer
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Safello account API
  slug: open-safello-account-api
- collection_type: open
  name: Safello account auth API
  slug: open-safello-auth-api
- collection_type: open
  name: Safello account compliance API
  slug: open-safello-compliance-api
- collection_type: open
  name: Safello account market API
  slug: open-safello-market-api
- collection_type: open
  name: Safello account orders API
  slug: open-safello-orders-api
- collection_type: open
  name: Safello account prices API
  slug: open-safello-prices-api
- collection_type: open
  name: Safello account wallet API
  slug: open-safello-wallet-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/safello-institutional-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://safello.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://safello.github.io/safello-api/docs/intro
- group: docs
  title: ''
  type: Documentation
  url: https://safello.github.io/safello-api/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://safello.github.io/safello-api/api
- group: start
  title: ''
  type: GettingStarted
  url: https://safello.github.io/safello-api/docs/getting-started/getting-started-intro
- group: operate
  title: ''
  type: Support
  url: https://help.safello.com/en/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/safello
- group: commercial
  title: ''
  type: Pricing
  url: https://help.safello.com/en/articles/166728-what-are-safello-s-fees
- group: start
  title: ''
  type: SignUp
  url: https://app.safello.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://safello.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://safello.com/legal/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/safello-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/safello-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/safello-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/safello-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/safello-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/safello-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/safello-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/safello-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/safello-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/safello-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/safello-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/safello-llms.txt
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/safello-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/safello-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/safello-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://safello.com/security-bug-bounty
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/safello-onboard-customer.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/safello-buy-crypto.yml
created: '2026-07-17'
description: Safello is a Swedish cryptocurrency brokerage founded in 2013, registered with the Swedish Financial Supervisory Authority (Finansinspektionen) and listed on Nasdaq First North Growth Market since 2021. It lets people buy, sell, trade, and store digital assets, and exposes a "Cryptocurrency as a Service" (CaaS) Institutional API so third-party organisations can embed crypto buying/selling, BankID customer onboarding, KYC and compliance verification, market data, order management, and wallet balances. The v2 Institutional API (base https://api.safello.com) uses OAuth2 with client-credentials, authorization-code, and a custom Swedish BankID grant, plus a staging environment at api.s4f3.io for testing.
image: https://framerusercontent.com/images/vWXBsKx9A6eh2AJFSk6wXzmHYNo.png
layout: provider
mcp_servers:
- description: ''
  name: Safello MCP Server
  slug: safello-mcp-server
modified: '2026-07-21'
name: Safello
nav: Providers
network: true
overview: 'Safello publishes 7 APIs on the [APIs.io](https://apis.io/) network, including account API, auth API, compliance API, and 4 more. Tagged areas include Company, Fintech, Cryptocurrency, Bitcoin, and Brokerage.


  Safello''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, authentication, and 24 more developer resources.'
random_paper: 7
scopes:
- name: Safello Scopes
  scope_count: 8
  slug: safello-scopes
  summary_line: 8 scopes · urn:safello:params:oauth:grant-type:bankid/clientCredentials/authorizationCode
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/safello/refs/heads/main/screenshots/safello-2026-08-17T081705.png
security:
- kind: authentication
  name: Safello Authentication
  slug: safello-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Safello Domain Security
  slug: safello-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Safello Vulnerability Disclosure
  slug: safello-vulnerability-disclosure
  summary_line: contact published
slug: safello
tags:
- Company
- Fintech
- Cryptocurrency
- Bitcoin
- Brokerage
- Payments
- Sweden
- Trading
- KYC
- BankID
website: https://safello.com
---
