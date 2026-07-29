---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
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
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 146
  human_in_the_loop: 0
  name: Affinda Agentic Access
  operation_count: 244
  slug: affinda-agentic-access
  summary_line: 244 operations · 146 acting
api_count: 16
apis:
- description: Upload documents (PDF, images, DOCX, XLSX, TXT, HTML) and Affinda returns structured JSON extraction with confidence scores, bounding boxes, and OCR text. Supports invoices, resumes, receipts, contrac
  name: Affinda Documents API
  slug: affinda-documents-api
- description: Manage document type definitions — the model configuration governing how a specific document category (invoice, resume, custom contract) is parsed. Each document type exposes a JSON Schema and optiona
  name: Affinda Document Types API
  slug: affinda-document-types-api
- description: Workspaces group together related collections, documents, members, and webhook subscriptions. Workspace identifiers scope every document upload, listing, and webhook delivery. Includes per-workspace u
  name: Affinda Workspaces API
  slug: affinda-workspaces-api
- description: Manage the top-level organization account — read and update organization details. Organizations contain users, billing, document types, and workspaces. Per-user limit of 3 API keys.
  name: Affinda Organizations API
  slug: affinda-organizations-api
- description: Manage custom mapping data sources — master-data lists used to match raw extracted values (vendor names, SKUs, categories) to known canonical entities. Upload values via the API and reference the data
  name: Affinda Data Sources API
  slug: affinda-data-sources-api
- description: Manually create, update, and delete annotations on uploaded documents. Annotations are the field-level extraction objects (value, confidence, bounding box, parent field) and provide the surface for hu
  name: Affinda Annotations API
  slug: affinda-annotations-api
- description: Track the status and findings of validation rules attached to parsed documents. Validation results record passes, failures, and remediation context for field-level rules and inform the embeddable vali
  name: Affinda Validation Results API
  slug: affinda-validation-results-api
- description: Tag management for parsed documents. Tags can be arbitrarily attached to documents to support routing, segmentation, search filters, and downstream workflow triggers. Supports batch-add and batch-remo
  name: Affinda Tags API
  slug: affinda-tags-api
- description: Retrieve daily credits consumption for the organization across all workspaces and document types. Used for billing reconciliation, budget tracking, and FinOps reporting.
  name: Affinda Usage API
  slug: affinda-usage-api
- description: Resthook-style webhook subscriptions for document parsing events. Create a subscription, receive a probe payload, and call the activation endpoint to confirm the receiver. Affinda delivers events such
  name: Affinda Webhooks API
  slug: affinda-webhooks-api
- description: Resume search, job description search, and matching across parsed-document indexes. Score candidates against a job description (or vice versa), retrieve match details, configure search and embed param
  name: Affinda Search and Match API
  slug: affinda-search-match-api
- description: Hidden endpoints not intended for public use. These endpoints include Splitting, Extractor, Organization, and Workspace Memberships & Usage functionality.
  name: Affinda Add x-hidden to endpoints API
  slug: affinda-add-x-hidden-to-endpoints-api
- description: Deprecated endpoints that are maintained for backward compatibility. These endpoints include Data Point, Collection, and Users functionality that has been superseded by newer APIs.
  name: Affinda Deprecated End Points API
  slug: affinda-deprecated-end-points-api
- description: The Document API - Extractor API from Affinda — 2 operation(s) for document api - extractor.
  name: Affinda Document API - Extractor API
  slug: affinda-document-api-extractor-api
- description: The Document API - Splitting API from Affinda — 3 operation(s) for document api - splitting.
  name: Affinda Document API - Splitting API
  slug: affinda-document-api-splitting-api
- description: The Organization API - Invitation API from Affinda — 3 operation(s) for organization api - invitation.
  name: Affinda Organization API - Invitation API
  slug: affinda-organization-api-invitation-api
