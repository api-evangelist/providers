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
    error_semantics: verified
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
  score: 32.5
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Cox Automotive Agentic Access
  operation_count: 100
  slug: cox-automotive-agentic-access
  summary_line: 100 operations · 24 acting
api_count: 10
apis:
- description: 'Manheim''s third-party integration surface — a suite of hypermedia (href-linked) JSON REST APIs over the wholesale vehicle remarketing lifecycle: auction locations, inventory units and consignments, ma'
  name: Manheim Hypermedia API Suite
  slug: manheim
- description: Publish/subscribe business-event notification service for the Manheim auction lifecycle. Consumers register a subscriber, create subscriptions with resource, type, text (VIN) or richFilter criteria, a
  name: Manheim Event Notifications
  slug: manheim-events
- description: The company-wide API storefront and integration platform fronting Cox Automotive's partner APIs — Dealertrack credit application, registration and titling, DealXG and Deal Push, Eventer publishing, MM
  name: Cox Automotive Integration Platform (API Storefront)
  slug: integration-platform
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ApplyConfiguration API from Cox Automotive — 1 operation(s) for applyconfiguration.
  name: Cox Automotive Apply Configuration API
  slug: cox-automotive-applyconfiguration-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The BodyStyles API from Cox Automotive — 1 operation(s) for bodystyles.
  name: Cox Automotive Body Styles API
  slug: cox-automotive-bodystyles-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ConsumerRatings API from Cox Automotive — 1 operation(s) for consumerratings.
  name: Cox Automotive Consumer Ratings API
  slug: cox-automotive-consumerratings-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ConsumerReviews API from Cox Automotive — 1 operation(s) for consumerreviews.
  name: Cox Automotive Consumer Reviews API
  slug: cox-automotive-consumerreviews-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The CostToOwn API from Cox Automotive — 1 operation(s) for costtoown.
  name: Cox Automotive Cost To Own API
  slug: cox-automotive-costtoown-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The CpoPrograms API from Cox Automotive — 1 operation(s) for cpoprograms.
  name: Cox Automotive Cpo Programs API
  slug: cox-automotive-cpoprograms-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ErrorCodes API from Cox Automotive — 2 operation(s) for errorcodes.
  name: Cox Automotive Error Codes API
  slug: cox-automotive-errorcodes-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ExpertRatings API from Cox Automotive — 1 operation(s) for expertratings.
  name: Cox Automotive Expert Ratings API
  slug: cox-automotive-expertratings-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ExpertReviews API from Cox Automotive — 1 operation(s) for expertreviews.
  name: Cox Automotive Expert Reviews API
  slug: cox-automotive-expertreviews-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Links API from Cox Automotive — 1 operation(s) for links.
  name: Cox Automotive Links API
  slug: cox-automotive-links-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Makes API from Cox Automotive — 2 operation(s) for makes.
  name: Cox Automotive Makes API
  slug: cox-automotive-makes-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The MarketingCategories API from Cox Automotive — 1 operation(s) for marketingcategories.
  name: Cox Automotive Marketing Categories API
  slug: cox-automotive-marketingcategories-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Models API from Cox Automotive — 2 operation(s) for models.
  name: Cox Automotive Models API
  slug: cox-automotive-models-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ModelYears API from Cox Automotive — 2 operation(s) for modelyears.
  name: Cox Automotive Model Years API
  slug: cox-automotive-modelyears-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: All methods related to an offer
  name: Cox Automotive Offer API
  slug: cox-automotive-offer-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: All methods related to a prospect
  name: Cox Automotive Prospect API
  slug: cox-automotive-prospect-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Specifications API from Cox Automotive — 1 operation(s) for specifications.
  name: Cox Automotive Specifications API
  slug: cox-automotive-specifications-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Token API from Cox Automotive — 1 operation(s) for token.
  name: Cox Automotive Token API
  slug: cox-automotive-token-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The TopTenLists API from Cox Automotive — 1 operation(s) for toptenlists.
  name: Cox Automotive Top Ten Lists API
  slug: cox-automotive-toptenlists-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Trims API from Cox Automotive — 2 operation(s) for trims.
  name: Cox Automotive Trims API
  slug: cox-automotive-trims-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Typicals API from Cox Automotive — 1 operation(s) for typicals.
  name: Cox Automotive Typicals API
  slug: cox-automotive-typicals-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The ValidateConfiguration API from Cox Automotive — 1 operation(s) for validateconfiguration.
  name: Cox Automotive Validate Configuration API
  slug: cox-automotive-validateconfiguration-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Values API from Cox Automotive — 1 operation(s) for values.
  name: Cox Automotive Values API
  slug: cox-automotive-values-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: All methods related to vehicles
  name: Cox Automotive Vehicle API
  slug: cox-automotive-vehicle-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The VehicleOptions API from Cox Automotive — 1 operation(s) for vehicleoptions.
  name: Cox Automotive Vehicle Options API
  slug: cox-automotive-vehicleoptions-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The VehicleSpecs API from Cox Automotive — 1 operation(s) for vehiclespecs.
  name: Cox Automotive Vehicle Specs API
  slug: cox-automotive-vehiclespecs-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Vin API from Cox Automotive — 1 operation(s) for vin.
  name: Cox Automotive Vin API
  slug: cox-automotive-vin-api
- baseURL: https://idws.datasolutions.coxautoinc.com
  baseurl_source: declared
  description: The Years API from Cox Automotive — 1 operation(s) for years.
  name: Cox Automotive Years API
  slug: cox-automotive-years-api
- baseURL: https://api.manheim.com
  baseurl_source: declared
  description: The Batch Jobs API from Cox Automotive — 5 operation(s) for batch jobs.
  name: Cox Automotive Batch Jobs API
  slug: cox-automotive-batch-jobs-api
artifact_total: 40
asyncapis:
- description: ''
  name: Cox Automotive Manheim Events Webhooks
  slug: cox-automotive-manheim-events-webhooks
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/overlays/cox-automotive-kbb-idws-editorial-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cox-automotive-kbb-idws-editorial-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/overlays/cox-automotive-kbb-advertising-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cox-automotive-kbb-advertising-data-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/overlays/cox-automotive-kbb-instant-cash-offer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cox-automotive-kbb-instant-cash-offer-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cox-automotive/refs/heads/main/overlays/cox-automotive-kbb-batch-vin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/cox-automotive-kbb-batch-vin-overlay.yaml
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
overview: 'Cox Automotive publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Apply Configuration API, Body Styles API, Consumer Ratings API, and 26 more. Tagged areas include Automotive, Vehicle Data, Vehicle Valuations, Auctions, and Dealer Software.


  The Cox Automotive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Cox Automotive''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 34 more developer resources.'
plans:
- name: Cox Automotive Plans Pricing
  plan_count: 0
  slug: cox-automotive-plans-pricing
random_paper: 2
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
  composite: 40.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 52.2
    developer_ergonomics: 39.9
    discoverability: 68.5
    operational_transparency: 57.9
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
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
