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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.0
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for the Ellipsis coding-agent platform. Start and manage agent sessions, read back typed results and transcripts, manage agent configs, defaults and templates, set sandbox variables, list int
  name: Ellipsis API
  slug: ellipsis-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ellipsis-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://app.ellipsis.dev
- group: docs
  title: ''
  type: Documentation
  url: https://www.ellipsis.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.ellipsis.dev/docs/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.ellipsis.dev/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.ellipsis.dev/support
- group: company
  title: ''
  type: Blog
  url: https://www.ellipsis.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ellipsis-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.ellipsis.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.ellipsis.dev/install
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ellipsis.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ellipsis.dev/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ellipsis.dev
- group: auth
  title: ''
  type: Compliance
  url: https://www.ellipsis.dev/platform/security
- group: build
  title: ''
  type: CLI
  url: cli/ellipsis-cli.yml
- group: build
  title: ''
  type: Packages
  url: packages/ellipsis-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ellipsis-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ellipsis-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ellipsis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ellipsis-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ellipsis-llms.txt
created: '2026-07-17'
description: Ellipsis is a managed cloud platform for running autonomous coding agents at scale. Engineering teams define agents as YAML config files that live in their repositories, and Ellipsis runs them in isolated, ephemeral sandboxes to review pull requests, fix bugs, build features, and investigate production issues. Agents trigger automatically on cron schedules, GitHub pull-request lifecycle events, or @ellipsis-dev mentions, and can also be launched on demand from the dashboard, the REST API, or the `agent` CLI. The platform runs Claude, Codex, and Gemini models, enforces hard budget caps and scoped per-session credentials, retains zero source code, and provides full observability with audit trails and replayable execution. Ellipsis (YC W24) serves 400+ engineering teams across 67,000+ connected repositories.
image: https://www.ellipsis.dev/brand/lockup-dark-transparent.png
layout: provider
mcp_servers:
- description: ''
  name: ellipsis-mcp.yml
  slug: ellipsis-mcpyml
modified: '2026-07-19'
name: Ellipsis
nav: Providers
network: true
overview: 'Ellipsis publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Code Review, AI Agents, Coding Agents, and Developer Tools.


  Ellipsis'' developer surface includes developer portal, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 14 more developer resources.'
random_paper: 57
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 0.0
    developer_ergonomics: 58.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 35.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ellipsis/refs/heads/main/screenshots/ellipsis-2026-07-25T213149.png
security:
- kind: authentication
  name: Ellipsis Authentication
  slug: ellipsis-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Ellipsis Domain Security
  slug: ellipsis-domain-security
  summary_line: TLSv1.2 · DMARC
slug: ellipsis
tags:
- Company
- Code Review
- AI Agents
- Coding Agents
- Developer Tools
- Software Development
- Automation
- DevOps
- Pull Requests
website: https://app.ellipsis.dev
---
