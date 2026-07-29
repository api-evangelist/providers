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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.0
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 30
  human_in_the_loop: 0
  name: Adobe Creative Suite Agentic Access
  operation_count: 39
  slug: adobe-creative-suite-agentic-access
  summary_line: 39 operations · 30 acting
api_count: 38
apis:
- description: 'The Adobe Illustrator API enables programmatic creation and manipulation of vector graphics through scripting and plugin interfaces. It exposes the Illustrator object model so developers can automate '
  name: Adobe Illustrator API
  slug: illustrator-api
- description: The Adobe InDesign API allows developers to automate document layout and publishing workflows through scripting and UXP plugins. It exposes InDesign's document model for tasks such as batch exporting,
  name: Adobe InDesign API
  slug: indesign-api
- description: The Adobe Premiere Pro API gives developers access to video editing automation through scripting and panel extensions. It allows integration with external media asset management systems, automated seq
  name: Adobe Premiere Pro API
  slug: premiere-pro-api
- description: 'The Adobe After Effects API enables scripting and plugin development for motion graphics and visual effects workflows. Developers can automate rendering, manipulate compositions programmatically, and '
  name: Adobe After Effects API
  slug: after-effects-api
- description: 'The Adobe Creative Cloud Libraries API provides access to shared design assets stored in Creative Cloud Libraries, including colors, character styles, graphics, and components. It allows applications '
  name: Adobe Creative Cloud Libraries API
  slug: creative-cloud-libraries-api
- description: The Adobe Analytics API provides programmatic access to Adobe Analytics report suites for retrieving, segmenting, and analyzing web and app behavioral data. It supports both the Reporting API for quer
  name: Adobe Analytics API
  slug: analytics-api
- description: The Adobe Experience Manager Assets API provides access to the AEM digital asset management system for uploading, retrieving, and managing assets stored in AEM as a Cloud Service. It enables integrati
  name: Adobe Experience Manager Assets API
  slug: experience-manager-assets-api
- description: The Adobe Acrobat Sign API enables sending, tracking, and managing electronic signature agreements programmatically. It supports creating agreements from documents or templates, managing signers and r
  name: Adobe Acrobat Sign API
  slug: acrobat-sign-api
- description: The Adobe Fonts API provides access to the Adobe Fonts library for discovering and embedding web fonts in applications and websites. It allows querying font families, retrieving font metadata, and gen
  name: Adobe Fonts API
  slug: fonts-api
- description: The Adobe Express Embed SDK allows developers to embed Adobe Express editing capabilities directly into their own web applications. It provides a customizable in-app editing experience for images, vid
  name: Adobe Express Embed SDK
  slug: express-embed-sdk
- description: Adobe UXP (Unified Extensibility Platform) is the modern plugin and scripting platform used across Adobe creative applications including Photoshop, InDesign, Illustrator, and XD. It provides a JavaScr
  name: Adobe UXP
  slug: uxp
- description: Auto-tag PDFs for accessibility compliance
  name: Adobe Creative Suite Accessibility API
  slug: adobe-creative-suite-accessibility-api
- description: Artboard creation and management
  name: Adobe Creative Suite Artboard API
  slug: adobe-creative-suite-artboard-api
- description: Upload and manage input/output assets for PDF operations
  name: Adobe Creative Suite Assets API
  slug: adobe-creative-suite-assets-api
- description: Combine multiple PDFs into one
  name: Adobe Creative Suite Combine PDF API
  slug: adobe-creative-suite-combine-pdf-api
- description: Reduce PDF file size
  name: Adobe Creative Suite Compress PDF API
  slug: adobe-creative-suite-compress-pdf-api
- description: Create PDF documents from other formats
  name: Adobe Creative Suite Create PDF API
  slug: adobe-creative-suite-create-pdf-api
- description: Background removal and masking operations
  name: Adobe Creative Suite Cutout API
  slug: adobe-creative-suite-cutout-api
- description: Document-level operations
  name: Adobe Creative Suite Document API
  slug: adobe-creative-suite-document-api
- description: Generate documents from templates and data
  name: Adobe Creative Suite Document Generation API
  slug: adobe-creative-suite-document-generation-api
- description: Export PDF documents to other formats
  name: Adobe Creative Suite Export PDF API
  slug: adobe-creative-suite-export-pdf-api
- description: Expand images beyond their original boundaries
  name: Adobe Creative Suite Generative Expand API
  slug: adobe-creative-suite-generative-expand-api
- description: Fill selected regions of images with AI-generated content
  name: Adobe Creative Suite Generative Fill API
  slug: adobe-creative-suite-generative-fill-api
- description: Text-to-image and image variation generation operations
  name: Adobe Creative Suite Image Generation API
  slug: adobe-creative-suite-image-generation-api
- description: PSD layer management operations
  name: Adobe Creative Suite Layers API
  slug: adobe-creative-suite-layers-api
- description: License stock assets for use in projects
  name: Adobe Creative Suite License API
  slug: adobe-creative-suite-license-api
- description: Optimize PDFs for fast web viewing
  name: Adobe Creative Suite Linearize PDF API
  slug: adobe-creative-suite-linearize-pdf-api
- description: Alpha mask creation operations
  name: Adobe Creative Suite Mask API
  slug: adobe-creative-suite-mask-api
- description: Member profile and licensing operations
  name: Adobe Creative Suite Member API
  slug: adobe-creative-suite-member-api
- description: Composite AI-generated objects into existing images
  name: Adobe Creative Suite Object Composite API
  slug: adobe-creative-suite-object-composite-api
- description: Apply optical character recognition to scanned PDFs
  name: Adobe Creative Suite OCR API
  slug: adobe-creative-suite-ocr-api
