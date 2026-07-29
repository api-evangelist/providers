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
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Imgbb Agentic Access
  operation_count: 2
  slug: imgbb-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 1
apis:
- description: The Images API from ImgBB — 1 operation(s) for images.
  name: ImgBB Images API
  slug: imgbb-images-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imgbb-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imgbb-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imgbb-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://imgbb.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.imgbb.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://imgbb.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://imgbb.com/page/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://imgbb.com/page/privacy_policy
- group: commercial
  title: ''
  type: Plans
  url: plans/imgbb-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imgbb-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imgbb-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/imgbb-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/imgbb-jsonld.json
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: '2026-06-13'
description: ImgBB is a free image hosting and sharing platform with a REST API for uploading images, retrieving shareable links, managing expiration, and accessing image metadata. Supports binary file upload, base64-encoded data, and image URLs up to 32 MB. The API returns direct image links, viewer page URLs, thumbnail URLs, and delete URLs in JSON. No registration is required to use the basic hosting service, but an API key is required for programmatic uploads via the v1 REST API.
examples:
- key_count: 4
  name: Upload Image Base64
  slug: upload-image-base64
- key_count: 4
  name: Upload Image Post
  slug: upload-image-post
- key_count: 4
  name: Upload Image Url
  slug: upload-image-url
finops:
- name: Imgbb Finops
  service_category: ''
  slug: imgbb-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imgbb.png
json_schemas:
- name: ImgBB Upload Request
  property_count: 4
  slug: upload-request
- name: ImgBB Upload Response
  property_count: 3
  slug: upload-response
layout: provider
modified: '2026-06-13'
name: ImgBB
nav: Providers
network: true
overview: 'ImgBB publishes 1 API on the [APIs.io](https://apis.io/) network: Images API. Tagged areas include Image Hosting, Image Upload, File Sharing, Cloud Storage, and Media.


  The ImgBB catalog on APIs.io includes 1 Spectral governance ruleset.


  ImgBB''s developer surface includes authentication, documentation, pricing, engineering blog, and 10 more developer resources.'
plans:
- name: Imgbb Plans Pricing
  plan_count: 4
  slug: imgbb-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Imgbb Rate Limits
  slug: imgbb-rate-limits
rules:
- name: ImgBB API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: imgbb-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.4
  delta: -4.7
  facets:
    commercial_clarity: 71.1
    contract_quality: 72.0
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 59.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imgbb/refs/heads/main/screenshots/imgbb-2026-06-20T183249.png
security:
- kind: authentication
  name: Imgbb Authentication
  slug: imgbb-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Imgbb Domain Security
  slug: imgbb-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imgbb
tags:
- Image Hosting
- Image Upload
- File Sharing
- Cloud Storage
- Media
- REST API
website: https://imgbb.com/
---
