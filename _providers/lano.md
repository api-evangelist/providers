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
api_count: 1
apis:
- description: Lano provides a global payroll consolidation and Employer of Record (EOR) platform with an API for workforce management.
  name: Lano API
  slug: lano-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/lano/plans/lano-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/lano-plans-pricing.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.lano.io/security
- group: other
  href: https://artifacts.apis.io/lano/hosts/lano-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lano-hosts.yml
- group: other
  href: https://artifacts.apis.io/lano/vendors/lano-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lano-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lano/security/lano-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/lano-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/lano/security/lano-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lano-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.lano.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.lano.io/
- group: docs
  title: ''
  type: Documentation
  url: https://www.lano.io/lano-api
- group: docs
  title: ''
  type: APIReference
  url: https://www.lano.io/lano-api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.lano.io/book-demo
- group: operate
  title: ''
  type: Support
  url: https://www.lano.io/help
- group: company
  title: ''
  type: Blog
  url: https://www.lano.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.lano.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.lano.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.lano.io/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: Documentation pages return JavaScript-rendered HTML shells, preventing machine‑readable spec discovery.
  evidence:
  - status: 404
    url: https://www.lano.io/en/docs/api
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Lano provides a global payroll consolidation and Employer of Record (EOR) platform, enabling companies to hire, pay, and manage employees and contractors across 170+ countries. Their solution includes payroll, compliance, benefits, and payments, with integrations to popular tools. Lano’s API allows developers to automate workforce management, retrieve payroll data, and integrate hiring workflows into their own systems.
image: https://a.storyblok.com/f/140335/1200x628/0bd5e6182c/fallback-image.png
layout: provider
modified: '2026-10-27'
name: Lano
nav: Providers
network: true
overview: 'Lano is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payroll, Employer of Record, and Global Hiring.


  Lano''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Lano Plans Pricing
  plan_count: 4
  slug: lano-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 11
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.3
  facets:
    access_clarity: 59.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 30.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 12.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lano/lano-2026-11-03T134640.png
security:
- kind: domain-security
  name: Lano Domain Security
  slug: lano-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Lano Trust Center
  slug: lano-trust-center
  summary_line: SOC 2, GDPR
slug: lano
tags:
- Company
- Payroll
- Employer of Record
- Global Hiring
website: https://www.lano.io/
---
