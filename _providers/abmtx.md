---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/abmtx-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/abmtx-llms.txt
- group: company
  title: ''
  type: Website
  url: http://www.abmtx.com/
- group: company
  title: ''
  type: About
  url: http://www.abmtx.com/site/company
- group: operate
  title: ''
  type: Contact
  url: http://www.abmtx.com/site/contactus
- group: company
  title: ''
  type: Newsroom
  url: http://www.abmtx.com/site/newscenter
- group: company
  title: ''
  type: InvestorRelations
  url: http://www.abmtx.com/site/Investors
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/abm-therapeutics
- group: other
  title: ''
  type: x-secondary-market-listing
  url: https://www.hiive.com/securities/abmtx-stock
coverage:
  checked: '2026-09-06'
  detail: ABM Therapeutics is a clinical-stage biopharmaceutical company developing small-molecule brain-cancer drugs (lead program ABM-1310); its entire public surface is a PHP-CMS corporate and investor brochure at http://www.abmtx.com/ that serves no developer section, and no api./developer./developers./docs. subdomain for abmtx.com resolves at all.
  evidence:
  - status: 200
    url: http://www.abmtx.com/
  - status: 404
    url: http://www.abmtx.com/openapi.json
  - status: 404
    url: http://www.abmtx.com/llms.txt
  - status: 404
    url: http://www.abmtx.com/.well-known/api-catalog
  - status: 404
    url: http://abmtx.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-09-06'
description: ABM Therapeutics (ABM) is a clinical-stage biopharmaceutical company founded in 2015, operating from San Diego, California and Zhangjiang, Pudong, Shanghai. It discovers and develops small-molecule targeted therapies for primary brain cancers including glioblastoma multiforme (GBM) and for brain metastases arising from melanoma, lung cancer and breast cancer. Its lead program, ABM-1310, is a brain-penetrant, selective BRAF V600 inhibitor that received US IND clearance in November 2019 and is in Phase 1 clinical study. ABM publishes no developer program, public API, SDK or machine-readable specification; its only public surface is a corporate, investor and clinical-news website. The company was surfaced through the API Evangelist harvest backlog from a secondary-market listing under the ticker-style slug "abmtx".
image: http://www.abmtx.com/themes/basic/skin/images/icon_logo.jpg
layout: provider
modified: '2026-09-06'
name: ABM Therapeutics
nav: Providers
network: true
overview: ABM Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Oncology.
random_paper: 15
security:
- kind: domain-security
  name: Abmtx Domain Security
  slug: abmtx-domain-security
  summary_line: no transport/DNS hardening detected
slug: abmtx
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Oncology
- Drug Discovery
- Clinical Trials
- Healthcare
website: http://www.abmtx.com/
---
