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
api_count: 1
apis:
- description: Zelta provides health supplement and lab test services, with an API for managing assessments and results.
  name: Zelta API
  slug: zelta-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/zelta-in/llms/zelta-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zelta-in-llms.txt
- group: other
  href: https://artifacts.apis.io/zelta-in/hosts/zelta-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zelta-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/zelta-in/vendors/zelta-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zelta-in-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://zelta.in/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://zelta.in/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://zelta.in/login
- group: docs
  title: ''
  type: Documentation
  url: https://zelta.in/guides/
- group: auth
  href: https://artifacts.apis.io/zelta-in/security/zelta-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zelta-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zelta.in/
- group: company
  title: ''
  type: Blog
  url: https://zelta.in/blog
- group: operate
  title: ''
  type: Support
  url: https://zelta.in/faq
coverage:
  detail: The provider's main site renders a JavaScript shell and no machine‑readable spec was found despite probing.
  evidence:
  - status: 200
    url: https://zelta.in/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Zelta-in is a technology company specializing in data analytics and advertising solutions. It provides a suite of APIs for managing campaigns, retrieving analytics, and integrating with third‑party platforms. The company focuses on privacy‑first data handling and offers detailed documentation for developers to build custom integrations and automate marketing workflows.
layout: provider
modified: '2026-10-29'
name: zelta-in
nav: Providers
network: true
overview: 'zelta-in is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Analytics, Advertising, Privacy, and Marketing.


  zelta-in''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 11
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 60.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zelta-in/zelta-in-2026-11-03T150438.png
security:
- kind: domain-security
  name: Zelta In Domain Security
  slug: zelta-in-domain-security
  summary_line: TLSv1.3 · DMARC
slug: zelta-in
tags:
- Company
- Data Analytics
- Advertising
- Privacy
- Marketing
website: https://zelta.in/
---
