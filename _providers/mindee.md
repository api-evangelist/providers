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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Mindee Agentic Access
  operation_count: 13
  slug: mindee-agentic-access
  summary_line: 13 operations · 6 acting
api_count: 6
apis:
- description: Extract structured fields from invoices, receipts, IDs, passports, resumes, bank statements, and any other document type via Mindee's configurable extraction models. Enqueue a file at POST /v2/inferen
  name: Mindee Extraction API
  slug: mindee-extraction-api
- description: 'Classify documents into predefined categories so they can be routed to the appropriate downstream extraction model. Enqueue at POST /v2/products/classification/enqueue and retrieve the label from GET '
  name: Mindee Classification API
  slug: mindee-classification-api
- description: Detect, isolate, and crop the document area inside a larger scanned image. Useful for cleaning up phone-captured documents prior to classification or extraction. Async enqueue/results pattern at /v2/p
  name: Mindee Crop API
  slug: mindee-crop-api
- description: Run full-page optical character recognition on a document and return the raw text plus bounding polygons. Enqueue at POST /v2/products/ocr/enqueue and retrieve the OCR payload from GET /v2/products/oc
  name: Mindee OCR API
  slug: mindee-ocr-api
- description: Split a multi-document PDF or image batch into individual documents that can each be classified and extracted independently. Async enqueue/results pattern at /v2/products/split/.
  name: Mindee Split API
  slug: mindee-split-api
- description: Poll the status of asynchronous Mindee inference jobs across every Mindee model family via GET /v2/jobs/{job_id}. Jobs return Waiting, Processing, Failed, or Success states and a polling_url plus opti
  name: Mindee Jobs API
  slug: mindee-jobs-api
arazzos:
- description: Enqueue a bank statement with RAG and raw text enabled, poll until processed, then read the extracted transactions and balances.
  name: Mindee Bank Statement Extraction
  slug: mindee-bank-statement-extraction-workflow
- description: Enqueue a document for classification, poll until processed, then read the predicted document type.
  name: Mindee Classify Document Type
  slug: mindee-classify-document-type-workflow
- description: Classify an unknown document, then run extraction on the same file once the type is known, reading the parsed fields.
  name: Mindee Classify Then Extract
  slug: mindee-classify-then-extract-workflow
- description: Enqueue a document for cropping, poll until processed, then read the detected objects and their crop coordinates.
  name: Mindee Crop Document
  slug: mindee-crop-document-workflow
- description: Enqueue an arbitrary document against a custom model with raw text capture, poll until processed, then read fields and full text.
  name: Mindee Custom Document Extraction
  slug: mindee-custom-document-extraction-workflow
- description: Enqueue a publicly hosted document by URL for extraction, poll until processed, then read the extracted fields.
  name: Mindee Extract From URL
  slug: mindee-extract-from-url-workflow
- description: Enqueue an invoice for extraction, poll the job until processed, then read the extracted fields.
  name: Mindee Invoice Extraction
  slug: mindee-invoice-extraction-workflow
- description: Enqueue a document for full-page OCR, poll until processed, then read the per-page words and text content.
  name: Mindee OCR Full Text
  slug: mindee-ocr-full-text-workflow
- description: Run OCR over a document to capture its raw text, then extract structured fields from the same file, reading both outputs.
  name: Mindee OCR Then Extract
  slug: mindee-ocr-then-extract-workflow
- description: Enqueue a passport or identity document with polygon locations, poll until processed, then read the extracted holder fields.
  name: Mindee Passport and ID Extraction
  slug: mindee-passport-id-extraction-workflow
- description: Enqueue an extraction, poll the job, and branch explicitly on Processed, Processing, or Failed before reading the result.
  name: Mindee Poll Job With Failure Branch
  slug: mindee-poll-job-with-failure-branch-workflow
- description: Enqueue a receipt with confidence scoring, poll until processed, then read the extracted line items and totals.
  name: Mindee Receipt Extraction
  slug: mindee-receipt-extraction-workflow
- description: Enqueue a multi-document file for splitting, poll until processed, then read the identified document ranges.
  name: Mindee Split Multi-Document File
  slug: mindee-split-multi-document-workflow
- description: Split a multi-document file into ranges, then extract structured fields from the original file, reading splits and fields.
  name: Mindee Split Then Extract
  slug: mindee-split-then-extract-workflow
artifact_total: 61
collections:
- collection_type: postman
  name: Mindee Classification API
  slug: postman-mindee-classification-api
- collection_type: postman
  name: Mindee Crop API
  slug: postman-mindee-crop-api
- collection_type: postman
  name: Mindee Extraction API
  slug: postman-mindee-extraction-api
- collection_type: postman
  name: Mindee Jobs API
  slug: postman-mindee-jobs-api
- collection_type: postman
  name: Mindee OCR API
  slug: postman-mindee-ocr-api
- collection_type: postman
  name: Mindee Split API
  slug: postman-mindee-split-api
- collection_type: open
  name: Mindee Classification API
  slug: open-mindee-classification-api
- collection_type: open
  name: Mindee Crop API
  slug: open-mindee-crop-api
- collection_type: open
  name: Mindee Extraction API
  slug: open-mindee-extraction-api
- collection_type: open
  name: Mindee Jobs API
  slug: open-mindee-jobs-api
- collection_type: open
  name: Mindee OCR API
  slug: open-mindee-ocr-api
