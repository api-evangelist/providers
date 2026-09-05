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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.2
  scored_at: '2026-09-04'
api_count: 7
apis:
- description: A hosted Model Context Protocol server that wraps the CargoCONNECT endpoints as tools for AI assistants - track a shipment by AWB, search flight rates, look up airline contacts and ground handling age
  name: CargoAi MCP Connector
  slug: cargoai-mcp-connector
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Ai API from CargoAi — 2 operation(s) for ai.
  name: CargoAi AI API
  slug: cargoai-ai-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Book API from CargoAi — 1 operation(s) for book.
  name: CargoAi Book API
  slug: cargoai-book-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Bookings API from CargoAi — 1 operation(s) for bookings.
  name: CargoAi Bookings API
  slug: cargoai-bookings-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Co2calculation API from CargoAi — 1 operation(s) for co2calculation.
  name: CargoAi Co2calculation API
  slug: cargoai-co2calculation-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Eawb API from CargoAi — 1 operation(s) for eawb.
  name: CargoAi Eawb API
  slug: cargoai-eawb-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Search API from CargoAi — 1 operation(s) for search.
  name: CargoAi Search API
  slug: cargoai-search-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Track API from CargoAi — 3 operation(s) for track.
  name: CargoAi Track API
  slug: cargoai-track-api
- baseURL: https://api.cargoai.co/solutions
  baseurl_source: declared
  description: The Users API from CargoAi — 1 operation(s) for users.
  name: CargoAi Users API
  slug: cargoai-users-api
artifact_total: 16
collections:
- collection_type: open
  name: Solutions
  slug: open-cargoai-booking-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-cargo2zero-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-cargocopilot-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-fwb-fhl-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-routes-schedules-and-rates-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-track-and-trace-api
- collection_type: open
  name: Solutions
  slug: open-cargoai-user-provisioning-api
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
layout: provider
modified: '2026-07-30'
name: CargoAi
nav: Providers
network: true
overview: 'CargoAi publishes 8 APIs on the [APIs.io](https://apis.io/) network, including AI API, Book API, Bookings API, and 5 more. Tagged areas include Logistics, Supply Chain, Singapore, Air Cargo, and Freight Forwarding.


  CargoAi''s developer surface includes documentation, API reference, changelog, engineering blog, developer portal, signup flow, and 8 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 16.9
  coverage:
    artifact_dirs: 5
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 15.3
    developer_ergonomics: 22.6
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 16.9
  provenance:
    contracts:
      callable: 100.0
      derived: 8
      marker_coverage: 100.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-04'
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
