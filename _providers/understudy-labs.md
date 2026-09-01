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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 10
  human_in_the_loop: 1
  name: Understudy Labs Agentic Access
  operation_count: 20
  slug: understudy-labs-agentic-access
  summary_line: 20 operations · 10 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Anthropic- and OpenAI-compatible LLM proxy at api.understudylabs.com. POST /v1/messages (Anthropic Messages), POST /v1/chat/completions (OpenAI Chat Completions), POST /v1/messages/count_tokens, GET /
  name: Understudy Gateway API
  slug: understudy-gateway-api
- description: REST surface behind the dashboard and CLI, served from the gateway host under /admin/v1 and /customer/v1, org-scoped and authenticated with sk_* bearer keys. Covers API key mint/list/revoke, project C
  name: Understudy Control Plane API
  slug: understudy-control-plane-api
- description: The Capabilities API from Understudy Labs — 1 operation(s) for capabilities.
  name: Understudy Labs Capabilities API
  slug: understudy-labs-capabilities-api
- description: The Conversations API from Understudy Labs — 1 operation(s) for conversations.
  name: Understudy Labs Conversations API
  slug: understudy-labs-conversations-api
- description: The Downloads API from Understudy Labs — 3 operation(s) for downloads.
  name: Understudy Labs Downloads API
  slug: understudy-labs-downloads-api
- description: The Feedback API from Understudy Labs — 1 operation(s) for feedback.
  name: Understudy Labs Feedback API
  slug: understudy-labs-feedback-api
- description: The Metrics API from Understudy Labs — 1 operation(s) for metrics.
  name: Understudy Labs Metrics API
  slug: understudy-labs-metrics-api
- description: The Models API from Understudy Labs — 2 operation(s) for models.
  name: Understudy Labs Models API
  slug: understudy-labs-models-api
- description: The Residency API from Understudy Labs — 6 operation(s) for residency.
  name: Understudy Labs Residency API
  slug: understudy-labs-residency-api
- description: The Runs API from Understudy Labs — 2 operation(s) for runs.
  name: Understudy Labs Runs API
  slug: understudy-labs-runs-api
- description: The Status API from Understudy Labs — 1 operation(s) for status.
  name: Understudy Labs Status API
  slug: understudy-labs-status-api
- description: The Supervision API from Understudy Labs — 1 operation(s) for supervision.
  name: Understudy Labs Supervision API
  slug: understudy-labs-supervision-api
arazzos:
- description: 'The core Understudy Desktop journey over the loopback Agent API - pick a model from the catalog, start and track its download, add a residency slot, assign and warm the model in the slot, then send a '
  name: Download, warm, and chat with a local model on Understudy Desktop
  slug: understudy-labs-download-warm-and-chat
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Understudy Desktop Agent Capabilities API
  slug: open-understudy-labs-capabilities-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Conversations API
  slug: open-understudy-labs-conversations-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Downloads API
  slug: open-understudy-labs-downloads-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Feedback API
  slug: open-understudy-labs-feedback-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Metrics API
  slug: open-understudy-labs-metrics-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Models API
  slug: open-understudy-labs-models-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Residency API
  slug: open-understudy-labs-residency-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Runs API
  slug: open-understudy-labs-runs-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Status API
  slug: open-understudy-labs-status-api
- collection_type: open
  name: Understudy Desktop Agent Capabilities Supervision API
  slug: open-understudy-labs-supervision-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/understudy-labs-desktop-api-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/understudy-labs-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/understudy-labs-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/understudy-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://understudylabs.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.understudylabs.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.understudylabs.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.understudylabs.com/reference/proxy-endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.understudylabs.com/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.understudylabs.com
- group: operate
  title: ''
  type: Support
  url: https://understudylabs.com/contact
- group: company
  title: ''
  type: Blog
  url: https://understudylabs.com/research
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/understudylabs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://understudylabs.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://understudylabs.com/privacy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/understudy-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/understudy-labs-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/understudy-labs-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/understudy-labs-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/understudy-labs-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/understudy-labs-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/understudy-labs-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/understudy-labs-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/understudy-labs-cli.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/understudy-labs-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/understudy-labs-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/understudy-labs-download-warm-and-chat.yml
created: '2026-07-17'
description: Understudy Labs (YC S26) is an LLM gateway and model-optimization platform that helps teams move repeated production LLM workloads onto open-weight models they own. The Understudy gateway is a drop-in replacement for the Anthropic and OpenAI API endpoints that captures request/response traces by project and workload, routes measured slices of traffic to managed open models, and falls back safely. A REST control plane manages keys, projects, workloads, routing, captures, evaluation cohorts, and reporting, while the MIT-licensed understudy-agent-tools repo ships a CLI, a coding-agent skill library, a local MCP server, and Understudy Desktop with a documented loopback OpenAPI 3.1 contract.
image: https://bookface-images.s3.amazonaws.com/small_logos/034b1bab6d92bd99439aee47bf2312630046798c.png
layout: provider
mcp_servers:
- description: ''
  name: Understudy Labs MCP Server
  slug: understudy-labs-mcp-server
modified: '2026-07-21'
name: Understudy Labs
nav: Providers
network: true
overview: 'Understudy Labs publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Capabilities API, Conversations API, Downloads API, and 7 more. Tagged areas include Artificial Intelligence, LLM Gateway, Machine-Learning, Open-Source, and Model Routing.


  Understudy Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, CLI, and 21 more developer resources.'
random_paper: 20
score:
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 47.8
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 43.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/understudy-labs/refs/heads/main/screenshots/understudy-labs-2026-08-17T082556.png
security:
- kind: authentication
  name: Understudy Labs Authentication
  slug: understudy-labs-authentication
  summary_line: apiKey/http · 5 schemes
- kind: domain-security
  name: Understudy Labs Domain Security
  slug: understudy-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: understudy-labs
tags:
- Artificial Intelligence
- LLM Gateway
- Machine-Learning
- Open-Source
- Model Routing
- Evaluations
- Fine-Tuning
- AI Infrastructure
- Developer Tools
website: https://understudylabs.com
---
