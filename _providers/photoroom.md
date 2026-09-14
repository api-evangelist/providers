---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Photoroom Agentic Access
  operation_count: 7
  slug: photoroom-agentic-access
  summary_line: 7 operations · 3 acting
api_count: 1
apis:
- baseURL: https://image-api.photoroom.com
  baseurl_source: declared
  description: The Account API from Photoroom — 2 operation(s) for account.
  name: Photoroom Account API
  slug: photoroom-account-api
- baseURL: https://image-api.photoroom.com
  baseurl_source: declared
  description: The Edit API from Photoroom — 1 operation(s) for edit.
  name: Photoroom Edit API
  slug: photoroom-edit-api
- baseURL: https://image-api.photoroom.com
  baseurl_source: declared
  description: The Render API from Photoroom — 1 operation(s) for render.
  name: Photoroom Render API
  slug: photoroom-render-api
- baseURL: https://image-api.photoroom.com
  baseurl_source: declared
  description: The Segment API from Photoroom — 1 operation(s) for segment.
  name: Photoroom Segment API
  slug: photoroom-segment-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Photoroom Account API
  slug: open-photoroom-account-api
- collection_type: open
  name: Photoroom Account Edit API
  slug: open-photoroom-edit-api
- collection_type: open
  name: Photoroom Account Render API
  slug: open-photoroom-render-api
- collection_type: open
  name: Photoroom Account Segment API
  slug: open-photoroom-segment-api
- collection_type: open
  name: Photoroom API
  slug: open-photoroom
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/photoroom-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/photoroom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/photoroom-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Photoroom
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/photoroom
- group: company
  title: ''
  type: Website
  url: https://www.photoroom.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.photoroom.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/photoroom-openapi.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/photoroom-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/photoroom-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/photoroom-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.photoroom.com/llms.txt
created: '2026-05-08'
description: Photoroom is an AI image editing platform with strong background removal and e-commerce-style product photo generation. Public APIs include the Remove Background API and the Image Editing API (Plus plan), with specialized endpoints for PhotoFix, Reposition, Product Beautifier, Analyze QA, Image to Video, Photo Composition, Virtual Model, Flat Lay, and Ghost Mannequin. OpenAPI spec is published.
finops:
- name: Photoroom Finops
  service_category: AI
  slug: photoroom-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/photoroom.png
layout: provider
modified: '2026-05-19'
name: Photoroom
nav: Providers
network: true
overview: 'Photoroom publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Edit API, Render API, and 1 more. Tagged areas include Artificial Intelligence, Image Editing, Background Removal, E-Commerce, and Visual.


  Photoroom''s developer surface includes authentication, documentation, and 10 more developer resources.'
plans:
- name: Photoroom Plans Pricing
  plan_count: 5
  slug: photoroom-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 3
  name: Photoroom Rate Limits
  slug: photoroom-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/photoroom/refs/heads/main/screenshots/photoroom-2026-06-20T191651.png
security:
- kind: authentication
  name: Photoroom Authentication
  slug: photoroom-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Photoroom Domain Security
  slug: photoroom-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: photoroom
tags:
- Artificial Intelligence
- Image Editing
- Background Removal
- E-Commerce
- Visual
website: https://www.photoroom.com/
---
