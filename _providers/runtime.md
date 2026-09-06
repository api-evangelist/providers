---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-05'
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
random_paper: 16
rate_limits:
- limit_count: 2
  name: Runtime Rate Limits
  slug: runtime-rate-limits
scopes:
- name: Runtime Scopes
  scope_count: 20
  slug: runtime-scopes
  summary_line: 20 scopes
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 15
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 50.0
  previous_composite: 33.8
  provenance:
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/runtime/refs/heads/main/screenshots/runtime-2026-09-02T154238.png
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
