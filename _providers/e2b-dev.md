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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: E2B Dev Agentic Access
  operation_count: 67
  slug: e2b-dev-agentic-access
  summary_line: 67 operations · 36 acting · 1 human-in-the-loop
api_count: 14
apis:
- description: 'Higher-level SDK on top of the Sandbox API that exposes a Jupyter-style code interpreter for LLM-driven Python and JavaScript execution. Returns structured execution results including stdout, stderr, '
  name: E2B Code Interpreter SDK
  slug: e2b-code-interpreter-api
- description: Sandbox flavor that boots a Linux desktop environment with a noVNC stream and exposes mouse, keyboard, screenshot, and window-management primitives. Built for computer-use agents pairing vision-capabl
  name: E2B Desktop Sandbox SDK
  slug: e2b-desktop-api
- description: The access-tokens API from E2B — 2 operation(s) for access-tokens.
  name: E2B access-tokens API
  slug: e2b-dev-access-tokens-api
- description: The admin API from E2B — 4 operation(s) for admin.
  name: E2B admin API
  slug: e2b-dev-admin-api
- description: The api-keys API from E2B — 2 operation(s) for api-keys.
  name: E2B api-keys API
  slug: e2b-dev-api-keys-api
- description: The auth API from E2B — 3 operation(s) for auth.
  name: E2B auth API
  slug: e2b-dev-auth-api
- description: The events API from E2B — 2 operation(s) for events.
  name: E2B events API
  slug: e2b-dev-events-api
- description: The Health API from E2B — 1 operation(s) for health.
  name: E2B Health API
  slug: e2b-dev-health-api
- description: The sandboxes API from E2B — 13 operation(s) for sandboxes.
  name: E2B sandboxes API
  slug: e2b-dev-sandboxes-api
- description: The snapshots API from E2B — 1 operation(s) for snapshots.
  name: E2B snapshots API
  slug: e2b-dev-snapshots-api
- description: The tags API from E2B — 2 operation(s) for tags.
  name: E2B tags API
  slug: e2b-dev-tags-api
- description: The templates API from E2B — 11 operation(s) for templates.
  name: E2B templates API
  slug: e2b-dev-templates-api
- description: The volumes API from E2B — 5 operation(s) for volumes.
  name: E2B volumes API
  slug: e2b-dev-volumes-api
- description: The webhooks API from E2B — 2 operation(s) for webhooks.
  name: E2B webhooks API
  slug: e2b-dev-webhooks-api
artifact_total: 47
collections:
- collection_type: open
  name: E2B API
  slug: open-e2b-api
- collection_type: open
  name: E2B Sandbox Events and Webhooks API
  slug: open-e2b-events
- collection_type: open
  name: E2B API
  slug: open-e2b-volumes
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/e2b-dev-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/e2b-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/e2b-dev-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/e2b-dev-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://e2b.dev
- group: docs
  title: ''
  type: Documentation
  url: https://e2b.dev/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://e2b.dev/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://e2b.dev/docs/sdk-reference
- group: auth
  title: ''
  type: Authentication
  url: https://e2b.dev/docs/api-key
- group: docs
  title: ''
  type: Documentation
  url: https://e2b.dev/docs/cli
- group: start
  title: ''
  type: Portal
  url: https://e2b.dev/dashboard
- group: auth
  title: ''
  type: Authentication
  url: https://e2b.dev/dashboard?tab=keys
- group: start
  title: ''
  type: Signup
  url: https://e2b.dev/auth/sign-up
- group: company
  title: ''
  type: Blog
  url: https://e2b.dev/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://e2b.dev/changelog
- group: operate
  title: ''
  type: Support
  url: https://e2b.dev/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://e2b.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://e2b.dev/privacy
- group: auth
  title: ''
  type: TrustCenter
  url: https://e2b.dev/security
- group: company
  title: ''
  type: Twitter
  url: https://x.com/e2b_dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/e2b-dev
- group: operate
  title: ''
  type: Forums
  url: https://discord.gg/U7KEcGErtQ
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/e2b-dev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/E2B
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/infra
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/firecracker
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/code-interpreter
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/desktop
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/surf
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/fragments
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/ai-analyst
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/open-computer-use
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/e2b-dev/e2b-cookbook
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/dashboard
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/docs
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/awesome-ai-agents
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/awesome-ai-sdks
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/e2b-dev/awesome-mcp-gateways
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/e2b
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@e2b/code-interpreter
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/e2b/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/e2b-code-interpreter/
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/e2b-desktop/
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@e2b/desktop
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@e2b/cli
- group: commercial
  title: ''
  type: Plans
  url: plans/e2b-dev-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/e2b-dev-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/e2b-dev-finops.yml
