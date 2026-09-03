---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 59.5
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 8
  human_in_the_loop: 1
  name: Zillapi Agentic Access
  operation_count: 29
  slug: zillapi-agentic-access
  summary_line: 29 operations · 8 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Account API from Zillapi — 2 operation(s) for account.
  name: Zillapi Account API
  slug: zillapi-account-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Buildings API from Zillapi — 1 operation(s) for buildings.
  name: Zillapi Buildings API
  slug: zillapi-buildings-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Jobs API from Zillapi — 3 operation(s) for jobs.
  name: Zillapi Jobs API
  slug: zillapi-jobs-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Listings API from Zillapi — 4 operation(s) for listings.
  name: Zillapi Listings API
  slug: zillapi-listings-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Properties API from Zillapi — 13 operation(s) for properties.
  name: Zillapi Properties API
  slug: zillapi-properties-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Search API from Zillapi — 2 operation(s) for search.
  name: Zillapi Search API
  slug: zillapi-search-api
- baseURL: https://api.zillapi.com
  baseurl_source: declared
  description: The Webhooks API from Zillapi — 3 operation(s) for webhooks.
  name: Zillapi Webhooks API
  slug: zillapi-webhooks-api
artifact_total: 24
asyncapis:
- description: ''
  name: Zillapi Webhooks
  slug: zillapi-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Zillapi: Zillow property data Account API'
  slug: open-zillapi-account-api
- collection_type: open
  name: 'Zillapi: Zillow property data Buildings API'
  slug: open-zillapi-buildings-api
- collection_type: open
  name: 'Zillapi: Zillow property data Jobs API'
  slug: open-zillapi-jobs-api
- collection_type: open
  name: 'Zillapi: Zillow property data Listings API'
  slug: open-zillapi-listings-api
- collection_type: open
  name: 'Zillapi: Zillow property data Properties API'
  slug: open-zillapi-properties-api
- collection_type: open
  name: 'Zillapi: Zillow property data Search API'
  slug: open-zillapi-search-api
- collection_type: open
  name: 'Zillapi: Zillow property data Webhooks API'
  slug: open-zillapi-webhooks-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/zillapi-capability-edges.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/zillapi-get-zestimate.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/zillapi-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/zillapi-openapi-overlay.yaml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zillapi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zillapi-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zillapi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zillapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/zillapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/zillapi-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/zillapi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/zillapi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/zillapi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/zillapi-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://zillapi.com/.well-known/api-catalog
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/zillapi-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zillapi-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/zillapi-plans.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zillapi-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/ZeroPointRepo/zillow-skills/blob/main/SECURITY.md
- group: start
  title: ''
  type: DeveloperPortal
  url: https://zillapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://zillapi.com/quickstart/
- group: docs
  title: ''
  type: APIReference
  url: https://zillapi.com/api/properties/
- group: start
  title: ''
  type: GettingStarted
  url: https://zillapi.com/quickstart/
- group: company
  title: ''
  type: Blog
  url: https://zillapi.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ZeroPointRepo/zillow-skills
- group: commercial
  title: ''
  type: Pricing
  url: https://zillapi.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://zillapi.com/signup
- group: start
  title: ''
  type: Login
  url: https://zillapi.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zillapi.com/legal/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zillapi.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: mailto:hello@zillapi.com
created: '2026-07-13'
description: Independent third-party provider of Zillow-sourced U.S. residential property data via a REST API, hosted MCP server, and agent skills. Returns ~300+ fields per property including price, Zestimate, rent Zestimate, photos, schools, taxes, and full price history, plus listing search, building extraction, async batch jobs, and signed webhooks.
image: https://zillapi.com/og.png
layout: provider
mcp_servers:
- description: ''
  name: Zillapi MCP Server
  slug: zillapi-mcp-server
modified: '2026-08-09'
name: Zillapi
nav: Providers
network: true
overview: 'Zillapi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Account API, Buildings API, Jobs API, and 4 more. Tagged areas include Real-Estate, PropTech, Property Data, Zillow, and Zestimate.


  The Zillapi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Zillapi''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 25 more developer resources.'
plans:
- name: Zillapi Plans
  plan_count: 4
  slug: zillapi-plans
random_paper: 1
rate_limits:
- limit_count: 3
  name: Zillapi Rate Limits
  slug: zillapi-rate-limits
scopes:
- name: Zillapi Scopes
  scope_count: 1
  slug: zillapi-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 62.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 66.3
    developer_ergonomics: 64.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 62.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zillapi/refs/heads/main/screenshots/zillapi-2026-08-17T083106.png
security:
- kind: authentication
  name: Zillapi Authentication
  slug: zillapi-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Zillapi Domain Security
  slug: zillapi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Zillapi Vulnerability Disclosure
  slug: zillapi-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: zillapi
tags:
- Real-Estate
- PropTech
- Property Data
- Zillow
- Zestimate
- Valuation
- AVM
- Listings
- MCP
- AI Agent
- REST API
website: https://zillapi.com/
---
