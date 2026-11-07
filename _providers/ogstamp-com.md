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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Ogstamp Com Agentic Access
  operation_count: 8
  slug: ogstamp-com-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Auto API from ogstamp-com — 1 operation(s) for auto.
  name: ogstamp-com Auto API
  slug: ogstamp-com-auto-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Credits API from ogstamp-com — 1 operation(s) for credits.
  name: ogstamp-com Credits API
  slug: ogstamp-com-credits-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Mcp API from ogstamp-com — 1 operation(s) for mcp.
  name: ogstamp-com MCP API
  slug: ogstamp-com-mcp-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Og API from ogstamp-com — 1 operation(s) for og.
  name: ogstamp-com Og API
  slug: ogstamp-com-og-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Packs API from ogstamp-com — 1 operation(s) for packs.
  name: ogstamp-com Packs API
  slug: ogstamp-com-packs-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Peek API from ogstamp-com — 1 operation(s) for peek.
  name: ogstamp-com Peek API
  slug: ogstamp-com-peek-api
- baseURL: https://ogstamp.com
  baseurl_source: declared
  description: The Recover API from ogstamp-com — 1 operation(s) for recover.
  name: ogstamp-com Recover API
  slug: ogstamp-com-recover-api
artifact_total: 16
common:
- group: agent
  href: https://artifacts.apis.io/ogstamp-com/agentic-access/ogstamp-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ogstamp-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/ogstamp-com/rate-limits/ogstamp-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ogstamp-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/ogstamp-com/plans/ogstamp-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ogstamp-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/ogstamp-com/rules/ogstamp-com-rules.yml
  title: ''
  type: Spectral
  url: rules/ogstamp-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/ogstamp-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/ogstamp-com/authentication/ogstamp-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ogstamp-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/ogstamp-com/errors/ogstamp-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ogstamp-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/ogstamp-com/conformance/ogstamp-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ogstamp-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/ogstamp-com/llms/ogstamp-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ogstamp-com-llms.txt
- group: build
  href: https://artifacts.apis.io/ogstamp-com/mcp/ogstamp-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ogstamp-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/ogstamp-com/mcp/ogstamp-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ogstamp-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/ogstamp-com/hosts/ogstamp-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ogstamp-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/ogstamp-com/vendors/ogstamp-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ogstamp-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/ogstamp-com/security/ogstamp-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ogstamp-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ogstamp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://ogstamp.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://ogstamp.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ogstamp.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ogstamp.com/privacy/
created: '2026-10-31'
description: OG Stamp provides a pay‑as‑you‑go API for generating Open Graph and social card images. Users can create custom images via a simple HTTP endpoint, purchase credit packs through PayPal, and integrate the service with client libraries for Node/TypeScript. No subscription required. The platform offers themes, automatic URL parsing for titles and descriptions, and a free designer for quick previews, making it suitable for developers and marketers seeking dynamic visual content without managing image assets.
image: https://ogstamp.com/logo.png
layout: provider
mcp_servers:
- description: Remote MCP server at ogstamp.com.
  name: ogstamp-com MCP Server
  slug: ogstamp-com-mcp-yml
modified: '2026-10-31'
name: ogstamp-com
nav: Providers
network: true
overview: 'ogstamp-com publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auto API, Credits API, MCP API, and 4 more. Tagged areas include OpenGraph, Image Generation, Pay-as-you-go, and Social Media.


  The ogstamp-com catalog on APIs.io includes 1 Spectral governance ruleset.


  ogstamp-com''s developer surface includes authentication, documentation, pricing, and 16 more developer resources.'
plans:
- name: Ogstamp Com Plans Pricing
  plan_count: 3
  slug: ogstamp-com-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 1
  name: Ogstamp Com Rate Limits
  slug: ogstamp-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: ogstamp-com API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: ogstamp-com-rules
scopes:
- name: Ogstamp Com Scopes
  scope_count: 0
  slug: ogstamp-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 56.5
    catalog_earned_first_party: 20.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 46.3
    developer_ergonomics: 23.1
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ogstamp-com/ogstamp-com-2026-11-03T140459.png
security:
- kind: authentication
  name: Ogstamp Com Authentication
  slug: ogstamp-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ogstamp Com Domain Security
  slug: ogstamp-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: render-og-image
  slug: ogstamp-com-render-og-image
slug: ogstamp-com
tags:
- OpenGraph
- Image Generation
- Pay-as-you-go
- Social Media
website: https://ogstamp.com/
---
