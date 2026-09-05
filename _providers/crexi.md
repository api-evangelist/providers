---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 6.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: The Crexi Exchange API is Crexi's partner-facing REST API, documented in a Theneo-published portal at api-docs.crexi.com (password protected) and fronted by a Swagger UI gateway at exchange.crexi.com.
  name: Crexi Exchange API
  slug: crexi-exchange-api
- description: The api.crexi.com host is the platform API backing the Crexi web and mobile applications. It anonymously publishes OpenID Connect discovery (/.well-known/openid-configuration) and OAuth 2.0 authorizat
  name: Crexi Platform API
  slug: crexi-platform-api
- description: 'The Crexi Listing API is a one-way data sync that lets qualifying organizations — MLSs and Realtor Boards, large brokerages and franchise networks, and real estate data providers — automatically push '
  name: Crexi Listing API
  slug: crexi-listing-api
artifact_total: 7
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/crexi-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/crexi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.crexi.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.crexi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.crexi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.crexi.com/listing-api-overview-crexi-help-center
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.crexi.com/crexi-basics
- group: operate
  title: ''
  type: Support
  url: https://learn.crexi.com/
- group: company
  title: ''
  type: Blog
  url: https://www.crexi.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/crexi-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://www.crexi.com/broker-plans
- group: start
  title: ''
  type: SignUp
  url: https://www.crexi.com/signup
- group: start
  title: ''
  type: Login
  url: https://admin.crexi.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.crexi.com/msa/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.crexi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.crexi.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/crexi-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/crexi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/crexi-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/crexi-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/crexi-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/crexi-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/crexi-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/crexi-llms.txt
- group: other
  title: ''
  type: Research
  url: https://research.crexi.com/
- group: other
  title: ''
  type: Podcast
  url: https://podcast.crexi.com/
created: '2026-08-01'
description: 'CREXi (Commercial Real Estate Exchange, Inc.) is a Los Angeles-based commercial real estate marketplace and data platform founded in 2015, operating a sales marketplace, lease marketplace, auction platform, Broker PRO tools and the Crexi Intelligence property-records product. Its API surface is partner-gated rather than self-serve: the Crexi Listing API is a one-way syndication feed that lets MLSs, Realtor Boards, brokerages and data providers push listings into the marketplace (RESO, RETS, WebAPI and XML feeds, synced daily, with Crexi stating 100% compliance with the RESO Data Dictionary and 100+ partner organizations), while the Crexi Exchange API is documented in a password-protected Theneo portal at api-docs.crexi.com and fronted by an API-key-gated Swagger UI at exchange.crexi.com. The platform API host api.crexi.com publishes anonymous OpenID Connect and OAuth 2.0 authorization-server discovery documents.'
image: https://learn.crexi.com/hubfs/crexi%20logo%20navy%20text.svg
layout: provider
mcp_servers:
- description: ''
  name: CREXi MCP Server
  slug: crexi-mcp-server
modified: '2026-08-01'
name: CREXi
nav: Providers
network: true
overview: 'CREXi publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Estate, Commercial Real Estate, Marketplace, Property Data, and Listings.


  CREXi''s developer surface includes API reference, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 14
scopes:
- name: Crexi Scopes
  scope_count: 2
  slug: crexi-scopes
  summary_line: 2 scopes · password/refresh_token/switch_user/single_use_token_exchange
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 57.1
    discoverability: 72.2
    governance: 18.2
    operational_transparency: 18.4
  previous_composite: 32.2
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/crexi/refs/heads/main/screenshots/crexi-2026-08-07T163841.png
security:
- kind: authentication
  name: Crexi Authentication
  slug: crexi-authentication
  summary_line: apiKey/http/oauth2/openIdConnect · 5 schemes
- kind: domain-security
  name: Crexi Domain Security
  slug: crexi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: crexi
tags:
- Real-Estate
- Commercial Real Estate
- Marketplace
- Property Data
- Listings
- Auctions
- Market Intelligence
- Data Syndication
- RESO
- Company
website: https://www.crexi.com/
---
