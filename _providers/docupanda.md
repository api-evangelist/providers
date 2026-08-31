---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-30'
api_count: 10
apis:
- description: Submit, retrieve, list, search, split, merge, bulk-download, and delete documents. DocuPanda parses files into searchable PDFs and structured page-level text, tables, and bounding boxes. Supports hand
  name: DocuPanda Documents API
  slug: docupanda-documents-api
- description: Create, edit, copy, delete, and list extraction schemas, plus AI auto-generate a schema from sample documents and retrieve schema proposals per document. Schemas define the structured JSON shape DocuP
  name: DocuPanda Schemas API
  slug: docupanda-schemas-api
- description: 'Run the agentic V3 standardization engine (or legacy V2) against documents to produce schema-compliant JSON. Retrieve results as JSON, plaintext, or XML; bulk-download as Excel or merged Excel; query '
  name: DocuPanda Standardizations API
  slug: docupanda-standardizations-api
- description: 'Classify batches of documents into a workspace-defined taxonomy. Manage the class taxonomy (add, edit, delete, list, copy classes across workspaces) and route documents to the right downstream schema '
  name: DocuPanda Classifications API
  slug: docupanda-classifications-api
- description: Run free-form LLM analysis prompts against a single document or a batch and retrieve the resulting analysis by id. Useful for one-off Q&A, summaries, or red-flag checks that do not require a fixed ext
  name: DocuPanda Analysis API
  slug: docupanda-analysis-api
- description: Generate visual extraction reviews that highlight where each standardized field was sourced in the original document. List, update, share via presigned URL, and delete reviews. Underpins human-in-the-
  name: DocuPanda Reviews API
  slug: docupanda-reviews-api
- description: Define on-submit-document workflows that chain classification, schema selection, standardization, and review automatically when a new document is uploaded. List, update, and delete workflows.
  name: DocuPanda Workflows API
  slug: docupanda-workflows-api
- description: Inspect every job DocuPanda runs on your behalf with the credit cost it consumed. Retrieve a job by id, list jobs, bulk-delete jobs, and pull a summary count with credit breakdown for FinOps reporting
  name: DocuPanda Jobs API
  slug: docupanda-jobs-api
- description: Register and deregister webhook endpoints to receive event-driven callbacks when documents finish processing, classifications complete, or standardizations are ready. Includes a portal-link endpoint t
  name: DocuPanda Webhooks API
  slug: docupanda-webhooks-api
- description: Fetch the current account profile including remaining credits, plan tier, and workspace context. Pair with the Jobs API to build internal usage dashboards.
  name: DocuPanda Account API
  slug: docupanda-account-api
artifact_total: 40
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/docupanda-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/docupanda-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://www.docupipe.ai/
- group: start
  title: ''
  type: Portal
  url: https://www.docupanda.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.docupipe.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.docupipe.ai/reference/getting-started-with-docupipe
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.docupipe.ai/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://docs.docupipe.ai/reference/authentication
- group: docs
  title: ''
  type: APIReference
  url: https://docs.docupipe.ai/llms.txt
- group: start
  title: ''
  type: Signup
  url: https://app.docupipe.ai/
- group: start
  title: ''
  type: Login
  url: https://app.docupipe.ai/
- group: start
  title: ''
  type: Console
  url: https://app.docupipe.ai/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.docupipe.ai/status
- group: company
  title: ''
  type: Blog
  url: https://www.docupipe.ai/blog
- group: auth
  title: ''
  type: Security
  url: https://www.docupipe.ai/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://docupipe.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.docupipe.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.docupipe.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.docupipe.ai/terms
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DocuPanda
- group: build
  title: ''
  type: SDKs
  url: https://github.com/DocuPanda/docupanda-python-api
- group: build
  title: ''
  type: Tools
  url: https://github.com/DocuPanda/docupanda-desktop
- group: commercial
  title: ''
  type: Pricing
  url: https://www.docupipe.ai/pricing
created: '2026-05-25'
description: DocuPanda (now also branded DocuPipe, operated by Hoss Inc.) is an AI-powered document intelligence API that converts unstructured documents — invoices, leases, medical records, claims, contracts, bills of lading, receipts, and more — into reliable structured JSON. The platform pairs an OCR + parsing pipeline with custom extraction schemas, an agentic standardization engine, classification, workflows, visual review, and webhooks. Over one billion pages processed, SOC 2 Type 2 and ISO 27001 certified, HIPAA BAA available, and deployable in cloud, VPC, or on-premises.
features:
- Document extraction across PDFs, images, Office docs, handwriting, tables, and checkboxes
- 60+ language support
- Custom JSON schemas with AI-assisted auto-generation from sample documents
- Agentic V3 standardization engine with legacy V2 still supported
- Document classification with workspace-defined taxonomies
- On-submit-document workflows that chain classify → schema-select → standardize → review
- Visual review with source highlighting for human-in-the-loop QA
- Natural-language query across standardized data
- Searchable PDFs with built-in OCR
- Bulk download as Excel, merged Excel, XML, OCR PDF, and original file
- Document split (AI-based) and document merge
- Webhooks via portal-link subscription management
- Per-job credit accounting via the Jobs API
- SOC 2 Type 2, ISO 27001, HIPAA, GDPR
- End-to-end encryption in transit and at rest
- Segregated workspaces, audit logs, redundancy and disaster recovery
- On-premises / VPC deployment for Enterprise
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/docupanda.png
integrations:
- description: Native Make app — DocuPanda actions and triggers for the no-code automation platform with 2,000+ connected apps.
  name: Make
- description: DocuPanda Document Understanding connector for the Workato enterprise iPaaS.
  name: Workato
- description: DocuPipe for n8n — extract documents inside open-source n8n workflows.
  name: n8n
- description: DocuPanda connector for Microsoft Power Automate.
  name: Microsoft Power Automate
- description: DocuPanda integration on the Boost.space platform.
  name: Boost.space
layout: provider
modified: '2026-05-25'
name: DocuPanda
nav: Providers
network: true
overview: 'DocuPanda publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Document Extraction, Document Intelligence, IDP, and OCR.


  DocuPanda''s developer surface includes developer portal, documentation, API reference, getting-started guide, authentication, signup flow, developer console, and 16 more developer resources.'
random_paper: 19
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 46.4
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 26.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/docupanda/refs/heads/main/screenshots/docupanda-2026-06-20T180119.png
security:
- kind: domain-security
  name: Docupanda Domain Security
  slug: docupanda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docupanda Trust Center
  slug: docupanda-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: docupanda
tags:
- Artificial Intelligence
- Document Extraction
- Document Intelligence
- IDP
- OCR
- Document AI
use_cases:
- description: Extract structured data from invoices, bank statements, loan applications, and purchase orders.
  name: Finance
- description: Standardize medical records and insurance claims with HIPAA BAA coverage.
  name: Healthcare
- description: Parse bills of lading, shipping documents, and customs paperwork.
  name: Logistics
- description: Extract lease terms (rental amount, dates, deposits, clauses) from rental and lease agreements.
  name: Real Estate
- description: Standardize contracts and extract clause-level data for downstream review.
  name: Legal
- description: 60+ language support for multinational document pipelines.
  name: Global Operations
website: https://www.docupipe.ai/
---
