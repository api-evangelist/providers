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
- acting_count: 3
  human_in_the_loop: 0
  name: Inferless Agentic Access
  operation_count: 3
  slug: inferless-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.inferless.com
  baseurl_source: declared
  description: The Inference API from Inferless — 1 operation(s) for inference.
  name: Inferless Inference API
  slug: inferless-inference-api
- baseURL: https://api.inferless.com
  baseurl_source: declared
  description: The Model Management API from Inferless — 2 operation(s) for model management.
  name: Inferless Model Management API
  slug: inferless-model-management-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Inferless Inference API
  slug: open-inferless-inference-api
- collection_type: open
  name: Inferless Inference Model Management API
  slug: open-inferless-model-management-api
- collection_type: open
  name: Inferless API
  slug: open-inferless
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/inferless-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/inferless-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/inferless-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inferless
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/inferless
- group: company
  title: ''
  type: Website
  url: https://www.inferless.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.inferless.com
- group: commercial
  title: ''
  type: Plans
  url: plans/inferless-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/inferless-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/inferless-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.inferless.com/blog/rss.xml
created: '2026-06-20'
description: Inferless is a serverless GPU inference platform for machine learning models. Teams import a model from Hugging Face, a Git repo, or a container and Inferless auto-generates a scalable REST inference endpoint billed per second of GPU compute. A workspace-scoped management API and CLI cover model import, deployment, settings, logs, secrets, and volumes.
finops:
- name: Inferless Finops
  service_category: AI and Machine Learning
  slug: inferless-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/inferless.png
layout: provider
modified: '2026-06-20'
name: Inferless
nav: Providers
network: true
overview: 'Inferless publishes 2 APIs on the [APIs.io](https://apis.io/) network: Inference API and Model Management API. Tagged areas include Artificial Intelligence, ML Inference, Serverless GPU, Model Deployment, and Inference.


  Inferless'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Inferless Plans Pricing
  plan_count: 4
  slug: inferless-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Inferless Rate Limits
  slug: inferless-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/inferless/refs/heads/main/screenshots/inferless-2026-06-20T183328.png
security:
- kind: authentication
  name: Inferless Authentication
  slug: inferless-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Inferless Domain Security
  slug: inferless-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: inferless
tags:
- Artificial Intelligence
- ML Inference
- Serverless GPU
- Model Deployment
- Inference
website: https://www.inferless.com
---
