---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 30.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Takehomeapi Com Agentic Access
  operation_count: 3
  slug: takehomeapi-com-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://api.takehomeapi.com
  baseurl_source: declared
  description: The Compare API from takehomeapi-com — 1 operation(s) for compare.
  name: takehomeapi-com Compare API
  slug: takehomeapi-com-compare-api
- baseURL: https://api.takehomeapi.com
  baseurl_source: declared
  description: The Rates API from takehomeapi-com — 1 operation(s) for rates.
  name: takehomeapi-com Rates API
  slug: takehomeapi-com-rates-api
- baseURL: https://api.takehomeapi.com
  baseurl_source: declared
  description: The Take Home API from takehomeapi-com — 1 operation(s) for take home.
  name: takehomeapi-com Take Home API
  slug: takehomeapi-com-take-home-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/takehomeapi-com/agentic-access/takehomeapi-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/takehomeapi-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/takehomeapi-com/rate-limits/takehomeapi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/takehomeapi-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/takehomeapi-com/plans/takehomeapi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/takehomeapi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/takehomeapi-com/rules/takehomeapi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/takehomeapi-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/takehomeapi-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/takehomeapi-com/authentication/takehomeapi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/takehomeapi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/takehomeapi-com/errors/takehomeapi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/takehomeapi-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/takehomeapi-com/conformance/takehomeapi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/takehomeapi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/takehomeapi-com/llms/takehomeapi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/takehomeapi-com-llms.txt
- group: other
  href: https://artifacts.apis.io/takehomeapi-com/hosts/takehomeapi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/takehomeapi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/takehomeapi-com/vendors/takehomeapi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/takehomeapi-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/takehomeapi-com/security/takehomeapi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/takehomeapi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://takehomeapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.takehomeapi.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://takehomeapi.com/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://takehomeapi.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://takehomeapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://takehomeapi.com/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:lee.day@leeday.uk
created: '2026-10-31'
description: TakeHome API provides UK take‑home pay calculations, including income tax (England, Wales, Northern Ireland and Scotland), National Insurance, student loans, pensions and the High Income Child Benefit Charge. It sources rates from GOV.UK and the Scottish Government for tax years 2025‑26 and 2026‑27, returning detailed breakdowns and assumptions. The service is offered as a REST API, an MCP server for AI agents, and a pay‑per‑call x402 model. It is operated by Hosting Easy Ltd, a UK‑registered company.
image: https://takehomeapi.com/logo-512.png
layout: provider
modified: '2026-10-31'
name: takehomeapi-com
nav: Providers
network: true
overview: 'takehomeapi-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Compare API, Rates API, and Take Home API. Tagged areas include Company, United Kingdom, Finance, Tax, and Payroll.


  The takehomeapi-com catalog on APIs.io includes 1 Spectral governance ruleset.


  takehomeapi-com''s developer surface includes authentication, API reference, getting-started guide, pricing, support, and 14 more developer resources.'
plans:
- name: Takehomeapi Com Plans Pricing
  plan_count: 4
  slug: takehomeapi-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Takehomeapi Com Rate Limits
  slug: takehomeapi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: takehomeapi-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: takehomeapi-com-rules
scopes:
- name: Takehomeapi Com Scopes
  scope_count: 0
  slug: takehomeapi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.7
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 47.4
    contract_governance: 18.2
    contract_quality: 48.8
    developer_ergonomics: 32.6
    discoverability: 66.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/takehomeapi-com/takehomeapi-com-2026-11-03T144312.png
security:
- kind: authentication
  name: Takehomeapi Com Authentication
  slug: takehomeapi-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Takehomeapi Com Domain Security
  slug: takehomeapi-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 3
skills:
- name: calculate-take-home
  slug: takehomeapi-com-calculate-take-home
- name: compare-scenarios
  slug: takehomeapi-com-compare-scenarios
- name: get-rates
  slug: takehomeapi-com-get-rates
slug: takehomeapi-com
tags:
- Company
- United Kingdom
- Finance
- Tax
- Payroll
website: https://takehomeapi.com/
---
