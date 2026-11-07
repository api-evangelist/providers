---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 24
  human_in_the_loop: 0
  name: Uploadcare Agentic Access
  operation_count: 44
  slug: uploadcare-agentic-access
  summary_line: 44 operations · 24 acting
api_count: 2
apis:
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: An `Add-On` is an application implemented by Uploadcare that accepts uploaded files as an input and can produce other files and/or [appdata](#operation/fileInfo) as an output.
  name: Uploadcare Add-Ons API
  slug: uploadcare-add-ons-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: The Conversion API from Uploadcare — 5 operation(s) for conversion.
  name: Uploadcare Conversion API
  slug: uploadcare-conversion-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: The File API from Uploadcare — 6 operation(s) for file.
  name: Uploadcare File API
  slug: uploadcare-file-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: 'There are a few ways to get information about uploaded file. One of them is on-the-fly with a request to CDN. Note: Other APIs also let you read file info: [after Upload](/docs/api/upload/upload/file-'
  name: Uploadcare File information API
  slug: uploadcare-file-information-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: File metadata is additional, arbitrary data, associated with uploaded file. As an example, you could store unique file identifier from your system. Metadata is key-value data. You can specify up to 50
  name: Uploadcare File metadata API
  slug: uploadcare-file-metadata-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: 'Your original filenames can be accessed via [REST API](/docs/api/rest/). Make a request to receive a JSON response with file parameters including `original_filename`. You can set an optional filename '
  name: Uploadcare File names API
  slug: uploadcare-file-names-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: The Group API from Uploadcare — 2 operation(s) for group.
  name: Uploadcare Group API
  slug: uploadcare-group-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: The Project API from Uploadcare — 1 operation(s) for project.
  name: Uploadcare Project API
  slug: uploadcare-project-api
- baseURL: https://api.uploadcare.com
  baseurl_source: declared
  description: The Webhook API from Uploadcare — 3 operation(s) for webhook.
  name: Uploadcare Webhook API
  slug: uploadcare-webhook-api
artifact_total: 38
collections:
- collection_type: open
  name: URL API Reference Add-Ons API
  slug: open-uploadcare-add-ons-api
- collection_type: open
  name: URL API Reference Add-Ons Conversion API
  slug: open-uploadcare-conversion-api
- collection_type: open
  name: URL API Reference Add-Ons File API
  slug: open-uploadcare-file-api
- collection_type: open
  name: URL API Reference Add-Ons File information API
  slug: open-uploadcare-file-information-api
- collection_type: open
  name: URL API Reference Add-Ons File metadata API
  slug: open-uploadcare-file-metadata-api
- collection_type: open
  name: URL API Reference Add-Ons File names API
  slug: open-uploadcare-file-names-api
- collection_type: open
  name: URL API Reference Add-Ons Group API
  slug: open-uploadcare-group-api
- collection_type: open
  name: URL API Reference Add-Ons Groups API
  slug: open-uploadcare-groups-api
- collection_type: open
  name: URL API Reference Add-Ons Project API
  slug: open-uploadcare-project-api
- collection_type: open
  name: URL API Reference Add-Ons Upload API
  slug: open-uploadcare-upload-api
- collection_type: open
  name: URL API Reference Add-Ons Webhook API
  slug: open-uploadcare-webhook-api
common:
- group: agent
  href: https://artifacts.apis.io/uploadcare/agentic-access/uploadcare-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/uploadcare-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/uploadcare/security/uploadcare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/uploadcare-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/uploadcare/security/uploadcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uploadcare-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/uploadcare/authentication/uploadcare-authentication.yml
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
  href: https://artifacts.apis.io/uploadcare/plans/uploadcare-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/uploadcare-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/uploadcare/rate-limits/uploadcare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/uploadcare-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/uploadcare/finops/uploadcare-finops.yml
  title: ''
  type: FinOps
  url: finops/uploadcare-finops.yml
- group: design
  href: https://artifacts.apis.io/uploadcare/vocabulary/uploadcare-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/uploadcare-vocabulary.yml
- group: docs
  href: https://artifacts.apis.io/uploadcare/json-schema/uploadcare-file.json
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-file.json
- group: docs
  href: https://artifacts.apis.io/uploadcare/json-schema/uploadcare-group.json
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-group.json
- group: docs
  href: https://artifacts.apis.io/uploadcare/json-schema/uploadcare-project.json
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-project.json
- group: docs
  href: https://artifacts.apis.io/uploadcare/json-schema/uploadcare-webhook.json
  title: ''
  type: JSONSchema
  url: json-schema/uploadcare-webhook.json
- group: design
  href: https://artifacts.apis.io/uploadcare/json-ld/uploadcare-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/uploadcare-context.jsonld
- group: company
  title: ''
  type: BlogRSS
  url: https://uploadcare.com/blog/rss.xml
created: 2026-06-12
description: Uploadcare is a file uploading and processing platform that provides REST APIs for file management, CDN delivery, image transformations, document conversion, video encoding, and malware scanning. Developers can integrate file upload widgets, manage files and metadata, apply on-the-fly image transformations via URL-based CDN API, handle multipart uploads for large files, configure webhooks, and leverage add-ons for extended processing capabilities.
finops:
- has_sources: false
  method: generated
  name: Uploadcare Finops
  primary_unit: ''
  service_category: ''
  slug: uploadcare-finops
  template: true
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
overview: 'Uploadcare publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Add-Ons API, Conversion API, File API, and 6 more. Tagged areas include File Upload, File Management, CDN, Image Transformation, and Document Conversion.


  The Uploadcare catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Uploadcare''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Uploadcare Plans Pricing
  plan_count: 4
  slug: uploadcare-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Uploadcare Rate Limits
  slug: uploadcare-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Uploadcare — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: uploadcare-jsonschema-spectral-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 58.8
    catalog_earned_first_party: 0.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 18.4
    contract_governance: 23.5
    contract_quality: 58.9
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 31.6
  previous_composite: 37.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/uploadcare/uploadcare-2026-06-20T200444.png
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
- Webhook
website: https://uploadcare.com/
---