arazzos:
- description: Create a workspace and collection, then add a custom data field plus data point to the collection.
  name: Affinda Add a Data Field to a Collection
  slug: affinda-add-collection-data-field-workflow
- description: Create a workspace in an organization and add a user to it as a member.
  name: Affinda Add a Member to a Workspace
  slug: affinda-add-workspace-member-workflow
- description: Create an organization, create a workspace inside it, then read the organization detail back.
  name: Affinda Bootstrap Organization and Workspace
  slug: affinda-bootstrap-organization-workspace-workflow
- description: Read the resume search config, update its weights, then mint a signed embeddable search URL.
  name: Affinda Configure and Embed Resume Search
  slug: affinda-configure-resume-search-embed-workflow
- description: Create an enum-style data point on an extractor and replace its full set of choices.
  name: Affinda Create Enum Data Point and Populate Choices
  slug: affinda-create-data-point-with-choices-workflow
- description: Create a mapping data source, add a value to it, then list its values.
  name: Affinda Create Mapping Data Source and Add a Value
  slug: affinda-create-data-source-and-add-value-workflow
- description: Create a resume document directly from structured data, wait for it, then add it to a search index.
  name: Affinda Create Document from Data and Index It
  slug: affinda-create-document-from-data-and-index-workflow
- description: Create a custom extractor in an organization and add a custom data point to it.
  name: Affinda Create Extractor with a Data Point
  slug: affinda-create-extractor-with-data-point-workflow
- description: Create a Search & Match index, add a document to it, then list the index's documents.
  name: Affinda Create Search Index and Add a Document
  slug: affinda-create-index-and-add-document-workflow
- description: Create a tag in a workspace and batch-apply it to a set of documents.
  name: Affinda Create a Tag and Apply It to Documents
  slug: affinda-create-tag-and-tag-documents-workflow
- description: Create a document type in an organization, then generate a JSON schema and Pydantic models from it.
  name: Affinda Create Document Type and Generate JSON Schema
  slug: affinda-document-type-to-json-schema-workflow
- description: Locate a document by its custom identifier, then move it into a different collection.
  name: Affinda Find a Document and Move It to Another Collection
  slug: affinda-find-and-move-document-workflow
- description: Create an organization invitation, look it up by token, and accept it on the invitee's behalf.
  name: Affinda Invite Organization Member and Respond
  slug: affinda-invite-member-and-respond-workflow
- description: Run a job description search using a resume and fetch the detail for the top matching role.
  name: Affinda Job Description Search and Detail
  slug: affinda-job-description-search-and-detail-workflow
- description: Upload a document, wait for parsing, list its annotations, then batch-correct them.
  name: Affinda Parse and Correct Annotations
  slug: affinda-parse-and-correct-annotations-workflow
- description: Upload a document, wait for parsing, inspect the result, then branch to reject or confirm it.
  name: Affinda Parse and Reject a Document
  slug: affinda-parse-and-reject-document-workflow
- description: Upload a document, wait for parsing, read its annotations, and record a validation result against it.
  name: Affinda Parse and Record a Validation Result
  slug: affinda-parse-and-validate-rule-workflow
- description: Create a workspace, create a collection bound to an extractor, then upload a document into it and parse it.
  name: Affinda Provision Collection and Ingest a Document
  slug: affinda-provision-and-ingest-document-workflow
- description: Create a workspace inside an organization and a collection bound to an extractor within it.
  name: Affinda Provision Workspace and Collection
  slug: affinda-provision-workspace-collection-workflow
- description: Look up a document type, rename it, then regenerate its JSON schema.
  name: Affinda Rename Document Type and Refresh Its Schema
  slug: affinda-rename-document-type-and-refresh-schema-workflow
- description: Run a resume search against an index and fetch the detailed match breakdown for the top result.
  name: Affinda Resume Search and Detail
  slug: affinda-resume-search-and-detail-workflow
