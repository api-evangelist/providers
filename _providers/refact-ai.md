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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: 'Local HTTP/LSP API exposed by the Rust `refact-lsp` engine that runs inside the user''s IDE or as a standalone server. Implements the agent runtime: provider/model capabilities, chat command queueing, '
  name: Refact Agent Engine API
  slug: refact-engine-api
- description: Refact Agent acts as an MCP (Model Context Protocol) client, attaching local or remote MCP servers (`npx`, Python `-m`, `docker run`, or remote SSE) into the agent's tool surface with per-tool confirm
  name: Refact MCP Integration
  slug: refact-mcp-integration
artifact_total: 26
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/smallcloudai/refact/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/smallcloudai/refact/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/smallcloudai/refact/blob/main/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/refact-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://refact.ai
- group: start
  title: ''
  type: Portal
  url: https://refact.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.refact.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.refact.ai/introduction/quickstart/
- group: other
  title: ''
  type: Enterprise
  url: https://refact.ai/enterprise/
- group: commercial
  title: ''
  type: Pricing
  url: https://refact.ai/pricing
- group: commercial
  title: ''
  type: Plans
  url: https://refact.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://refact.ai/blog/
- group: start
  title: ''
  type: Signup
  url: https://refact.smallcloud.ai/
- group: start
  title: ''
  type: Login
  url: https://refact.smallcloud.ai/
- group: operate
  title: ''
  type: Contact
  url: https://refact.ai/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smallcloudai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/refact
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/refact-vscode
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/refact-intellij
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/refact-bench
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/rust-sdk
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/smallcloudai/litellm
- group: commercial
  title: ''
  type: License
  url: https://github.com/smallcloudai/refact/blob/main/LICENSE
- group: build
  title: ''
  type: IDEExtension
  url: https://marketplace.visualstudio.com/items?itemName=smallcloud.codify
- group: build
  title: ''
  type: IDEExtension
  url: https://plugins.jetbrains.com/plugin/20647-refact-ai
- group: other
  title: ''
  type: AWSMarketplace
  url: https://aws.amazon.com/marketplace/seller-profile?id=seller-zb3svnusgaibm
- group: operate
  title: ''
  type: Discord
  url: https://www.smallcloud.ai/discord
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/refact_ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/smallcloud
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@refactai
created: '2026-05-25'
description: 'Refact.ai is an open-source, local-first AI coding assistant and autonomous software-engineering agent built by Small Magellanic Cloud Ai Ltd. ("SmallCloud"). The product combines an IDE-integrated chat experience (Ask / Explore / Debug / Review / Plan modes), accurate code completion powered by Qwen2.5-Coder with RAG over the workspace, and the Refact Agent — an autonomous mode that plans, executes, and iterates on engineering tasks end-to-end, integrating with Git hosts, databases, shells, browsers, and MCP servers. The full agent stack — a Rust HTTP/LSP engine (`refact-lsp`), a React/Vite chat GUI, and VS Code + JetBrains plugins — is open source under BSD-3-Clause at github.com/smallcloudai/refact and ranked #1 open-source agent on SWE-bench Lite (60.0%) and 93.3% on Aider''s Polyglot benchmark with thinking mode. Refact supports a cloud SaaS tier (Free / Pro / Enterprise) — though Refact Cloud is being wound down in favor of BYOK + self-hosting — plus enterprise on-premise
  deployment with LLM fine-tuning, AWS Marketplace listings, and bring-your-own-key access to Anthropic, OpenAI, Google, xAI, DeepSeek, Groq, Ollama, LM Studio, vLLM, GitHub Copilot, and any OpenAI-compatible endpoint. Refact is positioned as a privacy-preserving, self-hostable alternative to closed cloud coding agents — workspace context, checkpoints, knowledge graphs, and trajectories are stored locally; no code is sent to the vendor''s servers in self-hosted mode.'
features:
- Refact Agent — autonomous IDE agent that plans, executes, and iterates
- Agent modes — Ask, Explore, Debug, Review, Plan, Agent
- In-IDE chat with context-aware code understanding
- Real-time code completion powered by Qwen2.5-Coder + RAG over the workspace
- 25+ programming languages including Python, JavaScript/TypeScript, Java, Go, Rust, PHP, C#, Ruby, Kotlin, Swift
- Local-first execution — workspace context, checkpoints, knowledge, and trajectories stored locally
- Open-source agent stack under BSD-3-Clause (Rust engine + React GUI + IDE plugins)
- VS Code, JetBrains (IntelliJ, PyCharm, WebStorm, GoLand, CLion), Visual Studio, Neovim, Sublime Text plugins
- MCP (Model Context Protocol) client — attach any local or remote MCP server as agent tools
- Built-in tool integrations — GitHub, GitLab, Bitbucket, Docker, Chrome, Shell, PostgreSQL, MySQL, PDB
- Workspace checkpoints and one-click rollback for agent operations
- Knowledge graph and long-term memory across agent sessions
- Bring-Your-Own-Key for Anthropic, OpenAI, Google Gemini, xAI Grok, DeepSeek, Groq, OpenRouter, GitHub Copilot
- Local model providers — Ollama, LM Studio, vLLM, custom OpenAI-compatible endpoints
- LLM fine-tuning on company codebase (Refact, StarCoder, DeepSeek-Coder, CodeLlama variants)
- Enterprise on-premise deployment with full code privacy
- AWS Marketplace listing — EC2 deployment and usage-based pricing
- Runpod and reverse-proxy deployment recipes
- Image-to-code, code review, and AI Toolbox features
- Confirmation rules to block or prompt before sensitive tool/MCP calls
- null
- 93.3% on Aider Polyglot benchmark with thinking mode
- Coin-based usage metering on the cloud tier (replacing per-request limits)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/refact-ai.png
layout: provider
modified: '2026-05-25'
name: Refact.ai
nav: Providers
network: true
overview: 'Refact.ai publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Coding Assistant, AI Agent, Autonomous Agents, and Code Completion.


  Refact.ai''s developer surface includes developer portal, documentation, getting-started guide, pricing, engineering blog, signup flow, YouTube channel, and 23 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 14.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 14.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/refact-ai/refs/heads/main/screenshots/refact-ai-2026-06-20T192744.png
security:
- kind: domain-security
  name: Refact Ai Domain Security
  slug: refact-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: refact-ai
tags:
- Artificial Intelligence
- Coding Assistant
- AI Agent
- Autonomous Agents
- Code Completion
- Code Generation
- Developer Tools
- IDE
- VS Code
- JetBrains
- Self-Hosting
- On-Premise
- Open-Source
- LSP
- MCP
- Fine-Tuning
- SWE-Bench
- RAG
website: https://refact.ai
---
