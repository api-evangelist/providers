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
  url: security/lb-pharmaceuticals-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lbpharma.us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lbpharma.us/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://lbpharma.us/contact/
coverage:
  checked: '2026-08-23'
  detail: LB Pharmaceuticals is a clinical-stage drug developer whose entire web presence is a WordPress marketing and investor-relations site; the only machine-readable surface is the stock WordPress core REST API at lbpharma.us/wp-json/ (222 routes, every namespace a CMS plugin such as contact-form-7, redirection and wp-smush), with no product API, no developer or docs subdomain (api./docs./developer.lbpharma.us all NXDOMAIN), no GitHub organization and no published client library.
  evidence:
  - status: 200
    url: https://lbpharma.us/wp-json/
  - status: 404
    url: https://lbpharma.us/openapi.json
  - status: 404
    url: https://lbpharma.us/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/lbpharma
  reason: not-a-software-company
  state: none
created: '2026-08-23'
description: 'LB Pharmaceuticals Inc (Nasdaq: LBRX) is a clinical-stage biopharmaceutical company headquartered at One Pennsylvania Plaza, New York, developing novel therapies for neuropsychiatric diseases including schizophrenia and bipolar depression. Its lead asset, LB-102, is an oral small-molecule benzamide antipsychotic with potent D2, D3 and 5HT7 antagonism, positioned to become the first benzamide antipsychotic approved for neuropsychiatric disorders in the United States. The company reported positive Phase 2 schizophrenia results from its NOVA1 trial in January 2025 and initiated the ILLUMINATE-1 Phase 2 bipolar depression trial in January 2026. LB Pharmaceuticals is a drug developer, not a software vendor: it publishes no public API, developer portal, SDK or machine-readable contract, and its web presence is a WordPress corporate and investor-relations site.'
image: https://lbpharma.us/wp-content/uploads/2026/03/LBlogo-color_final-opt.png
layout: provider
modified: '2026-08-23'
name: LB Pharmaceuticals
nav: Providers
network: true
overview: 'LB Pharmaceuticals is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmaceuticals, Biotechnology, Life Sciences, and Health.


  LB Pharmaceuticals'' developer surface includes support and 3 more developer resources.'
random_paper: 14
screenshot: https://raw.githubusercontent.com/api-evangelist/lb-pharmaceuticals/refs/heads/main/screenshots/lb-pharmaceuticals-2026-09-02T150223.png
security:
- kind: domain-security
  name: Lb Pharmaceuticals Domain Security
  slug: lb-pharmaceuticals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lb-pharmaceuticals
tags:
- Company
- Pharmaceuticals
- Biotechnology
- Life Sciences
- Health
- Clinical Trials
- Neuroscience
- Drug Development
website: https://lbpharma.us/
---
