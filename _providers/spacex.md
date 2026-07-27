---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Spacex Agentic Access
  operation_count: 43
  slug: spacex-agentic-access
  summary_line: 43 operations · 13 acting
api_count: 15
apis:
- description: Community-maintained GraphQL gateways over the SpaceX REST data, providing typed schema access and nested-field selection across launches, rockets, missions, payloads, ships, and crew. Multiple commun
  name: SpaceX GraphQL API (community)
  slug: graphql-api
- description: Detailed info for serialized Dragon capsules.
  name: SpaceX (Community API) Capsules API
  slug: spacex-capsules-api
- description: Detailed info about SpaceX as a company (single document).
  name: SpaceX (Community API) Company API
  slug: spacex-company-api
- description: Detailed info for serialized first-stage cores.
  name: SpaceX (Community API) Cores API
  slug: spacex-cores-api
- description: Detailed info on Dragon crew members.
  name: SpaceX (Community API) Crew API
  slug: spacex-crew-api
- description: Detailed info about Dragon capsule versions.
  name: SpaceX (Community API) Dragons API
  slug: spacex-dragons-api
- description: Detailed info on SpaceX historical events.
  name: SpaceX (Community API) History API
  slug: spacex-history-api
- description: Detailed info about landing pads and droneships.
  name: SpaceX (Community API) Landpads API
  slug: spacex-landpads-api
- description: Detailed info about SpaceX launches (v4 and v5).
  name: SpaceX (Community API) Launches API
  slug: spacex-launches-api
- description: Detailed info about launchpads.
  name: SpaceX (Community API) Launchpads API
  slug: spacex-launchpads-api
- description: Detailed info about launch payloads.
  name: SpaceX (Community API) Payloads API
  slug: spacex-payloads-api
- description: Detailed info about Elon Musk's Tesla Roadster ephemeris.
  name: SpaceX (Community API) Roadster API
  slug: spacex-roadster-api
- description: Detailed info about rocket versions.
  name: SpaceX (Community API) Rockets API
  slug: spacex-rockets-api
- description: Detailed info about ships in the SpaceX fleet.
  name: SpaceX (Community API) Ships API
  slug: spacex-ships-api
- description: Detailed info about Starlink satellites and orbits.
  name: SpaceX (Community API) Starlink API
  slug: spacex-starlink-api
artifact_total: 68
collections:
- collection_type: open
  name: SpaceX REST API
  slug: open-spacex-rest-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spacex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spacex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spacex-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/r-spacex/SpaceX-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/r-spacex
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/r-spacex/SpaceX-API
- group: commercial
  title: Apache License 2.0
  type: License
  url: https://github.com/r-spacex/SpaceX-API/blob/master/LICENSE
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/r-spacex/SpaceX-API/tree/master/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/r-spacex/SpaceX-API/blob/master/README.md
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/r-spacex/SpaceX-API/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/r-spacex/SpaceX-API/issues
- group: other
  title: ''
  type: PullRequests
  url: https://github.com/r-spacex/SpaceX-API/pulls
- group: operate
  title: ''
  type: Status
  url: https://status.spacexdata.com
- group: other
  title: ''
  type: Backups
  url: https://backups.spacexdata.com
- group: other
  title: ''
  type: DockerImage
  url: https://hub.docker.com/r/jakewmeyer/spacex-api/
- group: build
  title: ''
  type: Clients
  url: https://github.com/r-spacex/SpaceX-API/blob/master/docs/clients.md
- group: other
  title: ''
  type: Apps
  url: https://github.com/r-spacex/SpaceX-API/blob/master/docs/apps.md
- group: docs
  title: ''
  type: APIStyleGuide
  url: https://github.com/r-spacex/api-style-guide
- group: other
  title: ''
  type: Subreddit
  url: https://www.reddit.com/r/spacex/
- group: commercial
  title: ''
  type: Plans
  url: plans/spacex-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spacex-rate-limits.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/spacex-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/spacex-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/spacex-context.jsonld
- group: build
  title: MCP Server (community)
  type: Tools
  url: https://github.com/fercervantesx/lnl-spacex-mcp-server
created: '2026-05-23'
description: Community-maintained, open-source REST and GraphQL API for SpaceX data — launches, rockets, capsules, cores, crew, dragons, payloads, ships, landpads, launchpads, Starlink satellites, the Tesla Roadster ephemeris, company info, and historical events. Operated by the r-spacex community (the same group behind the r/SpaceX subreddit) and licensed Apache 2.0. The canonical hosted base URL is https://api.spacexdata.com and the canonical source repository is https://github.com/r-spacex/SpaceX-API. The API is currently in MAINTENANCE-ONLY MODE as of 2024. New launches and missions are NOT being added to the dataset; the project remains online for historical lookups and as a teaching/sample API. This makes it an excellent fixture for SDK tutorials, MCP server demos, and API design exercises, but it is no longer a live source of upcoming SpaceX flight data. The data is organized as a MongoDB document store with cross-resource UUID references; the /query endpoints expose mongoose-paginate-v2
  with full MongoDB find()/options semantics. Authentication is only required for destructive (create/update/delete) admin routes; all read operations are public. This community project is not affiliated with, endorsed by, or officially connected to Space Exploration Technologies Corp.
examples:
- key_count: 9
  name: Spacex Getcapsule Example
  slug: spacex-getcapsule-example
- key_count: 16
  name: Spacex Getcompany Example
  slug: spacex-getcompany-example
- key_count: 11
  name: Spacex Getcore Example
  slug: spacex-getcore-example
- key_count: 7
  name: Spacex Getcrewmember Example
  slug: spacex-getcrewmember-example
