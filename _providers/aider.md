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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 32
  human_in_the_loop: 1
  name: Aider Agentic Access
  operation_count: 40
  slug: aider-agentic-access
  summary_line: 40 operations · 32 acting · 1 human-in-the-loop
api_count: 15
apis:
- description: Aider exposes a Python module entrypoint (`python -m aider`) and an importable package (`aider.main.main`) so Aider can be embedded in Python scripts, CI workflows, and other agents. The same flags an
  name: Aider Python Module
  slug: python-module
- description: Aider Commands That Manage the Chat Session and History.
  name: Aider Chat API
  slug: aider-chat-api
- description: Aider Commands That Drive Code Edits and Diffs.
  name: Aider Editing API
  slug: aider-editing-api
- description: Aider Commands That Manage Files in the Chat Session.
  name: Aider Files API
  slug: aider-files-api
- description: Aider Commands That Wrap Git Operations.
  name: Aider Git API
  slug: aider-git-api
- description: Aider Commands That Move Data In and Out of the Session.
  name: Aider IO API
  slug: aider-io-api
- description: Aider Launch-Time Configuration via Flags, YAML, and Environment Variables.
  name: Aider Launch API
  slug: aider-launch-api
- description: Aider Repository-Map Inspection.
  name: Aider Map API
  slug: aider-map-api
- description: Aider Commands That Switch or Query LLM Models.
  name: Aider Models API
  slug: aider-models-api
- description: Aider Chat Modes (Code, Architect, Ask, Help, Context).
  name: Aider Modes API
  slug: aider-modes-api
- description: Aider Commands That Run Linters and Tests.
  name: Aider Quality API
  slug: aider-quality-api
- description: Aider Session Lifecycle Commands.
  name: Aider Session API
  slug: aider-session-api
- description: Aider Settings, Tokens, and Reasoning Controls.
  name: Aider Settings API
  slug: aider-settings-api
- description: Aider Voice-to-Code Input.
  name: Aider Voice API
  slug: aider-voice-api
- description: Aider Commands That Pull in Web Content.
  name: Aider Web API
  slug: aider-web-api
artifact_total: 101
collections:
- collection_type: open
  name: Aider CLI
  slug: open-aider-cli
common:
- group: operate
  title: ''
  type: Releases
  url: https://github.com/Aider-AI/aider/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/Aider-AI/aider/blob/main/CONTRIBUTING.md
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aider-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aider-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aider-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aider.chat/
- group: docs
  title: ''
  type: Documentation
  url: https://aider.chat/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Aider-AI/aider
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Aider-AI
- group: operate
  title: ''
  type: Issues
  url: https://github.com/Aider-AI/aider/issues
- group: operate
  title: ''
  type: Forums
  url: https://github.com/Aider-AI/aider/discussions
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/aider-chat/
- group: other
  title: ''
  type: Installation
  url: https://aider.chat/docs/install.html
- group: docs
  title: ''
  type: UsageGuide
  url: https://aider.chat/docs/usage.html
- group: other
  title: ''
  type: Configuration
  url: https://aider.chat/docs/config.html
- group: operate
  title: ''
  type: SupportedModels
  url: https://aider.chat/docs/llms.html
- group: other
  title: ''
  type: Leaderboard
  url: https://aider.chat/docs/leaderboards/
- group: company
  title: ''
  type: Blog
  url: https://aider.chat/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://aider.chat/HISTORY.html
- group: commercial
  title: ''
  type: License
  url: https://github.com/Aider-AI/aider/blob/main/LICENSE.txt
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/Tv2uQnR88V
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/paulgauthier
- group: design
  title: ''
  type: Conventions
  url: https://github.com/Aider-AI/conventions
- group: other
  title: ''
  type: Benchmarks
  url: https://github.com/Aider-AI/polyglot-benchmark
- group: build
  title: aider-install Bootstrapper
  type: Tools
  url: https://github.com/Aider-AI/aider-install
- group: build
  title: grep-ast Repository Map Helper
  type: Tools
  url: https://github.com/Aider-AI/grep-ast
