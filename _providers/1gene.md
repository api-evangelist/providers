---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1gene-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 1GENE sells non-invasive cancer early-screening lab tests to consumers and clinics and publishes no developer program in either Chinese- or English-language sources; its own www.1gene.com.cn now answers HTTP 200 with an unconfigured Nginx Proxy Manager "Default Site" placeholder and every /.well-known/ and spec path on it returns a real 404, with no api./open./developer./docs. subdomain resolving and no GitHub organization or published package anywhere.
  evidence:
  - status: 200
    url: http://www.1gene.com.cn/
  - status: 404
    url: http://www.1gene.com.cn/openapi.json
  - status: 404
    url: http://www.1gene.com.cn/.well-known/agent-card.json
  - status: 404
    url: http://www.1gene.com.cn/llms.txt
  - status: 404
    url: https://api.github.com/orgs/1gene
  - status: 404
    url: https://pypi.org/pypi/1gene/json
  reason: no-developer-program
  state: none
created: '2026-09-05'
description: '1GENE (壹基因) is the brand of Hangzhou He-Yi Gene Technology Co., Ltd., a Chinese molecular-diagnostics company founded in Hangzhou''s Binjiang district in May 2014 by chairman and chief executive Junyi Wang. It develops non-invasive early cancer screening tests built on proprietary tumour DNA methylation markers and liquid- and stool-based biopsy chemistry, sold under the mission of "letting everyone stay away from cancer earlier". Its product pipeline covers colorectal cancer screening (常壹宁), gastric pathogen screening and medication guidance (优壹宁), gastric cancer screening (卫壹宁), and liver and oesophageal cancer screening in development; company scientists co-authored a validated stool-DNA biomarker panel for colorectal neoplasms in the Journal of Cancer Research and Clinical Oncology. The company raised an angel round in 2014, a RMB 49.5M Series A in 2015 and a Series B of several tens of millions of RMB from listed pharmaceutical maker Chengda Pharmaceuticals in December
  2022, and its shares are listed for secondary-market trading on EquityZen. 1GENE sells a clinical test, not software: it publishes no developer program, no public API, no SDK and no machine-readable specification, and as of this profile its own web origin at www.1gene.com.cn is unconfigured and serves a placeholder page.'
layout: provider
modified: '2026-09-05'
name: 1GENE
nav: Providers
network: true
overview: 1GENE is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Biotechnology, and Genomics.
random_paper: 2
security:
- kind: domain-security
  name: 1Gene Domain Security
  slug: 1gene-domain-security
  summary_line: no transport/DNS hardening detected
slug: 1gene
tags:
- Company
- Health
- Healthcare
- Biotechnology
- Genomics
- Diagnostics
- Cancer Screening
- Precision Medicine
- Life Sciences
- China
---
