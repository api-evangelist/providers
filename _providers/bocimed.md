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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bocimed-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.bocimed.com/
- group: company
  title: ''
  type: WebsiteEnglish
  url: http://en.bocimed.com/
- group: company
  title: ''
  type: About
  url: http://en.bocimed.com/index.php/List/2.html
- group: other
  title: ''
  type: Services
  url: http://en.bocimed.com/index.php/List/3.html
- group: company
  title: ''
  type: Blog
  url: http://en.bocimed.com/index.php/List/5.html
- group: operate
  title: ''
  type: Support
  url: http://en.bocimed.com/index.php/List/6.html
- group: company
  title: ''
  type: Careers
  url: http://en.bocimed.com/index.php/List/29.html
coverage:
  checked: '2026-08-08'
  detail: BociMed is a Shanghai pharmaceutical CRO/CDMO selling lab, drug-delivery, clinical and manufacturing services; its only web presence is a ThinkPHP marketing site in Chinese and English with no developer, API or documentation section, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt, /.well-known/*) returns a hard 404 on both hosts.
  evidence:
  - status: 200
    url: http://www.bocimed.com/
  - status: 200
    url: http://en.bocimed.com/
  - status: 404
    url: http://www.bocimed.com/openapi.json
  - status: 404
    url: http://en.bocimed.com/openapi.json
  - status: 404
    url: http://en.bocimed.com/.well-known/agent-card.json
  - status: 404
    url: http://en.bocimed.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/bocimed
  reason: not-a-software-company
  state: none
created: '2026-08-08'
description: 'Shanghai BociMed Pharmaceutical Research Co., Ltd. (上海博志研新药物研究有限公司) is a Chinese pharmaceutical CRO/CDMO founded in 2012 in the Zhangjiang Pharmaceutical Valley, Shanghai, with an R&D headquarters in Zhangjiang, a production base in Lingang, and a clinical subsidiary in Chengdu. BociMed offers small-molecule chemistry, CMC and process development, a portfolio of drug delivery technology platforms (oral, injectable, nasal, pulmonary, transdermal, ocular, implant, liposome and exosome), clinical research and SMO services, global regulatory registration consulting, and commercial API, intermediate and solid-dosage manufacturing. It is a laboratory and manufacturing services business rather than a software vendor: it publishes a marketing website in Chinese and English and no developer program, public API, SDK or machine-readable specification of any kind.'
layout: provider
modified: '2026-08-08'
name: BociMed
nav: Providers
network: true
overview: 'BociMed is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Life Sciences, Contract Research Organization, and CDMO.


  BociMed''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 4.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 90.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 46.3
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 4.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Bocimed Domain Security
  slug: bocimed-domain-security
  summary_line: no transport/DNS hardening detected
slug: bocimed
tags:
- Company
- Pharmaceuticals
- Life Sciences
- Contract Research Organization
- CDMO
- Drug Delivery
- Clinical Research
- Manufacturing
- China
- Shanghai
website: http://www.bocimed.com/
---
