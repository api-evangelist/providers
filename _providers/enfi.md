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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Enfi provides lending software platform; API details are not publicly documented.
  name: Enfi API
  slug: enfi-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/enfi/well-known/enfi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/enfi-well-known.yml
- group: other
  href: https://artifacts.apis.io/enfi/hosts/enfi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/enfi-hosts.yml
- group: other
  href: https://artifacts.apis.io/enfi/vendors/enfi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/enfi-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.enfi.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.enfi.ai/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.enfi.ai/news
- group: company
  title: ''
  type: Blog
  url: https://www.enfi.ai/blog/the-best-lending-software-of-2026
- group: docs
  title: ''
  type: Documentation
  url: https://help.enfi.ai/
- group: auth
  href: https://artifacts.apis.io/enfi/security/enfi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/enfi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.enfi.ai/
coverage:
  checked: '2026-10-29'
  detail: Docs at https://help.enfi.ai/ render via JavaScript and provide no machine‑readable spec.
  evidence:
  - status: 200
    url: https://help.enfi.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: EnFi provides an AI‑powered credit platform for commercial lenders, including banks, credit unions, and fintech lenders. The platform automates document intake, verification, financial spreading, credit memo generation, covenant monitoring, and annual reviews to accelerate loan decisions and increase lending capacity.
image: https://cdn.prod.website-files.com/6862cd747f8c5b29da7a6e1c/6ab2cbddd204d0f786225e82_OG-home.jpg
layout: provider
modified: '2026-10-29'
name: Enfi
nav: Providers
network: true
overview: 'Enfi is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Automation, Data Integration, and Cloud.


  Enfi''s developer surface includes engineering blog, documentation, and 8 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.9
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 49.1
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 13.2
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/enfi/enfi-2026-11-03T131523.png
security:
- kind: domain-security
  name: Enfi Domain Security
  slug: enfi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: enfi
tags:
- Fintech
- Automation
- Data Integration
- Cloud
website: https://www.enfi.ai/
---
