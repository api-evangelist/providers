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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 18
  human_in_the_loop: 0
  name: Pandadoc Agentic Access
  operation_count: 43
  slug: pandadoc-agentic-access
  summary_line: 43 operations · 18 acting
api_count: 1
apis:
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for retrieving API request logs useful for debugging and auditing integration activity.
  name: PandaDoc API Logs API
  slug: pandadoc-api-logs-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing the PandaDoc contacts directory, including creating, reading, updating, and deleting contact records.
  name: PandaDoc Contacts API
  slug: pandadoc-contacts-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing file attachments associated with a document, including uploading and downloading attachment files.
  name: PandaDoc Document Attachments API
  slug: pandadoc-document-attachments-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for retrieving and updating field values within a document, such as text fields, checkboxes, signatures, and date fields.
  name: PandaDoc Document Fields API
  slug: pandadoc-document-fields-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing links between PandaDoc documents and external CRM entities such as contacts, deals, or accounts.
  name: PandaDoc Document Link to CRM API
  slug: pandadoc-document-link-to-crm-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing recipients within documents, including adding, editing, reassigning, and deleting recipients.
  name: PandaDoc Document Recipients API
  slug: pandadoc-document-recipients-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for configuring automatic reminders sent to document recipients who have not yet completed their actions.
  name: PandaDoc Document Reminders API
  slug: pandadoc-document-reminders-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for creating, retrieving, sending, and managing the full lifecycle of documents including drafting, sending for signature, downloading, and deleting.
  name: PandaDoc Documents API
  slug: pandadoc-documents-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for organizing documents and templates into folders, including creating, renaming, and listing folder contents.
  name: PandaDoc Folders API
  slug: pandadoc-folders-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for retrieving and managing forms, which are publicly shareable document templates that can be filled and signed without a predefined recipient list.
  name: PandaDoc Forms API
  slug: pandadoc-forms-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing and retrieving details about workspace members, including listing members and generating member API tokens.
  name: PandaDoc Members API
  slug: pandadoc-members-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing document templates, including listing available templates, retrieving template details, creating templates from file upload, and deleting templates.
  name: PandaDoc Templates API
  slug: pandadoc-templates-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for querying the log of webhook events that have been dispatched, including filtering by type and delivery status.
  name: PandaDoc Webhook Events API
  slug: pandadoc-webhook-events-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing webhook subscriptions that deliver real-time event notifications for document lifecycle and other platform events.
  name: PandaDoc Webhook Subscriptions API
  slug: pandadoc-webhook-subscriptions-api
- baseURL: https://api.pandadoc.com/public/v1
  baseurl_source: declared
  description: Operations for managing organization workspaces, including listing, creating, and deactivating workspaces.
  name: PandaDoc Workspaces API
  slug: pandadoc-workspaces-api
artifact_total: 128
asyncapis:
- description: The PandaDoc webhook system delivers real-time event notifications to registered subscriber endpoints when document lifecycle and platform events occur. PandaDoc sends HTTP POST requests containing JS
  name: PandaDoc Webhook Events
  slug: pandadoc-webhooks-asyncapi
collections:
- collection_type: postman
  name: PandaDoc REST API Logs API
  slug: postman-pandadoc-api-logs-api
- collection_type: postman
  name: PandaDoc REST API Logs Contacts API
  slug: postman-pandadoc-contacts-api
- collection_type: postman
  name: PandaDoc REST API Logs Document Attachments API
  slug: postman-pandadoc-document-attachments-api
- collection_type: postman
  name: PandaDoc REST API Logs Document Fields API
  slug: postman-pandadoc-document-fields-api
- collection_type: postman
  name: PandaDoc REST API Logs Document Link to CRM API
  slug: postman-pandadoc-document-link-to-crm-api
- collection_type: postman
  name: PandaDoc REST API Logs Document Recipients API
  slug: postman-pandadoc-document-recipients-api
- collection_type: postman
  name: PandaDoc REST API Logs Document Reminders API
  slug: postman-pandadoc-document-reminders-api
