---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 46
  human_in_the_loop: 1
  name: Plandex Agentic Access
  operation_count: 80
  slug: plandex-agentic-access
  summary_line: 80 operations · 46 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: User account, email verification, and authentication operations.
  name: Plandex Accounts API
  slug: plandex-accounts-api
- description: Per-plan branches for parallel exploration and diffing.
  name: Plandex Branches API
  slug: plandex-branches-api
- description: Files, directory trees, URLs, notes, and images loaded into a plan.
  name: Plandex Context API
  slug: plandex-context-api
- description: Prompts, responses, and rewind history within a plan branch.
  name: Plandex Conversation API
  slug: plandex-conversation-api
- description: Per-file pending changes, apply, and reject operations.
  name: Plandex Diffs API
  slug: plandex-diffs-api
- description: Streaming connect, build, tell, and stop endpoints for plan execution.
  name: Plandex Execution API
  slug: plandex-execution-api
- description: Tree-sitter project map generation and cached map loading.
  name: Plandex FileMap API
  slug: plandex-filemap-api
- description: Operational health and version endpoints.
  name: Plandex Health API
  slug: plandex-health-api
- description: Invite users into an org and manage pending invites.
  name: Plandex Invites API
  slug: plandex-invites-api
- description: Model packs, custom models, custom providers, default settings.
  name: Plandex Models API
  slug: plandex-models-api
- description: Organization and role membership management.
  name: Plandex Orgs API
  slug: plandex-orgs-api
- description: Long-running, branchable units of AI coding work over loaded context.
  name: Plandex Plans API
  slug: plandex-plans-api
- description: Project containers that group plans, mapped to a working directory.
  name: Plandex Projects API
  slug: plandex-projects-api
- description: Per-plan model settings, default settings, and org/user config.
  name: Plandex Settings API
  slug: plandex-settings-api
- description: User listing and removal within an org.
  name: Plandex Users API
  slug: plandex-users-api
artifact_total: 87
collections:
- collection_type: open
  name: Plandex Server API
  slug: open-plandex-server
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plandex-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plandex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://plandex.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.plandex.ai
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plandex.ai/quick-start
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.plandex.ai/hosting/self-hosting/local-mode-quickstart
- group: other
  title: ''
  type: Install
  url: https://plandex.ai/install.sh
- group: build
  title: ''
  type: GitHub
  url: https://github.com/plandex-ai/plandex
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plandex-ai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/plandex-ai/plandex
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/plandex-ai/plandex
- group: commercial
  title: ''
  type: License
  url: https://github.com/plandex-ai/plandex/blob/main/LICENSE
- group: build
  title: ''
  type: CLI
  url: https://docs.plandex.ai/cli-reference
- group: other
  title: ''
  type: REPL
  url: https://docs.plandex.ai/repl
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.plandex.ai/hosting/cloud
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plandex.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plandex.ai/terms
- group: auth
  title: ''
  type: Security
  url: https://docs.plandex.ai/security
- group: company
  title: ''
  type: Blog
  url: https://plandex.ai/blog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/plandex-ai/plandex/releases
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/plandex-ai/plandex/releases
- group: operate
  title: ''
  type: Support
  url: https://github.com/plandex-ai/plandex/issues
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/plandex-ai
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/plandex_ai
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@plandex-ai
- group: operate
  title: ''
  type: Forums
  url: https://github.com/plandex-ai/plandex/discussions
- group: operate
  title: ''
  type: Issues
  url: https://github.com/plandex-ai/plandex/issues
- group: other
  title: ''
  type: Docker
  url: https://hub.docker.com/r/plandexai/plandex-server
- group: other
  title: ''
  type: DockerCompose
  url: https://github.com/plandex-ai/plandex/blob/main/app/docker-compose.yml
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/rules/plandex-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/vocabulary/plandex-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/json-ld/plandex-context.jsonld
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/plans/plandex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/rate-limits/plandex-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/plandex/main/finops/plandex-finops.yml
created: '2026-05-25'
description: Plandex is an open-source, terminal-based AI coding agent designed to take on large, multi-step software development tasks across many files in real world codebases. Written in Go and released under the MIT license, Plandex builds and executes long-running "plans" — durable, branchable units of work that combine intelligent context management, project maps generated with tree-sitter for 30+ programming languages, an effective 2M-token context window, and a cumulative diff review sandbox that isolates AI edits until a developer explicitly applies them. The tool ships as a CLI with an interactive REPL (fuzzy auto-complete), supports automated debugging of terminal commands and browser applications, integrates with Git for branching and commit-message generation, and is provider-neutral — working with Anthropic Claude, OpenAI, Google Gemini, OpenRouter.ai, Azure OpenAI, AWS Bedrock, DeepSeek, Perplexity, Ollama, and any OpenAI-compatible custom provider. The Plandex Server exposes
  a REST management/orchestration API (over 60 endpoints across accounts, orgs, projects, plans, branches, context, conversation, diffs, settings, model packs, and streaming execution) that powers both the CLI/REPL and the hosted Plandex Cloud. Plandex Cloud is winding down as of 2025-10-03; Plandex is now distributed primarily as a Docker-based self-hosted / local-mode product that users run with their own model-provider API keys.
