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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 17
  human_in_the_loop: 1
  name: Lightroom Agentic Access
  operation_count: 37
  slug: lightroom-agentic-access
  summary_line: 37 operations · 17 acting · 1 human-in-the-loop
api_count: 12
apis:
- description: Manage assets within albums
  name: Adobe Lightroom Album Assets API
  slug: lightroom-album-assets-api
- description: CRUD operations on albums
  name: Adobe Lightroom Albums API
  slug: lightroom-albums-api
- description: CRUD operations on photo and video assets
  name: Adobe Lightroom Assets API
  slug: lightroom-assets-api
- description: Automatically detect and correct image horizon alignment
  name: Adobe Lightroom Auto Straighten API
  slug: lightroom-auto-straighten-api
- description: Automatically adjust tonal values for optimal exposure and contrast
  name: Adobe Lightroom Auto Tone API
  slug: lightroom-auto-tone-api
- description: Catalog metadata and configuration
  name: Adobe Lightroom Catalog API
  slug: lightroom-catalog-api
- description: Apply custom Lightroom edit settings to images
  name: Adobe Lightroom Edit Image API
  slug: lightroom-edit-image-api
- description: API health and availability checks
  name: Adobe Lightroom Health API
  slug: lightroom-health-api
- description: Upload and manage original master files
  name: Adobe Lightroom Master API
  slug: lightroom-master-api
- description: Apply Lightroom presets (XMP develop settings) to images
  name: Adobe Lightroom Presets API
  slug: lightroom-presets-api
- description: Retrieve generated renditions (previews and thumbnails)
  name: Adobe Lightroom Renditions API
  slug: lightroom-renditions-api
- description: Read and write external develop XMP sidecar files
  name: Adobe Lightroom XMP API
  slug: lightroom-xmp-api
artifact_total: 166
collections:
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets API
  slug: postman-lightroom-album-assets-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Album Assets Albums API
  slug: postman-lightroom-albums-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets API
  slug: postman-lightroom-assets-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Auto Straighten API
  slug: postman-lightroom-auto-straighten-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Auto Tone API
  slug: postman-lightroom-auto-tone-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Catalog API
  slug: postman-lightroom-catalog-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Edit Image API
  slug: postman-lightroom-edit-image-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Health API
  slug: postman-lightroom-health-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Master API
  slug: postman-lightroom-master-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Presets API
  slug: postman-lightroom-presets-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets Renditions API
  slug: postman-lightroom-renditions-api
- collection_type: postman
  name: Adobe Lightroom Lightroom Albums Album Assets XMP API
  slug: postman-lightroom-xmp-api
- collection_type: open
  name: Adobe Lightroom Lightroom Albums API
  slug: open-lightroom-albums
- collection_type: open
  name: Adobe Lightroom Lightroom Assets API
  slug: open-lightroom-assets
- collection_type: open
  name: Adobe Lightroom Lightroom Catalog API
  slug: open-lightroom-catalog
- collection_type: open
  name: Adobe Lightroom API (Firefly Services)
  slug: open-lightroom-firefly-services
- collection_type: open
  name: Adobe Lightroom Lightroom Services API
  slug: open-lightroom-services
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-lightroom/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/lightroom-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lightroom-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lightroom-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/lightroom-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/lightroom-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/lightroom/lightroom-api-docs/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/console
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adobe.com/lightroom/lightroom-api-docs/release-notes/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AdobeDocs/lightroom-public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs
- group: build
  title: ''
  type: SDKs
  url: https://developer.adobe.com/firefly-services/docs/lightroom/
created: '2024-01-01'
description: APIs for Adobe Lightroom cloud services, enabling developers to access and manipulate photos, albums, and metadata programmatically. The Lightroom APIs are also available as part of Adobe Firefly Services for AI-powered image editing operations such as auto tone, auto straighten, and preset application.
examples:
- key_count: 1
  name: Lightroom Albums Album Assets Request Example
  slug: lightroom-albums-album-assets-request-example
