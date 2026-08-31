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
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.5
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Hopper Com Agentic Access
  operation_count: 23
  slug: hopper-com-agentic-access
  summary_line: 23 operations · 18 acting
api_count: 1
apis:
- description: In order to measure and continuously improve HTS Ancillaries performance, specific events occurring during a customer session can be sent by the partner airlines using some dedicated endpoints.
  name: Hopper Analytics API
  slug: hopper-com-analytics-api
- description: This API is authenticated with OAuth 2, Client Credentials grant.\ Clients should use their `client_id` and `client_secret` to obtain an `access_token`.\ The `access_token` should be included in every
  name: Hopper Authentication API
  slug: hopper-com-authentication-api
- description: '**What is Cancel For Any Reason?** Cancel For Any Reason (CFAR) enables airlines to offer refundability as an ancillary with HTS powering the dynamic pricing and supporting the refund cost. **** **How'
  name: Hopper Cancel For Any Reason (CFAR) API
  slug: hopper-com-cancel-for-any-reason-cfar-api
- description: '**What is Disruption Guarantee?** Disruption Guarantee (DG) offers a premium disruption assistance service to customers in case of flight disruption, including rebooking options on any airline or a re'
  name: Hopper Disruption Guarantee (DG) API
  slug: hopper-com-disruption-guarantee-dg-api
- description: Hopper uses a unique ID to correlate API calls and events produced by a user's interaction with an airline application. The duration of the user's interactions is called a "session", and the correlati
  name: Hopper Sessions API
  slug: hopper-com-sessions-api
artifact_total: 15
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Airline API
  slug: open-hopper-airlines
- collection_type: open
  name: Airline Analytics API
  slug: open-hopper-com-analytics-api
- collection_type: open
  name: Airline Analytics Authentication API
  slug: open-hopper-com-authentication-api
- collection_type: open
  name: Airline Analytics Cancel For Any Reason (CFAR) API
  slug: open-hopper-com-cancel-for-any-reason-cfar-api
- collection_type: open
  name: Airline Analytics Disruption Guarantee (DG) API
  slug: open-hopper-com-disruption-guarantee-dg-api
- collection_type: open
  name: Airline Analytics Sessions API
  slug: open-hopper-com-sessions-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hopper-com-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hopper-com-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hopper-com-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.hopper.com
- group: other
  title: ''
  type: B2B
  url: https://hts.hopper.com
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/cancel-for-any-reason
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/disruption-assistance-for-any-reason
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/hts-stays
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/hts-cars
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/hts-packages
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/travel-loyalty-portals
- group: other
  title: ''
  type: Product
  url: https://hts.hopper.com/hts-assist
- group: other
  title: ''
  type: Company
  url: https://www.hopper.com/about
- group: company
  title: ''
  type: Press
  url: https://www.hopper.com/press
- group: company
  title: ''
  type: Careers
  url: https://www.hopper.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://hts.hopper.com/contact
- group: build
  title: ''
  type: GitHub
  url: https://github.com/hopper
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hopper
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hopper
- group: company
  title: ''
  type: Blog
  url: https://hts.hopper.com/newsroom
created: '2026-05-25'
description: Hopper is a Boston- and Montreal-based travel booking platform and B2B travel fintech provider serving more than 120 million travelers globally. Its consumer app aggregates flights, hotels, rental cars, and homes alongside proprietary price prediction and a family of "for any reason" fintech ancillaries — Price Freeze, Cancel For Any Reason (CFAR), Change For Any Reason, Leave For Any Reason, and Disruption Guarantee. Through its B2B division, Hopper Technology Solutions (HTS), the company licenses those same fintech ancillaries, agentic AI customer service (HTS Assist), white-label travel agency products (HTS Stays, HTS Cars, HTS Packages), and travel loyalty portals to airlines, banks, and travel providers. HTS exposes a documented OAuth2-secured REST API — the HTS Airline API v1.1 — for embedding CFAR and Disruption Guarantee contracts in airline booking flows, with OpenAPI-generated SDKs for Java, .NET, Angular, and iOS, plus a JavaScript SDK for hotel price-freeze integration.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hopper-com.png
layout: provider
modified: '2026-05-25'
name: Hopper
nav: Providers
network: true
overview: 'Hopper publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Authentication API, Cancel For Any Reason (CFAR) API, and 2 more. Tagged areas include Travel, Travel Fintech, Price Prediction, Cancel For Any Reason, and Disruption Guarantee.


  Hopper''s developer surface includes authentication, GitHub presence, engineering blog, and 17 more developer resources.'
random_paper: 10
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 55.8
    developer_ergonomics: 40.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 30.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hopper-com/refs/heads/main/screenshots/hopper-com-2026-06-20T182832.png
security:
- kind: authentication
  name: Hopper Com Authentication
  slug: hopper-com-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Hopper Com Domain Security
  slug: hopper-com-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: hopper-com
tags:
- Travel
- Travel Fintech
- Price Prediction
- Cancel For Any Reason
- Disruption Guarantee
- Price Freeze
- Airlines
- Hotels
- Car Rental
- Vacation Rentals
- Ancillary Revenue
- B2B
- Loyalty
- Agentic AI
website: https://www.hopper.com
---
