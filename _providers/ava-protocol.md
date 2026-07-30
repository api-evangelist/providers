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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Ava Protocol Agentic Access
  operation_count: 32
  slug: ava-protocol-agentic-access
  summary_line: 32 operations · 16 acting
api_count: 10
apis:
- description: Token issuance and credential management
  name: Ava Protocol Auth API
  slug: ava-protocol-auth-api
- description: Workflow execution history and status
  name: Ava Protocol Executions API
  slug: ava-protocol-executions-api
- description: Liveness / readiness probes
  name: Ava Protocol Health API
  slug: ava-protocol-health-api
- description: Stand-alone node execution
  name: Ava Protocol Nodes API
  slug: ava-protocol-nodes-api
- description: Connected operator status (read-only)
  name: Ava Protocol Operators API
  slug: ava-protocol-operators-api
- description: User/workflow/org secret storage
  name: Ava Protocol Secrets API
  slug: ava-protocol-secrets-api
- description: ERC-20 metadata lookup
  name: Ava Protocol Tokens API
  slug: ava-protocol-tokens-api
- description: Stand-alone trigger evaluation
  name: Ava Protocol Triggers API
  slug: ava-protocol-triggers-api
- description: Smart-wallet derivation and operations
  name: Ava Protocol Wallets API
  slug: ava-protocol-wallets-api
- description: Workflow CRUD and lifecycle actions
  name: Ava Protocol Workflows API
  slug: ava-protocol-workflows-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ava-protocol-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ava-protocol-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ava-protocol-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/ava-protocol-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ava-protocol-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ava-protocol-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ava-protocol-llms.txt
- group: other
  title: ''
  type: Protobuf
  url: grpc/ava-protocol-avs.proto
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ava-protocol-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ava-protocol-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/ava-protocol-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ava-protocol-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ava-protocol-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ava-protocol-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/ava-protocol-sandbox.yml
- group: build
  title: ''
  type: CLI
  url: cli/ava-protocol-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://avaprotocol.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://avaprotocol.org/docs/ava-sdk-js/rest-api
- group: start
  title: ''
  type: GettingStarted
  url: https://avaprotocol.org/docs/ava-sdk-js/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://avaprotocol.org/docs/ava-sdk-js/authentication
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AvaProtocol
- group: company
  title: ''
  type: Blog
  url: https://avaprotocol.org/blog
- group: start
  title: ''
  type: SignUp
  url: https://app.avaprotocol.org
- group: operate
  title: ''
  type: Support
  url: https://avaprotocol.org/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avaprotocol.org/legal/discord-bot-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avaprotocol.org/legal/discord-bot-privacy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/ava_protocol
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/7W9UDvsbwh
created: '2026-07-17'
description: Ava Protocol is an AI-powered onchain automation platform for Ethereum and L2s (Base, Soneium), and the evolution of the OAK Network Substrate automation parachain. Users create "workflows" that connect triggers (scheduled time, price conditions, onchain events, or manual) to actions (swaps, transfers, contract calls, notifications) and run them non-custodially from scoped smart wallets — the user always approves before execution. Verifiable execution is provided by an EigenLayer AVS (Actively Validated Service). Developers integrate through a public REST API (the AVS aggregator gateway) and a TypeScript SDK, authenticating with a JWT bearer token obtained via wallet signature (EIP-191) or an operator-minted key.
image: https://avaprotocol.org/image/open-graph/index.jpg
layout: provider
mcp_servers:
- description: ''
  name: ava-protocol-mcp.yml
  slug: ava-protocol-mcpyml
modified: '2026-07-18'
name: Ava Protocol
nav: Providers
network: true
overview: 'Ava Protocol publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Executions API, Health API, and 7 more. Tagged areas include Company, Fintech, Blockchain, DeFi, and Automation.


  Ava Protocol''s developer surface includes authentication, sandbox, CLI, documentation, API reference, getting-started guide, engineering blog, and 24 more developer resources.'
random_paper: 9
score:
  band: developing
  composite: 44.8
  delta: -3.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 50.7
    developer_ergonomics: 75.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 47.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ava-protocol/refs/heads/main/screenshots/ava-protocol-2026-07-25T201902.png
security:
- kind: authentication
  name: Ava Protocol Authentication
  slug: ava-protocol-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ava Protocol Domain Security
  slug: ava-protocol-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ava-protocol
tags:
- Company
- Fintech
- Blockchain
- DeFi
- Automation
- Web3
- Ethereum
- Smart Wallets
- Workflows
- AI Agents
website: https://avaprotocol.org/
---
