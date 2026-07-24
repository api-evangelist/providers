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
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: Search and retrieve royalty-free images, illustrations, and vectors. Filter by category, image type, orientation, color, and more. Returns image URLs at multiple resolutions.
  name: Pixabay Image API
  slug: images
- description: Search and retrieve royalty-free videos with multiple resolutions (large, medium, small, tiny) and dimensions metadata.
  name: Pixabay Video API
  slug: videos
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pixabay-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixabay-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Pixabay
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pixabay
- group: company
  title: ''
  type: Website
  url: https://pixabay.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pixabay.com/api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/pixabay-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pixabay-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/pixabay-finops.yml
created: '2026-05-08'
description: Pixabay is a free stock images, videos, illustrations, vectors, and music platform. The Pixabay API offers a public REST API for searching and retrieving free media assets. Authentication is via API key obtained on free signup.
finops:
- name: Pixabay Finops
  service_category: Stock Media
  slug: pixabay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixabay.png
layout: provider
modified: '2026-05-08'
name: Pixabay
nav: Providers
network: true
overview: Pixabay publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Stock Media, Images, Videos, Illustrations, and Free.
plans:
- name: Pixabay Plans Pricing
  plan_count: 1
  slug: pixabay-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 2
  name: Pixabay Rate Limits
  slug: pixabay-rate-limits
score:
  band: emerging
  composite: 20.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 20.2
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixabay/refs/heads/main/screenshots/pixabay-2026-06-20T191736.png
security:
- kind: domain-security
  name: Pixabay Domain Security
  slug: pixabay-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Pixabay Vulnerability Disclosure
  slug: pixabay-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: pixabay
tags:
- Stock Media
- Images
- Videos
- Illustrations
- Free
- Search
website: https://pixabay.com/
---
