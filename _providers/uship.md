---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.7
  scored_at: '2026-08-30'
api_count: 8
apis:
- description: 'The core uShip marketplace API — a RESTful, hypermedia-driven JSON API over the shipment lifecycle: searching active listings, creating and retrieving listings by commodity category, bids and bid acce'
  name: uShip API v2
  slug: uship-api-v2
- description: Bookable, algorithmically priced rates published by service providers in response to shipping-customer rate requests, as an alternative to the auction/bidding flow. Covers the shipping-customer side (
  name: uShip Published Rates API
  slug: uship-published-rates-api
- description: LTL Connect is uShip's marketplace-connected less-than-truckload product, quoting and booking LTL freight against uShip's carrier network. Documented on the uShip developer portal with a dedicated imp
  name: uShip LTL Connect API
  slug: uship-ltl-connect-api
- description: LTL Direct exposes uShip's directly contracted LTL carrier rates for shipper integrations, as the counterpart to LTL Connect. Documented on the uShip developer portal with its own guide and API refere
  name: uShip LTL Direct API
  slug: uship-ltl-direct-api
- description: 'The vehicle-transport slice of the uShip API — listing creation, published rates, and booking for cars and light trucks, including year/make/model and body-type lookups used by dealers, auctions, and '
  name: uShip Cars and Light Trucks API
  slug: uship-cars-and-light-trucks-api
- description: The furniture and household-goods slice of the uShip API, used by furniture retailers and eCommerce sellers to quote, book, and track first-to-final-mile big-and-bulky home delivery through uShip's ca
  name: uShip Furniture and Home Delivery API
  slug: uship-furniture-and-home-delivery-api
- description: User-management endpoints for integration partners — provisioning and managing the uShip user accounts an integrator creates and acts on behalf of within the marketplace.
  name: uShip Integrator Users API
  slug: uship-integrator-users-api
- description: Shipment tracking and transit-status history for booked listings — retrieve the recorded location history and most recent reported location, with punctuality measured against the bid's latest pickup a
  name: uShip Tracking API
  slug: uship-tracking-api
artifact_total: 11
asyncapis:
- description: ''
  name: Uship Notifications Webhooks
  slug: uship-notifications-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uship-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uship.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.uship.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uship.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://developer.uship.com/resources
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.uship.com/about-our-apis/getting-started
- group: start
  title: ''
  type: SignUp
  url: https://www.uship.com/register/
- group: start
  title: ''
  type: Login
  url: https://www.uship.com/signin.aspx
- group: operate
  title: ''
  type: Support
  url: https://help.uship.com/
- group: company
  title: ''
  type: Blog
  url: https://www.uship.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/uShip
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.uship.com/hc/articles/360008771433-user-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.uship.com/hc/articles/360009056894-privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uship.com/cost-to-ship/
- group: operate
  title: ''
  type: StatusPage
  url: https://uship.statuspage.io/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uship-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/uship-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uship-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uship-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uship-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uship-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uship-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/uship-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/uship-notifications-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uship-sandbox.yml
created: '2026-08-02'
description: uShip is an online shipping marketplace, founded in 2004 and headquartered in Austin, Texas, that connects individuals and businesses with a network of professional transport service providers to move large, heavy, and oversized freight — cars and light trucks, motorcycles and powersports, boats, furniture and household goods, heavy equipment, livestock, and LTL freight. Shippers list a shipment for free and carriers compete with bids or bookable published rates, giving shippers pricing transparency and choice. uShip exposes the marketplace to partners, affiliates, brokers, carriers, and eCommerce platforms through the uShip API (v2), a RESTful, hypermedia-driven JSON API secured with OAuth 2.0 covering shipment search, listing creation by commodity category, bidding, published/LTL rate requests and rate acceptance, booking, tracking and transit statuses, lookups, and integrator user management. API access is partner-gated — the developer portal at developer.uship.com is invitation-only
  and access is granted by the uShip API team.
image: https://www.uship.com/apple-touch-icon.png
layout: provider
modified: '2026-08-02'
name: uShip
nav: Providers
network: true
overview: 'uShip publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Shipping, Logistics, freight, Marketplace, and Transportation.


  The uShip catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  uShip''s developer surface includes documentation, API reference, getting-started guide, signup flow, support, engineering blog, pricing, and 18 more developer resources.'
random_paper: 7
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 14
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 42.7
    developer_ergonomics: 26.2
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 37.0
  provenance:
    conformance: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uship/refs/heads/main/screenshots/uship-2026-08-17T082657.png
security:
- kind: authentication
  name: Uship Authentication
  slug: uship-authentication
  summary_line: oauth2/apiKey · 2 schemes
- kind: domain-security
  name: Uship Domain Security
  slug: uship-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: uship
tags:
- Shipping
- Logistics
- freight
- Marketplace
- Transportation
- auto-transport
- ltl-freight
- last-mile-delivery
- shipment-tracking
- E-Commerce
- Supply Chain
- rate-quotes
website: https://www.uship.com/
---
