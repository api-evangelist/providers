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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 15
  human_in_the_loop: 1
  name: Ondemand Agentic Access
  operation_count: 22
  slug: ondemand-agentic-access
  summary_line: 22 operations · 15 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The Chat API from Ondemand — 7 operation(s) for chat.
  name: Ondemand Chat API
  slug: ondemand-chat-api
- description: The Config API from Ondemand — 2 operation(s) for config.
  name: Ondemand Config API
  slug: ondemand-config-api
- description: The Execute API from Ondemand — 3 operation(s) for execute.
  name: Ondemand Execute API
  slug: ondemand-execute-api
- description: The Media API from Ondemand — 2 operation(s) for media.
  name: Ondemand Media API
  slug: ondemand-media-api
- description: The User API from Ondemand — 2 operation(s) for user.
  name: Ondemand User API
  slug: ondemand-user-api
- description: The Workflow API from Ondemand — 2 operation(s) for workflow.
  name: Ondemand Workflow API
  slug: ondemand-workflow-api
artifact_total: 19
asyncapis:
- description: ''
  name: Ondemand Webhooks
  slug: ondemand-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OnDemand AI Chat API
  slug: open-ondemand-chat-api
- collection_type: open
  name: OnDemand AI Chat Config API
  slug: open-ondemand-config-api
- collection_type: open
  name: OnDemand AI Chat Execute API
  slug: open-ondemand-execute-api
- collection_type: open
  name: OnDemand AI Chat Media API
  slug: open-ondemand-media-api
- collection_type: open
  name: OnDemand AI Chat User API
  slug: open-ondemand-user-api
- collection_type: open
  name: OnDemand AI Chat Workflow API
  slug: open-ondemand-workflow-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ondemand-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ondemand-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.on-demand.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.on-demand.io/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.on-demand.io/reference/intro-to-ondemand-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.on-demand.io/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://app.on-demand.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.on-demand.io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/on-demand-io
- group: auth
  title: ''
  type: Authentication
  url: authentication/ondemand-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ondemand-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/ondemand-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ondemand-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ondemand-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/ondemand-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/ondemand-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ondemand-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ondemand-lifecycle.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/ondemand-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ondemand-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ondemand-data-model.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ondemand-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: OnDemand AI (on-demand.io) is a RAG-powered AI Platform-as-a-Service that lets companies infuse AI into their products without managing model infrastructure. The platform exposes a REST API for chat sessions and queries against a library of predefined, BYOI (Bring Your Own Inference) and BYOM (Bring Your Own Model) fulfillment models, media ingestion and vector search, Knowledge / REST-API / IoT(MQTT) agents, an Agents Flow Builder for workflow automation, and cloud services for speech-to-text, text-to-speech and language translation. API access is authenticated with API keys, supports sync / stream / webhook response modes, offset- and cursor-based pagination, and per-object rate limits. Surfaced as a Canaan Partners portfolio lead and enriched from the provider's public developer documentation at docs.on-demand.io.
image: https://files.readme.io/52eb008-favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Ondemand MCP Server
  slug: ondemand-mcp-server
modified: '2026-07-20'
name: Ondemand
nav: Providers
network: true
overview: 'Ondemand publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Config API, Execute API, and 3 more. Tagged areas include Company, Artificial Intelligence, Machine-Learning, RAG, and Agents.


  The Ondemand catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Ondemand''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, authentication, and 17 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 4
  name: Ondemand Rate Limits
  slug: ondemand-rate-limits
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 60.2
    developer_ergonomics: 39.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 36.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ondemand/refs/heads/main/screenshots/ondemand-2026-08-07T190238.png
security:
- kind: authentication
  name: Ondemand Authentication
  slug: ondemand-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Ondemand Domain Security
  slug: ondemand-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ondemand
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- RAG
- Agents
- LLM
- Platform-as-a-Service
- Chat
- Workflow-Automation
- Vector Search
website: https://docs.on-demand.io
---
