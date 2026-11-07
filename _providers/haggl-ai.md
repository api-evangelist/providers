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
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: haggl.ai MCP endpoint providing tool definitions for price negotiation.
  name: haggl-ai MCP
  slug: haggl-ai-mcp
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/haggl-ai/plans/haggl-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/haggl-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/haggl-ai/errors/haggl-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/haggl-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/haggl-ai/llms/haggl-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/haggl-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/haggl-ai/mcp/haggl-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/haggl-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/haggl-ai/well-known/haggl-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/haggl-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/haggl-ai/hosts/haggl-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/haggl-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/haggl-ai/vendors/haggl-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/haggl-ai-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.haggl.ai/login
- group: other
  title: ''
  type: Leadership
  url: https://www.haggl.ai/team
- group: auth
  href: https://artifacts.apis.io/haggl-ai/security/haggl-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/haggl-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://haggl.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.haggl.ai/protocol
- group: docs
  title: ''
  type: APIReference
  url: https://www.haggl.ai/protocol
- group: start
  title: ''
  type: GettingStarted
  url: https://www.haggl.ai/launch
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.haggl.ai/launch
- group: commercial
  title: ''
  type: Pricing
  url: https://www.haggl.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.haggl.ai/blog
- group: operate
  title: ''
  type: Support
  url: https://www.haggl.ai/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.haggl.ai/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.haggl.ai/privacy
created: '2026-10-30'
description: haggl.ai provides performance marketing for agentic commerce, enabling merchants to have sales agents that negotiate personalized offers with shopper agents within defined budgets. The platform integrates with e‑commerce solutions like Shopify Plus and Wix, automating offer creation and handling. It leverages AI-driven negotiation protocols to streamline B2B and B2C transactions, delivering tailored pricing and improving conversion rates.
image: https://www.haggl.ai/brand/exchange-avatar-dark.png
layout: provider
mcp_servers:
- description: haggl.ai provides a hosted MCP server on its own domain. The documented URL is https://www.haggl.ai/api/mcp.
  name: haggl-ai MCP Server
  slug: haggl-ai-mcp-yml
modified: '2026-10-30'
name: haggl-ai
nav: Providers
network: true
overview: 'haggl-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Commerce, Negotiation, Marketing, and Platform.


  haggl-ai''s developer surface includes documentation, API reference, getting-started guide, pricing, engineering blog, support, and 14 more developer resources.'
plans:
- name: Haggl Ai Plans Pricing
  plan_count: 2
  slug: haggl-ai-plans-pricing
random_paper: 18
scopes:
- name: Haggl Ai Scopes
  scope_count: 0
  slug: haggl-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 75.8
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.7
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/haggl-ai/haggl-ai-2026-11-03T133132.png
security:
- kind: authentication
  name: Haggl Ai Authentication
  slug: haggl-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Haggl Ai Domain Security
  slug: haggl-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: haggl-ai
tags:
- Artificial Intelligence
- Commerce
- Negotiation
- Marketing
- Platform
website: https://haggl.ai/
---
