---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - rate-limits
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/orbital-materials-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.orbitalindustries.com/
- group: company
  title: ''
  type: About
  url: https://www.orbitalindustries.com/about
- group: company
  title: ''
  type: Blog
  url: https://www.orbitalindustries.com/news
- group: operate
  title: ''
  type: Support
  url: https://www.orbitalindustries.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/orbital-materials
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.orbitalindustries.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.orbitalindustries.com/legal/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/orbital-materials-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/orbital-materials-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/orbital-materials-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/orbital-materials-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/orbital-materials-rate-limits.yml
coverage:
  checked: '2026-08-26'
  detail: Orbital Materials (now Orbital Industries) ships its only public programmable surface as a locally-run Apache-2.0 Python package, `orb-models` on PyPI, and its full sitemap lists no /developers, /docs, /api or /pricing page — the CurieOS platform is offered only through a "Wondering what CurieOS could do for your R&D?" contact form, and the platform hosts that do exist in DNS never answer a TLS handshake from the public internet.
  evidence:
  - status: 200
    url: https://www.orbitalindustries.com/sitemap.xml
  - status: 200
    url: https://www.orbitalindustries.com/openapi.json
  - status: 200
    url: https://www.orbitalindustries.com/llms.txt
  - status: 404
    url: https://www.orbitalindustries.com/docs
  - status: 404
    url: https://www.orbitalindustries.com/.well-known/agent-card.json
  - status: 404
    url: https://orbitalindustries.com/.well-known/agent.json
  - status: 0
    url: https://platform.orbitalindustries.com/
  - status: 200
    url: https://pypi.org/pypi/orb-models/json
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: Orbital Materials (rebranded Orbital Industries in 2026) is an AI industrial company founded in 2022 by Jonathan Godwin, a former DeepMind researcher, with offices in London and San Francisco. It applies frontier AI to the discovery, testing and deployment of advanced materials and to the hardware and manufacturing built around them, co-designing materials and hardware together rather than sequentially. Its public technical output is a family of open-source machine-learned interatomic potentials — the Orb, Orb-v2/v3 and OrbMol foundation models for atomic simulation — distributed as the Apache-2.0 licensed `orb-models` Python package on PyPI and GitHub and as model weights on Hugging Face. Its internal platform, CurieOS, and its Orbital IT data-center module business are marketed through a contact form rather than a developer program. The company publishes no public HTTP API, developer portal, or machine-readable API contract of any kind.
image: https://www.orbitalindustries.com/og-image-main.jpg
layout: provider
modified: '2026-08-26'
name: Orbital Materials
nav: Providers
network: true
overview: 'Orbital Materials is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Machine-Learning, Materials Science, and Computational Chemistry.


  Orbital Materials'' developer surface includes engineering blog, support, changelog, and 10 more developer resources.'
plans:
- name: Orbital Materials Plans Pricing
  plan_count: 0
  slug: orbital-materials-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Orbital Materials Rate Limits
  slug: orbital-materials-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/orbital-materials/refs/heads/main/screenshots/orbital-materials-2026-09-02T150856.png
security:
- kind: domain-security
  name: Orbital Materials Domain Security
  slug: orbital-materials-domain-security
  summary_line: TLSv1.2 · HSTS
slug: orbital-materials
tags:
- Company
- Artificial Intelligence
- Machine-Learning
- Materials Science
- Computational Chemistry
- Scientific Computing
- Climate Technology
- Open Source Models
- Data Centers
- Manufacturing
website: https://www.orbitalindustries.com/
---
