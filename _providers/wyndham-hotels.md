---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: www.wyndhambusiness.com — the Wyndham Business corporate-travel program site — runs WordPress on WP Engine behind Cloudflare and leaves the standard WordPress REST API anonymously readable at /wp-json
  name: Wyndham Business WordPress REST API
  slug: wyndham-business-wordpress-rest-api
- description: A WordPress MCP adapter is registered on www.wyndhambusiness.com in the `mcp` namespace alongside wp-abilities/v1, and — unlike most WordPress MCP installs — it is bound to a working OAuth 2.1 authori
  name: Wyndham Business WordPress MCP Server (OAuth-gated)
  slug: wyndham-business-mcp-server
- description: development.wyndhamhotels.com — the franchise-development site — runs the same WordPress/WP Engine stack and likewise leaves the WordPress REST API anonymously readable at /wp-json/, advertising 403 r
  name: Wyndham Hotel Development WordPress REST API
  slug: development-wordpress-rest-api
artifact_total: 18
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wyndham-hotels-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wyndham-hotels-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wyndham-hotels-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wyndham-hotels-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wyndham-hotels-mcp.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wyndham-hotels-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wyndham-hotels-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wyndham-hotels-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wyndham-hotels-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wyndham-hotels-lifecycle.yml
- group: other
  title: ''
  type: DiscoveryDocument
  url: discovery/wyndham-hotels-wyndhambusiness-wp-json-root.json
- group: other
  title: ''
  type: DiscoveryDocument
  url: discovery/wyndham-hotels-development-wp-json-root.json
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wyndham-hotels-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wyndham-hotels-wyndhambusiness-llms.txt
- group: agent
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
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: 'Wyndham Hotels & Resorts, Inc. (NYSE: WH) is the world''s largest hotel franchising company by number of properties, with over 8,300 affiliated hotels and approximately 869,000 rooms across roughly 25 brands in 95+ countries, licensed to more than 6,200 franchisees. Headquartered in Parsippany, New Jersey, its home market is the United States. Wyndham does not operate most of its hotels — it franchises brands (Days Inn, Super 8, Ramada, La Quinta, Microtel, Baymont, Howard Johnson, Travelodge, Wingate, Wyndham, Wyndham Grand, Trademark Collection, TRYP, Dolce, ECHO Suites and others) and sells the demand that flows through them. It sits in the distribution chain as a franchisor and demand aggregator rather than as a distribution platform: inventory reaches buyers through Wyndham''s own brand.com sites and Wyndham Rewards, through GDS chain codes under master chain code WR, and through third-party online travel agents, with the central reservation layer supplied by Sabre Hospitality''s
  SynXis CRS under a relationship Sabre publicly renewed in July 2024. There is no travel API: no developer portal, no API documentation, no OpenAPI, and no property, rate, availability, reservation, loyalty or folio surface is machine-readable anywhere. developer., developers., docs. and api. subdomains do not resolve; /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs all return 404, and mcp.wyndhamhotels.com resolves with a valid certificate but serves an Akamai 503 on every path. The Terms of Use (effective 2026-03-12) affirmatively prohibit robots, spiders, meta-searching and automated access, and separately prohibit automated access to Wyndham''s AI Search. What a second enrichment round did find on 2026-07-28 is undocumented CMS infrastructure that is nonetheless genuinely live: www.wyndhambusiness.com and development.wyndhamhotels.com both run WordPress on WP Engine and leave the WordPress REST API anonymously readable (309 and 403 registered routes, with JSON Schema
  available by HTTP OPTIONS), and three WordPress MCP adapter routes are registered across the two estates — one of them, on www.wyndhambusiness.com, bound to a real OAuth 2.1 authorization server with RFC 8414 and RFC 9728 discovery metadata, mandatory PKCE S256 and a single `mcp` scope, returning a standards-correct 401 bearer challenge to anonymous callers. None of it is documented, supported, or usable without a credential Wyndham issues to no third party, and none of it carries hotel data. The integration surface that matters is still reached only through a franchise agreement, a commercial distribution agreement, or Sabre.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wyndham-hotels.png
json_schemas:
- name: category
  property_count: 10
  slug: wyndham-hotels-wp-v2-categories
- name: comment
  property_count: 17
  slug: wyndham-hotels-wp-v2-comments
- name: attachment
  property_count: 33
  slug: wyndham-hotels-wp-v2-media
- name: page
  property_count: 26
  slug: wyndham-hotels-wp-v2-pages
- name: post
  property_count: 28
  slug: wyndham-hotels-wp-v2-posts
- name: search-result
  property_count: 5
  slug: wyndham-hotels-wp-v2-search
- name: status
  property_count: 8
  slug: wyndham-hotels-wp-v2-statuses
- name: tag
  property_count: 8
  slug: wyndham-hotels-wp-v2-tags
- name: taxonomy
  property_count: 11
  slug: wyndham-hotels-wp-v2-taxonomies
- name: type
  property_count: 16
  slug: wyndham-hotels-wp-v2-types
- name: user
  property_count: 19
  slug: wyndham-hotels-wp-v2-users
layout: provider
mcp_servers:
- description: ''
  name: wyndham-hotels-mcp.yml
  slug: wyndham-hotels-mcpyml
modified: '2026-07-28'
name: Wyndham Hotels & Resorts
nav: Providers
network: true
overview: 'Wyndham Hotels & Resorts publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United States, Hospitality, Hotels, and Booking.


  Wyndham Hotels & Resorts'' developer surface includes authentication, support, engineering blog, and 33 more developer resources.'
random_paper: 2
scopes:
- name: Wyndham Hotels Scopes
  scope_count: 1
  slug: wyndham-hotels-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: emerging
  composite: 23.8
  facets:
    commercial_clarity: 21.1
    contract_quality: 16.1
    developer_ergonomics: 26.1
    discoverability: 92.6
    governance: 3.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
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
