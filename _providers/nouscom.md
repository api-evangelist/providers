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
  url: security/nouscom-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nouscom-llms.txt
- group: company
  title: ''
  type: Website
  url: https://nouscom.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nouscom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nouscom-ag/
coverage:
  checked: '2026-08-26'
  detail: Nouscom AG is a clinical-stage biotech whose product is a cancer immunotherapy, not software — it has no API host at all (api./dev./developer./docs./portal.nouscom.com are NXDOMAIN), its only public repository is R analysis code for the NOUS-209 Lynch Syndrome study, and its corporate WordPress site sits behind a SiteGround robot challenge that answers HTTP 202 to every path including /openapi.json.
  evidence:
  - status: 0
    url: https://api.nouscom.com/openapi.json
  - status: 202
    url: https://nouscom.com/openapi.json
  - status: 202
    url: https://nouscom.com/.well-known/agent-card.json
  - status: 200
    url: https://github.com/Nouscom
  reason: not-a-software-company
  state: none
created: '2026-08-26'
description: 'Nouscom AG is a private, clinical-stage immuno-oncology company developing next-generation neoantigen-targeted cancer immunotherapies, founded in 2015 by Riccardo Cortese and Alfredo Nicosia, with headquarters in Basel, Switzerland and research and manufacturing operations in Rome, Italy. Its proprietary viral vector platform — great ape adenovirus and MVA vectors able to encode large neoantigen payloads together with other immunomodulators — is used to build both off-the-shelf and personalized cancer vaccines. The lead program, NOUS-209, targets 209 shared frameshift neoantigens for cancer interception in Lynch Syndrome carriers and for the treatment of dMMR/MSI metastatic colorectal cancer in combination with pembrolizumab; its second clinical program, NOUS-PEV, is a personalized immunotherapy for advanced solid tumors. Nouscom raised an oversubscribed EUR 67.5 million Series C in November 2023, co-led by Andera Partners, Bpifrance (InnoBio 2) and M Ventures. Nouscom is a
  therapeutics developer, not a software vendor: it publishes no public API, developer portal, SDK or machine-readable API contract, and is profiled here as an identity-only record.'
layout: provider
modified: '2026-08-26'
name: Nouscom
nav: Providers
network: true
overview: Nouscom is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Immuno-Oncology, Pharmaceuticals, and Life Sciences.
random_paper: 16
screenshot: https://raw.githubusercontent.com/api-evangelist/nouscom/refs/heads/main/screenshots/nouscom-2026-09-02T150806.png
security:
- kind: domain-security
  name: Nouscom Domain Security
  slug: nouscom-domain-security
  summary_line: TLSv1.3
slug: nouscom
tags:
- Company
- Biotechnology
- Immuno-Oncology
- Pharmaceuticals
- Life Sciences
- Clinical Trials
- Cancer Immunotherapy
- Switzerland
- Italy
- Private Company
website: https://nouscom.com/
---
