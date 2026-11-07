---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: na
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jambase Agentic Access
  operation_count: 17
  slug: jambase-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Search Artists
  name: JamBase Artists API
  slug: jambase-artists-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Search Events
  name: JamBase Events API
  slug: jambase-events-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Lookup Genres
  name: JamBase Genres API
  slug: jambase-genres-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Lookup Countries, Cities, Etc
  name: JamBase Geographies API
  slug: jambase-geographies-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Lookup Identifiers
  name: JamBase Lookups API
  slug: jambase-lookups-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Search Streams
  name: JamBase Streams API
  slug: jambase-streams-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: Search Venues
  name: JamBase Venues API
  slug: jambase-venues-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: The FestivalSeries API from JamBase — 3 operation(s) for festivalseries.
  name: JamBase Festival Series API
  slug: jambase-festivalseries-api
- baseURL: https://data.jambase.com/v3
  baseurl_source: declared
  description: The Usage API from JamBase — 1 operation(s) for usage.
  name: JamBase Usage API
  slug: jambase-usage-api
artifact_total: 53
collections:
- collection_type: open
  name: JamBase Concert Data Artists API
  slug: open-jambase-artists-api
- collection_type: open
  name: JamBase Concert Data Artists Events API
  slug: open-jambase-events-api
- collection_type: open
  name: JamBase Concert Data Artists Genres API
  slug: open-jambase-genres-api
- collection_type: open
  name: JamBase Concert Data Artists Geographies API
  slug: open-jambase-geographies-api
- collection_type: open
  name: JamBase Concert Data Artists Lookups API
  slug: open-jambase-lookups-api
- collection_type: open
  name: JamBase Concert Data Artists Streams API
  slug: open-jambase-streams-api
- collection_type: open
  name: JamBase Concert Data Artists Venues API
  slug: open-jambase-venues-api
common:
- group: other
  href: https://artifacts.apis.io/jambase/capabilities/jambase-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/jambase-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/jambase/overview
- group: commercial
  href: https://artifacts.apis.io/jambase/plans/jambase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/jambase-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/jambase/rate-limits/jambase-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jambase-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/jambase/finops/jambase-finops.yml
  title: ''
  type: FinOps
  url: finops/jambase-finops.yml
- group: agent
  href: https://artifacts.apis.io/jambase/agentic-access/jambase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/jambase-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/jambase/security/jambase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/jambase-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/jambase/security/jambase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jambase-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/jambase/authentication/jambase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jambase-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://data.jambase.com
- group: docs
  title: ''
  type: Documentation
  url: https://data.jambase.com/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://data.jambase.com/api/docs/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://data.jambase.com/pricing
- group: other
  title: ''
  type: Data
  url: https://data.jambase.com/data
- group: agent
  title: ''
  type: MCPServer
  url: https://data.jambase.com/mcp
- group: company
  title: ''
  type: About
  url: https://data.jambase.com/about
- group: company
  title: ''
  type: Website
  url: https://www.jambase.com
- group: company
  title: ''
  type: Blog
  url: https://www.jambase.com/feed
created: '2026-06-13'
description: JamBase is a live music data platform with over 25 years of concert history, providing access to 5M+ performances, 616K+ artist profiles, 91K+ venues, and 20K+ festivals. Their REST API delivers real-time global show listings, festival schedules, artist metadata, venue details, and ticket pricing data. JamBase Data is trusted by Google, Spotify, and 450+ companies for jam band and concert discovery, setlist information, tour dates, and live music event data.
examples:
- key_count: 6
  name: Getartistdatasources
  slug: getArtistDataSources
- key_count: 6
  name: Getcountries
  slug: getCountries
- key_count: 6
  name: Geteventdatasources
  slug: getEventDataSources
- key_count: 6
  name: Getgenres
  slug: getGenres
- key_count: 6
  name: Getmetros
  slug: getMetros
- key_count: 6
  name: Getsingleartist
  slug: getSingleArtist
- key_count: 6
  name: Getsinglevenue
  slug: getSingleVenue
- key_count: 6
  name: Getstates
  slug: getStates
- key_count: 6
  name: Getstream
  slug: getStream
- key_count: 6
  name: Getupcomingevent
  slug: getUpcomingEvent
- key_count: 6
  name: Getvenuedatasources
  slug: getVenueDataSources
- key_count: 6
  name: Getstreamdatasources
  slug: getstreamDataSources
- key_count: 6
  name: Searchartists
  slug: searchArtists
- key_count: 6
  name: Searchcities
  slug: searchCities
- key_count: 6
  name: Searchevents
  slug: searchEvents
- key_count: 6
  name: Searchupcomingstreams
  slug: searchUpcomingStreams
- key_count: 6
  name: Searchvenues
  slug: searchVenues
finops:
- has_sources: true
  method: generated
  name: Jambase Finops
  primary_unit: ''
  service_category: Live Music Data
  slug: jambase-finops
  template: false
image: https://www.jambase.com/favicon.ico
json_schemas:
- name: Concert
  property_count: 9
  slug: concert
- name: Event
  property_count: 12
  slug: event
- name: Festival
  property_count: 5
  slug: festival
- name: Genre
  property_count: 2
  slug: genre
- name: JamBase Concert Data API Schemas
  property_count: 0
  slug: jambase-schemas
- name: MusicGroup
  property_count: 13
  slug: musicgroup
- name: MusicVenue
  property_count: 10
  slug: musicvenue
- name: Offer
  property_count: 6
  slug: offer
- name: Stream
  property_count: 7
  slug: stream
jsonld:
- class_count: 41
  name: Jambase Context
  property_count: 2
  slug: jambase-context
layout: provider
mcp_servers:
- description: ''
  name: JamBase MCP Server
  slug: mcp
- description: Remote MCP server at mcp.jambase.com over HTTP.
  name: JamBase MCP Server
  slug: jambase
modified: '2026-06-13'
name: JamBase
nav: Providers
network: true
overview: 'JamBase publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Artists API, Events API, Genres API, and 6 more. Tagged areas include Artists, Concerts, Event, Festivals, and Live Music.


  The JamBase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JamBase''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Jambase Plans Pricing
  plan_count: 5
  slug: jambase-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 9
  name: Jambase Rate Limits
  slug: jambase-rate-limits
rules:
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: JamBase — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: jambase-jsonschema-spectral-rules
score:
  band: developing
  composite: 40.9
  coverage:
    artifact_dirs: 20
    catalog_earned: 59.7
    catalog_earned_first_party: 0.0
    catalog_gap: 55.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 18.4
    contract_governance: 9.8
    contract_quality: 65.7
    developer_ergonomics: 46.4
    discoverability: 68.3
    operational_transparency: 18.4
  previous_composite: 40.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 52.9
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/jambase/jambase-2026-06-20T183655.png
security:
- kind: authentication
  name: Jambase Authentication
  slug: jambase-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Jambase Domain Security
  slug: jambase-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Jambase Vulnerability Disclosure
  slug: jambase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: jambase
tags:
- Artists
- Concerts
- Event
- Festivals
- Live Music
- Music
- Setlists
- Ticketing
- Tours
- Venues
website: https://www.jambase.com
---
