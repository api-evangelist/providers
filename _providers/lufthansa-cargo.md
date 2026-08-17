---
access_model:
  confidence: high
  label: Application approval · portal registration reviewed by LH Cargo API managers
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://developer.lufthansa-cargo.com/partneronboardingprocess
  - https://developer.lufthansa-cargo.com/how-to-connect
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-17'
api_count: 10
apis:
- description: Retrieves the current status of an air freight shipment by IATA Air Waybill, keyed on a 3-digit AWB prefix (020 = Lufthansa Cargo) plus an 8-digit AWB number. Returns the milestone plan, booking, flig
  name: Lufthansa Cargo Shipment Tracking API
  slug: lufthansa-cargo-shipment-tracking-api
- description: Subscription API that pushes shipment milestone updates to a caller-supplied HTTPS callback URL. Create, read, update, delete and list subscriptions for a given Air Waybill and status filter; the Open
  name: Lufthansa Cargo Shipment Tracking Subscribe API
  slug: lufthansa-cargo-shipment-tracking-subscribe-api
- description: Returns possible direct and connecting route offers between an origin and a destination 3-letter IATA airport code for a given departure date and Lufthansa Cargo product code, based on Latest Acceptan
  name: Lufthansa Cargo Routing Offer API
  slug: lufthansa-cargo-routing-offer-api
- description: Reference data for Lufthansa Cargo stations worldwide, keyed on 3-letter IATA station codes. Lists all station codes, returns detail for a single station, and accepts a POST batch of codes. Detail cov
  name: Lufthansa Cargo Station Information API
  slug: lufthansa-cargo-station-information-api
- description: 'Prior-agreement API. Lufthansa Cargo''s digital booking connect for forwarders wiring an in-house system to the carrier and for ePlatforms integrating LH Cargo offers and bookings. Documented services '
  name: Lufthansa Cargo smartBooking API
  slug: lufthansa-cargo-smartbooking-api
- description: Prior-agreement API. Manages advance notification of truck deliveries as an alternative to the Quick Drop-Off/Pick-Up page in the Lufthansa ePortal. Documented functions are Save (create Visit Declara
  name: Lufthansa Cargo TruckPreAdvice API
  slug: lufthansa-cargo-truck-preadvice-api
- description: 'Prior-agreement API behind the smartULD add-on service. Exposes sensory data from smart Unit Load Devices - ambient temperature, battery level, geodata - plus container check status from handling for '
  name: Lufthansa Cargo ULDStatus API
  slug: lufthansa-cargo-uld-status-api
- description: Prior-agreement API product named CargoXML in the Lufthansa Cargo portfolio, referencing the IATA Cargo-XML message standard. The portal publishes an OpenAPI 3.0.3 info block titled "CargoXML APIs" wh
  name: Lufthansa Cargo CargoXML API
  slug: lufthansa-cargo-cargoxml-api
- description: Prior-agreement API product listed as CargoIMP in the portfolio, referencing the legacy IATA Cargo Interchange Message Procedures EDI message set. The portal publishes an OpenAPI 3.0.1 info block titl
  name: Lufthansa Cargo CargoIMP API
  slug: lufthansa-cargo-cargoimp-api
- description: Prior-agreement API product covering airmail carriage for postal operators. The portal publishes an OpenAPI 3.0.3 info block titled "AirMail APIs" whose entire description is the prior-approval notice
  name: Lufthansa Cargo AirMail API
  slug: lufthansa-cargo-airmail-api
artifact_total: 14
collections:
- collection_type: open
  name: Routing Offer API
  slug: open-lufthansa-cargo-routing-offer-api
- collection_type: open
  name: Shipment Tracking API
  slug: open-lufthansa-cargo-shipment-tracking-api
- collection_type: open
  name: Shipment Tracking Subscribe API
  slug: open-lufthansa-cargo-shipment-tracking-subscribe-api
- collection_type: open
  name: Station Information API
  slug: open-lufthansa-cargo-station-information-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.lufthansa-cargo.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.lufthansa-cargo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.lufthansa-cargo.com/how-to-connect
- group: start
  title: ''
  type: Onboarding
  url: https://developer.lufthansa-cargo.com/partneronboardingprocess
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.lufthansa-cargo.com/terms
- group: operate
  title: ''
  type: Support
  url: https://developer.lufthansa-cargo.com/contact
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.lufthansa-cargo.com/news
- group: start
  title: ''
  type: SignUp
  url: https://developer.lufthansa-cargo.com/login
- group: start
  title: ''
  type: Sandbox
  url: https://developer-test.lufthansa-cargo.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/LufthansaCargo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lufthansa-cargo
created: '2026-07-30'
description: 'Lufthansa Cargo AG is the air freight arm of the Lufthansa Group, headquartered in Frankfurt, Germany. It sells and operates belly capacity across the Lufthansa passenger fleet plus its own Boeing 777F freighters, and runs the Frankfurt Cargo Center hub, so it sits in the chain as the airline carrier between the freight forwarder and the destination handling agent. Its API posture is real but two-speed: a live Apigee developer portal at developer.lufthansa-cargo.com publishes four OpenAPI 3.0 contracts anonymously downloadable without a login (Routing Offer, Shipment Tracking, Shipment Tracking Subscribe, Station Information), while six further API products in the same portfolio - smartBooking, Truck PreAdvice, ULD Status, AirMail, CargoXML and CargoIMP - are published only as info-block stubs carrying the sentence that access is granted upon prior approval and agreement. Registration is reviewed by Lufthansa Cargo API managers before keys are issued and production access requires
  successful test-environment validation, so this is application-approval, not self-serve. The published REST surface is a proprietary Lufthansa Cargo shape, but it carries open air-cargo vocabulary inside it - IATA AWB prefix 020 plus 8-digit AWB numbers, 3-letter IATA station codes and the IATA cargo status code set (RCS, MAN, DEP, ARR, RCF, NFD, DLV) - while the legacy Cargo-IMP and Cargo-XML EDI message sets remain in the portfolio as gated products and IATA ONE Record went live in July 2026 through the IBS Software ONE Record server rather than as anything Lufthansa Cargo publishes itself.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-30'
name: Lufthansa Cargo
nav: Providers
network: true
overview: 'Lufthansa Cargo publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Shipment Tracking API, Shipment Tracking Subscribe API, Routing Offer API, and 1 more. Tagged areas include Logistics, Supply Chain, Germany, Air Cargo, and Freight.


  Lufthansa Cargo''s developer surface includes documentation, support, changelog, signup flow, sandbox, and 6 more developer resources.'
random_paper: 45
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 23.7
    contract_quality: 53.7
    developer_ergonomics: 28.3
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.0
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lufthansa-cargo/refs/heads/main/screenshots/lufthansa-cargo-2026-08-07T171824.png
slug: lufthansa-cargo
tags:
- Logistics
- Supply Chain
- Germany
- Air Cargo
- Freight
- Track and Trace
- Standards
- Aviation
website: https://www.lufthansa-cargo.com/
---
