---
access_model:
  confidence: medium
  label: Free · Requires approval
  onboarding: approval
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-04'
api_count: 5
apis:
- description: Zillow Web Services were the legacy public XML-based APIs from Zillow including GetSearchResults, GetZestimate, GetDeepSearchResults, GetUpdatedPropertyDetails, GetComps, GetRegionChildren, and the Ne
  name: Zillow Web Services (Historical / Sunset)
  slug: zillow-web-services-historical
- description: Bridge Interactive is Zillow Group's RESO-compliant data distribution platform for MLSs, brokers, and approved vendors. It exposes a RESO Web API (OData-based) for searching listings, members, offices
  name: Bridge Interactive API
  slug: bridge-interactive-api
- description: Zillow Tech Connect is the partner program that lets approved real-estate software vendors integrate with Zillow Premier Agent for contact, lead, and listing sync. Vendors are vetted and onboarded dir
  name: Zillow Tech Connect
  slug: zillow-tech-connect
- description: 'Mortech is Zillow Group''s mortgage pricing and product eligibility engine for lenders and partners. It exposes web services for real-time rate quotes, scenario pricing, and product and pricing engine '
  name: Mortech API
  slug: mortech-api
- description: Zillow Showcase is a premium listing enhancement product for agents and MLSs that integrates immersive media (interactive floor plans, virtual tours, AI-enhanced photography) into Zillow listings. Int
  name: Zillow Showcase
  slug: showcase-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zillow-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zillow.com
- group: other
  title: ''
  type: ParentCompany
  url: https://www.zillowgroup.com
- group: start
  title: ''
  type: Portal
  url: https://www.zillowgroup.com/developers
- group: start
  title: ''
  type: Portal
  url: https://bridgedataoutput.com
- group: docs
  title: ''
  type: Documentation
  url: https://bridgedataoutput.com/docs/platform/
- group: company
  title: ''
  type: Partners
  url: https://www.zillowgroup.com/tech-connect/
- group: other
  title: ''
  type: Subsidiary
  url: https://www.mortech-inc.com
- group: other
  title: ''
  type: Product
  url: https://www.zillow.com/z/showcase/
- group: company
  title: ''
  type: Blog
  url: https://www.zillow.com/blog/
- group: other
  title: ''
  type: Research
  url: https://www.zillow.com/research/
- group: company
  title: ''
  type: Newsroom
  url: https://www.zillowgroup.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zillowgroup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zillow.com/z/corp/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zillow.com/z/corp/privacy/
- group: operate
  title: ''
  type: Support
  url: https://zillow.zendesk.com/hc/en-us
- group: other
  title: ''
  type: X
  url: https://x.com/zillow
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Zillow
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zillow
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/zillow
created: '2024-01-01'
description: Zillow is the largest U.S. real-estate marketplace, offering home and rental listings, Zestimate home value estimates, mortgage tools, and a connected agent and lender ecosystem. Zillow Group owns Trulia, StreetEasy, HotPads, Out East, Bridge Interactive, Mortech, Showcase, and ShowingTime+. Zillow sunset its legacy public consumer APIs (Zillow Web Services, the GetSearchResults / GetZestimate / Property Details APIs and the Mortgage APIs) on September 30, 2021. Programmatic access to Zillow Group listing, broker, and lender data is now delivered through Bridge Interactive (bridgedataoutput.com) for licensed real-estate professionals and MLSs, the Zillow Tech Connect partner program for vendors, Mortech for mortgage pricing, and the Showcase listing enhancement product. This profile documents what is publicly findable on each surviving API surface.
finops:
- name: Zillow Finops
  service_category: API
  slug: zillow-finops
graphqls:
- description: This is a conceptual GraphQL schema for the Zillow real estate search and data platform. Zillow is the largest U.S. real-estate marketplace, offering home and rental listings, Zestimate home value est
  name: Zillow GraphQL Schema
  slug: zillow-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zillow.png
layout: provider
modified: '2026-05-23'
name: Zillow
nav: Providers
network: true
overview: 'Zillow publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bridge, Brokers, IDX, Lenders, and Listings.


  Zillow''s developer surface includes developer portal, documentation, engineering blog, support, and 16 more developer resources.'
plans:
- name: Zillow Plans Pricing
  plan_count: 1
  slug: zillow-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Zillow Rate Limits
  slug: zillow-rate-limits
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 16.7
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 43.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zillow/refs/heads/main/screenshots/zillow-2026-06-20T201903.png
security:
- kind: domain-security
  name: Zillow Domain Security
  slug: zillow-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zillow
tags:
- Bridge
- Brokers
- IDX
- Lenders
- Listings
- Mortgage
- MLS
- Real-Estate
- Rentals
- RESO
website: https://www.zillow.com
---
