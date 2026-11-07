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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.1
  scored_at: '2026-11-06'
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
- baseURL: https://reaxml.realestate.com.au
  baseurl_source: declared
  description: The Oauth2 API from REA Group — 1 operation(s) for oauth2.
  name: REA Group Oauth2 API
  slug: rea-group-oauth2-api
artifact_total: 45
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
- group: commercial
  href: https://artifacts.apis.io/rea-group/finops/rea-group-finops.yml
  title: ''
  type: FinOps
  url: finops/rea-group-finops.yml
- group: design
  href: https://artifacts.apis.io/rea-group/rules/rea-group-rules.yml
  title: ''
  type: Spectral
  url: rules/rea-group-rules.yml
- group: design
  href: https://artifacts.apis.io/rea-group/vocabulary/rea-group-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rea-group-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rea-group/errors/rea-group-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rea-group-problem-types.yml
- group: other
  href: https://artifacts.apis.io/rea-group/hosts/rea-group-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rea-group-hosts.yml
- group: other
  href: https://artifacts.apis.io/rea-group/vendors/rea-group-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rea-group-vendors.yml
- group: other
  title: ''
  type: Leadership
  url: https://www.rea-group.com/about-us/our-people-and-story/leadership/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.proptrack.com.au/docs/apis/api-trials
- group: other
  href: https://artifacts.apis.io/rea-group/capabilities/rea-group-capability-edges.yml
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
  href: https://artifacts.apis.io/rea-group/authentication/rea-group-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rea-group-authentication.yml
- group: design
  href: https://artifacts.apis.io/rea-group/conventions/rea-group-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rea-group-conventions.yml
- group: design
  title: ''
  type: Pagination
  url: https://developer.proptrack.com.au/docs/apis/pagination
- group: operate
  href: https://artifacts.apis.io/rea-group/rate-limits/rea-group-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rea-group-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/rea-group/errors/rea-group-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/rea-group-error-codes.yml
- group: build
  href: https://artifacts.apis.io/rea-group/examples/rea-group-examples.yml
  title: ''
  type: Examples
  url: examples/rea-group-examples.yml
- group: design
  href: https://artifacts.apis.io/rea-group/data-model/rea-group-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rea-group-data-model.yml
- group: start
  href: https://artifacts.apis.io/rea-group/sandbox/rea-group-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rea-group-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/rea-group/plans/rea-group-plans.yml
  title: ''
  type: Plans
  url: plans/rea-group-plans.yml
- group: agent
  href: https://artifacts.apis.io/rea-group/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/rea-group/agentic-access/rea-group-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rea-group-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/rea-group/overlays/rea-group-security-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rea-group-security-overlay.yaml
- group: design
  href: https://artifacts.apis.io/rea-group/conformance/rea-group-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rea-group-conformance.yml
- group: design
  href: https://artifacts.apis.io/rea-group/lifecycle/rea-group-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rea-group-lifecycle.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://developer.proptrack.com.au/docs/apis/coming-soon
- group: agent
  href: https://artifacts.apis.io/rea-group/well-known/rea-group-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rea-group-well-known.yml
- group: auth
  href: https://artifacts.apis.io/rea-group/security/rea-group-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rea-group-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/rea-group/security/rea-group-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rea-group-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.rea-group.com/security
created: '2026-07-20'
description: REA Group Limited is an ASX-listed (ASX:REA) digital real estate advertising business headquartered in Melbourne, Australia and majority-owned by News Corp. It operates realestate.com.au and realcommercial.com.au, the property data and analytics brand PropTrack, the Mortgage Choice broking network, and REA India (Housing.com, PropTiger, and Makaan). REA Group's public developer surface is delivered through PropTrack, whose developer portal publishes nine OpenAPI 3.1 documents covering 32 operations - OAuth token issuance, address matching and suggestion, property summary, attributes, planning, tenure, listings and transactions, automated valuations (AVM Sale, Rent, Plus and Pro), PDF valuation and property reports, suburb-level market history, supply and demand, auction results and demographics, plus a Disclaimers API that serves the attribution text PropTrack contractually requires alongside its data. Every service also publishes a live, unauthenticated Stoplight mock server,
  so the contract can be exercised before a commercial agreement is signed. The APIs are documented publicly but are partner-gated - access requires a commercial agreement arranged through an Account Manager, and calls are authenticated with OAuth 2.0 client credentials exchanged for a one-hour JWT bearer token at data.proptrack.com. Alongside PropTrack, REA Group runs the realestate.com.au Partner Portal (partner.realestate.com.au), the integration surface for real estate agencies and their CRM / software providers to publish for-sale and for-rent listings onto realestate.com.au and realcommercial.com.au and to receive buyer and renter enquiries. Listing distribution uses REAXML, REA's long-standing industry-standard XML property feed (schema published at reaxml.realestate.com.au), which the majority of Australian agency CRMs implement, with partner onboarding, API credentials (Client ID + secret) and enquiry delivery managed through the partner portal.
finops:
- has_sources: true
  method: derived
  name: Rea Group Finops
  primary_unit: ''
  service_category: ''
  slug: rea-group-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rea-group.png
layout: provider
modified: '2026-07-27T12:00:00Z'
name: REA Group
nav: Providers
network: true
overview: 'REA Group publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attributes API, Auction Results API, AVM API, and 22 more. Tagged areas include Real Estate, Property Data, Valuation, AVM, and Market Insights.


  The REA Group catalog on APIs.io includes 1 Spectral governance ruleset.


  REA Group''s developer surface includes pricing, documentation, API reference, getting-started guide, YouTube channel, engineering blog, support, and 38 more developer resources.'
plans:
- name: Rea Group Plans
  plan_count: 0
  slug: rea-group-plans
random_paper: 2
rate_limits:
- limit_count: 16
  name: Rea Group Rate Limits
  slug: rea-group-rate-limits
rules:
- authorship: generated
  effective_rule_count: 94
  extends:
  - spectral:oas
  name: REA Group API Rules
  rule_count: 53
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 13
  slug: rea-group-rules
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 31
    catalog_earned: 57.8
    catalog_earned_first_party: 12.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 52.2
    developer_ergonomics: 62.5
    discoverability: 80.4
    operational_transparency: 50.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 51.3
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
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/rea-group/rea-group-2026-07-27T125400.png
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
skill_count: 3
skills:
- name: Order a PropTrack AVM valuation and retrieve the report
  slug: rea-group-order-avm-valuation
- name: Resolve an Australian address to a PropTrack property profile
  slug: rea-group-resolve-address-to-property
- name: Search PropTrack listings, sold transactions and suburb market trends
  slug: rea-group-search-listings-and-market
slug: rea-group
tags:
- Real Estate
- Property Data
- Valuation
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
