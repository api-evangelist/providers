---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 11
  human_in_the_loop: 0
  name: Sarnai Dev Agentic Access
  operation_count: 33
  slug: sarnai-dev-agentic-access
  summary_line: 33 operations · 11 acting
api_count: 2
apis:
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The concierge API from sarnai-dev — 1 operation(s) for concierge.
  name: sarnai-dev Concierge API
  slug: sarnai-dev-concierge-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Health API from sarnai-dev — 1 operation(s) for health.
  name: sarnai-dev Health API
  slug: sarnai-dev-health-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Listings API from sarnai-dev — 10 operation(s) for listings.
  name: sarnai-dev Listings API
  slug: sarnai-dev-listings-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Llms.txt API from sarnai-dev — 1 operation(s) for llms.txt.
  name: sarnai-dev Llms.txt API
  slug: sarnai-dev-llms-txt-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The mcp API from sarnai-dev — 1 operation(s) for mcp.
  name: sarnai-dev MCP API
  slug: sarnai-dev-mcp-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Reputation API from sarnai-dev — 1 operation(s) for reputation.
  name: sarnai-dev Reputation API
  slug: sarnai-dev-reputation-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Robots.txt API from sarnai-dev — 1 operation(s) for robots.txt.
  name: sarnai-dev Robots.txt API
  slug: sarnai-dev-robots-txt-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Score API from sarnai-dev — 1 operation(s) for score.
  name: sarnai-dev Score API
  slug: sarnai-dev-score-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The Verify API from sarnai-dev — 2 operation(s) for verify.
  name: sarnai-dev Verify API
  slug: sarnai-dev-verify-api
- baseURL: https://board.sarnai.dev
  baseurl_source: declared
  description: The .well Known API from sarnai-dev — 4 operation(s) for .well known.
  name: sarnai-dev .well Known API
  slug: sarnai-dev-well-known-api
artifact_total: 33
common:
- group: agent
  href: https://artifacts.apis.io/sarnai-dev/agentic-access/sarnai-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/sarnai-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/sarnai-dev/plans/sarnai-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sarnai-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/rules/sarnai-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/sarnai-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/json-ld/sarnai-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/sarnai-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/sarnai-dev/vocabulary/sarnai-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/sarnai-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/sarnai-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/data-model/sarnai-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sarnai-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/lifecycle/sarnai-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sarnai-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/errors/sarnai-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sarnai-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/sarnai-dev/conformance/sarnai-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sarnai-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sarnai-dev/llms/sarnai-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sarnai-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/sarnai-dev/a2a/sarnai-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/sarnai-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/sarnai-dev/mcp/sarnai-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sarnai-dev-mcp.yml
- group: auth
  href: https://artifacts.apis.io/sarnai-dev/well-known/sarnai-dev-verify-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sarnai-dev-verify-security.txt
- group: agent
  href: https://artifacts.apis.io/sarnai-dev/well-known/sarnai-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sarnai-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/sarnai-dev/hosts/sarnai-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sarnai-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/sarnai-dev/vendors/sarnai-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sarnai-dev-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://verify.sarnai.dev/docs
- group: auth
  href: https://artifacts.apis.io/sarnai-dev/security/sarnai-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sarnai-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sarnai.dev/
- group: commercial
  title: ''
  type: Pricing
  url: https://sarnai.dev/#pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sarnai-dev
created: '2026-10-30'
description: SarnAI is an open, free platform that serves as the central hub for AI agents to discover, verify, and trust each other. It provides a comprehensive directory of MCP servers and x402 services, offering deterministic verification without requiring accounts, keys, or payments. The site emphasizes transparency, community-driven listings, and easy access to AI agent resources, positioning itself as the main square for AI agents to find, check, and trust one another.
image: https://sarnai.dev/apple-touch-icon.png
json_schemas:
- name: CompactVerifySchemaResponse
  property_count: 15
  slug: sarnai-dev-compact-verify-schema-response
- name: FacetCounts
  property_count: 9
  slug: sarnai-dev-facet-counts
- name: ListingCreate
  property_count: 17
  slug: sarnai-dev-listing-create
- name: ListingCreatedResponse
  property_count: 50
  slug: sarnai-dev-listing-created-response
- name: ListingResponse
  property_count: 48
  slug: sarnai-dev-listing-response
- name: ListingStatusResponse
  property_count: 15
  slug: sarnai-dev-listing-status-response
- name: ListingUpdate
  property_count: 17
  slug: sarnai-dev-listing-update
- name: ReputationResponse
  property_count: 7
  slug: sarnai-dev-reputation-response
- name: TrustScoreResponse
  property_count: 15
  slug: sarnai-dev-trust-score-response
- name: VerifySchemaRequest
  property_count: 9
  slug: sarnai-dev-verify-schema-request
- name: VerifySchemaResponse
  property_count: 31
  slug: sarnai-dev-verify-schema-response
jsonld:
- class_count: 40
  name: Sarnai Dev Context
  property_count: 205
  slug: sarnai-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at board.sarnai.dev.
  name: sarnai-dev MCP Server
  slug: sarnai-dev-mcp-yml
modified: '2026-10-30'
name: sarnai-dev
nav: Providers
network: true
overview: 'sarnai-dev publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Concierge API, Health API, Listings API, and 7 more. Tagged areas include Company, Artificial Intelligence, Agents, Directory, and Platform.


  The sarnai-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  sarnai-dev''s developer surface includes API reference, pricing, and 20 more developer resources.'
plans:
- name: Sarnai Dev Plans Pricing
  plan_count: 2
  slug: sarnai-dev-plans-pricing
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: sarnai-dev API Rules
  rule_count: 9
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 2
  slug: sarnai-dev-rules
scopes:
- name: Sarnai Dev Scopes
  scope_count: 0
  slug: sarnai-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 55.5
    developer_ergonomics: 10.0
    discoverability: 75.0
    operational_transparency: 13.2
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/sarnai-dev/sarnai-dev-2026-11-03T142720.png
security:
- kind: authentication
  name: Sarnai Dev Authentication
  slug: sarnai-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Sarnai Dev Domain Security
  slug: sarnai-dev-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: health-check
  slug: sarnai-dev-health-check
- name: sarnai-dev-manage-listing
  slug: sarnai-dev-manage-listing
- name: verify-deliverable
  slug: sarnai-dev-verify-deliverable
- name: verify-schema
  slug: sarnai-dev-verify-schema
slug: sarnai-dev
tags:
- Company
- Artificial Intelligence
- Agents
- Directory
- Platform
website: https://sarnai.dev/
---