- description: Check operation job status
  name: Adobe Creative Suite Operations API
  slug: adobe-creative-suite-operations-api
- description: Rendition and export operations
  name: Adobe Creative Suite Rendition API
  slug: adobe-creative-suite-rendition-api
- description: Search and discover stock content
  name: Adobe Creative Suite Search API
  slug: adobe-creative-suite-search-api
- description: Smart object editing operations
  name: Adobe Creative Suite Smart Object API
  slug: adobe-creative-suite-smart-object-api
- description: Asynchronous job status polling
  name: Adobe Creative Suite Status API
  slug: adobe-creative-suite-status-api
- description: Text layer editing operations
  name: Adobe Creative Suite Text API
  slug: adobe-creative-suite-text-api
- description: Generate video from text prompts
  name: Adobe Creative Suite Video Generation API
  slug: adobe-creative-suite-video-generation-api
arazzos:
- description: Expand an image beyond its original boundaries with AI and poll the job to completion.
  name: Adobe Firefly Generative Expand Image
  slug: adobe-creative-suite-firefly-expand-image-workflow
- description: Generate variations similar to a reference image and poll the async job to completion.
  name: Adobe Firefly Generate Similar Images
  slug: adobe-creative-suite-firefly-generate-similar-workflow
- description: Fill a masked region of an image with AI-generated content and poll the job to completion.
  name: Adobe Firefly Generative Fill
  slug: adobe-creative-suite-firefly-generative-fill-workflow
- description: Composite an AI-generated object into a scene image and poll the async job to completion.
  name: Adobe Firefly Object Composite
  slug: adobe-creative-suite-firefly-object-composite-workflow
- description: Submit a text-to-image Firefly job, poll until it finishes, and return the generated image URLs.
  name: Adobe Firefly Text-to-Image Generation
  slug: adobe-creative-suite-firefly-text-to-image-workflow
- description: Submit a text-to-video Firefly job, poll until it finishes, and return the generated video URLs.
  name: Adobe Firefly Text-to-Video Generation
  slug: adobe-creative-suite-firefly-text-to-video-workflow
- description: Upload a PDF, auto-tag it for accessibility, poll the job, and get the tagged output download URI.
  name: Adobe PDF Services Auto-tag PDF for Accessibility
  slug: adobe-creative-suite-pdf-autotag-accessibility-workflow
- description: Upload two PDFs, combine them into one, poll the job, and get the merged output download URI.
  name: Adobe PDF Services Combine PDFs
  slug: adobe-creative-suite-pdf-combine-workflow
- description: Upload a PDF, compress it at a chosen level, poll the job, and get the compressed download URI.
  name: Adobe PDF Services Compress PDF
  slug: adobe-creative-suite-pdf-compress-workflow
- description: Upload an Office or HTML source, convert it to PDF, poll the job, and get the output download URI.
  name: Adobe PDF Services Create PDF from Office
  slug: adobe-creative-suite-pdf-create-from-office-workflow
- description: Upload a PDF, export it to a target Office format, poll the job, and get the output download URI.
  name: Adobe PDF Services Export PDF to Word
  slug: adobe-creative-suite-pdf-export-to-word-workflow
- description: Upload a Word template, merge JSON data into it, poll the job, get the output, and delete the template.
  name: Adobe PDF Services Generate Document from Template
  slug: adobe-creative-suite-pdf-generate-document-workflow
- description: Upload a PDF, linearize it for fast web view, poll the job, and get the optimized download URI.
  name: Adobe PDF Services Linearize PDF
  slug: adobe-creative-suite-pdf-linearize-workflow
- description: Upload a scanned PDF, apply OCR, poll the job, and get the searchable output download URI.
  name: Adobe PDF Services OCR PDF
  slug: adobe-creative-suite-pdf-ocr-workflow
- description: Submit a Sensei alpha-mask job, poll until it finishes, and return the mask output URL.
  name: Adobe Photoshop Create Alpha Mask
  slug: adobe-creative-suite-photoshop-create-mask-workflow
- description: Submit a rendition job from a PSD, poll until it finishes, and return the rendered output URL.
  name: Adobe Photoshop Create Rendition
  slug: adobe-creative-suite-photoshop-create-rendition-workflow
- description: Submit a PSD text-layer edit job, poll until it finishes, and return the edited output URL.
  name: Adobe Photoshop Edit Text Layers
  slug: adobe-creative-suite-photoshop-edit-text-layers-workflow
- description: Submit a Sensei product-crop job, poll until it finishes, and return the cropped output URL.
  name: Adobe Photoshop Product Crop
  slug: adobe-creative-suite-photoshop-product-crop-workflow
- description: Submit a Sensei background-removal job, poll until it finishes, and return the cutout output URL.
  name: Adobe Photoshop Remove Background
  slug: adobe-creative-suite-photoshop-remove-background-workflow
- description: Check the member download quota, license an image only when quota remains, and record the license history.
  name: Adobe Stock License Image with Quota Check
  slug: adobe-creative-suite-stock-license-with-quota-check-workflow
- description: Search Adobe Stock for photos, inspect the top match metadata, and license it for download.
  name: Adobe Stock Search and License Image
  slug: adobe-creative-suite-stock-search-and-license-image-workflow
- description: Search Adobe Stock for video clips and license the top match for download.
  name: Adobe Stock Search and License Video
  slug: adobe-creative-suite-stock-search-and-license-video-workflow
artifact_total: 331
collections:
- collection_type: postman
  name: Adobe Creative Suite Adobe Firefly API
  slug: postman-adobe-creative-suite-firefly
- collection_type: postman
  name: Adobe Creative Suite Adobe PDF Services API
  slug: postman-adobe-creative-suite-pdf-services
