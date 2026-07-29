---
access_model:
  confidence: high
  label: Accreditation required · Application approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - https://ndc.virginatlantic.com/help/how-to-access-ndc-apis
  - https://ndc.virginatlantic.com/certification
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
api_count: 12
apis:
- description: IATA NDC 21.3 AirShopping message. Flight shopping and availability search returning Virgin Atlantic offers, including calendar and multi-city itineraries. Documented publicly on VS NDC Connect; no ba
  name: Virgin Atlantic NDC AirShopping API
  slug: virgin-atlantic-ndc-airshopping-api
- description: IATA NDC 21.3 OfferPrice message. Prices a selected offer and returns the firm, bookable price with applicable rules before an order is created.
  name: Virgin Atlantic NDC OfferPrice API
  slug: virgin-atlantic-ndc-offerprice-api
- description: IATA NDC 21.3 OrderCreate message. Creates the Virgin Atlantic Order and PNR from a priced offer, including passenger details and form of payment, and returns an OrderView response.
  name: Virgin Atlantic NDC OrderCreate API
  slug: virgin-atlantic-ndc-ordercreate-api
- description: IATA NDC 21.3 SeatAvailability message. Returns the seat map and seat pricing for an offer or an existing order.
  name: Virgin Atlantic NDC SeatAvailability API
  slug: virgin-atlantic-ndc-seatavailability-api
- description: IATA NDC 21.3 ServiceList message. Returns the ancillary services available against an offer or an order, such as bags and paid services.
  name: Virgin Atlantic NDC ServiceList API
  slug: virgin-atlantic-ndc-servicelist-api
- description: IATA NDC 21.3 OrderRetrieve message. Retrieves a single Virgin Atlantic Order by order identifier or PNR record locator and returns an OrderView response.
  name: Virgin Atlantic NDC OrderRetrieve API
  slug: virgin-atlantic-ndc-orderretrieve-api
- description: IATA NDC 21.3 OrderReshop message. Searches for alternative offers against an existing order, used for voluntary date and time changes and passenger servicing.
  name: Virgin Atlantic NDC OrderReshop API
  slug: virgin-atlantic-ndc-orderreshop-api
- description: IATA NDC 21.3 OrderQuote message. Quotes the price of a proposed change to an existing order, including requote and confirm of a held booking.
  name: Virgin Atlantic NDC OrderQuote API
  slug: virgin-atlantic-ndc-orderquote-api
- description: IATA NDC 21.3 OrderChange message. Applies changes to an existing order - APIS information amendment, name correction, split order, post-sale seat and service purchase, and voluntary cancellation.
  name: Virgin Atlantic NDC OrderChange API
  slug: virgin-atlantic-ndc-orderchange-api
- description: IATA NDC 21.3 OrderChangeNotif message. Notifies the seller of airline-initiated changes to an order, such as schedule changes.
  name: Virgin Atlantic NDC OrderChangeNotif API
  slug: virgin-atlantic-ndc-orderchangenotif-api
- description: IATA NDC 21.3 OrderList message. Returns a list of orders matching search criteria for the authenticated seller.
  name: Virgin Atlantic NDC OrderList API
  slug: virgin-atlantic-ndc-orderlist-api
- description: IATA NDC 21.3 OrderHistory message. Returns the change history of an order. This is the closest thing Virgin Atlantic publishes to a data-retrieval operation; it is per-order and is not a bulk export.
  name: Virgin Atlantic NDC OrderHistory API
  slug: virgin-atlantic-ndc-orderhistory-api
artifact_total: 15
asyncapis:
- description: ''
  name: Virgin Atlantic Orderchangenotif Webhooks
  slug: virgin-atlantic-orderchangenotif-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.virginatlantic.com/
- group: start
  title: ''
  type: Portal
  url: https://ndc.virginatlantic.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ndc.virginatlantic.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.virginatlantic.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://ndc.virginatlantic.com/docs
- group: start
  title: ''
  type: SignUp
  url: https://ndc.virginatlantic.com/account/register
- group: auth
  title: ''
  type: Authentication
  url: https://ndc.virginatlantic.com/help/how-to-start-your-build
- group: auth
  title: ''
  type: Authentication
  url: authentication/virgin-atlantic-authentication.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://ndc.virginatlantic.com/help/how-to-access-ndc-apis
