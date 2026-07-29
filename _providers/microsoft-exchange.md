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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 51
  human_in_the_loop: 0
  name: Microsoft Exchange Agentic Access
  operation_count: 79
  slug: microsoft-exchange-agentic-access
  summary_line: 79 operations · 51 acting
api_count: 20
apis:
- description: Legacy SOAP-based API for Exchange Server providing comprehensive access to mailbox data and operations. Planned for deprecation in Exchange Online in October 2026, with Microsoft Graph recommended fo
  name: Exchange Web Services (EWS)
  slug: exchange-web-services-ews
- description: PowerShell module for managing Exchange Online through REST-based cmdlets. Provides the complete Exchange management surface for administrative tasks including mailbox management, mail flow rules, and
  name: Exchange Online PowerShell API
  slug: exchange-online-powershell-api
- description: Service that enables client applications to automatically configure themselves for Exchange connectivity using minimal user input. Supports SOAP and POX protocols for discovering EWS endpoint URLs and
  name: Exchange Autodiscover API
  slug: exchange-autodiscover-api
- description: View accepted domains and their configurations
  name: Microsoft Exchange Accepted Domains API
  slug: microsoft-exchange-accepted-domains-api
- description: Operations for managing message attachments
  name: Microsoft Exchange Attachments API
  slug: microsoft-exchange-attachments-api
- description: Operations for managing calendars
  name: Microsoft Exchange Calendars API
  slug: microsoft-exchange-calendars-api
- description: Operations for managing contact folders
  name: Microsoft Exchange Contact Folders API
  slug: microsoft-exchange-contact-folders-api
- description: Operations for managing personal contacts
  name: Microsoft Exchange Contacts API
  slug: microsoft-exchange-contacts-api
- description: Retrieve distribution group and dynamic distribution group membership
  name: Microsoft Exchange Distribution Groups API
  slug: microsoft-exchange-distribution-groups-api
- description: Operations for managing calendar events
  name: Microsoft Exchange Events API
  slug: microsoft-exchange-events-api
- description: Operations for managing mail folders
  name: Microsoft Exchange Mail Folders API
  slug: microsoft-exchange-mail-folders-api
- description: Operations for discovering mailbox structure and content
  name: Microsoft Exchange Mailbox Discovery API
  slug: microsoft-exchange-mailbox-discovery-api
- description: Operations for exporting content from mailboxes
  name: Microsoft Exchange Mailbox Export API
  slug: microsoft-exchange-mailbox-export-api
- description: View and manage mailbox folder permissions
  name: Microsoft Exchange Mailbox Folder Permissions API
  slug: microsoft-exchange-mailbox-folder-permissions-api
- description: Operations for importing content into mailboxes
  name: Microsoft Exchange Mailbox Import API
  slug: microsoft-exchange-mailbox-import-api
- description: View and update mailbox properties and delegation
  name: Microsoft Exchange Mailboxes API
  slug: microsoft-exchange-mailboxes-api
- description: Operations for managing email messages
  name: Microsoft Exchange Messages API
  slug: microsoft-exchange-messages-api
- description: Retrieve organization-level Exchange configuration
  name: Microsoft Exchange Organization Configuration API
  slug: microsoft-exchange-organization-configuration-api
- description: Operations for retrieving relevant people
  name: Microsoft Exchange People API
  slug: microsoft-exchange-people-api
- description: Operations for scheduling and free/busy information
  name: Microsoft Exchange Scheduling API
  slug: microsoft-exchange-scheduling-api
arazzos:
- description: Find a message that has attachments, read it, and list its attachments.
  name: Microsoft Exchange Audit Message Attachments
  slug: microsoft-exchange-audit-message-attachments-workflow
- description: Read Exchange organization configuration, then list accepted domains.
  name: Microsoft Exchange Audit Organization and Domains
  slug: microsoft-exchange-audit-org-and-domains-workflow
- description: Create a draft message, add a file attachment to it, then send the draft.
  name: Microsoft Exchange Compose, Attach, and Send Mail
  slug: microsoft-exchange-compose-attach-send-mail-workflow
- description: Discover a user's mailbox, drill into its folders, and list folder items.
  name: Microsoft Exchange Discover Mailbox Content
  slug: microsoft-exchange-discover-mailbox-content-workflow
- description: Suggest meeting times for attendees, then book the top suggestion.
  name: Microsoft Exchange Find Times and Book a Meeting
  slug: microsoft-exchange-find-times-and-book-meeting-workflow
- description: Read current folder permissions, then add a permission for a user.
  name: Microsoft Exchange Grant a Mailbox Folder Permission
  slug: microsoft-exchange-grant-folder-permission-workflow