- key_count: 23
  name: Spacex Getdragon Example
  slug: spacex-getdragon-example
- key_count: 6
  name: Spacex Gethistoryevent Example
  slug: spacex-gethistoryevent-example
- key_count: 15
  name: Spacex Getlandpad Example
  slug: spacex-getlandpad-example
- key_count: 27
  name: Spacex Getlatestlaunch Example
  slug: spacex-getlatestlaunch-example
- key_count: 15
  name: Spacex Getlaunchpad Example
  slug: spacex-getlaunchpad-example
- key_count: 27
  name: Spacex Getnextlaunch Example
  slug: spacex-getnextlaunch-example
- key_count: 28
  name: Spacex Getpayload Example
  slug: spacex-getpayload-example
- key_count: 27
  name: Spacex Getroadster Example
  slug: spacex-getroadster-example
- key_count: 22
  name: Spacex Getrocket Example
  slug: spacex-getrocket-example
- key_count: 24
  name: Spacex Getship Example
  slug: spacex-getship-example
- key_count: 8
  name: Spacex Getstarlinksatellite Example
  slug: spacex-getstarlinksatellite-example
graphqls:
- description: Community-maintained GraphQL gateways over the SpaceX REST data, providing typed schema access and nested-field selection across launches, rockets, missions, payloads, ships, and crew. Multiple commun
  name: SpaceX (Community API) GraphQL API
  slug: spacex-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spacex.png
json_schemas:
- name: SpaceX Capsule
  property_count: 10
  slug: spacex-capsule
- name: SpaceX Company
  property_count: 16
  slug: spacex-company
- name: SpaceX Core
  property_count: 11
  slug: spacex-core
- name: SpaceX CrewMember
  property_count: 7
  slug: spacex-crew
- name: SpaceX Dragon
  property_count: 23
  slug: spacex-dragon
- name: SpaceX HistoryEvent
  property_count: 6
  slug: spacex-history
- name: SpaceX Landpad
  property_count: 14
  slug: spacex-landpad
- name: SpaceX Launch
  property_count: 26
  slug: spacex-launch
- name: SpaceX Launchpad
  property_count: 13
  slug: spacex-launchpad
- name: SpaceX Payload
  property_count: 28
  slug: spacex-payload
- name: SpaceX Roadster
  property_count: 27
  slug: spacex-roadster
- name: SpaceX Rocket
  property_count: 22
  slug: spacex-rocket
- name: SpaceX Ship
  property_count: 24
  slug: spacex-ship
- name: SpaceX StarlinkSat
  property_count: 8
  slug: spacex-starlink
json_structures:
- name: Spacex Capsule Structure
  property_count: 10
  slug: spacex-capsule-structure
- name: Spacex Company Structure
  property_count: 16
  slug: spacex-company-structure
- name: Spacex Core Structure
  property_count: 11
  slug: spacex-core-structure
- name: Spacex Crew Structure
  property_count: 7
  slug: spacex-crew-structure
- name: Spacex Dragon Structure
  property_count: 23
  slug: spacex-dragon-structure
- name: Spacex History Structure
  property_count: 6
  slug: spacex-history-structure
- name: Spacex Landpad Structure
  property_count: 14
  slug: spacex-landpad-structure
- name: Spacex Launch Structure
  property_count: 26
  slug: spacex-launch-structure
- name: Spacex Launchpad Structure
  property_count: 13
  slug: spacex-launchpad-structure
- name: Spacex Payload Structure
  property_count: 28
  slug: spacex-payload-structure
- name: Spacex Roadster Structure
  property_count: 27
  slug: spacex-roadster-structure
- name: Spacex Rocket Structure
  property_count: 22
  slug: spacex-rocket-structure
- name: Spacex Ship Structure
  property_count: 24
  slug: spacex-ship-structure
- name: Spacex Starlink Structure
  property_count: 8
  slug: spacex-starlink-structure
jsonld:
- class_count: 0
  name: Spacex Context
  property_count: 14
  slug: spacex-context
layout: provider
modified: '2026-05-29'
name: SpaceX (Community API)
nav: Providers
network: true
overview: 'SpaceX (Community API) publishes 14 APIs on the [APIs.io](https://apis.io/) network, including Capsules API, Company API, Cores API, and 11 more. Tagged areas include Space, Launch, Satellites, Starlink, and Falcon 9.


  The SpaceX (Community API) catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SpaceX (Community API)''s developer surface includes authentication, documentation, getting-started guide, changelog, status page, tooling, and 19 more developer resources.'
plans:
- name: Spacex Plans Pricing
  plan_count: 2
  slug: spacex-plans-pricing
random_paper: 32
rate_limits:
- limit_count: 4
  name: Spacex Rate Limits
  slug: spacex-rate-limits
rules:
- name: SpaceX (Community API) API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: spacex-jsonschema-spectral-rules
- name: SpaceX (Community API) API Rules
  rule_count: 32
  severity_counts:
    error: 10
    hint: 0
    info: 7
    warn: 15
  slug: spacex-rules
score:
  band: developing
  composite: 51.0
  delta: 2.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 71.7
    developer_ergonomics: 30.4
    discoverability: 80.0
    governance: 86.8
    operational_transparency: 52.6
  previous_composite: 48.1
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spacex/refs/heads/main/screenshots/spacex-2026-06-20T194240.png
security:
- kind: authentication
  name: Spacex Authentication
  slug: spacex-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Spacex Domain Security
  slug: spacex-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: spacex
tags:
- Space
- Launch
- Satellites
- Starlink
- Falcon 9
- Falcon Heavy
- Dragon
- Rockets
- Open Source
- Community
- REST
- GraphQL
- Open Data
---
