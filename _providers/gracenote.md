---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-09-14'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Gracenote Agentic Access
  operation_count: 17
  slug: gracenote-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- description: The Gracenote OnConnect API delivers TV and video data including schedules, programs, celebrities, sports, images, and station lineups. Designed for mobile apps, connected TVs, EPGs, and streaming exp
  name: Gracenote OnConnect API
  slug: onconnect-api
- description: The Gracenote OnConnect Data API provides extended metadata for TV, movies, celebrities, and sports. It is designed for connected experiences and mobile applications that need rich entertainment data,
  name: Gracenote OnConnect Data API
  slug: onconnect-data-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Celebrities API from Gracenote — 2 operation(s) for celebrities.
  name: Gracenote Celebrities API
  slug: gracenote-celebrities-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Lineups API from Gracenote — 4 operation(s) for lineups.
  name: Gracenote Lineups API
  slug: gracenote-lineups-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Movies API from Gracenote — 2 operation(s) for movies.
  name: Gracenote Movies API
  slug: gracenote-movies-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Programs API from Gracenote — 2 operation(s) for programs.
  name: Gracenote Programs API
  slug: gracenote-programs-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Series API from Gracenote — 2 operation(s) for series.
  name: Gracenote Series API
  slug: gracenote-series-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Sports API from Gracenote — 2 operation(s) for sports.
  name: Gracenote Sports API
  slug: gracenote-sports-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The Stations API from Gracenote — 3 operation(s) for stations.
  name: Gracenote Stations API
  slug: gracenote-stations-api
- baseURL: https://on-api.gracenote.com
  baseurl_source: declared
  description: The On API is Gracenote's database-ingestion surface for television schedule data and related information — programs, schedules, celebrities, lineups, sources, sports events, teams, venues, video popu
  name: Gracenote On API
  slug: on-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: The current published definition of the OnConnect lookup family — 40 operations across programs, series, movies on TV and in theatres, celebrities, sports, stations and lineups. This is the request-re
  name: Gracenote OnConnect Lookup APIs
  slug: onconnect-lookup-apis
- baseURL: https://gvd-api.gracenote.com
  baseurl_source: declared
  description: The Global Video Data API is Gracenote's worldwide video metadata feed — schedules, VOD catalogs, availability days, lineups, media, contributors, controlled vocabulary and video popularity across 90+
  name: Gracenote GVD API
  slug: gvd-api
- baseURL: https://gnids.gracenote.com/api/v1
  baseurl_source: declared
  description: The GN IDS API is the only write surface Gracenote publishes. It lets content providers create, retrieve, update, delete and publish programs into Gracenote-licensed datasets across 85+ countries usin
  name: Gracenote GN IDS API
  slug: gn-ids-api
- baseURL: https://api.gmd.music.gracenote.com/v2
  baseurl_source: declared
  description: The Global Music Data API v2 provides artist, recording, album-edition, track and descriptor lookups and text search, with artist images, cover art, popularity scores, partner and industry IDs sold as
  name: Gracenote GMD API v2
  slug: gmd-api-v2
- baseURL: https://api.gmd.music.gracenote.com/v3
  baseurl_source: declared
  description: The beta third generation of the Global Music Data API, adding album masters, descriptor correlations, descriptor hierarchies and an entitlements lookup that lets a key ask what it is licensed for. Gr
  name: Gracenote GMD API v3 (Beta)
  slug: gmd-api-v3
- baseURL: https://api.nexus.gracenote.com/v1
  baseurl_source: declared
  description: Nexus is Gracenote's automotive entertainment platform API — music, podcasts, radio stations, sports, video, search, collections and per-user settings shaped for in-car infotainment. Keys are entitled
  name: Gracenote Nexus API
  slug: nexus-api
- baseURL: https://api.sports.gracenote.com/gns-api
  baseurl_source: declared
  description: Seventy-three read operations over Gracenote's sports data covering 4,000+ competitions — sports, series, leagues, league seasons, matches, teams, persons, venues, standings, brackets, classifications
  name: Gracenote Global Sports Data Lookup API
  slug: global-sports-data-lookup-api
- baseURL: https://api.sports.gracenote.com/gns-api
  baseurl_source: declared
  description: The update and ingestion counterpart to the Global Sports Data Lookup API — thirteen endpoints that deliver changed sports records so a consumer can keep a local store in sync rather than re-polling t
  name: Gracenote Global Sports Data Update API
  slug: global-sports-data-update-api
- baseURL: https://data.tmsapi.com/v1.1
  baseurl_source: declared
  description: Curated links to online and over-the-top video content, indexed and synced to Gracenote TMS IDs, alongside online social signals — for adding OTT availability and social context to a video product. Co
  name: Gracenote Online Video and Social APIs
  slug: online-video-social-apis
- description: A production remote Model Context Protocol server that grounds LLM responses in Gracenote's verified video metadata — more than 55 million titles plus continually updated viewing availability. Nine to
  name: Gracenote Video MCP Server
  slug: video-mcp-server
- description: A production remote Model Context Protocol server for live, upcoming and recent sports — eleven tools covering entity resolution, event discovery, match info, recaps, lineups, where-to-watch, team and
  name: Gracenote Sports MCP Server
  slug: sports-mcp-server
