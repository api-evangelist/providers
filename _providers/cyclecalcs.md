---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Cyclecalcs Agentic Access
  operation_count: 29
  slug: cyclecalcs-agentic-access
  summary_line: 29 operations
api_count: 1
apis:
- description: Hosted stateless Streamable HTTP MCP server exposing 11 astronomy tools backed by the v2 REST endpoints. Requires Bearer RapidAPI key on every call; basic plan free. Works with Claude Code, custom con
  name: CycleCalcs MCP Server
  slug: cyclecalcs-mcp-server
- description: The Apsides API from CycleCalcs — 1 operation(s) for apsides.
  name: CycleCalcs Apsides API
  slug: cyclecalcs-apsides-api
- description: The Attribution API from CycleCalcs — 1 operation(s) for attribution.
  name: CycleCalcs Attribution API
  slug: cyclecalcs-attribution-api
- description: The Conjunctions API from CycleCalcs — 1 operation(s) for conjunctions.
  name: CycleCalcs Conjunctions API
  slug: cyclecalcs-conjunctions-api
- description: The Conventions API from CycleCalcs — 1 operation(s) for conventions.
  name: CycleCalcs Conventions API
  slug: cyclecalcs-conventions-api
- description: The CycleCalcs Astronomy API API from CycleCalcs — 1 operation(s) for cyclecalcs astronomy api.
  name: CycleCalcs CycleCalcs Astronomy API API
  slug: cyclecalcs-cyclecalcs-astronomy-api-api
- description: The Cycles API from CycleCalcs — 1 operation(s) for cycles.
  name: CycleCalcs Cycles API
  slug: cyclecalcs-cycles-api
- description: The Dark Window API from CycleCalcs — 1 operation(s) for dark window.
  name: CycleCalcs Dark Window API
  slug: cyclecalcs-dark-window-api
- description: The Eclipses API from CycleCalcs — 1 operation(s) for eclipses.
  name: CycleCalcs Eclipses API
  slug: cyclecalcs-eclipses-api
- description: The Enums API from CycleCalcs — 1 operation(s) for enums.
  name: CycleCalcs Enums API
  slug: cyclecalcs-enums-api
- description: The Equation Of Time API from CycleCalcs — 1 operation(s) for equation of time.
  name: CycleCalcs Equation Of Time API
  slug: cyclecalcs-equation-of-time-api
- description: The Jupiter Moons API from CycleCalcs — 1 operation(s) for jupiter moons.
  name: CycleCalcs Jupiter Moons API
  slug: cyclecalcs-jupiter-moons-api
- description: The Libration API from CycleCalcs — 1 operation(s) for libration.
  name: CycleCalcs Libration API
  slug: cyclecalcs-libration-api
- description: The Moon API from CycleCalcs — 1 operation(s) for moon.
  name: CycleCalcs Moon API
  slug: cyclecalcs-moon-api
- description: The Moon Nodes API from CycleCalcs — 1 operation(s) for moon nodes.
  name: CycleCalcs Moon Nodes API
  slug: cyclecalcs-moon-nodes-api
- description: The Phases API from CycleCalcs — 1 operation(s) for phases.
  name: CycleCalcs Phases API
  slug: cyclecalcs-phases-api
- description: The Places API from CycleCalcs — 1 operation(s) for places.
  name: CycleCalcs Places API
  slug: cyclecalcs-places-api
- description: The Planet Board API from CycleCalcs — 1 operation(s) for planet board.
  name: CycleCalcs Planet Board API
  slug: cyclecalcs-planet-board-api
- description: The Planet Events API from CycleCalcs — 1 operation(s) for planet events.
  name: CycleCalcs Planet Events API
  slug: cyclecalcs-planet-events-api
- description: The Positions API from CycleCalcs — 1 operation(s) for positions.
  name: CycleCalcs Positions API
  slug: cyclecalcs-positions-api
- description: The Retrogrades API from CycleCalcs — 1 operation(s) for retrogrades.
  name: CycleCalcs Retrogrades API
  slug: cyclecalcs-retrogrades-api
