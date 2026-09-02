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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.9
  scored_at: '2026-09-01'
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
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FreightWaves SONAR Authentication API
  slug: open-freight-waves-authentication-api
- collection_type: open
  name: FreightWaves SONAR Authentication Data API
  slug: open-freight-waves-data-api
- collection_type: open
  name: FreightWaves SONAR Authentication Lookup API
  slug: open-freight-waves-lookup-api
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
  url: openapi/_original/freight-waves-sonar-openapi.yml
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
- description: FreightWaves hosts a remote MCP server exposing SONAR freight-market intelligence to agents. The endpoint is protected by OAuth 2.1 (bearer) with the mcp:read scope; unauthenticated requests return 40
  name: Freight Waves MCP Server
  slug: freight-waves-mcp-server
modified: '2026-07-19'
name: Freight Waves
nav: Providers
network: true
overview: 'Freight Waves publishes 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Data API, and Lookup API. Tagged areas include Company, Freight, Logistics, Supply Chain, and Transportation.


  Freight Waves'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 22 more developer resources.'
random_paper: 17
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
  composite: 39.6
  coverage:
    artifact_dirs: 19
    catalog_gap: 67.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -10.9
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 14.5
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 23.7
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/freight-waves/refs/heads/main/screenshots/freight-waves-2026-07-25T215152.png
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
- Sonar
website: https://freightwaves.com
---
