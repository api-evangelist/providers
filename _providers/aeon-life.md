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
  scored_at: '2026-09-10'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aeon-life-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aeon-life-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.aeonlife.com.cn/
- group: company
  title: ''
  type: About
  url: https://www.aeonlife.com.cn/about/companyprofile/index.shtml
- group: operate
  title: ''
  type: Support
  url: https://www.aeonlife.com.cn/customer/index.shtml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aeonlife.com.cn/footer/law/index.shtml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aeonlife.com.cn/footer/privacy/index.shtml
- group: start
  title: ''
  type: SignUp
  url: https://www.aeonlife.com.cn/einsurance/front/page/register.html
- group: start
  title: ''
  type: Login
  url: https://www.aeonlife.com.cn/einsurance/front/page/login.html
- group: company
  title: ''
  type: Newsroom
  url: https://www.aeonlife.com.cn/news/index.shtml
- group: company
  title: ''
  type: Careers
  url: https://www.aeonlife.com.cn/join/index.shtml
- group: auth
  title: ''
  type: X-InformationDisclosure
  url: https://www.aeonlife.com.cn/info/index.shtml
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/aeon-life-stock
coverage:
  checked: '2026-09-10'
  detail: Aeon Life Insurance Company, Ltd. (百年人寿) is a Chinese retail life insurer whose only public surface is a Chinese-language corporate site and insurance mall; api., open. and developer.aeonlife.com.cn have no DNS record at all, and the one machine-readable host it does run — the group flexible-benefits gateway o2o.aeonlife.com.cn — answers every path, documented or not, with the same JSON envelope {"resultCode":"-3","resultMsg":"…认证失败"} and publishes no reference of any kind.
  evidence:
  - status: 404
    url: https://www.aeonlife.com.cn/openapi.json
  - status: 404
    url: https://www.aeonlife.com.cn/.well-known/agent-card.json
  - status: 404
    url: https://www.aeonlife.com.cn/llms.txt
  - status: 404
    url: https://o2o.aeonlife.com.cn/v3/api-docs
  - status: 200
    url: https://o2o.aeonlife.com.cn/o2o/login
  reason: no-developer-program
  state: none
created: '2026-09-10'
description: Aeon Life Insurance Company, Ltd. (百年人寿保险股份有限公司, "AEON LIFE") is a Chinese life insurer headquartered in Dalian, Liaoning, established on 1 June 2009 with registered capital of RMB 7.9048 billion. Its licensed scope covers life, health and personal accident insurance and other personal-insurance lines, reinsurance of those lines, and regulated insurance-fund investment business, sold across twenty provinces and municipalities including Dalian, Liaoning, Beijing, Hubei, Hebei, Henan, Jiangsu, Shandong, Sichuan, Guangdong, Zhejiang and Chongqing. Its public web presence is a Chinese-language corporate site with an online insurance mall, claims and policy-service sections, and the information-disclosure pages Chinese insurance regulation requires. The company publishes no developer portal, no API documentation and no machine-readable API contract; its group flexible-benefits platform (o2o.aeonlife.com.cn) and e-insurance customer portal both sit behind logins.
image: https://www.aeonlife.com.cn/images/common/logo_aeon.png
layout: provider
modified: '2026-09-10'
name: Aeon Life
nav: Providers
network: true
overview: 'Aeon Life is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Life Insurance, Health Insurance, and Financial Services.


  Aeon Life''s developer surface includes support, signup flow, and 11 more developer resources.'
plans:
- name: Aeon Life Plans Pricing
  plan_count: 0
  slug: aeon-life-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Aeon Life Rate Limits
  slug: aeon-life-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 5
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
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aeon Life Domain Security
  slug: aeon-life-domain-security
  summary_line: TLSv1.2
slug: aeon-life
tags:
- Company
- Insurance
- Life Insurance
- Health Insurance
- Financial Services
- China
- Consumer
website: https://www.aeonlife.com.cn/
---
