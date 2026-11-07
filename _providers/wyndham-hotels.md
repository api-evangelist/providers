---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: platform
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: 'The public WordPress REST API (wp-json) of the Wyndham Hotels & Resorts website at www.wyndhambusiness.com: the route index of the site''s content management system, catalogued as one site surface rath'
  name: Wyndham Hotels & Resorts Website (WordPress REST, www.wyndhambusiness.com)
  slug: wyndhambusiness-com-website-wordpress-rest
- description: 'The public WordPress REST API (wp-json) of the Wyndham Hotels & Resorts website at development.wyndhamhotels.com: the route index of the site''s content management system, catalogued as one site surfac'
  name: Wyndham Hotels & Resorts Website (WordPress REST, development.wyndhamhotels.com)
  slug: development-wyndhamhotels-com-website-wordpress-rest
- description: A WordPress MCP adapter is registered on www.wyndhambusiness.com in the `mcp` namespace alongside wp-abilities/v1, and — unlike most WordPress MCP installs — it is bound to a working OAuth 2.1 authori
  name: Wyndham Business WordPress MCP Server (OAuth-gated)
  slug: wyndham-business-mcp-server
artifact_total: 7
common:
- group: auth
  href: https://artifacts.apis.io/wyndham-hotels/security/wyndham-hotels-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wyndham-hotels-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/wyndham-hotels/authentication/wyndham-hotels-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wyndham-hotels-authentication.yml
- group: auth
  href: https://artifacts.apis.io/wyndham-hotels/scopes/wyndham-hotels-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/wyndham-hotels-scopes.yml
- group: agent
  href: https://artifacts.apis.io/wyndham-hotels/well-known/wyndham-hotels-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/wyndham-hotels-well-known.yml
- group: agent
  href: https://artifacts.apis.io/wyndham-hotels/mcp/wyndham-hotels-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/wyndham-hotels-mcp.yml
- group: design
  href: https://artifacts.apis.io/wyndham-hotels/conventions/wyndham-hotels-conventions.yml
  title: ''
  type: Conventions
  url: conventions/wyndham-hotels-conventions.yml
- group: design
  href: https://artifacts.apis.io/wyndham-hotels/errors/wyndham-hotels-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wyndham-hotels-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wyndham-hotels/data-model/wyndham-hotels-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wyndham-hotels-data-model.yml
- group: design
  href: https://artifacts.apis.io/wyndham-hotels/conformance/wyndham-hotels-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wyndham-hotels-conformance.yml
- group: design
  href: https://artifacts.apis.io/wyndham-hotels/lifecycle/wyndham-hotels-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/wyndham-hotels-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/wyndham-hotels/discovery/wyndham-hotels-wyndhambusiness-wp-json-root.json
  title: ''
  type: DiscoveryDocument
  url: discovery/wyndham-hotels-wyndhambusiness-wp-json-root.json
- group: other
  href: https://artifacts.apis.io/wyndham-hotels/discovery/wyndham-hotels-development-wp-json-root.json
  title: ''
  type: DiscoveryDocument
  url: discovery/wyndham-hotels-development-wp-json-root.json
- group: agent
  href: https://artifacts.apis.io/wyndham-hotels/llms/wyndham-hotels-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wyndham-hotels-llms.txt
- group: agent
  href: https://artifacts.apis.io/wyndham-hotels/llms/wyndham-hotels-wyndhambusiness-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wyndham-hotels-wyndhambusiness-llms.txt
- group: agent
  href: https://artifacts.apis.io/wyndham-hotels/llms/wyndham-hotels-development-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wyndham-hotels-development-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.wyndhamhotels.com/
- group: company
  title: ''
  type: CorporateWebsite
  url: https://corporate.wyndhamhotels.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/wyndhamhotels
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Wyndham_Hotels_%26_Resorts
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wyndhamhotels.com/about-us/terms-of-use-more-info
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wyndhamhotels.com/about-us/privacy-notice-more-info
- group: operate
  title: ''
  type: Support
  url: https://www.wyndhamhotels.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://corporate.wyndhamhotels.com/news-media/
- group: agent
  title: ''
  type: LLMSTxt
  url: https://www.wyndhamhotels.com/llms.txt
- group: other
  title: ''
  type: Robots
  url: https://www.wyndhamhotels.com/robots.txt
- group: other
  title: ''
  type: Sitemap
  url: https://www.wyndhamhotels.com/sitemap.xml
- group: company
  title: ''
  type: InvestorRelations
  url: https://investor.wyndhamhotels.com/
- group: other
  title: ''
  type: AnnualReport
  url: https://www.sec.gov/Archives/edgar/data/1722684/000172268426000007/wh-20251231.htm
