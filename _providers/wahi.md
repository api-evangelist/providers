---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wahi Agentic Access
  operation_count: 1
  slug: wahi-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: 'The stock WordPress REST API served by Wahi''s marketing and Learning Centre CMS at https://wahi.com/wp-json/. It is publicly reachable and self-describing: an anonymous GET on the root returns a 319KB'
  name: Wahi WordPress REST API
  slug: wahi-wordpress-rest-api
- description: Wahi's own real estate API, and the only machine-readable contract it authors. Discovered through https://wahi.com/.well-known/ai-plugin.json, an OpenAI-style AI plugin manifest that points at https:/
  name: Wahi Listing Search API
  slug: wahi-listing-search-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wahi-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wahi-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wahi-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wahi-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wahi-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wahi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wahi-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wahi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wahi-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/wahi-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wahi-com
- group: operate
  title: ''
  type: Support
  url: https://wahi.com/ca/en/contact-us/
- group: company
  title: ''
  type: Website
  url: https://wahi.com/ca/en
- group: company
  title: ''
  type: About
  url: https://wahi.com/ca/en/about-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wahi.com/ca/en/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wahi.com/ca/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://wahi.com/ca/en/learning-centre/
- group: company
  title: ''
  type: BlogRSS
  url: https://wahi.com/ca/en/feed/
created: '2026-07-26'
description: 'Wahi is a Toronto-headquartered Canadian digital real estate platform and licensed brokerage — Wahi Inc., trading as Wahi Realty Inc., Brokerage — founded in 2021 by Benjy Katchen. It runs a consumer home search, an instant home valuation estimate, market data products (Market Pulse, House Price Index), a Wahi Select REALTOR matching service and a cashback program across Ontario, British Columbia, Alberta, Nova Scotia, Saskatchewan and New Brunswick. Wahi sits in the challenger layer of the Canadian listings value chain and does not own the data it surfaces: Canadian residential listings run through CREA, the single national cooperative that operates REALTOR.ca and the Data Distribution Facility (DDF), and Wahi reaches that data as a member brokerage and through a commercial MLS connectivity vendor (Repliers) rather than by operating a feed of its own. Wahi runs no developer programme: there is no developer portal, no api./developer./developers./docs. subdomain (all fail DNS
  resolution), no API key or OAuth credential path, and no RESO Web API certification, RESO Data Dictionary certification, OData service or $metadata document anywhere on its hosts — Wahi appears in neither the RESO certificates directory nor RESO''s Canadian membership roster. The Terms of Use expressly forbid automated access, crawling and scraping, and forbid collecting, copying, storing or redistributing MLS data. It does, however, publish two agent-facing artifacts that a portal-shaped search misses: a 421KB llms.txt at https://wahi.com/llms.txt (Last-Updated 2025-07-20) and an OpenAI-style AI plugin manifest at /.well-known/ai-plugin.json that points to a genuine OpenAPI 3.0.1 "Listing Search API" at https://wahi.com/gpt/openapi.yaml — one anonymous searchListings operation with 30 typed filters over Canadian listings. The spec is still served; the server it names, api.prod.wahi.com/gpt, returns 404, so the contract is published but unserved. A live Apollo GraphQL endpoint exists at
  api.prod.wahi.com/graphql with introspection disabled and robots.txt disallowing it, and the stock WordPress REST API of the marketing CMS remains anonymously callable. Wahi is overwhelmingly an API consumer rather than a producer, but not a zero.'
image: https://wahi.com/wp-content/uploads/2022/10/wahi-logo.svg
layout: provider
modified: '2026-07-26'
name: Wahi
nav: Providers
network: true
overview: 'Wahi publishes 1 API on the [APIs.io](https://apis.io/) network: Listing Search API. Tagged areas include Real Estate, Canada, Property Listings, MLS, and Valuation.


  Wahi''s developer surface includes authentication, support, engineering blog, and 16 more developer resources.'
random_paper: 86
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 47.3
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Wahi Authentication
  slug: wahi-authentication
  summary_line: none/http-basic/cookie · 3 schemes
- kind: domain-security
  name: Wahi Domain Security
  slug: wahi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wahi
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- Valuation
- AVM
- PropTech
- Rentals
- Brokerage
website: https://wahi.com/ca/en
---
