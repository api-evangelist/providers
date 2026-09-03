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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 30.7
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Tictactrip Agentic Access
  operation_count: 20
  slug: tictactrip-agentic-access
  summary_line: 20 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The Autocomplete API from TicTacTrip — 1 operation(s) for autocomplete.
  name: TicTacTrip Autocomplete API
  slug: tictactrip-autocomplete-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The Booking API from TicTacTrip — 9 operation(s) for booking.
  name: TicTacTrip Booking API
  slug: tictactrip-booking-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The Cities API from TicTacTrip — 2 operation(s) for cities.
  name: TicTacTrip Cities API
  slug: tictactrip-cities-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The Results API from TicTacTrip — 1 operation(s) for results.
  name: TicTacTrip Results API
  slug: tictactrip-results-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The SegmentProviders API from TicTacTrip — 1 operation(s) for segmentproviders.
  name: TicTacTrip SegmentProviders API
  slug: tictactrip-segmentproviders-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The StopClusters API from TicTacTrip — 2 operation(s) for stopclusters.
  name: TicTacTrip StopClusters API
  slug: tictactrip-stopclusters-api
- baseURL: https://api.tictactrip.eu
  baseurl_source: declared
  description: The StopGroups API from TicTacTrip — 2 operation(s) for stopgroups.
  name: TicTacTrip StopGroups API
  slug: tictactrip-stopgroups-api
artifact_total: 18
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/tictactrip-capability-edges.yml
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
  type: X-MCPServerCandidate
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
modified: '2026-07-21'
name: TicTacTrip
nav: Providers
network: true
overview: 'TicTacTrip publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Autocomplete API, Booking API, Cities API, and 4 more. Tagged areas include Company, Travel, Transportation, Trains, and Bus.


  TicTacTrip''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 20 more developer resources.'
random_paper: 8
score:
  band: thin
  composite: 36.6
  coverage:
    artifact_dirs: 17
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 49.5
    developer_ergonomics: 68.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 36.6
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
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tictactrip/refs/heads/main/screenshots/tictactrip-2026-09-02T163709.png
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
- Bus
- Booking
- Mobility
- Multi-Modal
- Ticketing
website: https://tictactrip.eu/
---
