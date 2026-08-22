---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.7
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tribune Media Agentic Access
  operation_count: 32
  slug: tribune-media-agentic-access
  summary_line: 32 operations
api_count: 10
apis:
- description: The Celebrities API from Tribune Media — 3 operation(s) for celebrities.
  name: Tribune Media Celebrities API
  slug: tribune-media-celebrities-api
- description: The Lineups API from Tribune Media — 4 operation(s) for lineups.
  name: Tribune Media Lineups API
  slug: tribune-media-lineups-api
- description: The Movies API from Tribune Media — 3 operation(s) for movies.
  name: Tribune Media Movies API
  slug: tribune-media-movies-api
- description: The Online Video API from Tribune Media — 3 operation(s) for online video.
  name: Tribune Media Online Video API
  slug: tribune-media-online-video-api
- description: The Programs API from Tribune Media — 5 operation(s) for programs.
  name: Tribune Media Programs API
  slug: tribune-media-programs-api
- description: The Series API from Tribune Media — 3 operation(s) for series.
  name: Tribune Media Series API
  slug: tribune-media-series-api
- description: The Social API from Tribune Media — 1 operation(s) for social.
  name: Tribune Media Social API
  slug: tribune-media-social-api
- description: The Sports API from Tribune Media — 5 operation(s) for sports.
  name: Tribune Media Sports API
  slug: tribune-media-sports-api
- description: The Stations API from Tribune Media — 3 operation(s) for stations.
  name: Tribune Media Stations API
  slug: tribune-media-stations-api
- description: The Theatres API from Tribune Media — 2 operation(s) for theatres.
  name: Tribune Media Theatres API
  slug: tribune-media-theatres-api
artifact_total: 39
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: TMS OnConnect API
  slug: open-tms-onconnect
- collection_type: open
  name: TMS OnConnect Celebrities API
  slug: open-tribune-media-celebrities-api
- collection_type: open
  name: TMS OnConnect Celebrities Lineups API
  slug: open-tribune-media-lineups-api
- collection_type: open
  name: TMS OnConnect Celebrities Movies API
  slug: open-tribune-media-movies-api
- collection_type: open
  name: TMS OnConnect Celebrities Online Video API
  slug: open-tribune-media-online-video-api
- collection_type: open
  name: TMS OnConnect Celebrities Programs API
  slug: open-tribune-media-programs-api
- collection_type: open
  name: TMS OnConnect Celebrities Series API
  slug: open-tribune-media-series-api
- collection_type: open
  name: TMS OnConnect Celebrities Social API
  slug: open-tribune-media-social-api
- collection_type: open
  name: TMS OnConnect Celebrities Sports API
  slug: open-tribune-media-sports-api
- collection_type: open
  name: TMS OnConnect Celebrities Stations API
  slug: open-tribune-media-stations-api
- collection_type: open
  name: TMS OnConnect Celebrities Theatres API
  slug: open-tribune-media-theatres-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tribune-media-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tribune-media-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tribune-media-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tribune-company
- group: company
  title: ''
  type: Website
  url: https://www.tribunemedia.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.tmsapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.tmsapi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.tmsapi.com/Getting_Started
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.tmsapi.com/page/API_Terms_of_Use
- group: start
  title: ''
  type: Signup
  url: https://developer.tmsapi.com/member/register
created: '2026-05-03'
description: Tribune Media was a diversified media and entertainment company with broadcasting, digital, and content businesses. Through Tribune Media Services (TMS), it provided comprehensive entertainment data APIs including TV programming, movie showtimes, celebrity information, and sports data. Tribune Media was acquired by Nexstar Media Group in 2019. The TMS OnConnect APIs are now operated by Gracenote (a Nielsen company), providing metadata for TV shows, movies, celebrities, and televised sports to consumer electronics manufacturers, cable operators, entertainment platforms, and application developers.
examples:
- key_count: 2
  name: Tms Onconnect Get Lineup Grid Example
  slug: tms-onconnect-get-lineup-grid-example
- key_count: 2
  name: Tms Onconnect Get Lineups Example
  slug: tms-onconnect-get-lineups-example
