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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/vercel/
- group: company
  title: ''
  type: Website
  url: https://www.geldata.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.geldata.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.geldata.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.geldata.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.geldata.com/learn/quickstart
- group: company
  title: ''
  type: Blog
  url: https://www.geldata.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/geldata
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/gel
- group: commercial
  title: ''
  type: Pricing
  url: https://www.geldata.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://cloud.geldata.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.geldata.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.geldata.com/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.geldata.com/changelog
- group: design
  title: ''
  type: Webhooks
  url: https://docs.geldata.com/reference/auth/webhooks
- group: build
  title: ''
  type: Packages
  url: packages/gel-data-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/gel-data-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/gel-data-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/gel-data-cli.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gel-data-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/gel-data-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/gel-data-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/gel-data-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/gel-data-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gel-data-domain-security.yml
created: '2026-07-17'
description: Gel Data (formerly EdgeDB Inc.) builds Gel, an open-source graph-relational database that supercharges PostgreSQL with a modern object-oriented data model, the EdgeQL query language (with full SQL and GraphQL support), a built-in migration and branching system, integrated authentication (OAuth, email/password, magic links, passkeys/WebAuthn), and GenAI features (automatic embeddings, RAG, and vector search). It ships official client libraries for TypeScript/JavaScript, Python, Go, Rust, .NET, Dart, and Elixir, a first-party CLI, a built-in admin UI, an EdgeQL-over-HTTP and GraphQL endpoint, an Auth HTTP API with webhooks, and an official MCP server for AI coding agents. In late 2025 the company was acquired by Vercel and the managed Gel Cloud is being wound down, but the database remains fully open source under the geldata GitHub organization.
image: https://avatars.githubusercontent.com/u/14262913?v=4
layout: provider
mcp_servers:
- description: Official Model Context Protocol server that gives AI coding agents access to a Gel database. Also installs Gel rules files, the TypeScript query builder, and the Python query builder/ORM into the curr
  name: Gel Data MCP Server
  slug: gel-data-mcp-server
modified: '2026-07-19'
name: Gel Data
nav: Providers
network: true
overview: 'Gel Data is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Open-Source, Database, PostgreSQL, and Graph Database.


  Gel Data''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 18 more developer resources.'
random_paper: 11
score:
  band: thin
  composite: 31.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 31.9
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gel-data/refs/heads/main/screenshots/gel-data-2026-07-25T215722.png
security:
- kind: authentication
  name: Gel Data Authentication
  slug: gel-data-authentication
  summary_line: http/oauth2/webauthn/magic-link/apiKey · 7 schemes
- kind: domain-security
  name: Gel Data Domain Security
  slug: gel-data-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gel-data
tags:
- Company
- Open-Source
- Database
- PostgreSQL
- Graph Database
- GraphQL
- Authentication
- Artificial Intelligence
- Vector Database
- Developer Tools
website: https://www.geldata.com/
---