- collection_type: postman
  name: Adobe Creative Suite Adobe Photoshop API
  slug: postman-adobe-creative-suite-photoshop
- collection_type: postman
  name: Adobe Creative Suite Adobe Stock API
  slug: postman-adobe-creative-suite-stock
- collection_type: open
  name: Adobe Creative Suite Adobe Firefly API
  slug: open-adobe-creative-suite-firefly
- collection_type: open
  name: Adobe Creative Suite Adobe PDF Services API
  slug: open-adobe-creative-suite-pdf-services
- collection_type: open
  name: Adobe Creative Suite Adobe Photoshop API
  slug: open-adobe-creative-suite-photoshop
- collection_type: open
  name: Adobe Creative Suite Adobe Stock API
  slug: open-adobe-creative-suite-stock
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-creative-suite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-creative-suite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-creative-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-creative-suite-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe-creative-suite/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-expand-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-generate-similar-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-generative-fill-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-object-composite-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-text-to-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-firefly-text-to-video-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-autotag-accessibility-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-combine-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-compress-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-create-from-office-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-export-to-word-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-generate-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-linearize-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-pdf-ocr-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-photoshop-create-mask-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-photoshop-create-rendition-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-photoshop-edit-text-layers-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-photoshop-product-crop-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-photoshop-remove-background-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-stock-license-with-quota-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-stock-search-and-license-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-creative-suite-stock-search-and-license-video-workflow.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-creative-suite-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-image-job-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-firefly-generation-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/adobe-creative-suite-stock-file-schema.json
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/console/home
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/developer-console/docs/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/adobe
- group: operate
  title: ''
  type: Community
  url: https://community.adobe.com/t5/developers/ct-p/developers
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/adobe
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adobe.com/developer-console/docs/release-notes/
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy.html
created: '2024-01-01'
description: Adobe Creative Suite is a collection of professional software applications for graphic design, video editing, web development, and photography.
examples:
- key_count: 2
  name: Adobe Creative Suite Firefly Async Job Submitted Example
  slug: adobe-creative-suite-firefly-async-job-submitted-example
- key_count: 3
  name: Adobe Creative Suite Firefly Error Response Example
  slug: adobe-creative-suite-firefly-error-response-example
- key_count: 5
  name: Adobe Creative Suite Firefly Generate Similar Request Example
  slug: adobe-creative-suite-firefly-generate-similar-request-example
- key_count: 0
  name: Adobe Creative Suite Firefly Generation Example
  slug: adobe-creative-suite-firefly-generation-example
- key_count: 6
  name: Adobe Creative Suite Firefly Generation Status Example
  slug: adobe-creative-suite-firefly-generation-status-example
- key_count: 7
  name: Adobe Creative Suite Firefly Image Expand Request Example
  slug: adobe-creative-suite-firefly-image-expand-request-example
- key_count: 6
  name: Adobe Creative Suite Firefly Image Fill Request Example
  slug: adobe-creative-suite-firefly-image-fill-request-example
- key_count: 8
  name: Adobe Creative Suite Firefly Image Generate Request Example
  slug: adobe-creative-suite-firefly-image-generate-request-example
- key_count: 2
  name: Adobe Creative Suite Firefly Image Size Example
  slug: adobe-creative-suite-firefly-image-size-example
- key_count: 1
  name: Adobe Creative Suite Firefly Input Image Reference Example
  slug: adobe-creative-suite-firefly-input-image-reference-example
- key_count: 7
  name: Adobe Creative Suite Firefly Object Composite Request Example
  slug: adobe-creative-suite-firefly-object-composite-request-example
- key_count: 3
  name: Adobe Creative Suite Firefly Output Image Example
  slug: adobe-creative-suite-firefly-output-image-example
- key_count: 3
  name: Adobe Creative Suite Firefly Style Options Example
  slug: adobe-creative-suite-firefly-style-options-example
- key_count: 4
  name: Adobe Creative Suite Firefly Video Generate Request Example
  slug: adobe-creative-suite-firefly-video-generate-request-example
- key_count: 8
  name: Adobe Creative Suite Image Job Example
  slug: adobe-creative-suite-image-job-example
- key_count: 4
  name: Adobe Creative Suite Pdf Services Asset Example
  slug: adobe-creative-suite-pdf-services-asset-example
- key_count: 1
  name: Adobe Creative Suite Pdf Services Asset Reference Example
  slug: adobe-creative-suite-pdf-services-asset-reference-example
- key_count: 1
  name: Adobe Creative Suite Pdf Services Asset Upload Request Example
  slug: adobe-creative-suite-pdf-services-asset-upload-request-example
- key_count: 2
  name: Adobe Creative Suite Pdf Services Asset Upload Response Example
  slug: adobe-creative-suite-pdf-services-asset-upload-response-example
- key_count: 3
  name: Adobe Creative Suite Pdf Services Auto Tag Request Example
  slug: adobe-creative-suite-pdf-services-auto-tag-request-example
- key_count: 1
  name: Adobe Creative Suite Pdf Services Combine Pdf Request Example
  slug: adobe-creative-suite-pdf-services-combine-pdf-request-example
- key_count: 2
  name: Adobe Creative Suite Pdf Services Compress Pdf Request Example
  slug: adobe-creative-suite-pdf-services-compress-pdf-request-example
- key_count: 2
  name: Adobe Creative Suite Pdf Services Create Pdf Request Example
  slug: adobe-creative-suite-pdf-services-create-pdf-request-example
- key_count: 4
  name: Adobe Creative Suite Pdf Services Document Generation Request Example
  slug: adobe-creative-suite-pdf-services-document-generation-request-example
