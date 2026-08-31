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
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Microsoft Outlook Agentic Access
  operation_count: 31
  slug: microsoft-outlook-agentic-access
  summary_line: 31 operations · 23 acting
api_count: 1
apis:
- description: JavaScript API for building Outlook add-ins that extend Outlook functionality with custom features, using the Office.js library and the Mailbox requirement set.
  name: Outlook Add-ins API
  slug: outlook-add-ins-api
- description: Operations on message attachments
  name: Microsoft Outlook Attachments API
  slug: microsoft-outlook-attachments-api
- description: Operations on mail folders in a user mailbox
  name: Microsoft Outlook Mail Folders API
  slug: microsoft-outlook-mail-folders-api
- description: Operations on email messages in a user mailbox
  name: Microsoft Outlook Messages API
  slug: microsoft-outlook-messages-api
arazzos:
- description: Create an archive folder, copy a message into it, and read the copy back.
  name: Microsoft Outlook Archive Copy of a Message
  slug: microsoft-outlook-archive-copy-message-workflow
- description: Create a parent folder, a child subfolder, and a seed draft inside the child.
  name: Microsoft Outlook Build Folder Tree and Seed Draft
  slug: microsoft-outlook-build-folder-tree-and-seed-draft-workflow
- description: Create a draft message, attach a file to it, and send the finished draft.
  name: Microsoft Outlook Compose, Attach, and Send
  slug: microsoft-outlook-compose-attach-send-workflow
- description: Create a draft, refine its body and importance, then send the polished draft.
  name: Microsoft Outlook Draft, Refine, and Send
  slug: microsoft-outlook-draft-refine-send-workflow
- description: Create a mail folder, find a matching message, and move it into the folder.
  name: Microsoft Outlook File Message into New Folder
  slug: microsoft-outlook-file-message-into-new-folder-workflow
- description: Find a message by subject, read it, then forward it to a new recipient.
  name: Microsoft Outlook Find and Forward
  slug: microsoft-outlook-find-and-forward-workflow
- description: Find a message with attachments, inspect the first one, and delete it.
  name: Microsoft Outlook Inspect and Remove Attachment
  slug: microsoft-outlook-inspect-and-remove-attachment-workflow
- description: Draft a message and open an upload session for a large (3-150 MB) attachment.
  name: Microsoft Outlook Large Attachment Upload Session
  slug: microsoft-outlook-large-attachment-upload-session-workflow
- description: Create a destination folder, find a source folder by name, and move it under the destination.
  name: Microsoft Outlook Reorganize Folder
  slug: microsoft-outlook-reorganize-folder-workflow
- description: Create a reply draft for a message, attach a file, and send the reply.
  name: Microsoft Outlook Reply Draft with Attachment
  slug: microsoft-outlook-reply-draft-with-attachment-workflow
- description: Open a mail folder, list its unread messages, and mark the top one as read.
  name: Microsoft Outlook Review Folder and Mark Read
  slug: microsoft-outlook-review-folder-and-mark-read-workflow
- description: List the newest messages, read the top one in full, and reply to its sender.
  name: Microsoft Outlook Triage and Reply
  slug: microsoft-outlook-triage-and-reply-workflow
artifact_total: 104
asyncapis:
- description: 'AsyncAPI specification for Microsoft Graph change notifications (webhooks) for Outlook mail resources. Enables real-time event-driven architecture by subscribing to changes in messages, mail folders, '
  name: Microsoft Outlook Change Notifications
  slug: microsoft-outlook-change-notifications-asyncapi
collections:
- collection_type: postman
  name: Microsoft Outlook Microsoft Graph Mail API
  slug: postman-microsoft-graph-mail-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Outlook Microsoft Graph Mail API
  slug: open-microsoft-graph-mail-api
- collection_type: open
  name: Microsoft Outlook Microsoft Graph Mail Attachments API
  slug: open-microsoft-outlook-attachments-api
- collection_type: open
  name: Microsoft Outlook Microsoft Graph Mail Attachments Mail Folders API
  slug: open-microsoft-outlook-mail-folders-api
- collection_type: open
  name: Microsoft Outlook Microsoft Graph Mail Attachments Messages API
  slug: open-microsoft-outlook-messages-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-outlook-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-outlook-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-outlook-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-outlook-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-outlook-scopes.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/microsoft-outlook-trust-center.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-outlook-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-outlook-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-outlook-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-outlook-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/microsoft-outlook-microsoft-graph-mail-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-outlook-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-outlook-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-outlook-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-outlook-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-outlook-data-model.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-outlook-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-outlook-cli.yml
