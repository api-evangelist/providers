---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/wagestream-co-uk/hosts/wagestream-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wagestream-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/wagestream-co-uk/vendors/wagestream-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wagestream-co-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wagestream-co-uk/security/wagestream-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wagestream-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wagestream.co.uk
coverage:
  checked: '2026-10-23'
  detail: Developer pages return HTML shells and require JavaScript, preventing machine-readable spec discovery.
  evidence:
  - status: 404
    url: https://stream.co/en-us/developers
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-22'
description: Stream provides a payroll and employee benefits platform that enables employers to pay wages instantly, manage employee onboarding, and offer financial wellbeing tools. The service integrates with payroll systems, banking APIs, and HR platforms to deliver real-time wage access, savings, and budgeting features for workers across the UK.
layout: provider
modified: '2026-10-22'
name: Stream
nav: Providers
network: true
overview: Stream is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payroll, Fintech, Employee Benefits, and Real-Time Payments.
random_paper: 12
score:
  band: minimal
  composite: 2.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 2.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wagestream-co-uk/wagestream-co-uk-2026-11-03T145947.png
security:
- kind: domain-security
  name: Wagestream Co Uk Domain Security
  slug: wagestream-co-uk-domain-security
  summary_line: DMARC
slug: wagestream-co-uk
tags:
- Company
- Payroll
- Fintech
- Employee Benefits
- Real-Time Payments
website: https://wagestream.co.uk
---
