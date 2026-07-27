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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: true
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 83.7
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Lucent Agentic Access
  operation_count: 6
  slug: lucent-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 4
apis:
- description: The Insights API from Lucent — 1 operation(s) for insights.
  name: Lucent Insights API
  slug: lucent-insights-api
- description: The Issues API from Lucent — 2 operation(s) for issues.
  name: Lucent Issues API
  slug: lucent-issues-api
- description: The Sdk API from Lucent — 1 operation(s) for sdk.
  name: Lucent Sdk API
  slug: lucent-sdk-api
- description: The Signals API from Lucent — 1 operation(s) for signals.
  name: Lucent Signals API
  slug: lucent-signals-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: List unresolved issues, fetch the top one, and mark it resolved.
  name: Lucent — triage and resolve an issue
  slug: lucent-triage-and-resolve
artifact_total: 12
asyncapis:
- description: Lucent pushes signed HTTP callbacks to a receiver URL you register (Organization → Webhooks) when events happen in your organization. Deliveries are signed with HMAC-SHA256 (Lucent-Signature) and carr
  name: Lucent Webhooks
  slug: lucent-webhooks-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lucent-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lucent-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lucent-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lucent-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/lucent-mcp.yml
- group: build
  title: ''
  type: Packages
  url: packages/lucent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/lucent-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/lucent-cli.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/lucent-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lucent-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/lucent-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/lucent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/lucent-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/lucent-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lucent-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/lucent-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/lucent-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/lucent-webhooks-asyncapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/lucent-openapi-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/lucent-triage-and-resolve.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lucent-triage-issues.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lucent-monitor-signals-insights.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/lucent-ingest-replay.md
- group: company
  title: ''
  type: Website
  url: https://lucenthq.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.lucenthq.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lucenthq.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.lucenthq.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.lucenthq.com/quickstart
- group: company
  title: ''
  type: Blog
  url: https://lucenthq.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://lucenthq.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.lucenthq.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.lucenthq.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lucenthq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lucenthq.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://lucenthq.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lucent-ai
created: '2026-07-17'
description: 'Lucent is an AI product manager for session replay: it watches user session recordings continuously and automatically detects bugs and UX issues, surfacing them as prioritized, AI-verified issues with reproduction steps, console logs, network activity, and affected-user counts. It ingests rrweb session batches from a lightweight browser SDK (plus React Native and Flutter), imports replays from providers such as PostHog and Sentry, and exposes a REST Data API to read issues, signals, and insights and to update issue status, webhooks for issue events, and a hosted Model Context Protocol (MCP) server so agents like Claude and Cursor can query Lucent data directly. Founded 2025, Y Combinator Winter 2026 batch.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lucent.png
layout: provider
mcp_servers:
- description: ''
  name: lucent-mcp.yml
  slug: lucent-mcpyml
modified: '2026-07-20'
name: Lucent
nav: Providers
network: true
overview: 'Lucent publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Insights API, Issues API, Sdk API, and 1 more. Tagged areas include Company, Session Replay, Product Analytics, Bug Detection, and Observability.


  The Lucent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Lucent''s developer surface includes authentication, CLI, documentation, API reference, getting-started guide, engineering blog, pricing, and 29 more developer resources.'
random_paper: 39
scopes:
- name: Lucent Scopes
  scope_count: 2
  slug: lucent-scopes
  summary_line: 2 scopes
score:
  band: developing
  composite: 54.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 70.8
    developer_ergonomics: 80.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 54.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lucent/refs/heads/main/screenshots/lucent-2026-07-25T225640.png
security:
- kind: authentication
  name: Lucent Authentication
  slug: lucent-authentication
  summary_line: apiKey/http/oauth2 · 2 schemes
- kind: domain-security
  name: Lucent Domain Security
  slug: lucent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: lucent
tags:
- Company
- Session Replay
- Product Analytics
- Bug Detection
- Observability
- Artificial Intelligence
- Developer Tools
- MCP
- Webhooks
website: https://lucenthq.com
---
