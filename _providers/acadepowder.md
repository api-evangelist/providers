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
  scored_at: '2026-09-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/acadepowder-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://www.acadepowder.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://equityzen.com/company/acadepowder
coverage:
  checked: '2026-09-06'
  detail: 'Acade Powder makes metal powders, not software: www.acadepowder.com is a nine-page ASP.NET corporate brochure site in Chinese with product, news and contact pages only, its apex domain and every api./shop./oa. subdomain are NXDOMAIN, and /openapi.json, /swagger.json, /api-docs, /graphql, /developers and all seven /.well-known/ paths return the site''s 404 handler.'
  evidence:
  - status: 200
    url: http://www.acadepowder.com/
  - status: 404
    url: http://www.acadepowder.com/openapi.json
  - status: 404
    url: http://www.acadepowder.com/api-docs
  - status: 404
    url: http://www.acadepowder.com/graphql
  - status: 404
    url: http://www.acadepowder.com/developers
  - status: 404
    url: http://www.acadepowder.com/.well-known/api-catalog
  - status: 404
    url: http://www.acadepowder.com/.well-known/agent-card.json
  - status: 404
    url: http://www.acadepowder.com/llms.txt
  - status: 200
    url: https://api.github.com/search/repositories?q=acadepowder
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: Acade Powder is the English trading name of Suzhou Luxin New Material Technology Co., Ltd. (苏州鲁信新材料科技有限公司), a Chinese advanced-materials manufacturer founded in 2013 and headquartered at No. 512 Fangqiao Road, Xiangcheng District, Suzhou, Jiangsu, with metal-powder production bases in Henan, Anhui and Jiangsu. It develops, produces and sells metal powders for additive manufacturing (3D printing), powder metallurgy, metal injection moulding and laser cladding — superalloy, titanium, aluminium, copper, cobalt-chrome, mould steel, high-speed steel and soft-magnetic grades, plus custom powders — for aerospace, new energy, electronics, photovoltaic, shipbuilding and medical/dental customers. A private pre-IPO company traded on the EquityZen secondary marketplace, it is a materials manufacturer rather than a software vendor and publishes no developer program, API documentation, SDK or machine-readable API contract.
image: http://www.acadepowder.com/luxinui/img/A1.png
layout: provider
modified: '2026-09-06'
name: Acade Powder
nav: Providers
network: true
overview: Acade Powder is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Materials, Advanced Materials, Metal Powder, and Additive Manufacturing.
random_paper: 17
score:
  band: minimal
  composite: 5.0
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  schema_version: 0.19.0
  scored_at: '2026-09-06'
security:
- kind: domain-security
  name: Acadepowder Domain Security
  slug: acadepowder-domain-security
  summary_line: DMARC
slug: acadepowder
tags:
- Company
- Materials
- Advanced Materials
- Metal Powder
- Additive Manufacturing
- 3D Printing
- Powder Metallurgy
- Manufacturing
- Aerospace
- China
website: http://www.acadepowder.com/
---
