---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Air Canada Agentic Access
  operation_count: 10
  slug: air-canada-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 10
apis:
- description: IATA NDC 17.2 AirShopping message pair (AirShoppingRQ / AirShoppingRS). Shops one-way, round-trip and North America multicity itineraries and returns branded fare-family offers with per-passenger pric
  name: Air Canada NDC AirShopping API
  slug: air-canada-ndc-airshopping-api
- description: IATA NDC 17.2 OfferPrice message pair (OfferPriceRQ / OfferPriceRS). Returns detailed and comprehensive pricing for a selected offer, including base fare, tax breakdown, surcharges and fare rules, for
  name: Air Canada NDC OfferPrice API
  slug: air-canada-ndc-offerprice-api
- description: IATA NDC 17.2 ServiceList message pair (ServiceListRQ / ServiceListRS). Returns the optional and ancillary services purchasable against an offer or order, such as Maple Leaf Lounge access and Air Cana
  name: Air Canada NDC ServiceList API
  slug: air-canada-ndc-servicelist-api
- description: IATA NDC 17.2 SeatAvailability message pair (SeatAvailabilityRQ / SeatAvailabilityRS). Returns seat maps with advance and preferred seat pricing, either during a booking flow against an OfferID or aft
  name: Air Canada NDC SeatAvailability API
  slug: air-canada-ndc-seatavailability-api
- description: IATA NDC 17.2 OrderCreate message pair (OrderCreateRQ / OrderViewRS). Creates an actual reservation and returns an airline-assigned OrderID plus an Air Canada record locator and associated reservation
  name: Air Canada NDC OrderCreate API
  slug: air-canada-ndc-ordercreate-api
- description: IATA NDC 17.2 OrderRetrieve message pair (OrderRetrieveRQ / OrderViewRS). Retrieves a single Order by mandatory OrderID and Owner. Air Canada documents that retrieving a cancelled Order, a GDS booking
  name: Air Canada NDC OrderRetrieve API
  slug: air-canada-ndc-orderretrieve-api
- description: IATA NDC 17.2 OrderChange message pair (OrderChangeRQ / OrderViewRS). Applies servicing changes to an existing Order, including seat and ancillary servicing with or without itinerary change, passenger
  name: Air Canada NDC OrderChange API
  slug: air-canada-ndc-orderchange-api
- description: IATA NDC 17.2 OrderReshop message pair (OrderReshopRQ / OrderReshopRS). Reshops an existing Order to produce change offers, including partially flown itineraries and origin/destination replacement.
  name: Air Canada NDC OrderReshop API
  slug: air-canada-ndc-orderreshop-api
- description: IATA NDC 17.2 OrderCancel message pair (OrderCancelRQ / OrderCancelRS). Cancels an existing Order held by Air Canada, referenced by OrderID and Owner.
  name: Air Canada NDC OrderCancel API
  slug: air-canada-ndc-ordercancel-api
- description: IATA NDC 17.2 OrderChangeNotif message. Air Canada-initiated notification of changes made to an Order outside the seller's own request, such as schedule change or involuntary disruption handling.
  name: Air Canada NDC OrderChangeNotification API
  slug: air-canada-ndc-orderchangenotification-api
artifact_total: 14
asyncapis:
- description: ''
  name: Air Canada Ocn Webhooks
  slug: air-canada-ocn-webhooks
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/air-canada-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/air-canada-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/air-canada-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/air-canada-error-codes.yml
- group: build
  title: ''
  type: DeclineCodes
  url: errors/air-canada-decline-codes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/air-canada-ocn-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/air-canada-sandbox.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/air-canada-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/air-canada-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/air-canada-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/air-canada-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/air-canada-vocabulary.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/air-canada-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/air-canada-packages.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/air-canada-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aircanada.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ndc.aircanada.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/api/documentation/ndcapis
- group: docs
  title: ''
  type: APIReference
  url: https://ndc.aircanada.com/api/documentation/ndcapis
