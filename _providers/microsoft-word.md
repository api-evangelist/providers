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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Microsoft Word Agentic Access
  operation_count: 55
  slug: microsoft-word-agentic-access
  summary_line: 55 operations · 27 acting
api_count: 19
apis:
- description: Server-side document conversion and automation service for SharePoint. Supports batch conversion of Word documents to PDF, XPS, and other formats without user interaction.
  name: Word Automation Services (SharePoint)
  slug: word-automation-services-sharepoint
- description: Operations on the document body content
  name: Microsoft Word Body API
  slug: microsoft-word-body-api
- description: Operations for checking in and out files
  name: Microsoft Word Checkout API
  slug: microsoft-word-checkout-api
- description: Operations for managing comments and replies
  name: Microsoft Word Comments API
  slug: microsoft-word-comments-api
- description: Operations for uploading and downloading file content
  name: Microsoft Word Content API
  slug: microsoft-word-content-api
- description: Operations for managing content controls
  name: Microsoft Word Content Controls API
  slug: microsoft-word-content-controls-api
- description: Operations for creating, opening, and managing Word documents
  name: Microsoft Word Documents API
  slug: microsoft-word-documents-api
- description: Operations for managing files and folders in OneDrive and SharePoint
  name: Microsoft Word Drive Items API
  slug: microsoft-word-drive-items-api
- description: Operations for managing headers and footers
  name: Microsoft Word Headers And Footers API
  slug: microsoft-word-headers-and-footers-api
- description: Operations for managing images in documents
  name: Microsoft Word Images API
  slug: microsoft-word-images-api
- description: Operations for managing paragraphs in documents
  name: Microsoft Word Paragraphs API
  slug: microsoft-word-paragraphs-api
- description: Operations for managing sharing and permissions on drive items
  name: Microsoft Word Permissions API
  slug: microsoft-word-permissions-api
- description: Operations for managing document properties
  name: Microsoft Word Properties API
  slug: microsoft-word-properties-api
- description: Operations for searching files and folders
  name: Microsoft Word Search API
  slug: microsoft-word-search-api
- description: Operations for managing document sections
  name: Microsoft Word Sections API
  slug: microsoft-word-sections-api
- description: Operations for managing document styles
  name: Microsoft Word Styles API
  slug: microsoft-word-styles-api
- description: Operations for creating and managing tables
  name: Microsoft Word Tables API
  slug: microsoft-word-tables-api
- description: Operations for retrieving file thumbnails
  name: Microsoft Word Thumbnails API
  slug: microsoft-word-thumbnails-api
- description: Operations for managing file version history
  name: Microsoft Word Versions API
  slug: microsoft-word-versions-api
arazzos:
- description: Create a blank Word document, insert HTML content into its body, and save it.
  name: Microsoft Word Author Document from HTML
  slug: microsoft-word-author-document-workflow
- description: List the documents in a folder and branch to copy the first item or report an empty folder.
  name: Microsoft Word Browse Folder and Copy Document
  slug: microsoft-word-browse-and-copy-workflow
- description: Insert a heading, add a data table, list the resulting paragraphs, and save the document.
  name: Microsoft Word Build Report Body
  slug: microsoft-word-build-report-body-workflow
- description: Lock a Word document for editing, upload revised content, and check it back in with a comment.
  name: Microsoft Word Checkout Edit and Check In Document
  slug: microsoft-word-checkout-edit-checkin-workflow
- description: Create a Word document with the Open XML SDK, add a paragraph and a table, then convert it to PDF.
  name: Microsoft Word Generate Document and Convert to PDF
  slug: microsoft-word-generate-and-convert-pdf-workflow
- description: Read an Open XML document's structure, update its properties, list its paragraphs, and export it to HTML.
  name: Microsoft Word Inspect Document and Export HTML
  slug: microsoft-word-inspect-and-export-html-workflow
- description: Create a project folder, upload a Word document into it, and invite reviewers with edit access.
  name: Microsoft Word Organize Folder and Invite Reviewers
  slug: microsoft-word-organize-and-invite-workflow
