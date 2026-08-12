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
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Fin Agentic Access
  operation_count: 62
  slug: fin-agentic-access
  summary_line: 62 operations · 31 acting
api_count: 9
apis:
- description: A modified OAuth 2.0 Client Credential Flow
  name: Fin Authentication API
  slug: fin-authentication-api
- description: Retrieve wallet balance information
  name: Fin Balances API
  slug: fin-balances-api
- description: Manage beneficiary accounts for payments and transfers
  name: Fin Beneficiaries API
  slug: fin-beneficiaries-api
- description: A set of endpoints to retrieve contextual data to assemble requests to fin.com's API
  name: Fin Catalogue API
  slug: fin-catalogue-api
- description: The Crypto Orchestration API from Fin — 3 operation(s) for crypto orchestration.
  name: Fin Crypto Orchestration API
  slug: fin-crypto-orchestration-api
- description: Customer management and document upload operations
  name: Fin Customers API
  slug: fin-customers-api
- description: Retrieve fees and foreign exchange rates
  name: Fin Fees & FX Rates API
  slug: fin-fees-fx-rates-api
- description: Transaction history and management for beneficiaries
  name: Fin Transactions API
  slug: fin-transactions-api
- description: Create and manage virtual accounts for USD to USDC conversions
  name: Fin Virtual Accounts API
  slug: fin-virtual-accounts-api
artifact_total: 14
asyncapis:
- description: ''
  name: Fin Webhooks
  slug: fin-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.fin.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.fin.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.fin.com/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.fin.com/index
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/fin-openapi-original.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/fin-openapi-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fin-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fin-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fin-problem-types.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/fin-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fin-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fin-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://fin.instatus.com
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.fin.com/changelogs/2026-04-20
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/fin-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/fin-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fin-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fin-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fin-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fin-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fin-llms.txt
- group: operate
  title: ''
  type: Support
  url: mailto:support@fin.com
- group: company
  title: ''
  type: Blog
  url: https://www.fin.com/stories
- group: company
  title: ''
  type: Website
  url: https://www.fin.com
created: '2026-07-17'
description: Fin (fin.com) is a global cross-border payments infrastructure company that moves money internationally over stablecoin rails and direct liquidity networks instead of traditional correspondent banking, settling in minutes rather than days. Its Orchestration API lets businesses onboard individual and business customers (KYC/KYB), create beneficiaries, quote FX and fees, send transfer and batch payouts, provision multi-currency virtual accounts that convert fiat deposits to crypto (e.g. USD to USDC), and run crypto orchestration across exchanges. Founded by ex-Citadel engineers, Fin raised a $17M Series A to bring its stablecoin-powered high-value payments product to market. This profile was enriched from the public developer surface at developer.fin.com.
image: https://cdn.sanity.io/images/xemwqsar/production/0e65aec0795ced77ed5301b8627cbb88059d11d2-1200x630.webp?w=1200&h=630&q=80&fit=crop
layout: provider
mcp_servers:
- description: ''
  name: fin-mcp.yml
  slug: fin-mcpyml
modified: '2026-07-19'
name: Fin
nav: Providers
network: true
overview: 'Fin publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balances API, Beneficiaries API, and 6 more. Tagged areas include Company, Payments, Cross-Border Payments, Stablecoins, and Fintech.


  The Fin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fin''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 18 more developer resources.'
random_paper: 85
score:
  band: developing
  composite: 42.4
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 68.0
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 47.4
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fin/refs/heads/main/screenshots/fin-2026-07-25T214454.png
security:
- kind: authentication
  name: Fin Authentication
  slug: fin-authentication
  summary_line: http/oauth2 · 1 scheme
- kind: domain-security
  name: Fin Domain Security
  slug: fin-domain-security
  summary_line: TLSv1.3 · DMARC
slug: fin
tags:
- Company
- Payments
- Cross-Border Payments
- Stablecoins
- Fintech
- Money Movement
- Foreign Exchange
- Virtual Accounts
- Crypto
website: https://www.fin.com
---