- key_count: 2
  name: Lightroom Albums Album Create Request Example
  slug: lightroom-albums-album-create-request-example
- key_count: 5
  name: Lightroom Albums Album Example
  slug: lightroom-albums-album-example
- key_count: 5
  name: Lightroom Albums Album Payload Example
  slug: lightroom-albums-album-payload-example
- key_count: 6
  name: Lightroom Albums Album Response Example
  slug: lightroom-albums-album-response-example
- key_count: 2
  name: Lightroom Albums Albums List Response Example
  slug: lightroom-albums-albums-list-response-example
- key_count: 2
  name: Lightroom Albums Assets List Response Example
  slug: lightroom-albums-assets-list-response-example
- key_count: 2
  name: Lightroom Albums Error Response Example
  slug: lightroom-albums-error-response-example
- key_count: 0
  name: Lightroom Albums Links Example
  slug: lightroom-albums-links-example
- key_count: 2
  name: Lightroom Assets Asset Create Request Example
  slug: lightroom-assets-asset-create-request-example
- key_count: 6
  name: Lightroom Assets Asset Example
  slug: lightroom-assets-asset-example
- key_count: 7
  name: Lightroom Assets Asset Payload Example
  slug: lightroom-assets-asset-payload-example
- key_count: 6
  name: Lightroom Assets Asset Response Example
  slug: lightroom-assets-asset-response-example
- key_count: 2
  name: Lightroom Assets Assets List Response Example
  slug: lightroom-assets-assets-list-response-example
- key_count: 2
  name: Lightroom Assets Error Response Example
  slug: lightroom-assets-error-response-example
- key_count: 0
  name: Lightroom Assets Links Example
  slug: lightroom-assets-links-example
- key_count: 7
  name: Lightroom Catalog Catalog Response Example
  slug: lightroom-catalog-catalog-response-example
- key_count: 2
  name: Lightroom Catalog Error Response Example
  slug: lightroom-catalog-error-response-example
- key_count: 2
  name: Lightroom Firefly Services Apply Presets Request Example
  slug: lightroom-firefly-services-apply-presets-request-example
- key_count: 2
  name: Lightroom Firefly Services Auto Straighten Request Example
  slug: lightroom-firefly-services-auto-straighten-request-example
- key_count: 2
  name: Lightroom Firefly Services Auto Tone Request Example
  slug: lightroom-firefly-services-auto-tone-request-example
- key_count: 3
  name: Lightroom Firefly Services Edit Image Request Example
  slug: lightroom-firefly-services-edit-image-request-example
- key_count: 4
  name: Lightroom Firefly Services Error Response Example
  slug: lightroom-firefly-services-error-response-example
- key_count: 5
  name: Lightroom Firefly Services Job Response Example
  slug: lightroom-firefly-services-job-response-example
- key_count: 2
  name: Lightroom Firefly Services Storage Input Example
  slug: lightroom-firefly-services-storage-input-example
- key_count: 5
  name: Lightroom Firefly Services Storage Output Example
  slug: lightroom-firefly-services-storage-output-example
- key_count: 1
  name: Lightroom Services Album Assets Request Example
  slug: lightroom-services-album-assets-request-example
- key_count: 2
  name: Lightroom Services Album Create Request Example
  slug: lightroom-services-album-create-request-example
- key_count: 6
  name: Lightroom Services Album Example
  slug: lightroom-services-album-example
- key_count: 7
  name: Lightroom Services Album Response Example
  slug: lightroom-services-album-response-example
- key_count: 2
  name: Lightroom Services Albums List Response Example
  slug: lightroom-services-albums-list-response-example
- key_count: 7
  name: Lightroom Services Asset Example
  slug: lightroom-services-asset-example
- key_count: 7
  name: Lightroom Services Asset Response Example
  slug: lightroom-services-asset-response-example
- key_count: 2
  name: Lightroom Services Asset Revision Request Example
  slug: lightroom-services-asset-revision-request-example
