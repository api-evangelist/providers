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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 8.8
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: Single GraphQL endpoint exposing start.gg (smash.gg) tournaments, events, entrants, sets, standings, players, and users, with mutations for reporting results and managing brackets.
  name: start.gg GraphQL API
  slug: startgg-graphql-api
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.start.gg
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.start.gg
- group: docs
  title: ''
  type: Documentation
  url: https://developer.start.gg/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developer.start.gg/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.start.gg/docs/intro
- group: auth
  title: ''
  type: Authentication
  url: authentication/smashgg-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/smashgg-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/smashgg-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/smashgg-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/smashgg-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smashgg-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smashgg-domain-security.yml
- group: design
  title: ''
  type: Components
  url: components/smashgg-components.yml
- group: build
  title: ''
  type: Packages
  url: packages/smashgg-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/smashgg-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/smashgg-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/smashgg-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smashgg-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://help.start.gg
- group: company
  title: ''
  type: Blog
  url: https://blog.start.gg/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/smashgg
- group: start
  title: ''
  type: Login
  url: https://www.start.gg/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.start.gg/about/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.start.gg/about/privacy
created: '2026-07-17'
description: Smashgg (now start.gg, following its acquisition by Microsoft) is a competitive-gaming and esports platform for running tournaments, brackets, and leagues across fighting games and other titles. Its public developer API is a single GraphQL endpoint (https://api.start.gg/gql/alpha) exposing tournaments, events, entrants, sets, phases, standings, players, and users, plus mutations for reporting set results and managing seeding and brackets. Authentication is via personal access tokens (Bearer, 1-year expiry) or OAuth 2.0 authorization-code tokens scoped to a user. The original smash.gg domain now redirects to start.gg.
image: https://www.start.gg/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Smashgg MCP Server
  slug: smashgg-mcp-server
modified: '2026-07-21'
name: Smashgg
nav: Providers
network: true
overview: 'Smashgg publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Esports, Gaming, and Tournaments.


  Smashgg''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 19 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 2
  name: Smashgg Rate Limits
  slug: smashgg-rate-limits
scopes:
- name: Smashgg Scopes
  scope_count: 4
  slug: smashgg-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 23.7
  previous_composite: 28.7
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/smashgg/refs/heads/main/screenshots/smashgg-2026-09-02T155940.png
security:
- kind: authentication
  name: Smashgg Authentication
  slug: smashgg-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Smashgg Domain Security
  slug: smashgg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: smashgg
tags:
- Company
- Consumer
- Esports
- Gaming
- Tournaments
- GraphQL
- Event
- Developer API
website: https://www.start.gg
---
