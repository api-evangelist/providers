---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 1
apis:
- description: REST API at https://api.meshy.ai for Text-to-3D (v2 with preview + refine workflow), Image-to-3D, Multi Image-to-3D, Remesh, Rigging, Animation, Retexture, Text-to-Image, Image-to-Image, Multi-Color P
  name: Meshy API
  slug: platform
- baseURL: https://api.meshy.ai/openapi/v2
  baseurl_source: declared
  description: The Image to 3D API from Meshy — 3 operation(s) for image to 3d.
  name: Meshy Image to 3D API
  slug: meshy-image-to-3d-api
- baseURL: https://api.meshy.ai/openapi/v2
  baseurl_source: declared
  description: The Text to 3D API from Meshy — 3 operation(s) for text to 3d.
  name: Meshy Text to 3D API
  slug: meshy-text-to-3d-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Meshy Image to 3D API
  slug: open-meshy-image-to-3d-api
- collection_type: open
  name: Meshy Text to 3D API
  slug: open-meshy-text-to-3d-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/meshy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meshy-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meshy-dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/meshyai
- group: company
  title: ''
  type: Website
  url: https://www.meshy.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meshy.ai/
- group: commercial
  title: ''
  type: Plans
  url: plans/meshy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meshy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/meshy-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.meshy.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.meshy.ai/blog
created: '2026-05-08'
description: Meshy is an AI 3D model generation platform offering Text-to-3D, Image-to-3D, Multi Image-to-3D, Remesh, Rigging, Animation, Retexture, Text-to-Image, Image-to-Image, Multi-Color Print, Analyze Printability, and Repair Printability APIs. The Meshy REST API is at https://api.meshy.ai with bearer token authentication.
finops:
- name: Meshy Finops
  service_category: AI
  slug: meshy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/meshy.png
layout: provider
modified: '2026-05-08'
name: Meshy
nav: Providers
network: true
overview: 'Meshy publishes 2 APIs on the [APIs.io](https://apis.io/) network: Image to 3D API and Text to 3D API. Tagged areas include Artificial Intelligence, 3D, Generation, Texturing, and Animation.


  Meshy''s developer surface includes documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Meshy Plans Pricing
  plan_count: 4
  slug: meshy-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 7
  name: Meshy Rate Limits
  slug: meshy-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/meshy/refs/heads/main/screenshots/meshy-2026-06-20T185245.png
security:
- kind: domain-security
  name: Meshy Domain Security
  slug: meshy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Meshy Vulnerability Disclosure
  slug: meshy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: meshy
tags:
- Artificial Intelligence
- 3D
- Generation
- Texturing
- Animation
- Rigging
- Printing
website: https://www.meshy.ai/
---
