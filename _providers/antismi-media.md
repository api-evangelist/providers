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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Antismi Media Agentic Access
  operation_count: 22
  slug: antismi-media-agentic-access
  summary_line: 22 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The authentication API from AntiSMI — 2 operation(s) for authentication.
  name: AntiSMI Authentication API
  slug: antismi-media-authentication-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The digest API from AntiSMI — 8 operation(s) for digest.
  name: AntiSMI Digest API
  slug: antismi-media-digest-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The Favicon.ico API from AntiSMI — 1 operation(s) for favicon.ico.
  name: AntiSMI Favicon.ico API
  slug: antismi-media-favicon-ico-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The Health API from AntiSMI — 1 operation(s) for health.
  name: AntiSMI Health API
  slug: antismi-media-health-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The Icon.png API from AntiSMI — 1 operation(s) for icon.png.
  name: AntiSMI Icon.png API
  slug: antismi-media-icon-png-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The Metrics API from AntiSMI — 1 operation(s) for metrics.
  name: AntiSMI Metrics API
  slug: antismi-media-metrics-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The news API from AntiSMI — 5 operation(s) for news.
  name: AntiSMI News API
  slug: antismi-media-news-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The reference API from AntiSMI — 2 operation(s) for reference.
  name: AntiSMI Reference API
  slug: antismi-media-reference-api
- baseURL: https://api.antismi.media
  baseurl_source: declared
  description: The Russian News Archive API API from AntiSMI — 1 operation(s) for russian news archive api.
  name: AntiSMI Russian News Archive API
  slug: antismi-media-russian-news-archive-api-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/antismi-media/agentic-access/antismi-media-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/antismi-media-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/antismi-media/rules/antismi-media-rules.yml
  title: ''
  type: Spectral
  url: rules/antismi-media-rules.yml
- group: design
  href: https://artifacts.apis.io/antismi-media/json-ld/antismi-media-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/antismi-media-context.jsonld
- group: design
  href: https://artifacts.apis.io/antismi-media/vocabulary/antismi-media-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/antismi-media-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/antismi-media/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/antismi-media/data-model/antismi-media-data-model.yml
  title: ''
  type: DataModel
  url: data-model/antismi-media-data-model.yml
- group: auth
  href: https://artifacts.apis.io/antismi-media/authentication/antismi-media-authentication.yml
  title: ''
  type: Authentication
  url: authentication/antismi-media-authentication.yml
- group: design
  href: https://artifacts.apis.io/antismi-media/errors/antismi-media-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/antismi-media-problem-types.yml
- group: design
  href: https://artifacts.apis.io/antismi-media/conformance/antismi-media-conformance.yml
  title: ''
  type: Conformance
  url: conformance/antismi-media-conformance.yml
- group: agent
  href: https://artifacts.apis.io/antismi-media/mcp/antismi-media-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/antismi-media-mcp.yml
- group: other
  href: https://artifacts.apis.io/antismi-media/hosts/antismi-media-hosts.yml
  title: ''
  type: Hosts
  url: hosts/antismi-media-hosts.yml
- group: other
  href: https://artifacts.apis.io/antismi-media/vendors/antismi-media-vendors.yml
  title: ''
  type: Vendors
  url: vendors/antismi-media-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://dashboard.antismi.media/login/?next=%2Fsuperset%2Fwelcome%2F
- group: auth
  href: https://artifacts.apis.io/antismi-media/security/antismi-media-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/antismi-media-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://antismi.media/
- group: docs
  title: ''
  type: Documentation
  url: https://api.antismi.media/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.antismi.media/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://news.antismi.media
- group: start
  title: ''
  type: GettingStarted
  url: https://news.antismi.media/en
- group: operate
  title: ''
  type: Support
  url: https://news.antismi.media/chat
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.antismi.media/openapi.json
  - status: 401
    url: https://mcp.antismi.media/mcp
  - status: 401
    url: https://api.antismi.media/mcp
  - status: 200
    url: https://antismi.media/
  reason: partner-login
  state: gated
created: '2026-11-01'
description: AntiSMI provides an AI‑powered news intelligence platform that archives Russian‑language news since 1999, offering over 3.7 million items. The service tags content in Russian and English, enabling semantic search, daily digests, trend analysis, and topic timelines. Developers can access a REST API for vector search, digests, and trends via API keys, with a free trial tier. The platform also includes an AI chat and MCP for developers.
image: https://antismi.media/og-image.png
json_schemas:
- name: AgencyDB
  property_count: 38
  slug: antismi-media-agency-db
- name: DigestRequest
  property_count: 17
  slug: antismi-media-digest-request
- name: HistoricalDigestRequest
  property_count: 10
  slug: antismi-media-historical-digest-request
- name: TopicTimelineRequest
  property_count: 9
  slug: antismi-media-topic-timeline-request
- name: TrendsRequest
  property_count: 9
  slug: antismi-media-trends-request
- name: WordCloudRequest
  property_count: 12
  slug: antismi-media-word-cloud-request
jsonld:
- class_count: 37
  name: Antismi Media Context
  property_count: 151
  slug: antismi-media-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.antismi.media.
  name: AntiSMI MCP Server
  slug: antismi-media-mcp-yml
modified: '2026-11-01'
name: AntiSMI
nav: Providers
network: true
overview: 'AntiSMI publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Digest API, Favicon.ico API, and 6 more. Tagged areas include News, Artificial Intelligence, Search, Media, and Russian.


  The AntiSMI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AntiSMI''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AntiSMI API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: antismi-media-rules
scopes:
- name: Antismi Media Scopes
  scope_count: 0
  slug: antismi-media-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.7
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 6.6
    contract_governance: 22.0
    contract_quality: 55.5
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 39.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Antismi Media Authentication
  slug: antismi-media-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Antismi Media Domain Security
  slug: antismi-media-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 3
skills:
- name: search
  slug: antismi-media-search
- name: topic-timeline
  slug: antismi-media-topic-timeline
- name: vector-search
  slug: antismi-media-vector-search
slug: antismi-media
tags:
- News
- Artificial Intelligence
- Search
- Media
- Russian
website: https://antismi.media/
---
