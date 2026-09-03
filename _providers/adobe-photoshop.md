---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.4
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Adobe Photoshop Agentic Access
  operation_count: 17
  slug: adobe-photoshop-agentic-access
  summary_line: 17 operations · 14 acting
api_count: 1
apis:
- description: A unified Node.js and TypeScript SDK that provides typed client libraries for accessing the Photoshop API and other Firefly Services. The PhotoshopClient class offers methods for background removal, m
  name: Adobe Firefly Services SDK for JavaScript
  slug: firefly-services-sdk
- description: The modern plugin development platform for Photoshop, replacing the legacy CEP framework. UXP (Unified Extensibility Platform) is powered by a V8 JavaScript engine supporting ES6+ and provides Spectru
  name: Adobe Photoshop UXP Plugin API
  slug: uxp-plugin-api
- description: A modern scripting system for Photoshop that allows developers to execute standalone JavaScript files with the .psjs extension to automate tasks. Unlike full UXP plugins, scripts are single files that
  name: Adobe Photoshop UXP Scripting
  slug: uxp-scripting
- description: 'A specialized plugin type that combines UXP''s JavaScript, HTML, and CSS plugin framework with native C++ code compiled as a .uxpaddon. This allows developers to write performance-critical code in C++ '
  name: Adobe Photoshop UXP Hybrid Plugins
  slug: uxp-hybrid-plugins
- description: A C++ based SDK for building low-level native Photoshop plugins. The SDK enables developers to extend Photoshop in seven categories including filters appearing under the Filter menu, file format impor
  name: Adobe Photoshop C++ Plugin SDK
  slug: cpp-plugin-sdk
- description: The legacy scripting system based on ExtendScript, Adobe's implementation of ECMAScript 3. ExtendScript scripts use the .jsx file extension and can automate nearly all Photoshop operations through a c
  name: Adobe Photoshop ExtendScript Scripting API
  slug: extendscript-scripting
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Execute Photoshop Action files (.atn) and Action JSON descriptors on images programmatically.
  name: Adobe Photoshop Actions API
  slug: adobe-photoshop-actions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Remove backgrounds from images and create masks using AI-powered subject detection.
  name: Adobe Photoshop Background Removal API
  slug: adobe-photoshop-background-removal-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Apply AI-powered product crop and depth blur effects to images.
  name: Adobe Photoshop Crop and Effects API
  slug: adobe-photoshop-crop-and-effects-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Create, modify, and inspect PSD documents including layer editing, adjustments, and metadata retrieval.
  name: Adobe Photoshop Document Operations API
  slug: adobe-photoshop-document-operations-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Fill masked areas of images using generative AI capabilities.
  name: Adobe Photoshop Generative API
  slug: adobe-photoshop-generative-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Service health check endpoint.
  name: Adobe Photoshop Health API
  slug: adobe-photoshop-health-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Generate flat image renditions from PSD files in various formats including JPEG, PNG, and TIFF.
  name: Adobe Photoshop Renditions API
  slug: adobe-photoshop-renditions-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Replace and manage embedded Smart Object layers within PSD documents.
  name: Adobe Photoshop Smart Objects API
  slug: adobe-photoshop-smart-objects-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Poll for the status of asynchronous jobs.
  name: Adobe Photoshop Status API
  slug: adobe-photoshop-status-api
- baseURL: https://image.adobe.io
  baseurl_source: declared
  description: Edit text layer content, character styles, and paragraph styles in PSD documents.
  name: Adobe Photoshop Text API
  slug: adobe-photoshop-text-api
arazzos:
- description: Composite an overlay onto an image using programmatic Action JSON descriptors.
  name: Adobe Photoshop Run Action JSON Composite
  slug: adobe-photoshop-action-json-composite-workflow
- description: Build a document from scratch with Action JSON descriptors, no input file required.
  name: Adobe Photoshop Create Document with Action JSON
  slug: adobe-photoshop-action-json-document-create-workflow
- description: Assemble a multi-artboard PSD from sized boards, then render it to a flat image.
  name: Adobe Photoshop Create Artboards and Render
  slug: adobe-photoshop-artboard-create-workflow
- description: Apply an AI depth-of-field blur to an image and poll the job to completion.
  name: Adobe Photoshop Depth Blur
  slug: adobe-photoshop-depth-blur-workflow
- description: Create a new PSD from dimensions and layers, then render it to a flat image.
  name: Adobe Photoshop Create Document and Render
  slug: adobe-photoshop-document-create-and-render-workflow
