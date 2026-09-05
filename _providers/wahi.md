---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wahi Agentic Access
  operation_count: 1
  slug: wahi-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'The stock WordPress REST API served by Wahi''s marketing and Learning Centre CMS at https://wahi.com/wp-json/. It is publicly reachable and self-describing: an anonymous GET on the root returns a 319KB'
  name: Wahi WordPress REST API
  slug: wahi-wordpress-rest-api
- baseURL: https://wahi.com/wp-json
  baseurl_source: declared
  description: The Search API from Wahi — 1 operation(s) for search.
  name: Wahi Search API
  slug: wahi-search-api
artifact_total: 7
collections:
- collection_type: open
  name: API Collection
  slug: open-wahi-wp-json-discovery
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/wahi-listing-search-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/wahi-search-listings.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wahi-mcp.yml
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
mcp_servers:
- description: ''
  name: Wahi MCP Server
  slug: wahi-mcp-server
modified: '2026-07-26'
name: Wahi
nav: Providers
network: true
overview: 'Wahi publishes 1 API on the [APIs.io](https://apis.io/) network: Search API. Tagged areas include Real-Estate, Canada, Property Listings, MLS, and Valuation.


  Wahi''s developer surface includes authentication, support, engineering blog, and 19 more developer resources.'
random_paper: 5
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 63.0
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 4.5
    contract_quality: 44.2
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 38.0
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
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wahi/refs/heads/main/screenshots/wahi-2026-09-02T170359.png
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
- Real-Estate
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
