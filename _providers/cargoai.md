---
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
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.5
  scored_at: '2026-08-12'
api_count: 8
apis:
- description: Search live routes, schedules, capacity, availability and rates across CargoAi's airline network from a single POST /search call, returning quotable flight options with rate types, transit times and C
  name: CargoAi Routes, Schedules and Rates API
  slug: cargoai-routes-schedules-and-rates-api
- description: Book a quoted air cargo option, read a booking back by flight UUID, and cancel a booking made through CargoCONNECT. Booking updates from the airline are pushed back on a customer-registered booking ca
  name: CargoAi Booking API
  slug: cargoai-booking-api
- description: Subscribe an air waybill to CargoAi's milestone tracking service and receive event updates by webhook callback and email, or unsubscribe. Supports interline subscriptions that merge two carriers' mile
  name: CargoAi Track & Trace API
  slug: cargoai-track-and-trace-api
- description: Send master (FWB) and house (FHL) air waybill data to the airline handling a booking as JSON, with CargoAi parsing and formatting it into the IATA cargo message the airline expects, so the caller need
  name: CargoAi FWB & FHL API
  slug: cargoai-fwb-fhl-api
- description: Create, read, update and delete the end users an integrator carries under its own CargoCONNECT API key, and mint a redirection token that drops a user into the CargoMART portal without a separate logi
  name: CargoAi User Provisioning API
  slug: cargoai-user-provisioning-api
- description: Return the CO2 emissions for an air waybill or a specific flight leg, calculated per IATA Recommended Practice 1678 using the exact routing and aircraft code rather than an origin-destination approxim
  name: CargoAi Cargo2ZERO CO2 API
  slug: cargoai-cargo2zero-api
- description: AI extraction endpoints that turn an air waybill image or raw shipment email text into structured JSON that can be fed straight into the quote, book and eAWB endpoints, removing manual re-keying betwe
  name: CargoAi CargoCOPILOT API
  slug: cargoai-cargocopilot-api
- description: A hosted Model Context Protocol server that wraps the CargoCONNECT endpoints as tools for AI assistants - track a shipment by AWB, search flight rates, look up airline contacts and ground handling age
  name: CargoAi MCP Connector
  slug: cargoai-mcp-connector
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.cargoai.co/
- group: docs
  title: ''
  type: Documentation
  url: https://cargoai.readme.io/reference/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://cargoai.readme.io/reference/introduction
- group: agent
  title: ''
  type: LLMsTxt
  url: https://cargoai.readme.io/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://cargoai.readme.io/reference/changelog
- group: start
  title: ''
  type: SupportPortal
  url: https://help.cargoai.co/
- group: company
  title: ''
  type: Blog
  url: https://www.cargoai.co/blog/
- group: other
  title: ''
  type: ProductPage
  url: https://www.cargoai.co/products/cargoconnect/
- group: start
  title: ''
  type: Portal
  url: https://app.cargoai.co
- group: start
  title: ''
  type: SignUp
  url: https://connect.cargoai.co/
- group: operate
  title: ''
  type: Contact
  url: https://cargoai.readme.io/reference/contact-us
- group: other
  title: ''
  type: Coverage
  url: https://bi.cargoai.co/superset/dashboard/API_Coverage
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cargoai
- group: company
  title: ''
  type: LinkedIn
  url: https://sg.linkedin.com/company/cargoai
created: '2026-07-30'
description: CargoAi is a Singapore-headquartered air cargo technology company that operates CargoMART, a digital marketplace where freight forwarders search routes, schedules, capacity and rates across 680+ airlines, book them, transmit the electronic air waybill, and track the shipment end to end. It sits in the middle of the air cargo chain as an aggregator between forwarders and their TMS vendors on one side and airline reservation and messaging systems on the other. Its API posture is genuinely public in documentation and sales-gated in access - the CargoCONNECT developer portal at cargoai.readme.io is open to anyone with no login and publishes a real OpenAPI 3.1 definition per operation, but an x-api-key is issued only after a commercial conversation with the CargoAi enterprise team. The published contract is a proprietary REST shape rather than an IATA ONE Record interface, though the payloads it carries are IATA-native - AWB numbers with airline prefixes, IATA airport and airline
  codes, Special Handling Codes, IATA cargo status event codes, FWB and FHL message content, and CO2 figures computed per IATA Recommended Practice 1678.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/groq.png
layout: provider
modified: '2026-07-30'
name: CargoAi
nav: Providers
network: true
overview: 'CargoAi publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Routes, Schedules and Rates API, Booking API, Track & Trace API, and 4 more. Tagged areas include Logistics, Supply Chain, Singapore, Air Cargo, and Freight Forwarding.


  CargoAi''s developer surface includes documentation, API reference, changelog, engineering blog, developer portal, signup flow, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 22.4
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 14.6
    developer_ergonomics: 26.1
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.4
  provenance:
    contracts:
      callable: 100.0
      derived: 7
      marker_coverage: 100.0
      total: 7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cargoai/refs/heads/main/screenshots/cargoai-2026-08-07T163015.png
slug: cargoai
tags:
- Logistics
- Supply Chain
- Singapore
- Air Cargo
- Freight Forwarding
- Track and Trace
- Booking
- Marketplace
- Standards
website: https://www.cargoai.co/
---
