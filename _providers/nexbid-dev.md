---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Nexbid Dev Agentic Access
  operation_count: 9
  slug: nexbid-dev-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 2
apis:
- baseURL: https://nexbid.dev
  baseurl_source: declared
  description: LLM-facing HTTP surface.
  name: nexbid-dev Agent API
  slug: nexbid-dev-agent-api
- baseURL: https://api.nexbid.dev
  baseurl_source: declared
  description: Click tracking and conversion attribution
  name: nexbid-dev Attribution API
  slug: nexbid-dev-attribution-api
- baseURL: https://nexbid.dev
  baseurl_source: declared
  description: Well-known capability manifests.
  name: nexbid-dev Discovery API
  slug: nexbid-dev-discovery-api
artifact_total: 24
common:
- group: agent
  href: https://artifacts.apis.io/nexbid-dev/agentic-access/nexbid-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/nexbid-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/nexbid-dev/plans/nexbid-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/nexbid-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/nexbid-dev/rules/nexbid-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/nexbid-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/nexbid-dev/json-ld/nexbid-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/nexbid-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/nexbid-dev/vocabulary/nexbid-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/nexbid-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/nexbid-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/nexbid-dev/data-model/nexbid-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/nexbid-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/nexbid-dev/errors/nexbid-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/nexbid-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/nexbid-dev/conformance/nexbid-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/nexbid-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/nexbid-dev/llms/nexbid-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/nexbid-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/nexbid-dev/a2a/nexbid-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/nexbid-dev-a2a.yml
- group: build
  href: https://artifacts.apis.io/nexbid-dev/mcp/nexbid-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/nexbid-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/nexbid-dev/mcp/nexbid-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/nexbid-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/nexbid-dev/well-known/nexbid-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/nexbid-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/nexbid-dev/hosts/nexbid-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nexbid-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/nexbid-dev/vendors/nexbid-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nexbid-dev-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://nexbid.dev/press
- group: auth
  href: https://artifacts.apis.io/nexbid-dev/security/nexbid-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nexbid-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://nexbid.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://nexbid.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://nexbid.dev/.well-known/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://nexbid.dev/docs/getting-started
- group: operate
  title: ''
  type: Support
  url: https://nexbid.dev/support
- group: company
  title: ''
  type: Blog
  url: https://nexbid.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nexbid-dev
- group: commercial
  title: ''
  type: Pricing
  url: https://nexbid.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://nexbid.dev/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nexbid.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nexbid.dev/privacy
created: '2026-10-30'
description: Nexbid provides an open-source infrastructure for agent commerce, enabling AI agents to discover and purchase products, recipes, services, and editorial content across a federated marketplace. Operated by digital opua GmbH in Switzerland, the platform processes data within the EU, complies with GDPR and nDSG, and offers both a Model Context Protocol (MCP) JSON-RPC endpoint and a REST discovery API. It supports standards such as OpenAPI, OpenRTB, and contributes to industry protocols through IAB Tech Lab and the Linux Foundation.
image: https://nexbid.dev/nexbid-logo.svg
json_schemas:
- name: AgentSnippet
  property_count: 11
  slug: nexbid-dev-agent-snippet
- name: ClickRequest
  property_count: 1
  slug: nexbid-dev-click-request
- name: ClickResponse
  property_count: 1
  slug: nexbid-dev-click-response
- name: DiscoverRequest
  property_count: 5
  slug: nexbid-dev-discover-request
- name: DiscoverResponse
  property_count: 1
  slug: nexbid-dev-discover-response
- name: FeedCreateRequest
  property_count: 5
  slug: nexbid-dev-feed-create-request
- name: FeedCreateResponse
  property_count: 1
  slug: nexbid-dev-feed-create-response
- name: MatchResponse
  property_count: 5
  slug: nexbid-dev-match-response
jsonld:
- class_count: 12
  name: Nexbid Dev Context
  property_count: 36
  slug: nexbid-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.nexbid.dev requiring an API key.
  name: nexbid-dev MCP Server
  slug: nexbid-dev-mcp-yml
modified: '2026-10-30'
name: nexbid-dev
nav: Providers
network: true
overview: 'nexbid-dev publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Agent API, Attribution API, and Discovery API. Tagged areas include Company, AI, Commerce, Advertising, and Switzerland.


  The nexbid-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  nexbid-dev''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Nexbid Dev Plans Pricing
  plan_count: 3
  slug: nexbid-dev-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Nexbid Dev Rate Limits
  slug: nexbid-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: nexbid-dev API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: nexbid-dev-rules
scopes:
- name: Nexbid Dev Scopes
  scope_count: 0
  slug: nexbid-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 22.0
    contract_quality: 60.9
    developer_ergonomics: 42.1
    discoverability: 66.7
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Nexbid Dev Authentication
  slug: nexbid-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Nexbid Dev Domain Security
  slug: nexbid-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: create-feed
  slug: nexbid-dev-create-feed
- name: discover-products
  slug: nexbid-dev-discover-products
- name: discovery
  slug: nexbid-dev-discovery
- name: generate-click-url
  slug: nexbid-dev-generate-click-url
slug: nexbid-dev
tags:
- Company
- AI
- Commerce
- Advertising
- Switzerland
- OpenSource
website: https://nexbid.dev/
---