- key_count: 2
  name: Lightroom Services Assets List Response Example
  slug: lightroom-services-assets-list-response-example
- key_count: 6
  name: Lightroom Services Catalog Response Example
  slug: lightroom-services-catalog-response-example
- key_count: 3
  name: Lightroom Services Error Response Example
  slug: lightroom-services-error-response-example
- key_count: 1
  name: Lightroom Services Health Response Example
  slug: lightroom-services-health-response-example
- key_count: 0
  name: Lightroom Services Links Example
  slug: lightroom-services-links-example
finops:
- name: Lightroom Finops
  service_category: API
  slug: lightroom-finops
image: /assets/icons/lightroom.png
json_schemas:
- name: Lightroom Album
  property_count: 7
  slug: lightroom-album
- name: AlbumAssetsRequest
  property_count: 1
  slug: lightroom-albums-album-assets-request
- name: AlbumCreateRequest
  property_count: 2
  slug: lightroom-albums-album-create-request
- name: AlbumPayload
  property_count: 5
  slug: lightroom-albums-album-payload
- name: AlbumResponse
  property_count: 6
  slug: lightroom-albums-album-response
- name: Album
  property_count: 5
  slug: lightroom-albums-album
- name: AlbumsListResponse
  property_count: 2
  slug: lightroom-albums-albums-list-response
- name: AssetsListResponse
  property_count: 2
  slug: lightroom-albums-assets-list-response
- name: ErrorResponse
  property_count: 2
  slug: lightroom-albums-error-response
- name: Links
  property_count: 0
  slug: lightroom-albums-links
- name: Lightroom Asset
  property_count: 8
  slug: lightroom-asset
- name: AssetCreateRequest
  property_count: 2
  slug: lightroom-assets-asset-create-request
- name: AssetPayload
  property_count: 7
  slug: lightroom-assets-asset-payload
- name: AssetResponse
  property_count: 6
  slug: lightroom-assets-asset-response
- name: Asset
  property_count: 6
  slug: lightroom-assets-asset
- name: AssetsListResponse
  property_count: 2
  slug: lightroom-assets-assets-list-response
- name: ErrorResponse
  property_count: 2
  slug: lightroom-assets-error-response
- name: Links
  property_count: 0
  slug: lightroom-assets-links
- name: CatalogResponse
  property_count: 7
  slug: lightroom-catalog-catalog-response
- name: ErrorResponse
  property_count: 2
  slug: lightroom-catalog-error-response
- name: Lightroom Catalog
  property_count: 6
  slug: lightroom-catalog
- name: ApplyPresetsRequest
  property_count: 2
  slug: lightroom-firefly-services-apply-presets-request
- name: AutoStraightenRequest
  property_count: 2
  slug: lightroom-firefly-services-auto-straighten-request
- name: AutoToneRequest
  property_count: 2
  slug: lightroom-firefly-services-auto-tone-request
- name: EditImageRequest
  property_count: 3
  slug: lightroom-firefly-services-edit-image-request
- name: ErrorResponse
  property_count: 4
  slug: lightroom-firefly-services-error-response
- name: JobResponse
  property_count: 5
  slug: lightroom-firefly-services-job-response
- name: StorageInput
  property_count: 2
  slug: lightroom-firefly-services-storage-input
- name: StorageOutput
  property_count: 5
  slug: lightroom-firefly-services-storage-output
- name: Lightroom Rendition
  property_count: 11
  slug: lightroom-rendition
- name: AlbumAssetsRequest
  property_count: 1
  slug: lightroom-services-album-assets-request
- name: AlbumCreateRequest
  property_count: 2
  slug: lightroom-services-album-create-request
- name: AlbumResponse
  property_count: 7
  slug: lightroom-services-album-response
- name: Album
  property_count: 6
  slug: lightroom-services-album
- name: AlbumsListResponse
  property_count: 2
  slug: lightroom-services-albums-list-response
