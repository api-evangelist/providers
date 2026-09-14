---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  - '{''url'': ''https://aetion.com/'', ''status'': 301, ''note'': ''declared website redirects to https://www.datavant.com/ — a different registrable domain (aetion.com -> datavant.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/datavant/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aetion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aetion.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aetion
- group: operate
  title: ''
  type: Support
  url: https://support.aetion.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.datavant.com/privacy-policy
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/aetion_stock/
coverage:
  checked: '2026-08-06'
  detail: Aetion was absorbed into Datavant when the acquisition closed on 11 July 2025, and every path on aetion.com — including /.well-known/* — now answers HTTP 301 into www.datavant.com, so there is no Aetion-origin developer surface left to read; the only Aetion host still serving anything of its own is the customer support portal at support.aetion.com, a Salesforce Experience Cloud community.
  evidence:
  - status: 301
    url: https://aetion.com/
  - status: 301
    url: https://aetion.com/technology/platform/
  - status: 301
    url: https://aetion.com/.well-known/agent-card.json
  - status: 503
    url: https://support.aetion.com/
  - status: 200
    url: https://github.com/aetion
  reason: defunct
  state: none
created: '2026-08-06'
description: 'Aetion is a healthcare technology company that builds real-world evidence (RWE) software for biopharma, medical device manufacturers, payers and regulators. Its Aetion Evidence Platform (AEP) turns claims, electronic health record, registry, patient-reported and trial data into transparent, reproducible, regulatory-grade evidence, delivered as a set of applications: Discover for exploratory analysis, Substantiate for study implementation, Activate as a low-code plus hosted-code workbench, and Generate for synthetic data. Founded by two Harvard Medical School professors, Aetion was acquired by Datavant; the acquisition closed 11 July 2025 and Aetion now operates inside Datavant''s Life Sciences business. As of this profile the aetion.com domain redirects wholesale to datavant.com and Aetion publishes no standalone developer program, public API reference or machine-readable specification.'
image: https://avatars.githubusercontent.com/u/54075156?v=4
layout: provider
modified: '2026-08-06'
name: Aetion
nav: Providers
network: true
overview: 'Aetion is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real-World Evidence, Healthcare, Life Sciences, and Clinical Research.


  Aetion''s developer surface includes support and 6 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/aetion/refs/heads/main/screenshots/aetion-2026-08-07T161016.png
security:
- kind: domain-security
  name: Aetion Domain Security
  slug: aetion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aetion
tags:
- Company
- Real-World Evidence
- Healthcare
- Life Sciences
- Clinical Research
- Health Data
- Data Analytics
website: https://aetion.com/
---
