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
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.1
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Signwell Agentic Access
  operation_count: 27
  slug: signwell-agentic-access
  summary_line: 27 operations · 14 acting
api_count: 7
apis:
- description: Manage API application settings and branding.
  name: SignWell API Application API
  slug: signwell-api-application-api
- description: Send a document to multiple recipients in batch using templates.
  name: SignWell Bulk Send API
  slug: signwell-bulk-send-api
- description: Create, send, and manage documents for electronic signing.
  name: SignWell Document API
  slug: signwell-document-api
- description: Retrieve account information for the authenticated API key.
  name: SignWell Me API
  slug: signwell-me-api
- description: Access region-specific endpoints for data residency compliance.
  name: SignWell Regional API
  slug: signwell-regional-api
- description: Create and manage reusable document templates.
  name: SignWell Template API
  slug: signwell-template-api
- description: Subscribe to document lifecycle events via webhook callbacks.
  name: SignWell Webhooks API
  slug: signwell-webhooks-api
artifact_total: 128
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/signwell-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/signwell-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signwell-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signwell-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.signwell.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.signwell.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Bidsketch
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/signwellapp
- group: company
  title: ''
  type: Blog
  url: https://www.signwell.com/resources/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.signwell.com/resources/feed/
- group: company
  title: ''
  type: Blog
  url: https://raw.githubusercontent.com/api-evangelist/signwell/refs/heads/main/blogs/blogs.json
- group: commercial
  title: ''
  type: Pricing
  url: https://www.signwell.com/api-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signwell.com
- group: other
  title: ''
  type: X
  url: https://x.com/signwellapp
- group: commercial
  title: ''
  type: Plans
  url: plans/signwell-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signwell-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/signwell-finops.yml
created: '2026-06-13'
description: E-signature platform with a REST API for sending documents for signature, creating templates, tracking document status, and managing signers programmatically. Supports embedded signing, bulk send, webhooks, and white-label customization with compliance for ESIGN, UETA, GDPR, and HIPAA.
examples:
- key_count: 8
  name: Createbulksend
  slug: createBulkSend
- key_count: 8
  name: Createdocument
  slug: createDocument
- key_count: 8
  name: Createdocumentfromtemplate
  slug: createDocumentFromTemplate
- key_count: 8
  name: Createtemplate
  slug: createTemplate
- key_count: 8
  name: Createwebhook
  slug: createWebhook
- key_count: 7
  name: Deleteapiapplication
  slug: deleteApiApplication
- key_count: 7
  name: Deletedocument
  slug: deleteDocument
- key_count: 7
  name: Deletetemplate
  slug: deleteTemplate
- key_count: 7
  name: Deletewebhook
  slug: deleteWebhook
- key_count: 7
  name: Getapiapplication
  slug: getApiApplication
- key_count: 7
  name: Getbulksend
  slug: getBulkSend
- key_count: 7
  name: Getbulksendcsvtemplate
  slug: getBulkSendCsvTemplate
- key_count: 7
  name: Getbulksenddocuments
  slug: getBulkSendDocuments
- key_count: 7
  name: Getcompletedpdf
  slug: getCompletedPdf
- key_count: 7
  name: Getdocument
  slug: getDocument
- key_count: 7
  name: Getme
  slug: getMe
- key_count: 7
  name: Getnom151Certificate
  slug: getNom151Certificate
- key_count: 7
  name: Gettemplate
  slug: getTemplate
- key_count: 7
  name: Listbulksends
  slug: listBulkSends
- key_count: 7
  name: Listdocuments
  slug: listDocuments
- key_count: 7
  name: Listtemplates
  slug: listTemplates
- key_count: 7
  name: Listwebhooks
  slug: listWebhooks
- key_count: 8
  name: Senddocument
  slug: sendDocument
- key_count: 8
  name: Sendreminder
  slug: sendReminder
- key_count: 8
  name: Updaterecipients
  slug: updateRecipients
- key_count: 8
  name: Updatetemplate
  slug: updateTemplate
- key_count: 8
  name: Validatebulksendcsv
  slug: validateBulkSendCsv
finops:
- name: Signwell Finops
  service_category: ''
  slug: signwell-finops
