---
access_model:
  confidence: high
  label: No published API programme · Listing data licensed through CREA/boards
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - probes
  - terms-of-use
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.8
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: The only anonymously reachable, machine-readable API surface found anywhere in the RE/MAX Canada estate. blog.remax.ca is a WordPress VIP site (CNAME remax-promotions.go-vip.net) that serves the stock
  name: RE/MAX Canada Blog WordPress REST API
  slug: re-max-canada-blog-wordpress-rest-api
artifact_total: 4
collections:
- collection_type: open
  name: API Collection
  slug: open-re-max-canada-blog-wp-json-index
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/re-max-canada-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/re-max-canada-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/re-max-canada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/re-max-canada-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/re-max-canada-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/re-max-canada-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/re-max-canada-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.remax.ca/
- group: company
  title: ''
  type: Website
  url: https://www.remax.ca/fr/
- group: company
  title: ''
  type: Blog
  url: https://blog.remax.ca/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.remax.ca/feed/
- group: company
  title: ''
  type: Website
  url: https://franchise.remax.ca/
- group: company
  title: ''
  type: Website
  url: https://join.remax.ca/
- group: company
  title: ''
  type: Website
  url: https://agentbrokerhub.remax.ca/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.remax.ca/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blog.remax.ca/privacy-notice/
- group: company
  title: ''
  type: Website
  url: https://www.remax.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/remax-canada
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/remaxcanada
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/remaxcanada/
created: '2026-07-26'
description: 'RE/MAX Canada is the Canadian arm of RE/MAX, LLC, operating the remax.ca consumer portal in English and French and franchising RE/MAX brokerages across the country. Since RE/MAX Holdings closed its USD 235 million purchase of the RE/MAX INTEGRA North America regions on 2021-07-21, the Ontario-Atlantic and Western Canada regions are company-owned regions of RE/MAX, LLC, folded into RE/MAX Canada; Quebec is served separately and remax.ca robots.txt explicitly disallows /qc and /quebec. Its home market is Canada, and it sits in the value chain as a brokerage franchisor and consumer portal operator rather than as a data owner. Canadian residential listing content is cooperatively controlled by CREA and the member boards through REALTOR.ca and the Data Distribution Facility, so RE/MAX Canada displays MLS content it licenses rather than publishes; the remax.ca footer carries CREA''s MLS trademark notice, and the site''s home price estimates are supplied by Teranet Inc. under a personal-use-only
  licence that forbids commercial use, resale, external distribution and sublicensing even though Teranet''s own inputs derive from public records collected by the Province of Ontario, the Province of Manitoba and the British Columbia Assessment Authority. Its API posture is recorded here honestly: there is no developer portal, no published API programme, no OpenAPI, Swagger, GraphQL or OData $metadata document, and no RESO Web API or Data Dictionary certification — a case-insensitive search of the full RESO certification directory returns zero RE/MAX matches, while 30 Canadian boards and pooled platforms do appear there. developer.remax.ca, developers.remax.ca and docs.remax.ca are wildcard DNS artifacts pointing at the kvCORE platform, proven by a control probe; api.remax.ca is a real AWS load balancer that 301-redirects every path to www.remax.ca; and the remax.ca terms of use prohibit crawlers, scripts and other automated devices outright. The only anonymously callable machine-readable
  RE/MAX Canada surface found is the default WordPress REST API on its WordPress VIP-hosted blog — content, not property data.'
image: https://static-images.remax.ca/next-assets/open-graph-logo/REMAX_Residential_og.png
layout: provider
modified: '2026-07-26'
name: RE/MAX Canada
nav: Providers
network: true
overview: 'RE/MAX Canada publishes 1 API on the [APIs.io](https://apis.io/) network: Blog WordPress REST API. Tagged areas include Real Estate, Canada, Brokerage, Property Listings, and MLS.


  RE/MAX Canada''s developer surface includes authentication, engineering blog, and 18 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 32.3
    developer_ergonomics: 13.0
    discoverability: 75.9
    governance: 3.1
    operational_transparency: 0.0
  previous_composite: 25.7
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 41.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Re Max Canada Authentication
  slug: re-max-canada-authentication
  summary_line: http · 3 schemes
- kind: domain-security
  name: Re Max Canada Domain Security
  slug: re-max-canada-domain-security
  summary_line: TLSv1.3 · DMARC
slug: re-max-canada
tags:
- Real Estate
- Canada
- Brokerage
- Property Listings
- MLS
- RESO
- IDX
- PropTech
- Land Registry
- Valuation
- Rentals
- Franchising
website: https://www.remax.ca/
---
