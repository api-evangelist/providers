---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Celanese API
  slug: open-celanese
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/celanese-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/celanese
- group: company
  title: ''
  type: Website
  url: https://www.celanese.com
- group: other
  title: ''
  type: Digital Assistant
  url: https://materials.celanese.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/celanese-llms.txt
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Celanese
coverage:
  checked: '2026-09-06'
  detail: 'Celanese sells polymers and acetyl chemicals, not software: there is no developer program to find — developer.celanese.com and developers.celanese.com do not resolve, api.celanese.com presents no matching certificate, the real github.com/Celanese organization publishes zero public repositories, seven package registries return zero first-party libraries, and the only digital product (the Chemille material-selection assistant at materials.celanese.com) is a browser app for engineers that ships no API, no llms.txt and no .well-known document.'
  evidence:
  - status: 404
    url: https://www.celanese.com/llms.txt
  - status: 404
    url: https://www.celanese.com/.well-known/security.txt
  - status: 404
    url: https://materials.celanese.com/.well-known/security.txt
  - status: 200
    url: https://api.github.com/orgs/Celanese/repos
  reason: not-a-software-company
  state: none
created: '2024-01-15'
description: Celanese Corporation is a global chemical and specialty materials company that produces high-performance engineered polymers and acetyl products used across automotive, medical, consumer, and industrial applications. Celanese has no publicly documented developer API; digital engagement is delivered through the Chemille digital materials assistant for product search and selection, and a Cognite Data Fusion based manufacturing data platform for internal operations.
finops:
- name: Celanese Finops
  service_category: API
  slug: celanese-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/celanese.png
layout: provider
modified: '2026-09-06'
name: Celanese
nav: Providers
network: true
overview: Celanese publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chemicals, Engineered Polymers, Materials, Specialty Materials, and Fortune 500.
plans:
- name: Celanese Plans Pricing
  plan_count: 0
  slug: celanese-plans-pricing
press:
- date: '2026-05-25'
  title: Celanese Designing the Future at K 2025
  url: https://www.celanese.com/news-and-media/2025/october/celanese-designing-the-future-at-k-2025
- date: '2026-05-25'
  title: Telecom Polymers
  url: https://www.celanese.com/industries/telecom
- date: '2026-05-25'
  title: Radix and Celanese Partnership Leverages AI to Harness the ...
  url: https://www.radixeng.com/post/radix-and-celanese-partnership-leverages-ai-to-harness-the-power-of-industrial-data
- date: '2026-05-25'
  title: Fourth Quarter 2025 Earnings Prepared Comments
  url: https://www.sec.gov/Archives/edgar/data/1306830/000130683026000017/q420258-kex991a.htm
- date: '2026-05-25'
  title: Celanese's Chemille AI Assistant Revolutionizes Material ...
  url: https://www.linkedin.com/posts/useready_materialsscience-enterpriseai-chemicalindustry-activity-7433474582881259520-V9F8
random_paper: 13
rate_limits:
- limit_count: 0
  name: Celanese Rate Limits
  slug: celanese-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/celanese/refs/heads/main/screenshots/celanese-2026-06-20T174110.png
security:
- kind: domain-security
  name: Celanese Domain Security
  slug: celanese-domain-security
  summary_line: TLSv1.3 · DMARC
slug: celanese
tags:
- Chemicals
- Engineered Polymers
- Materials
- Specialty Materials
- Fortune 500
website: https://www.celanese.com
---
