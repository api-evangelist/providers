---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.6
  scored_at: '2026-11-06'
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
  name: Airweave Collections API
  slug: airweave-collections-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The collections > search API from Airweave — 4 operation(s) for collections > search.
  name: Airweave collections > search API
  slug: airweave-collections-search-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The source-connections API from Airweave — 5 operation(s) for source-connections.
  name: Airweave Source Connections API
  slug: airweave-source-connections-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The sources API from Airweave — 2 operation(s) for sources.
  name: Airweave Sources API
  slug: airweave-sources-api
- baseURL: https://api.airweave.ai
  baseurl_source: declared
  description: The webhooks API from Airweave — 5 operation(s) for webhooks.
  name: Airweave Webhooks API
  slug: airweave-webhooks-api
artifact_total: 22
asyncapis:
- description: ''
  name: Airweave Webhooks
  slug: airweave-webhooks
collections:
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
- group: commercial
  href: https://artifacts.apis.io/airweave/plans/airweave-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/airweave-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/airweave/capabilities/airweave-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/airweave-capability-edges.yml
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
  href: https://artifacts.apis.io/airweave/llms/airweave-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/airweave-llms.txt
- group: build
  href: https://artifacts.apis.io/airweave/packages/airweave-packages.yml
  title: ''
  type: Packages
  url: packages/airweave-packages.yml
- group: build
  href: https://artifacts.apis.io/airweave/packages/airweave-packages.yml
  title: ''
  type: SDKs
  url: packages/airweave-packages.yml
- group: build
  href: https://artifacts.apis.io/airweave/cli/airweave-cli.yml
  title: ''
  type: CLI
  url: cli/airweave-cli.yml
- group: agent
  href: https://artifacts.apis.io/airweave/mcp/airweave-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/airweave-mcp.yml
- group: agent
  href: https://artifacts.apis.io/airweave/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/airweave/well-known/airweave-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/airweave-well-known.yml
- group: design
  href: https://artifacts.apis.io/airweave/asyncapi/airweave-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/airweave-webhooks.yml
- group: design
  href: https://artifacts.apis.io/airweave/conventions/airweave-conventions.yml
  title: ''
  type: Conventions
  url: conventions/airweave-conventions.yml
- group: design
  href: https://artifacts.apis.io/airweave/errors/airweave-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/airweave-problem-types.yml
- group: design
  href: https://artifacts.apis.io/airweave/lifecycle/airweave-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/airweave-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/airweave/rate-limits/airweave-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/airweave-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/airweave/conformance/airweave-conformance.yml
  title: ''
  type: Conformance
  url: conformance/airweave-conformance.yml
- group: design
  href: https://artifacts.apis.io/airweave/data-model/airweave-data-model.yml
  title: ''
  type: DataModel
  url: data-model/airweave-data-model.yml
- group: design
  href: https://artifacts.apis.io/airweave/components/airweave-components.yml
  title: ''
  type: Components
  url: components/airweave-components.yml
- group: other
  href: https://artifacts.apis.io/airweave/overlays/airweave-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/airweave-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/airweave/agentic-access/airweave-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/airweave-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/airweave/security/airweave-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/airweave-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/airweave/authentication/airweave-authentication.yml
  title: ''
  type: Authentication
  url: authentication/airweave-authentication.yml
created: '2026-07-17'
description: Airweave is an open-source (MIT) context-retrieval layer that lets AI agents and RAG pipelines search across 50+ connected apps and databases through a single API. It syncs data from sources like Slack, Notion, GitHub, Google Drive, and Postgres, then exposes instant (sub-second vector), classic (LLM-planned), and agentic (multi-step) search over unified collections. Query it via the REST API, official Python and TypeScript SDKs, a CLI, an embeddable Connect UI widget, or a hosted Model Context Protocol (MCP) server, with real-time Svix-backed webhooks for sync and source-connection lifecycle events.
finops:
- has_sources: true
  method: derived
  name: Airweave Finops
  primary_unit: subscription
  service_category: ''
  slug: airweave-finops
  template: false
image: https://github.com/airweave-ai.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.airweave.ai over HTTP; 2 tools listed.
  name: Airweave MCP Server
  slug: airweave
modified: '2026-07-17'
name: Airweave
nav: Providers
network: true
overview: 'Airweave publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Collections API, collections > search API, Source Connections API, and 2 more. Tagged areas include Company, Artificial Intelligence, Search, RAG, and Retrieval.


  The Airweave catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Airweave''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, pricing, and 26 more developer resources.'
plans:
- name: Airweave Plans Pricing
  plan_count: 4
  slug: airweave-plans-pricing
- name: Airweave Price Estimates
  plan_count: 0
  slug: airweave-price-estimates
random_paper: 12
rate_limits:
- limit_count: 3
  name: Airweave Rate Limits
  slug: airweave-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: Airweave API Rules
  rule_count: 53
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 7
  slug: airweave-rules
score:
  band: strong
  composite: 59.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 63.1
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 42.1
  previous_composite: 57.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 5
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/airweave/airweave-2026-07-25T195446.png
security:
- kind: authentication
  name: Airweave Authentication
  slug: airweave-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Airweave Domain Security
  slug: airweave-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: Search an Airweave collection
  slug: airweave-search
- name: Set up a collection and connect a source
  slug: airweave-setup
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