- description: Read a mailbox's properties, then grant Send on Behalf delegation.
  name: Microsoft Exchange Inspect and Delegate a Mailbox
  slug: microsoft-exchange-inspect-and-delegate-mailbox-workflow
- description: Pick a source item, export its full MIME content, and import it elsewhere.
  name: Microsoft Exchange Migrate a Mailbox Item
  slug: microsoft-exchange-migrate-mailbox-item-workflow
- description: Create a contact folder, add a contact to it, and read the contact back.
  name: Microsoft Exchange Organize a Contacts Folder
  slug: microsoft-exchange-organize-contacts-folder-workflow
- description: Create a mail folder, confirm it, and create a message inside it.
  name: Microsoft Exchange Organize a Folder and File a Message
  slug: microsoft-exchange-organize-folder-and-file-message-workflow
- description: Create a forward draft, edit its body, and send it to new recipients.
  name: Microsoft Exchange Prepare and Send a Forward
  slug: microsoft-exchange-prepare-and-send-forward-workflow
- description: Create a new calendar, add an event to it, and read the event back.
  name: Microsoft Exchange Provision a Calendar and Add an Event
  slug: microsoft-exchange-provision-calendar-and-add-event-workflow
- description: Find the newest message from a given sender, read it, and send a reply.
  name: Microsoft Exchange Reply to Latest Message from a Sender
  slug: microsoft-exchange-reply-to-latest-from-sender-workflow
- description: List upcoming events, read the next one, and accept the invitation.
  name: Microsoft Exchange Review and Respond to an Invite
  slug: microsoft-exchange-review-and-respond-to-invite-workflow
- description: Create a calendar event, confirm it, then attach a file to it.
  name: Microsoft Exchange Schedule an Event with an Attachment
  slug: microsoft-exchange-schedule-event-with-attachment-workflow
- description: Find the newest unread inbox message, read it, mark it read, and file it.
  name: Microsoft Exchange Triage and Move a Message
  slug: microsoft-exchange-triage-and-move-message-workflow
- description: Find a contact by email and update it if it exists, otherwise create it.
  name: Microsoft Exchange Upsert a Contact
  slug: microsoft-exchange-upsert-contact-workflow
artifact_total: 113
collections:
- collection_type: postman
  name: Microsoft Exchange Exchange Online Admin API
  slug: postman-microsoft-exchange-admin-api
- collection_type: postman
  name: Microsoft Exchange Microsoft Graph Calendar API
  slug: postman-microsoft-exchange-graph-calendar
- collection_type: postman
  name: Microsoft Exchange Microsoft Graph Contacts API
  slug: postman-microsoft-exchange-graph-contacts
- collection_type: postman
  name: Microsoft Exchange Microsoft Graph Mailbox Import Export API
  slug: postman-microsoft-exchange-graph-import-export
- collection_type: postman
  name: Microsoft Exchange Microsoft Graph Mail API
  slug: postman-microsoft-exchange-graph-mail
- collection_type: postman
  name: Microsoft Exchange Microsoft Graph People API
  slug: postman-microsoft-exchange-graph-people
- collection_type: open
  name: Microsoft Exchange Exchange Online Admin API
  slug: open-microsoft-exchange-admin-api
- collection_type: open
  name: Microsoft Exchange Microsoft Graph Calendar API
  slug: open-microsoft-exchange-graph-calendar
- collection_type: open
  name: Microsoft Exchange Microsoft Graph Contacts API
  slug: open-microsoft-exchange-graph-contacts
- collection_type: open
  name: Microsoft Exchange Microsoft Graph Mailbox Import Export API
  slug: open-microsoft-exchange-graph-import-export
- collection_type: open
  name: Microsoft Exchange Microsoft Graph Mail API
  slug: open-microsoft-exchange-graph-mail
