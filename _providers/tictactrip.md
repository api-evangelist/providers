---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.8
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Tictactrip Agentic Access
  operation_count: 20
  slug: tictactrip-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 7
apis:
- description: The Autocomplete API from TicTacTrip — 1 operation(s) for autocomplete.
  name: TicTacTrip Autocomplete API
  slug: tictactrip-autocomplete-api
- description: The Booking API from TicTacTrip — 9 operation(s) for booking.
  name: TicTacTrip Booking API
  slug: tictactrip-booking-api
- description: The Cities API from TicTacTrip — 2 operation(s) for cities.
  name: TicTacTrip Cities API
  slug: tictactrip-cities-api
- description: The Results API from TicTacTrip — 1 operation(s) for results.
  name: TicTacTrip Results API
  slug: tictactrip-results-api
- description: The SegmentProviders API from TicTacTrip — 1 operation(s) for segmentproviders.
  name: TicTacTrip SegmentProviders API
  slug: tictactrip-segmentproviders-api
- description: The StopClusters API from TicTacTrip — 2 operation(s) for stopclusters.
  name: TicTacTrip StopClusters API
  slug: tictactrip-stopclusters-api
- description: The StopGroups API from TicTacTrip — 2 operation(s) for stopgroups.
  name: TicTacTrip StopGroups API
  slug: tictactrip-stopgroups-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: '@tictactrip/api Autocomplete API'
  slug: open-tictactrip-autocomplete-api
- collection_type: open
  name: '@tictactrip/api Autocomplete Booking API'
  slug: open-tictactrip-booking-api
- collection_type: open
  name: '@tictactrip/api Autocomplete Cities API'
  slug: open-tictactrip-cities-api
- collection_type: open
  name: '@tictactrip/api Autocomplete Results API'
  slug: open-tictactrip-results-api
- collection_type: open
  name: '@tictactrip/api Autocomplete SegmentProviders API'
  slug: open-tictactrip-segmentproviders-api
- collection_type: open
  name: '@tictactrip/api Autocomplete StopClusters API'
  slug: open-tictactrip-stopclusters-api
- collection_type: open
  name: '@tictactrip/api Autocomplete StopGroups API'
  slug: open-tictactrip-stopgroups-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tictactrip-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tictactrip-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tictactrip-authentication.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tictactrip-openapi-original.json
- group: other
  title: ''
  type: Overlay
  url: overlays/tictactrip-openapi-overlay.yaml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tictactrip-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tictactrip-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tictactrip-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tictactrip-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tictactrip.eu/
- group: design
  title: ''
  type: Conventions
  url: conventions/tictactrip-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tictactrip-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/tictactrip-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tictactrip-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tictactrip-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.tictactrip.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.tictactrip.eu/docs/intro
- group: docs
  title: ''
  type: APIReference
  url: https://developers.tictactrip.eu/api
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.tictactrip.eu/docs/intro
- group: build
  title: ''
  type: Postman
  url: https://github.com/tictactrip/documentation/blob/main/static/Tictactrip.postman_collection.json
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tictactrip
- group: operate
  title: ''
  type: Support
  url: mailto:dev@tictactrip.eu
- group: company
  title: ''
  type: Website
  url: https://tictactrip.eu/
created: '2026-07-17'
description: TicTacTrip is a European multimodal travel search and booking platform (Techstars-backed) that aggregates train and bus inventory from 250+ carriers across 20+ European countries into single, combined itineraries. Its REST API exposes stop and city discovery, multimodal itinerary search with CO2 emissions per journey, and a full booking workflow — cart, order, book, e-ticket and cancellation — authenticated with partner bearer JWTs (API_SEARCH_PARTNER / API_BOOK_PARTNER roles). API access is provisioned via sales@tictactrip.eu.
image: https://developers.tictactrip.eu/img/logoTextBlack.svg
layout: provider
mcp_servers:
- description: ''
  name: tictactrip-mcp.yml
  slug: tictactrip-mcpyml
modified: '2026-07-21'
name: TicTacTrip
nav: Providers
network: true
overview: 'TicTacTrip publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Booking API, Cities API, and 4 more. Tagged areas include Company, Travel, Transportation, Trains, and Buses.


  TicTacTrip''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
random_paper: 36
score:
  band: thin
  composite: 38.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 52.1
    developer_ergonomics: 64.7
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 21.1
  previous_composite: 38.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Tictactrip Authentication
  slug: tictactrip-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tictactrip Domain Security
  slug: tictactrip-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tictactrip
tags:
- Company
- Travel
- Transportation
- Trains
- Buses
- Booking
- Mobility
- Multimodal
- Ticketing
website: https://tictactrip.eu/
---
