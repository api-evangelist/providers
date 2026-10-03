---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: API documentation is provided at the embedded content page, but no machine‑readable contract (OpenAPI, GraphQL, etc.) was found.
  name: Autonomy API
  slug: autonomy-api
artifact_total: 3
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/autonomy/refs/heads/main/plans/autonomy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/autonomy-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autonomy/refs/heads/main/hosts/autonomy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autonomy-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/autonomy/refs/heads/main/vendors/autonomy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autonomy-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://autonomy.com/status
- group: commercial
  title: ''
  type: Pricing
  url: https://autonomy.com/tesla/model-3/pricing-comparison
- group: company
  title: ''
  type: Newsroom
  url: https://autonomy.com/press
- group: operate
  title: ''
  type: ChangeLog
  url: https://autonomy.com/changelog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/autonomy/refs/heads/main/security/autonomy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autonomy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autonomy.com
- group: docs
  title: ''
  type: Documentation
  url: https://autonomy.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://autonomy.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://autonomy.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://autonomy.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://autonomy.com/privacy
coverage:
  checked: 2026-09-26
  detail: Documentation page is a JavaScript‑rendered single‑page app with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://autonomy.com/docs/embedded-content
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Autonomy provides a month-to-month car subscription service, allowing customers to drive a variety of vehicles without long-term loans or leases. Users select a vehicle, pay a start fee and monthly payment, and can keep, swap, or return the car at any time. The platform emphasizes flexibility, no commitment, and includes an app for managing subscriptions, payments, and vehicle selection across SUVs, trucks, and electric models.
image: https://autonomy.com/content/home/og-home.jpg
layout: provider
modified: '2026-09-26'
name: Autonomy
nav: Providers
network: true
overview: 'Autonomy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Mobility, Subscription, Car Sharing, and Automotive.


  Autonomy''s developer surface includes pricing, changelog, documentation, support, engineering blog, and 9 more developer resources.'
plans:
- name: Autonomy Plans Pricing
  plan_count: 4
  slug: autonomy-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 25.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 58.9
    operational_transparency: 31.6
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Autonomy Domain Security
  slug: autonomy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autonomy
tags:
- Company
- Mobility
- Subscription
- Car Sharing
- Automotive
website: https://autonomy.com
---
