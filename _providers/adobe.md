---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Adobe Agentic Access
  operation_count: 22
  slug: adobe-agentic-access
  summary_line: 22 operations · 20 acting
api_count: 32
apis:
- description: Extract text, images, tables, and more from native and scanned PDFs into structured JSON using AI technology.
  name: Adobe PDF Extract API
  slug: adobe-pdf-extract-api
- description: Embed e-signature workflows and manage signing agreements programmatically.
  name: Adobe Acrobat Sign API
  slug: adobe-acrobat-sign-api
- description: Access and analyze digital marketing data and metrics.
  name: Adobe Analytics API
  slug: adobe-analytics-api
- description: Generate and edit images using generative AI models through a RESTful API.
  name: Adobe Firefly API
  slug: adobe-firefly-api
- description: Build and manage customer experience applications on Adobe Experience Platform.
  name: Adobe Experience Platform API
  slug: adobe-experience-platform-api
- description: Search, license, and manage Adobe Stock assets including photos, vectors, videos, and templates.
  name: Adobe Stock API
  slug: adobe-stock-api
- description: Build and integrate e-commerce applications with REST, GraphQL, and SOAP web APIs.
  name: Adobe Commerce API
  slug: adobe-commerce-api
- description: Automate marketing processes and manage leads, campaigns, and assets via REST APIs.
  name: Adobe Marketo Engage API
  slug: adobe-marketo-engage-api
- description: Manage work, projects, tasks, and resources programmatically with a REST API.
  name: Adobe Workfront API
  slug: adobe-workfront-api
- description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  name: Adobe User Management API
  slug: adobe-user-management-api
- description: Subscribe to and receive near real-time events from Adobe services for event-driven integrations.
  name: Adobe I/O Events API
  slug: adobe-io-events-api
- description: Create, read, update, and delete content, assets, and forms in Adobe Experience Manager as a Cloud Service.
  name: Adobe Experience Manager API
  slug: adobe-experience-manager-api
- description: Automatically add accessibility tags to PDF documents using AI.
  name: Adobe PDF Services Accessibility Auto-Tag API
  slug: adobe-accessibility-auto-tag-api
- description: Upload and manage assets (source files) for PDF operations.
  name: Adobe PDF Services Assets API
  slug: adobe-assets-api
- description: Combine multiple PDF documents into a single PDF.
  name: Adobe PDF Services Combine PDF API
  slug: adobe-combine-pdf-api
- description: Reduce the file size of PDF documents while maintaining quality.
  name: Adobe PDF Services Compress PDF API
  slug: adobe-compress-pdf-api
- description: Create PDF documents from supported file formats including Microsoft Office, images, and HTML.
  name: Adobe PDF Services Create PDF API
  slug: adobe-create-pdf-api
- description: Delete specific pages from a PDF document.
  name: Adobe PDF Services Delete Pages API
  slug: adobe-delete-pages-api
- description: Generate PDF and Word documents from templates with dynamic JSON data.
  name: Adobe PDF Services Document Generation API
  slug: adobe-document-generation-api
- description: Export (convert) PDF documents to other formats such as DOCX, PPTX, XLSX, images, and RTF.
  name: Adobe PDF Services Export PDF API
  slug: adobe-export-pdf-api
- description: Extract text, tables, and figures from PDF documents into structured JSON output.
  name: Adobe PDF Services Extract PDF API
  slug: adobe-extract-pdf-api
- description: Insert pages from one PDF into another.
  name: Adobe PDF Services Insert Pages API
  slug: adobe-insert-pages-api
- description: Poll for the status and results of asynchronous PDF operations.
  name: Adobe PDF Services Jobs API
  slug: adobe-jobs-api
- description: Optimize PDFs for fast web viewing (linearization).
  name: Adobe PDF Services Linearize PDF API
  slug: adobe-linearize-pdf-api
- description: Apply optical character recognition to scanned PDFs to make text searchable and selectable.
  name: Adobe PDF Services OCR API
  slug: adobe-ocr-api
- description: Retrieve metadata and properties from PDF documents.
  name: Adobe PDF Services PDF Properties API
  slug: adobe-pdf-properties-api
- description: Add password protection and encryption to PDF documents.
  name: Adobe PDF Services Protect PDF API
  slug: adobe-protect-pdf-api
