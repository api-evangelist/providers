---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Activeloop Agentic Access
  operation_count: 1
  slug: activeloop-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- baseURL: https://app.activeloop.ai/api/query/v1
  baseurl_source: declared
  description: The Managed Database API from Activeloop — 1 operation(s) for managed database.
  name: Activeloop Managed Database API
  slug: activeloop-managed-database-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Activeloop Deep Lake Managed Database API
  slug: open-activeloop-managed-database-api
- collection_type: open
  name: Activeloop Deep Lake API
  slug: open-activeloop
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/activeloop-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/activeloop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/activeloop-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/activeloopai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/activeloop
- group: company
  title: ''
  type: Website
  url: https://www.activeloop.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deeplake.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/activeloop-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/activeloop-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/activeloop-finops.yml
created: '2026-06-20'
description: Activeloop builds Deep Lake, a database for AI that stores multimodal datasets (text, images, video, audio, embeddings) in a deep-learning-optimized format. The primary interface is the open-source Deep Lake Python SDK paired with the Tensor Query Language (TQL); datasets live locally, in your own cloud (S3, Azure, GCP), or in the managed Activeloop Cloud (app.activeloop.ai), which also exposes an alpha Managed Database REST query endpoint.
finops:
- name: Activeloop Finops
  service_category: AI and Machine Learning
  slug: activeloop-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/activeloop.png
layout: provider
modified: '2026-06-20'
name: Activeloop
nav: Providers
network: true
overview: 'Activeloop publishes 1 API on the [APIs.io](https://apis.io/) network: Managed Database API. Tagged areas include Artificial Intelligence, Vector Store, Data Lake, Multi-Modal, and Deep Learning.


  Activeloop''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Activeloop Plans Pricing
  plan_count: 4
  slug: activeloop-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Activeloop Rate Limits
  slug: activeloop-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/activeloop/refs/heads/main/screenshots/activeloop-2026-06-20T164223.png
security:
- kind: authentication
  name: Activeloop Authentication
  slug: activeloop-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Activeloop Domain Security
  slug: activeloop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: activeloop
tags:
- Artificial Intelligence
- Vector Store
- Data Lake
- Multi-Modal
- Deep Learning
- Python SDK
website: https://www.activeloop.ai
---