graphqls:
- description: 'This document describes the conceptual GraphQL schema for the SignWell e-signature API. SignWell provides a REST API at https://www.signwell.com/api/v1 for sending documents for electronic signature, '
  name: SignWell GraphQL Schema
  slug: signwell-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/signwell.png
json_schemas:
- name: AccountInfoResponse
  property_count: 9
  slug: AccountInfoResponse
- name: AdditionalFields
  property_count: 0
  slug: AdditionalFields
- name: AdditionalFiles
  property_count: 0
  slug: AdditionalFiles
- name: ApiApplicationId
  property_count: 0
  slug: ApiApplicationId
- name: ApiApplicationResponse
  property_count: 7
  slug: ApiApplicationResponse
- name: AttachmentRequestInfo
  property_count: 3
  slug: AttachmentRequestInfo
- name: AttachmentRequests
  property_count: 0
  slug: AttachmentRequests
- name: Base64Flag
  property_count: 0
  slug: Base64Flag
- name: BulkSendCreateResponse
  property_count: 7
  slug: BulkSendCreateResponse
- name: BulkSendCsv
  property_count: 0
  slug: BulkSendCsv
- name: BulkSendCsvRequest
  property_count: 2
  slug: BulkSendCsvRequest
- name: BulkSendCsvTemplateResponse
  property_count: 1
  slug: BulkSendCsvTemplateResponse
- name: BulkSendDocumentsResponse
  property_count: 12
  slug: BulkSendDocumentsResponse
- name: BulkSendId
  property_count: 0
  slug: BulkSendId
- name: BulkSendListItem
  property_count: 10
  slug: BulkSendListItem
- name: BulkSendListResponse
  property_count: 6
  slug: BulkSendListResponse
- name: BulkSendResponse
  property_count: 10
  slug: BulkSendResponse
- name: BulkSendTemplateIds
  property_count: 0
  slug: BulkSendTemplateIds
- name: BulkSendValidateCsvResponse
  property_count: 8
  slug: BulkSendValidateCsvResponse
- name: CheckboxGroupInfo
  property_count: 9
  slug: CheckboxGroupInfo
- name: CheckboxGroups
  property_count: 0
  slug: CheckboxGroups
- name: CheckboxValidation
  property_count: 0
  slug: CheckboxValidation
- name: CompletedDocumentId
  property_count: 0
  slug: CompletedDocumentId
- name: CompletedPdfBinaryResponse
  property_count: 0
  slug: CompletedPdfBinaryResponse
- name: CompletedPdfResponse
  property_count: 0
  slug: CompletedPdfResponse
- name: CompletedPdfUrlResponse
  property_count: 1
  slug: CompletedPdfUrlResponse
- name: CompletedPdfZipResponse
  property_count: 0
  slug: CompletedPdfZipResponse
- name: CopiedContactInfo
  property_count: 3
  slug: CopiedContactInfo
- name: CopiedContacts
  property_count: 0
  slug: CopiedContacts
- name: CopiedPlaceholders
  property_count: 0
  slug: CopiedPlaceholders
- name: CreateBulkSendRequest
  property_count: 10
  slug: CreateBulkSendRequest
- name: DateFormat
  property_count: 0
  slug: DateFormat
- name: DocumentFromTemplateRequest
  property_count: 32
  slug: DocumentFromTemplateRequest
- name: DocumentFromTemplateResponse
  property_count: 37
  slug: DocumentFromTemplateResponse
- name: DocumentId
  property_count: 0
  slug: DocumentId
- name: DocumentListResponse
  property_count: 6
  slug: DocumentListResponse
- name: DocumentRequest
  property_count: 29
  slug: DocumentRequest
- name: DocumentResponse
  property_count: 37
  slug: DocumentResponse
- name: DocumentTemplateListResponse
  property_count: 6
  slug: DocumentTemplateListResponse
- name: DocumentTemplateRequest
  property_count: 22
  slug: DocumentTemplateRequest
- name: DocumentTemplateResponse
  property_count: 30
  slug: DocumentTemplateResponse
- name: DocumentTemplateUpdateRequest
  property_count: 15
  slug: DocumentTemplateUpdateRequest
- name: DropdownOption
  property_count: 0
  slug: DropdownOption
- name: ErrorResponse
  property_count: 2
  slug: ErrorResponse
- name: FieldType
  property_count: 0
  slug: FieldType
