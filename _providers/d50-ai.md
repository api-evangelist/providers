---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
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
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://app.d50.ai
  baseurl_source: declared
  description: 'D50 AI API as documented publicly: 8 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: D50 AI API
  slug: d50-ai-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/d50-ai/plans/d50-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/d50-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/d50-ai/rules/d50-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/d50-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/d50-ai/json-ld/d50-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/d50-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/d50-ai/vocabulary/d50-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/d50-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/d50-ai/data-model/d50-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/d50-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/d50-ai/authentication/d50-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/d50-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/d50-ai/conformance/d50-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/d50-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/d50-ai/llms/d50-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/d50-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/d50-ai/mcp/d50-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/d50-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/d50-ai/well-known/d50-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/d50-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/d50-ai/hosts/d50-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/d50-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/d50-ai/vendors/d50-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/d50-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/d50-ai/security/d50-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/d50-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://d50.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://d50.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://d50.ai/developers/api
- group: commercial
  title: ''
  type: Pricing
  url: https://d50.ai/pricing
- group: start
  title: ''
  type: GettingStarted
  url: https://d50.ai/developers
coverage:
  checked: '2026-11-04'
  detail: API documentation pages are JavaScript‑rendered and no machine‑readable OpenAPI spec was found.
  evidence:
  - status: 200
    url: https://d50.ai/developers/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-04'
description: D50 AI is an all‑in‑one AI platform that helps businesses and agencies find customers, run ads, manage CRM, create content, and screen hires. It offers a unified credit wallet for AI services, providing tools for marketing, sales, content generation, and recruitment automation. The platform aims to simplify AI integration for small businesses and agencies, offering a free starter tier and scalable pricing.
image: https://d50.ai/d50-og-image.png
json_schemas:
- name: PostApiV1LeadsRevealRequest
  property_count: 1
  slug: d50-ai-post-api-v1-leads-reveal-request
- name: PostApiV1LeadsSearchRequest
  property_count: 3
  slug: d50-ai-post-api-v1-leads-search-request
jsonld:
- class_count: 2
  name: D50 Ai Context
  property_count: 4
  slug: d50-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.d50.ai requiring OAuth.
  name: D50 AI MCP Server
  slug: d50-ai-mcp-yml
modified: '2026-11-04'
name: D50 AI
nav: Providers
network: true
overview: 'D50 AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Marketing, CRM, and Automation.


  The D50 AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  D50 AI''s developer surface includes authentication, documentation, pricing, getting-started guide, and 14 more developer resources.'
plans:
- name: D50 Ai Plans Pricing
  plan_count: 3
  slug: d50-ai-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: D50 AI API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: d50-ai-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 68.8
    catalog_earned_first_party: 12.0
    catalog_gap: 46.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 42.9
    discoverability: 65.0
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
    score: 15.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: D50 Ai Authentication
  slug: d50-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: D50 Ai Domain Security
  slug: d50-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: d50-ai
tags:
- Company
- Artificial Intelligence
- Marketing
- CRM
- Automation
- Platform
website: https://d50.ai/
---