- group: design
  title: ''
  type: Components
  url: components/microsoft-outlook-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-outlook-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-outlook/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-archive-copy-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-build-folder-tree-and-seed-draft-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-compose-attach-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-draft-refine-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-file-message-into-new-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-find-and-forward-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-inspect-and-remove-attachment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-large-attachment-upload-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-reorganize-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-reply-draft-with-attachment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-review-folder-and-mark-read-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-triage-and-reply-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/graph/overview
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/outlook/
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/tag/outlook/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: start
  title: ''
  type: Signup
  url: https://developer.microsoft.com/en-us/microsoft-365/dev-program
- group: start
  title: ''
  type: Login
  url: https://portal.azure.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://learn.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/microsoft-graph
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.microsoft.com/en-us/graph/quick-start
- group: learn
  title: ''
  type: Training
  url: https://learn.microsoft.com/en-us/training/paths/m365-msgraph-fundamentals/
created: '2024'
description: Microsoft Outlook is a personal information manager and email client that is part of the Microsoft Office suite. It provides email, calendar, contact management, task management, and other productivity features.
examples:
- key_count: 2
  name: Microsoft Graph Mail Attachment Collection Response Example
  slug: microsoft-graph-mail-attachment-collection-response-example
- key_count: 10
  name: Microsoft Graph Mail Attachment Example
  slug: microsoft-graph-mail-attachment-example
- key_count: 2
  name: Microsoft Graph Mail Date Time Time Zone Example
  slug: microsoft-graph-mail-date-time-time-zone-example
- key_count: 2
  name: Microsoft Graph Mail Email Address Example
  slug: microsoft-graph-mail-email-address-example
- key_count: 1
  name: Microsoft Graph Mail Followup Flag Example
  slug: microsoft-graph-mail-followup-flag-example
- key_count: 2
  name: Microsoft Graph Mail Internet Message Header Example
  slug: microsoft-graph-mail-internet-message-header-example
- key_count: 2
  name: Microsoft Graph Mail Item Body Example
  slug: microsoft-graph-mail-item-body-example
- key_count: 3
  name: Microsoft Graph Mail Mail Folder Collection Response Example
  slug: microsoft-graph-mail-mail-folder-collection-response-example
- key_count: 7
  name: Microsoft Graph Mail Mail Folder Example
  slug: microsoft-graph-mail-mail-folder-example
- key_count: 4
  name: Microsoft Graph Mail Message Collection Response Example
  slug: microsoft-graph-mail-message-collection-response-example
- key_count: 27
  name: Microsoft Graph Mail Message Example
  slug: microsoft-graph-mail-message-example
- key_count: 1
  name: Microsoft Graph Mail O Data Error Example
  slug: microsoft-graph-mail-o-data-error-example
- key_count: 0
  name: Microsoft Graph Mail Recipient Example
  slug: microsoft-graph-mail-recipient-example
- key_count: 3
  name: Microsoft Graph Mail Upload Session Example
  slug: microsoft-graph-mail-upload-session-example
features:
- Email management with full CRUD operations on messages
- Calendar scheduling with meeting invitations and RSVPs
- Contact management across personal and organizational directories
- Task and to-do list management
- Focused Inbox classification and mail rules
- Real-time change notifications via webhooks
- Rich attachment handling with large file support
- Categories for organizing messages, events, and contacts
- People insights aggregated across multiple sources
- Outlook add-in extensibility via Office.js
finops:
- name: Microsoft Outlook Finops
  service_category: Email and Calendar
  slug: microsoft-outlook-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2019/11/Outlook-logo.png
integrations:
- Microsoft Teams
- Microsoft Power Automate
- Microsoft Power Apps
- SharePoint
- OneDrive
- Azure Active Directory
- Microsoft To Do
json_schemas:
- name: AttachmentCollectionResponse
  property_count: 2
  slug: microsoft-graph-mail-attachment-collection-response
- name: Attachment
  property_count: 10
  slug: microsoft-graph-mail-attachment
- name: DateTimeTimeZone
  property_count: 2
  slug: microsoft-graph-mail-date-time-time-zone
- name: EmailAddress
  property_count: 2
  slug: microsoft-graph-mail-email-address
- name: FollowupFlag
  property_count: 1
  slug: microsoft-graph-mail-followup-flag
- name: InternetMessageHeader
  property_count: 2
  slug: microsoft-graph-mail-internet-message-header
- name: ItemBody
  property_count: 2
  slug: microsoft-graph-mail-item-body
- name: MailFolderCollectionResponse
  property_count: 3
  slug: microsoft-graph-mail-mail-folder-collection-response
- name: MailFolder
  property_count: 7
  slug: microsoft-graph-mail-mail-folder
- name: MessageCollectionResponse
  property_count: 4
  slug: microsoft-graph-mail-message-collection-response
- name: Message
  property_count: 27
  slug: microsoft-graph-mail-message
- name: ODataError
  property_count: 1
  slug: microsoft-graph-mail-o-data-error
- name: Recipient
  property_count: 0
  slug: microsoft-graph-mail-recipient
- name: UploadSession
  property_count: 3
  slug: microsoft-graph-mail-upload-session
