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
- acting_count: 4
  human_in_the_loop: 0
  name: Holistics Agentic Access
  operation_count: 13
  slug: holistics-agentic-access
  summary_line: 13 operations · 4 acting
api_count: 1
apis:
- baseURL: https://secure.holistics.io/api/v2
  baseurl_source: declared
  description: Execute data imports and transforms.
  name: Holistics Data Pipeline API
  slug: holistics-data-pipeline-api
- baseURL: https://secure.holistics.io/api/v2
  baseurl_source: declared
  description: Query the Holistics dataset semantic layer.
  name: Holistics Datasets API
  slug: holistics-datasets-api
- baseURL: https://secure.holistics.io/api/v2
  baseurl_source: declared
  description: Asynchronous report data export jobs.
  name: Holistics Export API
  slug: holistics-export-api
- baseURL: https://secure.holistics.io/api/v2
  baseurl_source: declared
  description: Poll ETL and export job status.
  name: Holistics Jobs API
  slug: holistics-jobs-api
- baseURL: https://secure.holistics.io/api/v2
  baseurl_source: declared
  description: Submit report queries and retrieve results.
  name: Holistics Reports API
  slug: holistics-reports-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Holistics Data Pipeline API
  slug: open-holistics-data-pipeline-api
- collection_type: open
  name: Holistics Data Pipeline Datasets API
  slug: open-holistics-datasets-api
- collection_type: open
  name: Holistics Data Pipeline Export API
  slug: open-holistics-export-api
- collection_type: open
  name: Holistics Data Pipeline Jobs API
  slug: open-holistics-jobs-api
- collection_type: open
  name: Holistics Data Pipeline Reports API
  slug: open-holistics-reports-api
- collection_type: open
  name: Holistics API
  slug: open-holistics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/holistics-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/holistics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/holistics-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/holistics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/holistics
- group: company
  title: ''
  type: Website
  url: https://www.holistics.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs-v2.holistics.io/api
- group: commercial
  title: ''
  type: Plans
  url: plans/holistics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/holistics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/holistics-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.holistics.io/blog/
created: '2026-06-20'
description: Holistics is a self-service business intelligence and analytics platform built around code-based data modeling (AML - Analytics Modeling Language), Git version control, and a SQL/dataset semantic layer. Its REST API lets teams query datasets and reports, export data to CSV/JSON/XLSX, trigger data imports and transforms, and poll ETL jobs, while a JWT-signed Embed API powers embedded, multi-tenant analytics inside customer applications.
finops:
- name: Holistics Finops
  service_category: Analytics and Business Intelligence
  slug: holistics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/holistics.png
layout: provider
modified: '2026-06-20'
name: Holistics
nav: Providers
network: true
overview: 'Holistics publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Data Pipeline API, Datasets API, Export API, and 2 more. Tagged areas include Business Intelligence, Analytics, Self-Service BI, Data Modeling, and Embedded Analytics.


  Holistics'' developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Holistics Plans Pricing
  plan_count: 5
  slug: holistics-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 4
  name: Holistics Rate Limits
  slug: holistics-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/holistics/refs/heads/main/screenshots/holistics-2026-06-20T182813.png
security:
- kind: authentication
  name: Holistics Authentication
  slug: holistics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Holistics Domain Security
  slug: holistics-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: holistics
tags:
- Business Intelligence
- Analytics
- Self-Service BI
- Data Modeling
- Embedded Analytics
website: https://www.holistics.io
---
