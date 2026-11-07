---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 48.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Freight Waves Agentic Access
  operation_count: 9
  slug: freight-waves-agentic-access
  summary_line: 9 operations · 1 acting
api_count: 3
apis:
- baseURL: https://api.freightwaves.com
  baseurl_source: declared
  description: Obtain and refresh API bearer tokens.
  name: Freight Waves Authentication API
  slug: freight-waves-authentication-api
- baseURL: https://api.freightwaves.com
  baseurl_source: declared
  description: Billable index data queries by item, level, and lane.
  name: Freight Waves Data API
  slug: freight-waves-data-api
- baseURL: https://api.freightwaves.com
  baseurl_source: declared
  description: Free reference lookups for valid indexes, qualifiers, levels, lanes, and zip3.
  name: Freight Waves Lookup API
  slug: freight-waves-lookup-api
artifact_total: 14
collections:
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
  type: BlogRSS
  url: https://www.freightwaves.com:443/feed
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
- group: other
  href: https://artifacts.apis.io/freight-waves/overlays/freight-waves-sonar-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/freight-waves-sonar-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/freight-waves/mcp/freight-waves-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/freight-waves-mcp.yml
- group: agent
  href: https://artifacts.apis.io/freight-waves/well-known/freight-waves-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/freight-waves-well-known.yml
- group: agent
  href: https://artifacts.apis.io/freight-waves/llms/freight-waves-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/freight-waves-llms.txt
- group: auth
  href: https://artifacts.apis.io/freight-waves/authentication/freight-waves-authentication.yml
  title: ''
  type: Authentication
  url: authentication/freight-waves-authentication.yml
- group: auth
  href: https://artifacts.apis.io/freight-waves/scopes/freight-waves-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/freight-waves-scopes.yml
- group: design
  href: https://artifacts.apis.io/freight-waves/conventions/freight-waves-conventions.yml
  title: ''
  type: Conventions
  url: conventions/freight-waves-conventions.yml
- group: operate
  href: https://artifacts.apis.io/freight-waves/rate-limits/freight-waves-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/freight-waves-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/freight-waves/errors/freight-waves-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/freight-waves-problem-types.yml
- group: design
  href: https://artifacts.apis.io/freight-waves/lifecycle/freight-waves-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/freight-waves-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/freight-waves/conformance/freight-waves-conformance.yml
  title: ''
  type: Conformance
  url: conformance/freight-waves-conformance.yml
- group: auth
  href: https://artifacts.apis.io/freight-waves/security/freight-waves-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/freight-waves-domain-security.yml
- group: design
  href: https://artifacts.apis.io/freight-waves/data-model/freight-waves-data-model.yml
  title: ''
  type: DataModel
  url: data-model/freight-waves-data-model.yml
- group: agent
  href: https://artifacts.apis.io/freight-waves/agentic-access/freight-waves-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/freight-waves-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/freight-waves/skills/_index.yml
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
  slug: freightwaves
modified: '2026-10-06'
name: Freight Waves
nav: Providers
network: true
overview: 'Freight Waves is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Authentication API, Data API, and Lookup API. Tagged areas include Company, Freight, Logistics, Supply Chain, and Transportation.


  The Freight Waves catalog on APIs.io includes 1 Spectral governance ruleset.


  Freight Waves'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 22 more developer resources.'
random_paper: 20
rate_limits:
- limit_count: 1
  name: Freight Waves Rate Limits
  slug: freight-waves-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Freight Waves API Rules
  rule_count: 60
  severity_counts:
    error: 58
    hint: 0
    info: 1
    warn: 1
  slug: freight-waves-rules
scopes:
- name: Freight Waves Scopes
  scope_count: 1
  slug: freight-waves-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 23
    catalog_earned: 52.5
    catalog_earned_first_party: 8.0
    catalog_gap: 62.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 14.5
    developer_ergonomics: 58.9
    discoverability: 80.0
    operational_transparency: 23.7
  previous_composite: 38.7
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
    score: 32.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/freight-waves/freight-waves-2026-07-25T215152.png
security:
- kind: authentication
  name: Freight Waves Authentication
  slug: freight-waves-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Freight Waves Domain Security
  slug: freight-waves-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: Fetch SONAR freight-market index data
  slug: freight-waves-fetch-index-data
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
