---
access_model:
  confidence: high
  label: No published developer surface · contact only
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probes
  - website
  trial: false
  try_now: false
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
  url: security/savills-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.savills.com/
- group: company
  title: ''
  type: Website
  url: https://www.savills.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.savills.us/
- group: other
  title: ''
  type: PropertySearch
  url: https://search.savills.com/list
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.savills.com/
- group: other
  title: ''
  type: Research
  url: https://www.savills.com/insight-and-opinion/
- group: operate
  title: ''
  type: Contact
  url: https://www.savills.com/contact-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/savills
- group: other
  title: ''
  type: Subsidiary
  url: https://savillsim.com/
- group: company
  title: ''
  type: Blog
  url: https://www.savills.com/blog/
- group: company
  title: ''
  type: Blog
  url: https://www.savills.co.uk/blog/
- group: company
  title: ''
  type: News
  url: https://www.savills.com/news/
- group: company
  title: ''
  type: Careers
  url: https://www.savills.com/why-savills/careers.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.savills.com/footer/privacy-policy.aspx
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.savills.com/footer/terms-and-conditions.aspx
- group: other
  title: ''
  type: SiteMap
  url: https://www.savills.com/footer/site-map.aspx
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/savills-llms.txt
created: '2026-07-26'
description: 'Savills plc is a London-headquartered global real estate advisor, established in 1855, listed on the London Stock Exchange, with more than 42,000 people in over 70 countries. It sits on the advisory side of the property value chain rather than the data-platform side: commercial and prime residential agency, transaction advisory and capital markets, valuation and professional services, building and project consultancy, property and facilities management, rural and agricultural advisory, occupier services, the Savills Research publication programme, and a separate fund manager in Savills Investment Management. Its home market is the United Kingdom, where there is no MLS and no cooperative listing standard — residential stock reaches consumers through the Rightmove and Zoopla duopoly by way of agency CRM software (Reapit, Alto, Street, Apex27) rather than a shared cooperative pool. Savills is a supplier into that pipe, not an operator of it. Its API posture is the honest null
  case for this sector. Savills publishes no developer portal, no API documentation, no SDK, no Postman collection and no machine-readable contract of any kind: developer., developers., docs. and apis.savills.com do not resolve, /developers, /api, /docs, /openapi.json, /swagger.json and /api-docs on savills.com, savills.co.uk and savills.us all return 404, and no OpenID Connect discovery document is served. Undocumented internal service hosts do exist behind the consumer property search — livev6-searchapi, livev6-authentication and livev6-profile.savills.com, named in the search application''s own endpoints.js — but every one of them returns 404 to an anonymous client and none is described anywhere public. There is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in the Savills estate; RESO is a North American NAR/MLS construct and the UK has nothing to certify against. Savills publishes no open data either — its
  research output is PDF and web narrative, and the genuinely open UK property layer belongs to the public sector (HM Land Registry Price Paid Data and Ordnance Survey), not to the brokerage. For a developer there is no gate to pass, because there is no door: the only published route is the corporate contact form.'
image: https://www.savills.com/favicon-32x32.png
layout: provider
modified: '2026-07-26'
name: Savills
nav: Providers
network: true
overview: 'Savills is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United Kingdom, Commercial Real Estate, Property Listings, and Valuation.


  Savills'' developer surface includes engineering blog, product news, and 16 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 13.3
  delta: -1.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 68.5
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
  name: Savills Domain Security
  slug: savills-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: savills
tags:
- Real Estate
- United Kingdom
- Commercial Real Estate
- Property Listings
- Valuation
- Property Management
- Brokerage
- Rentals
- PropTech
- Investment Management
website: https://www.savills.com/
---
