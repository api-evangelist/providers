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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 37.5
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The hosted Runtime Cloud API — manage sandboxed coding-agent sessions, org templates, deployments, guardrails, secrets, knowledge and skill directives, and activity telemetry. Authenticated with scope
  name: Runtime Cloud API
  slug: runtime-cloud-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/runtime-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.runtm.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.runtm.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.runtm.com/cloud-api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.runtm.com/cloud-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.runtm.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.runtm.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/runtm-ai
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/JUuCkUKc
- group: commercial
  title: ''
  type: Pricing
  url: https://www.runtm.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.runtm.com/login
- group: start
  title: ''
  type: Login
  url: https://app.runtm.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.runtm.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.runtm.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/runtime-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/runtime-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/runtime-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/runtime-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/runtime-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/runtime-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/runtime-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/runtime-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/runtime-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/runtime-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/runtime-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/runtime-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/runtm-ai/runtm/blob/main/SECURITY.md
created: '2026-07-17'
description: Runtime (runtm.com) is a Y Combinator-backed platform (Spring 2026) that lets engineering and non-engineering teams safely run coding agents across an organization. It provides sandboxed per-session VMs, session-level observability, and configurable guardrails so teams can ship with agents like Claude Code, OpenAI Codex, and Gemini without breaking production. The hosted Runtime Cloud API (app.runtm.com/api/cloud) exposes sessions, templates, deployments, guardrails, secrets, knowledge and skill directives, and activity telemetry behind scoped bearer-token API keys, with a first-party CLI (runtm) and an agent-focused CLI (runtm-api).
image: https://runtm.com/og-image.png
layout: provider
modified: '2026-07-21'
name: Runtime
nav: Providers
network: true
overview: 'Runtime publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coding Agents, Developer Tools, AI Infrastructure, and Sandboxes.


  Runtime''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
random_paper: 7
rate_limits:
- limit_count: 0
  name: Runtime Rate Limits
  slug: runtime-rate-limits
scopes:
- name: Runtime Scopes
  scope_count: 20
  slug: runtime-scopes
  summary_line: 20 scopes
score:
  band: thin
  composite: 35.3
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 65.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.3
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Runtime Authentication
  slug: runtime-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Runtime Domain Security
  slug: runtime-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Runtime Vulnerability Disclosure
  slug: runtime-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: runtime
tags:
- Company
- Coding Agents
- Developer Tools
- AI Infrastructure
- Sandboxes
- Agent Orchestration
- DevOps
- Cloud
website: https://www.runtm.com/
---
