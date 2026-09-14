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
  url: security/cirius-therapeutics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cirius-therapeutics-llms.txt
- group: company
  title: ''
  type: Website
  url: https://ciriustx.com/
- group: company
  title: ''
  type: News
  url: https://ciriustx.com/news
- group: operate
  title: ''
  type: Contact
  url: https://ciriustx.com/contact
- group: other
  title: ''
  type: Team
  url: https://ciriustx.com/team
- group: other
  title: ''
  type: Science
  url: https://ciriustx.com/science
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cirius-therapeutics_stock/
coverage:
  checked: '2026-08-09'
  detail: Cirius Therapeutics is a clinical-stage pharmaceutical company whose entire web presence is a five-page GoDaddy-built marketing site (Home/Team/Science/News/Contact) about the MPC inhibitor azemiglitazone — there is no developer section, no API host, no GitHub organization, and every contract-discovery path on ciriustx.com returned a hard 404.
  evidence:
  - status: 200
    url: https://ciriustx.com/
  - status: 200
    url: https://ciriustx.com/llms.txt
  - status: 404
    url: https://ciriustx.com/openapi.json
  - status: 404
    url: https://ciriustx.com/.well-known/agent-card.json
  - status: 404
    url: https://ciriustx.com/.well-known/security.txt
  - status: 404
    url: https://api.github.com/orgs/cirius-therapeutics
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: Cirius Therapeutics, Inc. is a privately held clinical-stage pharmaceutical company based in Grand Rapids, Michigan, developing oral therapies for chronic metabolic diseases driven by insulin resistance, including Type 2 Diabetes, Type 1 Diabetes, obesity and gestational diabetes. Its lead candidate, azemiglitazone (CIR-0602K / MSDC-0602K), is a next-generation insulin sensitizer that inhibits the mitochondrial pyruvate carrier (MPC) to re-balance mitochondrial metabolism, improve glycemic control, preserve lean muscle mass and shift visceral fat to subcutaneous and brown adipose tissue, including in combination with GLP-1 receptor agonists such as tirzepatide. The company publishes a corporate marketing website only; it operates no developer program, public API, or machine-readable API contract.
image: https://img1.wsimg.com/isteam/ip/40701c08-78b4-429c-9131-4a2e35286e89/Cirius_1420x1200_Full-baa8525.jpg
layout: provider
modified: '2026-08-09'
name: Cirius Therapeutics
nav: Providers
network: true
overview: 'Cirius Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Healthcare.


  Cirius Therapeutics'' developer surface includes product news and 7 more developer resources.'
random_paper: 2
screenshot: https://raw.githubusercontent.com/api-evangelist/cirius-therapeutics/refs/heads/main/screenshots/cirius-therapeutics-2026-09-02T145038.png
security:
- kind: domain-security
  name: Cirius Therapeutics Domain Security
  slug: cirius-therapeutics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cirius-therapeutics
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Healthcare
- Clinical Trials
- Metabolic Disease
- Diabetes
website: https://ciriustx.com/
---
