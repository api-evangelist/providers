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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Uploadcare Agentic Access
  operation_count: 44
  slug: uploadcare-agentic-access
  summary_line: 44 operations · 24 acting
api_count: 11
apis:
- description: Upload API for direct binary file uploads, multipart uploads for large files (up to 5 TB), URL-based uploads, UUID-based uploads, and file group creation. Supports direct uploads from browser or serve
  name: Uploadcare Upload API
  slug: upload-api
- description: An `Add-On` is an application implemented by Uploadcare that accepts uploaded files as an input and can produce other files and/or [appdata](#operation/fileInfo) as an output.
  name: Uploadcare Add-Ons API
  slug: uploadcare-add-ons-api
- description: The Conversion API from Uploadcare — 5 operation(s) for conversion.
  name: Uploadcare Conversion API
  slug: uploadcare-conversion-api
- description: The File API from Uploadcare — 6 operation(s) for file.
  name: Uploadcare File API
  slug: uploadcare-file-api
- description: 'There are a few ways to get information about uploaded file. One of them is on-the-fly with a request to CDN. Note: Other APIs also let you read file info: [after Upload](/docs/api/upload/upload/file-'
  name: Uploadcare File information API
  slug: uploadcare-file-information-api
- description: File metadata is additional, arbitrary data, associated with uploaded file. As an example, you could store unique file identifier from your system. Metadata is key-value data. You can specify up to 50
  name: Uploadcare File metadata API
  slug: uploadcare-file-metadata-api
- description: 'Your original filenames can be accessed via [REST API](/docs/api/rest/). Make a request to receive a JSON response with file parameters including `original_filename`. You can set an optional filename '
  name: Uploadcare File names API
  slug: uploadcare-file-names-api
- description: The Group API from Uploadcare — 2 operation(s) for group.
  name: Uploadcare Group API
  slug: uploadcare-group-api
- description: The Groups API from Uploadcare — 2 operation(s) for groups.
  name: Uploadcare Groups API
  slug: uploadcare-groups-api
- description: The Project API from Uploadcare — 1 operation(s) for project.
  name: Uploadcare Project API
  slug: uploadcare-project-api
- description: The Webhook API from Uploadcare — 3 operation(s) for webhook.
  name: Uploadcare Webhook API
  slug: uploadcare-webhook-api
artifact_total: 30
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/uploadcare-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uploadcare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uploadcare-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uploadcare-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://uploadcare.com/
- group: docs
  title: ''
  type: Documentation
  url: https://uploadcare.com/docs/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/uploadcare
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uploadcare
- group: company
  title: ''
  type: Blog
  url: https://uploadcare.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://uploadcare.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uploadcare.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/uploadcare
- group: commercial
  title: ''
  type: Plans
  url: plans/uploadcare-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uploadcare-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uploadcare-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/uploadcare-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-file.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-group.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-project.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-webhook.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/uploadcare-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://uploadcare.com/blog/rss.xml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
created: 2026-06-12
description: Uploadcare is a file uploading and processing platform that provides REST APIs for file management, CDN delivery, image transformations, document conversion, video encoding, and malware scanning. Developers can integrate file upload widgets, manage files and metadata, apply on-the-fly image transformations via URL-based CDN API, handle multipart uploads for large files, configure webhooks, and leverage add-ons for extended processing capabilities.
finops:
- name: Uploadcare Finops
  service_category: ''
  slug: uploadcare-finops
graphqls:
- description: This is a conceptual GraphQL schema for the [Uploadcare](https://uploadcare.com/) platform, derived from the [Uploadcare REST API](https://uploadcare.com/api-refs/rest-api/), the [Upload API](https://
  name: Uploadcare GraphQL Schema
  slug: uploadcare-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uploadcare.png
json_schemas:
- name: Uploadcare Applicationdata
  property_count: 4
  slug: uploadcare-applicationdata
- name: Uploadcare Contentinfo
  property_count: 3
  slug: uploadcare-contentinfo
- name: Uploadcare File
  property_count: 15
  slug: uploadcare-file
- name: Uploadcare Group
  property_count: 5
  slug: uploadcare-group
- name: Uploadcare Imageinfo
  property_count: 9
  slug: uploadcare-imageinfo
- name: Uploadcare Metadata
  property_count: 0
  slug: uploadcare-metadata
- name: Uploadcare Project
  property_count: 4
  slug: uploadcare-project
- name: Uploadcare Videoinfo
  property_count: 5
  slug: uploadcare-videoinfo
- name: Uploadcare Webhook
  property_count: 9
  slug: uploadcare-webhook
jsonld:
- class_count: 37
  name: Uploadcare Context
  property_count: 22
  slug: uploadcare-context
layout: provider
modified: 2026-06-12
name: Uploadcare
nav: Providers
network: true
overview: 'Uploadcare publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Upload API, Add-Ons API, Conversion API, and 8 more. Tagged areas include File Upload, File Management, CDN, Image Transformation, and Document Conversion.


  The Uploadcare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Uploadcare''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 18 more developer resources.'
plans:
- name: Uploadcare Plans Pricing
  plan_count: 4
  slug: uploadcare-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 0
  name: Uploadcare Rate Limits
  slug: uploadcare-rate-limits
rules:
- name: Uploadcare API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uploadcare-jsonschema-spectral-rules
score:
  band: developing
  composite: 53.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 64.9
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 86.8
    operational_transparency: 21.1
  previous_composite: 53.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uploadcare/refs/heads/main/screenshots/uploadcare-2026-06-20T200444.png
security:
- kind: authentication
  name: Uploadcare Authentication
  slug: uploadcare-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Uploadcare Domain Security
  slug: uploadcare-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Uploadcare Vulnerability Disclosure
  slug: uploadcare-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: uploadcare
tags:
- File Upload
- File Management
- CDN
- Image Transformation
- Document Conversion
- Video Encoding
- Malware Scanning
- Storage
- Webhooks
website: https://uploadcare.com/
---