- description: Remove password protection from PDF documents.
  name: Adobe PDF Services Remove Protection API
  slug: adobe-remove-protection-api
- description: Reorder pages within a PDF document.
  name: Adobe PDF Services Reorder Pages API
  slug: adobe-reorder-pages-api
- description: Replace pages in a PDF with pages from another PDF.
  name: Adobe PDF Services Replace Pages API
  slug: adobe-replace-pages-api
- description: Rotate pages within a PDF document.
  name: Adobe PDF Services Rotate Pages API
  slug: adobe-rotate-pages-api
- description: Split a PDF document into multiple smaller PDFs.
  name: Adobe PDF Services Split PDF API
  slug: adobe-split-pdf-api
arazzos:
- description: Upload a PDF, auto-tag it for accessibility, poll the job, and fetch the tagged result.
  name: Adobe Auto-tag a PDF For Accessibility
  slug: adobe-auto-tag-pdf-workflow
- description: Upload two PDFs, combine them into a single document, poll the job, and fetch the merged result.
  name: Adobe Combine Two PDFs Into One
  slug: adobe-combine-pdfs-workflow
- description: Upload a PDF, compress it to reduce file size, poll the job, and fetch the smaller result.
  name: Adobe Compress a PDF
  slug: adobe-compress-pdf-workflow
- description: Upload a source document, convert it to PDF, poll the async job, and fetch the download URI.
  name: Adobe Create PDF From Source File
  slug: adobe-create-pdf-workflow
- description: Upload a PDF, delete a page range, poll the job, and fetch the trimmed result.
  name: Adobe Delete Pages From a PDF
  slug: adobe-delete-pages-workflow
- description: Resolve a download URI for a finished output asset, then delete it from the platform.
  name: Adobe Download Then Clean Up an Asset
  slug: adobe-download-and-cleanup-asset-workflow
- description: Upload a PDF, export it to DOCX/PPTX/XLSX/RTF/image, poll the job, and fetch the result.
  name: Adobe Export PDF To Another Format
  slug: adobe-export-pdf-workflow
- description: Upload a PDF, extract text and tables into structured JSON, poll the job, and fetch the result.
  name: Adobe Extract Content From a PDF
  slug: adobe-extract-pdf-workflow
- description: Upload a Word template, merge JSON data into it, poll the job, and fetch the generated document.
  name: Adobe Generate a Document From a Template
  slug: adobe-generate-document-workflow
- description: Upload a PDF, request its metadata properties, and poll the job until done or failed.
  name: Adobe Inspect PDF Properties
  slug: adobe-inspect-pdf-properties-workflow
- description: Upload a scanned PDF, run OCR to make it searchable, poll the job, and fetch the result.
  name: Adobe OCR a Scanned PDF
  slug: adobe-ocr-pdf-workflow
- description: Upload a PDF, apply password protection and encryption, poll the job, and fetch the result.
  name: Adobe Protect a PDF With a Password
  slug: adobe-protect-pdf-workflow
- description: Upload a protected PDF, unlock it with its password, poll the job, and fetch the result.
  name: Adobe Remove Protection From a PDF
  slug: adobe-remove-protection-workflow
- description: Upload a PDF, rotate a page range, poll the job, and fetch the rotated result.
  name: Adobe Rotate Pages In a PDF
  slug: adobe-rotate-pages-workflow
- description: Upload a PDF, split it by page count into multiple files, poll the job, and fetch the result.
  name: Adobe Split a PDF
  slug: adobe-split-pdf-workflow
artifact_total: 213
collections:
- collection_type: postman
  name: Adobe PDF Services API
  slug: postman-adobe-pdf-services-api
- collection_type: open
  name: Adobe PDF Services API
  slug: open-adobe-pdf-services-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/adobe-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/adobe-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-auto-tag-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-combine-pdfs-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-compress-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-create-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-delete-pages-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-download-and-cleanup-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-export-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-extract-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-generate-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-inspect-pdf-properties-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-ocr-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-protect-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-remove-protection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-rotate-pages-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/adobe-split-pdf-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
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
  type: Support
  url: https://developer.adobe.com/developer-support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs/
