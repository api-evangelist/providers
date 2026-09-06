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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-09-05'
api_count: 3
apis:
- description: Run SELECT-only ClickHouse SQL over a project's observability data via POST /v1/sql/query. Authenticates with a project API key as a bearer token, accepts a query plus typed {name:Type} parameters, an
  name: Laminar SQL Query API
  slug: laminar-sql-query-api
- description: 'The standard OpenTelemetry trace ingest endpoint at /v1/traces. Laminar accepts OTLP over gRPC, HTTP+protobuf, and (since May 2026) HTTP+JSON, so any OpenTelemetry-capable runtime — including browser '
  name: Laminar OpenTelemetry Trace Ingest API
  slug: laminar-otlp-trace-ingest-api
- description: 'The lower-level LaminarClient.evals surface for wiring evaluations into an existing pipeline: create an evaluation, pre-register each datapoint so a row is visible in the UI before the executor runs, '
  name: Laminar Evaluations API
  slug: laminar-evaluations-api
artifact_total: 7
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/lmnr-ai/lmnr/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/lmnr-ai/lmnr/releases
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/lmnr-ai/lmnr/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/lmnr-ai/lmnr/blob/main/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/laminar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://laminar.sh/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://laminar.sh/docs
- group: docs
  title: ''
  type: Documentation
  url: https://laminar.sh/docs
- group: docs
  title: ''
  type: APIReference
  url: https://laminar.sh/docs/sdk/client
- group: start
  title: ''
  type: GettingStarted
  url: https://laminar.sh/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/nNFUUDAKub
- group: company
  title: ''
  type: Blog
  url: https://laminar.sh/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/lmnr-ai
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/lmnr-ai/lmnr
- group: commercial
  title: ''
  type: Pricing
  url: https://laminar.sh/pricing
- group: start
  title: ''
  type: SignUp
  url: https://laminar.sh/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://laminar.sh/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://laminar.sh/policies/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.laminar.sh
- group: other
  title: ''
  type: SelfHosted
  url: https://laminar.sh/docs/self-hosting/overview
- group: build
  title: ''
  type: Packages
  url: packages/laminar-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/laminar-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/laminar-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/laminar-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/laminar-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/laminar-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/laminar-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/laminar-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/laminar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/laminar-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/laminar-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/laminar-plans.yml
created: '2026-07-17'
description: 'Laminar is an open-source, OpenTelemetry-native observability and debugging platform built for AI agents and LLM applications. It traces every LLM call, tool call, and sub-agent a run produces, renders each trace as a readable transcript rather than a raw span tree, and turns that data into answers: a record-and-replay Debugger that serves everything before your change from cache so each iteration takes seconds, and Signals that let you describe outcomes and failures in plain language and extract structured events across all traces for clustering and alerting. The platform adds evaluations, datasets and labeling queues, a playground, full-text search, custom dashboards, and read-only ClickHouse SQL over trace data from the UI, the lmnr-cli, or a hosted MCP server. Laminar ships TypeScript and Python SDKs with auto-instrumentation for the Vercel AI SDK, Claude Agent SDK, OpenAI Agents SDK, LangChain/LangGraph, Pydantic AI, Browser Use, Playwright and more, and can run as managed
  Laminar Cloud or fully self-hosted via Docker Compose or Kubernetes/Helm.'
image: https://laminar.sh/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Laminar MCP Server
  slug: laminar-mcp-server
modified: '2026-07-19'
name: Laminar
nav: Providers
network: true
overview: 'Laminar publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Observability, LLM, AI Agents, Tracing, and OpenTelemetry.


  Laminar''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Laminar Plans
  plan_count: 4
  slug: laminar-plans
random_paper: 5
score:
  band: developing
  composite: 45.3
  coverage:
    artifact_dirs: 15
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 26.3
  open_source:
    applies: true
    score: 50.0
  previous_composite: 44.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/laminar/refs/heads/main/screenshots/laminar-2026-07-25T224445.png
security:
- kind: authentication
  name: Laminar Authentication
  slug: laminar-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Laminar Domain Security
  slug: laminar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: laminar
tags:
- Observability
- LLM
- AI Agents
- Tracing
- OpenTelemetry
- Evaluations
- Monitoring
- Developer Tools
- Open-Source
website: https://laminar.sh/
---
