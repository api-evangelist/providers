---
access_model:
  confidence: high
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
    auth_clarity: false
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Quote, price and request a cost segregation workpaper or study on US rental and commercial property.
  name: ClickDrag Finance Cost Segregation API
  slug: cost-segregation-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/clickdrag-finance/rate-limits/clickdrag-finance-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/clickdrag-finance-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/clickdrag-finance/plans/clickdrag-finance-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clickdrag-finance-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clickdrag-finance/vocabulary/clickdrag-finance-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clickdrag-finance-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clickdrag-finance/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/clickdrag-finance/changelog/clickdrag-finance-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/clickdrag-finance-changelog.yml
- group: design
  href: https://artifacts.apis.io/clickdrag-finance/lifecycle/clickdrag-finance-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/clickdrag-finance-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/clickdrag-finance/errors/clickdrag-finance-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clickdrag-finance-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clickdrag-finance/conformance/clickdrag-finance-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clickdrag-finance-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clickdrag-finance/llms/clickdrag-finance-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clickdrag-finance-llms.txt
- group: build
  href: https://artifacts.apis.io/clickdrag-finance/mcp/clickdrag-finance-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/clickdrag-finance-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/clickdrag-finance/mcp/clickdrag-finance-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/clickdrag-finance-mcp.yml
- group: agent
  href: https://artifacts.apis.io/clickdrag-finance/well-known/clickdrag-finance-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clickdrag-finance-well-known.yml
- group: other
  href: https://artifacts.apis.io/clickdrag-finance/hosts/clickdrag-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clickdrag-finance-hosts.yml
- group: other
  href: https://artifacts.apis.io/clickdrag-finance/vendors/clickdrag-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clickdrag-finance-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.clickdragfinance.com/auth/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CostSeg-Solutions
- group: auth
  href: https://artifacts.apis.io/clickdrag-finance/security/clickdrag-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clickdrag-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.clickdragfinance.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.clickdragfinance.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.clickdragfinance.com/developers.md
- group: docs
  title: ''
  type: APIReference
  url: https://www.clickdragfinance.com/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://www.clickdragfinance.com/cost-segregation-audit-support
- group: company
  title: ''
  type: Blog
  url: https://www.clickdragfinance.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.clickdragfinance.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.clickdragfinance.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.clickdragfinance.com/privacy
created: '2026-10-30'
description: ClickDrag Finance provides cost segregation reports and studies for U.S. rental and commercial real estate owners, CPAs, and financial advisors. Their platform offers an API and MCP server that deliver cost segregation calculations, pricing, benchmarks, and consulting booking, with no API key required and generous rate limits. The service helps clients accelerate depreciation deductions and optimize tax savings.
image: https://www.clickdragfinance.com/og-default.png
layout: provider
mcp_servers:
- description: Remote MCP server at www.clickdragfinance.com.
  name: ClickDrag Finance MCP Server
  slug: clickdrag-finance-mcp-yml
modified: '2026-10-30'
name: ClickDrag Finance
nav: Providers
network: true
overview: 'ClickDrag Finance is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Cost Segregation, Real Estate, and Tax.


  ClickDrag Finance''s developer surface includes changelog, documentation, API reference, support, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Clickdrag Finance Plans Pricing
  plan_count: 3
  slug: clickdrag-finance-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 5
  name: Clickdrag Finance Rate Limits
  slug: clickdrag-finance-rate-limits
scopes:
- name: Clickdrag Finance Scopes
  scope_count: 0
  slug: clickdrag-finance-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 25
    catalog_earned: 57.3
    catalog_earned_first_party: 24.0
    catalog_gap: 57.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.5
  facets:
    access_clarity: 53.9
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 23.1
    discoverability: 56.7
    operational_transparency: 50.0
  previous_composite: 39.5
  provenance:
    conformance: derived
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/clickdrag-finance/clickdrag-finance-2026-11-03T124421.png
security:
- kind: authentication
  name: Clickdrag Finance Authentication
  slug: clickdrag-finance-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Clickdrag Finance Domain Security
  slug: clickdrag-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: get-cost-segregation-benchmarks
  slug: clickdrag-finance-get_cost_segregation_benchmarks
- name: get-cost-segregation-pricing
  slug: clickdrag-finance-get_cost_segregation_pricing
- name: get-cost-segregation-provider-facts
  slug: clickdrag-finance-get_cost_segregation_provider_facts
- name: quote-cost-segregation-study
  slug: clickdrag-finance-quote_cost_segregation_study
slug: clickdrag-finance
tags:
- Finance
- Cost Segregation
- Real Estate
- Tax
website: https://www.clickdragfinance.com
---
