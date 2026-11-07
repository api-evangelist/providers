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
- group: other
  href: https://artifacts.apis.io/invoicely/vendors/invoicely-vendors.yml
  title: ''
  type: Vendors
  url: vendors/invoicely-vendors.yml
- group: commercial
  href: https://artifacts.apis.io/invoicely/plans/invoicely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/invoicely-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/invoicely/hosts/invoicely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/invoicely-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://invoicely.com/login
- group: docs
  title: ''
  type: Documentation
  url: https://help.invoicely.com/
- group: auth
  href: https://artifacts.apis.io/invoicely/security/invoicely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/invoicely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://invoicely.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://invoicely.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.invoicely.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://invoicely.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://invoicely.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://invoicely.com/help
coverage:
  checked: '2026-10-26'
  detail: Invoicely’s help center is a JavaScript‑rendered Zendesk site with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://help.invoicely.com/hc/en-us
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-26'
description: Invoicely provides free online invoicing, billing, and payment solutions for small businesses. Their platform lets users create and send invoices, track time and expenses, accept online payments, and manage subscriptions, all through a web-based interface.
layout: provider
modified: '2026-10-26'
name: Invoicely
nav: Providers
network: true
overview: 'Invoicely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Invoicing, Billing, Payments, and Small Business.


  Invoicely''s developer surface includes documentation, pricing, engineering blog, support, and 8 more developer resources.'
plans:
- name: Invoicely Plans Pricing
  plan_count: 4
  slug: invoicely-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.0
  provenance:
    mcp: unknown
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
screenshot: https://apis.io/screenshots/invoicely/invoicely-2026-11-03T134004.png
security:
- kind: domain-security
  name: Invoicely Domain Security
  slug: invoicely-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: invoicely
tags:
- Company
- Invoicing
- Billing
- Payments
- Small Business
website: https://invoicely.com/
---