- group: auth
  title: ''
  type: Certification
  url: https://ndc.virginatlantic.com/certification
- group: operate
  title: ''
  type: Roadmap
  url: https://ndc.virginatlantic.com/capability/ndc-roadmap
- group: operate
  title: ''
  type: ChangeLog
  url: https://ndc.virginatlantic.com/product-release
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/virgin-atlantic-changelog.yml
- group: operate
  title: ''
  type: Support
  url: https://ndc.virginatlantic.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://ndc.virginatlantic.com/faq
- group: company
  title: ''
  type: Blog
  url: https://ndc.virginatlantic.com/news
- group: docs
  title: ''
  type: XMLSchema
  url: schemas/21_3_3_NDC_Schema.zip
- group: design
  title: ''
  type: Conventions
  url: conventions/virgin-atlantic-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/virgin-atlantic-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/virgin-atlantic-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/virgin-atlantic-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/virgin-atlantic-orderchangenotif-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: https://ndc.virginatlantic.com/docs/testing-your-build
- group: start
  title: ''
  type: Sandbox
  url: sandbox/virgin-atlantic-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/virgin-atlantic-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/virgin-atlantic-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/virgin-atlantic-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/virgin-atlantic-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/virgin-atlantic-domain-security.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://flywith.virginatlantic.com/gb/en/partner-hub/policies.html
- group: other
  title: ''
  type: Policy
  url: https://flywith.virginatlantic.com/gb/en/partner-hub/policies/distribution-policy.html
- group: other
  title: ''
  type: Policy
  url: https://flywith.virginatlantic.com/gb/en/partner-hub/policies/NDC_Novation_Policy.html
- group: other
  title: ''
  type: Policy
  url: https://flywith.virginatlantic.com/gb/en/partner-hub/policies/booking-policy.html
- group: commercial
  title: ''
  type: Privacy
  url: https://www.virginatlantic.com/policies/virgin-atlantic-airways-and-virgin-atlantic-holidays-privacy-notice
created: '2026-07-28'
description: Virgin Atlantic Airways is a United Kingdom long-haul carrier (IATA code VS) based at London Heathrow and Manchester, operating a transatlantic joint venture with Delta Air Lines, Air France-KLM and SkyTeam, and a SkyTeam member since 2023. In the distribution chain it sits as an airline supplier that reaches travel sellers through three routes at once - the legacy GDSs (Amadeus, Sabre, Travelport, all under renewed multi-year content agreements), its own IATA NDC direct connect, and its own consumer channels. Its API posture is distribution-only and honestly gated. Virgin Atlantic publishes no consumer, flight-status or loyalty API, and no OpenAPI or machine-readable API description of any kind. What it does publish, openly and without a login, is the VS NDC Connect portal at ndc.virginatlantic.com - full request and response reference documentation for twelve IATA NDC 21.3 messages, XML samples, workflow diagrams, a certification programme, and downloadable IATA NDC 21.3.3
  XSD schema assets. The contract itself is the IATA NDC standard rather than a Virgin-specific shape, but getting a key is not self-serve - production access requires valid IATA accreditation and Virgin Atlantic ticketing authority (or a service-provider connection), a signed Technical User Agreement, Data Processing Agreement and Agency Sales Agreement, and at minimum RED tier certification. There is no bulk export operation and no published base URL - public docs, accreditation required, no exit path.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-28'
name: Virgin Atlantic
nav: Providers
network: true
overview: 'Virgin Atlantic publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, United Kingdom, Aviation, Airline, and Distribution.


  The Virgin Atlantic catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Virgin Atlantic''s developer surface includes developer portal, documentation, API reference, signup flow, authentication, getting-started guide, changelog, and 29 more developer resources.'
random_paper: 8
score:
  band: developing
  composite: 46.6
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 60.3
    discoverability: 83.3
    governance: 22.9
    operational_transparency: 28.9
  provenance:
    conformance: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
security:
- kind: authentication
  name: Virgin Atlantic Authentication
  slug: virgin-atlantic-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Virgin Atlantic Domain Security
  slug: virgin-atlantic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: virgin-atlantic
tags:
- Travel
- United Kingdom
- Aviation
- Airline
- Distribution
- NDC
- Booking
- GDS
website: https://www.virginatlantic.com/
---
