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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: CourtDrive provides an AI‑powered docketing assistant API (no public machine‑readable contract found).
  name: CourtDrive API
  slug: courtdrive-api
artifact_total: 3
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.courtdrive.com/guides/add-email-to-courts
- group: commercial
  href: https://artifacts.apis.io/courtdrive/plans/courtdrive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/courtdrive-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/courtdrive/hosts/courtdrive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/courtdrive-hosts.yml
- group: other
  href: https://artifacts.apis.io/courtdrive/vendors/courtdrive-vendors.yml
  title: ''
  type: Vendors
  url: vendors/courtdrive-vendors.yml
- group: auth
  href: https://artifacts.apis.io/courtdrive/security/courtdrive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/courtdrive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://courtdrive.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.courtdrive.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.courtdrive.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.courtdrive.com/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.courtdrive.com/signupv3
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other contract files were found on any discovered host.
  evidence:
  - status: 0
    url: https://api.courtdrive.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: CourtDrive provides an AI‑powered docketing assistant for law firms, automating federal and state court e‑notice handling, calendaring, and document management integration. The platform offers free docket access, AI‑driven deadline calculation, and seamless syncing with systems like iManage, NetDocuments, Clio, Google Drive, and more, helping legal teams save time and reduce errors.
image: https://cdn.prod.website-files.com/5d69be272927f6d8b04b8908/686fea45fcba74cda5113dee_tsk06-graph-preview.webp
layout: provider
modified: '2026-10-28'
name: CourtDrive
nav: Providers
network: true
overview: 'CourtDrive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Legal Tech, Artificial Intelligence, Docketing, Automation, and Document Management.


  CourtDrive''s developer surface includes documentation, pricing, signup flow, and 7 more developer resources.'
plans:
- name: Courtdrive Plans Pricing
  plan_count: 4
  slug: courtdrive-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 16.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.9
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 22.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/courtdrive/courtdrive-2026-11-03T125442.png
security:
- kind: domain-security
  name: Courtdrive Domain Security
  slug: courtdrive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: courtdrive
tags:
- Legal Tech
- Artificial Intelligence
- Docketing
- Automation
- Document Management
- Company
website: https://courtdrive.com/
---
