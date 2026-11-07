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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/conduiit/hosts/conduiit-hosts.yml
  title: ''
  type: Hosts
  url: hosts/conduiit-hosts.yml
- group: other
  href: https://artifacts.apis.io/conduiit/vendors/conduiit-vendors.yml
  title: ''
  type: Vendors
  url: vendors/conduiit-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.conduiit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.conduiit.com/privacy
- group: auth
  href: https://artifacts.apis.io/conduiit/security/conduiit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/conduiit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.conduiit.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.conduiit.com/
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: no-developer-program
  state: none
created: '2026-10-10'
description: Conduiit provides modern finance infrastructure for film and TV productions, offering tools for tax credit incentives, expense management, and real‑time financial reporting. The platform streamlines approvals, payments, and documentation, enabling production teams to maintain control, compliance, and efficiency throughout the lifecycle of a project.
image: https://conduiit-website.vercel.app/api/media/file/conduiit%20logo.png
layout: provider
modified: '2026-10-10'
name: Conduiit
nav: Providers
network: true
overview: Conduiit is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Film Production, TVProduction, TaxIncentives, and Expense Management.
random_paper: 23
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 8.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/conduiit/conduiit-2026-11-03T125216.png
security:
- kind: domain-security
  name: Conduiit Domain Security
  slug: conduiit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: conduiit
tags:
- Finance
- Film Production
- TVProduction
- TaxIncentives
- Expense Management
website: https://www.conduiit.com/
---
