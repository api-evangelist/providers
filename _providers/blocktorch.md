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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Blocktorch Agentic Access
  operation_count: 2
  slug: blocktorch-agentic-access
  summary_line: 2 operations · 2 acting
api_count: 1
apis:
- description: Manage managed Hardhat fork instances.
  name: Blocktorch Hardhat API
  slug: blocktorch-hardhat-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blocktorch Forking Hardhat API
  slug: open-blocktorch-hardhat-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/blocktorch-hardhat-forking-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.blocktorch.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blocktorch.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blocktorch.xyz/overview/quickstart
- group: start
  title: ''
  type: SignUp
  url: https://beta.blocktorch.xyz
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@blocktorch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blocktorch-xyz
- group: operate
  title: ''
  type: Support
  url: mailto:contact@blocktorch.xyz
- group: company
  title: ''
  type: Website
  url: https://blocktorch.xyz
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/blocktorch-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/blocktorch-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/blocktorch-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/blocktorch-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/blocktorch-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/blocktorch-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blocktorch-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/blocktorch-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/blocktorch-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/blocktorch-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blocktorch-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blocktorch-domain-security.yml
created: '2026-07-17'
description: Blocktorch is an end-to-end observability platform built specifically for web3 services and decentralized applications (dApps). It gives engineering teams real-time monitoring of smart contract events, state variables and transaction data, plus log search, alerting, tracing, dashboarding, debugging and collaboration across multiple layers of the web3 stack (EVM chains, roll-ups, local Hardhat forks, oracles, account-abstraction modules and decentralized storage). Blocktorch also exposes a Hardhat Forking API for programmatically managing managed Hardhat fork instances for continuous development and testing. Backed by Speedinvest.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blocktorch.png
layout: provider
mcp_servers:
- description: ''
  name: blocktorch-mcp.yml
  slug: blocktorch-mcpyml
modified: '2026-07-18'
name: Blocktorch
nav: Providers
network: true
overview: 'Blocktorch publishes 1 API on the [APIs.io](https://apis.io/) network: Hardhat API. Tagged areas include Company, Web3, Observability, Monitoring, and Blockchain.


  Blocktorch''s developer surface includes documentation, getting-started guide, signup flow, engineering blog, support, CLI, authentication, and 15 more developer resources.'
random_paper: 24
score:
  band: thin
  composite: 40.1
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 61.2
    developer_ergonomics: 62.5
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blocktorch/refs/heads/main/screenshots/blocktorch-2026-07-25T203347.png
security:
- kind: authentication
  name: Blocktorch Authentication
  slug: blocktorch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blocktorch Domain Security
  slug: blocktorch-domain-security
  summary_line: no transport/DNS hardening detected
slug: blocktorch
tags:
- Company
- Web3
- Observability
- Monitoring
- Blockchain
- Smart Contracts
- dApps
- Developer Tools
website: https://blocktorch.xyz
---