- key_count: 3
  name: Adobe Creative Suite Pdf Services Export Pdf Request Example
  slug: adobe-creative-suite-pdf-services-export-pdf-request-example
- key_count: 1
  name: Adobe Creative Suite Pdf Services Linearize Pdf Request Example
  slug: adobe-creative-suite-pdf-services-linearize-pdf-request-example
- key_count: 2
  name: Adobe Creative Suite Pdf Services Ocr Request Example
  slug: adobe-creative-suite-pdf-services-ocr-request-example
- key_count: 3
  name: Adobe Creative Suite Pdf Services Operation Status Example
  slug: adobe-creative-suite-pdf-services-operation-status-example
- key_count: 1
  name: Adobe Creative Suite Pdf Services Operation Submitted Example
  slug: adobe-creative-suite-pdf-services-operation-submitted-example
- key_count: 2
  name: Adobe Creative Suite Pdf Services Page Range Example
  slug: adobe-creative-suite-pdf-services-page-range-example
- key_count: 2
  name: Adobe Creative Suite Photoshop Cutout Request Example
  slug: adobe-creative-suite-photoshop-cutout-request-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Document Operations Example
  slug: adobe-creative-suite-photoshop-document-operations-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Document Operations Request Example
  slug: adobe-creative-suite-photoshop-document-operations-request-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Job Input Example
  slug: adobe-creative-suite-photoshop-job-input-example
- key_count: 6
  name: Adobe Creative Suite Photoshop Job Output Example
  slug: adobe-creative-suite-photoshop-job-output-example
- key_count: 6
  name: Adobe Creative Suite Photoshop Job Status Example
  slug: adobe-creative-suite-photoshop-job-status-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Job Submitted Example
  slug: adobe-creative-suite-photoshop-job-submitted-example
- key_count: 10
  name: Adobe Creative Suite Photoshop Layer Example
  slug: adobe-creative-suite-photoshop-layer-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Layer Manage Request Example
  slug: adobe-creative-suite-photoshop-layer-manage-request-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Mask Request Example
  slug: adobe-creative-suite-photoshop-mask-request-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Product Crop Request Example
  slug: adobe-creative-suite-photoshop-product-crop-request-example
- key_count: 4
  name: Adobe Creative Suite Photoshop Render Output Example
  slug: adobe-creative-suite-photoshop-render-output-example
- key_count: 2
  name: Adobe Creative Suite Photoshop Rendition Create Request Example
  slug: adobe-creative-suite-photoshop-rendition-create-request-example
- key_count: 2
  name: Adobe Creative Suite Photoshop Straighten Request Example
  slug: adobe-creative-suite-photoshop-straighten-request-example
- key_count: 3
  name: Adobe Creative Suite Photoshop Text Edit Request Example
  slug: adobe-creative-suite-photoshop-text-edit-request-example
- key_count: 4
  name: Adobe Creative Suite Stock Category Example
  slug: adobe-creative-suite-stock-category-example
- key_count: 2
  name: Adobe Creative Suite Stock Error Response Example
  slug: adobe-creative-suite-stock-error-response-example
- key_count: 10
  name: Adobe Creative Suite Stock File Example
  slug: adobe-creative-suite-stock-file-example
- key_count: 2
  name: Adobe Creative Suite Stock License History Result Example
  slug: adobe-creative-suite-stock-license-history-result-example
- key_count: 2
  name: Adobe Creative Suite Stock License Reference Example
  slug: adobe-creative-suite-stock-license-reference-example
- key_count: 4
  name: Adobe Creative Suite Stock License Request Example
  slug: adobe-creative-suite-stock-license-request-example
- key_count: 3
  name: Adobe Creative Suite Stock License Response Example
  slug: adobe-creative-suite-stock-license-response-example
- key_count: 2
  name: Adobe Creative Suite Stock License Stats Response Example
  slug: adobe-creative-suite-stock-license-stats-response-example
- key_count: 1
  name: Adobe Creative Suite Stock Member Profile Example
  slug: adobe-creative-suite-stock-member-profile-example
- key_count: 2
  name: Adobe Creative Suite Stock Search Result Example
  slug: adobe-creative-suite-stock-search-result-example
- key_count: 10
  name: Adobe Creative Suite Stock Stock File Example
  slug: adobe-creative-suite-stock-stock-file-example
- key_count: 1
  name: Adobe Creative Suite Stock Stock File Response Example
  slug: adobe-creative-suite-stock-stock-file-response-example
features:
- description: Photoshop and Lightroom APIs for cloud-based image editing, background removal, and rendition generation.
  name: Cloud Image Processing
- description: Adobe Firefly API for text-to-image generation, generative fill, and style transfer.
  name: Generative AI
- description: Create, convert, extract, compress, and protect PDF documents programmatically.
  name: PDF Document Services
- description: Acrobat Sign API for creating and managing electronic signature workflows.
  name: Electronic Signatures
- description: Search, preview, and license photos, vectors, and videos from Adobe Stock.
  name: Stock Asset Licensing
- description: Sync colors, styles, and design assets across Adobe applications.
  name: Creative Cloud Libraries
- description: Adobe Fonts API for web font delivery and typography management.
  name: Font Delivery
- description: Premiere Pro and After Effects scripting for video production automation.
  name: Video Editing Automation
- description: Illustrator scripting for vector artwork creation and batch processing.
  name: Vector Graphics Automation
- description: InDesign Server and scripting for document layout automation.
  name: Desktop Publishing
- description: Adobe Express Embed SDK for integrating creative editing into web apps.
  name: Embeddable Creative Tools
- description: UXP framework for building modern plugins across Creative Cloud apps.
  name: Plugin Development
finops:
- name: Adobe Creative Suite Finops
  service_category: Creative SaaS (Discontinued)
  slug: adobe-creative-suite-finops