- collection_type: postman
  name: PandaDoc REST API Logs Documents API
  slug: postman-pandadoc-documents-api
- collection_type: postman
  name: PandaDoc REST API Logs Folders API
  slug: postman-pandadoc-folders-api
- collection_type: postman
  name: PandaDoc REST API Logs Forms API
  slug: postman-pandadoc-forms-api
- collection_type: postman
  name: PandaDoc REST API Logs Members API
  slug: postman-pandadoc-members-api
- collection_type: postman
  name: PandaDoc REST API Logs Templates API
  slug: postman-pandadoc-templates-api
- collection_type: postman
  name: PandaDoc REST API Logs Webhook Events API
  slug: postman-pandadoc-webhook-events-api
- collection_type: postman
  name: PandaDoc REST API Logs Webhook Subscriptions API
  slug: postman-pandadoc-webhook-subscriptions-api
- collection_type: postman
  name: PandaDoc REST API Logs Workspaces API
  slug: postman-pandadoc-workspaces-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PandaDoc REST API Logs API
  slug: open-pandadoc-api-logs-api
- collection_type: open
  name: PandaDoc REST API Logs Contacts API
  slug: open-pandadoc-contacts-api
- collection_type: open
  name: PandaDoc REST API Logs Document Attachments API
  slug: open-pandadoc-document-attachments-api
- collection_type: open
  name: PandaDoc REST API Logs Document Fields API
  slug: open-pandadoc-document-fields-api
- collection_type: open
  name: PandaDoc REST API Logs Document Link to CRM API
  slug: open-pandadoc-document-link-to-crm-api
- collection_type: open
  name: PandaDoc REST API Logs Document Recipients API
  slug: open-pandadoc-document-recipients-api
- collection_type: open
  name: PandaDoc REST API Logs Document Reminders API
  slug: open-pandadoc-document-reminders-api
- collection_type: open
  name: PandaDoc REST API Logs Documents API
  slug: open-pandadoc-documents-api
- collection_type: open
  name: PandaDoc REST API Logs Folders API
  slug: open-pandadoc-folders-api
- collection_type: open
  name: PandaDoc REST API Logs Forms API
  slug: open-pandadoc-forms-api
- collection_type: open
  name: PandaDoc REST API Logs Members API
  slug: open-pandadoc-members-api
- collection_type: open
  name: PandaDoc REST API
  slug: open-pandadoc-rest-api
- collection_type: open
  name: PandaDoc REST API Logs Templates API
  slug: open-pandadoc-templates-api
- collection_type: open
  name: PandaDoc REST API Logs Webhook Events API
  slug: open-pandadoc-webhook-events-api
- collection_type: open
  name: PandaDoc REST API Logs Webhook Subscriptions API
  slug: open-pandadoc-webhook-subscriptions-api
- collection_type: open
  name: PandaDoc REST API Logs Workspaces API
  slug: open-pandadoc-workspaces-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/pandadoc/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pandadoc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pandadoc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pandadoc-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pandadoc-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PandaDoc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pandadoc
- group: start
  title: ''
  type: Portal
  url: https://developers.pandadoc.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.pandadoc.com/docs/getting-started
- group: company
  title: ''
  type: Website
  url: https://www.pandadoc.com/
- group: company
  title: ''
  type: Blog
  url: https://www.pandadoc.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.pandadoc.com/login/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pandadoc.com/privacy-notice/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pandadoc.com/terms-of-use/
- group: operate
  title: ''
  type: Support
  url: https://support.pandadoc.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/pandadoc-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pandadoc-document-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/pandadoc-webhook-event-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.pandadoc.com/llms.txt
