---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Housesigma Agentic Access
  operation_count: 22
  slug: housesigma-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: The public, read-only WordPress REST API (wp/v2) behind housesigma.com/blog-en, which serves HouseSigma's Canadian housing-market analysis blog as JSON. This is the only anonymously callable, machine-
  name: HouseSigma Blog Content API
  slug: housesigma-blog-content-api
artifact_total: 11
collections:
- collection_type: open
  name: HouseSigma Blog Content API
  slug: open-housesigma-blog-content
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/housesigma-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/housesigma-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/housesigma-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/housesigma-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://housesigma.com/
- group: company
  title: ''
  type: Blog
  url: https://housesigma.com/blog-en/
- group: company
  title: ''
  type: BlogRSS
  url: https://housesigma.com/blog-en/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/housesigma
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/housesigma
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/housesigma-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/housesigma-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/housesigma-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/housesigma-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/housesigma-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/housesigma-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/housesigma-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/housesigma-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: Examples
  url: examples/
- group: other
  title: ''
  type: Overlay
  url: overlays/housesigma-blog-content-overlay.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://housesigma.com/blog-en/2018/04/25/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://housesigma.com/blog-en/2018/04/25/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://housesigma.com/blog-en/contact-us/
- group: operate
  title: ''
  type: FAQ
  url: https://housesigma.com/blog-en/faq/
- group: company
  title: ''
  type: About
  url: https://housesigma.com/blog-en/about-us/
- group: company
  title: ''
  type: Careers
  url: https://team.housesigma.com/
- group: other
  title: ''
  type: iOSApp
  url: https://itunes.apple.com/ca/app/toronto-real-estate-housesigma/id1255490256?mt=8
- group: other
  title: ''
  type: AndroidApp
  url: https://play.google.com/store/apps/details?id=com.housesigma.android&hl=en_CA
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/housesigma/
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/housesigma/
created: '2026-07-26'
description: 'HouseSigma, Inc. Brokerage is a Toronto-based Canadian residential real estate portal and licensed brokerage that pairs map-based MLS listing search with sold-price history and machine-learning home valuations (SigmaEstimate) across Ontario, British Columbia, and Alberta. It sits in the challenger layer of the Canadian value chain, below CREA, which operates REALTOR.ca and the national Data Distribution Facility (DDF) that syndicates member boards'' listings, and alongside Wahi, Zolo, and Properly, competing on visibility into data the boards control, a position it won in part through the Competition Bureau litigation that forced TRREB to release sold data in 2018. Its API posture is closed. There is no developer portal, no published API program, and no partner or data-licensing page; developer., developers., and docs.housesigma.com do not resolve in DNS, and /developers, /api, /api-docs, /openapi.json and /swagger.json all return the single-page-application shell rather than
  any contract. The listing, sold-history and valuation backend at housesigma.com/bkv2/api/ is private, keyless, undocumented, and explicitly disallowed to all crawlers in robots.txt. The one genuinely public, anonymously callable, machine-readable HTTP surface the company operates is the WordPress REST API behind housesigma.com/blog-en, which serves its Canadian housing-market analysis blog as JSON across 157 advertised routes; API Evangelist derived an OpenAPI for the 22 operations verified to answer anonymously. HouseSigma also publishes a real llms.txt and mobile deep-link association documents. RESO is absent: HouseSigma is not among the Canadian organizations RESO lists as members, and no Web API or Data Dictionary certification, OData $metadata document, or Universal Property Identifier usage was found. No open, unlicensed dataset is published. The underlying listing and sold data is board-licensed and reaches HouseSigma through its own brokerage membership, not through anything a
  third-party developer can sign up for.'
examples:
- key_count: 3
  name: Housesigma Blog Content Error 400 Rest_Invalid_Param
  slug: housesigma-blog-content-error-400-rest_invalid_param
- key_count: 3
  name: Housesigma Blog Content Error 401 Rest_Forbidden
  slug: housesigma-blog-content-error-401-rest_forbidden
- key_count: 3
  name: Housesigma Blog Content Error 404 Rest_Post_Invalid_Id
  slug: housesigma-blog-content-error-404-rest_post_invalid_id
- key_count: 12
  name: Housesigma Blog Content Getoembed 200
  slug: housesigma-blog-content-getOembed-200
- key_count: 4
  name: Housesigma Blog Content Listtaxonomies 200
  slug: housesigma-blog-content-listTaxonomies-200
image: https://housesigma.com/apple-touch-icon.png?v=2
layout: provider
mcp_servers:
- description: ''
  name: housesigma-mcp.yml
  slug: housesigma-mcpyml
modified: '2026-07-26'
name: HouseSigma
nav: Providers
network: true
overview: 'HouseSigma publishes 1 API on the [APIs.io](https://apis.io/) network: Blog Content API. Tagged areas include Real Estate, Canada, Property Listings, MLS, and Valuation.


  HouseSigma''s developer surface includes authentication, engineering blog, code examples, support, FAQ, and 25 more developer resources.'
random_paper: 6
score:
  band: thin
  composite: 33.2
  delta: -0.6
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 16.7
    contract_quality: 59.4
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 16.7
    operational_transparency: 2.6
  previous_composite: 33.8
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
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/housesigma/refs/heads/main/screenshots/housesigma-2026-08-07T170335.png
security:
- kind: authentication
  name: Housesigma Authentication
  slug: housesigma-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Housesigma Domain Security
  slug: housesigma-domain-security
  summary_line: TLSv1.3 · DMARC
slug: housesigma
tags:
- Real Estate
- Canada
- Property Listings
- MLS
- Valuation
- AVM
- PropTech
- Rentals
- Blog
- Content
- WordPress
- oEmbed
- Ontario
- British Columbia
- Toronto
website: https://housesigma.com/
---
