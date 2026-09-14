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
  url: security/soley-therapeutics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soleytherapeutics.com/
- group: company
  title: ''
  type: About
  url: https://soleytherapeutics.com/about/
- group: other
  title: ''
  type: Pipeline
  url: https://soleytherapeutics.com/pipeline/
- group: operate
  title: ''
  type: Contact
  url: https://soleytherapeutics.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Soley-Therapeutics
- group: other
  title: ''
  type: SecondaryMarket
  url: https://www.hiive.com/securities/soley-therapeutics-stock
coverage:
  checked: '2026-08-05'
  detail: 'Soley sells therapeutics, not software - its cell stress sensing platform is an internal discovery engine - and no API host exists to document: wildcard DNS makes api/docs/developer subdomains resolve to the same WordPress marketing host whose TLS certificate covers only the apex and www, the GitHub org holds only two forks of third-party ML infrastructure (NVIDIA dcgm-exporter), and no npm or PyPI package exists. Note the 202s below are a SiteGround "sg-captcha: challenge" interstitial that answers every path including a nonsense control, so the marketing site itself was never readable by our probe - the no-API finding rests on the DNS, TLS, GitHub and registry evidence, not on that host.'
  evidence:
  - status: 200
    url: https://github.com/Soley-Therapeutics
  - status: 200
    url: https://api.github.com/orgs/soley-therapeutics/repos
  - status: 200
    url: https://registry.npmjs.org/-/v1/search?text=soley%20therapeutics
  - status: 404
    url: https://pypi.org/pypi/soley-therapeutics/json
  - status: 202
    url: https://soleytherapeutics.com/.well-known/agent-card.json
  - status: 202
    url: https://soleytherapeutics.com/openapi.json
  reason: not-a-software-company
  state: none
created: '2026-08-05'
description: 'Soley Therapeutics is a science-first, tech-enabled drug discovery and development company headquartered in South San Francisco, California, using human cells as biological sensors to uncover first-in-class medicines. Its cell stress sensing platform captures time-resolved cellular responses across thousands of features and applies computer vision and machine learning to compress them into compact signatures, screening hundreds of thousands of compounds per week on proprietary automation and robotics. The company is advancing a lead oncology asset for acute myeloid leukemia toward an IND filing, a second oncology asset for solid tumors in IND-enabling studies, and non-oncology stress-reducing candidates for neurodegenerative and metabolic disease. Soley raised a $200M Series C in January 2026, bringing total funding to roughly $290M. The platform is an internal discovery engine: Soley is a therapeutics developer, not a software vendor, and publishes no public API, developer
  portal, or machine-readable specification.'
layout: provider
modified: '2026-08-05'
name: Soley Therapeutics
nav: Providers
network: true
overview: Soley Therapeutics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Drug Discovery, and Oncology.
random_paper: 8
screenshot: https://raw.githubusercontent.com/api-evangelist/soley-therapeutics/refs/heads/main/screenshots/soley-therapeutics-2026-09-02T160128.png
security:
- kind: domain-security
  name: Soley Therapeutics Domain Security
  slug: soley-therapeutics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: soley-therapeutics
tags:
- Company
- Biotechnology
- Therapeutics
- Drug Discovery
- Oncology
- Artificial Intelligence
- Machine-Learning
- Life Sciences
- Healthcare
website: https://soleytherapeutics.com/
---