- description: Upload a multi-page document, wait for parsing, then split it into separate documents that re-parse.
  name: Affinda Split a Document and Re-parse
  slug: affinda-split-document-and-reparse-workflow
- description: Update the parsed data of a resume document and refresh it in a search index.
  name: Affinda Update Resume Data and Re-index
  slug: affinda-update-resume-data-and-reindex-workflow
- description: Upload a document for parsing, poll until processing completes, then retrieve the parsed data.
  name: Affinda Upload and Parse a Document
  slug: affinda-upload-and-parse-document-workflow
- description: Upload a document by URL, wait for parsing, then confirm it in the validation tool.
  name: Affinda Upload from URL, Parse, and Confirm
  slug: affinda-upload-from-url-and-validate-workflow
- description: Create a resthook subscription for an event and activate it with the received secret.
  name: Affinda Subscribe and Activate a Webhook
  slug: affinda-webhook-subscribe-and-activate-workflow
- description: List an organization's workspaces, then pull a daily credit-consumption report scoped to the first workspace.
  name: Affinda Workspace Usage Report
  slug: affinda-workspace-usage-report-workflow
artifact_total: 117
collections:
- collection_type: postman
  name: Affinda Annotations API
  slug: postman-affinda-annotations-api
- collection_type: postman
  name: Affinda Data Sources API
  slug: postman-affinda-data-sources-api
- collection_type: postman
  name: Affinda Document Splitters API
  slug: postman-affinda-document-splitters-api
- collection_type: postman
  name: Affinda Document Types API
  slug: postman-affinda-document-types-api
- collection_type: postman
  name: Affinda Documents API
  slug: postman-affinda-documents-api
- collection_type: postman
  name: Affinda Extractors API
  slug: postman-affinda-extractors-api
- collection_type: postman
  name: Affinda Invitations API
  slug: postman-affinda-invitations-api
- collection_type: postman
  name: Affinda Organizations API
  slug: postman-affinda-organizations-api
- collection_type: postman
  name: Affinda Search and Match API
  slug: postman-affinda-search-match-api
- collection_type: postman
  name: Affinda Tags API
  slug: postman-affinda-tags-api
- collection_type: postman
  name: Affinda Usage API
  slug: postman-affinda-usage-api
- collection_type: postman
  name: Affinda Validation Results API
  slug: postman-affinda-validation-results-api
- collection_type: postman
  name: Affinda Webhooks API
  slug: postman-affinda-webhooks-api
- collection_type: postman
  name: Affinda Workspaces API
  slug: postman-affinda-workspaces-api
- collection_type: open
  name: Affinda Annotations API
  slug: open-affinda-annotations-api
- collection_type: open
  name: Affinda Data Sources API
  slug: open-affinda-data-sources-api
- collection_type: open
  name: Affinda Document Splitters API
  slug: open-affinda-document-splitters-api
- collection_type: open
  name: Affinda Document Types API
  slug: open-affinda-document-types-api
- collection_type: open
  name: Affinda Documents API
  slug: open-affinda-documents-api
- collection_type: open
  name: Affinda Extractors API
  slug: open-affinda-extractors-api
- collection_type: open
  name: Affinda Invitations API
  slug: open-affinda-invitations-api
- collection_type: open
  name: Affinda Organizations API
  slug: open-affinda-organizations-api
- collection_type: open
  name: Affinda Search and Match API
  slug: open-affinda-search-match-api
- collection_type: open
  name: Affinda Tags API
  slug: open-affinda-tags-api
- collection_type: open
  name: Affinda Usage API
  slug: open-affinda-usage-api
- collection_type: open
  name: Affinda API
  slug: open-affinda-v3
- collection_type: open
  name: Affinda Validation Results API
  slug: open-affinda-validation-results-api
- collection_type: open
  name: Affinda Webhooks API
  slug: open-affinda-webhooks-api
