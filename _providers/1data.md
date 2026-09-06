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
  url: security/1data-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oneaix.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/1data
- group: company
  title: ''
  type: Blog
  url: https://www.oneaix.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OneAIX
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1data-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/1data-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/1data-conformance.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/1data-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1data-rate-limits.yml
coverage:
  checked: '2026-09-05'
  detail: ONEAIX sells AI "digital employees" as a login-gated tenant application at www.yxd.info and markets no API at all — its sitemap and its own llms.txt site index list only marketing, solution, case and news pages, /developers /docs /api /pricing all 404 on the marketing host, every /.well-known/ path 404s, and www.yxd.info answers every probe path with the same 1,430-byte SPA shell rather than a spec.
  evidence:
  - status: 200
    url: https://www.oneaix.com/
  - status: 200
    url: https://www.oneaix.com/llms.txt
  - status: 404
    url: https://www.oneaix.com/openapi.json
  - status: 404
    url: https://www.oneaix.com/developers
  - status: 404
    url: https://www.oneaix.com/.well-known/api-catalog
  - status: 200
    url: https://www.yxd.info/swagger.json
  - status: 301
    url: https://1data.info/
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: 'ONEAIX (壹沓科技（上海）有限公司, formerly branded 1data / Yida Technology) is a Shanghai-headquartered enterprise AI company founded in 2016 that builds "digital employees" for global supply chains. Its 小沓AI platform ships two product lines — Cuber for supply-chain logistics (AI sales, route, operations, documentation and customs specialists covering quoting, booking, bills of lading, manifests and customs declaration) and Linker for supply-chain brands (brand, PR, GEO, content, e-commerce and data-analysis specialists) — on three in-house layers: Dax LLM, a supply-chain vertical LLM; Dax OS, an enterprise agent runtime and governance platform; and Dax KE, an agent-native knowledge engine, all delivered from the login-gated www.yxd.info tenant platform. Customers include COSCO Shipping, Sinotrans, Qingdao Port, DSV, Xtep and Colgate. ONEAIX publishes no developer program, API reference or machine-readable contract; the only agent-facing artifact it serves is a first-party llms.txt.'
image: https://www.oneaix.com/favicon.ico
layout: provider
modified: '2026-09-05'
name: ONEAIX (1data / Yida Technology)
nav: Providers
network: true
overview: 'ONEAIX (1data / Yida Technology) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Large Language Models, and Supply Chain.


  ONEAIX (1data / Yida Technology)''s developer surface includes engineering blog and 9 more developer resources.'
plans:
- name: 1Data Plans Pricing
  plan_count: 0
  slug: 1data-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: 1Data Rate Limits
  slug: 1data-rate-limits
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 2.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: domain-security
  name: 1Data Domain Security
  slug: 1data-domain-security
  summary_line: TLSv1.2 · DMARC
slug: 1data
tags:
- Company
- Artificial Intelligence
- AI Agents
- Large Language Models
- Supply Chain
- Logistics
- Freight Forwarding
- Robotic Process Automation
- Digital Workers
- Enterprise Software
- E-Commerce
- China
website: https://www.oneaix.com/
---