- group: build
  title: ''
  type: SDKs
  url: https://developer.adobe.com/apis
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/console/
- group: start
  title: ''
  type: Login
  url: https://developer.adobe.com/console/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/adobe-pdf-services-api-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/adobe-pdf-services-asset-upload-request-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/adobe-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/adobe-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://blog.developer.adobe.com/en/publish/2025/09/introducing-the-adobe-express-add-on-dev-mcp-server-beta
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.adobe.com/document-services/docs/overview/limits/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adobe.com/firefly-services/docs/firefly-api/
created: '2024-01-01'
description: Adobe provides APIs and developer resources for its creative, document, and experience cloud platforms. Developers can integrate with PDF services, Creative Cloud, generative AI (Firefly), analytics, e-commerce, e-signatures, and many other Adobe products and services.
examples:
- key_count: 6
  name: Adobe Autotagpdf Example
  slug: adobe-autotagpdf-example
- key_count: 6
  name: Adobe Combinepdf Example
  slug: adobe-combinepdf-example
- key_count: 6
  name: Adobe Compresspdf Example
  slug: adobe-compresspdf-example
- key_count: 6
  name: Adobe Createpdf Example
  slug: adobe-createpdf-example
- key_count: 6
  name: Adobe Deletepages Example
  slug: adobe-deletepages-example
- key_count: 6
  name: Adobe Exportpdf Example
  slug: adobe-exportpdf-example
- key_count: 6
  name: Adobe Extractpdf Example
  slug: adobe-extractpdf-example
- key_count: 6
  name: Adobe Generatedocument Example
  slug: adobe-generatedocument-example
- key_count: 6
  name: Adobe Getasset Example
  slug: adobe-getasset-example
- key_count: 6
  name: Adobe Getjobstatus Example
  slug: adobe-getjobstatus-example
- key_count: 6
  name: Adobe Getpdfproperties Example
  slug: adobe-getpdfproperties-example
- key_count: 6
  name: Adobe Insertpages Example
  slug: adobe-insertpages-example
- key_count: 6
  name: Adobe Linearizepdf Example
  slug: adobe-linearizepdf-example
- key_count: 6
  name: Adobe Ocrpdf Example
  slug: adobe-ocrpdf-example
- key_count: 2
  name: Adobe Pdf Services Asset Download Response Example
  slug: adobe-pdf-services-asset-download-response-example
- key_count: 1
  name: Adobe Pdf Services Asset Reference Example
  slug: adobe-pdf-services-asset-reference-example
- key_count: 1
  name: Adobe Pdf Services Asset Upload Request Example
  slug: adobe-pdf-services-asset-upload-request-example
- key_count: 2
  name: Adobe Pdf Services Asset Upload Response Example
  slug: adobe-pdf-services-asset-upload-response-example
- key_count: 3
  name: Adobe Pdf Services Auto Tag Request Example
  slug: adobe-pdf-services-auto-tag-request-example
- key_count: 1
  name: Adobe Pdf Services Combine Pdf Request Example
  slug: adobe-pdf-services-combine-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Compress Pdf Request Example
  slug: adobe-pdf-services-compress-pdf-request-example
- key_count: 6
  name: Adobe Pdf Services Create Pdf Request Example
  slug: adobe-pdf-services-create-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Delete Pages Request Example
  slug: adobe-pdf-services-delete-pages-request-example
- key_count: 4
  name: Adobe Pdf Services Document Generation Request Example
  slug: adobe-pdf-services-document-generation-request-example
- key_count: 1
  name: Adobe Pdf Services Error Response Example
  slug: adobe-pdf-services-error-response-example
- key_count: 3
  name: Adobe Pdf Services Export Pdf Request Example
  slug: adobe-pdf-services-export-pdf-request-example
- key_count: 6
  name: Adobe Pdf Services Extract Pdf Request Example
  slug: adobe-pdf-services-extract-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Insert Pages Request Example
  slug: adobe-pdf-services-insert-pages-request-example
- key_count: 3
  name: Adobe Pdf Services Job Status Response Example
  slug: adobe-pdf-services-job-status-response-example
- key_count: 1
  name: Adobe Pdf Services Linearize Pdf Request Example
  slug: adobe-pdf-services-linearize-pdf-request-example
- key_count: 3
  name: Adobe Pdf Services Ocr Request Example
  slug: adobe-pdf-services-ocr-request-example
- key_count: 2
  name: Adobe Pdf Services Page Range Example
  slug: adobe-pdf-services-page-range-example
