---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Helpdesk documentation provides guides for creating accounts, events, and managing settings.
  name: SimpleTix Helpdesk API
  slug: simpletix-helpdesk-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/simpletix/plans/simpletix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simpletix-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/simpletix/llms/simpletix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simpletix-llms.txt
- group: other
  href: https://artifacts.apis.io/simpletix/a2a/simpletix-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/simpletix-a2a.yml
- group: agent
  href: https://artifacts.apis.io/simpletix/well-known/simpletix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simpletix-well-known.yml
- group: other
  href: https://artifacts.apis.io/simpletix/hosts/simpletix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/simpletix-hosts.yml
- group: other
  href: https://artifacts.apis.io/simpletix/vendors/simpletix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/simpletix-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.simpletix.com/category/news/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.simpletix.com/docs/getting-started/creating-account
- group: auth
  href: https://artifacts.apis.io/simpletix/security/simpletix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simpletix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simpletix.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.simpletix.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.simpletix.com/pricing.php
- group: company
  title: ''
  type: Blog
  url: https://www.simpletix.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.simpletix.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.simpletix.com/terms.php
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.simpletix.com/Privacy.php
coverage:
  checked: '2026-10-27'
  detail: Helpdesk site renders documentation via JavaScript, preventing machine-readable contract discovery.
  evidence:
  - status: 200
    url: https://help.simpletix.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: SimpleTix provides an online ticketing platform for attractions, farms, festivals, and events. It offers customizable ticket sales, season passes, and integration with payment processors, aiming to reduce fees compared to competitors. The service includes a manager portal, support resources, and pricing plans for various organization sizes.
image: https://www.simpletix.com/assets/images/logo/logo-gradient.webp
layout: provider
modified: '2026-10-27'
name: SimpleTix
nav: Providers
network: true
overview: 'SimpleTix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Events, SaaS, and OnlinePayments.


  SimpleTix''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Simpletix Plans Pricing
  plan_count: 4
  slug: simpletix-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 58.9
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Simpletix Domain Security
  slug: simpletix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simpletix
tags:
- Company
- Ticketing
- Events
- SaaS
- OnlinePayments
website: https://simpletix.com/
---
