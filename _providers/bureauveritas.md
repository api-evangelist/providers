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
    mcp_server: documented
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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/bureauveritas/hosts/bureauveritas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bureauveritas-hosts.yml
- group: other
  href: https://artifacts.apis.io/bureauveritas/vendors/bureauveritas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bureauveritas-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://group.bureauveritas.com/terms-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://personaldataprotection.bureauveritas.com/privacypolicy
- group: company
  title: ''
  type: Newsroom
  url: https://group.bureauveritas.com/newsroom
- group: auth
  href: https://artifacts.apis.io/bureauveritas/security/bureauveritas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bureauveritas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://group.bureauveritas.com
coverage:
  checked: '2026-11-03'
  detail: Main website returns HTML pages without machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://group.bureauveritas.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-03'
description: Bureau Veritas is a global leader in testing, inspection and certification services, helping clients improve performance and manage risk across a wide range of industries. The company provides expertise in quality, health, safety, environment and sustainability, offering solutions that enable businesses to achieve excellence and compliance. With a presence in over 140 countries, Bureau Veritas supports clients in navigating technological and societal changes to drive sustainable performance.
layout: provider
modified: '2026-11-03'
name: Bureau Veritas
nav: Providers
network: true
overview: Bureau Veritas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Testing, Inspection, Certification, Sustainability, and ESG Reporting.
random_paper: 18
score:
  band: minimal
  composite: 5.9
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 45.5
    operational_transparency: 0.0
  provenance:
    mcp: first-party
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
  name: Bureauveritas Domain Security
  slug: bureauveritas-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bureauveritas
tags:
- Testing
- Inspection
- Certification
- Sustainability
- ESG Reporting
- Risk Management
website: https://group.bureauveritas.com
---
