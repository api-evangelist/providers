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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.3
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: 'The Definite REST API for programmatic access to the Definite data platform: stream JSON ingestion into DuckLake, signed-URL file uploads to Definite Drive, webhook-triggered Python pipelines, push-ba'
  name: Definite API
  slug: definite-api
artifact_total: 7
asyncapis:
- description: ''
  name: Definite Webhooks
  slug: definite-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/definite-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/definite-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.definite.app/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.definite.app/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.definite.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.definite.app/docs/definite-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.definite.app/docs/getting-started
- group: company
  title: ''
  type: Blog
  url: https://www.definite.app/blog
- group: operate
  title: ''
  type: Support
  url: https://www.definite.app/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.definite.app/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.definite.app/signup
- group: start
  title: ''
  type: Login
  url: https://www.definite.app/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.definite.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.definite.app/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/definite-app
- group: operate
  title: ''
  type: StatusPage
  url: https://status.definite.app
- group: auth
  title: ''
  type: Compliance
  url: https://www.definite.app/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/definite-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/definite-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/definite-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/definite-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/definite-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/definite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/definite-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/definite-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/definite-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/definite-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/definite-conformance.yml
- group: design
  title: ''
  type: Components
  url: components/definite-components.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/definite-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Definite is an all-in-one, AI-native data platform that consolidates data integration, warehouse storage, a semantic layer, BI dashboards, and AI agents into a single product. It ships 500+ managed data connectors, a DuckDB / DuckLake lakehouse, a Cube-based semantic layer, and Fi, a natural-language AI data analyst that builds complete data apps rather than just dashboards. Definite speaks the Model Context Protocol natively, exposing 40+ tools across six categories so Claude, Cursor, or any agent can query data, manage syncs, update semantic models, and build dashboards directly. The whole stack is self-hostable into a customer's own cloud account (BYOC) or on-prem, including the AI analyst, so data never leaves the environment. Its REST API supports stream ingestion into DuckLake, signed-URL file uploads, webhook-triggered Python pipelines, and embedding of Docs and data apps in external web apps.
image: https://www.definite.app/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Definite MCP Server
  slug: definite-mcp-server
modified: '2026-07-18'
name: Definite
nav: Providers
network: true
overview: 'Definite publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, Analytics, Business Intelligence, and Data Integration.


  The Definite catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Definite''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
random_paper: 0
scopes:
- name: Definite Scopes
  scope_count: 1
  slug: definite-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 50.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 78.6
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 49.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/definite/refs/heads/main/screenshots/definite-2026-07-25T211622.png
security:
- kind: authentication
  name: Definite Authentication
  slug: definite-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Definite Domain Security
  slug: definite-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Definite Trust Center
  slug: definite-trust-center
  summary_line: SOC 2
slug: definite
tags:
- Company
- Data
- Analytics
- Business Intelligence
- Data Integration
- Data Warehouse
- Lakehouse
- Semantic Layer
- Artificial Intelligence
- AI Agents
- MCP
- ETL
website: https://www.definite.app/
---
