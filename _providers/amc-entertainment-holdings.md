---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Amc Entertainment Holdings Agentic Access
  operation_count: 79
  slug: amc-entertainment-holdings-agentic-access
  summary_line: 79 operations · 23 acting
api_count: 1
apis:
- description: Ticket and loyalty QR codes and Code 128 barcodes.
  name: AMC Entertainment Holdings Barcodes API
  slug: amc-entertainment-holdings-barcodes-api
- description: Concessions ordering, categories, delivery and pickup logistics.
  name: AMC Entertainment Holdings Concessions API
  slug: amc-entertainment-holdings-concessions-api
- description: Geographic helpers for finding theatres by state, city, name, or coordinates.
  name: AMC Entertainment Holdings Locations API
  slug: amc-entertainment-holdings-locations-api
- description: AMC Stubs loyalty accounts, cards, redemptions, and registrations.
  name: AMC Entertainment Holdings Loyalty API
  slug: amc-entertainment-holdings-loyalty-api
- description: AMC market areas grouping theatres by region.
  name: AMC Entertainment Holdings Markets API
  slug: amc-entertainment-holdings-markets-api
- description: Images and videos for movies, theatres, and attributes.
  name: AMC Entertainment Holdings Media API
  slug: amc-entertainment-holdings-media-api
- description: Movie ticket confirmation lookups.
  name: AMC Entertainment Holdings MovieConfirmations API
  slug: amc-entertainment-holdings-movieconfirmations-api
- description: AMC movies, including now-playing, advance, coming-soon, and on-demand.
  name: AMC Entertainment Holdings Movies API
  slug: amc-entertainment-holdings-movies-api
- description: Order creation, payment, fulfillment, and management.
  name: AMC Entertainment Holdings Orders API
  slug: amc-entertainment-holdings-orders-api
- description: Order refunds, refund reasons, and fee waivers.
  name: AMC Entertainment Holdings Refunds API
  slug: amc-entertainment-holdings-refunds-api
- description: Seating layouts and seat selection.
  name: AMC Entertainment Holdings Seating API
  slug: amc-entertainment-holdings-seating-api
- description: Theatre showtimes for movies, including embargoed and proximity-based searches.
  name: AMC Entertainment Holdings Showtimes API
  slug: amc-entertainment-holdings-showtimes-api
- description: U.S. states served by AMC.
  name: AMC Entertainment Holdings States API
  slug: amc-entertainment-holdings-states-api
- description: AMC theatre locations, attributes, and metadata.
  name: AMC Entertainment Holdings Theatres API
  slug: amc-entertainment-holdings-theatres-api
- description: AMC account wallets for external billers.
  name: AMC Entertainment Holdings Wallet API
  slug: amc-entertainment-holdings-wallet-api
- description: Vendor webhook subscription and management.
  name: AMC Entertainment Holdings Webhooks API
  slug: amc-entertainment-holdings-webhooks-api
artifact_total: 60
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AMC Theatres Barcodes API
  slug: open-amc-entertainment-holdings-barcodes-api
- collection_type: open
  name: AMC Theatres Barcodes Concessions API
  slug: open-amc-entertainment-holdings-concessions-api
- collection_type: open
  name: AMC Theatres Barcodes Locations API
  slug: open-amc-entertainment-holdings-locations-api
- collection_type: open
  name: AMC Theatres Barcodes Loyalty API
  slug: open-amc-entertainment-holdings-loyalty-api
- collection_type: open
  name: AMC Theatres Barcodes Markets API
  slug: open-amc-entertainment-holdings-markets-api
- collection_type: open
  name: AMC Theatres Barcodes Media API
  slug: open-amc-entertainment-holdings-media-api
- collection_type: open
  name: AMC Theatres Barcodes MovieConfirmations API
  slug: open-amc-entertainment-holdings-movieconfirmations-api
- collection_type: open
  name: AMC Theatres Barcodes Movies API
  slug: open-amc-entertainment-holdings-movies-api
- collection_type: open
  name: AMC Theatres Barcodes Orders API
  slug: open-amc-entertainment-holdings-orders-api
- collection_type: open
  name: AMC Theatres Barcodes Refunds API
  slug: open-amc-entertainment-holdings-refunds-api
- collection_type: open
  name: AMC Theatres Barcodes Seating API
  slug: open-amc-entertainment-holdings-seating-api
- collection_type: open
  name: AMC Theatres Barcodes Showtimes API
  slug: open-amc-entertainment-holdings-showtimes-api
- collection_type: open
  name: AMC Theatres Barcodes States API
  slug: open-amc-entertainment-holdings-states-api
- collection_type: open
  name: AMC Barcodes Theatres API
  slug: open-amc-entertainment-holdings-theatres-api
- collection_type: open
  name: AMC Theatres Barcodes Wallet API
  slug: open-amc-entertainment-holdings-wallet-api
- collection_type: open
  name: AMC Theatres Barcodes Webhooks API
  slug: open-amc-entertainment-holdings-webhooks-api
