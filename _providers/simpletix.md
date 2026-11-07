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
overview: 'SimpleTix is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ticketing, Event, Software-as-a-Service, and Online Payments.


  SimpleTix''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 11 more developer resources.'
plans:
- name: Simpletix Plans Pricing
  plan_count: 4
  slug: simpletix-plans-pricing
random_paper: 7
score:
  band: emerging
  composite: 17.3
  coverage:
    artifact_dirs: 11
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 65.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 8.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/simpletix/simpletix-2026-11-03T143226.png
security:
- kind: domain-security
  name: Simpletix Domain Security
  slug: simpletix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simpletix
tags:
- Company
- Ticketing
- Event
- Software-as-a-Service
- Online Payments
website: https://simpletix.com/
---
