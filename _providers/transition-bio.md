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
- group: company
  title: ''
  type: Website
  url: https://transitionbio.com/
- group: company
  title: ''
  type: About
  url: https://transitionbio.com/about-us/
- group: company
  title: ''
  type: Blog
  url: https://transitionbio.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://transitionbio.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://transitionbio.com/contact-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/transitionbio
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transition-bio-inc/
- group: company
  title: ''
  type: Careers
  url: https://transitionbio.com/careers/
- group: company
  title: ''
  type: Partners
  url: https://transitionbio.com/collaborate/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/transition-bio-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transition-bio-domain-security.yml
coverage:
  checked: '2026-08-30'
  detail: Transition Bio is a preclinical therapeutics developer whose product is drug candidates, not software; its entire web presence is an 11-page WordPress marketing site with no developer section, and every contract-discovery path (/openapi.json, /swagger.json, /api-docs, /graphql, /llms.txt and all seven /.well-known/ paths) returned 404, while api./docs./developer. transitionbio.com are wildcard DNS to the same shared host serving that marketing site.
  evidence:
  - status: 404
    url: https://transitionbio.com/openapi.json
  - status: 404
    url: https://transitionbio.com/swagger.json
  - status: 404
    url: https://transitionbio.com/api-docs
  - status: 404
    url: https://transitionbio.com/graphql
  - status: 404
    url: https://transitionbio.com/llms.txt
  - status: 404
    url: https://transitionbio.com/.well-known/agent-card.json
  - status: 404
    url: https://transitionbio.com/.well-known/api-catalog
  - status: 200
    url: https://transitionbio.com/
  reason: not-a-software-company
  state: none
created: '2026-08-30'
description: 'Transition Bio is a preclinical drug discovery company built on biomolecular condensate science, operating as a joint spin-out of the University of Cambridge and Harvard University with sites in Cambridge, Massachusetts and Cambridge, United Kingdom. The company combines droplet-microfluidics high-throughput molecular screening with a machine learning engine to identify and optimize small molecules that modulate intrinsically disordered proteins and the condensates they form, an approach the company has described as its Condensomics platform. It was seeded in November 2020 and closed a $50 million Series A in June 2022 led by Northpond Ventures with Taiho Ventures, Bristol Myers Squibb and Magnetic Ventures participating, and in November 2025 announced a collaboration with Voyager Therapeutics on small molecules targeting TDP-43 in ALS and frontotemporal dementia. Transition Bio is a therapeutics developer rather than a software or data vendor: it publishes no developer portal,
  no API documentation and no machine-readable API contract on any host it controls.'
image: https://transitionbio.com/wp-content/uploads/2022/04/logo.png
layout: provider
modified: '2026-08-30'
name: Transition Bio
nav: Providers
network: true
overview: 'Transition Bio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Drug Discovery, Life Sciences, and Machine-Learning.


  Transition Bio''s developer surface includes engineering blog, support, and 9 more developer resources.'
random_paper: 9
screenshot: https://raw.githubusercontent.com/api-evangelist/transition-bio/refs/heads/main/screenshots/transition-bio-2026-09-02T164130.png
security:
- kind: domain-security
  name: Transition Bio Domain Security
  slug: transition-bio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: transition-bio
tags:
- Company
- Biotechnology
- Drug Discovery
- Life Sciences
- Machine-Learning
- Artificial Intelligence
- Microfluidics
- Proteomics
- Therapeutics
- Neurodegeneration
website: https://transitionbio.com/
---