- collection_type: open
  name: Mindee Split API
  slug: open-mindee-split-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mindee-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mindee-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/mindee-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/mindee/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-bank-statement-extraction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-classify-document-type-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-classify-then-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-crop-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-custom-document-extraction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-extract-from-url-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-invoice-extraction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-ocr-full-text-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-ocr-then-extract-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-passport-id-extraction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-poll-job-with-failure-branch-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-receipt-extraction-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-split-multi-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/mindee-split-then-extract-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://mindee.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindee.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.mindee.com/getting-started/quick-start
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindee.com/integrations/api-overview
- group: auth
  title: ''
  type: Authentication
  url: https://docs.mindee.com/integrations/api-keys
- group: design
  title: ''
  type: Webhooks
  url: https://docs.mindee.com/integrations/webhooks
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindee.com/integrations/polling-for-results
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.mindee.com/integrations/problem-database
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.mindee.com/integrations/technical-limitations
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mindee.com/integrations/response-times
- group: docs
  title: ''
  type: OpenAPI
  url: https://api-v2.mindee.net/openapi.json
- group: start
  title: ''
  type: Signup
  url: https://app.mindee.com
- group: auth
  title: ''
  type: Authentication
  url: https://app.mindee.com/api-keys
- group: operate
  title: ''
  type: StatusPage
  url: https://status.mindee.com
- group: commercial
  title: ''
  type: Pricing
  url: https://mindee.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://mindee.com/blog
- group: company
  title: ''
  type: AboutUs
  url: https://mindee.com/about
- group: company
  title: ''
  type: Careers
  url: https://mindee.com/careers
- group: operate
  title: ''
  type: Contact
  url: https://mindee.com/contact
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mindee
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/mindee_official
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/mindee
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-nodejs
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-java
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-php
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-ruby
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/mindee-api-dotnet
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/react-mindee-js
- group: build
  title: ''
  type: SDKs
  url: https://github.com/mindee/vue-mindee-js
- group: other
  title: ''
  type: OpenSource
  url: https://github.com/mindee/doctr
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mindee/platform-docs
- group: commercial
  title: ''
  type: Plans
  url: plans/mindee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/mindee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/mindee-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/mindee-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/mindee-rules.yml
created: '2026-05-25'
description: Mindee is a document parsing and intelligent document processing platform. Its REST API (api-v2.mindee.net) provides asynchronous inference across five model families — Extraction, Classification, Crop, OCR, and Split — plus a unified Jobs endpoint for polling. Mindee ships prebuilt models for invoices, receipts, passports, IDs, resumes, bank statements, and barcodes, along with customer-configurable extraction models with their own Data Schemas. Native SDKs cover Python, Node.js, Java, PHP, Ruby, and .NET, and front-end vision SDKs cover React and Vue. Mindee also stewards the open-source docTR OCR library.
examples:
- key_count: 2
  name: Mindee Extraction Enqueue Example
  slug: mindee-extraction-enqueue-example
- key_count: 2
  name: Mindee Extraction Result Example
  slug: mindee-extraction-result-example
features:
- Async enqueue/results pattern across all Mindee models with a unified job polling endpoint
- Configurable extraction models with customer-defined Data Schemas
- Library of ready-to-use models for invoices, receipts, IDs, passports, driver's licenses, resumes, bank statements, and barcodes
- Classification, Crop, OCR, and Split utility models for full IDP pipelines
- Continuous Learning via Retrieval-Augmented Generation against a customer knowledge base
- Confidence scores and bounding polygons (Pro and higher)
- Full raw OCR text option on extraction inferences
- 100 MB file size limit; up to 200 pages per PDF
- Webhook-based result delivery in addition to polling
- Per-model and per-API-key usage insights inside the platform console
- Native SDKs for Python, Node.js, Java, PHP, Ruby, and .NET
- Front-end computer vision SDKs for React and Vue
- Open-source docTR library for self-hosted OCR
- Zapier and Microsoft Flow integrations for no-code automation
- Credit-based pricing with monthly subscription tiers and per-credit overage
finops:
- name: Mindee Finops
  service_category: AI and Machine Learning
  slug: mindee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mindee.png
json_schemas:
- name: Mindee Inference
  property_count: 1
  slug: mindee-inference
- name: Mindee Job
  property_count: 1
  slug: mindee-job
json_structures:
- name: Mindee Extraction Structure
  property_count: 1
  slug: mindee-extraction-structure
jsonld:
- class_count: 11
  name: Mindee Context
  property_count: 14
  slug: mindee-context
layout: provider
modified: '2026-05-25'
name: Mindee
nav: Providers
network: true
overview: 'Mindee publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Extraction API, Classification API, Crop API, and 3 more. Tagged areas include Document Parsing, OCR, IDP, AI, and Machine Learning.


  The Mindee catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Mindee''s developer surface includes authentication, developer portal, documentation, getting-started guide, signup flow, pricing, engineering blog, and 48 more developer resources.'
plans:
- name: Mindee Plans Pricing
  plan_count: 4
  slug: mindee-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 0
  name: Mindee Rate Limits
  slug: mindee-rate-limits
rules:
- name: Mindee API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: mindee-jsonschema-spectral-rules
- name: Mindee API Rules
  rule_count: 6
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 2
  slug: mindee-rules
score:
  band: strong
  composite: 59.8
  delta: -4.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 76.7
    developer_ergonomics: 60.9
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 64.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mindee/refs/heads/main/screenshots/mindee-2026-06-20T185555.png
security:
- kind: authentication
  name: Mindee Authentication
  slug: mindee-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mindee Domain Security
  slug: mindee-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mindee
tags:
- Document Parsing
- OCR
- IDP
- AI
- Machine Learning
- Invoices
- Receipts
- IDs
- Computer Vision
website: https://mindee.com
---
