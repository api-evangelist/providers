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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gradient Agentic Access
  operation_count: 3
  slug: gradient-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 3
apis:
- description: Chat completion
  name: Gradient Chat API
  slug: gradient-chat-api
- description: Text completion
  name: Gradient Completions API
  slug: gradient-completions-api
- description: Model listing and management
  name: Gradient Models API
  slug: gradient-models-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://gradient.network
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.gradient.network
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gradient.network
- group: docs
  title: ''
  type: APIReference
  url: https://docs.gradient.network/enterprise-solutions/gradient-cloud/api-reference-documentation
- group: company
  title: ''
  type: Blog
  url: https://gradient.network/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.com/invite/gradientnetwork
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GradientHQ
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gradient-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/gradient-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gradient-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gradient-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/gradient-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gradient-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/gradient-cloud-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/gradient-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/gradient-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gradient-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/gradient-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gradient-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/gradient-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/gradient-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Gradient is a decentralized AI infrastructure company building the Open Intelligence Stack — a peer-powered, sovereign alternative to centralized AI clouds. Its stack pairs Parallax (a distributed model-serving / world inference engine that turns heterogeneous machines into one AI cluster), Lattica (a universal peer-to-peer data-motion engine that moves model weights and inference tokens across a global machine mesh), Echo (distributed reinforcement learning) and Symphony (a decentralized multi-agent framework). Gradient Cloud is the enterprise inference offering, exposing an OpenAI-compatible REST API (model listing, chat completion, and text completion, streaming or non-streaming) at apis.gradient.network. The projects run atop a Solana-based network whose Sentry Node browser extension let contributors share edge compute. Gradient is backed by Multicoin Capital and Wing Venture Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gradient.png
layout: provider
mcp_servers:
- description: ''
  name: gradient-mcp.yml
  slug: gradient-mcpyml
modified: '2026-07-19'
name: Gradient
nav: Providers
network: true
overview: 'Gradient publishes 3 APIs on the [APIs.io](https://apis.io/) network: Chat API, Completions API, and Models API. Tagged areas include Company, Crypto Web3, Artificial Intelligence, Machine Learning, and LLM Inference.


  Gradient''s developer surface includes documentation, API reference, engineering blog, support, authentication, changelog, CLI, and 15 more developer resources.'
random_paper: 56
score:
  band: thin
  composite: 39.3
  delta: -1.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 62.4
    developer_ergonomics: 51.6
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 40.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gradient/refs/heads/main/screenshots/gradient-2026-07-25T220159.png
security:
- kind: authentication
  name: Gradient Authentication
  slug: gradient-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gradient Domain Security
  slug: gradient-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gradient
tags:
- Company
- Crypto Web3
- Artificial Intelligence
- Machine Learning
- LLM Inference
- Decentralized Infrastructure
- Distributed Computing
- Edge Computing
- Developer Tools
website: https://gradient.network
---
