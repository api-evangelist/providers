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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: http://www.51haohuo.com/
- group: commercial
  title: ''
  type: Pricing
  url: http://www.51haohuo.com/#pricing
- group: operate
  title: ''
  type: Support
  url: http://www.51haohuo.com/#contact
- group: commercial
  title: ''
  type: Plans
  url: plans/51haohuo-com-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/51haohuo-com-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/51haohuo-com-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/51haohuo-com-llms.txt
coverage:
  checked: '2026-09-05'
  detail: 好活（苏州）数字科技有限公司 ships enterprise SaaS but its entire public web surface is one static Tailwind marketing page on nginx that 404s /docs, /api, /developer, /openapi.json and every /.well-known/ path — the only integration path it offers a partner is the 申请演示 (request-a-demo) contact form.
  evidence:
  - status: 200
    url: http://www.51haohuo.com/
  - status: 404
    url: http://www.51haohuo.com/developer
  - status: 404
    url: http://www.51haohuo.com/openapi.json
  - status: 404
    url: http://www.51haohuo.com/.well-known/api-catalog
  - status: 301
    url: http://51haohuo.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '51haohuo.com is the corporate site of 好活（苏州）数字科技有限公司 (Haohuo (Suzhou) Digital Technology Co., Ltd.), a Suzhou, Jiangsu based Chinese software vendor trading under the 苏爱才 ("Su Ai Cai") brand as a 人才服务供应商 — a talent-services supplier. It markets six enterprise SaaS lines to Chinese employers: a 零工平台 (gig-work platform), a 产业园平台 (industrial-park platform), 鹦鹉课堂 (a courseware/training product), a 智能体平台 (AI agent platform), a 做课平台 (course-authoring platform), and custom AIBPO engagements, sold on three published monthly tiers. As of the 2026-09-05 probe the company runs a single-page marketing site with a request-a-demo contact form and publishes no developer program, API reference, or machine-readable specification of any kind.'
layout: provider
modified: '2026-09-05'
name: 51haohuo.com
nav: Providers
network: true
overview: '51haohuo.com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, China, Human Resources, Staffing, and Gig Economy.


  51haohuo.com''s developer surface includes pricing, support, and 5 more developer resources.'
plans:
- name: 51Haohuo Com Plans Pricing
  plan_count: 4
  slug: 51haohuo-com-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: 51Haohuo Com Rate Limits
  slug: 51haohuo-com-rate-limits
score:
  band: emerging
  composite: 12.5
  coverage:
    artifact_dirs: 5
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 51Haohuo Com Domain Security
  slug: 51haohuo-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: 51haohuo-com
tags:
- Company
- China
- Human Resources
- Staffing
- Gig Economy
- Workforce Management
- Talent Services
- Enterprise Software
- SaaS
website: http://www.51haohuo.com/
---