- collection_type: open
  name: Microsoft Exchange Microsoft Graph People API
  slug: open-microsoft-exchange-graph-people
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-exchange-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-exchange-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-exchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-exchange-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-exchange-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/microsoft-exchange-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/microsoft-exchange-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-exchange-security.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/microsoft-exchange-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/microsoft-exchange-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/microsoft-exchange-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-exchange-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-exchange-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/microsoft-exchange-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/microsoft-exchange-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/microsoft-exchange-cli.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/microsoft-exchange-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/microsoft-exchange-sandbox.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-exchange/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-audit-message-attachments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-audit-org-and-domains-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-compose-attach-send-mail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-discover-mailbox-content-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-find-times-and-book-meeting-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-grant-folder-permission-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-inspect-and-delegate-mailbox-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-migrate-mailbox-item-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-organize-contacts-folder-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-organize-folder-and-file-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-prepare-and-send-forward-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-provision-calendar-and-add-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-reply-to-latest-from-sender-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-review-and-respond-to-invite-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-schedule-event-with-attachment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-triage-and-move-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-exchange-upsert-contact-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.microsoft.com/en-us/graph
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/exchange/client-developer/exchange-server-development
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.microsoft.com/en-us/graph/quick-start
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: company
  title: ''
  type: Blog
  url: https://devblogs.microsoft.com/microsoft365dev/tag/exchange/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office365.com/
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us/office
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/OfficeDev
- group: operate
  title: ''
  type: Community
  url: https://techcommunity.microsoft.com/category/exchange
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/microsoft-365/exchange/email
- group: start
  title: ''
  type: Login
  url: https://admin.exchange.microsoft.com
- group: start
  title: ''
  type: Signup
  url: https://signup.azure.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/microsoft-365/exchange/compare-microsoft-exchange-online-plans
- group: other
  title: ''
  type: Graph Explorer
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/microsoft-exchange-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-message-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-calendar-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-mail-folder-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/microsoft-exchange-person-schema.json
created: '2024-01-01'
description: A comprehensive API collection for Microsoft Exchange Server and Exchange Online, providing programmatic access to email, calendars, contacts, and other mailbox resources through Microsoft Graph, EWS, PowerShell, Autodiscover, and the Exchange Online Admin API.
finops:
- name: Microsoft Exchange Finops
  service_category: Email and Collaboration
  slug: microsoft-exchange-finops
image: https://learn.microsoft.com/en-us/media/logos/logo-ms-social.png
json_schemas:
- name: AdminApiResponse
  property_count: 3
  slug: microsoft-exchange-adminapiresponse
- name: Attachment
  property_count: 8
  slug: microsoft-exchange-attachment
- name: AttachmentCollectionResponse
  property_count: 2
  slug: microsoft-exchange-attachmentcollectionresponse
- name: Attendee
  property_count: 4
  slug: microsoft-exchange-attendee
- name: AttendeeBase
  property_count: 2
  slug: microsoft-exchange-attendeebase
- name: Microsoft Exchange Calendar
  property_count: 14
  slug: microsoft-exchange-calendar
- name: CalendarCollectionResponse
  property_count: 3
  slug: microsoft-exchange-calendarcollectionresponse
- name: Microsoft Exchange Contact
  property_count: 38
  slug: microsoft-exchange-contact
- name: ContactCollectionResponse
  property_count: 3
  slug: microsoft-exchange-contactcollectionresponse
- name: ContactDeltaResponse
  property_count: 4
  slug: microsoft-exchange-contactdeltaresponse
- name: ContactFolder
  property_count: 3
  slug: microsoft-exchange-contactfolder
- name: ContactFolderCollectionResponse
  property_count: 3
  slug: microsoft-exchange-contactfoldercollectionresponse
- name: DateTimeTimeZone
  property_count: 2
  slug: microsoft-exchange-datetimetimezone
- name: EmailAddress
  property_count: 2
  slug: microsoft-exchange-emailaddress
- name: Microsoft Exchange Calendar Event
  property_count: 40
  slug: microsoft-exchange-event
- name: EventCollectionResponse
  property_count: 3
  slug: microsoft-exchange-eventcollectionresponse
- name: FollowupFlag
  property_count: 4
  slug: microsoft-exchange-followupflag
- name: InternetMessageHeader
  property_count: 2
  slug: microsoft-exchange-internetmessageheader
- name: ItemBody
  property_count: 2
  slug: microsoft-exchange-itembody
- name: Location
  property_count: 8
  slug: microsoft-exchange-location
- name: LocationConstraint
  property_count: 3
  slug: microsoft-exchange-locationconstraint
- name: LocationConstraintItem
  property_count: 3
  slug: microsoft-exchange-locationconstraintitem
- name: Microsoft Exchange Mail Folder
  property_count: 7
  slug: microsoft-exchange-mail-folder
- name: Mailbox
  property_count: 6
  slug: microsoft-exchange-mailbox
- name: MailboxFolder
  property_count: 7
  slug: microsoft-exchange-mailboxfolder
- name: MailboxItem
  property_count: 8
  slug: microsoft-exchange-mailboxitem
- name: MailFolder
  property_count: 7
  slug: microsoft-exchange-mailfolder
- name: MailFolderCollectionResponse
  property_count: 3
  slug: microsoft-exchange-mailfoldercollectionresponse
- name: MeetingTimeSuggestion
  property_count: 7
  slug: microsoft-exchange-meetingtimesuggestion
