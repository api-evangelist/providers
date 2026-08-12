---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Continue Dev Agentic Access
  operation_count: 8
  slug: continue-dev-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 5
apis:
- description: Open-source IDE plugins shipping for VS Code and JetBrains. Provide chat, edit, apply, autocomplete, and agent modes. Bring your own LLM (Anthropic, OpenAI, Mistral, OpenRouter, Ollama) or use the Con
  name: Continue IDE Extensions
  slug: ide-extensions
- description: 'Open-source command-line interface powering Continue''s source-controlled AI checks. Checks are markdown files in .continue/checks/ that run as full AI agents against pull requests and surface results '
  name: Continue CLI
  slug: continue-cli
- description: Hosted registry where teams publish and share assistants, blocks (models, rules, prompts, docs, MCP servers, context providers), and policy. Powers the Continue Hub IDE API and is the primary commerci
  name: Continue Hub
  slug: continue-hub
- description: Observability surface for tracking check outcomes, agent runs, and adoption metrics across an organization's repositories. Part of the Team and Company tiers.
  name: Continue Mission Control
  slug: mission-control
- description: The Ide API from Continue — 8 operation(s) for ide.
  name: Continue Ide API
  slug: continue-dev-ide-api
artifact_total: 66
collections:
- collection_type: postman
  name: Continue Hub Ide API
  slug: postman-continue-dev-ide-api
- collection_type: open
  name: Continue Hub IDE API
  slug: open-continue-dev-hub-ide-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/continuedev/continue/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/continuedev/continue/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/continuedev/continue/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/continuedev/continue/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/continuedev/continue/blob/main/CONTRIBUTING.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/continue/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/continue-dev-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/continue-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/continue-dev-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.continue.dev/
- group: start
  title: ''
  type: Portal
  url: https://www.continue.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.continue.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/continuedev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/continuedev/continue
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/continuedev
- group: company
  title: ''
  type: Blog
  url: https://blog.continue.dev/
- group: start
  title: ''
  type: Signup
  url: https://continue.dev/login
- group: commercial
  title: ''
  type: Pricing
  url: https://www.continue.dev/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.continue.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.continue.dev/checks/quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://docs.continue.dev/checks/reference
- group: docs
  title: ''
  type: ChecksDocs
  url: https://continue.dev/check
- group: other
  title: ''
  type: Hub
  url: https://hub.continue.dev/
- group: commercial
  title: ''
  type: License
  url: https://github.com/continuedev/continue/blob/main/LICENSE
- group: build
  title: ''
  type: SDKs
  url: https://github.com/continuedev/continue/tree/main/packages/continue-sdk/typescript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/continuedev/continue/tree/main/packages/continue-sdk/python
- group: build
  title: ''
  type: Tools
  url: https://github.com/continuedev/rules
- group: build
  title: ''
  type: Tools
  url: https://github.com/continuedev/create-software-factory
- group: build
  title: ''
  type: Tools
  url: https://github.com/continuedev/pollhook
- group: build
  title: ''
  type: Tools
  url: https://github.com/continuedev/instinct
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/continuedev/awesome-rules
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/continuedev/checks
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/anthropic-continue-hub
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/openai-continue-hub
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/mistral-continue-hub
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/openrouter-continue-hub
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/ollama-continue-hub
- group: build
  title: ''
  type: Plugins
  url: https://github.com/continuedev/google-continue-hub
- group: design
  title: ''
  type: SpectralRules
  url: rules/continue-dev-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/continue-dev-vocabulary.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/continue-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/continue-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/continue-dev-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.continue.dev/llms.txt
