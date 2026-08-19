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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Nanonets Agentic Access
  operation_count: 20
  slug: nanonets-agentic-access
  summary_line: 20 operations · 16 acting
api_count: 10
apis:
- description: List external integrations connected to a Nanonets account (Postgres, MySQL, MSSQL, MongoDB, and other databases) and execute generic SQL queries against them in the context of a Nanonets workflow. Us
  name: Nanonets External Integrations API
  slug: nanonets-external-integrations-api
- description: Assign files to reviewers.
  name: Nanonets File Assignment API
  slug: nanonets-file-assignment-api
- description: Delete a processed file.
  name: Nanonets File Delete API
  slug: nanonets-file-delete-api
- description: Retry exports to configured downstream destinations.
  name: Nanonets File Export API
  slug: nanonets-file-export-api
- description: Approve and unapprove files post-extraction.
  name: Nanonets File Review API
  slug: nanonets-file-review-api
- description: Update or add extracted field values on a file.
  name: Nanonets File Update API
  slug: nanonets-file-update-api
- description: Predict on uploaded images or image URLs against a classification model.
  name: Nanonets Image Classification Predict API
  slug: nanonets-image-classification-predict-api
- description: Predict on uploaded files or file URLs against a Nanonets OCR model.
  name: Nanonets OCR Predict API
  slug: nanonets-ocr-predict-api
- description: Retrieve prediction results for a file, page, or batch.
  name: Nanonets OCR Retrieve API
  slug: nanonets-ocr-retrieve-api
- description: Upload training images and train or retrain an OCR model.
  name: Nanonets OCR Train API
  slug: nanonets-ocr-train-api
arazzos:
- description: Submit a large document for async OCR, then poll until the file-level prediction is ready.
  name: Nanonets Async OCR Predict and Poll
  slug: nanonets-async-ocr-predict-and-poll-workflow
- description: Async-predict a document by URL, poll until ready, then approve the file.
  name: Nanonets Async URL Predict Poll and Approve
  slug: nanonets-async-url-predict-poll-approve-workflow
- description: List a model's recent predictions, then approve the first unmoderated file.
  name: Nanonets Batch Review Pending Files
  slug: nanonets-batch-review-pending-files-workflow
- description: Classify an uploaded image and branch on whether a top label was predicted.
  name: Nanonets Classify Image and Branch
  slug: nanonets-classify-image-and-branch-workflow
- description: Pull a single page's prediction, correct its fields, then approve the file.
  name: Nanonets Page-Level Correct and Approve
  slug: nanonets-page-level-correct-and-approve-workflow
- description: Predict on a file, fetch the file-level result, and assign it to a reviewer.
  name: Nanonets Predict and Assign Reviewer
  slug: nanonets-predict-and-assign-reviewer-workflow
- description: Extract a document, then validate it against an external database integration.
  name: Nanonets Predict and Enrich with Database
  slug: nanonets-predict-and-enrich-with-database-workflow
- description: Predict on a file, correct its extracted fields, and retry the export.
  name: Nanonets Predict Correct and Re-export
  slug: nanonets-predict-correct-and-reexport-workflow
- description: List external integrations, pick the first one, and run a SQL-style query.
  name: Nanonets Resolve Integration and Query
  slug: nanonets-resolve-integration-and-query-workflow
- description: Run a sync OCR prediction on a small file, then approve or hold it for review.
  name: Nanonets Sync Predict and Review
  slug: nanonets-sync-predict-and-review-workflow
- description: Upload annotated local training images to an OCR model, then kick off training.
  name: Nanonets Upload Training Images and Train
  slug: nanonets-upload-training-images-and-train-workflow
- description: Add training images to an OCR model from public URLs, then start training.
  name: Nanonets Upload Training URLs and Train
  slug: nanonets-upload-training-urls-and-train-workflow
artifact_total: 115
collections:
- collection_type: postman
  name: Nanonets External Integrations API
  slug: postman-nanonets-external-integrations-api
- collection_type: postman
  name: Nanonets File Management API
  slug: postman-nanonets-file-management-api
- collection_type: postman
  name: Nanonets Image Classification API
  slug: postman-nanonets-image-classification-api
