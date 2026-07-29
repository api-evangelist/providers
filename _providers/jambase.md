---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Jambase Agentic Access
  operation_count: 17
  slug: jambase-agentic-access
  summary_line: 17 operations
api_count: 7
apis:
- description: Search Artists
  name: JamBase Artists API
  slug: jambase-artists-api
- description: Search Events
  name: JamBase Events API
  slug: jambase-events-api
- description: Lookup Genres
  name: JamBase Genres API
  slug: jambase-genres-api
- description: Lookup Countries, Cities, Etc
  name: JamBase Geographies API
  slug: jambase-geographies-api
- description: Lookup Identifiers
  name: JamBase Lookups API
  slug: jambase-lookups-api
- description: Search Streams
  name: JamBase Streams API
  slug: jambase-streams-api
- description: Search Venues
  name: JamBase Venues API
  slug: jambase-venues-api
artifact_total: 42
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/jambase-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/jambase-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jambase-domain-security.yml
- group: auth
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
  type: MCP
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
- name: Jambase Finops
  service_category: Live Music Data
  slug: jambase-finops
image: https://www.jambase.com/favicon.ico
json_schemas:
- name: Concert
  property_count: 0
  slug: concert
- name: Event
  property_count: 0
  slug: event
- name: Festival
  property_count: 0
  slug: festival
- name: Genre
  property_count: 2
  slug: genre
- name: JamBase Concert Data API Schemas
  property_count: 0
  slug: jambase-schemas
- name: MusicGroup
  property_count: 0
  slug: musicgroup
- name: MusicVenue
  property_count: 0
  slug: musicvenue
- name: Offer
  property_count: 0
  slug: offer
- name: Stream
  property_count: 0
  slug: stream
jsonld:
- class_count: 41
  name: Jambase Context
  property_count: 2
  slug: jambase-context
layout: provider
modified: '2026-06-13'
name: JamBase
nav: Providers
network: true
overview: 'JamBase publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Artists API, Events API, Genres API, and 4 more. Tagged areas include Artists, Concerts, Events, Festivals, and Live Music.


  The JamBase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  JamBase''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, and 7 more developer resources.'
plans:
- name: Jambase Plans Pricing
  plan_count: 5
  slug: jambase-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 9
  name: Jambase Rate Limits
  slug: jambase-rate-limits
rules:
- name: JamBase API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 3
    warn: 3
  slug: jambase-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.0
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 72.8
    developer_ergonomics: 41.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 59.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jambase/refs/heads/main/screenshots/jambase-2026-06-20T183655.png
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
- Events
- Festivals
- Live Music
- Music
- Setlists
- Tickets
- Tours
- Venues
website: https://www.jambase.com
---
