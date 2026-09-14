---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Notdiamond Agentic Access
  operation_count: 6
  slug: notdiamond-agentic-access
  summary_line: 6 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Custom Routers API from Not Diamond — 2 operation(s) for custom routers.
  name: Not Diamond Custom Routers API
  slug: notdiamond-custom-routers-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Feedback API from Not Diamond — 2 operation(s) for feedback.
  name: Not Diamond Feedback API
  slug: notdiamond-feedback-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Model Routing API from Not Diamond — 1 operation(s) for model routing.
  name: Not Diamond Model Routing API
  slug: notdiamond-model-routing-api
- baseURL: https://api.notdiamond.ai/v2
  baseurl_source: declared
  description: The Models API from Not Diamond — 1 operation(s) for models.
  name: Not Diamond Models API
  slug: notdiamond-models-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Not Diamond Custom Routers API
  slug: open-notdiamond-custom-routers-api
- collection_type: open
  name: Not Diamond Custom Routers Feedback API
  slug: open-notdiamond-feedback-api
- collection_type: open
  name: Not Diamond Custom Routers Model Routing API
  slug: open-notdiamond-model-routing-api
- collection_type: open
  name: Not Diamond Custom Routers Models API
  slug: open-notdiamond-models-api
- collection_type: open
  name: Not Diamond API
  slug: open-notdiamond
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/notdiamond-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/notdiamond-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/notdiamond-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.notdiamond.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Not-Diamond
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/not-diamond
- group: company
  title: ''
  type: Website
  url: https://www.notdiamond.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.notdiamond.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/notdiamond-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/notdiamond-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/notdiamond-finops.yml
created: '2026-06-20'
description: Not Diamond is an AI model router that determines the best LLM to call for any given prompt. Its REST API routes each request to the optimal model across providers based on quality, cost, and latency tradeoffs, accepts real-time feedback to personalize routing, and can train custom routers from evaluation datasets.
finops:
- name: Notdiamond Finops
  service_category: AI and Machine Learning
  slug: notdiamond-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/notdiamond.png
layout: provider
modified: '2026-06-20'
name: Not Diamond
nav: Providers
network: true
overview: 'Not Diamond publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Custom Routers API, Feedback API, Model Routing API, and 1 more. Tagged areas include Artificial Intelligence, LLM, Model Routing, Router, and Orchestration.


  Not Diamond''s developer surface includes authentication, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Notdiamond Plans Pricing
  plan_count: 2
  slug: notdiamond-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Notdiamond Rate Limits
  slug: notdiamond-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/notdiamond/refs/heads/main/screenshots/notdiamond-2026-06-20T190525.png
security:
- kind: authentication
  name: Notdiamond Authentication
  slug: notdiamond-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Notdiamond Domain Security
  slug: notdiamond-domain-security
  summary_line: TLSv1.3 · HSTS
slug: notdiamond
tags:
- Artificial Intelligence
- LLM
- Model Routing
- Router
- Orchestration
website: https://www.notdiamond.ai
---