- description: Generate a subject mask with background removal, then fill the masked area with generative AI.
  name: Adobe Photoshop Generative Fill from a Generated Mask
  slug: adobe-photoshop-generative-fill-workflow
- description: Read a PSD's layer tree, then apply layer edits and adjustments to it.
  name: Adobe Photoshop Inspect and Edit Layers
  slug: adobe-photoshop-layer-edit-workflow
- description: Replay a recorded .atn Action on an image, then render the result to a flat deliverable.
  name: Adobe Photoshop Run Action File and Render
  slug: adobe-photoshop-photoshop-action-batch-workflow
- description: Cut out a product, wait for the cutout, then smart-crop it to the subject.
  name: Adobe Photoshop Product Photo Pipeline
  slug: adobe-photoshop-product-photo-pipeline-workflow
- description: Verify service access, submit an AI background removal job, and poll it to completion.
  name: Adobe Photoshop Remove Background
  slug: adobe-photoshop-remove-background-workflow
- description: Read a PSD template's layer tree, swap Smart Object artwork, then render a flat image.
  name: Adobe Photoshop Smart Object Template Personalization
  slug: adobe-photoshop-smart-object-template-workflow
- description: Inspect a PSD's text layers, rewrite their content and styling, then render the result.
  name: Adobe Photoshop Text Layer Personalization
  slug: adobe-photoshop-text-layer-personalization-workflow
artifact_total: 138
asyncapis:
- description: Event-driven notifications for Adobe Photoshop API asynchronous job processing. When registered through Adobe I/O Events, webhooks deliver real-time notifications when Photoshop API jobs complete or f
  name: Adobe Photoshop API Webhook Events
  slug: adobe-photoshop-api-asyncapi-original
collections:
- collection_type: postman
  name: Adobe Photoshop Actions API
  slug: postman-adobe-photoshop-actions-api
- collection_type: postman
  name: Adobe Photoshop Actions Background Removal API
  slug: postman-adobe-photoshop-background-removal-api
- collection_type: postman
  name: Adobe Photoshop Actions Crop and Effects API
  slug: postman-adobe-photoshop-crop-and-effects-api
- collection_type: postman
  name: Adobe Photoshop Actions Document Operations API
  slug: postman-adobe-photoshop-document-operations-api
- collection_type: postman
  name: Adobe Photoshop Actions Generative API
  slug: postman-adobe-photoshop-generative-api
- collection_type: postman
  name: Adobe Photoshop Actions Health API
  slug: postman-adobe-photoshop-health-api
- collection_type: postman
  name: Adobe Photoshop Actions Renditions API
  slug: postman-adobe-photoshop-renditions-api
- collection_type: postman
  name: Adobe Photoshop Actions Smart Objects API
  slug: postman-adobe-photoshop-smart-objects-api
- collection_type: postman
  name: Adobe Photoshop Actions Status API
  slug: postman-adobe-photoshop-status-api
- collection_type: postman
  name: Adobe Photoshop Actions Text API
  slug: postman-adobe-photoshop-text-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe Photoshop Actions API
  slug: open-adobe-photoshop-actions-api
- collection_type: open
  name: Adobe Photoshop Actions Background Removal API
  slug: open-adobe-photoshop-background-removal-api
- collection_type: open
  name: Adobe Photoshop Actions Crop and Effects API
  slug: open-adobe-photoshop-crop-and-effects-api
- collection_type: open
  name: Adobe Photoshop Actions Document Operations API
  slug: open-adobe-photoshop-document-operations-api
- collection_type: open
  name: Adobe Photoshop Actions Generative API
  slug: open-adobe-photoshop-generative-api
- collection_type: open
  name: Adobe Photoshop Actions Health API
  slug: open-adobe-photoshop-health-api
- collection_type: open
  name: Adobe Photoshop Actions Renditions API
  slug: open-adobe-photoshop-renditions-api
- collection_type: open
  name: Adobe Photoshop Actions Smart Objects API
  slug: open-adobe-photoshop-smart-objects-api
- collection_type: open
  name: Adobe Photoshop Actions Status API
  slug: open-adobe-photoshop-status-api
