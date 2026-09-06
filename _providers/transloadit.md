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
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Core REST API for creating and managing Assemblies (processing jobs), Templates, Template Credentials, Webhooks, Billing, and Queue monitoring. Uses bearer token authentication. Supports video encodin
  name: Transloadit API
  slug: transloadit-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/transloadit-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/transloadit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/transloadit-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://transloadit.com/
- group: docs
  title: ''
  type: Documentation
  url: https://transloadit.com/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/transloadit
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/transloadit
- group: company
  title: ''
  type: Blog
  url: https://transloadit.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://transloadit.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.transloadit.com/
- group: other
  title: ''
  type: X
  url: https://x.com/transloadit
- group: commercial
  title: ''
  type: Plans
  url: plans/transloadit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/transloadit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/transloadit-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://transloadit.com/blog.atom
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/transloadit-context.jsonld
created: '2026-06-12'
description: File processing and media handling API for encoding video, resizing images, extracting audio, generating thumbnails, and transcribing media via assembly instructions. Supports 94 robots for automation, browser-based uploads via Uppy, Smart CDN, and integrations with S3, Google Drive, and more.
finops:
- name: Transloadit Finops
  service_category: ''
  slug: transloadit-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for the Transloadit file uploading and media processing API. Transloadit provides a REST API for creating and managing Assemblies (processing jobs),
  name: Transloadit GraphQL Schema
  slug: transloadit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/transloadit.png
jsonld:
- class_count: 31
  name: Transloadit Context
  property_count: 3
  slug: transloadit-context
layout: provider
modified: '2026-06-12'
name: Transloadit
nav: Providers
network: true
overview: 'Transloadit publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include File Processing, Media Encoding, Video Transcoding, Image Resizing, and Audio Extraction.


  The Transloadit catalog on APIs.io includes 1 JSON-LD context.


  Transloadit''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Transloadit Plans Pricing
  plan_count: 6
  slug: transloadit-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Transloadit Rate Limits
  slug: transloadit-rate-limits
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 72.0
    catalog_earned_first_party: 0.0
    catalog_gap: 43.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 50.0
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 44.7
  previous_composite: 41.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/transloadit/refs/heads/main/screenshots/transloadit-2026-06-20T195627.png
security:
- kind: domain-security
  name: Transloadit Domain Security
  slug: transloadit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Transloadit Vulnerability Disclosure
  slug: transloadit-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Transloadit Trust Center
  slug: transloadit-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: transloadit
tags:
- File Processing
- Media Encoding
- Video Transcoding
- Image Resizing
- Audio Extraction
- Thumbnail Generation
- File Uploading
- Media API
website: https://transloadit.com/
---