- group: build
  title: Polyglot Benchmark Suite
  type: Tools
  url: https://github.com/Aider-AI/polyglot-benchmark
- group: build
  title: Refactor Benchmark Suite
  type: Tools
  url: https://github.com/Aider-AI/refactor-benchmark
- group: build
  title: SWE-Bench Harness
  type: Tools
  url: https://github.com/Aider-AI/aider-swe-bench
- group: build
  title: MCP Server (Community — disler/aider-mcp-server)
  type: Tools
  url: https://github.com/disler/aider-mcp-server
- group: build
  title: MCP Server (Community — sengokudaikon/aider-mcp-server)
  type: Tools
  url: https://github.com/sengokudaikon/aider-mcp-server
- group: build
  title: MCP Package Manager for Aider (mcpm-aider)
  type: Tools
  url: https://github.com/lutzleonhardt/mcpm-aider
- group: design
  title: ''
  type: Rules
  url: rules/aider-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aider-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aider-rate-limits.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/aider-cli-context.jsonld
created: '2026-05-08'
description: 'Aider is an open-source, terminal-based AI pair programmer that edits code directly inside a developer''s local Git repository. Written in Python and distributed via PyPI under the Apache 2.0 license, Aider is a BYO-LLM tool: the user supplies API keys for hosted models (Anthropic Claude, OpenAI, DeepSeek, Google Gemini, OpenRouter, Mistral, xAI, GROQ, Cohere, GitHub Copilot, Azure OpenAI, Amazon Bedrock, Vertex AI) or points it at local models running through Ollama, LM Studio, or any OpenAI-compatible endpoint. Distinguishing capabilities include a repository-wide codebase map that lets the model reason about files it has not been shown, multi-file architectural edits with diff-based patching, automatic Git commits with conventional commit messages, a lint/test/repair loop, image and URL context, voice-to-code, and an IDE bridge via `--watch-files` that picks up `AI!` / `AI?` comments written from any editor. Aider supports 100+ programming languages via tree-sitter, publishes
  a public LLM coding leaderboard (the polyglot benchmark across C++, Go, Java, JavaScript, Python, Rust), and has accumulated 45K+ GitHub stars with 4.5K+ forks. The product surface is a rich CLI (40+ in-chat slash commands across four chat modes: code, architect, ask, help) plus a Python module entrypoint (`python -m aider`); there is no hosted SaaS, no Aider-operated REST API, and no app-level rate-limiting or billing — all model inference is delegated to the user''s chosen provider, and any pricing, rate limits, and FinOps surface live with that provider.'
examples:
- key_count: 2
  name: Aider Cli Add Files Request Example
  slug: aider-cli-add-files-request-example
- key_count: 1
  name: Aider Cli Ask Request Example
  slug: aider-cli-ask-request-example
- key_count: 2
  name: Aider Cli Ask Response Example
  slug: aider-cli-ask-response-example
- key_count: 1
  name: Aider Cli Chat Mode Request Example
  slug: aider-cli-chat-mode-request-example
- key_count: 1
  name: Aider Cli Commit Request Example
  slug: aider-cli-commit-request-example
- key_count: 2
  name: Aider Cli Commit Result Example
  slug: aider-cli-commit-result-example
- key_count: 2
  name: Aider Cli Diff Result Example
  slug: aider-cli-diff-result-example
- key_count: 1
  name: Aider Cli Drop Files Request Example
  slug: aider-cli-drop-files-request-example
- key_count: 3
  name: Aider Cli Edit Request Example
  slug: aider-cli-edit-request-example
- key_count: 5
  name: Aider Cli Edit Result Example
  slug: aider-cli-edit-result-example
- key_count: 2
  name: Aider Cli File Listing Example
  slug: aider-cli-file-listing-example
- key_count: 1
  name: Aider Cli File Path Request Example
  slug: aider-cli-file-path-request-example
- key_count: 22
  name: Aider Cli Launch Config Example
  slug: aider-cli-launch-config-example
- key_count: 1
  name: Aider Cli Lint Request Example
  slug: aider-cli-lint-request-example
- key_count: 1
  name: Aider Cli Model Catalog Example
  slug: aider-cli-model-catalog-example