- group: other
  title: ''
  type: Franchising
  url: https://development.wyndhamhotels.com/
- group: other
  title: ''
  type: Suppliers
  url: https://wyndham.supplierone.co/
- group: other
  title: ''
  type: TravelProfessionals
  url: https://www.wyndhamhotels.com/content/whg-ecomm-responsive/en-us/whg/about-us/travel-professionals.html
- group: other
  title: ''
  type: BusinessTravel
  url: https://www.wyndhambusiness.com/
- group: other
  title: ''
  type: Loyalty
  url: https://www.wyndhamhotels.com/wyndham-rewards
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Wyndham-Hotels-Resorts
- group: other
  title: ''
  type: Predecessor
  url: https://raw.githubusercontent.com/api-evangelist/wyndham-worldwide/refs/heads/main/apis.yml
- group: other
  href: https://artifacts.apis.io/wyndham-hotels/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: 'Wyndham Hotels & Resorts, Inc. (NYSE: WH) is the world''s largest hotel franchising company by number of properties, with over 8,300 affiliated hotels and approximately 869,000 rooms across roughly 25 brands in 95+ countries, licensed to more than 6,200 franchisees. Headquartered in Parsippany, New Jersey, its home market is the United States. Wyndham does not operate most of its hotels — it franchises brands (Days Inn, Super 8, Ramada, La Quinta, Microtel, Baymont, Howard Johnson, Travelodge, Wingate, Wyndham, Wyndham Grand, Trademark Collection, TRYP, Dolce, ECHO Suites and others) and sells the demand that flows through them. It sits in the distribution chain as a franchisor and demand aggregator rather than as a distribution platform: inventory reaches buyers through Wyndham''s own brand.com sites and Wyndham Rewards, through GDS chain codes under master chain code WR, and through third-party online travel agents, with the central reservation layer supplied by Sabre Hospitality''s
  SynXis CRS under a relationship Sabre publicly renewed in July 2024. There is no travel API: no developer portal, no API documentation, no OpenAPI, and no property, rate, availability, reservation, loyalty or folio surface is machine-readable anywhere. developer., developers., docs. and api. subdomains do not resolve; /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404, and mcp.wyndhamhotels.com resolves with a valid certificate but serves an Akamai 503 on every path. The Terms of Use (effective 2026-03-12) affirmatively prohibit robots, spiders, meta-searching and automated access, and separately prohibit automated access to Wyndham''s AI Search. What a second enrichment round did find on 2026-07-28 is undocumented CMS infrastructure that is nonetheless genuinely live: www.wyndhambusiness.com and development.wyndhamhotels.com both run WordPress on WP Engine and leave the WordPress REST API anonymously readable (309 and 403 registered routes, with JSON Schema
  available by HTTP OPTIONS), and three WordPress MCP adapter routes are registered across the two estates — one of them, on www.wyndhambusiness.com, bound to a real OAuth 2.1 authorization server with RFC 8414 and RFC 9728 discovery metadata, mandatory PKCE S256 and a single `mcp` scope, returning a standards-correct 401 bearer challenge to anonymous callers. None of it is documented, supported, or usable without a credential Wyndham issues to no third party, and none of it carries hotel data. The integration surface that matters is still reached only through a franchise agreement, a commercial distribution agreement, or Sabre.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wyndham-hotels.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.wyndhambusiness.com.
  name: Wyndham Hotels & Resorts MCP Server
  slug: wyndham-hotels-mcp-yml
modified: '2026-07-28'
name: Wyndham Hotels & Resorts
nav: Providers
network: true
overview: 'Wyndham Hotels & Resorts is listed with 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Hospitality, Hotels, and Booking.


  Wyndham Hotels & Resorts'' developer surface includes authentication, support, engineering blog, and 33 more developer resources.'
random_paper: 20
scopes:
- name: Wyndham Hotels Scopes
  scope_count: 1
  slug: wyndham-hotels-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 71.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 20.9
  provenance:
    conformance: derived
    mcp: site-plugin
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wyndham-hotels/wyndham-hotels-2026-09-02T171034.png
security:
- kind: authentication
  name: Wyndham Hotels Authentication
  slug: wyndham-hotels-authentication
  summary_line: none/oauth2 · 4 schemes
- kind: domain-security
  name: Wyndham Hotels Domain Security
  slug: wyndham-hotels-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: wyndham-hotels
tags:
- Travel
- United States
- Hospitality
- Hotels
- Booking
- Franchising
- Distribution
- Loyalty
- GDS
website: https://www.wyndhamhotels.com/
---
