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
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aante-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ant-fa.com/
- group: company
  title: ''
  type: Blog
  url: https://ant-fa.com/notice/news/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ant-fa.com/notice/notice-detail/44/?id=44
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ant-fa.com/notice/notice-detail/254/?id=254
- group: start
  title: ''
  type: SignUp
  url: https://ant-fa.com/login
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/aante-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/aante-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/aante-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: Aante sells factory-automation components through a Chinese-language Nuxt storefront at ant-fa.com and ships no developer surface at all — /openapi.json, /swagger.json and /llms.txt return 404, /graphql, /api-docs, /docs and every /.well-known/ path return the site's 31KB single-page-application HTML shell with HTTP 200, and api./open./developer./ docs./gateway.ant-fa.com are all NXDOMAIN.
  evidence:
  - status: 404
    url: https://ant-fa.com/openapi.json
  - status: 404
    url: https://ant-fa.com/llms.txt
  - status: 404
    url: https://ant-fa.com/.well-known/agent-card.json
  - status: 404
    url: https://ant-fa.com/.well-known/security.txt
  - status: 200
    url: https://ant-fa.com/graphql
  - status: 200
    url: https://ant-fa.com/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: Aante (爱安特) is a Chinese factory-automation (FA) parts distributor and one-stop industrial e-commerce procurement platform, operated by Aante (Changzhou) Precision Machinery Co., Ltd. (爱安特（常州）精密机械有限公司) and headquartered in Changzhou, Jiangsu. Established in 2002 as the successor to Sandi Automation, it sells linear motion, transmission, standard, machined, framing, motion-unit, electrical and pneumatic components across 96 product categories and roughly two million SKUs, distributing 30+ international brands including SMC and THK alongside its own Aante-branded line. It serves customers in semiconductors, new energy, 3C electronics, photovoltaics, LCD, automotive, medical and food manufacturing from three production bases and 30+ service centers, and in 2026 acquired software firm Zhuiguang Geometry to pair components with design software. The storefront at ant-fa.com is a Chinese-language Nuxt commerce site; no public developer program, API reference, or machine-readable contract
  is published.
image: https://dioguwdgf472v.cloudfront.net/media/logos/equityinvest/Company/aante_logo-55305772a85f0ab3.png
layout: provider
modified: '2026-09-05'
name: Aante
nav: Providers
network: true
overview: 'Aante is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Industrial Automation, Factory Automation, Manufacturing, and Distribution.


  Aante''s developer surface includes engineering blog, signup flow, and 7 more developer resources.'
plans:
- name: Aante Plans Pricing
  plan_count: 0
  slug: aante-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Aante Rate Limits
  slug: aante-rate-limits
score:
  band: emerging
  composite: 12.3
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
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: Aante Domain Security
  slug: aante-domain-security
  summary_line: TLSv1.2 · DMARC
slug: aante
tags:
- Company
- Industrial Automation
- Factory Automation
- Manufacturing
- Distribution
- E-Commerce
- Procurement
- Industrial Components
- China
website: https://ant-fa.com/
---
