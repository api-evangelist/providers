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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Leap platform providing endpoints for contractors (CRM, estimating, payments).
  name: Leap API
  slug: leap-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/leap-to-digital/plans/leap-to-digital-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/leap-to-digital-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/leap-to-digital/llms/leap-to-digital-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/leap-to-digital-llms.txt
- group: auth
  href: https://artifacts.apis.io/leap-to-digital/well-known/leap-to-digital-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/leap-to-digital-status-security.txt
- group: agent
  href: https://artifacts.apis.io/leap-to-digital/well-known/leap-to-digital-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/leap-to-digital-well-known.yml
- group: other
  href: https://artifacts.apis.io/leap-to-digital/hosts/leap-to-digital-hosts.yml
  title: ''
  type: Hosts
  url: hosts/leap-to-digital-hosts.yml
- group: other
  href: https://artifacts.apis.io/leap-to-digital/vendors/leap-to-digital-vendors.yml
  title: ''
  type: Vendors
  url: vendors/leap-to-digital-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.leaptodigital.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.leaptodigital.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://leaptodigital.com/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/leap-to-digital/security/leap-to-digital-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/leap-to-digital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://leaptodigital.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.leaptodigital.com/s/
- group: docs
  title: ''
  type: Documentation
  url: https://help.leaptodigital.com/s/
- group: company
  title: ''
  type: Blog
  url: https://leaptodigital.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://leaptodigital.com/pricing
coverage:
  checked: '2026-10-28'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://help.leaptodigital.com/s/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Leap provides cloud‑based software for roofing and remodeling contractors, offering tools for CRM, sales, estimating, contracts, payment processing, and subcontractor management. Their platform helps contractors streamline workflows, improve customer interactions, and grow their businesses with integrated features like dynamic contracts, customizable workflows, and industry‑specific solutions.
image: https://leaptodigital.com/wp-content/uploads/2023/03/Homepage-social-graphic.webp
layout: provider
modified: '2026-10-28'
name: Leap
nav: Providers
network: true
overview: 'Leap is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Roofing, Remodeling, ContractorSoftware, and SaaS.


  Leap''s developer surface includes support, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Leap To Digital Plans Pricing
  plan_count: 4
  slug: leap-to-digital-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 25.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 26.3
  provenance:
    mcp: unknown
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
  name: Leap To Digital Domain Security
  slug: leap-to-digital-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leap-to-digital
tags:
- Company
- Roofing
- Remodeling
- ContractorSoftware
- SaaS
website: https://leaptodigital.com/
---
