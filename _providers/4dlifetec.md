---
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://4dlifetec.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://4dlifetec.com/general-terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://4dlifetec.com/privacy-policy/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/4d-lifetec-ag
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4dlifetec-domain-security.yml
coverage:
  checked: '2026-09-05'
  detail: 4D Lifetec AG sells a CE-marked in-vitro diagnostic blood test and the instrument that runs it — its only software, 4D LifeAI, is the image-scoring application embedded in the 4D Lifechamber device — and its entire web presence is an eight-page SilverStripe marketing and investor-relations site whose own sitemap.xml lists no developer, documentation or API page, with /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and all nine probed /.well-known/ paths returning the site's 404 on both 4dlifetec.com and www, no api/docs/developer/portal/app subdomain resolving in DNS, and no GitHub organization under the name.
  evidence:
  - status: 200
    url: https://4dlifetec.com/
  - status: 200
    url: https://4dlifetec.com/sitemap.xml
  - status: 404
    url: https://4dlifetec.com/openapi.json
  - status: 404
    url: https://4dlifetec.com/graphql
  - status: 404
    url: https://4dlifetec.com/llms.txt
  - status: 404
    url: https://4dlifetec.com/.well-known/agent-card.json
  - status: 404
    url: https://www.4dlifetec.com/.well-known/agent.json
  - status: 404
    url: https://api.github.com/orgs/4dlifetec
  reason: not-a-software-company
  state: none
created: '2026-09-05'
description: 4D Lifetec AG is a Swiss in-vitro diagnostics company headquartered at Gewerbestrasse 8, 6330 Cham, Switzerland, developing the 4D Lifetest — a non-invasive, immuno-oncological blood test for the early detection of cancer. The test reads a proprietary DNA Damage Sensitivity (DDS) biomarker from a liquid biopsy using single-cell gel electrophoresis (the comet assay), run on the company's own 4D Lifechamber instrument for a fully automated and standardized procedure and scored by 4D LifeAI, its trained image analysis software. The flagship product is 4D Lifetest Lung Dx, with 4D Lifetest Breast Dx, Prostate Dx and Colon Dx as further assays in the same platform, and the company holds patent protection across the US, Europe, China and other territories. 4D Lifetec is a diagnostics manufacturer and laboratory-services company, not a software vendor. Its public web presence is an eight-page SilverStripe marketing and investor-relations site with no developer portal, no API reference,
  no SDKs, no public GitHub organization and no machine-readable specification of any kind; probing every documented contract location on 4dlifetec.com — /openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and the full /.well-known/ path list — returned the site's SilverStripe 404 page in every case, and no api, docs, developer, portal or app subdomain resolves in DNS. The only software the company describes, 4D LifeAI, is embedded in the instrument rather than exposed as a service.
image: https://4dlifetec.com/themes/base/images/4D_Lifetec_Logo.svg
layout: provider
modified: '2026-09-05'
name: 4D Lifetec
nav: Providers
network: true
overview: 4D Lifetec is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Diagnostics, Oncology, and Life Sciences.
random_paper: 2
security:
- kind: domain-security
  name: 4Dlifetec Domain Security
  slug: 4dlifetec-domain-security
  summary_line: TLSv1.3
slug: 4dlifetec
tags:
- Company
- Healthcare
- Diagnostics
- Oncology
- Life Sciences
- Biotechnology
- Laboratory
- Medical Devices
- Switzerland
website: https://4dlifetec.com/
---
