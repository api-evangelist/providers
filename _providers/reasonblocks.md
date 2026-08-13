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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Reasonblocks Agentic Access
  operation_count: 32
  slug: reasonblocks-agentic-access
  summary_line: 32 operations · 18 acting
api_count: 9
apis:
- description: The Billing API from ReasonBlocks — 1 operation(s) for billing.
  name: ReasonBlocks Billing API
  slug: reasonblocks-billing-api
- description: The Codebase Findings API from ReasonBlocks — 5 operation(s) for codebase findings.
  name: ReasonBlocks Codebase Findings API
  slug: reasonblocks-codebase-findings-api
- description: The Health API from ReasonBlocks — 1 operation(s) for health.
  name: ReasonBlocks Health API
  slug: reasonblocks-health-api
- description: The monitor API from ReasonBlocks — 11 operation(s) for monitor.
  name: ReasonBlocks monitor API
  slug: reasonblocks-monitor-api
- description: The Monitor Telemetry API from ReasonBlocks — 11 operation(s) for monitor telemetry.
  name: ReasonBlocks Monitor Telemetry API
  slug: reasonblocks-monitor-telemetry-api
- description: The Monitors API from ReasonBlocks — 1 operation(s) for monitors.
  name: ReasonBlocks Monitors API
  slug: reasonblocks-monitors-api
- description: The Pattern Library API from ReasonBlocks — 2 operation(s) for pattern library.
  name: ReasonBlocks Pattern Library API
  slug: reasonblocks-pattern-library-api
- description: The Patterns & Traces API from ReasonBlocks — 2 operation(s) for patterns & traces.
  name: ReasonBlocks Patterns & Traces API
  slug: reasonblocks-patterns-traces-api
- description: The Scoring API from ReasonBlocks — 1 operation(s) for scoring.
  name: ReasonBlocks Scoring API
  slug: reasonblocks-scoring-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.reasonblocks.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.reasonblocks.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://rb-api.reasonblocks.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.reasonblocks.com/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ReasonBlocks
- group: company
  title: ''
  type: Website
  url: https://reasonblocks.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/reasonblocks-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/reasonblocks-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/reasonblocks-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/reasonblocks-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/reasonblocks-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/reasonblocks-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/reasonblocks-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/reasonblocks-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/reasonblocks-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.reasonblocks.com/api-reference/rest-api/versioning
- group: design
  title: ''
  type: Conventions
  url: conventions/reasonblocks-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/reasonblocks-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/reasonblocks-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/reasonblocks-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/reasonblocks-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: ReasonBlocks is a Y Combinator (Spring 2026) startup building a drop-in runtime layer that makes production AI agents observable, self-correcting, and cheaper to run. The platform detects failing agent trajectories (loops and redundant work), compresses stale tool outputs and message histories to cut token spend, and builds a private learning library of reasoning patterns (E-traces) that steer future runs. It ships as a Python SDK with first-party integrations for LangChain, LangGraph, the OpenAI Agents SDK, and the Anthropic Claude / Claude Agent SDK, plus a language-agnostic REST API (rb-api) so any custom agent harness can wire in over three HTTP calls. Reported results include a 42% accuracy gain and ~52% token reduction on SWE-bench Pro.
image: https://reasonblocks.com/rb.png
layout: provider
mcp_servers:
- description: ''
  name: reasonblocks-mcp.yml
  slug: reasonblocks-mcpyml
modified: '2026-07-21'
name: ReasonBlocks
nav: Providers
network: true
overview: 'ReasonBlocks publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Codebase Findings API, Health API, and 6 more. Tagged areas include Company, AI Agents, Agent Observability, LLM, and Developer Tools.


  ReasonBlocks'' developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 17 more developer resources.'
random_paper: 86
score:
  band: thin
  composite: 36.3
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 50.2
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 13.2
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Reasonblocks Authentication
  slug: reasonblocks-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Reasonblocks Domain Security
  slug: reasonblocks-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: reasonblocks
tags:
- Company
- AI Agents
- Agent Observability
- LLM
- Developer Tools
- Token Optimization
- Agent Steering
- Machine Learning
- Artificial Intelligence
- SDK
website: https://reasonblocks.com
---
