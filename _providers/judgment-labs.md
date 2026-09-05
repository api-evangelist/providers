---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.6
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The backend platform API behind Judgeval — ingests agent traces/spans, runs evaluations and judges, and serves traces, sessions, behaviors, datasets, and automations. Consumed through the Judgeval SDK
  name: Judgment Platform API
  slug: judgment-platform-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.judgmentlabs.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.judgmentlabs.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.judgmentlabs.ai/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://docs.judgmentlabs.ai/sdk-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.judgmentlabs.ai/documentation
- group: operate
  title: ''
  type: Support
  url: mailto:support@judgmentlabs.ai
- group: company
  title: ''
  type: Blog
  url: https://www.judgmentlabs.ai/blogs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JudgmentLabs
- group: start
  title: ''
  type: Login
  url: https://app.judgmentlabs.ai/login
- group: start
  title: ''
  type: SignUp
  url: https://app.judgmentlabs.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.judgmentlabs.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.judgmentlabs.ai/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.judgmentlabs.ai
- group: build
  title: ''
  type: Packages
  url: packages/judgment-labs-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/judgment-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/judgment-labs-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/judgment-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/judgment-labs-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/judgment-labs-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/judgment-labs-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/judgment-labs-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/judgment-labs-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/judgment-labs-domain-security.yml
created: '2026-07-17'
description: 'Judgment Labs builds the continuous-improvement stack for AI agents: tooling to trace, evaluate, monitor, and improve agent behavior in production. Its open-source Judgeval SDK (Python and TypeScript, with Go and Java clients) instruments agent frameworks and model providers to capture traces, spans, and tool calls; Agent Judges and Code Judges score behavior against natural-language rubrics and deterministic checks; and Agent Behavior Monitoring plus automations and alerts surface regressions and failure modes. The platform is accessed through the Judgeval SDKs, the judgment CLI, and a hosted MCP server, and integrates with LangGraph, OpenAI Agents SDK, Claude Agent SDK, Google ADK, Vercel AI SDK, LiveKit, Pipecat, and OpenTelemetry / OpenInference tracing pipelines. The company is backed by Lightspeed with a $32M round.'
image: https://www.judgmentlabs.ai/logo/full_logo_dark.svg
layout: provider
mcp_servers:
- description: 'The Judgment MCP server exposes production agent data — traces, sessions, behaviors, judges, projects, views, datasets, prompts, and automations — to MCP-capable AI code editors and to the in-product '
  name: Judgment Labs MCP Server
  slug: judgment-labs-mcp-server
modified: '2026-07-19'
name: Judgment Labs
nav: Providers
network: true
overview: 'Judgment Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Agents, Artificial Intelligence, Agent Evaluation, and Observability.


  Judgment Labs'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 34.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/judgment-labs/refs/heads/main/screenshots/judgment-labs-2026-07-25T223257.png
security:
- kind: authentication
  name: Judgment Labs Authentication
  slug: judgment-labs-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Judgment Labs Domain Security
  slug: judgment-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: judgment-labs
tags:
- Company
- Agents
- Artificial Intelligence
- Agent Evaluation
- Observability
- Tracing
- Monitoring
- LLM
- Developer Tools
- MCP
website: https://www.judgmentlabs.ai
---
