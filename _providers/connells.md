---
access_model:
  confidence: high
  label: No published developer surface · lender-panel and commercial integration only · an undocumented anonymous read-only JSON surface exists at www.connells.co.uk/api but is not offered, documented or supported
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probes
  - website
  trial: false
  try_now: false
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
    openapi_examples: partial
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Connells Agentic Access
  operation_count: 7
  slug: connells-agentic-access
  summary_line: 7 operations
api_count: 1
apis:
- description: An undocumented, unauthenticated, read-only JSON surface served by the Connells consumer website at https://www.connells.co.uk/api. It is NOT a published Connells Group product — the group publishes n
  name: Connells Website JSON API (undocumented)
  slug: connells-website-json-api-undocumented
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/connells-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/connells-domain-security.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/connells-website-openapi.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/connells-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/connells-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/connells-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/connells-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/connells-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/connells-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/connells-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.connellsgroup.co.uk/required-disclosures-inc-modern-slavery-act-statement/
- group: build
  title: ''
  type: Packages
  url: packages/connells-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/connells-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.connellsgroup.co.uk/legal-notices/
- group: company
  title: ''
  type: Website
  url: https://www.connellsgroup.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.connells.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.countrywide.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.hamptons.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.sequencehome.co.uk/
- group: company
  title: ''
  type: Website
  url: https://www.connells-surveyors.co.uk/
- group: other
  title: ''
  type: PropertySearch
  url: https://www.connells.co.uk/properties/sales
- group: other
  title: ''
  type: PropertySearch
  url: https://www.connells.co.uk/properties/lettings
- group: other
  title: ''
  type: Research
  url: https://www.connellsgroup.co.uk/research/our-data/
- group: company
  title: ''
  type: Blog
  url: https://www.connellsgroup.co.uk/news/
- group: operate
  title: ''
  type: Contact
  url: https://www.connellsgroup.co.uk/contact-us/
- group: company
  title: ''
  type: Careers
  url: https://www.connellsgroup.co.uk/careers/work-with-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.connellsgroup.co.uk/privacy-policy/
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.connellsgroup.co.uk/cookie-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/connells-group
- group: other
  title: ''
  type: ParentCompany
  url: https://www.skipton.co.uk/
created: '2026-07-26'
description: 'Connells Limited, trading as Connells Group, is the United Kingdom''s largest estate agency and property services group, headquartered at Cumbria House in Leighton Buzzard, Bedfordshire, and a wholly owned subsidiary of Skipton Building Society. It states 1,200+ branches, 16,000+ colleagues, more than 80 local brands including Connells, Countrywide, Hamptons, Sequence, Bairstow Eves, Fox & Sons, John D Wood & Co, Gascoigne Halman and Blundells, roughly 115,000 property sales a year and about 10% market share, 165,000+ managed tenancies and £33bn+ of arranged mortgage lending. It occupies almost the entire residential value chain at once: estate agency, residential and corporate lettings, new homes, land and planning, auctions, surveys and valuations, conveyancing, mortgage services, asset management, affordable housing, EPCs and inventories, commercial agency and a research and consultancy practice. Its home market is the United Kingdom, where there is no MLS and no cooperative
  listing standard — residential stock reaches consumers through the Rightmove and Zoopla portal duopoly by way of agency CRM and website software rather than a shared pool, and Connells'' own consumer property sites are built on the Homeflow platform. Its API posture is closed and undocumented. No developer portal exists: developer., developers., api. and docs.connellsgroup.co.uk do not resolve, and /developers, /api, /docs, /openapi.json, /swagger.json, /api-docs and /.well-known/openid-configuration return 404 on both connellsgroup.co.uk and connells.co.uk. It publishes no OpenAPI, no GraphQL, no AsyncAPI, no MCP server and no client SDK — the only first-party package on any public registry is a dormant npm colour-token file for its website. Probing on 2026-07-26 did, however, find a small live JSON surface underneath the consumer site at https://www.connells.co.uk/api: six anonymous read-only Next.js route handlers serving the branch finder, people directory, testimonials wall and place
  autocomplete, plus a seventh (/api/properties) that returns HTTP 500. These are undocumented internal website routes, not a product — unversioned, unsupported, rate limited by Cloudflare, capped at 12 records because no paging parameter works, and carrying application errors inside HTTP 200 bodies. Only connells.co.uk exposes them; the sibling brand sites redirect /api/* away. The group''s 88-URL corporate sitemap contains no developer path — its one /developers/ page is addressed to property developers, not software developers. Integration is real but partner-only: Connells Survey & Valuation advertises delivering "totally integrated panel and risk management technology solutions to lenders" for the 40+ lenders whose valuation panels it manages, and reaches them through third-party platforms such as Cotality''s LenderHub, while Countrywide Surveying Services'' Geoconnect engine is described as connecting internal and external data sources through API integrations it consumes rather than
  publishes. There is no RESO Web API or Data Dictionary certification, no OData $metadata document and no Universal Property Identifier anywhere in the estate — RESO is a North American NAR/MLS mechanism and the UK has no MLS to certify against. Connells publishes no open data either; its research product, covering 88% of UK postcode areas from branch-level proprietary data, is sold through a brochure request and a contact form, and the genuinely open UK property layer belongs to the public sector (HM Land Registry Price Paid Data and Ordnance Survey), not to the brokerage.'
examples:
- key_count: 2
  name: Connells Branch By Id Response
  slug: connells-branch-by-id-response
- key_count: 3
  name: Connells Branches Response
  slug: connells-branches-response
- key_count: 2
  name: Connells Places Search Response
  slug: connells-places-search-response
- key_count: 3
  name: Connells Staff Response
  slug: connells-staff-response
- key_count: 3
  name: Connells Testimonials Response
  slug: connells-testimonials-response
image: https://www.connellsgroup.co.uk/Assets/images/favicons/apple-icon-180x180.png
layout: provider
modified: '2026-07-26'
name: Connells Group
nav: Providers
network: true
overview: 'Connells Group publishes 1 API on the [APIs.io](https://apis.io/) network: Connells Website JSON API (undocumented). Tagged areas include Real Estate, United Kingdom, Property Listings, Brokerage, and Estate Agency.


  Connells Group''s developer surface includes code examples, authentication, engineering blog, and 29 more developer resources.'
random_paper: 50
rate_limits:
- limit_count: 0
  name: Connells Rate Limits
  slug: connells-rate-limits
score:
  band: emerging
  composite: 26.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 13.4
    developer_ergonomics: 14.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 26.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/connells/refs/heads/main/screenshots/connells-2026-08-07T163756.png
security:
- kind: authentication
  name: Connells Authentication
  slug: connells-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Connells Domain Security
  slug: connells-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: connells
tags:
- Real Estate
- United Kingdom
- Property Listings
- Brokerage
- Estate Agency
- Rentals
- Valuation
- Conveyancing
- Mortgage
- Property Management
- Auctions
- PropTech
website: https://www.connellsgroup.co.uk/
---
