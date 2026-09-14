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
  url: security/truebinding-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.truebinding.com/
- group: operate
  title: ''
  type: Support
  url: https://www.truebinding.com/general-inquiry-page
- group: company
  title: ''
  type: Blog
  url: https://www.truebinding.com/column
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truebinding.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truebinding.com/term-and-condition
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truebinding-llms.txt
coverage:
  checked: '2026-08-30'
  detail: TrueBinding is a clinical-stage antibody biotherapeutics company and cGMP CDMO whose only web presence is a 67-page Squarespace marketing and patient-access site - api., docs. and developer. truebinding.com do not resolve at all, and every OpenAPI, GraphQL, MCP and A2A discovery path probed on www.truebinding.com returned 404.
  evidence:
  - status: 404
    url: https://www.truebinding.com/openapi.json
  - status: 404
    url: https://www.truebinding.com/.well-known/agent-card.json
  - status: 0
    url: https://api.truebinding.com/
  - status: 200
    url: https://www.truebinding.com/services-overview
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: TrueBinding, Inc. is a clinical-stage biotherapeutic company founded in 2016 and headquartered at 4701 Patrick Henry Drive, Santa Clara, California. It develops humanized monoclonal antibodies against Galectin-3 to resolve chronic inflammation ("inflammaging"), led by TB006, which has completed Phase 1b/2a work in Alzheimer's disease and holds an FDA IND clearance for a Phase 2A trial in Parkinson's disease, with additional research programs across ALS, glioblastoma, autism spectrum, stroke, metabolic disease and oncology. Alongside its own pipeline the company sells contract development and manufacturing (CDMO) services from its Santa Clara facility - antibody discovery, cell-line and process development, cGMP monoclonal antibody and media/buffer manufacturing, vivarium and toxicology studies, histology and imaging, clinical drug product logistics, and cGMP training and audit preparation. TrueBinding ships no software product and publishes no public API, SDK, developer portal
  or machine-readable API contract; its web presence is a Squarespace marketing and patient-access site.
image: https://images.squarespace-cdn.com/content/6118e5173909f118e816918e/6f42f3e6-5cbc-4557-960f-86f82b6cd3cd/Logo_Final_OL_082121-01.png?format=2500w&content-type=image%2Fpng
layout: provider
modified: '2026-08-30'
name: TrueBinding
nav: Providers
network: true
overview: 'TrueBinding is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Pharmaceuticals, Life Sciences, and Clinical Trials.


  TrueBinding''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 3
screenshot: https://raw.githubusercontent.com/api-evangelist/truebinding/refs/heads/main/screenshots/truebinding-2026-09-02T164338.png
security:
- kind: domain-security
  name: Truebinding Domain Security
  slug: truebinding-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truebinding
tags:
- Company
- Biotechnology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Drug Discovery
- Monoclonal Antibodies
- Neurodegenerative Disease
- CDMO
- Contract Manufacturing
- Healthcare
website: https://www.truebinding.com/
---