- description: Rename a Word document, move it to a new folder, and list its version history.
  name: Microsoft Word Rename Move and Audit Document
  slug: microsoft-word-rename-move-and-audit-workflow
- description: Open a resumable upload session for a large Word document and confirm the stored item afterward.
  name: Microsoft Word Resumable Upload Session
  slug: microsoft-word-resumable-upload-session-workflow
- description: Search OneDrive for a Word document by name, confirm its metadata, and download its content.
  name: Microsoft Word Search and Download Document
  slug: microsoft-word-search-and-download-workflow
- description: Search a document body for text, update the document properties, and save it.
  name: Microsoft Word Search Body and Tag Document
  slug: microsoft-word-search-and-tag-workflow
- description: Upload a Word document to OneDrive, confirm its metadata, and generate an organization sharing link.
  name: Microsoft Word Upload and Share Document
  slug: microsoft-word-upload-and-share-workflow
artifact_total: 109
collections:
- collection_type: postman
  name: Microsoft Graph Word API
  slug: postman-microsoft-word-graph-api
- collection_type: postman
  name: Microsoft Word JavaScript API
  slug: postman-microsoft-word-javascript-api
- collection_type: postman
  name: Microsoft Word Open XML SDK
  slug: postman-microsoft-word-open-xml-sdk
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Graph Word Body API
  slug: open-microsoft-word-body-api
- collection_type: open
  name: Microsoft Graph Word Body Checkout API
  slug: open-microsoft-word-checkout-api
- collection_type: open
  name: Microsoft Graph Word Body Comments API
  slug: open-microsoft-word-comments-api
- collection_type: open
  name: Microsoft Graph Word Body Content API
  slug: open-microsoft-word-content-api
- collection_type: open
  name: Microsoft Graph Word Body Content Controls API
  slug: open-microsoft-word-content-controls-api
- collection_type: open
  name: Microsoft Graph Word Body Documents API
  slug: open-microsoft-word-documents-api
- collection_type: open
  name: Microsoft Graph Word Body Drive Items API
  slug: open-microsoft-word-drive-items-api
- collection_type: open
  name: Microsoft Graph Word Body Headers And Footers API
  slug: open-microsoft-word-headers-and-footers-api
- collection_type: open
  name: Microsoft Graph Word Body Images API
  slug: open-microsoft-word-images-api
- collection_type: open
  name: Microsoft Graph Word Body Paragraphs API
  slug: open-microsoft-word-paragraphs-api
- collection_type: open
  name: Microsoft Graph Word Body Permissions API
  slug: open-microsoft-word-permissions-api
- collection_type: open
  name: Microsoft Graph Word Body Properties API
  slug: open-microsoft-word-properties-api
- collection_type: open
  name: Microsoft Graph Word Body Search API
  slug: open-microsoft-word-search-api
- collection_type: open
  name: Microsoft Graph Word Body Sections API
  slug: open-microsoft-word-sections-api
- collection_type: open
  name: Microsoft Graph Word Body Styles API
  slug: open-microsoft-word-styles-api
- collection_type: open
  name: Microsoft Graph Word Body Tables API
  slug: open-microsoft-word-tables-api
- collection_type: open
  name: Microsoft Graph Word Body Thumbnails API
  slug: open-microsoft-word-thumbnails-api
