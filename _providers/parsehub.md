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
  name: Parsehub Agentic Access
  operation_count: 8
  slug: parsehub-agentic-access
  summary_line: 8 operations · 3 acting
api_count: 1
apis:
- baseURL: https://www.parsehub.com/api/v2
  baseurl_source: declared
  description: The Projects API from ParseHub — 4 operation(s) for projects.
  name: ParseHub Projects API
  slug: parsehub-projects-api
- baseURL: https://www.parsehub.com/api/v2
  baseurl_source: declared
  description: The Runs API from ParseHub — 3 operation(s) for runs.
  name: ParseHub Runs API
  slug: parsehub-runs-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ParseHub Projects API
  slug: open-parsehub-projects-api
- collection_type: open
  name: ParseHub Projects Runs API
  slug: open-parsehub-runs-api
- collection_type: open
  name: ParseHub API
  slug: open-parsehub
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/parsehub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parsehub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/parsehub-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.parsehub.com/blog/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parsehub
- group: company
  title: ''
  type: Website
  url: https://www.parsehub.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.parsehub.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.parsehub.com/docs/ref/api/v2/
created: '2026-03-29'
description: ParseHub is a visual web scraping tool that turns any website into an API with a point-and-click interface for data extraction.
finops:
- name: Parsehub Finops
  service_category: API
  slug: parsehub-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parsehub.png
layout: provider
modified: '2026-05-19'
name: ParseHub
nav: Providers
network: true
overview: 'ParseHub publishes 2 APIs on the [APIs.io](https://apis.io/) network: Projects API and Runs API. Tagged areas include Data Extraction, Scraping, and Visual Scraping.


  ParseHub''s developer surface includes authentication, engineering blog, documentation, API reference, and 4 more developer resources.'
plans:
- name: Parsehub Plans Pricing
  plan_count: 3
  slug: parsehub-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Parsehub Rate Limits
  slug: parsehub-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/parsehub/refs/heads/main/screenshots/parsehub-2026-06-20T191423.png
security:
- kind: authentication
  name: Parsehub Authentication
  slug: parsehub-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Parsehub Domain Security
  slug: parsehub-domain-security
  summary_line: TLSv1.3 · HSTS
slug: parsehub
tags:
- Data Extraction
- Scraping
- Visual Scraping
website: https://www.parsehub.com/
---
