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
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Imagekit Agentic Access
  operation_count: 48
  slug: imagekit-agentic-access
  summary_line: 48 operations · 32 acting
api_count: 12
apis:
- description: The Account Management API API from ImageKit — 5 operation(s) for account management api.
  name: ImageKit Account Management API API
  slug: imagekit-account-management-api-api
- description: The Caching API from ImageKit — 2 operation(s) for caching.
  name: ImageKit Caching API
  slug: imagekit-caching-api
- description: The Custom metadata fields API from ImageKit — 2 operation(s) for custom metadata fields.
  name: ImageKit Custom metadata fields API
  slug: imagekit-custom-metadata-fields-api
- description: The Digital Asset Management (DAM) API from ImageKit — 22 operation(s) for digital asset management (dam).
  name: ImageKit Digital Asset Management (DAM) API
  slug: imagekit-digital-asset-management-dam-api
- description: The Dummy Test API from ImageKit — 1 operation(s) for dummy test.
  name: ImageKit Dummy Test API
  slug: imagekit-dummy-test-api
- description: The File Metadata API from ImageKit — 2 operation(s) for file metadata.
  name: ImageKit File Metadata API
  slug: imagekit-file-metadata-api
- description: The Managing assets API from ImageKit — 12 operation(s) for managing assets.
  name: ImageKit Managing assets API
  slug: imagekit-managing-assets-api
- description: The Managing folders API from ImageKit — 5 operation(s) for managing folders.
  name: ImageKit Managing folders API
  slug: imagekit-managing-folders-api
- description: The Origins API from ImageKit — 2 operation(s) for origins.
  name: ImageKit Origins API
  slug: imagekit-origins-api
- description: The Saved Extensions API from ImageKit — 2 operation(s) for saved extensions.
  name: ImageKit Saved Extensions API
  slug: imagekit-saved-extensions-api
- description: The Upload File API from ImageKit — 2 operation(s) for upload file.
  name: ImageKit Upload File API
  slug: imagekit-upload-file-api
- description: The URL endpoints API from ImageKit — 2 operation(s) for url endpoints.
  name: ImageKit URL endpoints API
  slug: imagekit-url-endpoints-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ImageKit Account Management API API
  slug: open-imagekit-account-management-api-api
- collection_type: open
  name: ImageKit Account Management API Caching API
  slug: open-imagekit-caching-api
- collection_type: open
  name: ImageKit Account Management API Custom metadata fields API
  slug: open-imagekit-custom-metadata-fields-api
- collection_type: open
  name: ImageKit Account Management API Digital Asset Management (DAM) API
  slug: open-imagekit-digital-asset-management-dam-api
- collection_type: open
  name: ImageKit Account Management API Dummy Test API
  slug: open-imagekit-dummy-test-api
- collection_type: open
  name: ImageKit Account Management API File Metadata API
  slug: open-imagekit-file-metadata-api
- collection_type: open
  name: ImageKit Account Management API Managing assets API
  slug: open-imagekit-managing-assets-api
- collection_type: open
  name: ImageKit Account Management API Managing folders API
  slug: open-imagekit-managing-folders-api
- collection_type: open
  name: ImageKit Account Management API Origins API
  slug: open-imagekit-origins-api
- collection_type: open
  name: ImageKit Account Management API Saved Extensions API
  slug: open-imagekit-saved-extensions-api
- collection_type: open
  name: ImageKit Account Management API Upload File API
  slug: open-imagekit-upload-file-api
- collection_type: open
  name: ImageKit Account Management API URL endpoints API
  slug: open-imagekit-url-endpoints-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/imagekit-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/imagekit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/imagekit-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://imagekit.io/
- group: docs
  title: ''
  type: Documentation
  url: https://imagekit.io/docs
- group: build
  title: ''
  type: GitHub
  url: https://github.com/imagekit-developer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/imagekit-io
- group: company
  title: ''
  type: Blog
  url: https://imagekit.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://imagekit.io/plans/
- group: operate
  title: ''
  type: StatusPage
  url: https://imagekitio.statuspage.io/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ImagekitIo
- group: commercial
  title: ''
  type: Plans
  url: plans/imagekit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/imagekit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/imagekit-finops.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://imagekit.io/blog/rss.xml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/imagekit-vocabulary.yml
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/imagekit-context.jsonld
created: '2026-06-12'
description: Real-time image and video optimization CDN with a REST API for media management, transformations, folder operations, and performance analytics. ImageKit provides a unified URL-based API with 50+ transformations, intelligent format optimization, compression, and an integrated Digital Asset Management (DAM) platform for managing and delivering media at scale.
examples:
- key_count: 2
  name: Imagekit Bulk Add Tags
  slug: imagekit-bulk-add-tags
- key_count: 2
  name: Imagekit Custom Metadata Field
  slug: imagekit-custom-metadata-field
- key_count: 3
  name: Imagekit List Files Request
  slug: imagekit-list-files-request
- key_count: 2
  name: Imagekit Purge Cache Request
  slug: imagekit-purge-cache-request
- key_count: 2
  name: Imagekit Upload File Response
  slug: imagekit-upload-file-response
- key_count: 3
  name: Imagekit Upload File
  slug: imagekit-upload-file
finops:
- name: Imagekit Finops
  service_category: ''
  slug: imagekit-finops
graphqls:
- description: This is a conceptual GraphQL schema for ImageKit, the real-time image and video optimization CDN and Digital Asset Management (DAM) platform. ImageKit does not currently expose a public GraphQL API; i
  name: ImageKit GraphQL Schema
  slug: imagekit-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/imagekit.png
json_schemas:
- name: CustomMetadataField
  property_count: 4
  slug: imagekit-custommetadatafield
- name: File & File Version
  property_count: 28
  slug: imagekit-filedetails
- name: FileUploadV1
  property_count: 23
  slug: imagekit-fileuploadv1
- name: FileUploadV2
  property_count: 20
  slug: imagekit-fileuploadv2
- name: Folder
  property_count: 7
  slug: imagekit-folderdetails
- name: Async Bulk Job Response
  property_count: 1
  slug: imagekit-jobresponse
- name: Metadata
  property_count: 14
  slug: imagekit-metadata
- name: Saved Extension
  property_count: 6
  slug: imagekit-savedextension
- name: Upload
  property_count: 25
  slug: imagekit-upload
- name: VersionInfo
  property_count: 2
  slug: imagekit-versioninfo
jsonld:
- class_count: 0
  name: Imagekit Context
  property_count: 50
  slug: imagekit-context
layout: provider
modified: '2026-06-12'
name: ImageKit
nav: Providers
network: true
overview: 'ImageKit publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Account Management API API, Caching API, Custom metadata fields API, and 9 more. Tagged areas include Images, Video, CDN, Media, and Optimization.


  The ImageKit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ImageKit''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Imagekit Plans Pricing
  plan_count: 7
  slug: imagekit-plans-pricing
random_paper: 98
rate_limits:
- limit_count: 5
  name: Imagekit Rate Limits
  slug: imagekit-rate-limits
rules:
- name: ImageKit API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: imagekit-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 71.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/imagekit/refs/heads/main/screenshots/imagekit-2026-06-20T183243.png
security:
- kind: authentication
  name: Imagekit Authentication
  slug: imagekit-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Imagekit Domain Security
  slug: imagekit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: imagekit
tags:
- Images
- Video
- CDN
- Media
- Optimization
- Transformations
- Digital Asset Management
- DAM
- Storage
- Cache
- Upload
website: https://imagekit.io/
---