examples:
- key_count: 11
  name: Plandex Server Context Item Example
  slug: plandex-server-context-item-example
- key_count: 8
  name: Plandex Server Convo Message Example
  slug: plandex-server-convo-message-example
- key_count: 11
  name: Plandex Server Model Pack Example
  slug: plandex-server-model-pack-example
- key_count: 11
  name: Plandex Server Plan Config Example
  slug: plandex-server-plan-config-example
- key_count: 10
  name: Plandex Server Plan Example
  slug: plandex-server-plan-example
features:
- description: Smart context management loads only what's needed per step, enabling reliable work in large projects and files.
  name: 2M-Token Effective Context Window
- description: Fast project map generation and syntax validation across 30+ programming languages. Indexes directories with 20M+ tokens.
  name: Tree-Sitter Project Maps
- description: AI-generated changes are isolated from project files until explicitly applied, with cumulative review and roll-back.
  name: Cumulative Diff Sandbox
- description: Five autonomy levels — None, Basic, Plus, Semi-Auto, Full-Auto — selectable per-plan or via CLI flags.
  name: Configurable Autonomy
- description: Repeatedly runs commands (builds, tests, lints, scripts) and auto-fixes failures with rollback. Also debugs browser apps via Chrome.
  name: Automated Debugging
- description: Curated combinations of models bound to internal roles (planner, coder, builder, summarizer, verifier, context loader); built-in packs for daily, reasoning, strong, cheap, oss, and planner-specialized variants.
  name: Model Packs
- description: First-class support for Anthropic, OpenAI, Google AI Studio, Google Vertex AI, Azure OpenAI, AWS Bedrock, DeepSeek, Perplexity, OpenRouter, Ollama, and any OpenAI-compatible custom provider.
  name: Multi-Provider Support
- description: Plandex can use a Claude Pro or Max subscription as the credential when calling Anthropic models.
  name: Claude Pro/Max Subscription
- description: Built-in context caching across OpenAI, Anthropic, and Google models reduces latency and cost on multi-step plans.
  name: Context Caching
- description: Every plan update is versioned, with branching for exploring multiple paths or comparing different models. Rewind to any prior SHA.
  name: Plan Version Control
- description: Commit message generation, optional auto-commits, and clean integration with project git history.
  name: Git Integration
- description: Interactive shell launched by `plandex` (or `pdx`) with fuzzy command and file completion; backslash equivalents (`\new`, `\tell`) for every command.
  name: REPL with Fuzzy Auto-Complete
- description: Zero-dependency CLI install via `curl -sL https://plandex.ai/install.sh | bash`. Docker compose for the self-hosted server.
  name: One-Line Install
- description: '`--bg` flag runs plans concurrently in the background under separate streams.'
  name: Background Tasks
- description: Loads only the files needed for each implementation step (smart-context) and uses the project map to choose them (auto-load-context).
  name: Smart Context + Auto-Load Context
- description: tell, build, and connect endpoints stream model responses live; clients can reconnect to in-progress plans after disconnects.
  name: Streaming Plan Execution
finops:
- name: Plandex Finops
  service_category: Developer Tools / AI Coding Agent
  slug: plandex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plandex.png
integrations:
- description: Direct Anthropic API integration; also supports Claude Pro/Max subscriptions.
  name: Anthropic Claude
- description: Direct OpenAI API integration via OPENAI_API_KEY.
  name: OpenAI
- description: Default recommended provider for self-hosted Plandex; also used as a failover route across other configured providers.
  name: OpenRouter.ai
- description: Gemini models via GEMINI_API_KEY.
  name: Google AI Studio
- description: Gemini and Anthropic models via Vertex AI credentials.
  name: Google Vertex AI
- description: OpenAI models on Azure with deployment-name mapping.
  name: Microsoft Azure OpenAI
- description: Anthropic models on Bedrock with AWS profile or env-var credentials.
  name: AWS Bedrock
- description: DeepSeek models via DEEPSEEK_API_KEY.
  name: DeepSeek
- description: Perplexity models via PERPLEXITY_API_KEY.
  name: Perplexity
- description: Local model hosting via Ollama; no API keys required.
  name: Ollama
- description: Any OpenAI-compatible API can be added via a JSON config (`plandex models custom`).
  name: Custom Providers
