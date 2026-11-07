---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Creatordb App Agentic Access
  operation_count: 42
  slug: creatordb-app-agentic-access
  summary_line: 42 operations · 4 acting
api_count: 1
apis:
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: The AI Search API from creatordb-app — 1 operation(s) for ai search.
  name: creatordb-app AI Search API
  slug: creatordb-app-ai-search-api
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: The General Operations API from creatordb-app — 1 operation(s) for general operations.
  name: creatordb-app General Operations API
  slug: creatordb-app-general-operations-api
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: Instagram creator data endpoints with metrics and advanced search capabilities.
  name: creatordb-app Instagram API
  slug: creatordb-app-instagram-api
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: Sponsor analysis endpoints including sponsor search and sponsor reports.
  name: creatordb-app Sponsor API
  slug: creatordb-app-sponsor-api
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: TikTok creator data endpoints with metrics and advanced search functionality.
  name: creatordb-app Tik Tok API
  slug: creatordb-app-tiktok-api
- baseURL: https://apiv3.creatordb.app
  baseurl_source: declared
  description: YouTube creator data endpoints including basic metrics, historical data, and detailed analytics.
  name: creatordb-app YouTube API
  slug: creatordb-app-youtube-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/creatordb-app/agentic-access/creatordb-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/creatordb-app-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/creatordb-app/rate-limits/creatordb-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/creatordb-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/creatordb-app/plans/creatordb-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/creatordb-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/rules/creatordb-app-rules.yml
  title: ''
  type: Spectral
  url: rules/creatordb-app-rules.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/json-ld/creatordb-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/creatordb-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/creatordb-app/vocabulary/creatordb-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/creatordb-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/creatordb-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/data-model/creatordb-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/creatordb-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/creatordb-app/changelog/creatordb-app-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/creatordb-app-changelog.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/conventions/creatordb-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/creatordb-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/creatordb-app/authentication/creatordb-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/creatordb-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/errors/creatordb-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/creatordb-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/creatordb-app/conformance/creatordb-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/creatordb-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/creatordb-app/llms/creatordb-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/creatordb-app-llms.txt
- group: other
  href: https://artifacts.apis.io/creatordb-app/a2a/creatordb-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/creatordb-app-a2a.yml
- group: build
  href: https://artifacts.apis.io/creatordb-app/mcp/creatordb-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/creatordb-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/creatordb-app/mcp/creatordb-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/creatordb-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/creatordb-app/well-known/creatordb-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/creatordb-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/creatordb-app/hosts/creatordb-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/creatordb-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/creatordb-app/vendors/creatordb-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/creatordb-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/creatordb-app/packages/creatordb-app-packages.yml
  title: ''
  type: SDKs
  url: packages/creatordb-app-packages.yml
- group: build
  href: https://artifacts.apis.io/creatordb-app/packages/creatordb-app-packages.yml
  title: ''
  type: Packages
  url: packages/creatordb-app-packages.yml
- group: company
  title: ''
  type: Newsroom
  url: https://creatordb.app/free-tools/whats-trending-on-youtube/news/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.creatordb.app/api-v3/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CreatorDB
- group: auth
  href: https://artifacts.apis.io/creatordb-app/security/creatordb-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/creatordb-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://creatordb.app/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.creatordb.app/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.creatordb.app/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.creatordb.app/api-v3/introduction
- group: operate
  title: ''
  type: Support
  url: mailto:product@creatordb.app
- group: company
  title: ''
  type: Blog
  url: https://creatordb.app/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://creatordb.app/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://creatordb.app/privacy-policy/
created: '2026-10-30'
description: CreatorDB provides a global creator data API and influencer marketing platform, offering real-time analytics on over 30 million YouTube, Instagram, and TikTok profiles. Founded in 2021, the service focuses on Asian markets with deep coverage, delivering proprietary engagement metrics, audience demographics, fake-follower detection, sponsorship history, and time-series data to brands and agencies worldwide.
image: https://creatordb.app/logo.png
json_schemas:
- name: InstagramPerformanceData
  property_count: 6
  slug: creatordb-app-instagram-performance-data
- name: InstagramPerformanceHistoryData
  property_count: 1
  slug: creatordb-app-instagram-performance-history-data
- name: InstagramSponsorshipData
  property_count: 1
  slug: creatordb-app-instagram-sponsorship-data
- name: YoutubePerformanceData
  property_count: 10
  slug: creatordb-app-youtube-performance-data
- name: YoutubePerformanceHistoryData
  property_count: 1
  slug: creatordb-app-youtube-performance-history-data
- name: YoutubeSponsorshipData
  property_count: 1
  slug: creatordb-app-youtube-sponsorship-data
jsonld:
- class_count: 21
  name: Creatordb App Context
  property_count: 57
  slug: creatordb-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.creatordb.app.
  name: creatordb-app MCP Server
  slug: creatordb-app-mcp-yml
modified: '2026-10-30'
name: creatordb-app
nav: Providers
network: true
overview: 'creatordb-app publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Search API, General Operations API, Instagram API, and 3 more. Tagged areas include Company, Creator Data, Influencer Marketing, Analytics, and Asia.


  The creatordb-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  creatordb-app''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 27 more developer resources.'
plans:
- name: Creatordb App Plans Pricing
  plan_count: 4
  slug: creatordb-app-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 1
  name: Creatordb App Rate Limits
  slug: creatordb-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 58
  extends:
  - spectral:oas
  name: creatordb-app API Rules
  rule_count: 17
  severity_counts:
    error: 15
    hint: 0
    info: 1
    warn: 1
  slug: creatordb-app-rules
scopes:
- name: Creatordb App Scopes
  scope_count: 0
  slug: creatordb-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.3
  coverage:
    artifact_dirs: 34
    catalog_earned: 82.8
    catalog_earned_first_party: 20.0
    catalog_gap: 32.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.9
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 65.5
    developer_ergonomics: 45.7
    discoverability: 65.8
    operational_transparency: 31.6
  previous_composite: 56.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/creatordb-app/creatordb-app-2026-11-03T125541.png
security:
- kind: authentication
  name: Creatordb App Authentication
  slug: creatordb-app-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Creatordb App Domain Security
  slug: creatordb-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 6
skills:
- name: account
  slug: creatordb-app-account
- name: brand-sponsorship
  slug: creatordb-app-brand-sponsorship
- name: content-analysis
  slug: creatordb-app-content-analysis
- name: creator-csv-workflow
  slug: creatordb-app-creator-csv-workflow
- name: creator-enrichment
  slug: creatordb-app-creator-enrichment
- name: creator-search
  slug: creatordb-app-creator-search
slug: creatordb-app
tags:
- Company
- Creator Data
- Influencer Marketing
- Analytics
- Asia
website: https://creatordb.app/
---