- key_count: 1
  name: Aider Cli Model Selection Example
  slug: aider-cli-model-selection-example
- key_count: 1
  name: Aider Cli Reasoning Effort Request Example
  slug: aider-cli-reasoning-effort-request-example
- key_count: 2
  name: Aider Cli Repository Map Example
  slug: aider-cli-repository-map-example
- key_count: 10
  name: Aider Cli Settings Snapshot Example
  slug: aider-cli-settings-snapshot-example
- key_count: 2
  name: Aider Cli Shell Request Example
  slug: aider-cli-shell-request-example
- key_count: 3
  name: Aider Cli Shell Result Example
  slug: aider-cli-shell-result-example
- key_count: 1
  name: Aider Cli Thinking Tokens Request Example
  slug: aider-cli-thinking-tokens-request-example
- key_count: 4
  name: Aider Cli Token Usage Example
  slug: aider-cli-token-usage-example
- key_count: 2
  name: Aider Cli Voice Transcript Example
  slug: aider-cli-voice-transcript-example
- key_count: 1
  name: Aider Cli Web Fetch Request Example
  slug: aider-cli-web-fetch-request-example
- key_count: 2
  name: Aider Cli Web Fetch Result Example
  slug: aider-cli-web-fetch-result-example
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aider.png
json_schemas:
- name: AddFilesRequest
  property_count: 2
  slug: aider-cli-add-files-request
- name: AskRequest
  property_count: 1
  slug: aider-cli-ask-request
- name: AskResponse
  property_count: 2
  slug: aider-cli-ask-response
- name: ChatModeRequest
  property_count: 1
  slug: aider-cli-chat-mode-request
- name: CommitRequest
  property_count: 1
  slug: aider-cli-commit-request
- name: CommitResult
  property_count: 2
  slug: aider-cli-commit-result
- name: DiffResult
  property_count: 2
  slug: aider-cli-diff-result
- name: DropFilesRequest
  property_count: 1
  slug: aider-cli-drop-files-request
- name: EditRequest
  property_count: 3
  slug: aider-cli-edit-request
- name: EditResult
  property_count: 5
  slug: aider-cli-edit-result
- name: FileListing
  property_count: 2
  slug: aider-cli-file-listing
- name: FilePathRequest
  property_count: 1
  slug: aider-cli-file-path-request
- name: LaunchConfig
  property_count: 22
  slug: aider-cli-launch-config
- name: LintRequest
  property_count: 1
  slug: aider-cli-lint-request
- name: ModelCatalog
  property_count: 1
  slug: aider-cli-model-catalog
- name: ModelSelection
  property_count: 1
  slug: aider-cli-model-selection
- name: ReasoningEffortRequest
  property_count: 1
  slug: aider-cli-reasoning-effort-request
- name: RepositoryMap
  property_count: 2
  slug: aider-cli-repository-map
- name: SettingsSnapshot
  property_count: 10
  slug: aider-cli-settings-snapshot
- name: ShellRequest
  property_count: 2
  slug: aider-cli-shell-request
- name: ShellResult
  property_count: 3
  slug: aider-cli-shell-result
- name: ThinkingTokensRequest
  property_count: 1
  slug: aider-cli-thinking-tokens-request
- name: TokenUsage
  property_count: 4
  slug: aider-cli-token-usage
- name: VoiceTranscript
  property_count: 2
  slug: aider-cli-voice-transcript
- name: WebFetchRequest
  property_count: 1
  slug: aider-cli-web-fetch-request
- name: WebFetchResult
  property_count: 2
  slug: aider-cli-web-fetch-result
json_structures:
- name: Aider Cli Add Files Request Structure
  property_count: 2
  slug: aider-cli-add-files-request-structure
- name: Aider Cli Ask Request Structure
  property_count: 1
  slug: aider-cli-ask-request-structure
- name: Aider Cli Ask Response Structure
  property_count: 2
  slug: aider-cli-ask-response-structure
- name: Aider Cli Chat Mode Request Structure
  property_count: 1
  slug: aider-cli-chat-mode-request-structure
