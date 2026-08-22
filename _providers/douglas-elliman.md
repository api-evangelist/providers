---
access_model:
  confidence: high
  label: No published developer access
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/douglas-elliman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.elliman.com/
- group: company
  title: ''
  type: About
  url: https://www.elliman.com/about-us
- group: company
  title: ''
  type: InvestorRelations
  url: https://investors.elliman.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.elliman.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.elliman.com/privacy-policy
- group: other
  title: ''
  type: SiteMap
  url: https://www.elliman.com/site-map
- group: company
  title: ''
  type: Press
  url: https://www.elliman.com/press-news
- group: company
  title: ''
  type: Careers
  url: https://www.elliman.com/careers
- group: other
  title: ''
  type: Research
  url: https://www.elliman.com/corporate-resources/market-reports
- group: other
  title: ''
  type: Research
  url: https://www.elliman.com/corporate-resources/research-reports
- group: docs
  title: ''
  type: Guides
  url: https://www.elliman.com/sellers-buyers-renters-guides
- group: company
  title: ''
  type: Blog
  url: https://www.elliman.com/insider
- group: operate
  title: ''
  type: Contact
  url: https://www.elliman.com/offices
- group: design
  title: ''
  type: Conformance
  url: conformance/douglas-elliman-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/douglas-elliman-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/douglas-elliman-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DouglasElliman
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/douglaselliman/
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/DouglasElliman
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/douglaselliman/
created: '2026-07-26'
description: 'Douglas Elliman Inc. (NYSE: DOUG) is a residential real estate brokerage founded in 1911 and headquartered at 575 Madison Avenue, New York City. It is one of the largest brokerages in the New York metropolitan area and among the largest in the United States, with roughly 6,000 agents across New York, Florida, California, Texas, Colorado, Massachusetts, Connecticut, Nevada, New Jersey, Vermont, the Mid-Atlantic, and international outposts in France and Monaco. Its home market is the United States. In the value chain Douglas Elliman sits on the SELL side as a licensed brokerage and MLS participant — it consumes MLS listing data under IDX and broker agreements rather than originating a syndicated feed — and it extends into development marketing, property management, commercial brokerage, title and escrow (Douglas Elliman Title), relocation, and PropTech venture investment through New Valley Ventures. Its API posture is honest and thin: no developer portal, no published API documentation,
  no OpenAPI or OData $metadata contract, and no published access path of any kind. developer.elliman.com, developers.elliman.com, and docs.elliman.com all resolve to the marketing homepage via a wildcard catch-all rather than to a portal, and api.elliman.com exists as an IIS/ASP.NET host that returns HTTP 403 at its root with no documentation behind it. On RESO, Douglas Elliman Real Estate is listed as a Class D member (Brokers, Agents and Appraisers) on the RESO membership roster but does NOT appear in the RESO certified-organizations directory — it is a RESO member, not a RESO-certified data provider, and it publishes no Web API or Data Dictionary certification, no OData endpoint, and no UPI surface. The single public engineering artifact the company ships is a GitHub fork of a third-party .NET RETS client library, which is consumer-side evidence that Elliman pulls MLS data in rather than producer-side evidence that it exposes any.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/douglas-elliman.png
layout: provider
modified: '2026-07-26'
name: Douglas Elliman
nav: Providers
network: true
overview: 'Douglas Elliman is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, United States, Brokerage, Property Listings, and MLS.


  Douglas Elliman''s developer surface includes engineering blog and 20 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 12.4
  delta: -3.1
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 15.5
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 31.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/douglas-elliman/refs/heads/main/screenshots/douglas-elliman-2026-08-07T164508.png
security:
- kind: domain-security
  name: Douglas Elliman Domain Security
  slug: douglas-elliman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: douglas-elliman
tags:
- Real Estate
- United States
- Brokerage
- Property Listings
- MLS
- IDX
- RESO
- Rentals
- Commercial Real Estate
- Property Management
- Title
- Escrow
- PropTech
- Luxury Real Estate
- New Development
website: https://www.elliman.com/
---