- key_count: 2
  name: Adobe Pdf Services Pdf Properties Request Example
  slug: adobe-pdf-services-pdf-properties-request-example
- key_count: 4
  name: Adobe Pdf Services Protect Pdf Request Example
  slug: adobe-pdf-services-protect-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Remove Protection Request Example
  slug: adobe-pdf-services-remove-protection-request-example
- key_count: 2
  name: Adobe Pdf Services Reorder Pages Request Example
  slug: adobe-pdf-services-reorder-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Replace Pages Request Example
  slug: adobe-pdf-services-replace-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Rotate Pages Request Example
  slug: adobe-pdf-services-rotate-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Split Pdf Request Example
  slug: adobe-pdf-services-split-pdf-request-example
- key_count: 6
  name: Adobe Protectpdf Example
  slug: adobe-protectpdf-example
- key_count: 6
  name: Adobe Removeprotection Example
  slug: adobe-removeprotection-example
- key_count: 6
  name: Adobe Reorderpages Example
  slug: adobe-reorderpages-example
- key_count: 6
  name: Adobe Replacepages Example
  slug: adobe-replacepages-example
- key_count: 6
  name: Adobe Rotatepages Example
  slug: adobe-rotatepages-example
- key_count: 6
  name: Adobe Splitpdf Example
  slug: adobe-splitpdf-example
- key_count: 6
  name: Adobe Uploadasset Example
  slug: adobe-uploadasset-example
features:
- PDF creation, conversion, and manipulation via REST API
- AI-powered PDF content extraction into structured JSON
- Generative AI image creation and editing with Firefly
- E-signature workflows with Acrobat Sign
- Digital analytics and marketing insights
- Customer data platform with Experience Platform
- Content management with Experience Manager
- Marketing automation with Marketo Engage
- E-commerce platform with Adobe Commerce
- Work management and project tracking with Workfront
- Event-driven integrations with I/O Events
- Stock asset search and licensing
finops:
- name: Adobe Finops
  service_category: Creative + Marketing + Document SaaS
  slug: adobe-finops
graphqls:
- description: ''
  name: Adobe GraphQL API
  slug: adobe-graphql
image: /assets/icons/adobe.png
integrations:
- Microsoft 365 and Teams integration
- Salesforce CRM integration
- Adobe Creative Cloud libraries
- Workfront and Jira project management
- SAP and Oracle ERP systems
- Shopify and Magento marketplaces
- Google Analytics and Tag Manager
- Slack and Microsoft Teams notifications
json_schemas:
- name: AssetDownloadResponse
  property_count: 2
  slug: adobe-assetdownloadresponse
- name: AssetReference
  property_count: 1
  slug: adobe-assetreference
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-assetuploadrequest
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-assetuploadresponse
- name: AutoTagRequest
  property_count: 3
  slug: adobe-autotagrequest
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-combinepdfrequest
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-compresspdfrequest
- name: CreatePDFRequest
  property_count: 6
  slug: adobe-createpdfrequest
- name: DeletePagesRequest
  property_count: 2
  slug: adobe-deletepagesrequest
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-documentgenerationrequest
- name: ErrorResponse
  property_count: 1
  slug: adobe-errorresponse
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-exportpdfrequest
- name: ExtractPDFRequest
  property_count: 6
  slug: adobe-extractpdfrequest
- name: InsertPagesRequest
  property_count: 2
  slug: adobe-insertpagesrequest
- name: JobStatusResponse
  property_count: 3
  slug: adobe-jobstatusresponse
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-linearizepdfrequest
- name: OCRRequest
  property_count: 3
  slug: adobe-ocrrequest
- name: PageRange
  property_count: 2
  slug: adobe-pagerange
- name: Adobe PDF Services Job
  property_count: 3
  slug: adobe-pdf-job
- name: AssetDownloadResponse
  property_count: 2
  slug: adobe-pdf-services-asset-download-response
- name: AssetReference
  property_count: 1
  slug: adobe-pdf-services-asset-reference
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-pdf-services-asset-upload-request
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-pdf-services-asset-upload-response
- name: AutoTagRequest
  property_count: 3
  slug: adobe-pdf-services-auto-tag-request
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-pdf-services-combine-pdf-request
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-pdf-services-compress-pdf-request
- name: CreatePDFRequest
  property_count: 6
  slug: adobe-pdf-services-create-pdf-request
