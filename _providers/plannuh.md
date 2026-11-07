---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
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
  band: agent-aware
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Planful provides cloud‑based budgeting, planning, and performance management software APIs.
  name: Planful API
  slug: planful-api
artifact_total: 7
common:
- group: operate
  href: https://artifacts.apis.io/plannuh/changelog/plannuh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/plannuh-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.planful.com/
- group: agent
  href: https://artifacts.apis.io/plannuh/llms/plannuh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/plannuh-llms.txt
- group: other
  href: https://artifacts.apis.io/plannuh/hosts/plannuh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/plannuh-hosts.yml
- group: other
  href: https://artifacts.apis.io/plannuh/vendors/plannuh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/plannuh-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planful.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planful.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://planful.com/newsroom/
- group: company
  title: ''
  type: Blog
  url: https://planful.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.planful.com/
- group: auth
  href: https://artifacts.apis.io/plannuh/security/plannuh-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/plannuh-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/plannuh/security/plannuh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/plannuh-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://planful.com/
coverage:
  checked: '2026-10-29'
  detail: Docs at https://developers.planful.com return a JavaScript rendered page that blocks automated fetching.
  evidence:
  - status: 200
    url: https://developers.planful.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Plannuh provides cloud‑based budgeting, planning, and performance management software for enterprises. The platform helps finance teams align strategic goals with operational execution, offering tools for budgeting, forecasting, reporting, and analytics. Plannuh aims to simplify complex financial processes, improve collaboration across departments, and deliver real‑time insights to drive better business decisions.
image: https://planfulprod.planful.com/wp-content/uploads/2026/07/og-home-1.png
layout: provider
modified: '2026-10-29'
name: Plannuh
nav: Providers
network: true
overview: 'Plannuh is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Finance, Planning, Budgeting, and Software-as-a-Service.


  Plannuh''s developer surface includes changelog, engineering blog, documentation, and 10 more developer resources.'
plans:
- name: Plannuh Plans Pricing
  plan_count: 0
  slug: plannuh-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Plannuh Rate Limits
  slug: plannuh-rate-limits
scopes:
- name: Plannuh Scopes
  scope_count: 0
  slug: plannuh-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 65.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 20.4
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Plannuh Authentication
  slug: plannuh-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Plannuh Domain Security
  slug: plannuh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plannuh Trust Center
  slug: plannuh-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: plannuh
tags:
- Company
- Finance
- Planning
- Budgeting
- Software-as-a-Service
website: https://planful.com/
---
