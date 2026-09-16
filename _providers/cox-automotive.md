---
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.6
  scored_at: '2026-09-15'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Cox Automotive Agentic Access
  operation_count: 100
  slug: cox-automotive-agentic-access
  summary_line: 100 operations · 24 acting
api_count: 5
apis:
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: InfoDriver Web Service (IDWS) 4.0 Vehicle Service — a RESTful Kelley Blue Book API returning vehicle configuration, makes, models, model years, trims, body styles, options, specifications, typicals, C
  name: Kelley Blue Book IDWS 4.0 Vehicle Service
  slug: kbb-idws-vehicle
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: InfoDriver Web Service (IDWS) 4.0 Editorial Service — Kelley Blue Book consumer ratings, consumer reviews, expert ratings, expert reviews and Top Ten lists for a vehicle, returned as JSON and authenti
  name: Kelley Blue Book IDWS 4.0 Editorial Service
  slug: kbb-idws-editorial
- baseURL: https://sandbox.api.kbb.com/ads
  baseurl_source: declared
  description: Vehicle data for building dynamic automotive advertising — pricing, cost-to-own, expert and consumer ratings and reviews, vehicle links, fuel cost, specifications, MPG and awards. Supports CORS, gzip,
  name: Kelley Blue Book Advertising Data API
  slug: kbb-advertising-data
- baseURL: https://api.kbb.com/ico/v1
  baseurl_source: declared
  description: Produces a Kelley Blue Book Instant Cash Offer for a vehicle. Vehicle configuration lookups (year, make, model, trim, transmission, engine, drivetrain, colour, options), licence-plate-to-VIN lookup, p
  name: Kelley Blue Book Instant Cash Offer (ICO) API
  slug: kbb-instant-cash-offer
- baseURL: https://sandbox.api.kbb.com/idbv
  baseurl_source: declared
  description: Asynchronous batch VIN decoding and valuation. Submit a batch job, poll its status, and retrieve the input and output files, or cancel a running job. Requires both a Mashery api_key and an OAuth-style
  name: Kelley Blue Book Batch VIN API
  slug: kbb-batch-vin
- description: 'Manheim''s third-party integration surface — a suite of hypermedia (href-linked) JSON REST APIs over the wholesale vehicle remarketing lifecycle: auction locations, inventory units and consignments, ma'
  name: Manheim Hypermedia API Suite
  slug: manheim
- description: Publish/subscribe business-event notification service for the Manheim auction lifecycle. Consumers register a subscriber, create subscriptions with resource, type, text (VIN) or richFilter criteria, a
  name: Manheim Event Notifications
  slug: manheim-events
- description: The company-wide API storefront and integration platform fronting Cox Automotive's partner APIs — Dealertrack credit application, registration and titling, DealXG and Deal Push, Eventer publishing, MM
  name: Cox Automotive Integration Platform (API Storefront)
  slug: integration-platform
artifact_total: 16
asyncapis:
- description: ''
  name: Cox Automotive Manheim Events Webhooks
  slug: cox-automotive-manheim-events-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.coxautoinc.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.coxautoinc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.manheim.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kbb.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.manheim.com/pages/accessAndEnvironments.html
- group: operate
  title: ''
  type: Support
  url: https://developer.manheim.com/support/help.html
- group: company
  title: ''
  type: Blog
  url: https://www.coxautoinc.com/insights/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cox-Automotive
- group: start
  title: ''
  type: SignUp
  url: https://developer.coxautoinc.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.coxautoinc.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.coxautoinc.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coxautoinc.com/privacy-statement/
