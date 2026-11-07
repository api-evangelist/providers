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
  score: 3.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API reference listed but no machine-readable contract found.
  name: Beaubi API
  slug: beaubi-api
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/beaubitw-com/llms/beaubitw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/beaubitw-com-llms.txt
- group: other
  href: https://artifacts.apis.io/beaubitw-com/hosts/beaubitw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/beaubitw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/beaubitw-com/vendors/beaubitw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/beaubitw-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/beaubitw-com/security/beaubitw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/beaubitw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://beaubitw.com/
- group: company
  title: ''
  type: Blog
  url: https://beaubitw.com/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://beaubitw.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://beaubitw.com/terms
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract found despite API reference page.
  evidence:
  - status: 404
    url: https://beaubitw.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Beaubi 行動美研提供美容師到府服務，涵蓋台北、新北、宜蘭、台中等地區，服務項目包括美甲、美睫、紋繡、採耳、肌膚管理與推拿。平台透過 GPS 全程追蹤、證照人工審核與雙向評價，確保服務品質與安全。使用者可於網站或行動應用預約，並可查看美容師專業證照與評價。公司亦設有自有培訓學院，提供美容師專業培訓課程，並提供會員制度與優惠方案。
image: https://beaubitw.com/brand/og-default.jpg
layout: provider
modified: '2026-11-02'
name: Beaubi 行動美研
nav: Providers
network: true
overview: 'Beaubi 行動美研 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  Beaubi 行動美研''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 15
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 39.3
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Beaubitw Com Domain Security
  slug: beaubitw-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: beaubitw-com
tags:
- Company
website: https://beaubitw.com/
---
