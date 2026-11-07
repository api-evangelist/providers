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
  score: 3.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/easyagency-co-kr/llms/easyagency-co-kr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyagency-co-kr-llms.txt
- group: agent
  href: https://artifacts.apis.io/easyagency-co-kr/mcp/easyagency-co-kr-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/easyagency-co-kr-mcp.yml
- group: other
  href: https://artifacts.apis.io/easyagency-co-kr/hosts/easyagency-co-kr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyagency-co-kr-hosts.yml
- group: other
  href: https://artifacts.apis.io/easyagency-co-kr/vendors/easyagency-co-kr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easyagency-co-kr-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easyagency.co.kr/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easyagency.co.kr/privacy
- group: auth
  href: https://artifacts.apis.io/easyagency-co-kr/security/easyagency-co-kr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyagency-co-kr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.easyagency.co.kr/
coverage:
  checked: '2026-11-06'
  detail: The provider's website returns only a JavaScript shell with no machine‑readable API documentation.
  evidence:
  - status: 200
    url: https://easyagency.co.kr/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-06'
description: 이지에이전시는 홈페이지·시스템 구축부터 브랜딩·마케팅, 운영까지 비즈니스에 필요한 모든 것을 제공하는 종합 솔루션 기업입니다. 고객의 디지털 전환을 지원하며 다양한 웹·앱 개발, 콘텐츠 제작, 마케팅, 브랜딩 서비스를 제공하고 있습니다. 또한 기업 맞춤형 프로젝트 관리와 컨설팅을 통해 효율적인 비즈니스 프로세스를 구현하고, 최신 트렌드와 기술을 활용한 혁신적인 디지털 경험을 제공합니다.
image: https://www.easyagency.co.kr/og.png
layout: provider
mcp_servers:
- description: Remote MCP server at builder.easyagency.co.kr.
  name: 이지에이전시 MCP Server
  slug: easyagency-co-kr-mcp-yml
modified: '2026-11-06'
name: 이지에이전시
nav: Providers
network: true
overview: 이지에이전시 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Web Development, Marketing, Branding, Content Creation, and South Korea.
random_paper: 2
score:
  band: minimal
  composite: 8.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Easyagency Co Kr Domain Security
  slug: easyagency-co-kr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easyagency-co-kr
tags:
- Web Development
- Marketing
- Branding
- Content Creation
- South Korea
website: https://www.easyagency.co.kr/
---
