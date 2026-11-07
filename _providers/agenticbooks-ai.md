---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: 'AgenticBooks documentation: agent-native financial infrastructure — onboarding, integrations, and the MCP tool surface.'
  name: AgenticBooks API
  slug: agenticbooks-api
- baseURL: https://api.agenticbooks.ai
  baseurl_source: declared
  description: 'AgenticBooks API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AgenticBooks API
  slug: agenticbooks-ai-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/agenticbooks-ai/plans/agenticbooks-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agenticbooks-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agenticbooks-ai/rules/agenticbooks-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticbooks-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agenticbooks-ai/json-ld/agenticbooks-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenticbooks-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenticbooks-ai/vocabulary/agenticbooks-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenticbooks-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agenticbooks-ai/data-model/agenticbooks-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenticbooks-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/agenticbooks-ai/conformance/agenticbooks-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticbooks-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticbooks-ai/llms/agenticbooks-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticbooks-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/agenticbooks-ai/mcp/agenticbooks-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenticbooks-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agenticbooks-ai/well-known/agenticbooks-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticbooks-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticbooks-ai/hosts/agenticbooks-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticbooks-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticbooks-ai/vendors/agenticbooks-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticbooks-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/agenticbooks-ai/packages/agenticbooks-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/agenticbooks-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/agenticbooks-ai/packages/agenticbooks-ai-packages.yml
  title: ''
  type: Packages
  url: packages/agenticbooks-ai-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agenticbooks.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agenticbooks.ai/privacy
- group: company
  title: ''
  type: Blog
  url: https://www.agenticbooks.ai/blog
- group: auth
  href: https://artifacts.apis.io/agenticbooks-ai/security/agenticbooks-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticbooks-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticbooks.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agenticbooks.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.agenticbooks.ai/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agenticbooks.ai/product
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agenticbooks.ai/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.agenticbooks.ai/contact
- group: start
  title: ''
  type: SignUp
  url: https://app.agenticbooks.ai/sign-up
coverage:
  checked: '2026-11-01'
  detail: Documentation is publicly readable but no machine‑readable spec (OpenAPI, AsyncAPI, GraphQL, etc.) is published.
  evidence:
  - status: 200
    url: https://www.agenticbooks.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: AgenticBooks provides instant financial statements for AI agents and founders. It connects data sources and automatically ships numbers to agents and accountants, enabling automated bookkeeping for AI-driven businesses. The platform offers a web app, API, and documentation for developers to integrate financial reporting into AI workflows.
image: https://www.agenticbooks.ai/icon.svg
json_schemas:
- name: GetAgentAuthTokenResponse
  property_count: 2
  slug: agenticbooks-ai-get-agent-auth-token-response
- name: PostAgentSignupRequest
  property_count: 3
  slug: agenticbooks-ai-post-agent-signup-request
- name: PostAgentSignupResponse
  property_count: 4
  slug: agenticbooks-ai-post-agent-signup-response
jsonld:
- class_count: 3
  name: Agenticbooks Ai Context
  property_count: 9
  slug: agenticbooks-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.agenticbooks.ai.
  name: AgenticBooks MCP Server
  slug: agenticbooks-ai-mcp-yml
modified: '2026-11-01'
name: AgenticBooks
nav: Providers
network: true
overview: 'AgenticBooks is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Bookkeeping, Finance, Automation, and Software-as-a-Service.


  The AgenticBooks catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AgenticBooks'' developer surface includes engineering blog, documentation, API reference, getting-started guide, pricing, support, signup flow, and 17 more developer resources.'
plans:
- name: Agenticbooks Ai Plans Pricing
  plan_count: 1
  slug: agenticbooks-ai-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Agenticbooks Ai Rate Limits
  slug: agenticbooks-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: AgenticBooks API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: agenticbooks-ai-rules
scopes:
- name: Agenticbooks Ai Scopes
  scope_count: 0
  slug: agenticbooks-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.3
  coverage:
    artifact_dirs: 28
    catalog_earned: 59.8
    catalog_earned_first_party: 8.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 25.0
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 37.9
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
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
  name: Agenticbooks Ai Authentication
  slug: agenticbooks-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticbooks Ai Domain Security
  slug: agenticbooks-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: agenticbooks-ai
tags:
- Artificial Intelligence
- Bookkeeping
- Finance
- Automation
- Software-as-a-Service
website: https://agenticbooks.ai/
---
