---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
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
  href: https://artifacts.apis.io/cardealertracker-app/plans/cardealertracker-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cardealertracker-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/cardealertracker-app/llms/cardealertracker-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cardealertracker-app-llms.txt
- group: other
  href: https://artifacts.apis.io/cardealertracker-app/hosts/cardealertracker-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cardealertracker-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cardealertracker-app/vendors/cardealertracker-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cardealertracker-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cardealertracker.app/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cardealertracker.app/privacy/
- group: start
  title: ''
  type: Login
  url: https://cardealertracker.app/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://cardealertracker.app/changelog/
- group: auth
  href: https://artifacts.apis.io/cardealertracker-app/security/cardealertracker-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cardealertracker-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cardealertracker.app/
- group: docs
  title: ''
  type: Documentation
  url: https://cardealertracker.app/mcp/
- group: commercial
  title: ''
  type: Pricing
  url: https://cardealertracker.app/pricing/
- group: company
  title: ''
  type: About
  url: https://cardealertracker.app/about/
- group: operate
  title: ''
  type: Support
  url: https://cardealertracker.app/support/
coverage:
  checked: '2026-11-03'
  detail: Documentation at https://cardealertracker.app/mcp/ is a JavaScript‑rendered site with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://cardealertracker.app/mcp/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Car Dealer Tracker is a founder‑led independent software company offering a voice‑enabled car dealer management app. Launched in 2022 in the United Arab Emirates, it helps independent dealers track inventory, expenses, repairs, sales and profit across web, iOS and Android. The platform supports 89 countries, over 2,700 vehicles and provides real‑time profit calculations, voice commands, and multi‑device sync for small to medium dealerships.
image: https://cardealertracker.app/og/og-en.jpg
layout: provider
modified: '2026-11-03'
name: Car Dealer Tracker
nav: Providers
network: true
overview: 'Car Dealer Tracker is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Dealership Software, Inventory, Vehicle Expenses, Profit Tracking, and CRM.


  Car Dealer Tracker''s developer surface includes changelog, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Cardealertracker App Plans Pricing
  plan_count: 4
  slug: cardealertracker-app-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 17.3
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
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 7.9
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cardealertracker App Domain Security
  slug: cardealertracker-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cardealertracker-app
tags:
- Dealership Software
- Inventory
- Vehicle Expenses
- Profit Tracking
- CRM
- Mobile App
- Voice Input
- Accounting
website: https://cardealertracker.app/
---
