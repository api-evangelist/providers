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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 61.5
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: Create, read, update, and delete company records.
  name: Fixture Accounts API
  slug: fixture-accounts-api
- description: List and ingest CRM Activity records.
  name: Fixture Activities API
  slug: fixture-activities-api
- description: Create, read, update, and delete person records.
  name: Fixture Contacts API
  slug: fixture-contacts-api
- description: Create, read, update, and delete Deal records.
  name: Fixture Deals API
  slug: fixture-deals-api
- description: The Fixture API API from Fixture — 1 operation(s) for fixture api.
  name: Fixture Fixture API API
  slug: fixture-fixture-api-api
- description: Create, read, update, and convert Leads.
  name: Fixture Leads API
  slug: fixture-leads-api
- description: Create Notes linked to CRM entities.
  name: Fixture Notes API
  slug: fixture-notes-api
- description: List Pipelines and inspect their nested stages.
  name: Fixture Pipelines API
  slug: fixture-pipelines-api
- description: List Task status definitions available to the current organization.
  name: Fixture Task Statuses API
  slug: fixture-task-statuses-api
- description: Create, read, update, and delete Tasks.
  name: Fixture Tasks API
  slug: fixture-tasks-api
- description: The Users API from Fixture — 1 operation(s) for users.
  name: Fixture Users API
  slug: fixture-users-api
artifact_total: 15
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fixture-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fixture.app
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fixture.app/docs
- group: docs
  title: ''
  type: Documentation
  url: https://fixture.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://fixture.app/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://fixture.app/docs/getting-started/quickstart
- group: start
  title: ''
  type: Login
  url: https://beta.fixture.app
- group: start
  title: ''
  type: SignUp
  url: https://fixture.app/beta
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fixture.app
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fixture.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fixture.app/privacy
- group: operate
  title: ''
  type: RateLimits
  url: https://fixture.app/docs/api-reference/rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://fixture.app/docs/api-reference/errors
- group: design
  title: ''
  type: Idempotency
  url: conventions/fixture-conventions.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/fixture-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/fixture-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/fixture-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fixture-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fixture-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fixture-mcp.yml
- group: build
  title: ''
  type: CLI
  url: cli/fixture-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/fixture-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fixture-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/fixture-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fixture-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fixture-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Fixture is an AI-native CRM built for startups, backed by Y Combinator (Winter 2026 batch). Fixture aggregates every customer interaction — email, calendar, Slack and Slack Connect, meeting notes from Granola, Notion and Circleback, and Stripe billing events — into a single structured activity graph across Accounts, Contacts, Deals, Leads, Tasks and Notes, then uses agents to surface next actions and keep records current without manual data entry. The whole system is programmable — Fixture publishes a documented REST v1 API with a generated OpenAPI 3.1 description, a hosted remote MCP server with OAuth 2.1 and dynamic client registration, and a first-party agent-oriented CLI, so humans and agents work against the same surface.
image: https://fixture.app/logo-for-black.svg
layout: provider
mcp_servers:
- description: ''
  name: fixture-mcp.yml
  slug: fixture-mcpyml
modified: '2026-07-20'
name: Fixture
nav: Providers
network: true
overview: 'Fixture publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Contacts API, and 8 more. Tagged areas include Company, CRM, Sales, B2B, and Artificial Intelligence.


  Fixture''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 21 more developer resources.'
random_paper: 79
scopes:
- name: Fixture Scopes
  scope_count: 0
  slug: fixture-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 65.1
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 15.8
  previous_composite: 48.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fixture/refs/heads/main/screenshots/fixture-2026-07-25T214655.png
security:
- kind: authentication
  name: Fixture Authentication
  slug: fixture-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Fixture Domain Security
  slug: fixture-domain-security
  summary_line: TLSv1.3 · HSTS
slug: fixture
tags:
- Company
- CRM
- Sales
- B2B
- Artificial Intelligence
- Agents
- MCP
- Customer Relationship Management
website: https://fixture.app
---
