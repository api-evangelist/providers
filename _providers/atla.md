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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://app.atla-ai.com
  baseurl_source: declared
  description: The SDK API from Atla — 3 operation(s) for sdk.
  name: Atla SDK API
  slug: atla-sdk-api
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Atla Insights SDK API
  slug: open-atla-sdk-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/atla-insights-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.atla-ai.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.atla-ai.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.atla-ai.com/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.atla-ai.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.atla-ai.com/troubleshooting-faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atla-ai
- group: company
  title: ''
  type: Website
  url: https://www.atla-ai.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/atla-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atla-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/atla-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/atla-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atla-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atla-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/atla-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atla-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atla-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atla-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atla-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atla-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Atla builds frontier AI evaluation models (Selene) and Atla Insights, an observability platform for monitoring and improving AI agents. Its Insights Data API exposes OpenTelemetry-based traces and spans of instrumented agent runs — list with time-window and metadata filters, fetch multiple by ID, and retrieve a single trace with full spans, summaries, and custom metrics. Atla ships official Python and JavaScript SDKs and an MCP server. The company is UK-based and backed by Creandum. Note: the Atla Insights platform is scheduled to sunset on 16 February 2026, and the separate Selene evaluation API SDK and MCP server were archived in 2025.'
image: https://avatars.githubusercontent.com/atla-ai
layout: provider
mcp_servers:
- description: Official MCP server providing a standardized interface for LLMs to interact with the Atla API (Selene evaluation). Repository archived by the provider.
  name: Atla MCP Server
  slug: atla-mcp-server
modified: '2026-07-18'
name: Atla
nav: Providers
network: true
overview: 'Atla publishes 1 API on the [APIs.io](https://apis.io/) network: SDK API. Tagged areas include Company, Software-as-a-Service, Artificial Intelligence, LLM Evaluation, and AI Agents.


  Atla''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 16 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 34.8
  coverage:
    artifact_dirs: 16
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
    contract_quality: 54.4
    developer_ergonomics: 63.7
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 34.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/atla/refs/heads/main/screenshots/atla-2026-07-25T201538.png
security:
- kind: authentication
  name: Atla Authentication
  slug: atla-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Atla Domain Security
  slug: atla-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: atla
tags:
- Company
- Software-as-a-Service
- Artificial Intelligence
- LLM Evaluation
- AI Agents
- Observability
- Monitoring
- OpenTelemetry
website: https://www.atla-ai.com/
---
