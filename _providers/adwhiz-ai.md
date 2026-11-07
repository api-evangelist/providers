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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: REST API for managing Google Ads and Meta Ads accounts.
  name: AdWhiz Ads Manager API
  slug: adwhiz-ads-manager-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/adwhiz-ai/rate-limits/adwhiz-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adwhiz-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/adwhiz-ai/plans/adwhiz-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adwhiz-ai-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/adwhiz-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/adwhiz-ai/changelog/adwhiz-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adwhiz-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/adwhiz-ai/authentication/adwhiz-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adwhiz-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/adwhiz-ai/scopes/adwhiz-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/adwhiz-ai-scopes.yml
- group: design
  href: https://artifacts.apis.io/adwhiz-ai/lifecycle/adwhiz-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adwhiz-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/adwhiz-ai/conformance/adwhiz-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adwhiz-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adwhiz-ai/llms/adwhiz-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adwhiz-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/adwhiz-ai/mcp/adwhiz-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adwhiz-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adwhiz-ai/mcp/adwhiz-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adwhiz-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/adwhiz-ai/well-known/adwhiz-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adwhiz-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adwhiz-ai/hosts/adwhiz-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adwhiz-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adwhiz-ai/vendors/adwhiz-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adwhiz-ai-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.adwhiz.ai/changelog
- group: auth
  href: https://artifacts.apis.io/adwhiz-ai/security/adwhiz-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adwhiz-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adwhiz.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.adwhiz.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.adwhiz.ai/docs/tools
- group: company
  title: ''
  type: Blog
  url: https://www.adwhiz.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adwhiz.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adwhiz.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adwhiz.ai/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.adwhiz.ai/contact
- group: start
  title: ''
  type: GettingStarted
  url: https://www.adwhiz.ai/use-cases
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.adwhiz.ai/docs
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.adwhiz.ai/mcp
  - status: 200
    url: https://adwhiz.ai/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: AdWhiz is an AI-powered platform that audits and manages Google Ads and Meta (Facebook) Ads. It offers free mini‑audits, AI‑generated dashboard health scores, and a suite of 47 MCP tools for integration with Claude Code, Cursor, Windsurf and other AI agents. Plans start at $79 /mo, with features including multi‑account management, automated bid adjustments, and detailed optimization recommendations.
image: https://www.adwhiz.ai/card.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.adwhiz.ai.
  name: adwhiz-ai MCP Server
  slug: adwhiz-ai-mcp-yml
modified: '2026-10-30'
name: adwhiz-ai
nav: Providers
network: true
overview: 'adwhiz-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Google Ads, and Meta Ads.


  adwhiz-ai''s developer surface includes changelog, authentication, documentation, API reference, engineering blog, pricing, support, and 19 more developer resources.'
plans:
- name: Adwhiz Ai Plans Pricing
  plan_count: 3
  slug: adwhiz-ai-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 3
  name: Adwhiz Ai Rate Limits
  slug: adwhiz-ai-rate-limits
scopes:
- name: Adwhiz Ai Scopes
  scope_count: 5
  slug: adwhiz-ai-scopes
  summary_line: 5 scopes
score:
  band: thin
  composite: 33.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.2
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 41.0
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 42.7
  provenance:
    conformance: first-party
    mcp: first-party
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
screenshot: https://apis.io/screenshots/adwhiz-ai/adwhiz-ai-2026-11-03T120327.png
security:
- kind: authentication
  name: Adwhiz Ai Authentication
  slug: adwhiz-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Adwhiz Ai Domain Security
  slug: adwhiz-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: create-campaign
  slug: adwhiz-ai-create-campaign
slug: adwhiz-ai
tags:
- Company
- Artificial Intelligence
- Advertising
- Google Ads
- Meta Ads
- Marketing
website: https://adwhiz.ai/
---
