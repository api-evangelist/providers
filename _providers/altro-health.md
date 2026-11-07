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
  href: https://artifacts.apis.io/altro-health/plans/altro-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/altro-health-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/altro-health/well-known/altro-health-help-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/altro-health-help-security.txt
- group: agent
  href: https://artifacts.apis.io/altro-health/well-known/altro-health-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/altro-health-well-known.yml
- group: other
  href: https://artifacts.apis.io/altro-health/hosts/altro-health-hosts.yml
  title: ''
  type: Hosts
  url: hosts/altro-health-hosts.yml
- group: other
  href: https://artifacts.apis.io/altro-health/vendors/altro-health-vendors.yml
  title: ''
  type: Vendors
  url: vendors/altro-health-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://altrohealth.com/news/test
- group: start
  title: ''
  type: Login
  url: https://altrohealth.com/log-in
- group: start
  title: ''
  type: GettingStarted
  url: https://help.altrohealth.com/en/collections/19597449-getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.altrohealth.com/
- group: auth
  href: https://artifacts.apis.io/altro-health/security/altro-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/altro-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://altrohealth.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://altrohealth.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://altrohealth.com/blogs
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://altrohealth.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://altrohealth.com/contact
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://altrohealth.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Altro Health provides a digital health platform that connects patients, providers, and payers to streamline care coordination, telehealth visits, and health data analytics. Founded by a collective of healthcare innovators, the company focuses on improving outcomes through integrated technology solutions and secure data exchange across the healthcare ecosystem.
image: https://cdn.prod.website-files.com/6a4834e640cd0e74356162bc/6a48368e7a3aff71d31eee38_Altro%20Health%20Logo%20Draft.png
layout: provider
modified: '2026-10-24'
name: Altro Health
nav: Providers
network: true
overview: 'Altro Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Digital Health, Platform, and Telehealth.


  Altro Health''s developer surface includes getting-started guide, documentation, pricing, engineering blog, support, and 10 more developer resources.'
plans:
- name: Altro Health Plans Pricing
  plan_count: 3
  slug: altro-health-plans-pricing
random_paper: 21
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.6
  facets:
    access_clarity: 48.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 24.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 6.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/altro-health/altro-health-2026-11-03T120742.png
security:
- kind: domain-security
  name: Altro Health Domain Security
  slug: altro-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: altro-health
tags:
- Company
- Health
- Digital Health
- Platform
- Telehealth
website: https://altrohealth.com/
---
