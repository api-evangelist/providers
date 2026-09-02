---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/xinhe-technology-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.xinhekeji.net/
- group: start
  title: ''
  type: Login
  url: https://cem.xinhekeji.net
- group: operate
  title: ''
  type: Support
  url: https://www.xinhekeji.net/ContactUs
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/xinhe-technology-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Xinhe Technology ships 心愿盒 Match Box only as an end-user product — a WeChat mini program for consumers and a brand CEM console at cem.xinhekeji.net — and the only HTTP API behind it is that console's own private Django REST Framework backend at https://cem.xinhekeji.net/api/, which answers anonymous callers with 401 "Authentication credentials were not provided." and serves no spec (/api/swagger.json, /api/openapi.json, /api/v3/api-docs all 404); there is no developer portal, no api./ developer./open./docs. subdomain, no SDK on npm or PyPI, and no GitHub organization.
  evidence:
  - status: 401
    url: https://cem.xinhekeji.net/api/cem/getBrand/
  - status: 404
    url: https://cem.xinhekeji.net/api/openapi.json
  - status: 404
    url: https://www.xinhekeji.net/llms.txt
  - status: 404
    url: https://api.github.com/orgs/xinhekeji
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Xinhe Technology (Shanghai Xinhe Box Technology Co., Ltd. / 上海心盒科技有限公司) operates 心愿盒 Match Box, a consumer experience co-creation platform. Brands distribute product samples to precisely targeted consumer segments matched on age, gender, occupation, and consumption-preference tags, collect structured questionnaire feedback and reviews for agile marketing iteration, and convert triallists into private-domain traffic on WeChat official accounts and mini programs. A DCM Ventures portfolio company; it publishes no public developer portal or API surface as of July 2026.
image: https://www.xinhekeji.net/logo192.png
layout: provider
modified: '2026-08-13'
name: Xinhe Technology
nav: Providers
network: true
overview: 'Xinhe Technology is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Enterprise, Consumer Insights, Product Sampling, and Customer Experience.


  Xinhe Technology''s developer surface includes support and 4 more developer resources.'
plans:
- name: Xinhe Technology Plans Pricing
  plan_count: 0
  slug: xinhe-technology-plans-pricing
random_paper: 10
score:
  band: minimal
  composite: 7.5
  coverage:
    artifact_dirs: 4
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Xinhe Technology Domain Security
  slug: xinhe-technology-domain-security
  summary_line: TLSv1.3 · DMARC
slug: xinhe-technology
tags:
- Company
- Enterprise
- Consumer Insights
- Product Sampling
- Customer Experience
- Marketing
- China
website: https://www.xinhekeji.net/
---