created: '2026-05-08'
description: Continue is the open-source AI code assistant for VS Code and JetBrains, distributed under Apache 2.0. The Continue IDE extensions and the Continue CLI federate to any LLM provider — Anthropic, OpenAI, Mistral, OpenRouter, Ollama, and a Continue-managed proxy — and load their configuration from Continue Hub. Continue Hub (api.continue.dev) is the registry and IDE API that serves assistants, blocks, models, rules, prompts, docs, and MCP servers to the extensions, along with free-trial status, organization policy, secrets sync, and the Stripe checkout URL for the Models Add-On. Continue has also pivoted into "continuous AI" — source- controlled checks that live as markdown files under .continue/checks/ and run in CI as GitHub status checks.
examples:
- key_count: 5
  name: Continue Dev Free Trial Status Example
  slug: continue-dev-free-trial-status-example
- key_count: 1
  name: Continue Dev List Organizations Example
  slug: continue-dev-list-organizations-example
features:
- Open-source VS Code extension with 33k+ GitHub stars on continuedev/continue
- Open-source JetBrains plugin (IntelliJ, PyCharm, GoLand, WebStorm, etc.)
- Open-source Continue CLI for local and CI execution
- Source-controlled AI checks (.continue/checks/*.md) that run as GitHub status checks on every PR
- Source-controlled assistants (.continue/agents/*.yaml) versioned alongside code
- Continue Hub registry for sharing assistants, blocks, models, rules, prompts, docs, and MCP servers
- Continue Hub IDE API (api.continue.dev) with 8 REST endpoints under /ide for assistants, organizations, policy, free-trial, secrets, and checkout
- BYO LLM provider — Anthropic, OpenAI, Mistral, OpenRouter, Ollama, AWS Bedrock, Google, xAI, Together AI, Cerebras, SambaNova, and more via Hub blocks
- Continue-managed proxy (alwaysUseProxy=true) routes model traffic through Continue with pass-through billing
- On-prem proxy option for organizations that need to keep prompt traffic inside their network
- Free trial with per-user chat and autocomplete quota tracked via /ide/free-trial-status
- Models Add-On purchasable via /ide/get-models-add-on-checkout-url (Stripe)
- Organization policy (allowed models, secret handling, telemetry) returned by /ide/policy
- Secrets sync from Hub to IDE via /ide/sync-secrets
- Mission Control metrics for tracking check outcomes and agent runs across repos
- Apache 2.0 license on extensions and CLI
- Auto-generated TypeScript and Python SDKs from the OpenAPI spec at packages/continue-sdk
- Swagger UI for local API exploration via npm run swagger-ui in packages/continue-sdk
- 70+ official Continue Hub blocks (per-provider repos under github.com/continuedev)
- Instinct — Continue's open Next Edit model
- Bearer auth with API keys prefixed con_
finops:
- name: Continue Dev Finops
  service_category: AI and Machine Learning
  slug: continue-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/continue-dev.png
integrations:
- description: Use Claude Opus, Sonnet, and Haiku as the chat/edit/apply/autocomplete model inside Continue. Anthropic-continue-hub publishes ready-to-use blocks.
  name: Anthropic
- description: Use GPT-class models as Continue model providers via openai-continue-hub.
  name: OpenAI
- description: mistral-continue-hub publishes Mistral models as Continue blocks.
  name: Mistral
- description: openrouter-continue-hub federates to any OpenRouter-hosted model.
  name: OpenRouter
- description: ollama-continue-hub points Continue at a local Ollama server for zero-egress inference.
  name: Ollama
- description: bedrock-continue-hub uses Bedrock-hosted models, including Claude on Bedrock.
  name: AWS Bedrock
- description: google-continue-hub federates to Gemini and Vertex AI models.
  name: Google
- description: Per-provider Continue Hub repositories ship blocks for each.
  name: Together AI, xAI, Cerebras, SambaNova, Cohere, IBM watsonx, Novita, NCompass, Inception Labs, Relace, IONOS
- description: Continue checks run in CI and report status checks back to the GitHub PR. The check-cli, checks-cli, and suggestions-cli automate these flows.
  name: GitHub
- description: Starter tier and above can connect Continue agents to Slack, Sentry, and Snyk.
  name: Slack, Sentry, Snyk
- description: docker-continue-hub publishes Docker-authored blocks for Continue.
  name: Docker
- description: Continue assistants compose MCP servers as tool sources; Continue maintains a fork of the official MCP TypeScript SDK.
  name: Model Context Protocol
json_schemas:
- name: Continue Hub Assistant
  property_count: 7
  slug: continue-dev-assistant
- name: Continue Free Trial Status
  property_count: 5
  slug: continue-dev-free-trial-status
- name: Continue Hub Organization
  property_count: 4
  slug: continue-dev-organization
json_structures:
- name: Continue Dev Assistant Structure
  property_count: 7
  slug: continue-dev-assistant-structure
jsonld:
- class_count: 0
  name: Continue Dev Context
  property_count: 5
  slug: continue-dev-context
layout: provider
modified: '2026-05-25'
name: Continue
nav: Providers
network: true
overview: 'Continue publishes 1 API on the [APIs.io](https://apis.io/) network: Ide API. Tagged areas include AI, Artificial Intelligence, Developer Tools, Code Assistant, and Open Source.


  The Continue catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Continue''s developer surface includes authentication, developer portal, documentation, engineering blog, signup flow, pricing, getting-started guide, and 37 more developer resources.'
plans:
- name: Continue Dev Plans Pricing
  plan_count: 4
  slug: continue-dev-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 4
  name: Continue Dev Rate Limits
  slug: continue-dev-rate-limits
rules:
- name: Continue API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: continue-dev-jsonschema-spectral-rules
- name: Continue API Rules
  rule_count: 5
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 3
  slug: continue-dev-rules
score:
  band: strong
  composite: 57.2
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.4
    developer_ergonomics: 52.2
    discoverability: 81.5
    governance: 68.8
    operational_transparency: 39.5
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/continue-dev/refs/heads/main/screenshots/continue-dev-2026-06-20T174940.png
security:
- kind: authentication
  name: Continue Dev Authentication
  slug: continue-dev-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Continue Dev Domain Security
  slug: continue-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: continue-dev
solutions:
- description: Codify coding standards as markdown checks; AI agents enforce them in CI on every pull request.
  name: Continuous AI for engineering teams
- description: Drop-in replacement for proprietary AI coding assistants without surrendering model choice or telemetry control.
  name: Open-source AI IDE for any LLM
- description: Centralize team assistants on Continue Hub instead of per-engineer config sprawl.
  name: Hub-managed assistant distribution
tags:
- AI
- Artificial Intelligence
- Developer Tools
- Code Assistant
- Open Source
- VS Code
- JetBrains
- CLI
- MCP
- Apache 2.0
use_cases:
- description: Use any frontier or local model directly inside VS Code and JetBrains without lock-in to one vendor.
  name: In-editor AI chat, edit, and apply
- description: Define checks as markdown in .continue/checks/, have AI enforce them on every PR, see results as GitHub status checks.
  name: Source-controlled coding standards enforced in CI
- description: Publish assistants on Continue Hub so every engineer pulls the same models, rules, prompts, docs, and MCP servers.
  name: Team-shared assistants
- description: Federate to a self-hosted Ollama, an OpenRouter account, or your own Anthropic/OpenAI key to keep AI spend on your existing provider.
  name: BYO LLM cost control
- description: Route model traffic through an on-prem Continue proxy so prompts and secrets never leave the corporate network.
  name: On-prem prompt isolation
- description: Run code completion against a local model for zero-egress, zero-cost inference.
  name: Local autocomplete with Ollama
- description: Compose MCP servers into a Continue assistant to give the agent access to internal tools without writing extension code.
  name: MCP tool integration
- description: Apply Continue's "standards as checks" model to legacy codebases — codify standards in markdown, then have AI agents drag the codebase toward them.
  name: Continuous AI
website: https://www.continue.dev/
---
