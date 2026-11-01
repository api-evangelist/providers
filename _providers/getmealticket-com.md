---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Meal Ticket provides API endpoints for its TrackMax+ platform, but no machine‑readable contract was found.
  name: Meal Ticket API
  slug: meal-ticket-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/getmealticket-com/llms/getmealticket-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getmealticket-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/getmealticket-com/well-known/getmealticket-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getmealticket-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/getmealticket-com/hosts/getmealticket-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/getmealticket-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/getmealticket-com/vendors/getmealticket-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/getmealticket-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mealticket.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mealticket.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/getmealticket-com/security/getmealticket-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getmealticket-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://getmealticket.com/
- group: company
  title: ''
  type: Blog
  url: https://www.mealticket.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.mealticket.com/support
- group: company
  title: ''
  type: About
  url: https://www.mealticket.com/about
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mealticket.com/get-a-demo
- group: start
  title: ''
  type: SignUp
  url: https://www.mealticket.com/demo
- group: start
  title: ''
  type: Login
  url: https://login.mealticket.com/
coverage:
  checked: '2026-10-29'
  detail: All attempted OpenAPI spec URLs on api.getmealticket.com returned redirects to www.mealticket.com and ultimately 404, with no machine‑readable API documentation found.
  evidence:
  - status: 302
    url: https://api.getmealticket.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Meal Ticket provides an end‑to‑end profitability management platform for foodservice distributors, suppliers, and restaurants. Their TrackMax+ solution helps businesses optimize pricing, rebates, and margins across the supply chain, delivering real‑time analytics and actionable insights to improve financial performance.
image: https://cdn.prod.website-files.com/69bb9bea9c683b00952f085d/69bbbd9b487f6dacf569a385_main_logo.svg
layout: provider
modified: '2026-10-29'
name: Meal Ticket
nav: Providers
network: true
overview: 'Meal Ticket is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Foodservice, Profitability, SaaS, and B2B.


  Meal Ticket''s developer surface includes engineering blog, support, getting-started guide, signup flow, and 10 more developer resources.'
random_paper: 15
scopes:
- name: Getmealticket Com Scopes
  scope_count: 0
  slug: getmealticket-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.5
  coverage:
    artifact_dirs: 19
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 29.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Getmealticket Com Authentication
  slug: getmealticket-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Getmealticket Com Domain Security
  slug: getmealticket-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: getmealticket-com
tags:
- Company
- Foodservice
- Profitability
- SaaS
- B2B
website: https://getmealticket.com/
---
