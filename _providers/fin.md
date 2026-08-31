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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 31
  human_in_the_loop: 0
  name: Fin Agentic Access
  operation_count: 62
  slug: fin-agentic-access
  summary_line: 62 operations · 31 acting
api_count: 1
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
- description: The Webhooks API from Fin — 0 operation(s) for webhooks.
  name: Fin Webhooks API
  slug: fin-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Fin Webhooks
  slug: fin-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fin.com Authentication API
  slug: open-fin-authentication-api
- collection_type: open
  name: Fin.com Authentication Balances API
  slug: open-fin-balances-api
- collection_type: open
  name: Fin.com Authentication Beneficiaries API
  slug: open-fin-beneficiaries-api
- collection_type: open
  name: Fin.com Authentication Catalogue API
  slug: open-fin-catalogue-api
- collection_type: open
  name: Fin.com Authentication Crypto Orchestration API
  slug: open-fin-crypto-orchestration-api
- collection_type: open
  name: Fin.com Authentication Customers API
  slug: open-fin-customers-api
- collection_type: open
  name: Fin.com Authentication Fees & FX Rates API
  slug: open-fin-fees-fx-rates-api
- collection_type: open
  name: Fin.com Authentication Transactions API
  slug: open-fin-transactions-api
- collection_type: open
  name: Fin.com Authentication Virtual Accounts API
  slug: open-fin-virtual-accounts-api
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
  name: Fin MCP Server
  slug: fin-mcp-server
modified: '2026-07-19'
name: Fin
nav: Providers
network: true
overview: 'Fin publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Balances API, Beneficiaries API, and 7 more. Tagged areas include Company, Payments, Cross-Border Payments, Stablecoins, and Fintech.


  The Fin catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Fin''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, support, and 18 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 39.7
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.4
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 40.2
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
