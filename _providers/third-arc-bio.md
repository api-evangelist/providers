---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/third-arc-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thirdarcbio.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirdarcbio.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirdarcbio.com/terms-of-service/
- group: company
  title: ''
  type: Blog
  url: https://thirdarcbio.com/news/
- group: operate
  title: ''
  type: Support
  url: mailto:info@thirdarcbio.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/third-arc-bio/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/third-arc-bio-llms.txt
coverage:
  checked: '2026-08-30'
  detail: Third Arc Bio is a clinical-stage antibody therapeutics developer; thirdarcbio.com is a Gatsby static marketing site with only science, pipeline, team, news and policy pages, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /docs, /developers, /api, /graphql, /llms.txt) plus every /.well-known/ document returns the site's 404 body, while api., developer., docs. and mcp. subdomains do not resolve in DNS.
  evidence:
  - status: 200
    url: https://thirdarcbio.com/
  - status: 404
    url: https://thirdarcbio.com/openapi.json
  - status: 404
    url: https://thirdarcbio.com/developers
  - status: 404
    url: https://thirdarcbio.com/.well-known/agent-card.json
  - status: 404
    url: https://thirdarcbio.com/.well-known/api-catalog
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: Third Arc Bio is a clinical-stage biotechnology company headquartered in Lower Gwynedd, Pennsylvania, developing multifunctional antibodies that build immune synapses to precisely activate or inhibit T cells. Its ARCStim platform targets solid tumors and its ARCTag platform pursues tissue-specific precision immune regulation for immunology and inflammation (I&I) indications; lead program ARC101 is a bispecific T-cell engager in a Phase 1 trial in patients with CLDN6-expressing solid tumors. The company launched in 2022 with seed financing from Omega Funds, raised an oversubscribed $165M Series A, and closed a $52M Series A extension in February 2026 with Andreessen Horowitz joining the syndicate. Third Arc Bio publishes no public API, developer portal, SDK or machine-readable specification — it is a therapeutics developer, not a software vendor.
image: https://thirdarcbio.com/thirdarc-og-image.png
layout: provider
modified: '2026-08-30'
name: Third Arc Bio
nav: Providers
network: true
overview: 'Third Arc Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Antibodies, and Oncology.


  Third Arc Bio''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/third-arc-bio/refs/heads/main/screenshots/third-arc-bio-2026-09-02T163537.png
security:
- kind: domain-security
  name: Third Arc Bio Domain Security
  slug: third-arc-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: third-arc-bio
tags:
- Company
- Biotechnology
- Therapeutics
- Antibodies
- Oncology
- Immunology
- Life Sciences
- Clinical Stage
website: https://thirdarcbio.com/
---
