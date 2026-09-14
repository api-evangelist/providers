---
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