- group: operate
  title: ''
  type: StatusPage
  url: https://coxautoapi.statuspage.io/
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/1195870-3ff750f7-69e7-49e2-bbaa-e42fecb49939
- group: auth
  title: ''
  type: Security
  url: https://www.coxautoinc.com/responsible-disclosure
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/well-known/cox-automotive-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/cox-automotive-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/well-known/cox-automotive-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/cox-automotive-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/security/cox-automotive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/cox-automotive-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/security/cox-automotive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cox-automotive-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/authentication/cox-automotive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/cox-automotive-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/scopes/cox-automotive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/cox-automotive-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/conventions/cox-automotive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/cox-automotive-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/conformance/cox-automotive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cox-automotive-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/errors/cox-automotive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cox-automotive-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/lifecycle/cox-automotive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/cox-automotive-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/data-model/cox-automotive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cox-automotive-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/rate-limits/cox-automotive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/cox-automotive-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/plans/cox-automotive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cox-automotive-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/packages/cox-automotive-packages.yml
  title: ''
  type: Packages
  url: packages/cox-automotive-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/llms/cox-automotive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cox-automotive-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/asyncapi/cox-automotive-manheim-events-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/cox-automotive-manheim-events-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/mcp/cox-automotive-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/cox-automotive-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/agentic-access/cox-automotive-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cox-automotive-agentic-access.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/sandbox/cox-automotive-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/cox-automotive-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/errors/cox-automotive-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/cox-automotive-error-codes.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/overlays/cox-automotive-kbb-idws-vehicle-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cox-automotive-kbb-idws-vehicle-overlay.yaml
created: '2026-09-13'
description: 'Cox Automotive is one of the world''s largest providers of products and services spanning the automotive ecosystem, operating a portfolio of brands that includes Manheim (wholesale vehicle auctions and remarketing), Kelley Blue Book (vehicle valuations and editorial data), Autotrader, Dealertrack (DMS, registration and titling, credit applications), vAuto, VinSolutions, Xtime, Dealer.com, HomeNet and Esntial. Its public API surface is split across several developer properties: the Kelley Blue Book Developer Portal (developer.kbb.com) publishes Swagger 2.0 contracts for the IDWS 4.0 vehicle and editorial services, the Advertising Data API, the Instant Cash Offer API and the Batch VIN API; the Manheim Developer Portal (developer.manheim.com) documents a hypermedia REST suite covering auctions, inventory, marketplace offerings, valuations, condition reports, images, users and a publish/subscribe event notification service; and the Cox Automotive Integration Platform / API Storefront
  (developer.coxautoinc.com) fronts the partner-gated catalogue of more than seventy runtime services visible on the public Cox Automotive API status page. Access to every environment is granted after a review by a Cox Automotive account representative, with keys issued through the Boomi/Mashery gateway.'
image: https://www.coxautoinc.com/wp-content/uploads/2025/09/CAI-1200x628-1.png
layout: provider
modified: '2026-09-13'
name: Cox Automotive
nav: Providers
network: true
overview: 'Cox Automotive publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Kelley Blue Book IDWS 4.0 Vehicle Service, Kelley Blue Book IDWS 4.0 Editorial Service, Kelley Blue Book Advertising Data API, and 2 more. Tagged areas include Automotive, Vehicle Data, Vehicle Valuations, Auctions, and Dealer Software.


  The Cox Automotive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cox Automotive''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 30 more developer resources.'
plans:
- name: Cox Automotive Plans Pricing
  plan_count: 0
  slug: cox-automotive-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 2
  name: Cox Automotive Rate Limits
  slug: cox-automotive-rate-limits
scopes:
- name: Cox Automotive Scopes
  scope_count: 0
  slug: cox-automotive-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 49.5
    developer_ergonomics: 39.9
    discoverability: 74.1
    operational_transparency: 57.9
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-15'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Cox Automotive Authentication
  slug: cox-automotive-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Cox Automotive Domain Security
  slug: cox-automotive-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Cox Automotive Vulnerability Disclosure
  slug: cox-automotive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: cox-automotive
tags:
- Automotive
- Vehicle Data
- Vehicle Valuations
- Auctions
- Dealer Software
- Automotive Retail
- VIN Decoding
- Inventory Management
- Remarketing
- Event
- Webhook
website: https://www.coxautoinc.com/
---