- collection_type: open
  name: Adobe Photoshop Actions Text API
  slug: open-adobe-photoshop-text-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-photoshop/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-photoshop-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-photoshop-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-photoshop-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-photoshop-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/adobe-photoshop-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/adobe-photoshop-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/adobe-photoshop-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/adobe-photoshop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/adobe-photoshop-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/adobe-photoshop-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/adobe-photoshop-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/adobe-photoshop-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-photoshop-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/adobe-photoshop-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/adobe-photoshop-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/adobe-photoshop-data-model.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-remove-background-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-product-photo-pipeline-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-smart-object-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-text-layer-personalization-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-generative-fill-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-document-create-and-render-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-layer-edit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-photoshop-action-batch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-action-json-composite-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-action-json-document-create-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-depth-blur-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-photoshop-artboard-create-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/photoshop/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/firefly-services/docs/photoshop/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/photoshop/uxp/2022/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/firefly-services/docs/photoshop/getting_started/
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/developer-console/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adobe.com/firefly-services/docs/photoshop/api/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/firefly-services/docs/guides/sdks/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Firefly-Services/firefly-services-sdk-js
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/AdobeDocs/photoshop-cpp-sdk
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/products/photoshop.html
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: operate
  title: ''
  type: Forums
  url: https://community.adobe.com/t5/photoshop-ecosystem-discussions/bd-p/photoshop
- group: operate
  title: ''
  type: Forums
  url: https://forums.creativeclouddeveloper.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security/products/photoshop.html
- group: other
  title: ''
  type: X
  url: https://x.com/Photoshop
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@AdobeCreativeCloud
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: commercial
  title: ''
  type: License
  url: https://www.adobe.com/legal/licenses-terms.html
created: '2025-02-28'
description: Adobe Photoshop is the industry-standard image editing and digital design application. Its developer platform offers a cloud-based REST API for programmatic image processing via Firefly Services, the UXP plugin framework for building desktop extensions with modern JavaScript, a C++ plugin SDK for native filters and file formats, and scripting interfaces for workflow automation.
examples:
- key_count: 3
  name: Adobe Photoshop Api Action Json Request Example
  slug: adobe-photoshop-api-action-json-request-example
- key_count: 2
  name: Adobe Photoshop Api Artboard Create Request Example
  slug: adobe-photoshop-api-artboard-create-request-example
- key_count: 3
  name: Adobe Photoshop Api Depth Blur Request Example
  slug: adobe-photoshop-api-depth-blur-request-example
- key_count: 2
  name: Adobe Photoshop Api Document Create Request Example
  slug: adobe-photoshop-api-document-create-request-example
- key_count: 2
  name: Adobe Photoshop Api Document Manifest Request Example
  slug: adobe-photoshop-api-document-manifest-request-example
- key_count: 3
  name: Adobe Photoshop Api Document Operations Request Example
  slug: adobe-photoshop-api-document-operations-request-example
- key_count: 2
  name: Adobe Photoshop Api Fill Masked Areas Request Example
  slug: adobe-photoshop-api-fill-masked-areas-request-example
- key_count: 3
  name: Adobe Photoshop Api Photoshop Actions Request Example
  slug: adobe-photoshop-api-photoshop-actions-request-example
- key_count: 3
  name: Adobe Photoshop Api Product Crop Request Example
  slug: adobe-photoshop-api-product-crop-request-example
- key_count: 6
  name: Adobe Photoshop Api Remove Background Request Example
  slug: adobe-photoshop-api-remove-background-request-example
- key_count: 2
  name: Adobe Photoshop Api Rendition Create Request Example
  slug: adobe-photoshop-api-rendition-create-request-example
- key_count: 3
  name: Adobe Photoshop Api Smart Object Request Example
  slug: adobe-photoshop-api-smart-object-request-example
- key_count: 2
  name: Adobe Photoshop Api Storage Input Example
  slug: adobe-photoshop-api-storage-input-example
- key_count: 5
  name: Adobe Photoshop Api Storage Output Example
  slug: adobe-photoshop-api-storage-output-example
- key_count: 3
  name: Adobe Photoshop Api Text Edit Request Example
  slug: adobe-photoshop-api-text-edit-request-example
- key_count: 10
  name: Adobe Photoshop Uxp Plugin Manifest Example
  slug: adobe-photoshop-uxp-plugin-manifest-example
features:
- description: Process images in the cloud without local Photoshop installation via the REST API.
  name: Cloud Image Processing
- description: AI-powered automatic background removal and mask generation.
  name: Background Removal
- description: Create, read, and modify PSD files including layers, Smart Objects, and text.
  name: PSD Document Editing
- description: AI-powered content generation to fill, extend, or replace image regions.
  name: Generative Fill
- description: Replace embedded Smart Object content across PSD templates programmatically.
  name: Smart Object Replacement
- description: Modify text content, fonts, colors, and styling in PSD text layers.
  name: Text Layer Editing
