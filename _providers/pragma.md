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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.0
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Public external REST API for FirstLook, Pragma's playtest and community platform. Uses scoped API tokens to query players, look up or find-or-create a player, record analytics events (sessions, counte
  name: FirstLook External API
  slug: firstlook-external-api
- description: Pragma Connect is a suite of backend game-development tools — player accounts, social, economy/commerce, and Limited Access Mode — that integrate with Steam, Twitch, Discord and more, with an API refe
  name: Pragma Connect
  slug: pragma-connect
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://pragma.gg/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud-docs.pragma.gg/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firstlook.gg/
- group: docs
  title: ''
  type: APIReference
  url: https://api.firstlook.gg/external/swagger-ui/
- group: start
  title: ''
  type: GettingStarted
  url: https://cloud-docs.pragma.gg/get-started
- group: company
  title: ''
  type: Blog
  url: https://pragma.gg/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://pragma.gg/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.firstlook.gg/manage/~/signup
- group: operate
  title: ''
  type: Support
  url: https://pragma.gg/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pragma.gg/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pragma.gg/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pragmaplatform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firstlook.gg
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pragma-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pragma-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/pragma-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pragma-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pragma-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pragma-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pragma-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/pragma-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pragma-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pragma-domain-security.yml
created: '2026-07-17'
description: Pragma is a backend infrastructure company for game developers, used by more than half of top PC and console studios (including studios such as Bungie, EA, and Remedy) to launch and operate live games. The Pragma Platform provides a game backend engine (game loops, player data, live operations, telemetry, and admin dashboards), plus social and commerce services (cross-platform authentication with Steam, Discord, Twitch, PlayStation, Xbox and more, virtual currency, entitlements, and order management). Pragma Connect packages these as a suite of backend tools for Unreal and Unity. Pragma also operates FirstLook, a playtest and community-management platform that runs onboarding, key management, surveys, rewards, creator programs, and player analytics — and exposes a public external REST API (scoped API tokens), Unity/Unreal SDKs, and a hosted MCP server for AI assistants. Added to the API Evangelist network from VC-portfolio signal (Greylock, Insight Partners) and enriched from
  Pragma's public developer surface.
image: https://pragma.gg/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Pragma MCP Server
  slug: pragma-mcp-server
modified: '2026-07-20'
name: Pragma
nav: Providers
network: true
overview: 'Pragma publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Infrastructure, Gaming, Game Backend, and Live Operations.


  Pragma''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 16 more developer resources.'
random_paper: 2
scopes:
- name: Pragma Scopes
  scope_count: 5
  slug: pragma-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 10
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 64.3
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 30.3
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Pragma Authentication
  slug: pragma-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Pragma Domain Security
  slug: pragma-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pragma
tags:
- Company
- Infrastructure
- Gaming
- Game Backend
- Live Operations
- Player Accounts
- Authentication
- Commerce
- Playtesting
- Community
- Analytics
- Developer Tools
website: https://pragma.gg/
---
