---
access_model:
  confidence: medium
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
    error_semantics: false
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free, public Google Ads MCP server. Connect Claude, Cursor, or any MCP-compatible AI tool to your Google Ads data in under 2 minutes. Read-only, secure, unlimited usage.
  name: Google Ads MCP Server
  slug: google-ads-mcp-server
artifact_total: 7
common:
- group: commercial
  href: https://artifacts.apis.io/adramp-ai/plans/adramp-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adramp-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adramp-ai/mcp/adramp-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adramp-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adramp-ai/well-known/adramp-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adramp-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adramp-ai/hosts/adramp-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adramp-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adramp-ai/vendors/adramp-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adramp-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/adramp-ai/security/adramp-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adramp-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adramp.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://adramp.ai/mcp/
- group: commercial
  title: ''
  type: Pricing
  url: https://adramp.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://adramp.ai/blog/
- group: start
  title: ''
  type: SignUp
  url: https://app.adramp.ai/accounts/signup/
- group: start
  title: ''
  type: Login
  url: https://app.adramp.ai/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://adramp.ai/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://adramp.ai/privacy/
coverage:
  checked: '2026-10-31'
  detail: The public MCP documentation page provides human‑readable information but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable specification is published.
  evidence:
  - status: 200
    url: https://adramp.ai/mcp/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AdRamp is an AI‑powered performance marketing platform that connects to Google Ads, Meta, Shopify and Klaviyo data. Users can ask natural‑language questions, get instant insights, and execute changes directly in their ad accounts via a chat interface. The tool surfaces wasteful search terms, underperforming keywords and budget drains, allowing one‑click actions such as pausing ads, adding negative keywords, and reallocating budgets. Real‑time dashboards track spend, revenue, conversions, ROAS and CPA across campaigns. AdRamp operates as a read‑only, human‑in‑the‑loop system that respects user approvals and privacy. Early‑access is free with plans to be announced.
image: https://adramp.ai/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adramp.ai requiring OAuth.
  name: AdRamp MCP Server
  slug: adramp-ai-mcp-yml
modified: '2026-10-31'
name: AdRamp
nav: Providers
network: true
overview: 'AdRamp is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Marketing, Advertising, Analytics, and Automation.


  AdRamp''s developer surface includes pricing, engineering blog, signup flow, and 11 more developer resources.'
plans:
- name: Adramp Ai Plans Pricing
  plan_count: 2
  slug: adramp-ai-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Adramp Ai Rate Limits
  slug: adramp-ai-rate-limits
scopes:
- name: Adramp Ai Scopes
  scope_count: 0
  slug: adramp-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.2
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.0
    operational_transparency: 0.0
  previous_composite: 23.9
  provenance:
    conformance: unknown
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
security:
- kind: authentication
  name: Adramp Ai Authentication
  slug: adramp-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Adramp Ai Domain Security
  slug: adramp-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: adramp-ai
tags:
- Artificial Intelligence
- Marketing
- Advertising
- Analytics
- Automation
- Software-as-a-Service
website: https://adramp.ai/
---
