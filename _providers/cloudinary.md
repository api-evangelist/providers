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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Cloudinary Agentic Access
  operation_count: 8
  slug: cloudinary-agentic-access
  summary_line: 8 operations · 7 acting
api_count: 9
apis:
- description: The Admin API supports bulk asset management (search, retrieval, update, delete, restore), and CRUD management of folders, metadata fields, metadata rules, upload presets, transformations, streaming p
  name: Cloudinary Admin API
  slug: admin
- description: The Search API exposes Lucene-style query expressions across asset metadata, tags, contextual metadata, structured metadata, and AI-derived tags. Supports sorting, aggregation, pagination via cursors,
  name: Cloudinary Search API
  slug: search
- description: The Provisioning API enables enterprise account-level management of product environments (sub-accounts), users, user groups, and API keys. Authentication uses provisioning API key and secret. Useful f
  name: Cloudinary Provisioning API
  slug: provisioning
- description: The Permissions API assigns granular permissions to principals (users, groups, API keys) by roles or directly. Supports folder-scoped, asset- scoped, and product-environment-scoped permission grants a
  name: Cloudinary Permissions API
  slug: permissions
- description: The Transformation URL API delivers and transforms images and videos by composing parameters into the delivery URL path (/{cloud_name}/{resource_type}/{type}/{transformations}/{public_id}). Supports r
  name: Cloudinary Transformation URL API
  slug: transformations
- description: Cloudinary fires HTTP webhook notifications for upload completion, eager transformation completion, AI moderation outcomes, asset deletion, and backup events. Notifications include signatures for veri
  name: Cloudinary Notifications and Webhooks
  slug: notifications
- description: Backup retrieval operations.
  name: Cloudinary Backup API
  slug: cloudinary-backup-api
- description: Apply transformations to existing assets.
  name: Cloudinary Transformation API
  slug: cloudinary-transformation-api
- description: Asset upload and management.
  name: Cloudinary Upload API
  slug: cloudinary-upload-api
artifact_total: 45
asyncapis:
- description: 'AsyncAPI description of Cloudinary''s outbound notification (webhook) surface. Cloudinary delivers event notifications by issuing HTTP POST requests with a JSON body to a notification URL the customer '
  name: Cloudinary Notifications
  slug: cloudinary-notifications-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cloudinary Upload Backup API
  slug: open-cloudinary-backup-api
- collection_type: open
  name: Cloudinary Upload Backup Transformation API
  slug: open-cloudinary-transformation-api
- collection_type: open
  name: Cloudinary Backup Upload API
  slug: open-cloudinary-upload-api
- collection_type: open
  name: Cloudinary Upload API
  slug: open-cloudinary
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cloudinary-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cloudinary-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cloudinary-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cloudinary
- group: company
  title: ''
  type: Website
  url: https://cloudinary.com/
- group: start
  title: ''
  type: Portal
  url: https://console.cloudinary.com/
- group: docs
  title: ''
  type: Documentation
  url: https://cloudinary.com/documentation
- group: start
  title: ''
  type: Signup
  url: https://cloudinary.com/users/register_free
- group: commercial
  title: ''
  type: Pricing
  url: https://cloudinary.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloudinary.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/cloudinary
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cloudinary.com/tos
- group: commercial
  title: ''
  type: Privacy
  url: https://cloudinary.com/privacy
- group: agent
  title: ''
  type: LlmsText
  url: https://cloudinary.com/llms.txt
created: '2024-11-13'
description: Cloudinary is a cloud-based service that provides comprehensive solutions for managing digital media assets, including images and videos, for websites and mobile applications. The platform exposes REST APIs for uploading and transforming media, administering assets and product environments, provisioning users and accounts, and configuring granular permissions. APIs use Basic Authentication with API key and secret over HTTPS.
features:
- 'Free: 25 monthly credits with all core features'
- 'Plus at $99/mo: 225 credits, S3 backup, auto-tagging'
- 'Advanced at $249/mo: 600 credits, custom domain, SSL'
- 'Enterprise: custom credits, multi-CDN, dedicated CSM'
- Credits = sum of transformations + storage + bandwidth
- Image and video transformation API
- URL-based on-the-fly transformations
- Video transcoding and adaptive bitrate streaming
- Upload API with auto-tagging
- 'Admin API: 500 req/hr Free, 2K req/hr Paid'
- Bulk delete up to 1,000 resources/request
- AI-powered transformations (background removal, generative fill)
- Auto-format and auto-quality for delivery
- Programmable Media SDKs (JS, mobile, server)
- Digital Asset Management (DAM) with workflows
- Multi-CDN delivery (Akamai + Fastly + others on Enterprise)
finops:
- name: Cloudinary Finops
  service_category: Media Cloud
  slug: cloudinary-finops
graphqls:
- description: Cloudinary does not currently expose a public GraphQL API. This conceptual schema represents the domain model of Cloudinary's media management and transformation platform, derived from their REST APIs
  name: Cloudinary GraphQL Schema
  slug: cloudinary-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cloudinary.png
json_schemas:
- name: Asset
  property_count: 6
  slug: cloudinary-asset
- name: GenericRequest
  property_count: 0
  slug: cloudinary-genericrequest
- name: GenericResponse
  property_count: 0
  slug: cloudinary-genericresponse
- name: UploadRequest
  property_count: 5
  slug: cloudinary-uploadrequest
json_structures:
- name: Cloudinary Structure
  property_count: 0
  slug: cloudinary-structure
layout: provider
modified: '2026-05-30'
name: Cloudinary
nav: Providers
network: true
overview: 'Cloudinary publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Notifications and Webhooks, Backup API, Transformation API, and 1 more. Tagged areas include Asset Management, Digital Asset Management, Image Processing, Image Transformation, and Media.


  The Cloudinary catalog on APIs.io includes 1 event-driven AsyncAPI specification and 2 Spectral governance rulesets.


  Cloudinary''s developer surface includes authentication, developer portal, documentation, signup flow, pricing, GitHub presence, privacy policy, and 7 more developer resources.'
plans:
- name: Cloudinary Plans Pricing
  plan_count: 4
  slug: cloudinary-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 4
  name: Cloudinary Rate Limits
  slug: cloudinary-rate-limits
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Cloudinary API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: cloudinary-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Cloudinary API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: cloudinary-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: 2.4
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 13.6
    contract_quality: 64.9
    developer_ergonomics: 42.9
    discoverability: 72.2
    governance: 13.6
    operational_transparency: 28.9
  previous_composite: 47.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cloudinary/refs/heads/main/screenshots/cloudinary-2026-06-20T174606.png
security:
- kind: authentication
  name: Cloudinary Authentication
  slug: cloudinary-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Cloudinary Domain Security
  slug: cloudinary-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cloudinary
tags:
- Asset Management
- Digital Asset Management
- Image Processing
- Image Transformation
- Media
- Software-as-a-Service
- Video Processing
website: https://cloudinary.com/
---