created: '2026-03-21'
description: PandaDoc is a document automation platform that enables businesses to create, send, track, and e-sign documents programmatically. Their developer platform provides REST APIs and embedded tools for integrating document generation, e-signature collection, and workflow automation directly into third-party applications.
features:
- 'Free: 60 documents/year, unlimited seats'
- 'Starter at $19/mo: 110 documents/year, audit trail'
- 'Business at $49/seat/mo: unlimited documents, CRM integrations'
- 'Enterprise: CPQ, workflow automation, SSO, API access'
- REST API at api.pandadoc.com
- Default 100 req/min/workspace
- Documents API + Templates API + Contacts API
- OAuth 2.0 + API keys (Bearer)
- Webhooks for document state changes
- Drag-and-drop editor with rich media
- E-signature legally binding (eIDAS, ESIGN)
- Audit trail for all document interactions
- CRM integrations (Salesforce, HubSpot, etc.)
- Approval workflows
- Deal rooms for buyer collaboration
- Smart content for dynamic documents (Enterprise)
finops:
- name: Pandadoc Finops
  service_category: E-Signature / Documents
  slug: pandadoc-finops
graphqls:
- description: This GraphQL schema represents the PandaDoc document automation and e-signature platform. PandaDoc provides REST APIs at `https://api.pandadoc.com/public/v1` for creating, sending, tracking, and e-sig
  name: PandaDoc GraphQL Schema
  slug: pandadoc-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pandadoc.png
json_schemas:
- name: ApiLogListResponse
  property_count: 1
  slug: pandadoc-apiloglistresponse
- name: Contact
  property_count: 12
  slug: pandadoc-contact
- name: ContactCreateRequest
  property_count: 6
  slug: pandadoc-contactcreaterequest
- name: ContactListResponse
  property_count: 1
  slug: pandadoc-contactlistresponse
- name: ContactUpdateRequest
  property_count: 6
  slug: pandadoc-contactupdaterequest
- name: PandaDoc Document
  property_count: 17
  slug: pandadoc-document
- name: DocumentAttachment
  property_count: 3
  slug: pandadoc-documentattachment
- name: DocumentAttachmentsResponse
  property_count: 1
  slug: pandadoc-documentattachmentsresponse
- name: DocumentAutoReminderResponse
  property_count: 2
  slug: pandadoc-documentautoreminderresponse
- name: DocumentCreateRequest
  property_count: 9
  slug: pandadoc-documentcreaterequest
- name: DocumentCreateResponse
  property_count: 7
  slug: pandadoc-documentcreateresponse
- name: DocumentDetailsResponse
  property_count: 11
  slug: pandadoc-documentdetailsresponse
- name: DocumentField
  property_count: 5
  slug: pandadoc-documentfield
- name: DocumentFieldsResponse
  property_count: 1
  slug: pandadoc-documentfieldsresponse
- name: DocumentFieldsUpdateRequest
  property_count: 1
  slug: pandadoc-documentfieldsupdaterequest
- name: DocumentListItem
  property_count: 7
  slug: pandadoc-documentlistitem
- name: DocumentListResponse
  property_count: 1
  slug: pandadoc-documentlistresponse
- name: DocumentRecipient
  property_count: 11
  slug: pandadoc-documentrecipient
- name: DocumentRecipientCreateRequest
  property_count: 7
  slug: pandadoc-documentrecipientcreaterequest
- name: DocumentRecipientsResponse
  property_count: 1
  slug: pandadoc-documentrecipientsresponse
- name: DocumentRecipientUpdateRequest
  property_count: 4
  slug: pandadoc-documentrecipientupdaterequest
- name: DocumentSendRequest
  property_count: 4
  slug: pandadoc-documentsendrequest
- name: DocumentSendResponse
  property_count: 3
  slug: pandadoc-documentsendresponse
- name: DocumentSessionCreateRequest
  property_count: 3
  slug: pandadoc-documentsessioncreaterequest
- name: DocumentSessionCreateResponse
  property_count: 1
  slug: pandadoc-documentsessioncreateresponse
- name: DocumentStatus
  property_count: 0
  slug: pandadoc-documentstatus
- name: DocumentStatusResponse
  property_count: 3
  slug: pandadoc-documentstatusresponse
- name: ErrorResponse
  property_count: 2
  slug: pandadoc-errorresponse
- name: Folder
  property_count: 4
  slug: pandadoc-folder
