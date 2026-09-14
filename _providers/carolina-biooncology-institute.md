---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carolina-biooncology-institute-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carolina-biooncology-institute-llms.txt
- group: company
  title: ''
  type: Website
  url: https://carolinabiooncology.org/
- group: company
  title: ''
  type: About
  url: https://carolinabiooncology.org/about-us/
- group: company
  title: ''
  type: Blog
  url: https://carolinabiooncology.org/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://carolinabiooncology.org/feed/
- group: operate
  title: ''
  type: Support
  url: https://carolinabiooncology.org/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carolinabiooncology.org/privacy-policy/
- group: operate
  title: ''
  type: FAQ
  url: https://carolinabiooncology.org/faq/
- group: company
  title: ''
  type: Careers
  url: https://carolinabiooncology.org/careers/
coverage:
  checked: '2026-09-02'
  detail: Carolina BioOncology Institute is a Phase I oncology clinic and cGMP cell-processing lab, not a software vendor — its site is a 34-page WordPress brochure whose only machine-readable endpoint is the CMS's own /wp-json/ route index, and openapi.json, swagger.json, api-docs, graphql, llms.txt and every named /.well-known/ path all 404 while api. and developer. subdomains do not resolve.
  evidence:
  - status: 404
    url: https://carolinabiooncology.org/openapi.json
  - status: 404
    url: https://carolinabiooncology.org/graphql
  - status: 404
    url: https://carolinabiooncology.org/.well-known/agent-card.json
  - status: 404
    url: https://carolinabiooncology.org/llms.txt
  - status: 200
    url: https://carolinabiooncology.org/wp-json/
  reason: not-a-software-company
  state: none
created: '2026-09-02'
description: Carolina BioOncology Institute (CBOI) is a physician-owned Phase I oncology clinical research clinic and translational laboratory in Huntersville, North Carolina, founded by Dr. John Powderly II. It runs first-in-human and early-phase immunotherapy trials for patients with advanced solid tumors, having opened more than 100 oncology trials over fifteen years, and operates the Human Applications Lab — a cGMP-capable cell-processing and biorepository facility developing autologous cellular therapies — alongside research-use-only analytical and clinical lab analysis services for trial sponsors. CBOI is the parent company of BioCytics and an openEHR Industry Partner. It publishes no public API, developer portal, SDK or machine-readable contract; the only machine-readable surface on its domain is the stock WordPress REST API its CMS emits, which is not a product API and is deliberately not registered here.
image: https://carolinabiooncology.org/wp-content/uploads/2020/09/CBOI-Logo.png
layout: provider
modified: '2026-09-02'
name: Carolina BioOncology Institute
nav: Providers
network: true
overview: 'Carolina BioOncology Institute is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Oncology, Clinical Trials, and Clinical Research.


  Carolina BioOncology Institute''s developer surface includes engineering blog, support, FAQ, and 7 more developer resources.'
random_paper: 12
security:
- kind: domain-security
  name: Carolina Biooncology Institute Domain Security
  slug: carolina-biooncology-institute-domain-security
  summary_line: TLSv1.3 · DMARC
slug: carolina-biooncology-institute
tags:
- Company
- Health Care
- Oncology
- Clinical Trials
- Clinical Research
- Biotechnology
- Cell Therapy
- Laboratory
- Life Sciences
- North Carolina
website: https://carolinabiooncology.org/
---