- description: The Rise Set API from CycleCalcs — 1 operation(s) for rise set.
  name: CycleCalcs Rise Set API
  slug: cyclecalcs-rise-set-api
- description: The Seasons API from CycleCalcs — 1 operation(s) for seasons.
  name: CycleCalcs Seasons API
  slug: cyclecalcs-seasons-api
- description: The Separation API from CycleCalcs — 1 operation(s) for separation.
  name: CycleCalcs Separation API
  slug: cyclecalcs-separation-api
- description: The Sidereal Time API from CycleCalcs — 1 operation(s) for sidereal time.
  name: CycleCalcs Sidereal Time API
  slug: cyclecalcs-sidereal-time-api
- description: The Sky Quality API from CycleCalcs — 1 operation(s) for sky quality.
  name: CycleCalcs Sky Quality API
  slug: cyclecalcs-sky-quality-api
- description: The Sun API from CycleCalcs — 1 operation(s) for sun.
  name: CycleCalcs Sun API
  slug: cyclecalcs-sun-api
- description: The Time API from CycleCalcs — 1 operation(s) for time.
  name: CycleCalcs Time API
  slug: cyclecalcs-time-api
- description: The Today API from CycleCalcs — 1 operation(s) for today.
  name: CycleCalcs Today API
  slug: cyclecalcs-today-api
- description: The Twilight API from CycleCalcs — 1 operation(s) for twilight.
  name: CycleCalcs Twilight API
  slug: cyclecalcs-twilight-api
arazzos:
- description: Resolve an observer, then ask the eclipse endpoint for an explicit visible-from-here answer with local contact times.
  name: Is the next eclipse visible from here
  slug: cyclecalcs-eclipse-visibility
- description: One ranged request for the solar day, one for daily moon state, one for the quarter instants — a month of calendar in three calls, not ninety.
  name: Build a sun and moon calendar for a location
  slug: cyclecalcs-sun-moon-calendar
- description: Resolve a place name, take the whole-sky snapshot, then find the dark moonless observing window for the next week.
  name: Tonight's sky for a place
  slug: cyclecalcs-tonights-sky
artifact_total: 83
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CycleCalcs Astronomy Apsides API
  slug: open-cyclecalcs-apsides-api
- collection_type: open
  name: CycleCalcs Astronomy Attribution API
  slug: open-cyclecalcs-attribution-api
- collection_type: open
  name: CycleCalcs Astronomy Conjunctions API
  slug: open-cyclecalcs-conjunctions-api
- collection_type: open
  name: CycleCalcs Astronomy Conventions API
  slug: open-cyclecalcs-conventions-api
- collection_type: open
  name: CycleCalcs Astronomy CycleCalcs Astronomy API API
  slug: open-cyclecalcs-cyclecalcs-astronomy-api-api
- collection_type: open
  name: CycleCalcs Astronomy Cycles API
  slug: open-cyclecalcs-cycles-api
- collection_type: open
  name: CycleCalcs Astronomy Dark Window API
  slug: open-cyclecalcs-dark-window-api
- collection_type: open
  name: CycleCalcs Astronomy Eclipses API
  slug: open-cyclecalcs-eclipses-api
- collection_type: open
  name: CycleCalcs Astronomy Enums API
  slug: open-cyclecalcs-enums-api
- collection_type: open
  name: CycleCalcs Astronomy Equation Of Time API
  slug: open-cyclecalcs-equation-of-time-api
- collection_type: open
  name: CycleCalcs Astronomy Jupiter Moons API
  slug: open-cyclecalcs-jupiter-moons-api
- collection_type: open
  name: CycleCalcs Astronomy Libration API
  slug: open-cyclecalcs-libration-api
- collection_type: open
  name: CycleCalcs Astronomy Moon API
  slug: open-cyclecalcs-moon-api
- collection_type: open
  name: CycleCalcs Astronomy Moon Nodes API
  slug: open-cyclecalcs-moon-nodes-api
- collection_type: open
  name: CycleCalcs Astronomy Phases API
  slug: open-cyclecalcs-phases-api
