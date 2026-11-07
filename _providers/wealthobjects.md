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
- group: agent
  href: https://artifacts.apis.io/wealthobjects/llms/wealthobjects-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/wealthobjects-llms.txt
- group: other
  href: https://artifacts.apis.io/wealthobjects/hosts/wealthobjects-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wealthobjects-hosts.yml
- group: other
  href: https://artifacts.apis.io/wealthobjects/vendors/wealthobjects-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wealthobjects-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wealthobjectsplatform.com/terms-of-use
- group: operate
  title: ''
  type: Support
  url: https://wealthobjectsplatform.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wealthobjectsplatform.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://wealthobjectsplatform.com/news
- group: company
  title: ''
  type: Blog
  url: https://wealthobjectsplatform.com/blog
- group: auth
  href: https://artifacts.apis.io/wealthobjects/security/wealthobjects-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/wealthobjects-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wealthobjectsplatform.com/
coverage:
  checked: '2026-10-21'
  detail: OpenAPI spec not found at https://api.wealthobjects.com/openapi.json (no response)
  evidence:
  - status: no-response
    url: https://api.wealthobjects.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: WealthObjects provides a platform for financial advisors and wealth managers to aggregate client data, generate reports, and automate compliance. The service integrates with major custodians, broker‑dealers, and data providers, offering APIs for account information, transaction history, portfolio analytics, and document management. WealthObjects aims to streamline wealth management workflows, improve data accuracy, and enhance client communication through secure, scalable cloud services. Founded in 2015, the company serves thousands of advisors across the United States, emphasizing regulatory compliance and data security.
layout: provider
modified: '2026-10-21'
name: WealthObjects
nav: Providers
network: true
overview: 'WealthObjects is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Wealth Management, API Platform, Data Aggregation, and Compliance.


  WealthObjects'' developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 23
score:
  band: minimal
  composite: 7.3
  coverage:
    artifact_dirs: 10
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 52.7
    operational_transparency: 0.0
  previous_composite: 10.8
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/wealthobjects/wealthobjects-2026-11-03T150018.png
security:
- kind: domain-security
  name: Wealthobjects Domain Security
  slug: wealthobjects-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wealthobjects
tags:
- Fintech
- Wealth Management
- API Platform
- Data Aggregation
- Compliance
website: https://wealthobjectsplatform.com/
---