- name: DeletePagesRequest
  property_count: 2
  slug: adobe-pdf-services-delete-pages-request
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-pdf-services-document-generation-request
- name: ErrorResponse
  property_count: 1
  slug: adobe-pdf-services-error-response
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-pdf-services-export-pdf-request
- name: ExtractPDFRequest
  property_count: 6
  slug: adobe-pdf-services-extract-pdf-request
- name: InsertPagesRequest
  property_count: 2
  slug: adobe-pdf-services-insert-pages-request
- name: JobStatusResponse
  property_count: 3
  slug: adobe-pdf-services-job-status-response
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-pdf-services-linearize-pdf-request
- name: OCRRequest
  property_count: 3
  slug: adobe-pdf-services-ocr-request
- name: PageRange
  property_count: 2
  slug: adobe-pdf-services-page-range
- name: PDFPropertiesRequest
  property_count: 2
  slug: adobe-pdf-services-pdf-properties-request
- name: ProtectPDFRequest
  property_count: 4
  slug: adobe-pdf-services-protect-pdf-request
- name: RemoveProtectionRequest
  property_count: 2
  slug: adobe-pdf-services-remove-protection-request
- name: ReorderPagesRequest
  property_count: 2
  slug: adobe-pdf-services-reorder-pages-request
- name: ReplacePagesRequest
  property_count: 2
  slug: adobe-pdf-services-replace-pages-request
- name: RotatePagesRequest
  property_count: 2
  slug: adobe-pdf-services-rotate-pages-request
- name: SplitPDFRequest
  property_count: 2
  slug: adobe-pdf-services-split-pdf-request
- name: PDFPropertiesRequest
  property_count: 2
  slug: adobe-pdfpropertiesrequest
- name: ProtectPDFRequest
  property_count: 4
  slug: adobe-protectpdfrequest
- name: RemoveProtectionRequest
  property_count: 2
  slug: adobe-removeprotectionrequest
- name: ReorderPagesRequest
  property_count: 2
  slug: adobe-reorderpagesrequest
- name: ReplacePagesRequest
  property_count: 2
  slug: adobe-replacepagesrequest
- name: RotatePagesRequest
  property_count: 2
  slug: adobe-rotatepagesrequest
- name: SplitPDFRequest
  property_count: 2
  slug: adobe-splitpdfrequest
json_structures:
- name: Adobe Pdf Services Asset Download Response Structure
  property_count: 2
  slug: adobe-pdf-services-asset-download-response-structure
- name: Adobe Pdf Services Asset Reference Structure
  property_count: 1
  slug: adobe-pdf-services-asset-reference-structure
- name: Adobe Pdf Services Asset Upload Request Structure
  property_count: 1
  slug: adobe-pdf-services-asset-upload-request-structure
- name: Adobe Pdf Services Asset Upload Response Structure
  property_count: 2
  slug: adobe-pdf-services-asset-upload-response-structure
- name: Adobe Pdf Services Auto Tag Request Structure
  property_count: 3
  slug: adobe-pdf-services-auto-tag-request-structure
- name: Adobe Pdf Services Combine Pdf Request Structure
  property_count: 1
  slug: adobe-pdf-services-combine-pdf-request-structure
- name: Adobe Pdf Services Compress Pdf Request Structure
  property_count: 2
  slug: adobe-pdf-services-compress-pdf-request-structure
- name: Adobe Pdf Services Create Pdf Request Structure
  property_count: 6
  slug: adobe-pdf-services-create-pdf-request-structure
- name: Adobe Pdf Services Delete Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-delete-pages-request-structure
- name: Adobe Pdf Services Document Generation Request Structure
  property_count: 4
  slug: adobe-pdf-services-document-generation-request-structure
- name: Adobe Pdf Services Error Response Structure
  property_count: 1
  slug: adobe-pdf-services-error-response-structure
- name: Adobe Pdf Services Export Pdf Request Structure
  property_count: 3
  slug: adobe-pdf-services-export-pdf-request-structure
- name: Adobe Pdf Services Extract Pdf Request Structure
  property_count: 6
  slug: adobe-pdf-services-extract-pdf-request-structure
- name: Adobe Pdf Services Insert Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-insert-pages-request-structure
- name: Adobe Pdf Services Job Status Response Structure
  property_count: 3
  slug: adobe-pdf-services-job-status-response-structure