- name: AssetResponse
  property_count: 7
  slug: lightroom-services-asset-response
- name: AssetRevisionRequest
  property_count: 2
  slug: lightroom-services-asset-revision-request
- name: Asset
  property_count: 7
  slug: lightroom-services-asset
- name: AssetsListResponse
  property_count: 2
  slug: lightroom-services-assets-list-response
- name: CatalogResponse
  property_count: 6
  slug: lightroom-services-catalog-response
- name: ErrorResponse
  property_count: 3
  slug: lightroom-services-error-response
- name: HealthResponse
  property_count: 1
  slug: lightroom-services-health-response
- name: Links
  property_count: 0
  slug: lightroom-services-links
json_structures:
- name: Lightroom Albums Album Assets Request Structure
  property_count: 1
  slug: lightroom-albums-album-assets-request-structure
- name: Lightroom Albums Album Create Request Structure
  property_count: 2
  slug: lightroom-albums-album-create-request-structure
- name: Lightroom Albums Album Payload Structure
  property_count: 5
  slug: lightroom-albums-album-payload-structure
- name: Lightroom Albums Album Response Structure
  property_count: 6
  slug: lightroom-albums-album-response-structure
- name: Lightroom Albums Album Structure
  property_count: 5
  slug: lightroom-albums-album-structure
- name: Lightroom Albums Albums List Response Structure
  property_count: 2
  slug: lightroom-albums-albums-list-response-structure
- name: Lightroom Albums Assets List Response Structure
  property_count: 2
  slug: lightroom-albums-assets-list-response-structure
- name: Lightroom Albums Error Response Structure
  property_count: 2
  slug: lightroom-albums-error-response-structure
- name: Lightroom Albums Links Structure
  property_count: 0
  slug: lightroom-albums-links-structure
- name: Lightroom Assets Asset Create Request Structure
  property_count: 2
  slug: lightroom-assets-asset-create-request-structure
- name: Lightroom Assets Asset Payload Structure
  property_count: 7
  slug: lightroom-assets-asset-payload-structure
- name: Lightroom Assets Asset Response Structure
  property_count: 6
  slug: lightroom-assets-asset-response-structure
- name: Lightroom Assets Asset Structure
  property_count: 6
  slug: lightroom-assets-asset-structure
- name: Lightroom Assets Assets List Response Structure
  property_count: 2
  slug: lightroom-assets-assets-list-response-structure
- name: Lightroom Assets Error Response Structure
  property_count: 2
  slug: lightroom-assets-error-response-structure
- name: Lightroom Assets Links Structure
  property_count: 0
  slug: lightroom-assets-links-structure
- name: Lightroom Catalog Catalog Response Structure
  property_count: 7
  slug: lightroom-catalog-catalog-response-structure
- name: Lightroom Catalog Error Response Structure
  property_count: 2
  slug: lightroom-catalog-error-response-structure
- name: Lightroom Firefly Services Apply Presets Request Structure
  property_count: 2
  slug: lightroom-firefly-services-apply-presets-request-structure
- name: Lightroom Firefly Services Auto Straighten Request Structure
  property_count: 2
  slug: lightroom-firefly-services-auto-straighten-request-structure
- name: Lightroom Firefly Services Auto Tone Request Structure
  property_count: 2
  slug: lightroom-firefly-services-auto-tone-request-structure
- name: Lightroom Firefly Services Edit Image Request Structure
  property_count: 3
  slug: lightroom-firefly-services-edit-image-request-structure
- name: Lightroom Firefly Services Error Response Structure
  property_count: 4
  slug: lightroom-firefly-services-error-response-structure
- name: Lightroom Firefly Services Job Response Structure
  property_count: 5
  slug: lightroom-firefly-services-job-response-structure
- name: Lightroom Firefly Services Storage Input Structure
  property_count: 2
  slug: lightroom-firefly-services-storage-input-structure
