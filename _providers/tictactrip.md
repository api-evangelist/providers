---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