image: /assets/icons/adobe-creative-suite.png
json_schemas:
- name: ArtboardRequest
  property_count: 3
  slug: adobe-creative-suite-artboardrequest
- name: Asset
  property_count: 4
  slug: adobe-creative-suite-asset
- name: AssetReference
  property_count: 1
  slug: adobe-creative-suite-assetreference
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-creative-suite-assetuploadrequest
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-creative-suite-assetuploadresponse
- name: AsyncJobSubmitted
  property_count: 2
  slug: adobe-creative-suite-asyncjobsubmitted
- name: AutoTagRequest
  property_count: 3
  slug: adobe-creative-suite-autotagrequest
- name: Category
  property_count: 4
  slug: adobe-creative-suite-category
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-creative-suite-combinepdfrequest
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-creative-suite-compresspdfrequest
- name: CreatePDFRequest
  property_count: 2
  slug: adobe-creative-suite-createpdfrequest
- name: CutoutRequest
  property_count: 2
  slug: adobe-creative-suite-cutoutrequest
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-creative-suite-documentgenerationrequest
- name: DocumentOperations
  property_count: 3
  slug: adobe-creative-suite-documentoperations
- name: DocumentOperationsRequest
  property_count: 3
  slug: adobe-creative-suite-documentoperationsrequest
- name: ErrorResponse
  property_count: 3
  slug: adobe-creative-suite-errorresponse
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-creative-suite-exportpdfrequest
- name: AsyncJobSubmitted
  property_count: 2
  slug: adobe-creative-suite-firefly-async-job-submitted
- name: ErrorResponse
  property_count: 3
  slug: adobe-creative-suite-firefly-error-response
- name: GenerateSimilarRequest
  property_count: 5
  slug: adobe-creative-suite-firefly-generate-similar-request
- name: Adobe Firefly Generation Request and Response
  property_count: 0
  slug: adobe-creative-suite-firefly-generation
- name: GenerationStatus
  property_count: 6
  slug: adobe-creative-suite-firefly-generation-status
- name: ImageExpandRequest
  property_count: 7
  slug: adobe-creative-suite-firefly-image-expand-request
- name: ImageFillRequest
  property_count: 6
  slug: adobe-creative-suite-firefly-image-fill-request
- name: ImageGenerateRequest
  property_count: 8
  slug: adobe-creative-suite-firefly-image-generate-request
- name: ImageSize
  property_count: 2
  slug: adobe-creative-suite-firefly-image-size
- name: InputImageReference
  property_count: 1
  slug: adobe-creative-suite-firefly-input-image-reference
- name: ObjectCompositeRequest
  property_count: 7
  slug: adobe-creative-suite-firefly-object-composite-request
- name: OutputImage
  property_count: 3
  slug: adobe-creative-suite-firefly-output-image
- name: StyleOptions
  property_count: 3
  slug: adobe-creative-suite-firefly-style-options
- name: VideoGenerateRequest
  property_count: 4
  slug: adobe-creative-suite-firefly-video-generate-request
- name: GenerateSimilarRequest
  property_count: 5
  slug: adobe-creative-suite-generatesimilarrequest
- name: GenerationStatus
  property_count: 6
  slug: adobe-creative-suite-generationstatus
- name: Adobe Creative Suite Image Job
  property_count: 8
  slug: adobe-creative-suite-image-job
- name: ImageExpandRequest
  property_count: 7
  slug: adobe-creative-suite-imageexpandrequest
- name: ImageFillRequest
  property_count: 6
  slug: adobe-creative-suite-imagefillrequest
- name: ImageGenerateRequest
  property_count: 8
  slug: adobe-creative-suite-imagegeneraterequest
- name: ImageSize
  property_count: 2
  slug: adobe-creative-suite-imagesize
- name: InputImageReference
  property_count: 1
  slug: adobe-creative-suite-inputimagereference
- name: JobError
  property_count: 3
  slug: adobe-creative-suite-joberror
- name: JobInput
  property_count: 3
  slug: adobe-creative-suite-jobinput
- name: JobOutput
  property_count: 6
  slug: adobe-creative-suite-joboutput
- name: JobStatus
  property_count: 6
  slug: adobe-creative-suite-jobstatus
- name: JobSubmitted
  property_count: 3
  slug: adobe-creative-suite-jobsubmitted
- name: Layer
  property_count: 10
  slug: adobe-creative-suite-layer
- name: LayerManageRequest
  property_count: 3
  slug: adobe-creative-suite-layermanagerequest
- name: LicenseHistoryResult
  property_count: 2
  slug: adobe-creative-suite-licensehistoryresult
- name: LicenseReference
  property_count: 2
  slug: adobe-creative-suite-licensereference
- name: LicenseRequest
  property_count: 4
  slug: adobe-creative-suite-licenserequest
- name: LicenseResponse
  property_count: 3
  slug: adobe-creative-suite-licenseresponse
- name: LicenseStatsResponse
  property_count: 2
  slug: adobe-creative-suite-licensestatsresponse
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-creative-suite-linearizepdfrequest
- name: MaskRequest
  property_count: 3
  slug: adobe-creative-suite-maskrequest
- name: MemberProfile
  property_count: 1
  slug: adobe-creative-suite-memberprofile
- name: ObjectCompositeRequest
  property_count: 7
  slug: adobe-creative-suite-objectcompositerequest
- name: OCRRequest
  property_count: 2
  slug: adobe-creative-suite-ocrrequest
- name: OperationStatus
  property_count: 3
  slug: adobe-creative-suite-operationstatus
- name: OperationSubmitted
  property_count: 1
  slug: adobe-creative-suite-operationsubmitted
