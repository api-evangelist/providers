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
    well_known_catalog: true
  schema_version: 0.2
  score: 3.6
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/flight-centre-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.fctgl.com/
- group: other
  title: ''
  type: Brands
  url: https://www.fctgl.com/brands
- group: company
  title: ''
  type: InvestorRelations
  url: https://www.fctgl.com/investors
- group: company
  title: ''
  type: News
  url: https://www.fctgl.com/news
- group: other
  title: ''
  type: Locations
  url: https://www.fctgl.com/global-locations
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fctgl.com/privacy-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fcmtravel.com/en/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.flightcentre.com.au/s/article/terms-of-use-au
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.flightcentre.com.au/s/article/booking-terms-conditions-au
- group: operate
  title: ''
  type: Support
  url: https://help.flightcentre.com.au/s/
- group: company
  title: ''
  type: Blog
  url: https://www.fcmtravel.com/en-us/resources/news-hub
- group: company
  title: ''
  type: About
  url: https://www.fctgl.com/about
- group: company
  title: ''
  type: Careers
  url: https://www.fctgcareers.com/
- group: other
  title: ''
  type: Cookies
  url: https://www.fctgl.com/cookies-policy
- group: other
  title: ''
  type: DataPortability
  url: https://privacyportal-de.onetrust.com/webform/01c95262-28d1-4b76-89f7-6b0b650d1af2/d036c47c-47be-4cb7-be63-5a65a9cc5f0d
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/flight-centre
- group: docs
  title: ''
  type: Documentation
  url: https://www.fcmtravel.com/en-us/llm-info
- group: docs
  title: ''
  type: Documentation
  url: https://www.corporatetraveler.us/en-us/llm-info
- group: docs
  title: ''
  type: Documentation
  url: https://www.fcmtravel.com/en/travel-insights/our-approach-ndc
- group: auth
  title: ''
  type: Certification
  url: https://www.fcmtravel.com/en/resources/news-hub/fcm-is-first-global-tmc-to-achieve-iata-ndc-level-4-certification
- group: docs
  title: ''
  type: Documentation
  url: https://tpconnects.com/iris-travel-seller-solutions/iris-api/
- group: design
  title: ''
  type: Conformance
  url: conformance/flight-centre-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/flight-centre-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/flight-centre-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/flight-centre-llms.txt
- group: other
  title: ''
  type: Research
  url: mcp/flight-centre-mcp.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-07-28'
description: Flight Centre Travel Group (ASX FLT) is a Brisbane-headquartered travel retailer and corporate travel manager, one of the largest agency groups in the world and by far the largest in its home market of Australia. It operates more than thirty brands across leisure retail (Flight Centre, Travel Associates, Cruiseabout, Aunt Betty, BYOjet, Envoyage, Scott Dunn, StudentUniverse), corporate travel management (FCM, Corporate Traveller, Stage and Screen, FCM Consulting) and wholesale supply (Discova, Infinity Holidays, Topdeck, Backroads Touring, TPConnects), with company-owned operations in twenty-four countries and licensed operations in roughly ninety more. Structurally it sits on the demand side of the travel distribution chain - it is an aggregator-reseller that buys airline, hotel, cruise and land content through the GDSs (Sabre and Amadeus), through NDC aggregators, and through direct supplier agreements, and resells it to consumers and corporate travel programmes. Its API posture
  is honestly assessed as none published - Flight Centre Travel Group operates no developer portal, publishes no API reference, no OpenAPI, and no partner API documentation on any of its brand domains, and probing developer, developers, docs and api subdomains of fctgl.com, fcmtravel.com and flightcentre.com.au returns no DNS record at all. The group's genuine machine-readable distribution asset is TPConnects, the Dubai NDC aggregator it holds a majority stake in, whose Iris and Astra APIs are described on public product pages but whose reference documentation sits behind a ReadMe login. Flight Centre and FCM were the first global travel management company to receive IATA NDC Level 4 certification for full offer and order management, yet no public NDC endpoint is exposed. There is no self-serve access gate and no bulk export - the only documented exit path is a personal-data subject access request through a OneTrust web form.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Flight Centre Travel Group
nav: Providers
network: true
overview: 'Flight Centre Travel Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Australia, Corporate Travel, Travel Agency, and Distribution.


  Flight Centre Travel Group''s developer surface includes product news, support, engineering blog, documentation, and 24 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 15.6
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: domain-security
  name: Flight Centre Domain Security
  slug: flight-centre-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: flight-centre
tags:
- Travel
- Australia
- Corporate Travel
- Travel Agency
- Distribution
- NDC
- Aviation
- Booking
- Hotels
- Aggregator
website: https://www.fctgl.com/
---
