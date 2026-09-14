---
access_model:
  confidence: high
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Zuva Agentic Access
  operation_count: 22
  slug: zuva-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 1
apis:
- baseURL: https://us.app.zuva.ai/api/v2
  baseurl_source: declared
  description: Multi-level document classification.
  name: Zuva Classification API
  slug: zuva-classification-api
- baseURL: https://us.app.zuva.ai/api/v2
  baseurl_source: declared
  description: Extract field values from documents.
  name: Zuva Field Extraction API
  slug: zuva-field-extraction-api
- baseURL: https://us.app.zuva.ai/api/v2
  baseurl_source: declared
  description: Field catalog management.
  name: Zuva Fields API
  slug: zuva-fields-api
- baseURL: https://us.app.zuva.ai/api/v2
  baseurl_source: declared
  description: Upload and manage document files.
  name: Zuva Files API
  slug: zuva-files-api
- baseURL: https://us.app.zuva.ai/api/v2
  baseurl_source: declared
  description: Optical character recognition.
  name: Zuva OCR API
  slug: zuva-ocr-api
artifact_total: 18
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zuva DocAI Classification API
  slug: open-zuva-classification-api
- collection_type: open
  name: Zuva DocAI Classification Field Extraction API
  slug: open-zuva-field-extraction-api
- collection_type: open
  name: Zuva DocAI Classification Fields API
  slug: open-zuva-fields-api
- collection_type: open
  name: Zuva DocAI Classification Files API
  slug: open-zuva-files-api
- collection_type: open
  name: Zuva DocAI Classification OCR API
  slug: open-zuva-ocr-api
- collection_type: open
  name: Zuva DocAI API
  slug: open-zuva
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zuva-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zuva-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zuva-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zuvaai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zuva-inc
- group: company
  title: ''
  type: Website
  url: https://zuva.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://zuva.ai/documentation/
- group: commercial
  title: ''
  type: Plans
  url: plans/zuva-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zuva-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zuva-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://zuva.ai/blog/
created: '2026-06-21'
description: Zuva (by Kira Systems) provides a contract and document AI REST API for extracting structured data from unstructured documents. The Zuva DocAI API offers asynchronous OCR, field extraction across 1,400+ pre-built fields, multi-level document classification across 220+ document types, language detection, and a searchable fields catalog, secured with Bearer API tokens across US and EU regions.
finops:
- name: Zuva Finops
  service_category: AI and Machine Learning
  slug: zuva-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zuva.png
layout: provider
modified: '2026-06-21'
name: Zuva
nav: Providers
network: true
overview: 'Zuva publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Classification API, Field Extraction API, Fields API, and 2 more. Tagged areas include Artificial Intelligence, Document AI, Contract Analysis, Field Extraction, and Classification.


  Zuva''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Zuva Plans Pricing
  plan_count: 3
  slug: zuva-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 6
  name: Zuva Rate Limits
  slug: zuva-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/zuva/refs/heads/main/screenshots/zuva-2026-09-02T171913.png
security:
- kind: authentication
  name: Zuva Authentication
  slug: zuva-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zuva Domain Security
  slug: zuva-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: zuva
tags:
- Artificial Intelligence
- Document AI
- Contract Analysis
- Field Extraction
- Classification
- OCR
website: https://zuva.ai/
---
