---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-07-28'
api_count: 8
apis:
- description: OpenAI-compatible inference API for open-source AI models hosted on io.net's decentralized GPU network. Exposes /v1/models and /v1/chat/completions over the base URL https://api.intelligence.io.soluti
  name: IO Intelligence API
  slug: io-intelligence-api
- description: REST API for discovering, configuring, and running AI agents and agentic workflows on io.net's no-code workflow editor. Supports agent discovery, workflow execution, workflow-schema retrieval, and CRU
  name: IO Agents API
  slug: io-agents-api
- description: Container-as-a-Service REST API for deploying GPU-backed containers across io.net's decentralized network. Operations include container deployment and termination, real-time log streaming, replica ava
  name: IO Cloud Container-as-a-Service API
  slug: io-cloud-caas-api
- description: VM-as-a-Service REST API for provisioning, extending, and terminating GPU virtual machines on io.net. Surfaces hardware availability and pricing, supports multi-VM cluster orchestration, and exposes j
  name: IO Cloud VM-as-a-Service API
  slug: io-cloud-vmaas-api
- description: 'Network analytics API exposing device summaries and detailed metrics, block-reward analysis, proof-of-work challenge tracking, and device notifications. Powers the public IO Explorer dashboard and is '
  name: IO Explorer API
  slug: io-explorer-api
- description: Administrative API for creating scoped sub-API keys with per-model restrictions and per-key credit limits, tracking usage and aggregated spend, and revoking keys. Designed for teams and partners resel
  name: IO Sub-API Key Management API
  slug: io-sub-api-key-api
- description: Hosted Model Context Protocol server at https://mcp.io.solutions/mcp that exposes IO Cloud provisioning and management tools to MCP-aware agents (Claude Desktop, Claude Code, Cursor, etc.). Authentica
  name: IO Cloud MCP Server
  slug: io-cloud-mcp-server
- description: Open-source FastAPI remote attestation service for Intel TDX and NVIDIA H200 confidential VMs operating on the io.net network. Issues verifiable cryptographic attestations that a workload is running i
  name: Confidential Compute Attestation Agent API
  slug: cc-attestation-agent-api
artifact_total: 26
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/io-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://io.net
- group: start
  title: ''
  type: Portal
  url: https://io.net
- group: docs
  title: ''
  type: Documentation
  url: https://io.net/docs
- group: docs
  title: ''
  type: Documentation
  url: https://docs.io.net
- group: start
  title: ''
  type: GettingStarted
  url: https://io.net/docs
- group: docs
  title: ''
  type: APIReference
  url: https://io.net/docs/reference/ai-models/get-started-with-io-intelligence-api
- group: other
  title: ''
  type: Intelligence
  url: https://io.net/intelligence
- group: other
  title: ''
  type: Cloud
  url: https://io.net/cloud
- group: other
  title: ''
  type: Explorer
  url: https://explorer.io.net
- group: start
  title: ''
  type: Signup
  url: https://ai.io.net
- group: start
  title: ''
  type: Console
  url: https://ai.io.net
- group: auth
  title: ''
  type: APIKeys
  url: https://ai.io.net/ai/api-keys
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ionet-official
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ionet-official/cc-attestation-agent-api
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ionet-official/io-net-official-setup-script
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ionet-official/io_launch_binaries
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ionet-official/docs
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ionet-official/io-ray-serve-chat-demo
- group: company
  title: ''
  type: Blog
  url: https://io.net/blog
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ionet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/io-net
- group: other
  title: ''
  type: Medium
  url: https://ionet.medium.com
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/ionet
- group: auth
  title: ''
  type: Token
  url: https://io.net/token
- group: auth
  title: ''
  type: Tokenomics
  url: https://io.net/token
- group: other
  title: ''
  type: Staking
  url: https://io.net/staking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://io.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://io.net/privacy
created: '2026-05-25'
description: 'io.net is a decentralized GPU network for AI compute, built on Solana, that aggregates idle consumer and data-center GPUs (NVIDIA A100, H100, H200, and Blackwell-class) into on-demand, geo-distributed compute clusters orchestrated with the Ray framework. The platform exposes a Web3-native alternative to hyperscaler GPU cloud through several developer-facing surfaces: IO Intelligence (an OpenAI-compatible inference API for 15+ open-source models including Llama 3.3 70B), IO Cloud (Container-as-a-Service and VM-as-a-Service APIs for deploying GPU containers, Ray clusters, Kubernetes clusters, and bare-metal instances), IO Agents (agent and agentic-workflow APIs), IO Explorer (a network analytics API for devices, clusters, and block rewards), IO Worker (the supplier-side onboarding stack), IO ID (the account/wallet hub), and IO Staking. Confidential Compute on Intel TDX-enabled H100/H200/B200 GPUs and a remote attestation service for Intel TDX and NVIDIA H200 confidential VMs
  round out the security surface. The IO token is an SPL token on Solana used for settlement, staking, and rewards; fiat and USDC payments are accepted and converted to IO. io.net also publishes an MCP server at mcp.io.solutions for agent-driven cluster provisioning. The platform''s tagline is "the open-source AI infrastructure platform" and its commercial pitch is AI compute at 50–70% below comparable hyperscaler rates.'
features:
- IO Intelligence — OpenAI-compatible inference API for 15+ open-source models including Llama 3.3 70B
- IO Cloud — decentralized GPU compute spanning Container-as-a-Service, Ray clusters, Kubernetes clusters, and bare-metal
- IO Agents — agentic workflow builder with no-code visual editor and Agents API
- IO Explorer — network analytics, device and cluster metrics, block-reward tracking, proof-of-work transparency
- IO Worker — supplier-side onboarding for GPU providers across Ubuntu, Windows, macOS, HiveOS
- IO ID — unified user dashboard for wallets, credits, usage, and withdrawals
- IO Staking — device-owner staking plus collaborative co-staking with reliability scoring
- Confidential Compute on Intel TDX-enabled H100/H200/B200 GPUs with remote attestation
- Confidential Inference with cryptographic proof of secure execution
- MCP server at mcp.io.solutions for agent-driven IO Cloud provisioning
- Built on Solana — IO is an SPL token; fiat and USDC payments accepted and converted to IO
- Ray framework orchestration for distributed AI workloads
- Sub-API keys with per-model restrictions and per-key credit limits
- Vision (image upload) and reasoning content supported on IO Intelligence
- OpenAI SDK drop-in compatibility (`openai` Python / Node) with custom base_url
- Stripe / fiat credit-card billing alongside crypto settlement
- Pitched at 50–70% below hyperscaler GPU pricing
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/io-net.png
layout: provider
modified: '2026-05-25'
name: io.net
nav: Providers
network: true
overview: 'io.net publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Artificial Intelligence, GPU, Decentralized Compute, and DePIN.


  io.net''s developer surface includes developer portal, documentation, getting-started guide, API reference, signup flow, developer console, engineering blog, and 22 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 20.1
  delta: -2.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/io-net/refs/heads/main/screenshots/io-net-2026-06-20T183527.png
security:
- kind: domain-security
  name: Io Net Domain Security
  slug: io-net-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: io-net
tags:
- AI
- Artificial Intelligence
- GPU
- Decentralized Compute
- DePIN
- Web3
- Solana
- Inference
- LLM
- Distributed Computing
- Ray
- Kubernetes
- Containers
- Confidential Compute
- Agents
- MCP
website: https://io.net
---
