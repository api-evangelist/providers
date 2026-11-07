---
access_model:
  confidence: low
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
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
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/shiftrx/llms/shiftrx-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/shiftrx-llms.txt
- group: other
  href: https://artifacts.apis.io/shiftrx/hosts/shiftrx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/shiftrx-hosts.yml
- group: other
  href: https://artifacts.apis.io/shiftrx/vendors/shiftrx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/shiftrx-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.shiftrx.io/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ShiftRx
- group: auth
  href: https://artifacts.apis.io/shiftrx/security/shiftrx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/shiftrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.shiftrx.io/
coverage:
  checked: '2026-10-30'
  detail: The provider's documentation host https://www.works.ai/ returns a homepage with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://www.works.ai/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Works AI (Trusted Works) provides an integrated platform that automates staffing and scheduling for hospitals and health systems. The solution offers demand forecasting, schedule optimization, extended workforce orchestration, and shift‑fill automation to balance clinical coverage, productivity, and clinician preferences.
layout: provider
modified: '2026-10-30'
name: ShiftRx
nav: Providers
network: true
overview: ShiftRx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Staffing, Scheduling, Healthcare, Workforce Optimization, and Demand Forecasting.
plans:
- name: Shiftrx Plans Pricing
  plan_count: 0
  slug: shiftrx-plans-pricing
random_paper: 8
scopes:
- name: Shiftrx Scopes
  scope_count: 0
  slug: shiftrx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.7
  facets:
    access_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.8
    operational_transparency: 2.6
  previous_composite: 9.4
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 18.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/shiftrx/shiftrx-2026-11-03T143119.png
security:
- kind: authentication
  name: Shiftrx Authentication
  slug: shiftrx-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Shiftrx Domain Security
  slug: shiftrx-domain-security
  summary_line: TLSv1.3 · DMARC
slug: shiftrx
tags:
- Staffing
- Scheduling
- Healthcare
- Workforce Optimization
- Demand Forecasting
- Automation
website: https://www.shiftrx.io/
---
