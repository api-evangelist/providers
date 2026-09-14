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
- acting_count: 5
  human_in_the_loop: 0
  name: Nected Agentic Access
  operation_count: 12
  slug: nected-agentic-access
  summary_line: 12 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.nected.ai
  baseurl_source: declared
  description: The Dev API from Nected — 7 operation(s) for dev.
  name: Nected Dev API
  slug: nected-dev-api
- baseURL: https://api.nected.ai
  baseurl_source: declared
  description: The Nected API from Nected — 2 operation(s) for nected.
  name: Nected Nected API
  slug: nected-nected-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nected Dev API
  slug: open-nected-dev-api
- collection_type: open
  name: Dev Nected API
  slug: open-nected-nected-api
- collection_type: open
  name: Nected API
  slug: open-nected
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nected-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nected-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nected-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Nected
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nected-ai
- group: company
  title: ''
  type: Website
  url: https://www.nected.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nected.ai
- group: company
  title: ''
  type: Blog
  url: https://www.nected.ai/blog
created: '2026-03-27'
description: Nected is a low-code workflow automation and decision engine platform for building business rules and automated processes. The API supports triggering rules and workflows, managing global variables, listing entities, retrieving audit logs, and checking usage.
finops:
- name: Nected Finops
  service_category: API
  slug: nected-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nected.png
layout: provider
modified: '2026-05-19'
name: Nected
nav: Providers
network: true
overview: 'Nected publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dev API and Nected API. Tagged areas include Low-Code, Workflow-Automation, Decision Engine, and Business Rules.


  Nected''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Nected Plans Pricing
  plan_count: 3
  slug: nected-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Nected Rate Limits
  slug: nected-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/nected/refs/heads/main/screenshots/nected-2026-06-20T190119.png
security:
- kind: authentication
  name: Nected Authentication
  slug: nected-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nected Domain Security
  slug: nected-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nected
tags:
- Low-Code
- Workflow-Automation
- Decision Engine
- Business Rules
website: https://www.nected.ai
---
