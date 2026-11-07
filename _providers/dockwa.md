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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/dockwa/plans/dockwa-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dockwa-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dockwa/llms/dockwa-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dockwa-llms.txt
- group: auth
  href: https://artifacts.apis.io/dockwa/well-known/dockwa-mayday-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/dockwa-mayday-security.txt
- group: agent
  href: https://artifacts.apis.io/dockwa/well-known/dockwa-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dockwa-well-known.yml
- group: other
  href: https://artifacts.apis.io/dockwa/hosts/dockwa-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dockwa-hosts.yml
- group: other
  href: https://artifacts.apis.io/dockwa/vendors/dockwa-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dockwa-vendors.yml
- group: auth
  href: https://artifacts.apis.io/dockwa/security/dockwa-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dockwa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dockwa.com
- group: docs
  title: ''
  type: Documentation
  url: https://dockwa.com/about-us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dockwa.com
- group: company
  title: ''
  type: Blog
  url: http://blog.dockwa.com
- group: commercial
  title: ''
  type: Pricing
  url: https://dockwa.com/plus
- group: start
  title: ''
  type: SignUp
  url: https://dockwa.com/claim
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://blog.dockwa.com/mcp
  - status: 200
    url: https://dockwa.com
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-23'
description: Dockwa provides marina management software connecting boaters and marinas. Their platform offers tools for reservations, contracts, customer communication, and occupancy optimization, serving a network of over 300,000 boaters and numerous marinas worldwide.
image: https://assets.dockwa.com/assets/dockwa-social-logo-d4f79ce439ebda4384d8357a16f33b1822a81180afa77a20aa5e0101ce7ef346.png
layout: provider
modified: '2026-10-23'
name: Dockwa
nav: Providers
network: true
overview: 'Dockwa is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Marina, Boating, Software, Software-as-a-Service, and Marketplace.


  Dockwa''s developer surface includes documentation, engineering blog, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Dockwa Plans Pricing
  plan_count: 10
  slug: dockwa-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.6
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 10.7
    discoverability: 55.4
    operational_transparency: 10.5
  previous_composite: 20.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dockwa/dockwa-2026-11-03T130837.png
security:
- kind: domain-security
  name: Dockwa Domain Security
  slug: dockwa-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dockwa
tags:
- Marina
- Boating
- Software
- Software-as-a-Service
- Marketplace
website: https://dockwa.com
---
