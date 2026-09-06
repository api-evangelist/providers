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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/syntheticgenomics
- group: build
  title: ''
  type: Packages
  url: packages/synthetic-genomics-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/synthetic-genomics-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/synthetic-genomics-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/synthetic-genomics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/synthetic-genomics-rate-limits.yml
- group: other
  title: ''
  type: Wikipedia
  url: https://en.wikipedia.org/wiki/Viridos_(company)
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/synthetic-genomics_stock/
coverage:
  checked: '2026-08-29'
  detail: Viridos sold substantially all of its algae biofuel technology in Chapter 11 and had its case dismissed on 2025-11-26; viridos.com now returns a 21-byte "403 | Access blocked" page from a SiteGround default vhost on every path, behind a certificate issued for giowm1252.siteground.biz, and the legacy syntheticgenomics.com domain was dropped and is now a Canadian online-casino affiliate site.
  evidence:
  - status: 403
    url: https://viridos.com/
  - status: 403
    url: https://viridos.com/openapi.json
  - status: 403
    url: https://viridos.com/.well-known/api-catalog
  - status: 403
    url: https://dspace.bio/
  - status: 200
    url: https://github.com/syntheticgenomics
  - status: 200
    url: https://cases.stretto.com/viridos/
  reason: defunct
  state: none
created: '2026-08-29'
description: Viridos, founded in 2005 as Synthetic Genomics, Inc. by J. Craig Venter and Hamilton Smith and renamed Viridos in September 2021, was a La Jolla, California synthetic-biology company that engineered microalgae genomes to produce low-carbon-intensity biofuels, running its algal biofuel program as a long-term research partnership with ExxonMobil. The company never published an API, a developer portal, or any machine-readable contract; its only public developer surface was a GitHub organization holding two first-party open-source projects - the AGPL-licensed sgidspace deep-learning protein annotation library and a sensor calibration app - alongside seven forks of third-party tools. Viridos filed for Chapter 11 bankruptcy in the District of Delaware on 2025-04-14, sold substantially all of its algae biofuel technology to Breakthrough Energy Ventures II, L.P., and the case was dismissed on 2025-11-26. Its website has served no content since roughly October 2025.
layout: provider
modified: '2026-08-29'
name: Viridos
nav: Providers
network: true
overview: Viridos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Synthetic Biology, Biotechnology, Genomics, and Biofuels.
plans:
- name: Synthetic Genomics Plans Pricing
  plan_count: 0
  slug: synthetic-genomics-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Synthetic Genomics Rate Limits
  slug: synthetic-genomics-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/synthetic-genomics/refs/heads/main/screenshots/synthetic-genomics-2026-09-02T161635.png
security:
- kind: domain-security
  name: Synthetic Genomics Domain Security
  slug: synthetic-genomics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: synthetic-genomics
tags:
- Company
- Synthetic Biology
- Biotechnology
- Genomics
- Biofuels
- Algae
- Climate Tech
- Life Sciences
- Open-Source
- Defunct
---
