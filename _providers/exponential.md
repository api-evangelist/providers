---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.5
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Exponential Agentic Access
  operation_count: 12
  slug: exponential-agentic-access
  summary_line: 12 operations
api_count: 2
apis:
- description: The Agent API from Exponential — 4 operation(s) for agent.
  name: Exponential Agent API
  slug: exponential-agent-api
- description: The History API from Exponential — 1 operation(s) for history.
  name: Exponential History API
  slug: exponential-history-api
- description: The Performance API from Exponential — 1 operation(s) for performance.
  name: Exponential Performance API
  slug: exponential-performance-api
- description: The Public API from Exponential — 1 operation(s) for public.
  name: Exponential Public API
  slug: exponential-public-api
- description: The Vault API from Exponential — 5 operation(s) for vault.
  name: Exponential Vault API
  slug: exponential-vault-api
arazzos:
- description: Learn the graph schema, find an entity, read its risk grade and rationale, then map its 1-hop dependencies. Every step settles an x402 micropayment.
  name: YO Risk Graph triage
  slug: exponential-risk-graph-triage
- description: Read a vault's current snapshot, yield and TVL history, and a user's pending redemptions.
  name: YO vault snapshot and user position
  slug: exponential-vault-snapshot
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Yo Protocol Agent API
  slug: open-exponential-agent-api
- collection_type: open
  name: Yo Protocol Agent History API
  slug: open-exponential-history-api
- collection_type: open
  name: Yo Protocol Agent Performance API
  slug: open-exponential-performance-api
- collection_type: open
  name: Yo Protocol Agent Public API
  slug: open-exponential-public-api
- collection_type: open
  name: Yo Protocol Agent Vault API
  slug: open-exponential-vault-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/exponential-protocol-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/exponential-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/exponential-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://exponential.fi
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.yo.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.yo.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.yo.xyz/integrations/api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.yo.xyz/integrations/integration-guides/sdk/getting-started/quickstart
- group: company
  title: ''
  type: Blog
  url: https://docs.yo.xyz/welcome-to-yo/what-is-yo
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/yoprotocol
- group: auth
  title: ''
  type: Security
  url: https://docs.yo.xyz/protocol/security-framework
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.yo.xyz/yo-risk-graph/agent-api
- group: build
  title: ''
  type: Packages
  url: packages/exponential-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/exponential-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/exponential-cli.yml
- group: design
  title: ''
  type: Components
  url: components/exponential-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/exponential-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/exponential-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/exponential-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/exponential-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/exponential-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/exponential-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/exponential-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/exponential-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/exponential-data-model.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/exponential-finops.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exponential-vault-snapshot.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/exponential-risk-graph-triage.yml
created: '2026-07-17'
description: Exponential.fi is a DeFi company (backed by Paradigm and Norwest Venture Partners) behind YO Protocol — a cross-chain "Yield Optimizer" that automatically allocates deposits across the best-performing liquidity pools on multiple blockchains to deliver the highest risk-adjusted yield, using Exponential.fi's own Risk Ratings to balance risk and reward. yoVaults are ERC-4626 tokenized vaults (yoUSD, yoETH, yoBTC, yoEUR, yoGOLD, yoSOL and more) with ERC-7540-style async redemption, all routed through the single yoGateway entry point. The developer surface spans a public read API (api.yo.xyz), a first-party TypeScript SDK/React kit/CLI (@yo-protocol/*), official agent skills and a Base MCP plugin, and the YO Risk Graph — a paid, agent-facing DeFi risk-intelligence API monetized per-call via the x402 USDC micropayment standard on Base.
finops:
- name: Exponential Finops
  service_category: ''
  slug: exponential-finops
image: https://raw.githubusercontent.com/api-evangelist/exponential/refs/heads/main/apis.yml
layout: provider
mcp_servers:
- description: ''
  name: Exponential MCP Server
  slug: exponential-mcp-server
modified: '2026-07-19'
name: Exponential
nav: Providers
network: true
overview: 'Exponential publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Agent API, History API, Performance API, and 2 more. Tagged areas include Company, DeFi, Decentralized Finance, Yield, and Yield Optimizer.


  Exponential''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, CLI, authentication, and 22 more developer resources.'
random_paper: 15
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 42.9
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 40.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/exponential/refs/heads/main/screenshots/exponential-2026-07-25T213934.png
security:
- kind: authentication
  name: Exponential Authentication
  slug: exponential-authentication
  summary_line: none/payment-gated · 3 schemes
- kind: domain-security
  name: Exponential Domain Security
  slug: exponential-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: exponential
tags:
- Company
- DeFi
- Decentralized Finance
- Yield
- Yield Optimizer
- Vault
- ERC-4626
- Cross-Chain
- Blockchain
- Crypto
- Risk
- Risk Ratings
- Agents
- x402
- Web3
website: https://exponential.fi
---
