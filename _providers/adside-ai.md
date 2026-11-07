---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.adside.ai
  baseurl_source: declared
  description: Unified API for managing ad campaigns across Meta, LinkedIn, and Google.
  name: Multi-Source Ads API
  slug: multi-source-ads-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/adside-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/adside-ai/rate-limits/adside-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adside-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/adside-ai/plans/adside-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adside-ai-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/adside-ai/authentication/adside-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adside-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/adside-ai/errors/adside-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adside-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/adside-ai/conformance/adside-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adside-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/adside-ai/llms/adside-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adside-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/adside-ai/a2a/adside-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/adside-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/adside-ai/mcp/adside-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adside-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/adside-ai/mcp/adside-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adside-ai-mcp.yml
- group: auth
  href: https://artifacts.apis.io/adside-ai/well-known/adside-ai-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adside-ai-help-security.txt
- group: agent
  href: https://artifacts.apis.io/adside-ai/well-known/adside-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adside-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/adside-ai/hosts/adside-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/adside-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/adside-ai/vendors/adside-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/adside-ai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.adside.ai/en/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.adside.ai/changelog
- group: auth
  href: https://artifacts.apis.io/adside-ai/security/adside-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adside-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://adside.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.adside.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.adside.ai/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.adside.ai/getting-started.md
- group: company
  title: ''
  type: Blog
  url: https://www.adside.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.adside.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adside.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adside.ai/privacy
- group: start
  title: ''
  type: SignUp
  url: https://app.adside.ai/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://app.adside.ai/sign-in
created: '2026-10-31'
description: Adside provides a team of AI agents that manage paid advertising across platforms such as Meta, Google, LinkedIn, Reddit, and Twitter. The service offers market research, strategy drafting, creative generation, campaign monitoring, and optimization. It is available as a self‑service product for $290 per brand per month (or $190 with annual prepay) and as a managed service charging 10 % of ad spend with a $3,500 monthly minimum. Users can get started via the Get Started page, access free tools, view pricing and read the blog for updates.
image: https://www.adside.ai/assets/adside-logo-blue.svg
layout: provider
mcp_servers:
- description: Remote MCP server at docs.adside.ai.
  name: Adside MCP Server
  slug: adside-ai-mcp-yml
modified: '2026-10-31'
name: Adside
nav: Providers
network: true
overview: 'Adside is listed with 1 API on the [APIs.io](https://apis.io/) network: Multi-Source Ads API. Tagged areas include Advertising, Artificial Intelligence, Marketing, Software-as-a-Service, and Automation.


  Adside''s developer surface includes authentication, support, changelog, documentation, API reference, getting-started guide, engineering blog, and 20 more developer resources.'
plans:
- name: Adside Ai Plans Pricing
  plan_count: 3
  slug: adside-ai-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Adside Ai Rate Limits
  slug: adside-ai-rate-limits
scopes:
- name: Adside Ai Scopes
  scope_count: 0
  slug: adside-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.2
  coverage:
    artifact_dirs: 27
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.6
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 32.1
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 39.5
  previous_composite: 49.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
security:
- kind: authentication
  name: Adside Ai Authentication
  slug: adside-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Adside Ai Domain Security
  slug: adside-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: adside-ai
tags:
- Advertising
- Artificial Intelligence
- Marketing
- Software-as-a-Service
- Automation
website: https://adside.ai/
---