artifact_total: 38
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities API
  slug: open-gracenote-celebrities-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Lineups API
  slug: open-gracenote-lineups-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Movies API
  slug: open-gracenote-movies-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Programs API
  slug: open-gracenote-programs-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Series API
  slug: open-gracenote-series-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Sports API
  slug: open-gracenote-sports-api
- collection_type: open
  name: Gracenote OnConnect TMS Celebrities Stations API
  slug: open-gracenote-stations-api
- collection_type: open
  name: Gracenote OnConnect TMS API
  slug: open-gracenote
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/capabilities/gracenote-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/gracenote-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/agentic-access/gracenote-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gracenote-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/security/gracenote-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gracenote-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/authentication/gracenote-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gracenote-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gracenote
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gracenote
- group: company
  title: ''
  type: Website
  url: https://www.gracenote.com/
- group: other
  title: ''
  type: Developer
  url: https://developer.tmsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://devportal.gracenote.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tmsapi.com/Getting_Started
- group: operate
  title: ''
  type: Support
  url: https://www.gracenote.com/support/
- group: other
  title: ''
  type: Products
  url: https://www.gracenote.com/products/
- group: other
  title: ''
  type: Parent
  url: https://www.nielsen.com/
- group: company
  title: ''
  type: Blog
  url: https://gracenote.com/insights/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/mcp/gracenote-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gracenote-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/mcp/gracenote-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/gracenote-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/well-known/gracenote-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gracenote-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/llms/gracenote-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gracenote-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/conventions/gracenote-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gracenote-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/errors/gracenote-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gracenote-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/lifecycle/gracenote-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/gracenote-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/lifecycle/gracenote-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/gracenote-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/changelog/gracenote-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/gracenote-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/conformance/gracenote-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gracenote-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/data-model/gracenote-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gracenote-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/packages/gracenote-packages.yml
  title: ''
  type: Packages
  url: packages/gracenote-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/packages/gracenote-packages.yml
  title: ''
  type: SDKs
  url: packages/gracenote-packages.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/sandbox/gracenote-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/gracenote-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/plans/gracenote-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gracenote-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/rate-limits/gracenote-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gracenote-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/finops/gracenote-finops.yml
  title: ''
  type: FinOps
  url: finops/gracenote-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/security/gracenote-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/gracenote-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.gracenote.com/
- group: docs
  title: ''
  type: APIReference
  url: https://devportal.gracenote.com/catalog
- group: start
  title: ''
  type: SignUp
  url: https://devportal.gracenote.com/register
- group: start
  title: ''
  type: Login
  url: https://devportal.gracenote.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gracenote.com/gracenote-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gracenote.com/gracenote-website-privacy-notice/
created: '2026-03-16'
description: Gracenote, a Nielsen company, provides entertainment metadata, content recognition technology, and developer APIs for the TV, video, music, sports and automotive industries, powering content discovery, search and personalization across linear and streaming services worldwide. It publishes ten first-party OpenAPI 3.1.1 definitions covering 298 operations — TV schedules and program data (On API, OnConnect, GVD), the GN IDS content-submission API, global music data (GMD v2 and v3 Beta), automotive in-car entertainment (Nexus) and global sports data — plus two production Model Context Protocol servers for video and sports that ground LLM answers in Gracenote's verified metadata. Access is licensed through sales rather than self-serve.
finops:
- name: Gracenote Finops
  service_category: API
  slug: gracenote-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gracenote.png
layout: provider
mcp_servers:
- description: Gracenote publishes two production, hosted Model Context Protocol servers — a Video MCP Server and a Sports MCP Server — that ground LLM responses in Gracenote's verified entertainment and sports meta
  name: Gracenote MCP Servers
  slug: gracenote-mcp-servers
modified: '2026-09-12'
name: Gracenote
nav: Providers
network: true
overview: 'Gracenote publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Celebrities API, Lineups API, Movies API, and 14 more. Tagged areas include Artificial Intelligence, Automotive, Content Metadata, Entertainment, and MCP.


  Gracenote''s developer surface includes authentication, documentation, getting-started guide, support, engineering blog, changelog, sandbox, and 32 more developer resources.'
plans:
- name: Gracenote Plans Pricing
  plan_count: 0
  slug: gracenote-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Gracenote Rate Limits
  slug: gracenote-rate-limits
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 24
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 48.0
    developer_ergonomics: 66.1
    discoverability: 68.5
    operational_transparency: 10.5
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 47.1
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-14'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/gracenote/refs/heads/main/screenshots/gracenote-2026-06-20T182312.png
security:
- kind: authentication
  name: Gracenote Authentication
  slug: gracenote-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Gracenote Domain Security
  slug: gracenote-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gracenote Vulnerability Disclosure
  slug: gracenote-vulnerability-disclosure
  summary_line: Hackerone
slug: gracenote
tags:
- Artificial Intelligence
- Automotive
- Content Metadata
- Entertainment
- MCP
- Music
- Nielsen
- Sports
- Sports Data
- Streaming
- Television
- Video
- Video Metadata
website: https://www.gracenote.com/
---
