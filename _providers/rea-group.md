---
access_model:
  confidence: high
  label: Partner-gated, commercial agreement required; public mock servers
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.proptrack.com.au/docs/apis/api-trials
  - https://developer.proptrack.com.au/docs/apis/how-to-authenticate
  - plans/rea-group-plans.yml
  - sandbox/rea-group-sandbox.yml
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rea Group Agentic Access
  operation_count: 32
  slug: rea-group-agentic-access
  summary_line: 32 operations · 5 acting
api_count: 9
apis:
- description: REA Group's REAXML listing feed - the long-standing industry-standard XML property schema used by Australian agency CRMs to publish residential and commercial for-sale and for-rent listings onto reale
  name: realestate.com.au Listing Feed (REAXML)
  slug: realestate-listing-feed-reaxml
- description: The realestate.com.au Partner Portal is REA Group's integration surface for agencies and their software / CRM providers - covering partner onboarding, API credential management (Client ID + API secret
  name: realestate.com.au Partner Portal
  slug: realestate-partner-portal
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Attributes
  name: REA Group Attributes API
  slug: rea-group-attributes-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Auction Results API from REA Group — 1 operation(s) for auction results.
  name: REA Group Auction Results API
  slug: rea-group-auction-results-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: AVM
  name: REA Group AVM API
  slug: rea-group-avm-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The AVM Report API from REA Group — 1 operation(s) for avm report.
  name: REA Group AVM Report API
  slug: rea-group-avm-report-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Demographics API from REA Group — 1 operation(s) for demographics.
  name: REA Group Demographics API
  slug: rea-group-demographics-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Disclaimers API from REA Group — 1 operation(s) for disclaimers.
  name: REA Group Disclaimers API
  slug: rea-group-disclaimers-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Listing by listingId API from REA Group — 1 operation(s) for listing by listingid.
  name: REA Group Listing by listingId API
  slug: rea-group-listing-by-listingid-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Listings
  name: REA Group Listings API
  slug: rea-group-listings-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Match API from REA Group — 1 operation(s) for match.
  name: REA Group Match API
  slug: rea-group-match-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Oauth2 API from REA Group — 1 operation(s) for oauth2.
  name: REA Group Oauth2 API
  slug: rea-group-oauth2-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Planning Overlays
  name: REA Group Planning API
  slug: rea-group-planning-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Point & Radius Search API from REA Group — 2 operation(s) for point & radius search.
  name: REA Group Point & Radius Search API
  slug: rea-group-point-radius-search-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Property Report API from REA Group — 1 operation(s) for property report.
  name: REA Group Property Report API
  slug: rea-group-property-report-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Rent History API from REA Group — 1 operation(s) for rent history.
  name: REA Group Rent History API
  slug: rea-group-rent-history-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Sale History API from REA Group — 1 operation(s) for sale history.
  name: REA Group Sale History API
  slug: rea-group-sale-history-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Schools API from REA Group — 1 operation(s) for schools.
  name: REA Group Schools API
  slug: rea-group-schools-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Search
  name: REA Group Search API
  slug: rea-group-search-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Suburb & Postcode Search API from REA Group — 2 operation(s) for suburb & postcode search.
  name: REA Group Suburb & Postcode Search API
  slug: rea-group-suburb-postcode-search-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Suggest API from REA Group — 1 operation(s) for suggest.
  name: REA Group Suggest API
  slug: rea-group-suggest-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Summary
  name: REA Group Summary API
  slug: rea-group-summary-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: The Supply & Demand API from REA Group — 1 operation(s) for supply & demand.
  name: REA Group Supply & Demand API
  slug: rea-group-supply-demand-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Tenure Type History
  name: REA Group Tenure Type API
  slug: rea-group-tenure-type-api
- baseURL: https://data.proptrack.com
  baseurl_source: declared
  description: Property Transactions
  name: REA Group Transactions API
  slug: rea-group-transactions-api
artifact_total: 40
collections:
- collection_type: open
  name: Address API
  slug: open-rea-group-address
- collection_type: open
  name: Coming Soon
  slug: open-rea-group-coming-soon
- collection_type: open
  name: Disclaimers API
  slug: open-rea-group-disclaimers
- collection_type: open
  name: Listings API
  slug: open-rea-group-listings
- collection_type: open
  name: Market
  slug: open-rea-group-market
- collection_type: open
  name: OAuth 2.0
  slug: open-rea-group-oauth
