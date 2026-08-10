---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Cloudimage Agentic Access
  operation_count: 9
  slug: cloudimage-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 3
apis:
- description: Upload and asset-management REST endpoints.
  name: Cloudimage Filerobot DAM API
  slug: cloudimage-filerobot-dam-api
- description: URL-based image transformation operations.
  name: Cloudimage Image API
  slug: cloudimage-image-api
- description: URL-based video transformation and transcoding operations.
  name: Cloudimage Video API
  slug: cloudimage-video-api
artifact_total: 10
collections:
- collection_type: open
  name: Cloudimage API
  slug: open-cloudimage
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudimage-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudimage-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudimage-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/scaleflex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scaleflex
- group: company
  title: ''
  type: Website
  url: https://www.cloudimage.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloudimage.io/
- group: commercial
  title: ''
  type: Plans
  url: plans/cloudimage-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cloudimage-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cloudimage-finops.yml
created: '2026-06-20'
description: Cloudimage (by Scaleflex) is an image and video optimization, resizing, and CDN service. Its core interface is a URL-based transformation API - you request an origin image through https://{token}.cloudimg.io/{origin-url} and apply resize, crop, format, compression, filter, and watermark operations via query parameters, delivered over a global multi-CDN. A companion Filerobot DAM provides a REST upload and asset-management API.
finops:
- name: Cloudimage Finops
  service_category: Content Delivery and Media Optimization
  slug: cloudimage-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudimage.png
layout: provider
modified: '2026-06-20'
name: Cloudimage
nav: Providers
network: true
overview: 'Cloudimage publishes 3 APIs on the [APIs.io](https://apis.io/) network: Filerobot DAM API, Image API, and Video API. Tagged areas include Image Optimization, Image CDN, Resizing, Transformation, and DAM.


  Cloudimage''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Cloudimage Plans Pricing
  plan_count: 4
  slug: cloudimage-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Cloudimage Rate Limits
  slug: cloudimage-rate-limits
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 60.6
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudimage/refs/heads/main/screenshots/cloudimage-2026-06-20T174604.png
security:
- kind: authentication
  name: Cloudimage Authentication
  slug: cloudimage-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Cloudimage Domain Security
  slug: cloudimage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cloudimage
tags:
- Image Optimization
- Image CDN
- Resizing
- Transformation
- DAM
website: https://www.cloudimage.io/
---
