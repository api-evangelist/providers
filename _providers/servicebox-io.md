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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/servicebox-io/plans/servicebox-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/servicebox-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/servicebox-io/llms/servicebox-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/servicebox-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/servicebox-io/well-known/servicebox-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/servicebox-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/servicebox-io/hosts/servicebox-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/servicebox-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/servicebox-io/vendors/servicebox-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/servicebox-io-vendors.yml
- group: auth
  href: https://artifacts.apis.io/servicebox-io/security/servicebox-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/servicebox-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://servicebox.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.servicebox.io/dashboard
- group: start
  title: ''
  type: Login
  url: https://servicebox.io/signin
- group: commercial
  title: ''
  type: Pricing
  url: https://servicebox.io/pricing
- group: start
  title: ''
  type: Sandbox
  url: https://servicebox.io/apis/gold?tab=playground
- group: start
  title: ''
  type: SignUp
  url: https://servicebox.io/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://servicebox.io/status
- group: operate
  title: ''
  type: Support
  url: https://servicebox.io/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://servicebox.io/terms
coverage:
  checked: '2026-10-31'
  detail: API reference page https://servicebox.io/apis returned 404, indicating no public developer documentation.
  evidence:
  - status: 404
    url: https://servicebox.io/apis
  reason: no-developer-program
  state: none
created: '2026-10-31'
description: ServiceBox.io provides a suite of APIs delivering global and local data for Europe and Turkey, covering markets, weather, geography, and more. The platform offers developers easy access to real-time and historical datasets, with comprehensive documentation, sandbox environments, and flexible pricing plans, enabling integration into applications across industries.
image: https://servicebox.io/og/servicebox-tr.png
layout: provider
modified: '2026-10-31'
name: servicebox-io
nav: Providers
network: true
overview: 'servicebox-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data, APIs, Europe, and Turkey.


  servicebox-io''s developer surface includes engineering blog, pricing, sandbox, signup flow, support, and 10 more developer resources.'
plans:
- name: Servicebox Io Plans Pricing
  plan_count: 4
  slug: servicebox-io-plans-pricing
random_paper: 23
score:
  band: emerging
  composite: 22.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.8
    catalog_earned_first_party: 0.0
    catalog_gap: 77.2
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 62.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 48.2
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Servicebox Io Domain Security
  slug: servicebox-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: servicebox-io
tags:
- Company
- Data
- APIs
- Europe
- Turkey
website: https://servicebox.io/
---