- collection_type: open
  name: Microsoft Graph Word Body Versions API
  slug: open-microsoft-word-versions-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/OfficeDev/Open-XML-SDK/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/OfficeDev/Open-XML-SDK/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/dotnet/Open-XML-SDK/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dotnet/Open-XML-SDK/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dotnet/Open-XML-SDK/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/OfficeDev/Open-XML-SDK/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-word-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-word-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-word-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-word-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-word-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-word-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-word-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-word-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-word-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-word-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-word-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-word-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-word-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-word-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-word-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-word-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-word-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-word-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-word-graph-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-word-javascript-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-word-open-xml-sdk-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-word/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-author-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-browse-and-copy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-build-report-body-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-checkout-edit-checkin-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-generate-and-convert-pdf-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-inspect-and-export-html-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-organize-and-invite-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-rename-move-and-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-resumable-upload-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-search-and-download-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-search-and-tag-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-word-upload-and-share-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-word-online-training
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/graph
- group: start
  title: ''
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: start
  title: ''
  type: Signup
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/get-started
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/graph/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- group: other
  title: ''
  type: X
  url: https://twitter.com/MSGraphDev
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@Microsoft365Developer
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/browse/?products=ms-graph
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-word-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-word-vocabulary.yaml
created: '2024'
description: APIs for Microsoft Word document creation, manipulation, and automation across Microsoft 365 cloud services, Office Add-ins, SharePoint, and Open XML document processing.
examples:
- key_count: 14
  name: Graph Api Drive Item Example
  slug: graph-api-drive-item-example
- key_count: 4
  name: Graph Api Permission Example
  slug: graph-api-permission-example
- key_count: 6
  name: Javascript Api Comment Example
  slug: javascript-api-comment-example
- key_count: 8
  name: Javascript Api Content Control Example
  slug: javascript-api-content-control-example
- key_count: 8
  name: Javascript Api Paragraph Example
  slug: javascript-api-paragraph-example
- key_count: 6
  name: Javascript Api Table Example
  slug: javascript-api-table-example
- key_count: 14
  name: Open Xml Sdk Document Properties Example
  slug: open-xml-sdk-document-properties-example
features:
- description: Programmatically create Word documents from templates or scratch using REST APIs or JavaScript.
  name: Document Creation
- description: Convert Word documents to PDF, HTML, and other formats using server-side automation services.
  name: Document Conversion
- description: Insert, edit, and format text, paragraphs, tables, images, and content controls in Word documents.
  name: Content Manipulation
- description: Track changes, manage comments, co-authoring sessions, and revision history through APIs.
  name: Collaboration
- description: Mail merge, document assembly, and template-based document generation for enterprise workflows.
  name: Template Processing
- description: Access and manipulate Word documents stored in OneDrive, SharePoint, and Microsoft 365 cloud services.
  name: Cloud Storage Integration
- description: Build custom Word add-ins with JavaScript APIs for task panes, content insertion, and document automation.
  name: Add-In Extensibility
- description: Low-level manipulation of Word document structure using the ECMA-376 Open XML standard.
  name: Open XML Processing
finops:
- name: Microsoft Word Finops
  service_category: Productivity / Documents
  slug: microsoft-word-finops
image: /assets/icons/microsoft-word.png
integrations:
- description: Store, manage, and collaborate on Word documents through SharePoint document libraries and workflows.
  name: Microsoft SharePoint
- description: Access and sync Word documents via OneDrive cloud storage through Microsoft Graph APIs.
  name: Microsoft OneDrive
- description: Collaborate on Word documents directly within Teams channels and chat conversations.
  name: Microsoft Teams
- description: Automate Word document workflows including creation, conversion, and approval routing with Power Automate flows.
  name: Microsoft Power Automate
- description: AI-powered document creation, editing, and summarization through Copilot agents with add-in actions.
  name: Microsoft Copilot
- description: OAuth 2.0 authentication and authorization for secure API access through Microsoft Identity Platform.
  name: Azure Active Directory
json_schemas:
- name: DriveItem
  property_count: 15
  slug: graph-api-drive-item
- name: Permission
  property_count: 4
  slug: graph-api-permission
- name: Comment
  property_count: 6
  slug: javascript-api-comment
- name: ContentControl
  property_count: 8
  slug: javascript-api-content-control
- name: Paragraph
  property_count: 8
  slug: javascript-api-paragraph
- name: Table
  property_count: 6
  slug: javascript-api-table
- name: OpenXmlDocumentProperties
  property_count: 14
  slug: open-xml-sdk-document-properties
