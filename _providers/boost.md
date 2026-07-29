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
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Boost Agentic Access
  operation_count: 17
  slug: boost-agentic-access
  summary_line: 17 operations
api_count: 8
apis:
- description: The Action API from Boost — 2 operation(s) for action.
  name: Boost Action API
  slug: boost-action-api
- description: The Action Template API from Boost — 2 operation(s) for action template.
  name: Boost Action Template API
  slug: boost-action-template-api
- description: The Blocklist API from Boost — 1 operation(s) for blocklist.
  name: Boost Blocklist API
  slug: boost-blocklist-api
- description: The Boost API from Boost — 9 operation(s) for boost.
  name: Boost Boost API
  slug: boost-boost-api
- description: The Budget API from Boost — 2 operation(s) for budget.
  name: Boost Budget API
  slug: boost-budget-api
- description: The Contract API from Boost — 2 operation(s) for contract.
  name: Boost Contract API
  slug: boost-contract-api
- description: The RewardKit API from Boost — 3 operation(s) for rewardkit.
  name: Boost RewardKit API
  slug: boost-rewardkit-api
- description: The RewardKitTrending API from Boost — 1 operation(s) for rewardkittrending.
  name: Boost RewardKitTrending API
  slug: boost-rewardkittrending-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Website
  url: https://boost.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.boost.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.boost.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.boost.xyz/v2/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.boost.xyz/platform/overview
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/gdu3EpeqsD
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/boostxyz
- group: start
  title: ''
  type: SignUp
  url: https://app.boost.xyz
- group: build
  title: ''
  type: Packages
  url: packages/boost-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/boost-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/boost-cli.yml
- group: design
  title: ''
  type: Components
  url: components/boost-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/boost-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/boost-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/boost-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/boost-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/boost-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/boost-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/boost-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/boost-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/boost-v2-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/boost-lifecycle.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/boost-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/boost-domain-security.yml
created: '2026-07-17'
description: Boost is a distributed onchain incentives network that lets any team reward any onchain action with any token. Teams define target actions, fund a budget, and deploy campaigns across Base, Optimism, Arbitrum and other EVM chains, then measure ROI and iterate in real time. Boost ships two products — One-Time Actions and Time-Based Incentives (TBI) — plus RewardKit and a Headless SDK for embedding reward primitives, a public read-only Boost V2 REST API, a TypeScript SDK, a CLI, and a published MCP server. Founded by Ido Ben-Natan and Raz Niv and backed by Electric Capital and Greylock.
image: https://www.boost.xyz/og-image.png
layout: provider
mcp_servers:
- description: ''
  name: boost-mcp.yml
  slug: boost-mcpyml
modified: '2026-07-18'
name: Boost
nav: Providers
network: true
overview: 'Boost publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Action API, Action Template API, Blocklist API, and 5 more. Tagged areas include Company, Crypto, Web3, Incentives, and Rewards.


  Boost''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, CLI, authentication, and 18 more developer resources.'
random_paper: 77
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 55.5
    developer_ergonomics: 73.4
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/boost/refs/heads/main/screenshots/boost-2026-07-25T203625.png
security:
- kind: authentication
  name: Boost Authentication
  slug: boost-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Boost Domain Security
  slug: boost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: boost
tags:
- Company
- Crypto
- Web3
- Incentives
- Rewards
- Blockchain
- DeFi
- Onchain
- EVM
website: https://boost.xyz/
---
