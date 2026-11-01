---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.1
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API for AI agents to create and manage LNX profiles.
  name: LNX AI Agent API
  slug: lnx-ai-agent-api
- description: 'lnx-net API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: lnx-net API
  slug: lnx-net-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/lnx-net/rules/lnx-net-rules.yml
  title: ''
  type: Spectral
  url: rules/lnx-net-rules.yml
- group: design
  href: https://artifacts.apis.io/lnx-net/json-ld/lnx-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/lnx-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/lnx-net/vocabulary/lnx-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/lnx-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/lnx-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/lnx-net/data-model/lnx-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/lnx-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/lnx-net/conformance/lnx-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/lnx-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/lnx-net/llms/lnx-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lnx-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/lnx-net/mcp/lnx-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/lnx-net-mcp.yml
- group: agent
  href: https://artifacts.apis.io/lnx-net/well-known/lnx-net-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/lnx-net-well-known.yml
- group: other
  href: https://artifacts.apis.io/lnx-net/hosts/lnx-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lnx-net-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://lnx.net/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://lnx.net/docs/mcp
- group: auth
  href: https://artifacts.apis.io/lnx-net/security/lnx-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lnx-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lnx.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://lnx.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lnx.net/privacy
coverage:
  checked: '2026-10-30'
  detail: MCP tools/list endpoint requires a valid session ID, preventing unauthenticated access to the contract.
  evidence:
  - status: 400
    url: https://lnx.net/mcp
  reason: partner-login
  state: gated
created: '2026-10-30'
description: LNX provides a free link‑in‑bio tool that lets creators build a customizable landing page with multiple links, QR code generation, analytics, and themes. The service supports Instagram, TikTok, and other social platforms, offering a simple interface for creators to consolidate their online presence. LNX is a SaaS product focused on creators, offering free and premium features, and operates under the domain lnx.net.
image: https://lnx.net/assets/images/social/lnx-og-card(5).png?v=20260616
json_schemas:
- name: GetXUsernameWellKnownAgentJsonResponse
  property_count: 8
  slug: lnx-net-get-xusername-well-known-agent-json-response
- name: PostApiAgentToolsRequest
  property_count: 8
  slug: lnx-net-post-api-agent-tools-request
- name: PostApiAgentUploadRequest
  property_count: 2
  slug: lnx-net-post-api-agent-upload-request
- name: PostApiAgentsRegisterRequest
  property_count: 6
  slug: lnx-net-post-api-agents-register-request
- name: PostApiAgentsRegisterResponse
  property_count: 6
  slug: lnx-net-post-api-agents-register-response
- name: PutApiAgentProfileRequest
  property_count: 9
  slug: lnx-net-put-api-agent-profile-request
jsonld:
- class_count: 15
  name: Lnx Net Context
  property_count: 37
  slug: lnx-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at lnx.net requiring OAuth.
  name: lnx-net MCP Server
  slug: lnx-net-mcp-yml
modified: '2026-10-30'
name: lnx-net
nav: Providers
network: true
overview: 'lnx-net is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Link-in-bio, Creator Tools, SaaS, and Social Media.


  The lnx-net catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  lnx-net''s developer surface includes documentation and 15 more developer resources.'
plans:
- name: Lnx Net Plans Pricing
  plan_count: 0
  slug: lnx-net-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Lnx Net Rate Limits
  slug: lnx-net-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: lnx-net API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: lnx-net-rules
scopes:
- name: Lnx Net Scopes
  scope_count: 0
  slug: lnx-net-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.0
    catalog_earned_first_party: 0.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 23.5
    developer_ergonomics: 16.0
    discoverability: 56.7
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Lnx Net Authentication
  slug: lnx-net-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Lnx Net Domain Security
  slug: lnx-net-domain-security
  summary_line: TLSv1.3
slug: lnx-net
tags:
- Company
- Link-in-bio
- Creator Tools
- SaaS
- Social Media
- Analytics
website: https://lnx.net/
---