- name: OutputImage
  property_count: 3
  slug: adobe-creative-suite-outputimage
- name: PageRange
  property_count: 2
  slug: adobe-creative-suite-pagerange
- name: AssetReference
  property_count: 1
  slug: adobe-creative-suite-pdf-services-asset-reference
- name: Asset
  property_count: 4
  slug: adobe-creative-suite-pdf-services-asset
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-creative-suite-pdf-services-asset-upload-request
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-creative-suite-pdf-services-asset-upload-response
- name: AutoTagRequest
  property_count: 3
  slug: adobe-creative-suite-pdf-services-auto-tag-request
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-creative-suite-pdf-services-combine-pdf-request
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-creative-suite-pdf-services-compress-pdf-request
- name: CreatePDFRequest
  property_count: 2
  slug: adobe-creative-suite-pdf-services-create-pdf-request
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-creative-suite-pdf-services-document-generation-request
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-creative-suite-pdf-services-export-pdf-request
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-creative-suite-pdf-services-linearize-pdf-request
- name: OCRRequest
  property_count: 2
  slug: adobe-creative-suite-pdf-services-ocr-request
- name: OperationStatus
  property_count: 3
  slug: adobe-creative-suite-pdf-services-operation-status
- name: OperationSubmitted
  property_count: 1
  slug: adobe-creative-suite-pdf-services-operation-submitted
- name: PageRange
  property_count: 2
  slug: adobe-creative-suite-pdf-services-page-range
- name: CutoutRequest
  property_count: 2
  slug: adobe-creative-suite-photoshop-cutout-request
- name: DocumentOperationsRequest
  property_count: 3
  slug: adobe-creative-suite-photoshop-document-operations-request
- name: DocumentOperations
  property_count: 3
  slug: adobe-creative-suite-photoshop-document-operations
- name: JobInput
  property_count: 3
  slug: adobe-creative-suite-photoshop-job-input
- name: JobOutput
  property_count: 6
  slug: adobe-creative-suite-photoshop-job-output
- name: JobStatus
  property_count: 6
  slug: adobe-creative-suite-photoshop-job-status
- name: JobSubmitted
  property_count: 3
  slug: adobe-creative-suite-photoshop-job-submitted
- name: LayerManageRequest
  property_count: 3
  slug: adobe-creative-suite-photoshop-layer-manage-request
- name: Layer
  property_count: 10
  slug: adobe-creative-suite-photoshop-layer
- name: MaskRequest
  property_count: 3
  slug: adobe-creative-suite-photoshop-mask-request
- name: ProductCropRequest
  property_count: 3
  slug: adobe-creative-suite-photoshop-product-crop-request
- name: RenderOutput
  property_count: 4
  slug: adobe-creative-suite-photoshop-render-output
- name: RenditionCreateRequest
  property_count: 2
  slug: adobe-creative-suite-photoshop-rendition-create-request
- name: StraightenRequest
  property_count: 2
  slug: adobe-creative-suite-photoshop-straighten-request
- name: TextEditRequest
  property_count: 3
  slug: adobe-creative-suite-photoshop-text-edit-request
- name: ProductCropRequest
  property_count: 3
  slug: adobe-creative-suite-productcroprequest
- name: RenderOutput
  property_count: 4
  slug: adobe-creative-suite-renderoutput
- name: RenditionCreateRequest
  property_count: 2
  slug: adobe-creative-suite-renditioncreaterequest
- name: SearchResult
  property_count: 2
  slug: adobe-creative-suite-searchresult
- name: SmartObjectRequest
  property_count: 3
  slug: adobe-creative-suite-smartobjectrequest
- name: Category
  property_count: 4
  slug: adobe-creative-suite-stock-category
- name: ErrorResponse
  property_count: 2
  slug: adobe-creative-suite-stock-error-response
- name: Adobe Stock File
  property_count: 23
  slug: adobe-creative-suite-stock-file
- name: LicenseHistoryResult
  property_count: 2
  slug: adobe-creative-suite-stock-license-history-result
- name: LicenseReference
  property_count: 2
  slug: adobe-creative-suite-stock-license-reference
- name: LicenseRequest
  property_count: 4
  slug: adobe-creative-suite-stock-license-request
- name: LicenseResponse
  property_count: 3
  slug: adobe-creative-suite-stock-license-response
- name: LicenseStatsResponse
  property_count: 2
  slug: adobe-creative-suite-stock-license-stats-response
- name: MemberProfile
  property_count: 1
  slug: adobe-creative-suite-stock-member-profile
- name: SearchResult
  property_count: 2
  slug: adobe-creative-suite-stock-search-result
- name: StockFileResponse
  property_count: 1
  slug: adobe-creative-suite-stock-stock-file-response
- name: StockFile
  property_count: 18
  slug: adobe-creative-suite-stock-stock-file
- name: StockFile
  property_count: 18
  slug: adobe-creative-suite-stockfile
- name: StockFileResponse
  property_count: 1
  slug: adobe-creative-suite-stockfileresponse
- name: StraightenRequest
  property_count: 2
  slug: adobe-creative-suite-straightenrequest
- name: StyleOptions
  property_count: 3
  slug: adobe-creative-suite-styleoptions
- name: StylePreset
  property_count: 0
  slug: adobe-creative-suite-stylepreset
- name: TextEditRequest
  property_count: 3
  slug: adobe-creative-suite-texteditrequest
- name: VideoGenerateRequest
  property_count: 4
  slug: adobe-creative-suite-videogeneraterequest
json_structures:
- name: Adobe Creative Suite Firefly Async Job Submitted Structure
  property_count: 2
  slug: adobe-creative-suite-firefly-async-job-submitted-structure
