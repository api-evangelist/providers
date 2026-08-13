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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 19.6
  scored_at: '2026-08-12'
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
  name: smashgg-mcp.yml
  slug: smashgg-mcpyml
modified: '2026-07-21'
name: Smashgg
nav: Providers
network: true
overview: 'Smashgg publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Esports, Gaming, and Tournaments.


  Smashgg''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 19 more developer resources.'
random_paper: 26
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
  composite: 30.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 26.3
  previous_composite: 30.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
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
- Events
- Developer API
website: https://www.start.gg
---
