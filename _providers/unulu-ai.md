---
access_model:
  confidence: high
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: flavored
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
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Unulu Ai Agentic Access
  operation_count: 9
  slug: unulu-ai-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.unulu.ai
  baseurl_source: declared
  description: The Claims API from unulu-ai — 1 operation(s) for claims.
  name: unulu-ai Claims API
  slug: unulu-ai-claims-api
- baseURL: https://api.unulu.ai
  baseurl_source: declared
  description: The Feature Votes API from unulu-ai — 1 operation(s) for feature votes.
  name: unulu-ai Feature Votes API
  slug: unulu-ai-feature-votes-api
- baseURL: https://api.unulu.ai
  baseurl_source: declared
  description: The Sites API from unulu-ai — 5 operation(s) for sites.
  name: unulu-ai Sites API
  slug: unulu-ai-sites-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/unulu-ai/agentic-access/unulu-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/unulu-ai-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/unulu-ai/rules/unulu-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/unulu-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/unulu-ai/json-ld/unulu-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/unulu-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/unulu-ai/vocabulary/unulu-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/unulu-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/unulu-ai/data-model/unulu-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/unulu-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/unulu-ai/errors/unulu-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/unulu-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/unulu-ai/conformance/unulu-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/unulu-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/unulu-ai/llms/unulu-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/unulu-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/unulu-ai/a2a/unulu-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/unulu-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/unulu-ai/mcp/unulu-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/unulu-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/unulu-ai/mcp/unulu-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/unulu-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/unulu-ai/well-known/unulu-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/unulu-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/unulu-ai/hosts/unulu-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/unulu-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/unulu-ai/vendors/unulu-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/unulu-ai-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://unulu.ai/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unulu.ai/terms
- group: operate
  title: ''
  type: Support
  url: https://unulu.ai/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unulu.ai/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://unulu.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://unulu.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://unulu.ai/install
- group: auth
  href: https://artifacts.apis.io/unulu-ai/security/unulu-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/unulu-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://unulu.ai/
- group: agent
  title: ''
  type: llms.txt
  url: https://unulu.ai/llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/unulu-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://unulu.ai/pricing
created: '2026-10-31'
description: unulu™ provides an AI‑powered link‑in‑bio site builder. Developers can create and publish personalized link‑in‑bio pages instantly via a MCP server or REST API, without signup or templates. The service runs on the unu.lu domain, offers free usage, and integrates with major AI agents like Claude, ChatGPT, and Gemini.
image: https://unulu.ai/opengraph-image?faec48898589e26b
json_schemas:
- name: SkinId
  property_count: 0
  slug: unulu-ai-skin-id
jsonld:
- class_count: 2
  name: Unulu Ai Context
  property_count: 1
  slug: unulu-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.unulu.ai.
  name: unulu-ai MCP Server
  slug: unulu-ai-mcp-yml
modified: '2026-10-31'
name: unulu-ai
nav: Providers
network: true
overview: 'unulu-ai publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Claims API, Feature Votes API, and Sites API. Tagged areas include Company, Artificial Intelligence, Link in Bio, and MCP.


  The unulu-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  unulu-ai''s developer surface includes support, documentation, engineering blog, getting-started guide, pricing, and 21 more developer resources.'
plans:
- name: Unulu Ai Plans Pricing
  plan_count: 1
  slug: unulu-ai-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Unulu Ai Rate Limits
  slug: unulu-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: unulu-ai API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: unulu-ai-rules
scopes:
- name: Unulu Ai Scopes
  scope_count: 0
  slug: unulu-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 34
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 40.8
    contract_governance: 22.0
    contract_quality: 51.8
    developer_ergonomics: 14.3
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/unulu-ai/unulu-ai-2026-11-03T145456.png
security:
- kind: authentication
  name: Unulu Ai Authentication
  slug: unulu-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Unulu Ai Domain Security
  slug: unulu-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: unulu-check-handle
  slug: unulu-check-handle
- name: unulu-create-site
  slug: unulu-create-site
- name: unulu-get-state
  slug: unulu-get-state
- name: unulu-update-site
  slug: unulu-update-site
slug: unulu-ai
tags:
- Company
- Artificial Intelligence
- Link in Bio
- MCP
website: https://unulu.ai/
---