- name: Adobe Creative Suite Firefly Error Response Structure
  property_count: 3
  slug: adobe-creative-suite-firefly-error-response-structure
- name: Adobe Creative Suite Firefly Generate Similar Request Structure
  property_count: 5
  slug: adobe-creative-suite-firefly-generate-similar-request-structure
- name: Adobe Creative Suite Firefly Generation Status Structure
  property_count: 6
  slug: adobe-creative-suite-firefly-generation-status-structure
- name: Adobe Creative Suite Firefly Generation Structure
  property_count: 0
  slug: adobe-creative-suite-firefly-generation-structure
- name: Adobe Creative Suite Firefly Image Expand Request Structure
  property_count: 7
  slug: adobe-creative-suite-firefly-image-expand-request-structure
- name: Adobe Creative Suite Firefly Image Fill Request Structure
  property_count: 6
  slug: adobe-creative-suite-firefly-image-fill-request-structure
- name: Adobe Creative Suite Firefly Image Generate Request Structure
  property_count: 8
  slug: adobe-creative-suite-firefly-image-generate-request-structure
- name: Adobe Creative Suite Firefly Image Size Structure
  property_count: 2
  slug: adobe-creative-suite-firefly-image-size-structure
- name: Adobe Creative Suite Firefly Input Image Reference Structure
  property_count: 1
  slug: adobe-creative-suite-firefly-input-image-reference-structure
- name: Adobe Creative Suite Firefly Object Composite Request Structure
  property_count: 7
  slug: adobe-creative-suite-firefly-object-composite-request-structure
- name: Adobe Creative Suite Firefly Output Image Structure
  property_count: 3
  slug: adobe-creative-suite-firefly-output-image-structure
- name: Adobe Creative Suite Firefly Style Options Structure
  property_count: 3
  slug: adobe-creative-suite-firefly-style-options-structure
- name: Adobe Creative Suite Firefly Video Generate Request Structure
  property_count: 4
  slug: adobe-creative-suite-firefly-video-generate-request-structure
- name: Adobe Creative Suite Image Job Structure
  property_count: 8
  slug: adobe-creative-suite-image-job-structure
- name: Adobe Creative Suite Pdf Services Asset Reference Structure
  property_count: 1
  slug: adobe-creative-suite-pdf-services-asset-reference-structure
- name: Adobe Creative Suite Pdf Services Asset Structure
  property_count: 4
  slug: adobe-creative-suite-pdf-services-asset-structure
- name: Adobe Creative Suite Pdf Services Asset Upload Request Structure
  property_count: 1
  slug: adobe-creative-suite-pdf-services-asset-upload-request-structure
- name: Adobe Creative Suite Pdf Services Asset Upload Response Structure
  property_count: 2
  slug: adobe-creative-suite-pdf-services-asset-upload-response-structure
- name: Adobe Creative Suite Pdf Services Auto Tag Request Structure
  property_count: 3
  slug: adobe-creative-suite-pdf-services-auto-tag-request-structure
- name: Adobe Creative Suite Pdf Services Combine Pdf Request Structure
  property_count: 1
  slug: adobe-creative-suite-pdf-services-combine-pdf-request-structure
- name: Adobe Creative Suite Pdf Services Compress Pdf Request Structure
  property_count: 2
  slug: adobe-creative-suite-pdf-services-compress-pdf-request-structure
- name: Adobe Creative Suite Pdf Services Create Pdf Request Structure
  property_count: 2
  slug: adobe-creative-suite-pdf-services-create-pdf-request-structure
- name: Adobe Creative Suite Pdf Services Document Generation Request Structure
  property_count: 4
  slug: adobe-creative-suite-pdf-services-document-generation-request-structure
- name: Adobe Creative Suite Pdf Services Export Pdf Request Structure
  property_count: 3
  slug: adobe-creative-suite-pdf-services-export-pdf-request-structure
- name: Adobe Creative Suite Pdf Services Linearize Pdf Request Structure
  property_count: 1
  slug: adobe-creative-suite-pdf-services-linearize-pdf-request-structure
- name: Adobe Creative Suite Pdf Services Ocr Request Structure
  property_count: 2
  slug: adobe-creative-suite-pdf-services-ocr-request-structure
- name: Adobe Creative Suite Pdf Services Operation Status Structure
  property_count: 3
  slug: adobe-creative-suite-pdf-services-operation-status-structure
- name: Adobe Creative Suite Pdf Services Operation Submitted Structure
  property_count: 1
  slug: adobe-creative-suite-pdf-services-operation-submitted-structure
- name: Adobe Creative Suite Pdf Services Page Range Structure
  property_count: 2
  slug: adobe-creative-suite-pdf-services-page-range-structure
- name: Adobe Creative Suite Photoshop Cutout Request Structure
  property_count: 2
  slug: adobe-creative-suite-photoshop-cutout-request-structure
- name: Adobe Creative Suite Photoshop Document Operations Request Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-document-operations-request-structure
- name: Adobe Creative Suite Photoshop Document Operations Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-document-operations-structure
- name: Adobe Creative Suite Photoshop Job Input Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-job-input-structure
- name: Adobe Creative Suite Photoshop Job Output Structure
  property_count: 6
  slug: adobe-creative-suite-photoshop-job-output-structure
- name: Adobe Creative Suite Photoshop Job Status Structure
  property_count: 6
  slug: adobe-creative-suite-photoshop-job-status-structure
- name: Adobe Creative Suite Photoshop Job Submitted Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-job-submitted-structure
- name: Adobe Creative Suite Photoshop Layer Manage Request Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-layer-manage-request-structure
- name: Adobe Creative Suite Photoshop Layer Structure
  property_count: 10
  slug: adobe-creative-suite-photoshop-layer-structure
