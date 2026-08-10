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
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Rea Group Agentic Access
  operation_count: 32
  slug: rea-group-agentic-access
  summary_line: 32 operations · 5 acting
api_count: 11
apis:
- description: 'The OAuth 2.0 client credentials token service. POST /oauth2/token with the partner api_key and api_secret Base64-encoded as HTTP Basic returns a JWT access token with a 3600 second TTL, presented as '
  name: PropTrack OAuth 2.0 Token API
  slug: proptrack-oauth-api
- description: Address match and address suggest. Resolves free-text or partial Australian addresses to a canonical propertyId and gpid with a matchScore - the entry point for almost every PropTrack workflow. Struct
  name: PropTrack Address API
  slug: proptrack-address-api
- description: The largest PropTrack service - 15 operations spanning property summary, attributes, listings, planning and zoning, tenure type, transactions and property search (summaries and map geopoints) under /a
  name: PropTrack Properties API
  slug: proptrack-properties-api
- description: Listing detail by listingId plus two cursor-paginated search shapes - point and radius, and suburb and postcode - exposing for-sale and for-rent listing data from realestate.com.au and realcommercial.
  name: PropTrack Listings API
  slug: proptrack-listings-api
- description: Sold transaction search by point and radius and by suburb and postcode, cursor-paginated. On trial agreements, transactions sourced from the Victorian Valuer-General are withheld while agent-advised t
  name: PropTrack Transactions API
  slug: proptrack-transactions-api
- description: Suburb-level market statistics - sale price history, rent history, supply and demand, auction results and demographics. Keyed by geography (searchType plus state, postcode or suburb) rather than by pr
  name: PropTrack Market API
  slug: proptrack-market-api
- description: Renders an ordered AVM valuation as a PDF by valuationId, and orders a standalone property report. Rate limited to 25 requests per second and the only operations besides AVM that document a 504 Gatewa
  name: PropTrack Reports API
  slug: proptrack-reports-api
- description: Serves the attribution and disclaimer text PropTrack contractually requires be displayed wherever its data is rendered, plus the associated branding rules. Fetching it rather than hardcoding is the do
  name: PropTrack Disclaimers API
  slug: proptrack-disclaimers-api
- description: Documented but not yet released. A nearby-education-facilities endpoint keyed by propertyId, published ahead of availability on the Coming Soon page - the closest thing PropTrack publishes to a roadma
  name: PropTrack Upcoming APIs (Schools)
  slug: proptrack-upcoming-api
- description: REA Group's REAXML listing feed - the long-standing industry-standard XML property schema used by Australian agency CRMs to publish residential and commercial for-sale and for-rent listings onto reale
  name: realestate.com.au Listing Feed (REAXML)
  slug: realestate-listing-feed-reaxml
- description: The realestate.com.au Partner Portal is REA Group's integration surface for agencies and their software / CRM providers - covering partner onboarding, API credential management (Client ID + API secret
  name: realestate.com.au Partner Portal
  slug: realestate-partner-portal
artifact_total: 17
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
overview: 'REA Group publishes 9 APIs on the [APIs.io](https://apis.io/) network, including PropTrack OAuth 2.0 Token API, PropTrack Address API, PropTrack Properties API, and 6 more. Tagged areas include Real Estate, Property Data, Valuations, AVM, and Market Insights.


  REA Group''s developer surface includes documentation, API reference, getting-started guide, YouTube channel, engineering blog, support, FAQ, and 31 more developer resources.'
plans:
- name: Rea Group Plans
  plan_count: 2
  slug: rea-group-plans
random_paper: 102
rate_limits:
- limit_count: 16
  name: Rea Group Rate Limits
  slug: rea-group-rate-limits
score:
  band: strong
  composite: 56.1
  delta: 0.0
  facets:
    commercial_clarity: 55.3
    contract_quality: 62.1
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 52.6
  previous_composite: 56.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
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
- Real Estate
- Property Data
- Valuations
- AVM
- Market Insights
- Listings
- Transactions
- Address Matching
- REAXML
- Partner Portal
- PropTech
- Australia
website: https://www.rea-group.com/
---
