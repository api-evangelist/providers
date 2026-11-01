---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Hooklayer MCP provides 14 AI tools via a Model Context Protocol server.
  name: Hooklayer MCP API
  slug: hooklayer-mcp-api
- description: 'hooklayer-dev API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: hooklayer-dev API
  slug: hooklayer-dev-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/hooklayer-dev/rules/hooklayer-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/hooklayer-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/hooklayer-dev/json-ld/hooklayer-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hooklayer-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/hooklayer-dev/vocabulary/hooklayer-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hooklayer-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/hooklayer-dev/data-model/hooklayer-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hooklayer-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/hooklayer-dev/conformance/hooklayer-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hooklayer-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hooklayer-dev/llms/hooklayer-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hooklayer-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/hooklayer-dev/mcp/hooklayer-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hooklayer-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hooklayer-dev/well-known/hooklayer-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hooklayer-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/hooklayer-dev/hosts/hooklayer-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hooklayer-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/hooklayer-dev/vendors/hooklayer-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hooklayer-dev-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://hooklayer.dev/auth/signup
- group: start
  title: ''
  type: Sandbox
  url: https://hooklayer.dev/hooklayer/playground
- group: operate
  title: ''
  type: ChangeLog
  url: https://hooklayer.dev/hooklayer/whats-new
- group: auth
  href: https://artifacts.apis.io/hooklayer-dev/security/hooklayer-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hooklayer-dev-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/hooklayer-dev/security/hooklayer-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hooklayer-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hooklayer.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://hooklayer.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://hooklayer.dev/api/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://hooklayer.dev/pricing
- group: company
  title: ''
  type: Blog
  url: https://hooklayer.dev/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hooklayer.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hooklayer.dev/privacy
- group: operate
  title: ''
  type: Support
  url: https://hooklayer.dev/support
created: '2026-10-30'
description: Hooklayer provides a Model Context Protocol (MCP) server that offers AI‑driven viral content intelligence for TikTok, Instagram Reels, and YouTube Shorts. It exposes 14 tools across scoring, research, analysis, shopping, generation, and monitoring, enabling creators, marketers, and agencies to test hooks, predict virality, and automate content workflows directly within Claude and ChatGPT. The platform offers a free tier with no credit‑card required and integrates with popular AI assistants and automation tools.
examples:
- key_count: 9
  name: Hooklayer Dev Mcp
  slug: hooklayer-dev-mcp
image: https://hooklayer.dev/hooklayer-banner.png
json_schemas:
- name: PostApiV1HookScoreRequest
  property_count: 1
  slug: hooklayer-dev-post-api-v1-hook-score-request
jsonld:
- class_count: 1
  name: Hooklayer Dev Context
  property_count: 1
  slug: hooklayer-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at hooklayer.dev; 18 tools listed.
  name: hooklayer-dev MCP Server
  slug: hooklayer-dev-mcp-yml
modified: '2026-10-30'
name: hooklayer-dev
nav: Providers
network: true
overview: 'hooklayer-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include MCP, AI, Video, Marketing, and Analytics.


  The hooklayer-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  hooklayer-dev''s developer surface includes signup flow, sandbox, changelog, documentation, API reference, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Hooklayer Dev Plans Pricing
  plan_count: 0
  slug: hooklayer-dev-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Hooklayer Dev Rate Limits
  slug: hooklayer-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: hooklayer-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: hooklayer-dev-rules
scopes:
- name: Hooklayer Dev Scopes
  scope_count: 0
  slug: hooklayer-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.1
  coverage:
    artifact_dirs: 27
    catalog_earned: 63.1
    catalog_earned_first_party: 0.0
    catalog_gap: 51.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 45.0
    developer_ergonomics: 31.0
    discoverability: 56.7
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Hooklayer Dev Authentication
  slug: hooklayer-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Hooklayer Dev Domain Security
  slug: hooklayer-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hooklayer-dev
tags:
- MCP
- AI
- Video
- Marketing
- Analytics
- Content
website: https://hooklayer.dev/
---
