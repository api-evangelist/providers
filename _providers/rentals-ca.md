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
api_count: 3
apis:
- description: REST API described on the public Rentsync Partners portal (branded "LIFT System API") as giving partners "access to the underlying data structures of the LIFT System" with "detailed Canadian rental in
  name: Rentsync Partners REST API
  slug: rentsync-partners-rest-api
- description: Ad syndication API described on the public Rentsync Partners portal as programming interfaces used to "interact with rental industry professionals using Rentsync's Ad Syndication to manage their onlin
  name: Rentsync Ad Syndication API
  slug: rentsync-ad-syndication-api
- description: Search API described on the public Rentsync Partners portal as a way to "query the LIFT platform for specific information", positioned by the vendor as "a great way to get data for mapping application
  name: Rentsync Search API
  slug: rentsync-search-api
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rentals-ca-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rentals.ca/
- group: start
  title: ''
  type: Portal
  url: https://partners.rentsync.ca/
- group: start
  title: ''
  type: Signup
  url: https://partners.rentsync.ca/users/sign_up
- group: start
  title: ''
  type: Login
  url: https://partners.rentsync.ca/users/sign_in
- group: operate
  title: ''
  type: StatusPage
  url: https://status.rentals.ca/
- group: company
  title: ''
  type: Blog
  url: https://rentals.ca/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://ca.linkedin.com/company/rentals.ca
- group: company
  title: ''
  type: Website
  url: https://rentsync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rentsync.com/integrations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rentsync.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rentsync.com/terms-of-use
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rentals-ca-llms.txt
created: '2026-07-26'
description: 'Rentals.ca is a Toronto-headquartered residential rental marketplace and the flagship brand of the Rentals.ca Network, which also operates Rentfaster.ca, Louer.ca, Rentboard.ca, RentCanada.com and TorontoRentals.com across more than 100 Canadian cities. The network is owned and operated by Rentsync (formerly Landlord Web Solutions Inc.), which also acquired the research firm Urbanation in January 2026 and co-publishes the monthly Rentals.ca / Urbanation National Rent Report; Rentals.ca listing data also feeds a Statistics Canada rental housing index. In the Canadian real estate value chain it sits on the rentals side of the market, outside CREA''s REALTOR.ca and Data Distribution Facility, which syndicate member boards'' for-sale listings. Its API posture is honest but closed: rentals.ca itself publishes no developer portal, no OpenAPI, and no documented public endpoint, and the entire consumer site sits behind a Cloudflare managed challenge that returns HTTP 403 to anonymous
  clients. The real developer surface belongs to the parent, at the Rentsync Partners portal (partners.rentsync.ca, branded "LIFT System API"), which publicly names a REST API, an Ad Syndication API and a Search API but places all documentation behind an account whose registration form requires a written application explaining what you intend to build. There is no RESO Web API or Data Dictionary certification, no OData $metadata document, no Universal Property Identifier, and no open dataset published by the company.'
image: https://rentals.ca/static/fe/img/favicon/apple-touch-icon.png
layout: provider
modified: '2026-07-26'
name: Rentals.ca
nav: Providers
network: true
overview: 'Rentals.ca publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Canada, Rentals, Property Listings, and Rental Marketplace.


  Rentals.ca''s developer surface includes developer portal, signup flow, engineering blog, documentation, and 9 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 20.5
  delta: -2.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 23.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Rentals Ca Domain Security
  slug: rentals-ca-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rentals-ca
tags:
- Real Estate
- Canada
- Rentals
- Property Listings
- Rental Marketplace
- PropTech
- Listing Syndication
- Market Data
website: https://rentals.ca/
---
