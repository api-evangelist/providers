---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.yuanfudao.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/yuanfudao_stock/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kanyun-inc
- group: auth
  title: ''
  type: Security
  url: https://security.kanyun.com/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/yuanfudao-vulnerability-disclosure.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://m.yuanfudao.com/native/help/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://m.yuanfudao.com/native/help/service-agreement
- group: operate
  title: ''
  type: Support
  url: https://www.yuanfudao.com/u/feedback
- group: start
  title: ''
  type: Login
  url: https://www.yuanfudao.com/u/
- group: build
  title: ''
  type: Packages
  url: packages/yuanfudao-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/yuanfudao-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/yuanfudao-domain-security.yml
coverage:
  checked: '2026-09-04'
  detail: 'Yuanfudao ships only consumer learning apps: www.yuanfudao.com returns a marketing site with no developer link, its robots.txt disallows /api/ and /sdk/, the kanyun-inc GitHub org holds 19 repos of general-purpose OSS and internal AI tooling but zero API clients, and all seven /.well-known/ paths 404 on all six Yuanfudao and Kanyun hosts probed.'
  evidence:
  - status: 200
    url: https://www.yuanfudao.com/
  - status: 404
    url: https://www.yuanfudao.com/openapi.json
  - status: 404
    url: https://ape-api.yuanfudao.com/openapi.json
  - status: 404
    url: https://www.yuanfudao.com/.well-known/api-catalog
  - status: 404
    url: https://www.kanyun.com/llms.txt
  - status: 200
    url: https://security.kanyun.com/
  reason: no-developer-program
  state: none
created: '2026-09-04'
description: Yuanfudao (猿辅导) is a Beijing-based online education technology company founded in 2012 and operated under Kanyun Holdings (看云控股集团). Its consumer products include the Yuanfudao tutoring platform, Zebra AI Learning (斑马AI学), Xiaoyuan AI / Xiaoyuan Kousuan (小猿AI / 小猿口算), Xiaoyuan Souti (小猿搜题), Ape Programming (猿编程) and Haitun Zixi (海豚自习), delivering live classes, smart practice and problem-solving analysis to K-12 and preschool learners in China. The company publishes no public developer program, API reference or machine-readable API contract; its visible public engineering surface is the kanyun-inc GitHub organization of open-source libraries and developer tooling, and the Kanyun Security Response Center (YSRC) vulnerability disclosure program at security.kanyun.com.
image: https://yfdpc.fbcontent.cn/s/logo-563d697805.svg
layout: provider
modified: '2026-09-04'
name: Yuanfudao
nav: Providers
network: true
overview: 'Yuanfudao is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, EdTech, Online Learning, and Tutoring.


  Yuanfudao''s developer surface includes support and 11 more developer resources.'
plans:
- name: Yuanfudao Plans Pricing
  plan_count: 0
  slug: yuanfudao-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Yuanfudao Rate Limits
  slug: yuanfudao-rate-limits
score:
  band: emerging
  composite: 16.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 37.0
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: domain-security
  name: Yuanfudao Domain Security
  slug: yuanfudao-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Yuanfudao Vulnerability Disclosure
  slug: yuanfudao-vulnerability-disclosure
  summary_line: contact published
slug: yuanfudao
tags:
- Company
- Education
- EdTech
- Online Learning
- Tutoring
- Artificial Intelligence
- Mobile Applications
- China
website: https://www.yuanfudao.com/
---
