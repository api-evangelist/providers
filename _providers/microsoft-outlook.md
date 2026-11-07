---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.5
  scored_at: '2026-11-06'
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
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on message attachments
  name: Microsoft Outlook Attachments API
  slug: microsoft-outlook-attachments-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on mail folders in a user mailbox
  name: Microsoft Outlook Mail Folders API
  slug: microsoft-outlook-mail-folders-api
- baseURL: https://graph.microsoft.com/v1.0
  baseurl_source: declared
  description: Operations on email messages in a user mailbox
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
artifact_total: 107
asyncapis:
- description: 'AsyncAPI specification for Microsoft Graph change notifications (webhooks) for Outlook mail resources. Enables real-time event-driven architecture by subscribing to changes in messages, mail folders, '
  name: Microsoft Outlook Change Notifications
  slug: microsoft-outlook-change-notifications-asyncapi
collections:
- collection_type: postman
  name: Microsoft Outlook Microsoft Graph Mail API
  slug: postman-microsoft-graph-mail-api
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
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/rules/microsoft-outlook-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-outlook-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/rules/microsoft-outlook-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-outlook-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/rules/microsoft-outlook-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-outlook-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/rules/microsoft-outlook-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-outlook-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/json-ld/microsoft-graph-mail-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-graph-mail-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/vocabulary/microsoft-outlook-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-outlook-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-outlook/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/microsoft-outlook/asyncapi/microsoft-outlook-change-notifications-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/microsoft-outlook-change-notifications-asyncapi.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/graph/versioning-and-support#deprecation
- group: build
  href: https://artifacts.apis.io/microsoft-outlook/mcp/microsoft-outlook-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-outlook-tool-crosswalk.yml
- group: other
  href: https://artifacts.apis.io/microsoft-outlook/hosts/microsoft-outlook-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-outlook-hosts.yml
- group: build
  href: https://artifacts.apis.io/microsoft-outlook/integrations/microsoft-outlook-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/microsoft-outlook-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/microsoft-outlook/vendors/microsoft-outlook-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-outlook-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: commercial
  href: https://artifacts.apis.io/microsoft-outlook/plans/microsoft-outlook-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-outlook-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-outlook/rate-limits/microsoft-outlook-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-outlook-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-outlook/finops/microsoft-outlook-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-outlook-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/
- group: agent
  href: https://artifacts.apis.io/microsoft-outlook/agentic-access/microsoft-outlook-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-outlook-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-outlook/security/microsoft-outlook-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-outlook-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-outlook/security/microsoft-outlook-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-outlook-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-outlook/authentication/microsoft-outlook-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-outlook-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-outlook/scopes/microsoft-outlook-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-outlook-scopes.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-outlook/security/microsoft-outlook-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-outlook-trust-center.yml
- group: build
  href: https://artifacts.apis.io/microsoft-outlook/packages/microsoft-outlook-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-outlook-packages.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-outlook/well-known/microsoft-outlook-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-outlook-well-known.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-outlook/mcp/microsoft-outlook-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-outlook-mcp.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-outlook/llms/microsoft-outlook-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-outlook-llms.txt
- group: other
  href: https://artifacts.apis.io/microsoft-outlook/overlays/microsoft-outlook-microsoft-graph-mail-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/microsoft-outlook-microsoft-graph-mail-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/conformance/microsoft-outlook-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-outlook-conformance.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/errors/microsoft-outlook-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-outlook-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/lifecycle/microsoft-outlook-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-outlook-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/conventions/microsoft-outlook-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-outlook-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/data-model/microsoft-outlook-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-outlook-data-model.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-outlook/changelog/microsoft-outlook-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-outlook-changelog.yml
- group: build
  href: https://artifacts.apis.io/microsoft-outlook/cli/microsoft-outlook-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-outlook-cli.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/components/microsoft-outlook-components.yml
  title: ''
  type: Components
  url: components/microsoft-outlook-components.yml
- group: start
  href: https://artifacts.apis.io/microsoft-outlook/sandbox/microsoft-outlook-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-outlook-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-outlook/overview
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-archive-copy-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-archive-copy-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-build-folder-tree-and-seed-draft-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-build-folder-tree-and-seed-draft-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-compose-attach-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-compose-attach-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-draft-refine-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-draft-refine-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-file-message-into-new-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-file-message-into-new-folder-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-find-and-forward-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-find-and-forward-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-inspect-and-remove-attachment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-inspect-and-remove-attachment-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-large-attachment-upload-session-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-large-attachment-upload-session-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-reorganize-folder-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-reorganize-folder-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-reply-draft-with-attachment-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-reply-draft-with-attachment-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-review-folder-and-mark-read-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/microsoft-outlook-review-folder-and-mark-read-workflow.yml
- group: design
  href: https://artifacts.apis.io/microsoft-outlook/arazzo/microsoft-outlook-triage-and-reply-workflow.yml
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
- has_sources: true
  method: generated
  name: Microsoft Outlook Finops
  primary_unit: ''
  service_category: Email and Calendar
  slug: microsoft-outlook-finops
  template: false
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
- description: Remote MCP server at mcp.svc.cloud.microsoft over HTTP; 3 tools listed.
  name: Microsoft MCP Server for Enterprise
  slug: microsoft-mcp-server-for-enterprise
modified: '2026-06-20'
name: Microsoft Outlook
nav: Providers
network: true
overview: 'Microsoft Outlook publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Mail Folders API, Messages API, and 1 more. Tagged areas include Calendar, Contacts, Email, Enterprise, and Microsoft.


  The Microsoft Outlook catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 4 Spectral governance rulesets.


  Microsoft Outlook''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, getting-started guide, documentation, and 64 more developer resources.'
plans:
- name: Microsoft Outlook Plans Pricing
  plan_count: 5
  slug: microsoft-outlook-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 7
  name: Microsoft Outlook Rate Limits
  slug: microsoft-outlook-rate-limits
rules:
- authorship: generated
  effective_rule_count: 36
  extends:
  - spectral:asyncapi
  name: Microsoft Outlook — asyncapi rules
  rule_count: 9
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 7
  slug: microsoft-outlook-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Microsoft Outlook — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-outlook-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 110
  extends:
  - spectral:oas
  name: Microsoft Outlook API Rules
  rule_count: 69
  severity_counts:
    error: 62
    hint: 0
    info: 2
    warn: 5
  slug: microsoft-outlook-rules
- authorship: generated
  effective_rule_count: 59
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
  band: exemplar
  composite: 70.6
  coverage:
    artifact_dirs: 41
    catalog_earned: 65.4
    catalog_earned_first_party: 0.0
    catalog_gap: 49.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.7
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 79.8
    developer_ergonomics: 81.5
    discoverability: 83.3
    operational_transparency: 52.6
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-outlook/microsoft-outlook-2026-06-20T185517.png
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
  summary_line: GDPR
skill_count: 3
skills:
- name: microsoft-outlook-compose-attach-send
  slug: microsoft-outlook-compose-attach-send
- name: microsoft-outlook-file-into-folder
  slug: microsoft-outlook-file-into-folder
- name: microsoft-outlook-triage-and-reply
  slug: microsoft-outlook-triage-and-reply
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
website: https://www.microsoft.com/
---