- group: start
  title: ''
  type: GettingStarted
  url: https://ndc.aircanada.com/api/gettingstarted/gettingstarted
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/api/gettingstarted/apisetup
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/api/gettingstarted/sellersetup
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/api/gettingstarted/apisorchestration
- group: build
  title: ''
  type: Examples
  url: https://ndc.aircanada.com/api/gettingstarted/testdata
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/api/documentation/scenario
- group: start
  title: ''
  type: SignUp
  url: https://ndc.aircanada.com/seller-registration-form
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/ndc-program/registration
- group: company
  title: ''
  type: Partners
  url: https://ndc.aircanada.com/ndc-program/connection-options
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/ndc-program/ndc-capabilities
- group: start
  title: ''
  type: Sandbox
  url: https://gold-ndc-sandbox.aircanada.com/login
- group: operate
  title: ''
  type: Support
  url: https://ndc.aircanada.com/support
- group: operate
  title: ''
  type: FAQ
  url: https://ndc.aircanada.com/support/faq
- group: docs
  title: ''
  type: Documentation
  url: https://ndc.aircanada.com/support/knownissues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aircanada
- group: operate
  title: ''
  type: StatusPage
  url: https://ndc.aircanada.com/support/statusMonitoring
- group: operate
  title: ''
  type: ChangeLog
  url: https://ndc.aircanada.com/api/releasenotes/latestrelease
- group: operate
  title: ''
  type: Roadmap
  url: https://ndc.aircanada.com/api/roadmap
- group: docs
  title: ''
  type: Documentation
  url: https://www.aircanada.com/ca/en/aco/home/ndc.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.aircanada.com/content/dam/aircanada/portal/documents/PDF/ndc-displayRequirements-en.pdf
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aircanada.com/ca/en/aco/home/legal/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aircanada.com/ca/en/aco/home/legal/privacy-policy.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/air-canada
created: '2026-07-28'
description: 'Air Canada is Canada''s flag carrier and largest airline, headquartered in Montreal, operating scheduled passenger service under the AC designator along with Air Canada Rouge, Air Canada Express and the Aeroplan loyalty programme. Its home market is Canada, where it forms a duopoly with WestJet. Air Canada sits at the supply end of the travel distribution chain: it is the sole source of its own seat inventory, reached either through the legacy GDS EDIFACT channel (Amadeus, Sabre, Travelport), through certified NDC aggregators, or directly through its own NDC API. Its API posture is unusual for a carrier in that the distribution surface is genuinely well documented in public: the ndc.aircanada.com developer portal publishes complete IATA NDC 17.2 (EDIST) message documentation, request/response element tables, error catalogues, use cases and downloadable sample XML with no login. What is not public is access itself - production credentials require a commercial agreement with
  Air Canada''s distribution team, accredited IATA/ARC codes passed on every request, and passing Air Canada display certification test cases. There is no consumer API (no public flight status, booking or Aeroplan endpoint), no OpenAPI or machine-readable contract, no bulk export operation, and Air Canada publishes that it may revoke NDC programme access at its sole discretion. Public docs, gated access, no exit path.'
image: https://www.aircanada.com/favicon.ico
layout: provider
modified: '2026-07-28'
name: Air Canada
nav: Providers
network: true
overview: 'Air Canada publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Canada, Aviation, Airline, and NDC.


  The Air Canada catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Air Canada''s developer surface includes authentication, sandbox, changelog, code examples, documentation, API reference, getting-started guide, and 37 more developer resources.'
random_paper: 16
score:
  band: thin
  composite: 32.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 73.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 48.1
    developer_ergonomics: 23.2
    discoverability: 74.1
    governance: 22.0
    operational_transparency: 10.5
  previous_composite: 32.3
  provenance:
    agentic_access: derived
    conformance: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
security:
- kind: authentication
  name: Air Canada Authentication
  slug: air-canada-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Air Canada Domain Security
  slug: air-canada-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: air-canada
tags:
- Travel
- Canada
- Aviation
- Airline
- NDC
- Distribution
- Booking
- Airlines
- Loyalty
website: https://www.aircanada.com/
---
