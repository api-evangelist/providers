---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_server: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Beyond Payday provides a personal finance platform with tools for budgeting, retirement planning, and financial tracking.
  name: Beyond Payday API
  slug: beyond-payday-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/beyondpayday-com/plans/beyondpayday-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/beyondpayday-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/beyondpayday-com/llms/beyondpayday-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beyondpayday-com-llms.txt
- group: auth
  href: https://artifacts.apis.io/beyondpayday-com/well-known/beyondpayday-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/beyondpayday-com-security.txt
- group: agent
  href: https://artifacts.apis.io/beyondpayday-com/well-known/beyondpayday-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/beyondpayday-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/beyondpayday-com/hosts/beyondpayday-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beyondpayday-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beyondpayday-com/vendors/beyondpayday-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beyondpayday-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beyondpayday.com/terms
- group: operate
  title: ''
  type: Support
  url: https://beyondpayday.com/help
- group: auth
  title: ''
  type: Security
  url: https://beyondpayday.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beyondpayday.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://beyondpayday.com/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://beyondpayday.com/press
- group: start
  title: ''
  type: Login
  url: https://beyondpayday.com/auth/login
- group: start
  title: ''
  type: GettingStarted
  url: https://beyondpayday.com/help/getting-started
- group: company
  title: ''
  type: Blog
  url: https://beyondpayday.com/blog
- group: auth
  href: https://artifacts.apis.io/beyondpayday-com/security/beyondpayday-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/beyondpayday-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/beyondpayday-com/security/beyondpayday-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beyondpayday-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beyondpayday.com/
coverage:
  detail: Documentation is public but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL was found despite probing.
  evidence:
  - status: 200
    url: https://beyondpayday.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Beyond Payday provides a personal finance platform that helps users track income, bills, debts, net worth, and retirement planning. Built by Shane Stebner through HTMLGuy LLC in St. Petersburg, Florida, it operates without venture capital, investors, or data sales, offering free and paid plans for comprehensive financial insights.
image: https://beyondpayday.com/images/open-graph.jpg
layout: provider
modified: '2026-11-02'
name: Beyond Payday
nav: Providers
network: true
overview: 'Beyond Payday is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Financial Planning, Retirement Planning, Household Budgeting, Personal Finance, and AI Assistant.


  Beyond Payday''s developer surface includes support, pricing, getting-started guide, engineering blog, and 14 more developer resources.'
plans:
- name: Beyondpayday Com Plans Pricing
  plan_count: 2
  slug: beyondpayday-com-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 58.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 21.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beyondpayday Com Domain Security
  slug: beyondpayday-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Beyondpayday Com Vulnerability Disclosure
  slug: beyondpayday-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: beyondpayday-com
tags:
- Financial Planning
- Retirement Planning
- Household Budgeting
- Personal Finance
- AI Assistant
- Debt Payoff
- Financial-Tools
website: https://beyondpayday.com/
---