- collection_type: open
  name: Affinda Workspaces API
  slug: open-affinda-workspaces-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/affinda-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/affinda-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/affinda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/affinda-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/affinda/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-add-collection-data-field-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-add-workspace-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-bootstrap-organization-workspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-configure-resume-search-embed-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-data-point-with-choices-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-data-source-and-add-value-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-document-from-data-and-index-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-extractor-with-data-point-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-index-and-add-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-create-tag-and-tag-documents-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-document-type-to-json-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-find-and-move-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-invite-member-and-respond-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-job-description-search-and-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-parse-and-correct-annotations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-parse-and-reject-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-parse-and-validate-rule-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-provision-and-ingest-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-provision-workspace-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-rename-document-type-and-refresh-schema-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-resume-search-and-detail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-split-document-and-reparse-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-update-resume-data-and-reindex-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-upload-and-parse-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-upload-from-url-and-validate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-webhook-subscribe-and-activate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/affinda-workspace-usage-report-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.affinda.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.affinda.com
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.affinda.com/reference/getting-started
- group: docs
  title: ''
  type: OpenAPI
  url: https://api.affinda.com/static/v3/api_spec.yaml
- group: agent
  title: ''
  type: AgentSkills
  url: https://docs.affinda.com/skill.md
- group: docs
  title: ''
  type: APIReference
  url: https://docs.affinda.com/reference
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affinda.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.affinda.com/auth/register
- group: start
  title: ''
  type: Login
  url: https://app.affinda.com/auth/login
- group: start
  title: ''
  type: Login
  url: https://app.us1.affinda.com/auth/login
- group: start
  title: ''
  type: Login
  url: https://app.eu1.affinda.com/auth/login
- group: auth
  title: ''
  type: Authentication
  url: https://docs.affinda.com/reference/authentication
- group: design
  title: ''
  type: Webhooks
  url: https://docs.affinda.com/reference/webhooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.affinda.com/changelog
- group: company
  title: ''
  type: Blog
  url: https://www.affinda.com/blog
- group: learn
  title: ''
  type: Academy
  url: https://www.affinda.com/affinda-academy
- group: operate
  title: ''
  type: Support
  url: https://support.affinda.com
- group: operate
  title: ''
  type: ContactUs
  url: https://www.affinda.com/contact
- group: auth
  title: ''
  type: Security
  url: https://www.affinda.com/security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.affinda.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affinda.com/legal/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affinda
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affinda
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/affinda_ai
- group: build
  title: ''
  type: SDKs
  url: https://github.com/affinda/affinda-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/affinda/affinda-typescript
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@affinda/affinda
- group: build
  title: ''
  type: SDKs
  url: https://pypi.org/project/affinda/
- group: build
  title: ''
  type: SDKs
  url: https://www.nuget.org/packages/Affinda.API
- group: build
  title: ''
  type: SDKs
  url: https://central.sonatype.com/artifact/com.affinda.api/affinda-api-client
- group: other
  title: ''
  type: Regions
  url: ''
- group: auth
  title: ''
  type: Compliance
  url: ''
- group: commercial
  title: ''
  type: Plans
  url: plans/affinda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/affinda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/affinda-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Affinda is an Intelligent Document Processing (IDP) platform that uses AI to extract structured data from documents — resumes, invoices, receipts, contracts, passports, IDs, and custom document types. The v3 REST API exposes document upload and parsing, document type configuration, workspaces, collections, data sources for master-data matching, validation results, annotations for human-in-the-loop review, webhooks via resthook subscriptions, daily usage reporting, and resume / job-description search and match for recruitment workflows. The platform is deployed across AUS/Global, US, and EU regions for data residency, holds SOC 2 Type II and ISO 27001:2022 certification, and ships official Python, TypeScript, .NET, and Java SDKs alongside a skill.md file for AI coding agents.
examples:
- key_count: 4
  name: Affinda Get Parsed Resume Example
  slug: affinda-get-parsed-resume-example
- key_count: 4
  name: Affinda Resume Search Example
  slug: affinda-resume-search-example
