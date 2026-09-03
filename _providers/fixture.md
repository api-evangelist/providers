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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.5
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete company records.
  name: Fixture Accounts API
  slug: fixture-accounts-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: List and ingest CRM Activity records.
  name: Fixture Activities API
  slug: fixture-activities-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete person records.
  name: Fixture Contacts API
  slug: fixture-contacts-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete Deal records.
  name: Fixture Deals API
  slug: fixture-deals-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: The Fixture API API from Fixture — 1 operation(s) for fixture api.
  name: Fixture Fixture API API
  slug: fixture-fixture-api-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create, read, update, and convert Leads.
  name: Fixture Leads API
  slug: fixture-leads-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create Notes linked to CRM entities.
  name: Fixture Notes API
  slug: fixture-notes-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: List Pipelines and inspect their nested stages.
  name: Fixture Pipelines API
  slug: fixture-pipelines-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: List Task status definitions available to the current organization.
  name: Fixture Task Statuses API
  slug: fixture-task-statuses-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: Create, read, update, and delete Tasks.
  name: Fixture Tasks API
  slug: fixture-tasks-api
- baseURL: https://beta-api.fixture.app/api/v1
  baseurl_source: declared
  description: The Users API from Fixture — 1 operation(s) for users.
  name: Fixture Users API
  slug: fixture-users-api
artifact_total: 27
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Fixture Accounts API
  slug: open-fixture-accounts-api
- collection_type: open
  name: Fixture Accounts Activities API
  slug: open-fixture-activities-api
- collection_type: open
  name: Fixture Accounts Contacts API
  slug: open-fixture-contacts-api
- collection_type: open
  name: Fixture Accounts Deals API
  slug: open-fixture-deals-api
- collection_type: open
  name: Fixture Accounts Fixture API API
  slug: open-fixture-fixture-api-api
- collection_type: open
  name: Fixture Accounts Leads API
  slug: open-fixture-leads-api
- collection_type: open
  name: Fixture Accounts Notes API
  slug: open-fixture-notes-api
- collection_type: open
  name: Fixture Accounts Pipelines API
  slug: open-fixture-pipelines-api
- collection_type: open
  name: Fixture Accounts Task Statuses API
  slug: open-fixture-task-statuses-api
- collection_type: open
  name: Fixture Accounts Tasks API
  slug: open-fixture-tasks-api
- collection_type: open
  name: Fixture Accounts Users API
  slug: open-fixture-users-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/fixture-v1-overlay.yaml
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
  name: Fixture MCP
  slug: fixture-mcp
modified: '2026-07-20'
name: Fixture
nav: Providers
network: true
overview: 'Fixture publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Activities API, Contacts API, and 8 more. Tagged areas include Company, CRM, Sales, B2B, and Artificial Intelligence.


  Fixture''s developer surface includes documentation, API reference, getting-started guide, signup flow, authentication, CLI, and 22 more developer resources.'
random_paper: 19
scopes:
- name: Fixture Scopes
  scope_count: 0
  slug: fixture-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 62.0
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 42.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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
website: https://fixture.app
---
