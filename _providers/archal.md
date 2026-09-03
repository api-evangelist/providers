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
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: Archal Agentic Access
  operation_count: 16
  slug: archal-agentic-access
  summary_line: 16 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://archal.ai
  baseurl_source: declared
  description: CLI and device authentication.
  name: Archal Auth API
  slug: archal-auth-api
- baseURL: https://archal.ai
  baseurl_source: declared
  description: Clone and scenario discovery.
  name: Archal Catalog API
  slug: archal-catalog-api
- baseURL: https://archal.ai
  baseurl_source: declared
  description: Run, trace, and test-result reporting.
  name: Archal Results API
  slug: archal-results-api
- baseURL: https://archal.ai
  baseurl_source: declared
  description: Direct calls into a running clone.
  name: Archal Runtime API
  slug: archal-runtime-api
- baseURL: https://archal.ai
  baseurl_source: declared
  description: Hosted clone session lifecycle.
  name: Archal Sessions API
  slug: archal-sessions-api
arazzos:
- description: Provision a hosted clone session, POST a request into the cloned service through the runtime proxy, read the resulting trace, then stop the session.
  name: Create an Archal clone session, drive it, and read the trace
  slug: archal-create-and-evaluate
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Archal Auth API
  slug: open-archal-auth-api
- collection_type: open
  name: Archal Auth Catalog API
  slug: open-archal-catalog-api
- collection_type: open
  name: Archal Auth Results API
  slug: open-archal-results-api
- collection_type: open
  name: Archal Auth Runtime API
  slug: open-archal-runtime-api
- collection_type: open
  name: Archal Auth Sessions API
  slug: open-archal-sessions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/archal-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archal-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archal-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.archal.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.archal.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.archal.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.archal.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Archal-Labs
- group: build
  title: ''
  type: Packages
  url: packages/archal-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/archal-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/archal-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/archal-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/archal-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/archal-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/archal-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/archal-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archal-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/archal-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archal-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/archal-openapi-overlay.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/archal-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/archal-create-and-evaluate.yml
created: '2026-07-17'
description: Archal is a Y Combinator (S26) company building QA and an improvement loop for AI agents. It provisions hosted, service-shaped CLONES of real SaaS services — GitHub, Slack, Stripe, Jira, Linear, Supabase, Ramp, HubSpot, Datadog, Discord, Google Workspace and more — so an agent that can send emails, change code repositories, or call third-party APIs is tested and scored before it touches production. Clones hold state, enforce referential integrity, and return authentic error shapes, unlike traditional mocks. Its Autoloop turns real production agent traces into reproducible failures and can open a fix PR. Archal ships an npm CLI and Vitest SDK, a device-auth login, a runtime clone proxy, and per-session MCP endpoints.
image: https://docs.archal.ai/logo/dark.svg
layout: provider
mcp_servers:
- description: ''
  name: Archal MCP Server
  slug: archal-mcp-server
modified: '2026-07-18'
name: Archal
nav: Providers
network: true
overview: 'Archal publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Catalog API, Results API, and 2 more. Tagged areas include Company, AI Agents, Agent Testing, Developer Tools, and API Testing.


  Archal''s developer surface includes authentication, documentation, API reference, getting-started guide, CLI, sandbox, and 17 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 35.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 51.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 35.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archal/refs/heads/main/screenshots/archal-2026-07-25T201020.png
security:
- kind: authentication
  name: Archal Authentication
  slug: archal-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Archal Domain Security
  slug: archal-domain-security
  summary_line: TLSv1.3 · DMARC
slug: archal
tags:
- Company
- AI Agents
- Agent Testing
- Developer Tools
- API Testing
- Sandbox
- Evaluation
- Infrastructure
website: https://docs.archal.ai
---