- name: Fields
  property_count: 0
  slug: Fields
- name: FileFormat
  property_count: 0
  slug: FileFormat
- name: FileInfo
  property_count: 2
  slug: FileInfo
- name: Files
  property_count: 0
  slug: Files
- name: IncludeAuditPage
  property_count: 0
  slug: IncludeAuditPage
- name: LabelInfo
  property_count: 2
  slug: LabelInfo
- name: LabelRequest
  property_count: 1
  slug: LabelRequest
- name: LabelResponse
  property_count: 2
  slug: LabelResponse
- name: Labels
  property_count: 0
  slug: Labels
- name: LabelsResponse
  property_count: 0
  slug: LabelsResponse
- name: LabelsUpdate
  property_count: 0
  slug: LabelsUpdate
- name: Limit
  property_count: 0
  slug: Limit
- name: MeResponse
  property_count: 7
  slug: MeResponse
- name: Nom151CertificateResponse
  property_count: 1
  slug: Nom151CertificateResponse
- name: Nom151UrlResponse
  property_count: 1
  slug: Nom151UrlResponse
- name: ObjectOnly
  property_count: 0
  slug: ObjectOnly
- name: Page
  property_count: 0
  slug: Page
- name: PaginationMeta
  property_count: 5
  slug: PaginationMeta
- name: Placeholders
  property_count: 0
  slug: Placeholders
- name: RateLimitErrorResponse
  property_count: 1
  slug: RateLimitErrorResponse
- name: Recipients
  property_count: 0
  slug: Recipients
- name: ReminderRecipients
  property_count: 0
  slug: ReminderRecipients
- name: SendReminderRequest
  property_count: 1
  slug: SendReminderRequest
- name: TemplateAttachmentRequests
  property_count: 0
  slug: TemplateAttachmentRequests
- name: TemplateCheckboxGroups
  property_count: 0
  slug: TemplateCheckboxGroups
- name: TemplateFieldValues
  property_count: 0
  slug: TemplateFieldValues
- name: TemplateFields
  property_count: 0
  slug: TemplateFields
- name: TemplateId
  property_count: 0
  slug: TemplateId
- name: TemplateIds
  property_count: 0
  slug: TemplateIds
- name: TemplateRecipients
  property_count: 0
  slug: TemplateRecipients
- name: TextValidation
  property_count: 0
  slug: TextValidation
- name: UpdateDocumentAndSendRequest
  property_count: 19
  slug: UpdateDocumentAndSendRequest
- name: UrlOnly
  property_count: 0
  slug: UrlOnly
- name: UserEmail
  property_count: 0
  slug: UserEmail
- name: ValidationErrorResponse
  property_count: 1
  slug: ValidationErrorResponse
- name: WebhookListResponse
  property_count: 0
  slug: WebhookListResponse
- name: WebhookResponse
  property_count: 3
  slug: WebhookResponse
- name: update_recipients_map
  property_count: 0
  slug: update_recipients_map
- name: update_recipients_request
  property_count: 1
  slug: update_recipients_request
jsonld:
- class_count: 4
  name: Signwell Context
  property_count: 35
  slug: signwell-context
layout: provider
modified: '2026-06-13'
name: SignWell
nav: Providers
network: true
overview: 'SignWell publishes 7 APIs on the [APIs.io](https://apis.io/) network, including API Application API, Bulk Send API, Document API, and 4 more. Tagged areas include E-Signature, Electronic Signature, Documents, PDF, and Signing.


  The SignWell catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  SignWell''s developer surface includes authentication, documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Signwell Plans Pricing
  plan_count: 7
  slug: signwell-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 3
  name: Signwell Rate Limits
  slug: signwell-rate-limits
rules:
- name: SignWell API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: signwell-jsonschema-spectral-rules
score:
  band: developing
  composite: 55.9
  delta: -4.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 74.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 59.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signwell/refs/heads/main/screenshots/signwell-2026-06-20T193916.png
security:
- kind: authentication
  name: Signwell Authentication
  slug: signwell-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Signwell Domain Security
  slug: signwell-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Signwell Trust Center
  slug: signwell-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: signwell
tags:
- E-Signature
- Electronic Signature
- Documents
- PDF
- Signing
- Templates
- Workflows
- HIPAA
- SOC2
website: https://www.signwell.com/
---
