---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/century-21-canada-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/century-21-canada-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.c21.ca/
- group: company
  title: ''
  type: Blog
  url: https://www.c21.ca/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.c21.ca/feed
- group: operate
  title: ''
  type: PressReleases
  url: https://www.c21.ca/category/press-releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.c21.ca/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.c21.ca/privacy-policy
- group: other
  title: ''
  type: Sitemap
  url: https://www.c21.ca/sitemap.xml
- group: other
  title: ''
  type: PropertySearch
  url: https://www.c21.ca/search/
- group: other
  title: ''
  type: OfficeDirectory
  url: https://www.c21.ca/directory
- group: other
  title: ''
  type: CommercialListings
  url: https://www.c21.ca/commercial-listings
- group: other
  title: ''
  type: RegionalSite
  url: https://quebec.c21.ca/
- group: other
  title: ''
  type: FranchiseSales
  url: https://century21franchise.ca/
- group: company
  title: ''
  type: Careers
  url: https://join.c21.ca/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.c21.ca/contact
- group: start
  title: ''
  type: MemberPortal
  url: https://my.hub21.ca/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CENTURY21Canada
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/century21canada/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCK9uFomKQuOUR8sSKHe7yWQ
created: '2026-07-26'
description: 'CENTURY 21 Canada Limited Partnership is the Canadian master franchisor of the CENTURY 21® real estate brand, headquartered at 1285 West Pender Street in Vancouver, British Columbia. The master licence for Canada was secured in Vancouver in 1976 — the first international franchise of the CENTURY 21 System — and the network today spans roughly 400 independently owned and operated offices from coast to coast. Century 21 Canada sits in the brokerage/franchisor layer of the Canadian real estate value chain: it does not originate listing data, it consumes it. Canadian residential listings are consolidated nationally by the Canadian Real Estate Association (CREA), which runs REALTOR.ca and the Data Distribution Facility (DDF®); franchisors and brokerages redistribute that member-owned MLS® content under CREA rules rather than publishing it themselves. Century 21 Canada''s API posture is accordingly empty. As of a 2026-07-26 probe there is no developer portal, no API documentation,
  no published base URL, no SDK, no webhooks, no Postman collection and no machine-readable contract of any kind on century21.ca or c21.ca — both century21.ca and c21.ca resolve to the same WordPress consumer site whose terms of use name MoxiWorks LLC as the site operator, and whose property search is a hosted MoxiWorks Web Marketing System surface rather than a first-party API. Wildcard DNS on *.century21.ca and *.c21.ca returns HTTP 200 for every subdomain probed (developer., developers., api., docs.) by parking them all on eboat.moxiworks.com, so those 200s are a DNS artifact and not a developer portal. RESO is absent: no RESO Web API or Data Dictionary certification, no OData or $metadata endpoint, and no Universal Property Identifier reference appears anywhere in the public surface — consistent with Canada, where RESO certification is not the operative seam and CREA''s DDF® is. The only genuinely public, anonymously callable machine-readable surface found is the incidental WordPress
  REST API route index at https://www.c21.ca/wp-json/, which is a CMS artifact, is undocumented by Century 21 Canada, and is deliberately not listed here as a product API. Agent- and franchisee-facing tools live behind the hub21.ca member login. This profile is therefore identity-only and honestly records a brokerage franchisor with no published developer surface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/century-21-canada.png
layout: provider
modified: '2026-07-26'
name: Century 21 Canada
nav: Providers
network: true
overview: 'Century 21 Canada is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Brokerage, Franchising, and Property Listings.


  Century 21 Canada''s developer surface includes engineering blog, YouTube channel, and 18 more developer resources.'
random_paper: 28
score:
  band: minimal
  composite: 12.3
  delta: -2.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.3
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Century 21 Canada Domain Security
  slug: century-21-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: century-21-canada
tags:
- Real Estate
- Canada
- Brokerage
- Franchising
- Property Listings
- MLS
- Residential Real Estate
- Commercial Real Estate
- PropTech
website: https://www.c21.ca/
---