- name: Adobe Pdf Services Linearize Pdf Request Structure
  property_count: 1
  slug: adobe-pdf-services-linearize-pdf-request-structure
- name: Adobe Pdf Services Ocr Request Structure
  property_count: 3
  slug: adobe-pdf-services-ocr-request-structure
- name: Adobe Pdf Services Page Range Structure
  property_count: 2
  slug: adobe-pdf-services-page-range-structure
- name: Adobe Pdf Services Pdf Properties Request Structure
  property_count: 2
  slug: adobe-pdf-services-pdf-properties-request-structure
- name: Adobe Pdf Services Protect Pdf Request Structure
  property_count: 4
  slug: adobe-pdf-services-protect-pdf-request-structure
- name: Adobe Pdf Services Remove Protection Request Structure
  property_count: 2
  slug: adobe-pdf-services-remove-protection-request-structure
- name: Adobe Pdf Services Reorder Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-reorder-pages-request-structure
- name: Adobe Pdf Services Replace Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-replace-pages-request-structure
- name: Adobe Pdf Services Rotate Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-rotate-pages-request-structure
- name: Adobe Pdf Services Split Pdf Request Structure
  property_count: 2
  slug: adobe-pdf-services-split-pdf-request-structure
- name: Adobe Structure
  property_count: 0
  slug: adobe-structure
jsonld:
- class_count: 45
  name: Adobe Context
  property_count: 51
  slug: adobe-context
- class_count: 0
  name: Adobe Pdf Services Context
  property_count: 0
  slug: adobe-pdf-services-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Adobe
nav: Providers
network: true
overview: 'Adobe publishes 20 APIs on the [APIs.io](https://apis.io/) network, including PDF Services Accessibility Auto-Tag API, PDF Services Assets API, PDF Services Combine PDF API, and 17 more. Tagged areas include Fortune 1000, Analytics, Creative Cloud, Digital Asset Management, and Document Services.


  The Adobe catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Adobe''s developer surface includes authentication, developer portal, developer console, support, engineering blog, getting-started guide, signup flow, and 35 more developer resources.'
paper_is_own: true
plans:
- name: Adobe Plans Pricing
  plan_count: 4
  slug: adobe-plans-pricing
press:
- date: '2026-05-25'
  title: Adobe
  url: https://www.facebook.com/Adobe/
- date: '2026-05-25'
  title: Adobe Inc.
  url: https://en.wikipedia.org/wiki/Adobe_Inc.
- date: '2026-05-25'
  title: Adobe (@adobe) · San Jose, CA
  url: https://www.instagram.com/adobe/?hl=en
- date: '2026-05-25'
  title: 'Adobe: Creative, marketing and document management ...'
  url: https://www.adobe.com/
- date: '2026-05-25'
  title: Adobe (@Adobe) / Posts / X
  url: https://x.com/Adobe
random_paper: 25
rate_limits:
- limit_count: 2
  name: Adobe Rate Limits
  slug: adobe-rate-limits
rules:
- name: Adobe API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: adobe-jsonschema-spectral-rules
- name: Adobe API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: adobe-spectral-rules
score:
  band: exemplar
  composite: 69.4
  delta: 0.0
  facets:
    commercial_clarity: 73.7
    contract_quality: 81.3
    developer_ergonomics: 63.0
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 57.9
  previous_composite: 69.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/screenshots/adobe-2026-07-25T181652.png
security:
- kind: authentication
  name: Adobe Authentication
  slug: adobe-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Adobe Domain Security
  slug: adobe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Vulnerability Disclosure
  slug: adobe-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: adobe
tags:
- Fortune 1000
- Analytics
- Creative Cloud
- Digital Asset Management
- Document Services
- E-Commerce
- E-Signatures
- Experience Cloud
- Generative AI
- Marketing
- PDF
- Work Management
use_cases:
- Automating document workflows with PDF Services API
- Extracting data from invoices and forms with PDF Extract
- Generating creative assets at scale with Firefly API
- Embedding e-signature capabilities into business applications
- Building personalized customer experiences with Experience Platform
- Automating marketing campaigns and lead management
- Managing digital content and assets across channels
- Building and managing e-commerce storefronts
website: https://developer.adobe.com/
---