- name: MeetingTimeSuggestionsResult
  property_count: 3
  slug: microsoft-exchange-meetingtimesuggestionsresult
- name: Microsoft Exchange Message
  property_count: 31
  slug: microsoft-exchange-message
- name: MessageCollectionResponse
  property_count: 3
  slug: microsoft-exchange-messagecollectionresponse
- name: ODataError
  property_count: 1
  slug: microsoft-exchange-odataerror
- name: OnlineMeetingInfo
  property_count: 6
  slug: microsoft-exchange-onlinemeetinginfo
- name: OutlookGeoCoordinates
  property_count: 5
  slug: microsoft-exchange-outlookgeocoordinates
- name: PatternedRecurrence
  property_count: 2
  slug: microsoft-exchange-patternedrecurrence
- name: Microsoft Exchange Person
  property_count: 20
  slug: microsoft-exchange-person
- name: PersonCollectionResponse
  property_count: 3
  slug: microsoft-exchange-personcollectionresponse
- name: PersonType
  property_count: 2
  slug: microsoft-exchange-persontype
- name: Phone
  property_count: 2
  slug: microsoft-exchange-phone
- name: PhysicalAddress
  property_count: 5
  slug: microsoft-exchange-physicaladdress
- name: Recipient
  property_count: 1
  slug: microsoft-exchange-recipient
- name: RecurrencePattern
  property_count: 7
  slug: microsoft-exchange-recurrencepattern
- name: RecurrenceRange
  property_count: 5
  slug: microsoft-exchange-recurrencerange
- name: ResponseStatus
  property_count: 2
  slug: microsoft-exchange-responsestatus
- name: ScheduleInformation
  property_count: 5
  slug: microsoft-exchange-scheduleinformation
- name: ScheduleItem
  property_count: 6
  slug: microsoft-exchange-scheduleitem
- name: ScoredEmailAddress
  property_count: 3
  slug: microsoft-exchange-scoredemailaddress
- name: TimeConstraint
  property_count: 2
  slug: microsoft-exchange-timeconstraint
- name: TimeSlot
  property_count: 2
  slug: microsoft-exchange-timeslot
- name: Website
  property_count: 3
  slug: microsoft-exchange-website
- name: WorkingHours
  property_count: 4
  slug: microsoft-exchange-workinghours
json_structures:
- name: Microsoft Exchange Structure
  property_count: 0
  slug: microsoft-exchange-structure
jsonld:
- class_count: 0
  name: Microsoft Exchange Context
  property_count: 13
  slug: microsoft-exchange-context
layout: provider
mcp_servers:
- description: ''
  name: microsoft-exchange-mcp.yml
  slug: microsoft-exchange-mcpyml
modified: '2026-06-20'
name: Microsoft Exchange
nav: Providers
network: true
overview: 'Microsoft Exchange publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Accepted Domains API, Attachments API, Calendars API, and 14 more. Tagged areas include Calendar, Collaboration, Contacts, Email, and Enterprise.


  The Microsoft Exchange catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Exchange''s developer surface includes authentication, changelog, CLI, sandbox, developer portal, documentation, getting-started guide, and 54 more developer resources.'
plans:
- name: Microsoft Exchange Plans Pricing
  plan_count: 4
  slug: microsoft-exchange-plans-pricing
random_paper: 80
rate_limits:
- limit_count: 7
  name: Microsoft Exchange Rate Limits
  slug: microsoft-exchange-rate-limits
rules:
- name: Microsoft Exchange API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: microsoft-exchange-jsonschema-spectral-rules
scopes:
- name: Microsoft Exchange Scopes
  scope_count: 18
  slug: microsoft-exchange-scopes
  summary_line: 18 scopes · clientCredentials/authorizationCode
score:
  band: exemplar
  composite: 74.5
  delta: -2.1
  facets:
    commercial_clarity: 84.2
    contract_quality: 69.6
    developer_ergonomics: 71.7
    discoverability: 87.0
    governance: 69.8
    operational_transparency: 68.4
  previous_composite: 76.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
    mcp: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-exchange/refs/heads/main/screenshots/microsoft-exchange-2026-06-20T185501.png
security:
- kind: authentication
  name: Microsoft Exchange Authentication
  slug: microsoft-exchange-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Exchange Domain Security
  slug: microsoft-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Exchange Vulnerability Disclosure
  slug: microsoft-exchange-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-exchange
tags:
- Calendar
- Collaboration
- Contacts
- Email
- Enterprise
website: https://www.microsoft.com/en-us/microsoft-365/exchange/email
---
