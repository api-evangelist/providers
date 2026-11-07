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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API providing long-term care institution evaluation data as described on the site.
  name: Caregrade API
  slug: caregrade-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/caregrade-kr/plans/caregrade-kr-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/caregrade-kr-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/caregrade-kr/llms/caregrade-kr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/caregrade-kr-llms.txt
- group: other
  href: https://artifacts.apis.io/caregrade-kr/hosts/caregrade-kr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/caregrade-kr-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://caregrade.kr/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://caregrade.kr/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://caregrade.kr/biz/pricing
- group: start
  title: ''
  type: Login
  url: https://app.caregrade.kr/login
- group: auth
  href: https://artifacts.apis.io/caregrade-kr/security/caregrade-kr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/caregrade-kr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://caregrade.kr/
- group: company
  title: ''
  type: Blog
  url: https://caregrade.kr/blog/
- group: company
  title: ''
  type: News
  url: https://caregrade.kr/news/
- group: operate
  title: ''
  type: FAQ
  url: https://caregrade.kr/faq/
coverage:
  checked: '2026-11-03'
  detail: The provider offers a public API reference page but no machine‑readable OpenAPI or other contract is published.
  evidence:
  - status: 404
    url: https://caregrade.kr/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: 케어그레이드(케어그레이드)는 국민건강보험공단이 공개한 장기요양기관 평가 데이터를 지역·급여종류별로 비교·제공하는 서비스입니다. 전국 21,213곳의 평가·인력·정원을 한눈에 확인할 수 있으며, 회원가입 없이 무료로 이용할 수 있습니다. 데이터는 공공기관이 제공한 최신 정보를 기반으로 합니다.
image: https://caregrade.kr/opengraph-image.jpg?opengraph-image.3wqck6ef8of5e.jpg
layout: provider
modified: '2026-11-03'
name: 케어그레이드
nav: Providers
network: true
overview: '케어그레이드 is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Data, South Korea, Long-Term Care, and Public.


  케어그레이드''s developer surface includes pricing, engineering blog, product news, FAQ, and 8 more developer resources.'
plans:
- name: Caregrade Kr Plans Pricing
  plan_count: 1
  slug: caregrade-kr-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 49.1
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - south-korea
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Caregrade Kr Domain Security
  slug: caregrade-kr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: caregrade-kr
tags:
- Healthcare
- Data
- South Korea
- Long-Term Care
- Public
website: https://caregrade.kr/
---