- key_count: 2
  name: Tms Onconnect Get Movie Showings Example
  slug: tms-onconnect-get-movie-showings-example
- key_count: 2
  name: Tms Onconnect Search Programs Example
  slug: tms-onconnect-search-programs-example
finops:
- name: Tribune Media Finops
  service_category: API
  slug: tribune-media-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tribune-media.png
json_schemas:
- name: TMS Airing
  property_count: 7
  slug: tms-airing
- name: TMS Program
  property_count: 15
  slug: tms-program
json_structures:
- name: Tms Airing Structure
  property_count: 0
  slug: tms-airing-structure
- name: Tms Program Structure
  property_count: 0
  slug: tms-program-structure
jsonld:
- class_count: 9
  name: Tribune Media Context
  property_count: 41
  slug: tribune-media-context
layout: provider
modified: '2026-05-19'
name: Tribune Media
nav: Providers
network: true
overview: 'Tribune Media publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Celebrities API, Lineups API, Movies API, and 7 more. Tagged areas include Media, Entertainment, Broadcasting, Television, and Movies.


  The Tribune Media catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tribune Media''s developer surface includes authentication, documentation, getting-started guide, signup flow, and 6 more developer resources.'
plans:
- name: Tribune Media Plans Pricing
  plan_count: 3
  slug: tribune-media-plans-pricing
press:
- date: '2026-05-25'
  title: AN News
  url: https://newspapers.org/an-news/?page_size=20&category_id=902&sub_type=stories%2Cphotos%2Cvideos%2Cspecialsections%2Cprintissues%2Ceeditions%2Cpackages%2Cmagazines%2Cmaps%2Cfeeds%2Cpolls&page=67
- date: '2026-05-25'
  title: 💻 Byron Allen on consolidating media assets and funding ...
  url: https://www.facebook.com/djenvy/posts/-byron-allen-on-consolidating-media-assets-and-funding-aidriven-local-news/1514662133360299/
- date: '2026-05-25'
  title: Daily Tribune's media snowflakery and AI articles
  url: https://www.facebook.com/groups/708242270391120/posts/1450915709457102/
- date: '2026-05-25'
  title: tronc/Tribune
  url: https://www.usnewsdeserts.com/reports/expanding-news-desert/enduring-legacy-new-media-barons/tronc-tribune/
- date: '2026-05-25'
  title: Nexstar Media Group Enters into Definitive Agreement to ...
  url: https://www.nexstar.tv/nexstar_agrees_to_acquire_tribune/
- date: '2019-10-16'
  title: Press Coverage
  url: http://www.tribunemedia.com/press-coverage/
- date: '2019-09-19'
  title: Nexstar Media Group Completes Tribune Media Acquisition Creating the Nation’s Largest Local Television Broadcaster
  url: http://www.tribunemedia.com/nexstar-media-group-completes-tribune-media-acquisition-creating-the-nations-largest-local-television-broadcaster/
- date: '2019-09-19'
  title: About Nexstar
  url: http://nexstar.tv#new_tab
random_paper: 16
rate_limits:
- limit_count: 5
  name: Tribune Media Rate Limits
  slug: tribune-media-rate-limits
rules:
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Tribune Media API Rules
  rule_count: 12
  severity_counts:
    error: 4
    hint: 3
    info: 0
    warn: 5
  slug: tms-onconnect-rules
- effective_rule_count: 5
  extends: []
  name: Tribune Media API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tribune-media-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.0
  delta: 3.2
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 45.5
    contract_quality: 62.1
    developer_ergonomics: 42.9
    discoverability: 64.8
    governance: 45.5
    operational_transparency: 7.9
  previous_composite: 41.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tribune-media/refs/heads/main/screenshots/tribune-media-2026-06-20T195707.png
security:
- kind: authentication
  name: Tribune Media Authentication
  slug: tribune-media-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Tribune Media Domain Security
  slug: tribune-media-domain-security
  summary_line: TLSv1.3 · DMARC
slug: tribune-media
tags:
- Media
- Entertainment
- Broadcasting
- Television
- Movies
- Sports
- Celebrity
- Fortune 1000
website: https://www.tribunemedia.com/
---