- description: Run recorded Photoshop Actions (.atn files) on images in the cloud.
  name: Photoshop Actions Execution
- description: Build desktop plugins with modern JavaScript, HTML, CSS, and Spectrum UI components.
  name: UXP Plugin Framework
- description: Create native filters, file format support, and selection tools with the C++ SDK.
  name: C++ Plugin SDK
- description: Legacy scripting interface for batch processing and workflow automation.
  name: ExtendScript Automation
- description: AI-powered automatic cropping to isolate product subjects.
  name: Product Crop
- description: Apply realistic depth-of-field blur effects using AI depth estimation.
  name: Depth Blur
finops:
- name: Adobe Photoshop Finops
  service_category: Creative SaaS
  slug: adobe-photoshop-finops
image: /assets/icons/adobe-photoshop.png
integrations:
- description: Native integration with other Creative Cloud apps via shared libraries and cloud storage.
  name: Adobe Creative Cloud
- description: Roundtrip editing between Lightroom and Photoshop for photography workflows.
  name: Adobe Lightroom
- description: Generative AI features powered by Adobe Firefly for content creation.
  name: Adobe Firefly
- description: API supports input/output from AWS S3, Azure Blob, Google Cloud Storage, and Dropbox.
  name: Cloud Storage Providers
json_schemas:
- name: ActionJSONRequest
  property_count: 3
  slug: adobe-photoshop-api-action-json-request
- name: ArtboardCreateRequest
  property_count: 2
  slug: adobe-photoshop-api-artboard-create-request
- name: DepthBlurRequest
  property_count: 3
  slug: adobe-photoshop-api-depth-blur-request
- name: DocumentCreateRequest
  property_count: 2
  slug: adobe-photoshop-api-document-create-request
- name: DocumentManifestRequest
  property_count: 2
  slug: adobe-photoshop-api-document-manifest-request
- name: DocumentOperationsRequest
  property_count: 3
  slug: adobe-photoshop-api-document-operations-request
- name: FillMaskedAreasRequest
  property_count: 2
  slug: adobe-photoshop-api-fill-masked-areas-request
- name: PhotoshopActionsRequest
  property_count: 3
  slug: adobe-photoshop-api-photoshop-actions-request
- name: ProductCropRequest
  property_count: 3
  slug: adobe-photoshop-api-product-crop-request
- name: RemoveBackgroundRequest
  property_count: 6
  slug: adobe-photoshop-api-remove-background-request
- name: RenditionCreateRequest
  property_count: 2
  slug: adobe-photoshop-api-rendition-create-request
- name: SmartObjectRequest
  property_count: 3
  slug: adobe-photoshop-api-smart-object-request
- name: StorageInput
  property_count: 2
  slug: adobe-photoshop-api-storage-input
- name: StorageOutput
  property_count: 5
  slug: adobe-photoshop-api-storage-output
- name: TextEditRequest
  property_count: 3
  slug: adobe-photoshop-api-text-edit-request
- name: Adobe Photoshop UXP Plugin Manifest
  property_count: 13
  slug: adobe-photoshop-uxp-plugin-manifest
json_structures:
- name: Adobe Photoshop Api Action Json Request Structure
  property_count: 3
  slug: adobe-photoshop-api-action-json-request-structure
- name: Adobe Photoshop Api Artboard Create Request Structure
  property_count: 2
  slug: adobe-photoshop-api-artboard-create-request-structure
- name: Adobe Photoshop Api Depth Blur Request Structure
  property_count: 3
  slug: adobe-photoshop-api-depth-blur-request-structure
- name: Adobe Photoshop Api Document Create Request Structure
  property_count: 2
  slug: adobe-photoshop-api-document-create-request-structure
- name: Adobe Photoshop Api Document Manifest Request Structure
  property_count: 2
  slug: adobe-photoshop-api-document-manifest-request-structure
- name: Adobe Photoshop Api Document Operations Request Structure
  property_count: 3
  slug: adobe-photoshop-api-document-operations-request-structure
- name: Adobe Photoshop Api Fill Masked Areas Request Structure
  property_count: 2
  slug: adobe-photoshop-api-fill-masked-areas-request-structure
- name: Adobe Photoshop Api Photoshop Actions Request Structure
  property_count: 3
  slug: adobe-photoshop-api-photoshop-actions-request-structure
- name: Adobe Photoshop Api Product Crop Request Structure
  property_count: 3
  slug: adobe-photoshop-api-product-crop-request-structure
- name: Adobe Photoshop Api Remove Background Request Structure
  property_count: 6
  slug: adobe-photoshop-api-remove-background-request-structure