- name: Microsoft Outlook Message
  property_count: 32
  slug: microsoft-outlook-message
json_structures:
- name: Microsoft Graph Mail Attachment Collection Response Structure
  property_count: 2
  slug: microsoft-graph-mail-attachment-collection-response-structure
- name: Microsoft Graph Mail Attachment Structure
  property_count: 10
  slug: microsoft-graph-mail-attachment-structure
- name: Microsoft Graph Mail Date Time Time Zone Structure
  property_count: 2
  slug: microsoft-graph-mail-date-time-time-zone-structure
- name: Microsoft Graph Mail Email Address Structure
  property_count: 2
  slug: microsoft-graph-mail-email-address-structure
- name: Microsoft Graph Mail Followup Flag Structure
  property_count: 1
  slug: microsoft-graph-mail-followup-flag-structure
- name: Microsoft Graph Mail Internet Message Header Structure
  property_count: 2
  slug: microsoft-graph-mail-internet-message-header-structure
- name: Microsoft Graph Mail Item Body Structure
  property_count: 2
  slug: microsoft-graph-mail-item-body-structure
- name: Microsoft Graph Mail Mail Folder Collection Response Structure
  property_count: 3
  slug: microsoft-graph-mail-mail-folder-collection-response-structure
- name: Microsoft Graph Mail Mail Folder Structure
  property_count: 7
  slug: microsoft-graph-mail-mail-folder-structure
- name: Microsoft Graph Mail Message Collection Response Structure
  property_count: 4
  slug: microsoft-graph-mail-message-collection-response-structure
- name: Microsoft Graph Mail Message Structure
  property_count: 27
  slug: microsoft-graph-mail-message-structure
- name: Microsoft Graph Mail O Data Error Structure
  property_count: 1
  slug: microsoft-graph-mail-o-data-error-structure
- name: Microsoft Graph Mail Recipient Structure
  property_count: 0
  slug: microsoft-graph-mail-recipient-structure
- name: Microsoft Graph Mail Upload Session Structure
  property_count: 3
  slug: microsoft-graph-mail-upload-session-structure
jsonld:
- class_count: 0
  name: Microsoft Graph Mail Context
  property_count: 0
  slug: microsoft-graph-mail-context
- class_count: 0
  name: Microsoft Outlook Context
  property_count: 13
  slug: microsoft-outlook-context
layout: provider
mcp_servers:
- description: ''
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-06-20'
name: Microsoft Outlook
nav: Providers
network: true
overview: 'Microsoft Outlook publishes 3 APIs on the [APIs.io](https://apis.io/) network: Attachments API, Mail Folders API, and Messages API. Tagged areas include Calendar, Contacts, Email, Enterprise, and Microsoft.


  The Microsoft Outlook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 3 Spectral governance rulesets.


  Microsoft Outlook''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, getting-started guide, documentation, and 44 more developer resources.'
plans:
- name: Microsoft Outlook Plans Pricing
  plan_count: 5
  slug: microsoft-outlook-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 7
  name: Microsoft Outlook Rate Limits
  slug: microsoft-outlook-rate-limits
rules:
- effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Microsoft Outlook API Rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: microsoft-outlook-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Microsoft Outlook API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-outlook-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Microsoft Outlook API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: microsoft-outlook-spectral-rules
scopes:
- name: Microsoft Outlook Scopes
  scope_count: 20
  slug: microsoft-outlook-scopes
  summary_line: 20 scopes · authorizationCode
score:
  band: strong
  composite: 64.0
  coverage:
    artifact_dirs: 34
    catalog_gap: 50.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 87.4
    developer_ergonomics: 83.3
    discoverability: 83.3
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 64.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-outlook/refs/heads/main/screenshots/microsoft-outlook-2026-06-20T185517.png
security:
- kind: authentication
  name: Microsoft Outlook Authentication
  slug: microsoft-outlook-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Outlook Domain Security
  slug: microsoft-outlook-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Outlook Vulnerability Disclosure
  slug: microsoft-outlook-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Outlook Trust Center
  slug: microsoft-outlook-trust-center
  summary_line: SOC 1, SOC 2, SOC 3, ISO 27001, ISO 27017, ISO 27018, ISO 27701, ISO 42001, ISO 22301, CSA STAR Certification, CSA STAR Attestation, FedRAMP, FIPS 140-2, HIPAA / HITECH, HITRUST, PCI DSS, GDPR, SOX
slug: microsoft-outlook
tags:
- Calendar
- Contacts
- Email
- Enterprise
- Microsoft
- Office 365
- Productivity
use_cases:
- Building email client integrations and automation workflows
- Scheduling meetings and managing calendars programmatically
- Syncing contacts between systems
- Creating automated email processing pipelines
- Building productivity dashboards with mail and calendar data
- Extending Outlook with custom add-ins
website: https://developer.microsoft.com/en-us/graph
---