- name: Lightroom Firefly Services Storage Output Structure
  property_count: 5
  slug: lightroom-firefly-services-storage-output-structure
- name: Lightroom Services Album Assets Request Structure
  property_count: 1
  slug: lightroom-services-album-assets-request-structure
- name: Lightroom Services Album Create Request Structure
  property_count: 2
  slug: lightroom-services-album-create-request-structure
- name: Lightroom Services Album Response Structure
  property_count: 7
  slug: lightroom-services-album-response-structure
- name: Lightroom Services Album Structure
  property_count: 6
  slug: lightroom-services-album-structure
- name: Lightroom Services Albums List Response Structure
  property_count: 2
  slug: lightroom-services-albums-list-response-structure
- name: Lightroom Services Asset Response Structure
  property_count: 7
  slug: lightroom-services-asset-response-structure
- name: Lightroom Services Asset Revision Request Structure
  property_count: 2
  slug: lightroom-services-asset-revision-request-structure
- name: Lightroom Services Asset Structure
  property_count: 7
  slug: lightroom-services-asset-structure
- name: Lightroom Services Assets List Response Structure
  property_count: 2
  slug: lightroom-services-assets-list-response-structure
- name: Lightroom Services Catalog Response Structure
  property_count: 6
  slug: lightroom-services-catalog-response-structure
- name: Lightroom Services Error Response Structure
  property_count: 3
  slug: lightroom-services-error-response-structure
- name: Lightroom Services Health Response Structure
  property_count: 1
  slug: lightroom-services-health-response-structure
- name: Lightroom Services Links Structure
  property_count: 0
  slug: lightroom-services-links-structure
jsonld:
- class_count: 0
  name: Lightroom Albums Context
  property_count: 0
  slug: lightroom-albums-context
- class_count: 0
  name: Lightroom Assets Context
  property_count: 0
  slug: lightroom-assets-context
- class_count: 0
  name: Lightroom Catalog Context
  property_count: 0
  slug: lightroom-catalog-context
- class_count: 0
  name: Lightroom Context
  property_count: 5
  slug: lightroom-context
- class_count: 0
  name: Lightroom Firefly Services Context
  property_count: 0
  slug: lightroom-firefly-services-context
- class_count: 0
  name: Lightroom Services Context
  property_count: 0
  slug: lightroom-services-context
layout: provider
modified: '2026-05-19'
name: Adobe Lightroom
nav: Providers
network: true
overview: 'Adobe Lightroom publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Album Assets API, Albums API, Assets API, and 9 more. Tagged areas include Cloud Storage, Image Editing, Metadata, Photo Management, and Photography.


  The Adobe Lightroom catalog on APIs.io includes 6 JSON-LD contexts and 2 Spectral governance rulesets.


  Adobe Lightroom''s developer surface includes authentication, documentation, developer console, signup flow, engineering blog, changelog, and 12 more developer resources.'
plans:
- name: Lightroom Plans Pricing
  plan_count: 3
  slug: lightroom-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 5
  name: Lightroom Rate Limits
  slug: lightroom-rate-limits
rules:
- name: Adobe Lightroom API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: lightroom-jsonschema-spectral-rules
- name: Adobe Lightroom API Rules
  rule_count: 17
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 9
  slug: lightroom-spectral-rules
scopes:
- name: Lightroom Scopes
  scope_count: 3
  slug: lightroom-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 59.6
  delta: -2.9
  facets:
    commercial_clarity: 60.5
    contract_quality: 69.2
    developer_ergonomics: 39.1
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 68.4
  previous_composite: 62.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lightroom/refs/heads/main/screenshots/lightroom-2026-06-20T184522.png
security:
- kind: authentication
  name: Lightroom Authentication
  slug: lightroom-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Lightroom Domain Security
  slug: lightroom-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lightroom Vulnerability Disclosure
  slug: lightroom-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: lightroom
tags:
- Cloud Storage
- Image Editing
- Metadata
- Photo Management
- Photography
---