- collection_type: open
  name: CycleCalcs Astronomy Places API
  slug: open-cyclecalcs-places-api
- collection_type: open
  name: CycleCalcs Astronomy Planet Board API
  slug: open-cyclecalcs-planet-board-api
- collection_type: open
  name: CycleCalcs Astronomy Planet Events API
  slug: open-cyclecalcs-planet-events-api
- collection_type: open
  name: CycleCalcs Astronomy Positions API
  slug: open-cyclecalcs-positions-api
- collection_type: open
  name: CycleCalcs Astronomy Retrogrades API
  slug: open-cyclecalcs-retrogrades-api
- collection_type: open
  name: CycleCalcs Astronomy Rise Set API
  slug: open-cyclecalcs-rise-set-api
- collection_type: open
  name: CycleCalcs Astronomy Seasons API
  slug: open-cyclecalcs-seasons-api
- collection_type: open
  name: CycleCalcs Astronomy Separation API
  slug: open-cyclecalcs-separation-api
- collection_type: open
  name: CycleCalcs Astronomy Sidereal Time API
  slug: open-cyclecalcs-sidereal-time-api
- collection_type: open
  name: CycleCalcs Astronomy Sky Quality API
  slug: open-cyclecalcs-sky-quality-api
- collection_type: open
  name: CycleCalcs Astronomy Sun API
  slug: open-cyclecalcs-sun-api
- collection_type: open
  name: CycleCalcs Astronomy Time API
  slug: open-cyclecalcs-time-api
- collection_type: open
  name: CycleCalcs Astronomy Today API
  slug: open-cyclecalcs-today-api
- collection_type: open
  name: CycleCalcs Astronomy Twilight API
  slug: open-cyclecalcs-twilight-api
- collection_type: open
  name: API Collection
  slug: open-cyclecalcs-v2-discovery
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/cyclecalcs-astronomy-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cyclecalcs-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cyclecalcs-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cyclecalcs-authentication.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.cyclecalcs.com/api.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.cyclecalcs.com/api/reference.html
- group: docs
  title: ''
  type: APIReference
  url: https://www.cyclecalcs.com/api/reference.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.cyclecalcs.com/api.html
- group: operate
  title: ''
  type: Support
  url: https://www.cyclecalcs.com/about.html
- group: commercial
  title: ''
  type: Pricing
  url: https://rapidapi.com/info-8KZIhinZ9/api/cyclecalcs-astronomy-api3
- group: start
  title: ''
  type: SignUp
  url: https://rapidapi.com/info-8KZIhinZ9/api/cyclecalcs-astronomy-api3
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cyclecalcs.com/api/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cyclecalcs.com/privacy.html
- group: operate
  title: ''
  type: StatusPage
  url: https://stats.uptimerobot.com/b2ue50rVZI
- group: operate
  title: ''
  type: Deprecation
  url: https://www.cyclecalcs.com/api/versioning.html
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cyclecalcs-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cyclecalcs-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/cyclecalcs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cyclecalcs-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cyclecalcs-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cyclecalcs-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.cyclecalcs.com/.well-known/api-catalog
- group: build
  title: ''
  type: Packages
  url: packages/cyclecalcs-packages.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/cyclecalcs-vocabulary.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/cyclecalcs-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/cyclecalcs-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/cyclecalcs-components.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cyclecalcs-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cyclecalcs-plans.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cyclecalcs-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cyclecalcs-tonights-sky.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cyclecalcs-eclipse-visibility.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/cyclecalcs-sun-moon-calendar.yml
created: '2026-08-09'
description: 'CycleCalcs publishes a read-only positional-astronomy engine as both a REST API and a hosted MCP server over the same core: sun and moon rise/set and twilight, moon phases and libration, planet positions and a visibility board, eclipses with per-observer local circumstances, seasons, apsides, lunar nodes, retrograde stations, conjunctions and angular separation, sidereal time, the equation of time, Jupiter''s Galilean moons, sky quality and dark-sky windows, place lookup, and a one-call whole-sky snapshot. It returns the named answer and the numbers behind it rather than raw ephemeris, and every response states its frame, epoch, time scale and refraction model. Computed live with the MIT-licensed Astronomy Engine, arcminute class for the Sun, Moon and planets from 1700 to 2200. Twenty-nine GET endpoints, JSON/CSV/TXT, RFC 9457 problem documents, open CORS, and a free tier that needs no key, no signup and no card; paid volume tiers sell through RapidAPI. Pure astronomy — no
  astrology and no claims that sky events affect people or Earth.'
