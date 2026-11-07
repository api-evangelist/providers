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
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/bidon-kr/llms/bidon-kr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bidon-kr-llms.txt
- group: other
  href: https://artifacts.apis.io/bidon-kr/hosts/bidon-kr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bidon-kr-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://bidon.kr/login
- group: auth
  href: https://artifacts.apis.io/bidon-kr/security/bidon-kr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bidon-kr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bidon.kr/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bidon.kr/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bidon.kr/privacy
coverage:
  checked: '2026-11-02'
  detail: MCP endpoint requires POST and is not callable via GET, blocking contract discovery.
  evidence:
  - status: 405
    url: https://bidon.kr/api/mcp
  reason: auth-required
  state: gated
created: '2026-11-02'
description: 비드온 BIDON은 부품·자재 구매·영업 AI 에이전트 서비스로, 품번 하나로 재고·판매처·견적을 제공하고, 품절 시 대체품까지 찾아줍니다. 모든 기능은 무료이며, 구매자와 판매자를 연결해 효율적인 거래를 지원합니다.
image: https://bidon.kr/images/og-bidon.png
layout: provider
modified: '2026-11-02'
name: 비드온 BIDON
nav: Providers
network: true
overview: 비드온 BIDON is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Procurement, Marketplace, and Free.
random_paper: 22
score:
  band: minimal
  composite: 6.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 39.3
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bidon Kr Domain Security
  slug: bidon-kr-domain-security
  summary_line: TLSv1.3
slug: bidon-kr
tags:
- Company
- Artificial Intelligence
- Procurement
- Marketplace
- Free
website: https://bidon.kr/
---
