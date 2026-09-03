---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/skyscanner-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/skyscanner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skyscanner.net
- group: company
  title: ''
  type: Partners
  url: https://www.partners.skyscanner.net/
- group: other
  title: ''
  type: TravelAPI
  url: https://www.partners.skyscanner.net/product/travel-api
- group: other
  title: ''
  type: AffiliateProgramme
  url: https://www.partners.skyscanner.net/product/affiliates
- group: other
  title: ''
  type: DistributionNetwork
  url: https://www.partners.skyscanner.net/product/distribution
- group: docs
  title: ''
  type: DeveloperDocs
  url: https://developers.skyscanner.net/docs/intro
- group: other
  title: ''
  type: ApplyForTravelAPI
  url: https://www.partners.skyscanner.net/contact/travel-api
- group: start
  title: ''
  type: SupportPortal
  url: https://skyscannerpartnersupport.zendesk.com/hc/en-us/
- group: operate
  title: ''
  type: SelfServeHelpCentre
  url: https://www.partners.skyscanner.net/self-serve-help-centre
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Skyscanner
- group: other
  title: ''
  type: EngineeringPrinciples
  url: https://github.com/Skyscanner/engineering-principles
- group: other
  title: ''
  type: Backpack
  url: https://backpack.github.io/
- group: other
  title: ''
  type: Company
  url: https://www.skyscanner.net/media
- group: company
  title: ''
  type: Careers
  url: https://www.skyscanner.net/jobs
- group: other
  title: ''
  type: ParentCompany
  url: https://www.trip.com/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Skyscanner
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/skyscanner
created: '2026-05-25'
description: Skyscanner is an Edinburgh, Scotland–headquartered global travel marketplace that helps travellers compare flights, hotels, and car hire across hundreds of airlines, hotel providers, and online travel agents. Founded in 2003 and acquired by Trip.com Group (formerly Ctrip) in 2016, Skyscanner operates the consumer site skyscanner.net and a B2B partner programme that powers travel search experiences for third-party publishers and apps. The Skyscanner Travel APIs — Flights Live Prices, Flights Indicative Prices, Hotels Live Prices, Hotels Indicative Prices, Hotels Content, Hotels Reviews, Car Hire Live Prices, Car Hire Indicative Prices, Car Hire Agents, plus utility services for Culture, Geo, Autosuggest, and Carriers — are gated behind a partner application process and exposed only to approved partners with significant audience scale; full API documentation, base URLs, and OpenAPI specifications are published inside the partner portal rather than on the public developer site.
  Alongside the Travel APIs, Skyscanner runs an Affiliate Programme (commission on referred bookings) and a Distribution Network connecting airlines, hotel providers, car-hire suppliers, and OTAs to its 160M+ monthly users. Its public GitHub organisation is best known for the Backpack design system and for open-source infrastructure tooling such as cfripper and turbolift, rather than for SDKs against the Travel APIs.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/skyscanner.png
layout: provider
modified: '2026-05-30'
name: Skyscanner
nav: Providers
network: true
overview: 'Skyscanner is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Travel Search, Flights, Hotels, and Car Hire.


  Skyscanner''s developer surface includes GitHub presence and 18 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 5.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/skyscanner/refs/heads/main/screenshots/skyscanner-2026-06-20T194018.png
security:
- kind: domain-security
  name: Skyscanner Domain Security
  slug: skyscanner-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Skyscanner Vulnerability Disclosure
  slug: skyscanner-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: skyscanner
tags:
- Travel
- Travel Search
- Flights
- Hotels
- Car Hire
- Metasearch
- Affiliates
- Distribution
- Online Travel Agency
- Trip.com Group
website: https://www.skyscanner.net
---