json_structures:
- name: Graph Api Drive Item Structure
  property_count: 10
  slug: graph-api-drive-item-structure
- name: Graph Api Permission Structure
  property_count: 3
  slug: graph-api-permission-structure
- name: Javascript Api Comment Structure
  property_count: 6
  slug: javascript-api-comment-structure
- name: Javascript Api Content Control Structure
  property_count: 8
  slug: javascript-api-content-control-structure
- name: Javascript Api Paragraph Structure
  property_count: 8
  slug: javascript-api-paragraph-structure
- name: Javascript Api Table Structure
  property_count: 6
  slug: javascript-api-table-structure
- name: Open Xml Sdk Document Properties Structure
  property_count: 14
  slug: open-xml-sdk-document-properties-structure
jsonld:
- class_count: 11
  name: Microsoft Word Graph Api Context
  property_count: 16
  slug: microsoft-word-graph-api-context
- class_count: 10
  name: Microsoft Word Javascript Api Context
  property_count: 27
  slug: microsoft-word-javascript-api-context
- class_count: 4
  name: Microsoft Word Open Xml Sdk Context
  property_count: 23
  slug: microsoft-word-open-xml-sdk-context
layout: provider
mcp_servers:
- description: ''
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-06-20'
name: Microsoft Word
nav: Providers
network: true
overview: 'Microsoft Word publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Body API, Checkout API, Comments API, and 15 more. Tagged areas include Documents, Microsoft-365, Office, Productivity, and Word Processing.


  The Microsoft Word catalog on APIs.io includes 3 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Word''s developer surface includes authentication, sandbox, changelog, CLI, developer portal, developer console, signup flow, and 53 more developer resources.'
plans:
- name: Microsoft Word Plans Pricing
  plan_count: 7
  slug: microsoft-word-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Microsoft Word Rate Limits
  slug: microsoft-word-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Microsoft Word API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-word-jsonschema-spectral-rules
- effective_rule_count: 82
  extends:
  - spectral:oas
  name: Microsoft Word API Rules
  rule_count: 41
  severity_counts:
    error: 18
    hint: 0
    info: 4
    warn: 19
  slug: microsoft-word-spectral-rules
scopes:
- name: Microsoft Word Scopes
  scope_count: 8
  slug: microsoft-word-scopes
  summary_line: 8 scopes · authorizationCode
score:
  band: strong
  composite: 55.0
  delta: 7.4
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 45.5
    contract_quality: 34.0
    developer_ergonomics: 92.9
    discoverability: 61.1
    governance: 45.5
    operational_transparency: 36.8
  previous_composite: 47.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 18
      marker_coverage: 100.0
      total: 18
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-word/refs/heads/main/screenshots/microsoft-word-2026-08-07T172841.png
security:
- kind: authentication
  name: Microsoft Word Authentication
  slug: microsoft-word-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Word Domain Security
  slug: microsoft-word-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Word Vulnerability Disclosure
  slug: microsoft-word-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Word Trust Center
  slug: microsoft-word-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, FedRAMP, FIPS 140-2, HIPAA
slug: microsoft-word
tags:
- Documents
- Microsoft-365
- Office
- Productivity
- Word Processing
use_cases:
- description: Generate standardized reports from data sources using templates and API-driven document creation.
  name: Automated Report Generation
- description: Assemble legal documents by merging clauses, terms, and client data into Word templates.
  name: Contract and Legal Document Assembly
- description: Automate review cycles with tracked changes, comments, and approval workflows via APIs.
  name: Document Review Workflows
- description: Process large volumes of Word documents for format conversion, content extraction, or metadata updates.
  name: Bulk Document Processing
- description: Build task pane add-ins that connect Word to CRM, ERP, or other business systems for data insertion.
  name: Custom Business Add-Ins
- description: Ensure regulatory compliance by automating document formatting, metadata tagging, and archiving.
  name: Compliance Document Management
website: https://developer.microsoft.com/en-us/graph
---
