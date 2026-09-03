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
  band_gated_from: agent-native
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.0
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Airweave Agentic Access
  operation_count: 27
  slug: airweave-agentic-access
  summary_line: 27 operations · 16 acting
api_count: 1
apis:
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The collections API from Airweave — 2 operation(s) for collections.
  name: Airweave collections API
  slug: airweave-collections-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The collections > search API from Airweave — 4 operation(s) for collections > search.
  name: Airweave collections > search API
  slug: airweave-collections-search-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The source-connections API from Airweave — 5 operation(s) for source-connections.
  name: Airweave source-connections API
  slug: airweave-source-connections-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The sources API from Airweave — 2 operation(s) for sources.
  name: Airweave sources API
  slug: airweave-sources-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The webhooks API from Airweave — 5 operation(s) for webhooks.
  name: Airweave webhooks API
  slug: airweave-webhooks-api
artifact_total: 17
asyncapis:
- description: ''
  name: Airweave Webhooks
  slug: airweave-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: API Reference collections API
  slug: open-airweave-collections-api
- collection_type: open
  name: API Reference collections collections > search API
  slug: open-airweave-collections-search-api
- collection_type: open
  name: API Reference collections source-connections API
  slug: open-airweave-source-connections-api
- collection_type: open
  name: API Reference collections sources API
  slug: open-airweave-sources-api
- collection_type: open
  name: API Reference collections webhooks API
  slug: open-airweave-webhooks-api
common:
- group: company
  title: ''
  type: Website
  url: https://airweave.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.airweave.ai/welcome
- group: docs
  title: ''
  type: Documentation
  url: https://docs.airweave.ai/welcome
- group: docs
  title: ''
  type: APIReference
  url: https://docs.airweave.ai/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.airweave.ai/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/airweave-ai
- group: company
  title: ''
  type: Blog
  url: https://airweave.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://airweave.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.airweave.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://airweave.ai/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airweave.ai/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airweave.ai/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/airweave-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/airweave-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/airweave-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/airweave-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/airweave-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/airweave-well-known.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/airweave-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/airweave-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/airweave-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/airweave-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/airweave-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/airweave-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/airweave-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/airweave-components.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/airweave-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/airweave-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airweave-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/airweave-authentication.yml
created: '2026-07-17'
description: Airweave is an open-source (MIT) context-retrieval layer that lets AI agents and RAG pipelines search across 50+ connected apps and databases through a single API. It syncs data from sources like Slack, Notion, GitHub, Google Drive, and Postgres, then exposes instant (sub-second vector), classic (LLM-planned), and agentic (multi-step) search over unified collections. Query it via the REST API, official Python and TypeScript SDKs, a CLI, an embeddable Connect UI widget, or a hosted Model Context Protocol (MCP) server, with real-time Svix-backed webhooks for sync and source-connection lifecycle events.
image: https://github.com/airweave-ai.png
layout: provider
mcp_servers:
- description: ''
  name: Airweave MCP Server
  slug: airweave-mcp-server
modified: '2026-07-17'
name: Airweave
nav: Providers
network: true
overview: 'Airweave publishes 5 APIs on the [APIs.io](https://apis.io/) network, including collections API, collections > search API, source-connections API, and 2 more. Tagged areas include Company, Artificial Intelligence, Search, RAG, and Retrieval.


  The Airweave catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Airweave''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 24 more developer resources.'
random_paper: 12
rate_limits:
- limit_count: 3
  name: Airweave Rate Limits
  slug: airweave-rate-limits
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 24
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 4.5
    contract_quality: 63.1
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 49.3
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airweave/refs/heads/main/screenshots/airweave-2026-07-25T195446.png
security:
- kind: authentication
  name: Airweave Authentication
  slug: airweave-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airweave Domain Security
  slug: airweave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: airweave
tags:
- Company
- Artificial Intelligence
- Search
- RAG
- Retrieval
- Agents
- MCP
- Vector Search
- Data Integration
- Context
website: https://airweave.ai
---