- collection_type: postman
  name: Nanonets OCR API
  slug: postman-nanonets-ocr-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Nanonets External Integrations API
  slug: open-nanonets-external-integrations-api
- collection_type: open
  name: Nanonets External Integrations File Assignment API
  slug: open-nanonets-file-assignment-api
- collection_type: open
  name: Nanonets External Integrations File Delete API
  slug: open-nanonets-file-delete-api
- collection_type: open
  name: Nanonets External Integrations File Export API
  slug: open-nanonets-file-export-api
- collection_type: open
  name: Nanonets File Management API
  slug: open-nanonets-file-management-api
- collection_type: open
  name: Nanonets External Integrations File Update API
  slug: open-nanonets-file-update-api
- collection_type: open
  name: Nanonets Image Classification API
  slug: open-nanonets-image-classification-api
- collection_type: open
  name: Nanonets External Integrations Image Classification Predict API
  slug: open-nanonets-image-classification-predict-api
- collection_type: open
  name: Nanonets OCR API
  slug: open-nanonets-ocr-api
- collection_type: open
  name: Nanonets External Integrations OCR Predict API
  slug: open-nanonets-ocr-predict-api
- collection_type: open
  name: Nanonets External Integrations OCR Retrieve API
  slug: open-nanonets-ocr-retrieve-api
- collection_type: open
  name: Nanonets External Integrations OCR Train API
  slug: open-nanonets-ocr-train-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nanonets-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nanonets-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nanonets-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/nanonets/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-async-ocr-predict-and-poll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-async-url-predict-poll-approve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-batch-review-pending-files-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-classify-image-and-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-page-level-correct-and-approve-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-predict-and-assign-reviewer-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-predict-and-enrich-with-database-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-predict-correct-and-reexport-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-resolve-integration-and-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-sync-predict-and-review-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-upload-training-images-and-train-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nanonets-upload-training-urls-and-train-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://nanonets.com
- group: start
  title: ''
  type: Console
  url: https://app.nanonets.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanonets.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.nanonets.com/docs/nanonets-overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.nanonets.com/reference/authentication
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.nanonets.com/reference/response-code-error
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.nanonets.com/reference/how-to-handle-429-error
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanonets.com/docs/generate-api-key
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanonets.com/docs/async-and-sync-file-processing
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanonets.com/docs/file-formats
- group: docs
  title: ''
  type: Documentation
  url: https://docs.nanonets.com/docs/language-supported
- group: design
  title: ''
  type: Webhooks
  url: https://docs.nanonets.com/docs/webhook-export
- group: company
  title: ''
  type: Blog
  url: https://nanonets.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://accounts.nanonets.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.nanonets.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.nanonets.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://legal.nanonets.com/dpa
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/NanoNets
- group: docs
  title: ''
  type: Documentation
  url: https://www.postman.com/nanonetsapi/nanonets
- group: docs
  title: ''
  type: Documentation
  url: https://huggingface.co/nanonets
- group: docs
  title: ''
  type: Documentation
  url: https://www.idp-leaderboard.org/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NanoNets/docext
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NanoNets/docstrange
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/NanoNets/nanoindex
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NanoNets/nanonets-python-client
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NanoNets/nanonets-javascript
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NanoNets/nanonets-go
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NanoNets/ocr-js-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/NanoNets/ic-js-sdk
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NanoNets/object-detection-sample-python
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NanoNets/object-detection-sample-nodejs
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NanoNets/object-detection-sample-golang
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NanoNets/object-detection-sample-php
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/NanoNets/nanonets-ocr-sample-python
- group: build
  title: ''
  type: Tools
  url: https://github.com/NanoNets/n8n-nodes-nanonets
- group: commercial
  title: ''
  type: Plans
  url: plans/nanonets-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nanonets-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/nanonets-finops.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/nanonets-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/nanonets-vocabulary.yml