- collection_type: open
  name: Properties API
  slug: open-rea-group-properties
- collection_type: open
  name: Reports
  slug: open-rea-group-reports
- collection_type: open
  name: Transactions
  slug: open-rea-group-transactions
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/rea-group-capability-edges.yml
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
- group: docs
  title: ''
  type: APIReference
  url: https://developer.proptrack.com.au/docs/apis/guide
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.proptrack.com.au/docs/apis/how-to-authenticate
- group: start
  title: ''
  type: PartnerPortal
  url: https://partner.realestate.com.au/
- group: docs
  title: ''
  type: Schema
  url: https://reaxml.realestate.com.au/propertyList.dtd
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
- group: operate
  title: ''
  type: Support
  url: https://www.proptrack.com.au/support/contact-support/
- group: operate
  title: ''
  type: FAQ
  url: https://developer.proptrack.com.au/docs/apis/faqs
- group: start
  title: ''
  type: SignUp
  url: https://www.proptrack.com.au/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rea-group.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.proptrack.com.au/docs/apis/terms-of-use
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
  type: Pagination
  url: https://developer.proptrack.com.au/docs/apis/pagination
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/rea-group-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/rea-group-error-codes.yml
- group: build
  title: ''
  type: Examples
  url: examples/rea-group-examples.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/rea-group-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/rea-group-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rea-group-plans.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rea-group-agentic-access.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/rea-group-security-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/rea-group-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rea-group-lifecycle.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.proptrack.com.au/docs/apis/coming-soon
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
description: REA Group Limited is an ASX-listed (ASX:REA) digital real estate advertising business headquartered in Melbourne, Australia and majority-owned by News Corp. It operates realestate.com.au and realcommercial.com.au, the property data and analytics brand PropTrack, the Mortgage Choice broking network, and REA India (Housing.com, PropTiger, and Makaan). REA Group's public developer surface is delivered through PropTrack, whose developer portal publishes nine OpenAPI 3.1 documents covering 32 operations - OAuth token issuance, address matching and suggestion, property summary, attributes, planning, tenure, listings and transactions, automated valuations (AVM Sale, Rent, Plus and Pro), PDF valuation and property reports, suburb-level market history, supply and demand, auction results and demographics, plus a Disclaimers API that serves the attribution text PropTrack contractually requires alongside its data. Every service also publishes a live, unauthenticated Stoplight mock server,
  so the contract can be exercised before a commercial agreement is signed. The APIs are documented publicly but are partner-gated - access requires a commercial agreement arranged through an Account Manager, and calls are authenticated with OAuth 2.0 client credentials exchanged for a one-hour JWT bearer token at data.proptrack.com. Alongside PropTrack, REA Group runs the realestate.com.au Partner Portal (partner.realestate.com.au), the integration surface for real estate agencies and their CRM / software providers to publish for-sale and for-rent listings onto realestate.com.au and realcommercial.com.au and to receive buyer and renter enquiries. Listing distribution uses REAXML, REA's long-standing industry-standard XML property feed (schema published at reaxml.realestate.com.au), which the majority of Australian agency CRMs implement, with partner onboarding, API credentials (Client ID + secret) and enquiry delivery managed through the partner portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rea-group.png
layout: provider
modified: '2026-07-27T12:00:00Z'
name: REA Group
nav: Providers
network: true
overview: 'REA Group publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Attributes API, Auction Results API, AVM API, and 20 more. Tagged areas include Real-Estate, Property Data, Valuations, AVM, and Market Insights.


  REA Group''s developer surface includes documentation, API reference, getting-started guide, YouTube channel, engineering blog, support, FAQ, and 32 more developer resources.'
plans:
- name: Rea Group Plans
  plan_count: 2
  slug: rea-group-plans
random_paper: 11
rate_limits:
- limit_count: 16
  name: Rea Group Rate Limits
  slug: rea-group-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 4.5
    contract_quality: 57.7
    developer_ergonomics: 62.5
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 49.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rea-group/refs/heads/main/screenshots/rea-group-2026-07-27T125400.png
security:
- kind: authentication
  name: Rea Group Authentication
  slug: rea-group-authentication
  summary_line: oauth2 · 2 schemes
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
- Real-Estate
- Property Data
- Valuations
- AVM
- Market Insights
- Listings
- Transaction
- Address Matching
- REAXML
- Partner Portal
- PropTech
- Australia
website: https://www.rea-group.com/
---
