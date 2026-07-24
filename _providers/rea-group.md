---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 16.3
  scored_at: '2026-07-23'
api_count: 5
apis:
- description: 'Retrieves data on a specific property - attributes, history, and property reports - drawn from PropTrack''s property dataset behind realestate.com.au. Access is partner-gated and authenticated via REA '
  name: PropTrack Properties API
  slug: proptrack-properties-api
- description: Address match and address suggest endpoints that resolve free-text or partial addresses to canonical Australian property records, with structured address match noted as coming soon. Partner-gated.
  name: PropTrack Address API
  slug: proptrack-address-api
- description: PropTrack's Automated Valuation Model (AVM) and valuation endpoints return estimated property values and confidence ranges used across banking, broking, and valuation workflows. Access is partner-gate
  name: PropTrack Valuations API (AVM)
  slug: proptrack-valuations-api
- description: Listing details, listing history, and listings search by point and radius, plus sold transactions search by point and radius, exposing for-sale and sold listing data from realestate.com.au. Partner-ga
  name: PropTrack Listings API
  slug: proptrack-listings-api
- description: Suburb-level market statistics including sale insights, rent insights, best value insights, and economic reports for researching property market trends across Australia. Partner-gated.
  name: PropTrack Market API
  slug: proptrack-market-api
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.rea-group.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.proptrack.com.au/docs/apis/home
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.proptrack.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/realestate-com-au
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rea-group/
- group: other
  title: ''
  type: X
  url: https://twitter.com/REA_Group
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/channel/UCfLcFXAN3pjad2aCzUNhUaA
- group: company
  title: ''
  type: Blog
  url: https://www.rea-group.com/about-us/news-and-insights/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.proptrack.com.au/docs/apis/home
- group: operate
  title: ''
  type: Support
  url: https://www.proptrack.com.au/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rea-group.com/privacy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/rea-group-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/rea-group-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/rea-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rea-group-lifecycle.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rea-group-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/rea-group-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rea-group-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/rea-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rea-group.com/security
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/rea-group-llms.txt
created: '2026-07-20'
description: REA Group Limited is an ASX-listed (ASX:REA) digital real estate advertising business headquartered in Melbourne, Australia and majority-owned by News Corp. It operates realestate.com.au and realcommercial.com.au, the property data and analytics brand PropTrack, the Mortgage Choice broking network, and REA India (Housing.com, PropTiger, and Makaan). REA Group's public developer surface is delivered through PropTrack, whose developer portal documents a suite of property data APIs - address matching, automated valuations (AVM), property and listing data, sold transactions, and suburb-level market insights - sourced from Australia's largest real estate portal. The APIs are documented publicly but are partner-gated; access requires a commercial agreement, and the data endpoints are authenticated via REA Group's OAuth identity service rather than being self-serve.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rea-group.png
layout: provider
modified: '2026-07-20T12:00:00Z'
name: REA Group
nav: Providers
network: true
overview: 'REA Group publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real Estate, Property Data, Valuations, Market Insights, and Listings.


  REA Group''s developer surface includes documentation, YouTube channel, engineering blog, API reference, support, authentication, and 15 more developer resources.'
random_paper: 47
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 41.3
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 22.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: authentication
  name: Rea Group Authentication
  slug: rea-group-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Rea Group Domain Security
  slug: rea-group-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rea Group Vulnerability Disclosure
  slug: rea-group-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rea-group
tags:
- Real Estate
- Property Data
- Valuations
- Market Insights
- Listings
- PropTech
- Australia
website: https://www.rea-group.com/
---
