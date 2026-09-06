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
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.9
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Reasonblocks Agentic Access
  operation_count: 32
  slug: reasonblocks-agentic-access
  summary_line: 32 operations · 18 acting
api_count: 1
apis:
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Billing API from ReasonBlocks — 1 operation(s) for billing.
  name: ReasonBlocks Billing API
  slug: reasonblocks-billing-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Codebase Findings API from ReasonBlocks — 5 operation(s) for codebase findings.
  name: ReasonBlocks Codebase Findings API
  slug: reasonblocks-codebase-findings-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Health API from ReasonBlocks — 1 operation(s) for health.
  name: ReasonBlocks Health API
  slug: reasonblocks-health-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The monitor API from ReasonBlocks — 11 operation(s) for monitor.
  name: ReasonBlocks monitor API
  slug: reasonblocks-monitor-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Monitor Telemetry API from ReasonBlocks — 11 operation(s) for monitor telemetry.
  name: ReasonBlocks Monitor Telemetry API
  slug: reasonblocks-monitor-telemetry-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Monitors API from ReasonBlocks — 1 operation(s) for monitors.
  name: ReasonBlocks Monitors API
  slug: reasonblocks-monitors-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Pattern Library API from ReasonBlocks — 2 operation(s) for pattern library.
  name: ReasonBlocks Pattern Library API
  slug: reasonblocks-pattern-library-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Patterns & Traces API from ReasonBlocks — 2 operation(s) for patterns & traces.
  name: ReasonBlocks Patterns & Traces API
  slug: reasonblocks-patterns-traces-api
- baseURL: https://rb-api.reasonblocks.com
  baseurl_source: declared
  description: The Scoring API from ReasonBlocks — 1 operation(s) for scoring.
  name: ReasonBlocks Scoring API
  slug: reasonblocks-scoring-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ReasonBlocks Billing API
  slug: open-reasonblocks-billing-api
- collection_type: open
  name: ReasonBlocks Billing Codebase Findings API
  slug: open-reasonblocks-codebase-findings-api
- collection_type: open
  name: ReasonBlocks Billing Health API
  slug: open-reasonblocks-health-api
- collection_type: open
  name: ReasonBlocks Billing monitor API
  slug: open-reasonblocks-monitor-api
- collection_type: open
  name: ReasonBlocks Billing Monitor Telemetry API
  slug: open-reasonblocks-monitor-telemetry-api
- collection_type: open
  name: ReasonBlocks Billing Monitors API
  slug: open-reasonblocks-monitors-api
- collection_type: open
  name: ReasonBlocks Billing Pattern Library API
  slug: open-reasonblocks-pattern-library-api
- collection_type: open
  name: ReasonBlocks Billing Patterns & Traces API
  slug: open-reasonblocks-patterns-traces-api
- collection_type: open
  name: ReasonBlocks Billing Scoring API
  slug: open-reasonblocks-scoring-api
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: ReasonBlocks
nav: Providers
network: true
overview: 'ReasonBlocks publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Billing API, Codebase Findings API, Health API, and 6 more. Tagged areas include Company, AI Agents, Agent Observability, LLM, and Developer Tools.


  ReasonBlocks'' developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, and 17 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 54.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 10.5
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/reasonblocks/refs/heads/main/screenshots/reasonblocks-2026-09-02T153021.png
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
- Machine-Learning
- Artificial Intelligence
- SDK
website: https://reasonblocks.com
---