- name: Adobe Photoshop Api Rendition Create Request Structure
  property_count: 2
  slug: adobe-photoshop-api-rendition-create-request-structure
- name: Adobe Photoshop Api Smart Object Request Structure
  property_count: 3
  slug: adobe-photoshop-api-smart-object-request-structure
- name: Adobe Photoshop Api Storage Input Structure
  property_count: 2
  slug: adobe-photoshop-api-storage-input-structure
- name: Adobe Photoshop Api Storage Output Structure
  property_count: 5
  slug: adobe-photoshop-api-storage-output-structure
- name: Adobe Photoshop Api Text Edit Request Structure
  property_count: 3
  slug: adobe-photoshop-api-text-edit-request-structure
- name: Adobe Photoshop Uxp Plugin Manifest Structure
  property_count: 13
  slug: adobe-photoshop-uxp-plugin-manifest-structure
jsonld:
- class_count: 16
  name: Adobe Photoshop Context
  property_count: 28
  slug: adobe-photoshop-context
layout: provider
mcp_servers:
- description: ''
  name: Adobe Photoshop MCP Server
  slug: adobe-photoshop-mcp-server
modified: '2026-06-20'
name: Adobe Photoshop
nav: Providers
network: true
overview: 'Adobe Photoshop publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Actions API, Background Removal API, Crop and Effects API, and 7 more. Tagged areas include Ai Ml, Creative Cloud, Image Editing, Photoshop, and Plugins.


  The Adobe Photoshop catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Adobe Photoshop''s developer surface includes authentication, changelog, developer portal, documentation, getting-started guide, API reference, engineering blog, and 42 more developer resources.'
plans:
- name: Adobe Photoshop Plans Pricing
  plan_count: 4
  slug: adobe-photoshop-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 2
  name: Adobe Photoshop Rate Limits
  slug: adobe-photoshop-rate-limits
rules:
- effective_rule_count: 31
  extends:
  - spectral:asyncapi
  name: Adobe Photoshop API Rules
  rule_count: 4
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 2
  slug: adobe-photoshop-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Adobe Photoshop API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adobe-photoshop-jsonschema-spectral-rules
- effective_rule_count: 69
  extends:
  - spectral:oas
  name: Adobe Photoshop API Rules
  rule_count: 28
  severity_counts:
    error: 13
    hint: 0
    info: 2
    warn: 13
  slug: adobe-photoshop-spectral-rules
score:
  band: developing
  composite: 52.4
  coverage:
    artifact_dirs: 30
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 18.2
    contract_quality: 76.8
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 52.6
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-photoshop/refs/heads/main/screenshots/adobe-photoshop-2026-06-20T164959.png
security:
- kind: authentication
  name: Adobe Photoshop Authentication
  slug: adobe-photoshop-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Adobe Photoshop Domain Security
  slug: adobe-photoshop-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Photoshop Vulnerability Disclosure
  slug: adobe-photoshop-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-photoshop
solutions:
- description: Cloud-based REST API for programmatic image processing at scale.
  name: Photoshop API (Firefly Services)
- description: Modern plugin platform for extending Photoshop with JavaScript and HTML.
  name: Photoshop Desktop (UXP)
- description: Native plugin SDK for filters, file formats, and performance-critical extensions.
  name: Photoshop Desktop (C++ SDK)
- description: Automation via UXP scripts (.psjs) or legacy ExtendScript (.jsx).
  name: Photoshop Scripting
tags:
- Ai Ml
- Creative Cloud
- Image Editing
- Photoshop
- Plugins
- REST API
- Scripting
use_cases:
- description: Automate background removal, product crop, and image enhancement for e-commerce catalogs.
  name: Product Photography Automation
- description: Replace Smart Objects in PSD templates to generate personalized marketing materials at scale.
  name: Template-Based Design Generation
- description: Process thousands of images with consistent edits using the cloud API or Actions.
  name: Batch Image Processing
- description: Build UXP plugins that add custom panels, automate tasks, and integrate with external services.
  name: Creative Workflow Plugins
- description: Convert between PSD, JPEG, PNG, TIFF, and other formats programmatically.
  name: Image Format Conversion
- description: Use generative fill and AI features to extend, modify, or enhance image content.
  name: Content-Aware Editing
- description: Automate print-ready output generation with proper color spaces and bleed settings.
  name: Print Production Automation
- description: Connect digital asset management systems with Photoshop for automated processing pipelines.
  name: DAM Integration
website: https://www.adobe.com/products/photoshop.html
---