- key_count: 4
  name: Affinda Upload Document Example
  slug: affinda-upload-document-example
- key_count: 4
  name: Affinda Webhook Subscription Example
  slug: affinda-webhook-subscription-example
features:
- Intelligent Document Processing platform with natural-language workflow configuration
- Resume parsing with skills, work experience, education, and language extraction
- Invoice parsing with line items, tax breakdown, supplier matching, and currency normalization
- Receipt parsing for expense automation
- Passport and ID document extraction
- Contract data extraction and clause identification
- Custom document types configured via dashboard or natural language
- Document splitting and classification across multi-document PDFs
- Handwriting / OCR recognition
- Table extraction across complex multi-page tables
- Confidence scoring with bounding box coordinates on every field
- Master-data matching against custom mapping data sources
- Validation rules and embeddable validation UI (Business and Enterprise tiers)
- Resume search and matching against job descriptions with score breakdown
- Job description search against indexed resumes
- Workspace + collection scoping for multi-tenant document orgs
- Resthook-style webhook subscriptions with activation handshake
- Webhook events for document parsed, failed, and validated states
- Daily credits usage reporting at organization and workspace level
- High-priority queue (20 documents/minute) and unlimited low-priority queue
- Multi-region deployment (AUS/Global, US, EU) with data residency
- SOC 2 Type II, ISO 27001:2022, GDPR, and HIPAA (Enterprise) compliance
- On-premise / private-cloud deployment available on Enterprise
- SSO and dedicated environment options on Enterprise
- Free 14-day pay-as-you-go trial with prepaid credits
- Official Python, TypeScript, .NET, and Java client libraries
- skill.md file for AI agents (Claude Code, Cursor) describing the full API surface
finops:
- name: Affinda Finops
  service_category: AI and Machine Learning
  slug: affinda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/affinda.png
json_schemas:
- name: Affinda Annotation
  property_count: 15
  slug: affinda-annotation
- name: Affinda Document
  property_count: 3
  slug: affinda-document
- name: Affinda Invoice
  property_count: 27
  slug: affinda-invoice
- name: Affinda Resume
  property_count: 15
  slug: affinda-resume
jsonld:
- class_count: 0
  name: Affinda Context
  property_count: 10
  slug: affinda-context
layout: provider
modified: '2026-05-25'
name: Affinda
nav: Providers
network: true
overview: 'Affinda publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Documents API, Document Types API, Workspaces API, and 13 more. Tagged areas include AI, Artificial Intelligence, Document Processing, Intelligent Document Processing, and IDP.


  The Affinda catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Affinda''s developer surface includes authentication, developer portal, documentation, getting-started guide, API reference, pricing, signup flow, and 58 more developer resources.'
plans:
- name: Affinda Plans Pricing
  plan_count: 3
  slug: affinda-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 2
  name: Affinda Rate Limits
  slug: affinda-rate-limits
rules:
- name: Affinda API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: affinda-jsonschema-spectral-rules
- name: Affinda API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: affinda-rules
score:
  band: exemplar
  composite: 68.6
  delta: -6.9
  facets:
    commercial_clarity: 100.0
    contract_quality: 68.1
    developer_ergonomics: 71.7
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 60.5
  previous_composite: 75.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/affinda/refs/heads/main/screenshots/affinda-2026-06-20T165616.png
security:
- kind: authentication
  name: Affinda Authentication
  slug: affinda-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Affinda Domain Security
  slug: affinda-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Affinda Trust Center
  slug: affinda-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: affinda
tags:
- AI
- Artificial Intelligence
- Document Processing
- Intelligent Document Processing
- IDP
- OCR
- Resume Parsing
- Invoice Parsing
- Receipt Parsing
- Document Extraction
- Document Classification
- Document Splitting
- Recruitment
- Banking
- Insurance
- Logistics
- Healthcare
- Government
website: https://www.affinda.com
---
