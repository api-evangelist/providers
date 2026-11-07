---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wahi Agentic Access
  operation_count: 1
  slug: wahi-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'The public WordPress REST API (wp-json) of the Wahi website at wahi.com: the route index of the site''s content management system, catalogued as one site surface rather than as separate APIs.'
  name: Wahi Website (WordPress REST)
  slug: wahi-com-website-wordpress-rest
- baseURL: https://api.prod.wahi.com/gpt
  baseurl_source: declared
  description: The Search API from Wahi — 1 operation(s) for search.
  name: Wahi Search API
  slug: wahi-search-api
artifact_total: 9
collections:
- collection_type: open
  name: API Collection
  slug: open-wahi-wp-json-discovery
common:
- group: other
  href: https://artifacts.apis.io/wahi/overlays/wahi-listing-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/wahi-listing-search-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/wahi/skills/wahi-search-listings.md
  title: ''
  type: AgentSkill
  url: skills/wahi-search-listings.md
- group: agent
  href: https://artifacts.apis.io/wahi/mcp/wahi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wahi-mcp.yml
- group: auth
  href: https://artifacts.apis.io/wahi/security/wahi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wahi-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/wahi/agentic-access/wahi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wahi-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/wahi/llms/wahi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wahi-llms.txt
- group: agent
  href: https://artifacts.apis.io/wahi/well-known/wahi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wahi-well-known.yml
- group: auth
  href: https://artifacts.apis.io/wahi/authentication/wahi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wahi-authentication.yml
- group: design
  href: https://artifacts.apis.io/wahi/conventions/wahi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wahi-conventions.yml
- group: design
  href: https://artifacts.apis.io/wahi/errors/wahi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wahi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wahi/lifecycle/wahi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wahi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/wahi/conformance/wahi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wahi-conformance.yml
- group: build
  href: https://artifacts.apis.io/wahi/packages/wahi-packages.yml
  title: ''
  type: Packages
  url: packages/wahi-packages.yml
- group: agent
  href: https://artifacts.apis.io/wahi/skills/_index.yml
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
  slug: wahi-mcp-yml
modified: '2026-07-26'
name: Wahi
nav: Providers
network: true
overview: 'Wahi publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Search API, and 1 more. Tagged areas include Real Estate, Canada, Property Listings, MLS, and Valuation.


  The Wahi catalog on APIs.io includes 1 Spectral governance ruleset.


  Wahi''s developer surface includes authentication, support, engineering blog, and 19 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 82
  extends:
  - spectral:oas
  name: Wahi API Rules
  rule_count: 41
  severity_counts:
    error: 39
    hint: 0
    info: 1
    warn: 1
  slug: wahi-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 23
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 39.8
    developer_ergonomics: 25.6
    discoverability: 64.3
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 36.8
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
    score: 23.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/wahi/wahi-2026-09-02T170359.png
security:
- kind: authentication
  name: Wahi Authentication
  slug: wahi-authentication
  summary_line: none/http-basic/cookie · 3 schemes
- kind: domain-security
  name: Wahi Domain Security
  slug: wahi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: Search Canadian property listings on Wahi
  slug: wahi-search-listings
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
