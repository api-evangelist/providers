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
  href: https://artifacts.apis.io/book345-com/hosts/book345-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/book345-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/book345-com/vendors/book345-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/book345-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.book345.com/privacy
- group: auth
  href: https://artifacts.apis.io/book345-com/security/book345-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/book345-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://book345.com/
coverage:
  checked: '2026-11-02'
  detail: The provider's site returns a JavaScript shell with no machine-readable documentation.
  evidence:
  - status: 200
    url: https://www.book345.com/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: 无名图书是一家提供图书推荐、书评、内容解析与电子书下载的服务平台，致力于帮助用户发现高质量的学术、社科、职场成长类书籍。平台通过智能推荐和详细的阅读指南，提升阅读体验，覆盖人文社科、专业技术以及自我成长等多个领域。
image: https://www.book345.com/web_images/logo.png
layout: provider
modified: '2026-11-02'
name: 无名图书
nav: Providers
network: true
overview: 无名图书 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Book, Recommendations, Reading, Chinese, and Platform.
random_paper: 11
score:
  band: minimal
  composite: 3.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Book345 Com Domain Security
  slug: book345-com-domain-security
  summary_line: TLSv1.3
slug: book345-com
tags:
- Book
- Recommendations
- Reading
- Chinese
- Platform
website: https://book345.com/
---
