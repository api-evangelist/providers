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
  href: https://artifacts.apis.io/wealthcounsel/hosts/wealthcounsel-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wealthcounsel-hosts.yml
- group: other
  href: https://artifacts.apis.io/wealthcounsel/vendors/wealthcounsel-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wealthcounsel-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wealthcounsel.com/
- group: auth
  href: https://artifacts.apis.io/wealthcounsel/security/wealthcounsel-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wealthcounsel-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wealthcounsel.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wealthcounsel.com/
- group: company
  title: ''
  type: Blog
  url: https://info.wealthcounsel.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.wealthcounsel.com/customer-support-training
coverage:
  checked: '2026-10-28'
  detail: Developer portal at https://developer.wealthcounsel.com/ returns a JavaScript shell preventing machine-readable access.
  evidence:
  - status: 200
    url: https://developer.wealthcounsel.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: WealthCounsel provides estate planning software for attorneys, offering a suite of document automation tools such as Wealth Docx, Elder Docx, Business Docx, Wealth Tracx, and Gun Docx. The platform supports membership tiers, integrates with practice management systems, and delivers resources for legal professionals to streamline estate planning and wealth management processes.
image: https://cdn.craft.cloud/01a082b3-e21e-734d-af35-5f6a7fa8537d/assets/logo/WC-Flag-Logo-FullColor_2021-11-03-230907_dmfh.svg
layout: provider
modified: '2026-10-28'
name: WealthCounsel
nav: Providers
network: true
overview: 'WealthCounsel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Legal Tech, Estate Planning, Document Automation, and Software.


  WealthCounsel''s developer surface includes documentation, engineering blog, support, and 5 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 6.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.7
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 7.9
  previous_composite: 8.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/wealthcounsel/wealthcounsel-2026-11-03T150020.png
security:
- kind: domain-security
  name: Wealthcounsel Domain Security
  slug: wealthcounsel-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wealthcounsel
tags:
- Company
- Legal Tech
- Estate Planning
- Document Automation
- Software
website: https://wealthcounsel.com/
---
