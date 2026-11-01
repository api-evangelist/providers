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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: DateFit provides a platform for integrating fitness data, scheduling appointments, and accessing personalized health insights.
  name: DateFit API
  slug: datefit-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/datefit/plans/datefit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/datefit-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/datefit/hosts/datefit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/datefit-hosts.yml
- group: other
  href: https://artifacts.apis.io/datefit/vendors/datefit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/datefit-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://datefit.com/trust
- group: company
  title: ''
  type: Newsroom
  url: https://datefit.com/press
- group: auth
  href: https://artifacts.apis.io/datefit/security/datefit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/datefit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://datefit.com
- group: docs
  title: ''
  type: Documentation
  url: https://datefit.com/about
- group: company
  title: ''
  type: Blog
  url: https://blog.datefit.com
- group: commercial
  title: ''
  type: Pricing
  url: https://datefit.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://datefit.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datefit.com/privacy-and-data-use-policy
- group: operate
  title: ''
  type: Contact
  url: https://datefit.com/contact
coverage:
  checked: '2026-10-22'
  detail: Docs are served as a JavaScript-rendered single-page app, preventing machine-readable spec discovery.
  evidence:
  - status: 200
    url: https://datefit.com/about
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Datefit is a health and wellness technology company that offers a platform for tracking and analyzing personal health metrics. It provides APIs for integrating fitness data, scheduling appointments, and accessing personalized health insights. The company aims to empower users to make data-driven decisions about their well-being through seamless data integration and analytics.
image: https://datefit.com/og-image.png
layout: provider
modified: '2026-10-22'
name: Datefit
nav: Providers
network: true
overview: 'Datefit is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Wellness, Fitness, and Data Analytics.


  Datefit''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Datefit Plans Pricing
  plan_count: 4
  slug: datefit-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 22.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 71.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 14.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Datefit Domain Security
  slug: datefit-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datefit
tags:
- Health
- Wellness
- Fitness
- Data Analytics
website: https://datefit.com
---
