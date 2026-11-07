---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Machine-readable contract exposing DataSocial's table and SQL query tools via MCP JSON-RPC.
  name: DataSocial MCP
  slug: datasocial-mcp
- baseURL: https://api.datasocial.ai
  baseurl_source: declared
  description: 'DataSocial API as documented publicly: 15 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DataSocial API
  slug: datasocial-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/datasocial-ai/rules/datasocial-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/datasocial-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/datasocial-ai/json-ld/datasocial-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/datasocial-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/datasocial-ai/vocabulary/datasocial-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/datasocial-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/datasocial-ai/data-model/datasocial-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/datasocial-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/datasocial-ai/conformance/datasocial-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/datasocial-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/datasocial-ai/mcp/datasocial-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/datasocial-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/datasocial-ai/hosts/datasocial-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datasocial-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/datasocial-ai/vendors/datasocial-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datasocial-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datasocial.ai/terms
- group: start
  title: ''
  type: Sandbox
  url: https://datasocial.ai/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datasocial.ai/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://datasocial.ai/docs
- group: auth
  href: https://artifacts.apis.io/datasocial-ai/security/datasocial-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datasocial-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datasocial.ai/
created: '2026-11-05'
description: DataSocial provides a data platform offering answers about billions of TikTok creators, videos, sounds, and related metrics. The service aggregates daily historical data, enabling users to query tables and charts about creator counts, video volumes, sound usage, and follower statistics across the TikTok ecosystem. It serves analytics, research, and business intelligence use cases with a public API.
image: https://datasocial.ai/og/home-v2.png
json_schemas:
- name: GetV1UserFollowersResponse
  property_count: 12
  slug: datasocial-ai-get-v1-user-followers-response
- name: GetV1UserFollowingResponse
  property_count: 13
  slug: datasocial-ai-get-v1-user-following-response
- name: GetV1UserPostsResponse
  property_count: 10
  slug: datasocial-ai-get-v1-user-posts-response
- name: GetV1VideoCommentsRepliesResponse
  property_count: 8
  slug: datasocial-ai-get-v1-video-comments-replies-response
- name: GetV1VideoCommentsResponse
  property_count: 14
  slug: datasocial-ai-get-v1-video-comments-response
- name: GetV1VideoInfoResponse
  property_count: 5
  slug: datasocial-ai-get-v1-video-info-response
jsonld:
- class_count: 13
  name: Datasocial Ai Context
  property_count: 45
  slug: datasocial-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.datasocial.ai.
  name: DataSocial MCP Server
  slug: datasocial-ai-mcp-yml
modified: '2026-11-05'
name: DataSocial
nav: Providers
network: true
overview: 'DataSocial is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data, Analytics, TikTok, and Platform.


  The DataSocial catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  DataSocial''s developer surface includes sandbox, documentation, and 12 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: DataSocial API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: datasocial-ai-rules
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 16.7
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datasocial Ai Domain Security
  slug: datasocial-ai-domain-security
  summary_line: TLSv1.3
slug: datasocial-ai
tags:
- Data
- Analytics
- TikTok
- Platform
website: https://datasocial.ai/
---