- name: Adobe Creative Suite Photoshop Mask Request Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-mask-request-structure
- name: Adobe Creative Suite Photoshop Product Crop Request Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-product-crop-request-structure
- name: Adobe Creative Suite Photoshop Render Output Structure
  property_count: 4
  slug: adobe-creative-suite-photoshop-render-output-structure
- name: Adobe Creative Suite Photoshop Rendition Create Request Structure
  property_count: 2
  slug: adobe-creative-suite-photoshop-rendition-create-request-structure
- name: Adobe Creative Suite Photoshop Straighten Request Structure
  property_count: 2
  slug: adobe-creative-suite-photoshop-straighten-request-structure
- name: Adobe Creative Suite Photoshop Text Edit Request Structure
  property_count: 3
  slug: adobe-creative-suite-photoshop-text-edit-request-structure
- name: Adobe Creative Suite Stock Category Structure
  property_count: 4
  slug: adobe-creative-suite-stock-category-structure
- name: Adobe Creative Suite Stock Error Response Structure
  property_count: 2
  slug: adobe-creative-suite-stock-error-response-structure
- name: Adobe Creative Suite Stock File Structure
  property_count: 23
  slug: adobe-creative-suite-stock-file-structure
- name: Adobe Creative Suite Stock License History Result Structure
  property_count: 2
  slug: adobe-creative-suite-stock-license-history-result-structure
- name: Adobe Creative Suite Stock License Reference Structure
  property_count: 2
  slug: adobe-creative-suite-stock-license-reference-structure
- name: Adobe Creative Suite Stock License Request Structure
  property_count: 4
  slug: adobe-creative-suite-stock-license-request-structure
- name: Adobe Creative Suite Stock License Response Structure
  property_count: 3
  slug: adobe-creative-suite-stock-license-response-structure
- name: Adobe Creative Suite Stock License Stats Response Structure
  property_count: 2
  slug: adobe-creative-suite-stock-license-stats-response-structure
- name: Adobe Creative Suite Stock Member Profile Structure
  property_count: 1
  slug: adobe-creative-suite-stock-member-profile-structure
- name: Adobe Creative Suite Stock Search Result Structure
  property_count: 2
  slug: adobe-creative-suite-stock-search-result-structure
- name: Adobe Creative Suite Stock Stock File Response Structure
  property_count: 1
  slug: adobe-creative-suite-stock-stock-file-response-structure
- name: Adobe Creative Suite Stock Stock File Structure
  property_count: 18
  slug: adobe-creative-suite-stock-stock-file-structure
- name: Adobe Creative Suite Structure
  property_count: 0
  slug: adobe-creative-suite-structure
jsonld:
- class_count: 56
  name: Adobe Creative Suite Context
  property_count: 99
  slug: adobe-creative-suite-context
layout: provider
modified: '2026-05-19'
name: Adobe Creative Suite
nav: Providers
network: true
overview: 'Adobe Creative Suite publishes 27 APIs on the [APIs.io](https://apis.io/) network, including Accessibility API, Artboard API, Assets API, and 24 more. Tagged areas include Creative, Design, Graphics, Photography, and Video.


  The Adobe Creative Suite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Adobe Creative Suite''s developer surface includes authentication, developer portal, signup flow, getting-started guide, documentation, engineering blog, Stack Overflow tag, and 39 more developer resources.'
plans:
- name: Adobe Creative Suite Plans Pricing
  plan_count: 1
  slug: adobe-creative-suite-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 1
  name: Adobe Creative Suite Rate Limits
  slug: adobe-creative-suite-rate-limits
rules:
- name: Adobe Creative Suite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: adobe-creative-suite-jsonschema-spectral-rules
- name: Adobe Creative Suite API Rules
  rule_count: 23
  severity_counts:
    error: 14
    hint: 0
    info: 2
    warn: 7
  slug: adobe-creative-suite-spectral-rules
score:
  band: strong
  composite: 61.9
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 80.4
    developer_ergonomics: 56.5
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 66.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe-creative-suite/refs/heads/main/screenshots/adobe-creative-suite-2026-06-20T164857.png
security:
- kind: authentication
  name: Adobe Creative Suite Authentication
  slug: adobe-creative-suite-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Adobe Creative Suite Domain Security
  slug: adobe-creative-suite-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Creative Suite Vulnerability Disclosure
  slug: adobe-creative-suite-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe-creative-suite
solutions:
- description: Complete suite of 20+ creative applications with API access.
  name: Adobe Creative Cloud
- description: Generative AI APIs combining Firefly, Photoshop, and Lightroom.
  name: Adobe Firefly Services
- description: PDF Services, Document Generation, and Acrobat Sign APIs.
  name: Adobe Acrobat Services
- description: Embeddable creative tools with quick actions and templates.
  name: Adobe Express
tags:
- Creative
- Design
- Graphics
- Photography
- Video
use_cases:
- description: Automate background removal, cropping, and enhancement for e-commerce.
  name: Product Photography Automation
- description: Generate personalized visual content using Firefly and template automation.
  name: Content Personalization at Scale
- description: PDF creation, conversion, signing, and archiving workflows.
  name: Document Workflow Automation
- description: Centralize brand assets in Creative Cloud Libraries for consistent usage.
  name: Brand Asset Management
- description: Automate video editing, rendering, and export with Premiere Pro APIs.
  name: Video Production Pipeline
- description: Automate layout, typesetting, and print-ready output with InDesign.
  name: Print Production
- description: Generate icon sets, components, and design tokens from data.
  name: Design System Generation
- description: Export optimized SVGs, images, and fonts for web applications.
  name: Web Asset Pipeline
website: https://developer.adobe.com/
---