- name: FolderCreateRequest
  property_count: 2
  slug: pandadoc-foldercreaterequest
- name: FolderListResponse
  property_count: 1
  slug: pandadoc-folderlistresponse
- name: FormListItem
  property_count: 4
  slug: pandadoc-formlistitem
- name: FormListResponse
  property_count: 1
  slug: pandadoc-formlistresponse
- name: LinkedObjectsResponse
  property_count: 1
  slug: pandadoc-linkedobjectsresponse
- name: Member
  property_count: 7
  slug: pandadoc-member
- name: MemberListResponse
  property_count: 1
  slug: pandadoc-memberlistresponse
- name: TemplateDetailsResponse
  property_count: 7
  slug: pandadoc-templatedetailsresponse
- name: TemplateListItem
  property_count: 5
  slug: pandadoc-templatelistitem
- name: TemplateListResponse
  property_count: 1
  slug: pandadoc-templatelistresponse
- name: PandaDoc Webhook Event
  property_count: 0
  slug: pandadoc-webhook-event
- name: WebhookEventDetails
  property_count: 11
  slug: pandadoc-webhookeventdetails
- name: WebhookEventListItem
  property_count: 6
  slug: pandadoc-webhookeventlistitem
- name: WebhookEventListResponse
  property_count: 1
  slug: pandadoc-webhookeventlistresponse
- name: WebhookEventTrigger
  property_count: 0
  slug: pandadoc-webhookeventtrigger
- name: WebhookSharedKeyResponse
  property_count: 1
  slug: pandadoc-webhooksharedkeyresponse
- name: WebhookSubscription
  property_count: 9
  slug: pandadoc-webhooksubscription
- name: WebhookSubscriptionCreateRequest
  property_count: 5
  slug: pandadoc-webhooksubscriptioncreaterequest
- name: WebhookSubscriptionListResponse
  property_count: 1
  slug: pandadoc-webhooksubscriptionlistresponse
- name: WebhookSubscriptionUpdateRequest
  property_count: 5
  slug: pandadoc-webhooksubscriptionupdaterequest
- name: Workspace
  property_count: 4
  slug: pandadoc-workspace
- name: WorkspaceCreateRequest
  property_count: 1
  slug: pandadoc-workspacecreaterequest
- name: WorkspaceListResponse
  property_count: 2
  slug: pandadoc-workspacelistresponse
json_structures:
- name: Pandadoc Structure
  property_count: 0
  slug: pandadoc-structure
jsonld:
- class_count: 0
  name: Pandadoc Context
  property_count: 10
  slug: pandadoc-context
layout: provider
modified: '2026-05-19'
name: PandaDoc
nav: Providers
network: true
overview: 'PandaDoc publishes 15 APIs on the [APIs.io](https://apis.io/) network, including API Logs API, Contacts API, Document Attachments API, and 12 more. Tagged areas include Document Automation, E-Signature, Document-Management, Document Generation, and Webhook.


  The PandaDoc catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  PandaDoc''s developer surface includes authentication, developer portal, documentation, engineering blog, support, and 14 more developer resources.'
plans:
- name: Pandadoc Plans Pricing
  plan_count: 4
  slug: pandadoc-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Pandadoc Rate Limits
  slug: pandadoc-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: PandaDoc API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: pandadoc-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: PandaDoc API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: pandadoc-jsonschema-spectral-rules
scopes:
- name: Pandadoc Scopes
  scope_count: 2
  slug: pandadoc-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.5
    catalog_earned_first_party: 0.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.8
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 13.6
    contract_quality: 76.8
    developer_ergonomics: 38.1
    discoverability: 75.9
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 44.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 15
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pandadoc/refs/heads/main/screenshots/pandadoc-2026-06-20T191334.png
security:
- kind: authentication
  name: Pandadoc Authentication
  slug: pandadoc-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Pandadoc Domain Security
  slug: pandadoc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pandadoc
tags:
- Document Automation
- E-Signature
- Document-Management
- Document Generation
- Webhook
website: https://www.pandadoc.com/
---
