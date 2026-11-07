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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Audioalpha Io Agentic Access
  operation_count: 23
  slug: audioalpha-io-agentic-access
  summary_line: 23 operations
api_count: 1
apis:
- baseURL: https://www.audioalpha.io/api/v1
  baseurl_source: declared
  description: Individual episode data
  name: AudioAlpha Episode API
  slug: audioalpha-io-episode-api
- baseURL: https://www.audioalpha.io/api/v1
  baseurl_source: declared
  description: Market-wide sentiment and narrative data
  name: AudioAlpha Market API
  slug: audioalpha-io-market-api
- baseURL: https://www.audioalpha.io/api/v1
  baseurl_source: declared
  description: Personalised feed based on favorites
  name: AudioAlpha Personal API
  slug: audioalpha-io-personal-api
- baseURL: https://www.audioalpha.io/api/v1
  baseurl_source: declared
  description: Podcast discovery and episode listing
  name: AudioAlpha Podcast API
  slug: audioalpha-io-podcast-api
- baseURL: https://www.audioalpha.io/api/v1
  baseurl_source: declared
  description: Asset-level sentiment and signals
  name: AudioAlpha Ticker API
  slug: audioalpha-io-ticker-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/audioalpha-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/audioalpha-io/agentic-access/audioalpha-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/audioalpha-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/audioalpha-io/rules/audioalpha-io-rules.yml
  title: ''
  type: Spectral
  url: rules/audioalpha-io-rules.yml
- group: design
  href: https://artifacts.apis.io/audioalpha-io/json-ld/audioalpha-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/audioalpha-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/audioalpha-io/vocabulary/audioalpha-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/audioalpha-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/audioalpha-io/data-model/audioalpha-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/audioalpha-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/audioalpha-io/errors/audioalpha-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/audioalpha-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/audioalpha-io/conformance/audioalpha-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/audioalpha-io-conformance.yml
- group: build
  href: https://artifacts.apis.io/audioalpha-io/mcp/audioalpha-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/audioalpha-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/audioalpha-io/mcp/audioalpha-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/audioalpha-io-mcp.yml
- group: agent
  href: https://artifacts.apis.io/audioalpha-io/well-known/audioalpha-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/audioalpha-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/audioalpha-io/hosts/audioalpha-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/audioalpha-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/audioalpha-io/vendors/audioalpha-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/audioalpha-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/audioalpha-io/authentication/audioalpha-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/audioalpha-io-authentication.yml
- group: auth
  href: https://artifacts.apis.io/audioalpha-io/security/audioalpha-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/audioalpha-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://audioalpha.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.audioalpha.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.audioalpha.io/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.audioalpha.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.audioalpha.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.audioalpha.io/auth/login
- group: operate
  title: ''
  type: Support
  url: https://www.audioalpha.io/faq
- group: company
  title: ''
  type: Blog
  url: https://www.audioalpha.io/insights
created: '2026-11-02'
description: AudioAlpha provides a platform that transcribes over 150 finance and cryptocurrency podcasts, extracting more than 85,000 episodes into proprietary narrative metrics, daily market summaries, scenario signals, and offers an API/MCP for developers to integrate measurable market insights into their applications.
image: https://www.audioalpha.io/favicon.ico
json_schemas:
- name: AssetSnapshot
  property_count: 29
  slug: audioalpha-io-asset-snapshot
- name: EpisodeFull
  property_count: 13
  slug: audioalpha-io-episode-full
- name: LeaderboardHighlights
  property_count: 6
  slug: audioalpha-io-leaderboard-highlights
- name: MarketSnapshot
  property_count: 26
  slug: audioalpha-io-market-snapshot
- name: PersonalizedFeed
  property_count: 4
  slug: audioalpha-io-personalized-feed
- name: Signal
  property_count: 11
  slug: audioalpha-io-signal
jsonld:
- class_count: 18
  name: Audioalpha Io Context
  property_count: 99
  slug: audioalpha-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at audioalpha.io.
  name: AudioAlpha MCP Server
  slug: audioalpha-io-mcp-yml
modified: '2026-11-02'
name: AudioAlpha
nav: Providers
network: true
overview: 'AudioAlpha publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Episode API, Market API, Personal API, and 2 more. Tagged areas include Finance, Podcasts, Transcription, Market Data, and Company.


  The AudioAlpha catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AudioAlpha''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 16 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: AudioAlpha API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 2
  slug: audioalpha-io-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 63.2
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 39.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Audioalpha Io Authentication
  slug: audioalpha-io-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Audioalpha Io Domain Security
  slug: audioalpha-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: audioalpha-io
tags:
- Finance
- Podcasts
- Transcription
- Market Data
- Company
website: https://audioalpha.io/
---
