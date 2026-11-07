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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/greythr/plans/greythr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/greythr-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/greythr/llms/greythr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/greythr-llms.txt
- group: agent
  href: https://artifacts.apis.io/greythr/well-known/greythr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/greythr-well-known.yml
- group: other
  href: https://artifacts.apis.io/greythr/hosts/greythr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/greythr-hosts.yml
- group: other
  href: https://artifacts.apis.io/greythr/vendors/greythr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/greythr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.greythr.com/terms-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.greythr.com/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://www.greythr.com/login/
- group: auth
  href: https://artifacts.apis.io/greythr/security/greythr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/greythr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.greythr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.greythr.com/greythr-help/
- group: docs
  title: ''
  type: APIReference
  url: https://www.greythr.com/greythr-help/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.greythr.com/guides/complete-guide-hrms/
- group: operate
  title: ''
  type: Support
  url: https://www.greythr.com/greythr-help/
- group: company
  title: ''
  type: Blog
  url: https://www.greythr.com/resources/blogs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.greythr.com/pricing
created: '2026-10-22'
description: greytHR provides an AI‑first full‑suite HRMS and payroll platform serving over 33,000 companies across 30+ countries. It automates recruitment, onboarding, attendance, leave, payroll, performance management and compliance, offering a unified employee record and AI‑driven assistance (NAVOS) to simplify HR operations for enterprises of all sizes.
image: https://www.datocms-assets.com/40521/1725456826-home-page-thumbnail.png?auto=format
layout: provider
modified: '2026-10-22'
name: greytHR
nav: Providers
network: true
overview: 'greytHR is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Human Resources, Payroll, Artificial Intelligence, and Software-as-a-Service.


  greytHR''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Greythr Plans Pricing
  plan_count: 1
  slug: greythr-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.6
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 55.4
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 25.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/greythr/greythr-2026-11-03T133051.png
security:
- kind: domain-security
  name: Greythr Domain Security
  slug: greythr-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: greythr
tags:
- Company
- Human Resources
- Payroll
- Artificial Intelligence
- Software-as-a-Service
website: https://www.greythr.com/
---