created: '2026-05-25'
description: E2B (e2b-dev) provides secure, isolated cloud sandboxes for AI agents and AI-generated code, built on a forked Firecracker microVM runtime. The platform ships a REST Sandbox API, JavaScript and Python SDKs, a Code Interpreter SDK, a Desktop Sandbox for computer-use agents, persistent volumes, a custom template build system, and an e2b CLI. The Apache-2.0 licensed core repos — E2B, infra, firecracker, code-interpreter, and desktop — also support self-hosted deployments on AWS, GCP, Azure, or bare Linux. E2B is LLM-agnostic and used by labs and enterprises building code interpreters, deep-research agents, data analysis features, reinforcement-learning environments, and computer-use agents.
examples:
- key_count: 2
  name: E2B Create Sandbox Example
  slug: e2b-create-sandbox-example
- key_count: 2
  name: E2B List Templates Example
  slug: e2b-list-templates-example
features:
- Firecracker microVM sandboxes that cold-start in under 200ms in-region and run up to 24 hours on Pro
- Pause, resume, and snapshot sandboxes to persist agent state across invocations
- Custom sandbox templates built from e2b.toml or programmatic SDK definitions with cached build layers
- Persistent volumes attachable to any sandbox with a separate Volume Content API authenticated by short-lived JWTs
- Up to 100 concurrent sandboxes on Pro (expandable to 1,100 with purchase) and up to 20 on Hobby
- Adjustable per-sandbox CPU and RAM, plus 10-20 GiB of free storage depending on tier
- JavaScript/TypeScript and Python SDKs for the Sandbox, Code Interpreter, and Desktop products
- Code Interpreter SDK returns Jupyter-style outputs (stdout, charts, images, html, markdown, latex)
- Desktop Sandbox boots a Linux desktop with noVNC stream and mouse/keyboard/screenshot primitives for computer-use agents
- MCP Gateway and MCP server integrations that expose sandboxes as tools to Claude, ChatGPT, and other MCP clients
- LLM-agnostic — works with Anthropic, OpenAI, Mistral, Llama, and any custom model
- Built-in integration patterns with LangChain, LlamaIndex, Vercel AI SDK, CrewAI, AutoGen, and Hugging Face
- Open-source CLI (`e2b`) for template init, build, list, deploy, sandbox connect, and logs
- Apache-2.0 licensed core; the platform is buildable from the e2b-dev/infra Go monorepo for self-hosting on AWS, GCP, Azure, or bare Linux
- Enterprise BYOC and on-prem deployments with a forked Firecracker microVM runtime in Rust
- Per-second usage-based pricing on CPU, RAM, and storage with a $100 signup credit
- Used in production by AI labs, agent startups, and Fortune 100 enterprises; 1B+ sandboxes started and 3.5M+ monthly SDK downloads
finops:
- name: E2B Dev Finops
  service_category: ''
  slug: e2b-dev-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/e2b-dev.png
json_schemas:
- name: E2B Sandbox
  property_count: 14
  slug: e2b-sandbox
- name: E2B Sandbox Template
  property_count: 9
  slug: e2b-template
jsonld:
- class_count: 20
  name: E2B Dev Context
  property_count: 11
  slug: e2b-dev-context
layout: provider
modified: '2026-05-30'
name: E2B
nav: Providers
network: true
overview: 'E2B publishes 12 APIs on the [APIs.io](https://apis.io/) network, including access-tokens API, admin API, api-keys API, and 9 more. Tagged areas include AI, Agents, Code Execution, Code Interpreter, and Sandboxes.


  The E2B catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  E2B''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, signup flow, engineering blog, and 41 more developer resources.'
plans:
- name: E2B Dev Plans Pricing
  plan_count: 3
  slug: e2b-dev-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: E2B Dev Rate Limits
  slug: e2b-dev-rate-limits
rules:
- name: E2B API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: e2b-dev-jsonschema-spectral-rules
score:
  band: strong
  composite: 64.7
  delta: 4.2
  facets:
    commercial_clarity: 68.4
    contract_quality: 63.6
    developer_ergonomics: 73.9
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 21.1
  previous_composite: 60.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/e2b-dev/refs/heads/main/screenshots/e2b-dev-2026-06-20T180353.png
security:
- kind: authentication
  name: E2B Dev Authentication
  slug: e2b-dev-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: E2B Dev Domain Security
  slug: e2b-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: E2B Dev Vulnerability Disclosure
  slug: e2b-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: e2b-dev
tags:
- AI
- Agents
- Code Execution
- Code Interpreter
- Sandboxes
- Firecracker
- microVMs
- Computer Use
- Desktop Sandbox
- Templates
- MCP
- Open Source
website: https://e2b.dev
---
