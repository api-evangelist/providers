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
  href: https://artifacts.apis.io/tanda/plans/tanda-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tanda-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tanda/changelog/tanda-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tanda-changelog.yml
- group: other
  href: https://artifacts.apis.io/tanda/hosts/tanda-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tanda-hosts.yml
- group: other
  href: https://artifacts.apis.io/tanda/vendors/tanda-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tanda-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tanda.com.au/legal/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tanda.com.au/whats-new/july-2025
- group: start
  title: ''
  type: GettingStarted
  url: https://www.tanda.com.au/tools/tanda-payroll-setup
- group: auth
  href: https://artifacts.apis.io/tanda/security/tanda-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tanda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.tanda.com.au/
- group: company
  title: ''
  type: Blog
  url: https://www.tanda.com.au/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tanda.com.au/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://www.tanda.com.au/resource-hub
created: '2026-10-27'
description: Tanda provides cloud‑based workforce management software for Australian businesses, offering tools for roster creation, time‑clock integration, payroll processing, and HR administration. Their platform helps companies automate scheduling, track employee hours, manage leave, and ensure compliance with local labor regulations, all through an intuitive web interface and mobile apps.
image: https://cdn.prod.website-files.com/65aa1c98d591554ddbb5a872/67465d8249e3b3aea783ff69_Open%20Image%20Graph%20(1).png
layout: provider
modified: '2026-10-27'
name: Tanda
nav: Providers
network: true
overview: 'Tanda is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Workforce Management, Payroll, Human Resources, and Scheduling.


  Tanda''s developer surface includes changelog, getting-started guide, engineering blog, pricing, documentation, and 7 more developer resources.'
plans:
- name: Tanda Plans Pricing
  plan_count: 1
  slug: tanda-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 12.9
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 7.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.7
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/tanda/tanda-2026-11-03T144339.png
security:
- kind: domain-security
  name: Tanda Domain Security
  slug: tanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tanda
tags:
- Company
- Workforce Management
- Payroll
- Human Resources
- Scheduling
- Australia
website: https://www.tanda.com.au/
---