- description: Instant-apply fallback model used when Plandex cannot apply edits deterministically (Plandex Cloud).
  name: Relace
- description: Branching, commit-message generation, optional auto-commits.
  name: Git
- description: Automated debugging of browser applications when Chrome is installed.
  name: Chrome
- description: Self-hosted server distributed as a Docker image with a published docker-compose stack.
  name: Docker
- description: Backing database for the Plandex server.
  name: Postgres
- description: Embedded LiteLLM proxy used by the server to talk to model providers uniformly.
  name: LiteLLM Proxy
- description: Payment processing for Plandex Cloud subscriptions and credit purchases.
  name: Stripe
- description: Email marketing for Plandex updates (Plandex Cloud).
  name: Loops
- description: Basic usage analytics (Plandex Cloud).
  name: Google Analytics
- description: Error tracking (Plandex Cloud).
  name: Rollbar
json_schemas:
- name: Branch
  property_count: 6
  slug: plandex-server-branch
- name: ContextItem
  property_count: 12
  slug: plandex-server-context-item
- name: ConvoMessage
  property_count: 8
  slug: plandex-server-convo-message
- name: ModelPack
  property_count: 11
  slug: plandex-server-model-pack
- name: PlanConfig
  property_count: 11
  slug: plandex-server-plan-config
- name: Plan
  property_count: 10
  slug: plandex-server-plan
json_structures:
- name: Plandex Server Context Item Structure
  property_count: 12
  slug: plandex-server-context-item-structure
- name: Plandex Server Model Pack Structure
  property_count: 11
  slug: plandex-server-model-pack-structure
- name: Plandex Server Plan Structure
  property_count: 10
  slug: plandex-server-plan-structure
jsonld:
- class_count: 41
  name: Plandex Context
  property_count: 2
  slug: plandex-context
layout: provider
modified: '2026-05-29'
name: Plandex
nav: Providers
network: true
overview: 'Plandex publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Branches API, Context API, and 12 more. Tagged areas include AI, AI Coding Agent, Developer Tools, Open Source, and CLI.


  The Plandex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Plandex''s developer surface includes authentication, documentation, getting-started guide, GitHub presence, CLI, pricing, engineering blog, and 28 more developer resources.'
plans:
- name: Plandex Plans Pricing
  plan_count: 3
  slug: plandex-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 5
  name: Plandex Rate Limits
  slug: plandex-rate-limits
rules:
- name: Plandex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: plandex-jsonschema-spectral-rules
- name: Plandex API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 4
    warn: 3
  slug: plandex-rules
score:
  band: strong
  composite: 63.6
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 61.3
    developer_ergonomics: 43.5
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 63.2
  previous_composite: 63.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Plandex Authentication
  slug: plandex-authentication
  summary_line: http · 1 scheme
slug: plandex
solutions:
- description: Run Plandex locally with Docker and BYO model-provider keys. MIT-licensed and free.
  name: Self-Hosted / Local Mode
- description: Hosted Plandex with user-supplied provider keys, $30/month after trial. Winding down 2025-10-03.
  name: Plandex Cloud — BYO API Key Mode (Historical)
- description: Hosted Plandex with integrated credit billing, $45/month including $20/mo of non-expiring credits. Winding down 2025-10-03.
  name: Plandex Cloud — Integrated Models Mode (Historical)
tags:
- AI
- AI Coding Agent
- Developer Tools
- Open Source
- CLI
- Terminal
- LLM
- Coding Assistant
- Agents
- Go
- Context Management
- Plans
- Self-Hosted
- REST
use_cases:
- description: Coordinate refactors that touch dozens of files across a large codebase without losing the thread between steps.
  name: Large Refactors
- description: Work in repositories that span 30+ languages thanks to tree-sitter project maps.
  name: Polyglot Project Work
- description: Take a feature from idea through chat mode, into a detailed implementation plan, into reviewed and applied file changes.
  name: Adding Features To Real Projects
- description: Wrap a flaky build, test, or browser app in `plandex debug` and let Plandex iteratively repair it.
  name: Automated Debugging
- description: Use chat mode and the project map to ask questions about an unfamiliar codebase.
  name: Codebase Onboarding And Q&A
- description: Branch a plan to run different model packs against the same context and compare results.
  name: Multi-Model Comparisons
- description: Kick off `--bg` plans, switch repos, and reconnect to streaming output later.
  name: Long-Running Background Coding
- description: Use a Claude Pro/Max subscription as the credential for an autonomous coding agent.
  name: BYO Subscription Coding Agent
- description: Run the Plandex server in Docker on-prem with locally-hosted Ollama models or a private custom provider.
  name: Self-Hosted AI Coding For Sensitive Codebases
website: https://plandex.ai
---
