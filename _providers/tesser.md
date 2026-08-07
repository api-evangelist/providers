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
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-08-06'
api_count: 14
apis:
- description: The Accounts API from Tesser — 5 operation(s) for accounts.
  name: Tesser Accounts API
  slug: tesser-accounts-api
- description: The Admin API from Tesser — 1 operation(s) for admin.
  name: Tesser Admin API
  slug: tesser-admin-api
- description: The API Keys API from Tesser — 3 operation(s) for api keys.
  name: Tesser API Keys API
  slug: tesser-api-keys-api
- description: The Counterparties API from Tesser — 2 operation(s) for counterparties.
  name: Tesser Counterparties API
  slug: tesser-counterparties-api
- description: The Currencies API from Tesser — 1 operation(s) for currencies.
  name: Tesser Currencies API
  slug: tesser-currencies-api
- description: The health API from Tesser — 2 operation(s) for health.
  name: Tesser health API
  slug: tesser-health-api
- description: The MCP API from Tesser — 1 operation(s) for mcp.
  name: Tesser MCP API
  slug: tesser-mcp-api
- description: The Networks API from Tesser — 1 operation(s) for networks.
  name: Tesser Networks API
  slug: tesser-networks-api
- description: The Organizations API from Tesser — 2 operation(s) for organizations.
  name: Tesser Organizations API
  slug: tesser-organizations-api
- description: The Payments API from Tesser — 7 operation(s) for payments.
  name: Tesser Payments API
  slug: tesser-payments-api
- description: The Tenants API from Tesser — 2 operation(s) for tenants.
  name: Tesser Tenants API
  slug: tesser-tenants-api
- description: The Treasury API from Tesser — 12 operation(s) for treasury.
  name: Tesser Treasury API
  slug: tesser-treasury-api
- description: The Users API from Tesser — 2 operation(s) for users.
  name: Tesser Users API
  slug: tesser-users-api
- description: The webhooks API from Tesser — 6 operation(s) for webhooks.
  name: Tesser webhooks API
  slug: tesser-webhooks-api
artifact_total: 18
asyncapis:
- description: ''
  name: Tesser Webhooks
  slug: tesser-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tesser-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.tesser.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tesser.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tesser.xyz/api/v1/schema.json
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tesser.xyz/overviews/authentication
- group: company
  title: ''
  type: Website
  url: https://tesser.xyz
- group: start
  title: ''
  type: SignUp
  url: https://app.tesser.xyz
- group: start
  title: ''
  type: Login
  url: https://app.tesser.xyz
- group: operate
  title: ''
  type: Support
  url: https://tesser.xyz/#contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tesser.xyz/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tesser.xyz/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tesser-payments
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tesserpayments/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/tesser-openapi-original.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tesser-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/tesser-authentication.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tesser-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tesser-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/tesser-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tesser-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tesser-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tesser-error-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/tesser-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/tesser-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tesser-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tesser-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tesser-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/tesser-openapi-overlay.yaml
created: '2026-07-17'
description: Tesser is a New York-based stablecoin payments infrastructure company that lets licensed financial institutions, banks, fintechs, and payment service providers move money across borders instantly and compliantly on modern stablecoin rails. Its full-stack platform handles wallet provisioning, treasury management, compliance orchestration, and reconciliation, letting institutions integrate stablecoin payments in under a month. The Tesser API (OpenAPI 3.1, v1) exposes accounts, counterparties, tenants, payments, and treasury operations (deposits, withdrawals, rebalances) secured with Auth0 client-credentials JWTs, plus Ed25519-signed webhooks, first-party TypeScript and Kotlin signer SDKs, a published Model Context Protocol server, and an open-source agentic onboarding skill. Founded by Geetha Panchapakesan (ex-MoneyGram, Visa Direct, Circle); raised a $4.5M seed in October 2025 led by Castle Island Ventures with Anthemis, Strobe Ventures, and Digital Currency Group.
image: https://raw.githubusercontent.com/tesser-payments/public/8ec11667adbdf3ba7ea626044483a24ba1a504f1/tesser-logo-Blue.svg
layout: provider
mcp_servers:
- description: ''
  name: tesser-mcp.yml
  slug: tesser-mcpyml
modified: '2026-07-21'
name: Tesser
nav: Providers
network: true
overview: 'Tesser publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Admin API, API Keys API, and 11 more. Tagged areas include Company, Payments, Stablecoins, Cross-Border Payments, and Fintech.


  The Tesser catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Tesser''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, authentication, sandbox, and 22 more developer resources.'
random_paper: 97
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 64.7
    developer_ergonomics: 78.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 48.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 31.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Tesser Authentication
  slug: tesser-authentication
  summary_line: oauth2/http · 1 scheme
- kind: domain-security
  name: Tesser Domain Security
  slug: tesser-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tesser
tags:
- Company
- Payments
- Stablecoins
- Cross-Border Payments
- Fintech
- Treasury
- Banking
- Blockchain
- Compliance
- MCP
- Developer Platform
website: https://tesser.xyz
---
