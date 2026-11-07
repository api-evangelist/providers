---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Awareness provides a persistent memory API via MCP on https://awareness.market/mcp.
  name: Awareness API
  slug: awareness-api
- description: 'Awareness API as documented publicly: 22 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Awareness API
  slug: awareness-market-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/awareness-market/rate-limits/awareness-market-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/awareness-market-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/awareness-market/plans/awareness-market-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/awareness-market-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/awareness-market/rules/awareness-market-rules.yml
  title: ''
  type: Spectral
  url: rules/awareness-market-rules.yml
- group: design
  href: https://artifacts.apis.io/awareness-market/json-ld/awareness-market-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/awareness-market-context.jsonld
- group: design
  href: https://artifacts.apis.io/awareness-market/vocabulary/awareness-market-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/awareness-market-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/awareness-market/data-model/awareness-market-data-model.yml
  title: ''
  type: DataModel
  url: data-model/awareness-market-data-model.yml
- group: operate
  href: https://artifacts.apis.io/awareness-market/changelog/awareness-market-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/awareness-market-changelog.yml
- group: design
  href: https://artifacts.apis.io/awareness-market/conformance/awareness-market-conformance.yml
  title: ''
  type: Conformance
  url: conformance/awareness-market-conformance.yml
- group: agent
  href: https://artifacts.apis.io/awareness-market/llms/awareness-market-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/awareness-market-llms.txt
- group: other
  href: https://artifacts.apis.io/awareness-market/a2a/awareness-market-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/awareness-market-a2a.yml
- group: build
  href: https://artifacts.apis.io/awareness-market/mcp/awareness-market-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/awareness-market-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/awareness-market/mcp/awareness-market-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/awareness-market-mcp.yml
- group: agent
  href: https://artifacts.apis.io/awareness-market/well-known/awareness-market-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/awareness-market-well-known.yml
- group: other
  href: https://artifacts.apis.io/awareness-market/hosts/awareness-market-hosts.yml
  title: ''
  type: Hosts
  url: hosts/awareness-market-hosts.yml
- group: build
  href: https://artifacts.apis.io/awareness-market/packages/awareness-market-packages.yml
  title: ''
  type: SDKs
  url: packages/awareness-market-packages.yml
- group: build
  href: https://artifacts.apis.io/awareness-market/packages/awareness-market-packages.yml
  title: ''
  type: Packages
  url: packages/awareness-market-packages.yml
- group: start
  title: ''
  type: Login
  url: https://awareness.market/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://awareness.market/en/blog/category/changelog
- group: auth
  href: https://artifacts.apis.io/awareness-market/security/awareness-market-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/awareness-market-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://awareness.market/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://awareness.market/developers
- group: docs
  title: ''
  type: Documentation
  url: https://awareness.market/docs
- group: docs
  title: ''
  type: APIReference
  url: https://awareness.market/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://awareness.market/pricing
- group: company
  title: ''
  type: Blog
  url: https://awareness.market/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://awareness.market/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://awareness.market/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/everest-an
created: '2026-11-02'
description: Awareness provides a persistent memory cloud for AI agents and copilots, enabling multi‑agent collaboration, long‑term context retention, and local‑first data storage. It offers open‑source SDKs, MCP support, and optional cloud sync, with tamper‑evident on‑chain history and no login required for basic use.
image: https://awareness.market/og-cover.png
json_schemas:
- name: PostApiV1DealsDealidMatchesRequest
  property_count: 2
  slug: awareness-market-post-api-v1-deals-dealid-matches-request
- name: PostApiV1DealsRequest
  property_count: 4
  slug: awareness-market-post-api-v1-deals-request
- name: PostApiV1OrgKnowledgePublishRequest
  property_count: 2
  slug: awareness-market-post-api-v1-org-knowledge-publish-request
- name: PostApiV1PublicContributionsRequest
  property_count: 6
  slug: awareness-market-post-api-v1-public-contributions-request
- name: PostApiV1PublicRetrieveRequest
  property_count: 2
  slug: awareness-market-post-api-v1-public-retrieve-request
- name: PostMcpResponse
  property_count: 2
  slug: awareness-market-post-mcp-response
jsonld:
- class_count: 7
  name: Awareness Market Context
  property_count: 17
  slug: awareness-market-context
layout: provider
mcp_servers:
- description: Remote MCP server at awareness.market.
  name: Awareness MCP Server
  slug: awareness-market-mcp-yml
modified: '2026-11-02'
name: Awareness
nav: Providers
network: true
overview: 'Awareness is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Memory, Agents, Open Source, and Cloud.


  The Awareness catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Awareness'' developer surface includes changelog, documentation, API reference, pricing, engineering blog, and 23 more developer resources.'
plans:
- name: Awareness Market Plans Pricing
  plan_count: 3
  slug: awareness-market-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Awareness Market Rate Limits
  slug: awareness-market-rate-limits
rules:
- authorship: generated
  effective_rule_count: 86
  extends:
  - spectral:oas
  name: Awareness API Rules
  rule_count: 45
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 4
  slug: awareness-market-rules
scopes:
- name: Awareness Market Scopes
  scope_count: 0
  slug: awareness-market-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 53.9
    contract_governance: 35.6
    contract_quality: 24.7
    developer_ergonomics: 21.4
    discoverability: 56.7
    operational_transparency: 31.6
  previous_composite: 46.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Awareness Market Authentication
  slug: awareness-market-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Awareness Market Domain Security
  slug: awareness-market-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: awareness-market
tags:
- Artificial Intelligence
- Memory
- Agents
- Open Source
- Cloud
website: https://awareness.market/
---
