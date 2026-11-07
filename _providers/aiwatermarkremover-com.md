---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Aiwatermarkremover Com Agentic Access
  operation_count: 2
  slug: aiwatermarkremover-com-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: Process only images you own or have permission to edit. One successful paid removal uses one account credit.
  name: AI Watermark Remover API
  slug: api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/aiwatermarkremover-com/agentic-access/aiwatermarkremover-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aiwatermarkremover-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/aiwatermarkremover-com/rate-limits/aiwatermarkremover-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aiwatermarkremover-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/aiwatermarkremover-com/plans/aiwatermarkremover-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aiwatermarkremover-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/rules/aiwatermarkremover-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aiwatermarkremover-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/json-ld/aiwatermarkremover-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aiwatermarkremover-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/vocabulary/aiwatermarkremover-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aiwatermarkremover-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aiwatermarkremover-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/data-model/aiwatermarkremover-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aiwatermarkremover-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/aiwatermarkremover-com/authentication/aiwatermarkremover-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aiwatermarkremover-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/errors/aiwatermarkremover-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aiwatermarkremover-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aiwatermarkremover-com/conformance/aiwatermarkremover-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aiwatermarkremover-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aiwatermarkremover-com/mcp/aiwatermarkremover-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aiwatermarkremover-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/aiwatermarkremover-com/well-known/aiwatermarkremover-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aiwatermarkremover-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aiwatermarkremover-com/hosts/aiwatermarkremover-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aiwatermarkremover-com-hosts.yml
- group: auth
  href: https://artifacts.apis.io/aiwatermarkremover-com/security/aiwatermarkremover-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aiwatermarkremover-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aiwatermarkremover.com/
- group: start
  title: ''
  type: Portal
  url: https://aiwatermarkremover.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://aiwatermarkremover.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://aiwatermarkremover.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://aiwatermarkremover.com/contact
- group: company
  title: ''
  type: Blog
  url: https://aiwatermarkremover.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aiwatermarkremover.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aiwatermarkremover.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aiwatermarkremover.com/privacy
created: '2026-11-01'
description: AI Watermark Remover provides an online tool that uses artificial intelligence to automatically detect and remove watermarks, logos, and text from images. It offers fast processing, first removal free, supports multiple formats (PNG, JPG, JPEG, WebP, HEIC) up to 5MB, preserves original resolution and colors, and ensures privacy. The service is accessible via a simple drag‑and‑drop interface and does not require signup.
image: https://aiwatermarkremover.com/logos/logo-64.png
json_schemas:
- name: Account
  property_count: 5
  slug: aiwatermarkremover-com-account
- name: RemovalResponse
  property_count: 1
  slug: aiwatermarkremover-com-removal-response
jsonld:
- class_count: 3
  name: Aiwatermarkremover Com Context
  property_count: 7
  slug: aiwatermarkremover-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at aiwatermarkremover.com.
  name: AI Watermark Remover MCP Server
  slug: aiwatermarkremover-com-mcp-yml
modified: '2026-11-01'
name: AI Watermark Remover
nav: Providers
network: true
overview: 'AI Watermark Remover is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Image Processing, Watermark Removal, Online Tool, and Free.


  The AI Watermark Remover catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AI Watermark Remover''s developer surface includes authentication, developer portal, documentation, API reference, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Aiwatermarkremover Com Plans Pricing
  plan_count: 1
  slug: aiwatermarkremover-com-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Aiwatermarkremover Com Rate Limits
  slug: aiwatermarkremover-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: AI Watermark Remover API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: aiwatermarkremover-com-rules
scopes:
- name: Aiwatermarkremover Com Scopes
  scope_count: 0
  slug: aiwatermarkremover-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 35.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 72.8
    catalog_earned_first_party: 16.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.1
  facets:
    access_clarity: 36.8
    contract_governance: 35.6
    contract_quality: 18.7
    developer_ergonomics: 39.8
    discoverability: 65.0
    operational_transparency: 21.1
  previous_composite: 41.6
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: unknown
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
  name: Aiwatermarkremover Com Authentication
  slug: aiwatermarkremover-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Aiwatermarkremover Com Domain Security
  slug: aiwatermarkremover-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 2
skills:
- name: get-account
  slug: aiwatermarkremover-com-get-account
- name: remove-watermark
  slug: aiwatermarkremover-com-remove-watermark
slug: aiwatermarkremover-com
tags:
- Artificial Intelligence
- Image Processing
- Watermark Removal
- Online Tool
- Free
website: https://aiwatermarkremover.com/
---
