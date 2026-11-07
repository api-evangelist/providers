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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/buildcheap-app/plans/buildcheap-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildcheap-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/buildcheap-app/llms/buildcheap-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildcheap-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildcheap-app/well-known/buildcheap-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildcheap-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildcheap-app/hosts/buildcheap-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildcheap-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildcheap-app/vendors/buildcheap-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildcheap-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.buildcheap.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.buildcheap.app/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.buildcheap.app/pricing
- group: start
  title: ''
  type: Login
  url: https://www.buildcheap.app/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.buildcheap.app/blog/v0-alternatives
- group: auth
  href: https://artifacts.apis.io/buildcheap-app/security/buildcheap-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildcheap-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildcheap.app/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://buildcheap.app/
  reason: no-developer-program
  state: none
created: '2026-11-03'
description: BuildCheap AI is an AI‑powered no‑code platform that lets users turn prompts into live web applications, SaaS products, and APIs with built‑in databases, hosting, and real URLs. It aims to accelerate product development by automating code generation and deployment, targeting developers, startups, and enterprises seeking rapid prototyping and scalable cloud services.
image: https://www.buildcheap.app/api/screenshot?url=https:/www.buildcheap.app&title=BuildCheap
layout: provider
modified: '2026-11-03'
name: BuildCheap
nav: Providers
network: true
overview: 'BuildCheap is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, No-Code, Platform, Software-as-a-Service, and Automation.


  BuildCheap''s developer surface includes pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Buildcheap App Plans Pricing
  plan_count: 5
  slug: buildcheap-app-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildcheap App Domain Security
  slug: buildcheap-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: buildcheap-app
tags:
- Artificial Intelligence
- No-Code
- Platform
- Software-as-a-Service
- Automation
website: https://buildcheap.app/
---
