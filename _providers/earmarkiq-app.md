---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
- description: AI‑powered payroll intelligence platform
  name: Earmark API
  slug: earmark-api
artifact_total: 2
common:
- group: design
  href: https://artifacts.apis.io/earmarkiq-app/conformance/earmarkiq-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/earmarkiq-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/earmarkiq-app/llms/earmarkiq-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/earmarkiq-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/earmarkiq-app/well-known/earmarkiq-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/earmarkiq-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/earmarkiq-app/hosts/earmarkiq-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/earmarkiq-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/earmarkiq-app/vendors/earmarkiq-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/earmarkiq-app-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://earmarkiq.app/news/iran-war-uk-inflation-cost-of-living-2026
- group: start
  title: ''
  type: Login
  url: https://earmarkiq.app/login
- group: auth
  href: https://artifacts.apis.io/earmarkiq-app/security/earmarkiq-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/earmarkiq-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://earmarkiq.app/
- group: company
  title: ''
  type: Blog
  url: https://earmarkiq.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://earmarkiq.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://earmarkiq.app/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.earmarkiq.app/openapi.json
  - status: 401
    url: https://api.earmarkiq.app/mcp
  - status: 200
    url: https://earmarkiq.app/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: earmarkIQ is an AI‑powered budgeting application targeting UK professionals. It connects to all major UK bank accounts, providing a personal money coach that tracks spending, suggests bill switches, and helps users meet savings goals. The app is free to download on iOS and offers insights to optimise cash flow, aiming to simplify financial management for busy professionals.
image: https://earmarkiq.app/api/og?title=Meet%20the%20AI%20that%20actually%20knows%20your%20money&subtitle=AI%20money%20coach%20for%20UK%20professionals&stat=%C2%A3588%2Fyr%20saved
layout: provider
modified: '2026-11-06'
name: earmarkIQ
nav: Providers
network: true
overview: 'earmarkIQ is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Artificial Intelligence, Budgeting, and United Kingdom.


  earmarkIQ''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 67.9
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Earmarkiq App Domain Security
  slug: earmarkiq-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: earmarkiq-app
tags:
- Company
- Finance
- Artificial Intelligence
- Budgeting
- United Kingdom
website: https://earmarkiq.app/
---
