---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
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
    openapi_examples: verified
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-10-31'
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
overview: 'takehomeapi-com publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Compare API, Rates API, and Take Home API. Tagged areas include Company, UK, Finance, Tax, and Payroll.


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
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 23
    catalog_earned: 64.0
    catalog_earned_first_party: 0.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.0
    contract_governance: 65.5
    contract_quality: 45.7
    developer_ergonomics: 42.1
    discoverability: 66.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
- UK
- Finance
- Tax
- Payroll
website: https://takehomeapi.com/
---