created: '2026-05-25'
description: Nanonets is a no-code document AI and OCR platform that combines a custom-model OCR API, pre-built document models (invoices, receipts, purchase orders, bills of lading, passports, driver's licenses, bank statements), image classification, and a visual workflow builder with imports, transformations, lookups, approvals, and ERP/CRM/database exports. The Nanonets OCR-3 model and the open-source docext toolkit power the IDP Leaderboard number-one ranking. Enterprise tier adds SAML SSO, SCIM, role-based access, on-prem and private-cloud deployment, HIPAA, SOC 2 Type II, and ISO 27001.
examples:
- key_count: 2
  name: Nanonets Image Classify Urls Example
  slug: nanonets-image-classify-urls-example
- key_count: 2
  name: Nanonets Ocr Predict File Example
  slug: nanonets-ocr-predict-file-example
features:
- description: Highest-accuracy OCR model on the public IDP Leaderboard, ahead of GPT-5, Gemini, and Claude.
  name: Nanonets OCR-3 model
- description: Train an extraction model from a handful of examples or even from a written field description, without large labeled datasets.
  name: Instant Learning (zero-shot) models
- description: Ready-to-use models for invoices, receipts, purchase orders, bills of lading, bank statements, passports, and driver's licenses.
  name: Pre-built document models
- description: Upload images, annotate labels and tables, train and retrain a model tied to a unique `model_id`.
  name: Custom-trained OCR models
- description: Classify incoming documents and route each to the correct extraction model and workflow.
  name: Document Classification and Routing
- description: Multi-page table parsing with per-cell bounding boxes, row/column indices, and OCR text.
  name: Table extraction
- description: Sync endpoints optimized for ≤3-page files; async endpoints for larger documents with polling by `request_file_id`.
  name: Sync and async file processing
- description: No-code visual pipeline of imports, transformations, lookups, approvals, conditional routing, and exports.
  name: Workflow builder
- description: Field- and cell-level approval rules with reviewer assignment, comments, validation status, and duplicate detection.
  name: Approval rules and review queues
- description: Custom Python blocks inside the workflow for bespoke data transformation and validation logic.
  name: Python post-processing blocks
- description: LLM-powered transformation steps for normalization, enrichment, and classification.
  name: Generative AI blocks
- description: Mask personally identifiable information before downstream export.
  name: PII Masking
- description: Per-field and per-cell confidence scores feed routing rules and human-in-the-loop review.
  name: Confidence scoring
- description: Run the Nanonets OCR stack inside customer infrastructure with the OCR Docker offering.
  name: On-prem and private cloud deployment
- description: Embed the Nanonets review experience under a customer-branded domain.
  name: White-label review and approval UI
- description: Enterprise-grade identity and lifecycle management.
  name: SAML SSO and SCIM
- description: Enterprise audit trail with SIEM-ready export.
  name: Audit logs and SIEM integration
- description: US, EU, and APAC region choices for enterprise customers.
  name: Data residency
- description: On-prem, OCR-free unstructured data extraction and benchmarking toolkit, MIT-licensed.
  name: Open-source extraction toolkit (docext)
- description: Convert any document, PDF, image, Word doc, PPT, or URL into Markdown, JSON, CSV, or HTML.
  name: Document conversion (docstrange)
- description: Tree- and graph-based reasoning harness for long-document retrieval with citations down to the pixel.
  name: Agentic RAG (nanoindex)
finops:
- name: Nanonets Finops
  service_category: AI and Machine Learning
  slug: nanonets-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nanonets.png
integrations:
- description: ERP export connector for posting extracted data.
  name: SAP
- description: Accounting export connector for invoices and bills.
  name: QuickBooks
- description: Accounting export connector and lookup data source.
  name: Xero
- description: ERP export connector.
  name: Sage
- description: ERP export connector with credential setup guide and lookup support.
  name: NetSuite
- description: Accounting export connector.
  name: Zoho Books
- description: CRM export connector for routing extracted records into Salesforce objects.
  name: Salesforce
- description: CRM destination for extracted data.
  name: HubSpot
- description: Email import and inbox-based intake.
  name: Gmail
- description: Email import action with run history.
  name: Microsoft Outlook / Email
- description: Notification and collaboration channel.
  name: Slack
- description: Notification and collaboration channel.
  name: Microsoft Teams
- description: Project management destination.
  name: Jira
- description: Project management destination.
  name: Asana
- description: Import and export connector for cloud-stored documents.
  name: Google Drive
- description: Import and export connector.
  name: Dropbox
- description: Cloud storage source.
  name: Box
- description: Import and export connector.
  name: OneDrive
- description: Import and export connector.
  name: SharePoint
- description: Lookup data source and export destination.
  name: Google Sheets
- description: Export destination.
  name: Google Docs
- description: Export destination.
  name: Microsoft Excel
- description: Export destination.
  name: Smartsheet
- description: Export destination for partner integrations.
  name: FTP server
- description: Data warehouse destination.
  name: Snowflake
- description: Payment and billing data source.
  name: Stripe
- description: Support workflow integration.
  name: Zendesk
- description: Document destination.
  name: Notion
- description: Trigger-based intake for arbitrary SaaS connections.
  name: Zapier
- description: Open-source workflow automation via `n8n-nodes-nanonets`.
  name: n8n
- description: Push extracted data to any HTTP endpoint with a documented payload structure.
  name: Webhooks
- description: External database integrations for lookups and execute-query operations.
  name: PostgreSQL / MySQL / MSSQL / MongoDB
json_schemas:
- name: Nanonets Prediction
  property_count: 15
  slug: nanonets-prediction
jsonld:
- class_count: 34
  name: Nanonets Context
  property_count: 1
  slug: nanonets-context
layout: provider
modified: '2026-05-25'
name: Nanonets
nav: Providers
network: true
overview: 'Nanonets publishes 10 APIs on the [APIs.io](https://apis.io/) network, including External Integrations API, File Assignment API, File Delete API, and 7 more. Tagged areas include AI, Artificial Intelligence, OCR, Document AI, and Intelligent Document Processing.


  The Nanonets catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Nanonets'' developer surface includes authentication, developer portal, developer console, documentation, getting-started guide, engineering blog, signup flow, and 49 more developer resources.'
plans:
- name: Nanonets Plans Pricing
  plan_count: 3
  slug: nanonets-plans-pricing
random_paper: 125
rate_limits:
- limit_count: 3
  name: Nanonets Rate Limits
  slug: nanonets-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Nanonets API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: nanonets-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Nanonets API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: nanonets-rules
score:
  band: strong
  composite: 59.6
  delta: -5.8
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 25.0
    contract_quality: 65.2
    developer_ergonomics: 69.0
    discoverability: 59.3
    governance: 25.0
    operational_transparency: 44.7
  previous_composite: 65.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/nanonets/refs/heads/main/screenshots/nanonets-2026-06-20T185940.png
security:
- kind: authentication
  name: Nanonets Authentication
  slug: nanonets-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Nanonets Domain Security
  slug: nanonets-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nanonets
solutions:
- description: Free tier with $200 in credits, API access, email import, cloud storage connectors, up to 3 users, and community support.
  name: Starter
- description: Volume-discount tier adding classification AI, barcode and signature detection, generative AI blocks, custom Python blocks, ERP and database integrations, AI reporting, and team-wide credit sharing.
  name: Growth
- description: Tailored pricing with SAML SSO, SCIM, RBAC, HIPAA and SOC 2 compliance, private cloud or on-prem deployment, data residency, enterprise connectors (Salesforce, SAP, Oracle), dedicated support and SLAs, audit logs, SIEM integration, and whitelabel UI.
  name: Enterprise
tags:
- AI
- Artificial Intelligence
- OCR
- Document AI
- Intelligent Document Processing
- Data Extraction
- Workflow Automation
- Computer Vision
- No-Code
use_cases:
- description: Multi-format invoice capture, 3-way matching, approval routing, and ERP posting (claimed 80% cost reduction).
  name: Accounts Payable automation
- description: Extract and reconcile purchase orders across formats and channels.
  name: Order management
- description: Bill of lading, packing list, and customs document extraction.
  name: Logistics and shipping
- description: Medical claim, EOB, and patient intake document processing under HIPAA BAA.
  name: Healthcare revenue cycle
- description: Extract obligations, parties, dates, and renewal terms from contracts.
  name: Contract analysis
- description: Insurance claim intake, FNOL document parsing, and adjudication support.
  name: Claims handling
- description: Extract W-9, tax certificate, and KYB document data for vendor master records.
  name: Vendor onboarding
- description: Driver's license, passport, and insurance card capture for identity workflows.
  name: ID and insurance verification
website: https://nanonets.com
---
