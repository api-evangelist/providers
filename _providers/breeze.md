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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.6
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 45
  human_in_the_loop: 1
  name: Breeze Agentic Access
  operation_count: 89
  slug: breeze-agentic-access
  summary_line: 89 operations · 45 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: Administrative operations
  name: Breeze Admin API
  slug: breeze-admin-api
- description: Deposit operations
  name: Breeze Deposits API
  slug: breeze-deposits-api
- description: The fund API from Breeze — 1 operation(s) for fund.
  name: Breeze fund API
  slug: breeze-fund-api
- description: Fund management operations
  name: Breeze Funds API
  slug: breeze-funds-api
- description: Global configuration and supported assets
  name: Breeze Global Config API
  slug: breeze-global-config-api
- description: Organization API key management
  name: Breeze Organization API Keys API
  slug: breeze-organization-api-keys-api
- description: Organization onboarding and status
  name: Breeze Organization API
  slug: breeze-organization-api
- description: The Organization Funds API from Breeze — 1 operation(s) for organization funds.
  name: Breeze Organization Funds API
  slug: breeze-organization-funds-api
- description: The Organization Settings API from Breeze — 1 operation(s) for organization settings.
  name: Breeze Organization Settings API
  slug: breeze-organization-settings-api
- description: The Selective Yield Sources API from Breeze — 1 operation(s) for selective yield sources.
  name: Breeze Selective Yield Sources API
  slug: breeze-selective-yield-sources-api
- description: The Strategies API from Breeze — 14 operation(s) for strategies.
  name: Breeze Strategies API
  slug: breeze-strategies-api
- description: The Strategy API from Breeze — 1 operation(s) for strategy.
  name: Breeze Strategy API
  slug: breeze-strategy-api
- description: User balance and yield data
  name: Breeze User Data API
  slug: breeze-user-data-api
- description: Withdrawal operations
  name: Breeze Withdrawals API
  slug: breeze-withdrawals-api
- description: Yield source information and statistics
  name: Breeze Yield Sources API
  slug: breeze-yield-sources-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Breeze Admin API
  slug: open-breeze-admin-api
- collection_type: open
  name: Breeze Admin Deposits API
  slug: open-breeze-deposits-api
- collection_type: open
  name: Breeze Admin fund API
  slug: open-breeze-fund-api
- collection_type: open
  name: Breeze Admin Funds API
  slug: open-breeze-funds-api
- collection_type: open
  name: Breeze Admin Global Config API
  slug: open-breeze-global-config-api
- collection_type: open
  name: Breeze Admin Organization API Keys API
  slug: open-breeze-organization-api-keys-api
- collection_type: open
  name: Breeze Admin Organization API
  slug: open-breeze-organization-api
- collection_type: open
  name: Breeze Admin Organization Funds API
  slug: open-breeze-organization-funds-api
- collection_type: open
  name: Breeze Admin Organization Settings API
  slug: open-breeze-organization-settings-api
- collection_type: open
  name: Breeze Admin Selective Yield Sources API
  slug: open-breeze-selective-yield-sources-api
- collection_type: open
  name: Breeze Admin Strategies API
  slug: open-breeze-strategies-api
- collection_type: open
  name: Breeze Admin Strategy API
  slug: open-breeze-strategy-api
- collection_type: open
  name: Breeze Admin User Data API
  slug: open-breeze-user-data-api
- collection_type: open
  name: Breeze Admin Withdrawals API
  slug: open-breeze-withdrawals-api
- collection_type: open
  name: Breeze Admin Yield Sources API
  slug: open-breeze-yield-sources-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.breeze.baby
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.breeze.baby
- group: start
  title: ''
  type: SignUp
  url: https://portal.breeze.baby
- group: docs
  title: ''
  type: Documentation
  url: https://docs.breeze.baby
- group: docs
  title: ''
  type: APIReference
  url: https://docs.breeze.baby/breeze-api/breeze-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.breeze.baby/get-your-api-key/instruction
- group: operate
  title: ''
  type: Support
  url: https://t.me/breezedevs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anagrambuild
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/breeze-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/breeze-openapi-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/breeze-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/breeze-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/breeze-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/breeze-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/breeze-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/breeze-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/breeze-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/breeze-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/breeze-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/breeze-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/breeze-components.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/breeze-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/breeze-agentic-access.yml
created: '2026-07-17'
description: Breeze is instant, non-custodial yield infrastructure for Solana. Any Solana app — wallets, payment products, trading platforms, Telegram bots, and AI agents — can embed automated yield for its users with a few lines of code via the Breeze REST API, a TypeScript SDK, prebuilt UI components, and an Agent Kit (MCP server, x402 and MPP pay-per-call access, and a drop-in Agent Skill). Yield is generated on USDC, USDT, USDS, SOL and Solana LSTs (JitoSOL, mSOL, JupSOL) plus JLP while custody stays with the user and positions remain liquid and composable. Breeze was built by Anagram and is backed by Multicoin Capital.
image: https://www.breeze.baby/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Breeze MCP Server
  slug: breeze-mcp-server
modified: '2026-07-18'
name: Breeze
nav: Providers
network: true
overview: 'Breeze publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Admin API, Deposits API, fund API, and 12 more. Tagged areas include Company, Crypto Web3, Solana, Yield, and DeFi.


  Breeze''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, authentication, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 16.7
    contract_quality: 48.7
    developer_ergonomics: 63.7
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/breeze/refs/heads/main/screenshots/breeze-2026-07-25T203743.png
security:
- kind: authentication
  name: Breeze Authentication
  slug: breeze-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Breeze Domain Security
  slug: breeze-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: breeze
tags:
- Company
- Crypto Web3
- Solana
- Yield
- DeFi
- Payments
- Blockchain
- AI Agents
website: https://www.breeze.baby
---