- collection_type: open
  name: AMC Theatres API
  slug: open-amc-theatres-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amc-entertainment-holdings-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amc-entertainment-holdings-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amc-entertainment-holdings-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amc-entertainment-holdings-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.amctheatres.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.amctheatres.com
- group: other
  title: ''
  type: Customers
  url: https://www.amctheatres.com/amcstubs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amctheatres.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amctheatres.com/legal/privacy-policy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/amc-theatres
- group: build
  title: ''
  type: GitHub
  url: https://github.com/amctheatres
created: '2026-05-04'
description: AMC Entertainment Holdings is the largest movie exhibition company in the United States and the world, operating AMC Theatres, AMC Stubs loyalty programs, and related entertainment brands. AMC publishes a public developer portal at developers.amctheatres.com that exposes a REST API for movies, showtimes, theatres, locations, seating, ticketing, concessions, AMC Stubs loyalty, refunds, fee waivers, barcodes, and webhooks. The API is the primary integration surface for distributors, partners, and third-party developers building movie discovery, ticket sales, and AMC Stubs co-marketing experiences.
examples:
- key_count: 2
  name: Amc Theatres Create Order Example
  slug: amc-theatres-create-order-example
- key_count: 10
  name: Amc Theatres Get Loyalty Account Example
  slug: amc-theatres-get-loyalty-account-example
- key_count: 4
  name: Amc Theatres List Movies Now Playing Example
  slug: amc-theatres-list-movies-now-playing-example
- key_count: 4
  name: Amc Theatres List Theatre Showtimes Example
  slug: amc-theatres-list-theatre-showtimes-example
- key_count: 5
  name: Amc Theatres List Theatres Example
  slug: amc-theatres-list-theatres-example
finops:
- name: Amc Entertainment Holdings Finops
  service_category: API
  slug: amc-entertainment-holdings-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amc-entertainment-holdings.png
json_schemas:
- name: AMC Attribute
  property_count: 10
  slug: amc-theatres-attribute
- name: AMC Stubs Loyalty Account
  property_count: 10
  slug: amc-theatres-loyalty-account
- name: AMC Movie
  property_count: 19
  slug: amc-theatres-movie
- name: AMC Order
  property_count: 12
  slug: amc-theatres-order
- name: AMC Showtime
  property_count: 24
  slug: amc-theatres-showtime
- name: AMC Theatre
  property_count: 28
  slug: amc-theatres-theatre
json_structures:
- name: Amc Theatres Loyalty Account Structure
  property_count: 8
  slug: amc-theatres-loyalty-account-structure
- name: Amc Theatres Movie Structure
  property_count: 13
  slug: amc-theatres-movie-structure
- name: Amc Theatres Order Structure
  property_count: 9
  slug: amc-theatres-order-structure
- name: Amc Theatres Showtime Structure
  property_count: 16
  slug: amc-theatres-showtime-structure
- name: Amc Theatres Theatre Structure
  property_count: 16
  slug: amc-theatres-theatre-structure
jsonld:
- class_count: 53
  name: Amc Entertainment Holdings Context
  property_count: 50
  slug: amc-entertainment-holdings-context
layout: provider
modified: '2026-05-19'
name: AMC Entertainment Holdings
nav: Providers
network: true
overview: 'AMC Entertainment Holdings publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Barcodes API, Concessions API, Locations API, and 13 more. Tagged areas include Entertainment, Movies, Theatres, Showtimes, and Ticketing.


  The AMC Entertainment Holdings catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AMC Entertainment Holdings'' developer surface includes authentication, GitHub presence, and 9 more developer resources.'
plans:
- name: Amc Entertainment Holdings Plans Pricing
  plan_count: 1
  slug: amc-entertainment-holdings-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Amc Entertainment Holdings Rate Limits
  slug: amc-entertainment-holdings-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: AMC Entertainment Holdings API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amc-entertainment-holdings-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: AMC Entertainment Holdings API Rules
  rule_count: 28
  severity_counts:
    error: 10
    hint: 0
    info: 5
    warn: 13
  slug: amc-theatres-rules
score:
  band: thin
  composite: 38.9
  coverage:
    artifact_dirs: 15
    catalog_gap: 31.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 28.8
    contract_quality: 32.5
    developer_ergonomics: 38.1
    discoverability: 63.0
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 38.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 16
      marker_coverage: 100.0
      total: 16
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amc-entertainment-holdings/refs/heads/main/screenshots/amc-entertainment-holdings-2026-06-20T171856.png
security:
- kind: authentication
  name: Amc Entertainment Holdings Authentication
  slug: amc-entertainment-holdings-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amc Entertainment Holdings Domain Security
  slug: amc-entertainment-holdings-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amc Entertainment Holdings Vulnerability Disclosure
  slug: amc-entertainment-holdings-vulnerability-disclosure
  summary_line: disclosure policy published
slug: amc-entertainment-holdings
tags:
- Entertainment
- Movies
- Theatres
- Showtimes
- Ticketing
- Concessions
- Loyalty
- Fortune 500
website: https://www.amctheatres.com
---