examples:
- key_count: 9
  name: Cyclecalcs V2 Cycles Example
  slug: cyclecalcs-v2-cycles-example
- key_count: 9
  name: Cyclecalcs V2 Dark Window Example
  slug: cyclecalcs-v2-dark-window-example
- key_count: 9
  name: Cyclecalcs V2 Eclipses Example
  slug: cyclecalcs-v2-eclipses-example
- key_count: 9
  name: Cyclecalcs V2 Moon Example
  slug: cyclecalcs-v2-moon-example
- key_count: 9
  name: Cyclecalcs V2 Phases Example
  slug: cyclecalcs-v2-phases-example
- key_count: 9
  name: Cyclecalcs V2 Places Example
  slug: cyclecalcs-v2-places-example
- key_count: 9
  name: Cyclecalcs V2 Planet Board Example
  slug: cyclecalcs-v2-planet-board-example
- key_count: 9
  name: Cyclecalcs V2 Planet Events Example
  slug: cyclecalcs-v2-planet-events-example
- key_count: 9
  name: Cyclecalcs V2 Positions Example
  slug: cyclecalcs-v2-positions-example
- key_count: 9
  name: Cyclecalcs V2 Rise Set Example
  slug: cyclecalcs-v2-rise-set-example
- key_count: 9
  name: Cyclecalcs V2 Sun Example
  slug: cyclecalcs-v2-sun-example
- key_count: 9
  name: Cyclecalcs V2 Today Example
  slug: cyclecalcs-v2-today-example
image: https://www.cyclecalcs.com/assets/og-card.png?v=2
layout: provider
mcp_servers:
- description: ''
  name: CycleCalcs MCP Server
  slug: cyclecalcs-mcp-server
- description: CycleCalcs publishes a hosted, stateless Streamable HTTP MCP server that exposes eleven read-only astronomy tools, each backed by exactly one live /v2 REST endpoint. The server speaks MCP revision 202
  name: MCP server manifest (11 tools, captured from tools/list)
  slug: mcp-server-manifest-11-tools-captured-from-toolslist
modified: '2026-08-09'
name: CycleCalcs
nav: Providers
network: true
overview: 'CycleCalcs publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Apsides API, Attribution API, Conjunctions API, and 26 more. Tagged areas include Astronomy, Space, Science, Ephemeris, and Sun.


  CycleCalcs'' developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Cyclecalcs Plans
  plan_count: 4
  slug: cyclecalcs-plans
random_paper: 17
rate_limits:
- limit_count: 15
  name: Cyclecalcs Rate Limits
  slug: cyclecalcs-rate-limits
score:
  band: strong
  composite: 63.5
  coverage:
    artifact_dirs: 25
    catalog_gap: 49.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 33.3
    contract_quality: 62.5
    developer_ergonomics: 63.7
    discoverability: 87.0
    governance: 33.3
    operational_transparency: 55.3
  previous_composite: 63.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 96.7
      derived: 0
      marker_coverage: 0.0
      total: 30
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cyclecalcs/refs/heads/main/screenshots/cyclecalcs-2026-08-17T080843.png
security:
- kind: authentication
  name: Cyclecalcs Authentication
  slug: cyclecalcs-authentication
  summary_line: none/apiKey · 4 schemes
- kind: domain-security
  name: Cyclecalcs Domain Security
  slug: cyclecalcs-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: cyclecalcs
tags:
- Astronomy
- Space
- Science
- Ephemeris
- Sun
- Moon
- Planets
- Eclipses
- Time
- Calendar
- Geolocation
- MCP
- agent-native
website: https://www.cyclecalcs.com/api.html
---