- name: Aider Cli Commit Request Structure
  property_count: 1
  slug: aider-cli-commit-request-structure
- name: Aider Cli Commit Result Structure
  property_count: 2
  slug: aider-cli-commit-result-structure
- name: Aider Cli Diff Result Structure
  property_count: 2
  slug: aider-cli-diff-result-structure
- name: Aider Cli Drop Files Request Structure
  property_count: 1
  slug: aider-cli-drop-files-request-structure
- name: Aider Cli Edit Request Structure
  property_count: 3
  slug: aider-cli-edit-request-structure
- name: Aider Cli Edit Result Structure
  property_count: 5
  slug: aider-cli-edit-result-structure
- name: Aider Cli File Listing Structure
  property_count: 2
  slug: aider-cli-file-listing-structure
- name: Aider Cli File Path Request Structure
  property_count: 1
  slug: aider-cli-file-path-request-structure
- name: Aider Cli Launch Config Structure
  property_count: 22
  slug: aider-cli-launch-config-structure
- name: Aider Cli Lint Request Structure
  property_count: 1
  slug: aider-cli-lint-request-structure
- name: Aider Cli Model Catalog Structure
  property_count: 1
  slug: aider-cli-model-catalog-structure
- name: Aider Cli Model Selection Structure
  property_count: 1
  slug: aider-cli-model-selection-structure
- name: Aider Cli Reasoning Effort Request Structure
  property_count: 1
  slug: aider-cli-reasoning-effort-request-structure
- name: Aider Cli Repository Map Structure
  property_count: 2
  slug: aider-cli-repository-map-structure
- name: Aider Cli Settings Snapshot Structure
  property_count: 10
  slug: aider-cli-settings-snapshot-structure
- name: Aider Cli Shell Request Structure
  property_count: 2
  slug: aider-cli-shell-request-structure
- name: Aider Cli Shell Result Structure
  property_count: 3
  slug: aider-cli-shell-result-structure
- name: Aider Cli Thinking Tokens Request Structure
  property_count: 1
  slug: aider-cli-thinking-tokens-request-structure
- name: Aider Cli Token Usage Structure
  property_count: 4
  slug: aider-cli-token-usage-structure
- name: Aider Cli Voice Transcript Structure
  property_count: 2
  slug: aider-cli-voice-transcript-structure
- name: Aider Cli Web Fetch Request Structure
  property_count: 1
  slug: aider-cli-web-fetch-request-structure
- name: Aider Cli Web Fetch Result Structure
  property_count: 2
  slug: aider-cli-web-fetch-result-structure
jsonld:
- class_count: 26
  name: Aider Cli Context
  property_count: 63
  slug: aider-cli-context
layout: provider
modified: '2026-05-30'
name: Aider
nav: Providers
network: true
overview: 'Aider publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Editing API, Files API, and 11 more. Tagged areas include AI, AI Pair Programming, Developer Tools, CLI, and Command Line.


  The Aider catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Aider''s developer surface includes authentication, documentation, GitHub presence, engineering blog, changelog, tooling, and 30 more developer resources.'
random_paper: 37
rate_limits:
- limit_count: 4
  name: Aider Rate Limits
  slug: aider-rate-limits
rules:
- name: Aider API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: aider-jsonschema-spectral-rules
- name: Aider API Rules
  rule_count: 38
  severity_counts:
    error: 19
    hint: 0
    info: 4
    warn: 15
  slug: aider-rules
score:
  band: thin
  composite: 32.6
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 21.9
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 32.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 14
      marker_coverage: 100.0
      total: 14
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aider/refs/heads/main/screenshots/aider-2026-06-20T170838.png
security:
- kind: authentication
  name: Aider Authentication
  slug: aider-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aider Domain Security
  slug: aider-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: aider
tags:
- AI
- AI Pair Programming
- Developer Tools
- CLI
- Command Line
- Coding Assistant
- Code Generation
- Open Source
- Python
- Apache 2.0
- LLM
- Git
- BYO LLM
- Terminal
- Polyglot
- Tree Sitter
- Repository Map
- Pair Programming
website: https://aider.chat/
---
