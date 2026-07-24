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
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.1
  score: 76.0
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Freight Waves Agentic Access
  operation_count: 9
  slug: freight-waves-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 3
apis:
- description: Obtain and refresh API bearer tokens.
  name: Freight Waves Authentication API
  slug: freight-waves-authentication-api
- description: Billable index data queries by item, level, and lane.
  name: Freight Waves Data API
  slug: freight-waves-data-api
- description: Free reference lookups for valid indexes, qualifiers, levels, lanes, and zip3.
  name: Freight Waves Lookup API
  slug: freight-waves-lookup-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://freightwaves.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://knowledge.gosonar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.gosonar.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sonar.surf/Help/
- group: start
  title: ''
  type: GettingStarted
  url: https://knowledge.gosonar.com/
- group: operate
  title: ''
  type: Support
  url: https://www.freightwaves.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.freightwaves.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FreightWaves
- group: start
  title: ''
  type: Login
  url: https://sonar.surf/auth/login
- group: start
  title: ''
  type: SignUp
  url: https://gosonar.com/sonar-demo-request
- group: commercial
  title: ''
  type: Pricing
  url: https://www.freightwaves.com/subscribe
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.freightwaves.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firecrown.com/privacy-policy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/freight-waves-sonar-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/freight-waves-sonar-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/freight-waves-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/freight-waves-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/freight-waves-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/freight-waves-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/freight-waves-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/freight-waves-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/freight-waves-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/freight-waves-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/freight-waves-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/freight-waves-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/freight-waves-domain-security.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/freight-waves-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/freight-waves-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: FreightWaves is a supply-chain, logistics, and transportation news and market- intelligence company based in Chattanooga, TN, and backed by 8vc. Its SONAR platform delivers freight-market data — rate indexes, tender volumes and rejection indexes, capacity and pricing signals — by market, lane, and national geography over a REST API at api.freightwaves.com. Access uses a bearer token obtained from the Credential authenticate endpoint (valid one year); data calls are billable while lookup calls (indexes, qualifiers, levels, lanes, zip3, latest) are free, and a global 100 requests/minute rate limit applies. FreightWaves also operates a hosted, OAuth-protected MCP server (api.freightwaves.com/mcp, scope mcp:read) exposing SONAR data to agents.
image: https://www.freightwaves.com/wp-content/uploads/2020/01/FreightWaves-1.png
layout: provider
mcp_servers:
- description: ''
  name: freight-waves-mcp.yml
  slug: freight-waves-mcpyml
modified: '2026-07-19'
name: Freight Waves
nav: Providers
network: true
overview: 'Freight Waves publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Data API, and Lookup API. Tagged areas include Company, Freight, Logistics, Supply Chain, and Transportation.


  Freight Waves'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 22 more developer resources.'
random_paper: 14
rate_limits:
- limit_count: 1
  name: Freight Waves Rate Limits
  slug: freight-waves-rate-limits
scopes:
- name: Freight Waves Scopes
  scope_count: 1
  slug: freight-waves-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 54.5
  delta: 3.8
  facets:
    commercial_clarity: 44.7
    contract_quality: 59.6
    developer_ergonomics: 67.4
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 50.7
  regulatory:
    applies: true
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 76.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Freight Waves Authentication
  slug: freight-waves-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Freight Waves Domain Security
  slug: freight-waves-domain-security
  summary_line: TLSv1.3 · DMARC
slug: freight-waves
tags:
- Company
- Freight
- Logistics
- Supply Chain
- Transportation
- Trucking
- Market Data
- Analytics
- Freight Rates
- SONAR
website: https://freightwaves.com
---
