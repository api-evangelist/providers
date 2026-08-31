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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Microsoft Office 365 Agentic Access
  operation_count: 31
  slug: microsoft-office-365-agentic-access
  summary_line: 31 operations · 17 acting
api_count: 1
apis:
- description: Access to Outlook personal contacts for managing contact information, creating contact folders, and organizing people data.
  name: Outlook Contacts API
  slug: outlook-contacts-api
- description: Access to OneNote notebooks, sections, and pages for creating and managing notes and structured content.
  name: OneNote API
  slug: onenote-api
- description: Read and modify Excel workbooks stored in OneDrive and SharePoint, including managing worksheets, tables, charts, ranges, and sessions.
  name: Excel Workbooks and Charts API
  slug: excel-workbooks-and-charts-api
- description: Manage tasks and task lists across To Do clients, Outlook, and Teams for personal task management and day planning.
  name: Microsoft To Do API
  slug: microsoft-to-do-api
- description: Manage customer bookings, appointment scheduling, business services, and staff information for enterprise and small business owners.
  name: Microsoft Bookings API
  slug: microsoft-bookings-api
- description: Connect security products, services, and partners to streamline security operations and improve threat protection, detection, and response.
  name: Microsoft Graph Security API
  slug: microsoft-graph-security-api
- description: Create and join online meetings, manage call records, and enable cloud communications capabilities for applications.
  name: Microsoft Graph Communications API
  slug: microsoft-graph-communications-api
- description: Platform for building solutions that extend Office applications including Excel, Outlook, Word, PowerPoint, and OneNote using web technologies and the Office JavaScript API.
  name: Office Add-ins Platform
  slug: office-add-ins-platform
- description: Access and manage Outlook calendar events, calendars, and calendar groups. Supports scheduling, meeting management, and free/busy lookups.
  name: Microsoft Office 365 Calendar API
  slug: microsoft-office-365-calendar-api
- description: Manage Microsoft 365 groups and security groups. Groups provide shared access to resources such as SharePoint sites, shared mailboxes, Planner plans, OneNote notebooks, and conversations.
  name: Microsoft Office 365 Groups API
  slug: microsoft-office-365-groups-api
- description: Access and manage Outlook mail messages, mail folders, and message attachments. Supports reading, creating, sending, replying, forwarding, and organizing email.
  name: Microsoft Office 365 Mail API
  slug: microsoft-office-365-mail-api
- description: Manage users in Azure Active Directory. Users are the core identity resource representing a person, including their profile, organizational relationships, and access to services.
  name: Microsoft Office 365 Users API
  slug: microsoft-office-365-users-api
arazzos:
- description: Create an event, read it back to confirm, then delete it from the calendar.
  name: Microsoft Office 365 Cancel Event
  slug: microsoft-office-365-cancel-event-workflow
- description: Create a draft, read it back, then delete it from the mailbox.
  name: Microsoft Office 365 Cleanup Draft Message
  slug: microsoft-office-365-cleanup-draft-message-workflow
- description: Create a Microsoft 365 group, add a member, then list members to confirm.
  name: Microsoft Office 365 Create Group With Members
  slug: microsoft-office-365-create-group-with-members-workflow
- description: Disable a user account, confirm the change, then delete the user.
  name: Microsoft Office 365 Deprovision User
  slug: microsoft-office-365-deprovision-user-workflow
- description: Create a draft message, read it back, then send it from the mailbox.
  name: Microsoft Office 365 Draft and Send Mail
  slug: microsoft-office-365-draft-and-send-mail-workflow
- description: Query a calendar view for a time window, then read the first event found.
  name: Microsoft Office 365 Find Event in Window
  slug: microsoft-office-365-find-event-in-window-workflow
- description: Look up a group by display name and create it only if it does not exist.
  name: Microsoft Office 365 Find or Create Group
  slug: microsoft-office-365-find-or-create-group-workflow
- description: Create a user, then send a welcome email to their new mailbox address.
  name: Microsoft Office 365 Notify New User
  slug: microsoft-office-365-notify-new-user-workflow
- description: Create a user, add them to an existing group, then confirm membership.
  name: Microsoft Office 365 Onboard User to Group
  slug: microsoft-office-365-onboard-user-to-group-workflow
- description: Create a new user, then read it back to confirm provisioning.
  name: Microsoft Office 365 Provision User
  slug: microsoft-office-365-provision-user-workflow
- description: Create an event, patch its start and end times, then read it back.
  name: Microsoft Office 365 Reschedule Event
  slug: microsoft-office-365-reschedule-event-workflow
- description: Read an event, then accept or decline it based on a desired response.
  name: Microsoft Office 365 Respond to Invitation
  slug: microsoft-office-365-respond-to-invitation-workflow
- description: Remove one member from a group, add another, then list members to confirm.
  name: Microsoft Office 365 Rotate Group Member
  slug: microsoft-office-365-rotate-group-member-workflow
- description: Create an event, then accept it on behalf of the signed-in user.
  name: Microsoft Office 365 Schedule and Accept Event
  slug: microsoft-office-365-schedule-and-accept-event-workflow
- description: Create a calendar event, then read it back to confirm the booking.
  name: Microsoft Office 365 Schedule Event
  slug: microsoft-office-365-schedule-event-workflow
- description: Read the latest inbox message, then mark it as read and categorize it.
  name: Microsoft Office 365 Triage Inbox Message
  slug: microsoft-office-365-triage-inbox-message-workflow
- description: Create a draft, patch its subject and body, then send the updated message.
  name: Microsoft Office 365 Update Draft and Send
  slug: microsoft-office-365-update-draft-and-send-workflow
- description: Patch a group's properties, then read it back to verify the change.
  name: Microsoft Office 365 Update Group and Verify
  slug: microsoft-office-365-update-group-and-verify-workflow
- description: Patch a user's profile properties, then read the user back to verify.
  name: Microsoft Office 365 Update User Profile
  slug: microsoft-office-365-update-user-profile-workflow
artifact_total: 261
collections:
- collection_type: postman
  name: Microsoft Office 365 Microsoft Graph API
  slug: postman-microsoft-graph-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Microsoft Office 365 Microsoft Graph API
  slug: open-microsoft-graph-api
- collection_type: open
  name: Microsoft Office 365 Microsoft Graph Calendar API
  slug: open-microsoft-office-365-calendar-api
- collection_type: open
  name: Microsoft Office 365 Microsoft Graph Calendar Groups API
  slug: open-microsoft-office-365-groups-api
- collection_type: open
  name: Microsoft Office 365 Microsoft Graph Calendar Mail API
  slug: open-microsoft-office-365-mail-api
- collection_type: open
  name: Microsoft Office 365 Microsoft Graph Calendar Users API
  slug: open-microsoft-office-365-users-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-office-365-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-office-365-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-office-365-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/microsoft-office-365-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/microsoft-office-365-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-office-365-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/microsoft-office-365/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-cancel-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-cleanup-draft-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-create-group-with-members-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-deprovision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-draft-and-send-mail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-find-event-in-window-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-find-or-create-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-notify-new-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-onboard-user-to-group-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-provision-user-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-reschedule-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-respond-to-invitation-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-rotate-group-member-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-schedule-and-accept-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-schedule-event-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-triage-inbox-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-update-draft-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-update-group-and-verify-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/microsoft-office-365-update-user-profile-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/microsoft-365
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.microsoft.com/en-us/microsoft-365
- group: operate
  title: ''
  type: StatusPage
  url: https://status.office365.com/
- group: operate
  title: ''
  type: Support
  url: https://developer.microsoft.com/en-us/graph/support
- group: company
  title: ''
  type: Blog
  url: https://developer.microsoft.com/en-us/graph/blogs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoftgraph
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: start
  title: Graph Explorer
  type: Console
  url: https://developer.microsoft.com/en-us/graph/graph-explorer
- group: build
  title: ''
  type: SDKs
  url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.microsoft.com/en-us/graph/changelog
- group: operate
  title: What's New
  type: ReleaseNotes
  url: https://learn.microsoft.com/en-us/graph/whats-new-overview
- group: auth
  title: ''
  type: Authentication
  url: https://learn.microsoft.com/en-us/graph/auth/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.microsoft.com/en-us/legal/microsoft-apis/terms-of-use
- group: operate
  title: ''
  type: RateLimits
  url: https://learn.microsoft.com/en-us/graph/throttling
- group: docs
  title: Webhooks
  type: Documentation
  url: https://learn.microsoft.com/en-us/graph/change-notifications-delivery-webhooks
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.microsoft.com/en-us/graph/quick-start
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/graph/api/overview?view=graph-rest-1.0
- group: auth
  title: ''
  type: Compliance
  url: https://learn.microsoft.com/en-us/graph/compliance-concept-overview
- group: design
  title: ''
  type: SpectralRules
  url: rules/microsoft-office-365-spectral-rules.yml
created: '2024-01-15'
description: A collection of APIs provided by Microsoft Office 365 for productivity, collaboration, and enterprise services.
examples:
- key_count: 2
  name: Microsoft Graph Assigned License Example
  slug: microsoft-graph-assigned-license-example
- key_count: 1
  name: Microsoft Graph Attendee Example
  slug: microsoft-graph-attendee-example
- key_count: 3
  name: Microsoft Graph Calendar Collection Response Example
  slug: microsoft-graph-calendar-collection-response-example
- key_count: 13
  name: Microsoft Graph Calendar Example
  slug: microsoft-graph-calendar-example
- key_count: 2
  name: Microsoft Graph Date Time Time Zone Example
  slug: microsoft-graph-date-time-time-zone-example
- key_count: 4
  name: Microsoft Graph Directory Object Collection Response Example
  slug: microsoft-graph-directory-object-collection-response-example
- key_count: 3
  name: Microsoft Graph Directory Object Example
  slug: microsoft-graph-directory-object-example
- key_count: 2
  name: Microsoft Graph Email Address Example
  slug: microsoft-graph-email-address-example
- key_count: 4
  name: Microsoft Graph Event Collection Response Example
  slug: microsoft-graph-event-collection-response-example
- key_count: 14
  name: Microsoft Graph Event Create Request Example
  slug: microsoft-graph-event-create-request-example
- key_count: 26
  name: Microsoft Graph Event Example
  slug: microsoft-graph-event-example
- key_count: 11
  name: Microsoft Graph Event Update Request Example
  slug: microsoft-graph-event-update-request-example
- key_count: 1
  name: Microsoft Graph Followup Flag Example
  slug: microsoft-graph-followup-flag-example
- key_count: 4
  name: Microsoft Graph Group Collection Response Example
  slug: microsoft-graph-group-collection-response-example
- key_count: 9
  name: Microsoft Graph Group Create Request Example
  slug: microsoft-graph-group-create-request-example
- key_count: 17
  name: Microsoft Graph Group Example
  slug: microsoft-graph-group-example
- key_count: 5
  name: Microsoft Graph Group Update Request Example
  slug: microsoft-graph-group-update-request-example
- key_count: 2
  name: Microsoft Graph Item Body Example
  slug: microsoft-graph-item-body-example
- key_count: 5
  name: Microsoft Graph Location Example
  slug: microsoft-graph-location-example
- key_count: 3
  name: Microsoft Graph Mail Folder Collection Response Example
  slug: microsoft-graph-mail-folder-collection-response-example
- key_count: 7
  name: Microsoft Graph Mail Folder Example
  slug: microsoft-graph-mail-folder-example
- key_count: 4
  name: Microsoft Graph Message Collection Response Example
  slug: microsoft-graph-message-collection-response-example
- key_count: 9
  name: Microsoft Graph Message Create Request Example
  slug: microsoft-graph-message-create-request-example
- key_count: 24
  name: Microsoft Graph Message Example
  slug: microsoft-graph-message-example
- key_count: 8
  name: Microsoft Graph Message Update Request Example
  slug: microsoft-graph-message-update-request-example
- key_count: 1
  name: Microsoft Graph O Data Error Example
  slug: microsoft-graph-o-data-error-example
- key_count: 3
  name: Microsoft Graph Object Identity Example
  slug: microsoft-graph-object-identity-example
- key_count: 6
  name: Microsoft Graph Online Meeting Info Example
  slug: microsoft-graph-online-meeting-info-example
- key_count: 5
  name: Microsoft Graph Outlook Geo Coordinates Example
  slug: microsoft-graph-outlook-geo-coordinates-example
- key_count: 3
  name: Microsoft Graph Password Profile Example
  slug: microsoft-graph-password-profile-example
- key_count: 0
  name: Microsoft Graph Patterned Recurrence Example
  slug: microsoft-graph-patterned-recurrence-example
- key_count: 5
  name: Microsoft Graph Physical Address Example
  slug: microsoft-graph-physical-address-example
- key_count: 0
  name: Microsoft Graph Recipient Example
  slug: microsoft-graph-recipient-example
- key_count: 7
  name: Microsoft Graph Recurrence Pattern Example
  slug: microsoft-graph-recurrence-pattern-example
- key_count: 5
  name: Microsoft Graph Recurrence Range Example
  slug: microsoft-graph-recurrence-range-example
- key_count: 2
  name: Microsoft Graph Response Status Example
  slug: microsoft-graph-response-status-example
- key_count: 0
  name: Microsoft Graph Time Slot Example
  slug: microsoft-graph-time-slot-example
- key_count: 4
  name: Microsoft Graph User Collection Response Example
  slug: microsoft-graph-user-collection-response-example
- key_count: 11
  name: Microsoft Graph User Create Request Example
  slug: microsoft-graph-user-create-request-example
- key_count: 25
  name: Microsoft Graph User Example
  slug: microsoft-graph-user-example
- key_count: 16
  name: Microsoft Graph User Update Request Example
  slug: microsoft-graph-user-update-request-example
- key_count: 6
  name: Microsoft Office 365 Acceptevent Example
  slug: microsoft-office-365-acceptevent-example
- key_count: 6
  name: Microsoft Office 365 Addgroupmember Example
  slug: microsoft-office-365-addgroupmember-example
- key_count: 6
  name: Microsoft Office 365 Createevent Example
  slug: microsoft-office-365-createevent-example
- key_count: 6
  name: Microsoft Office 365 Creategroup Example
  slug: microsoft-office-365-creategroup-example
- key_count: 6
  name: Microsoft Office 365 Createmessage Example
  slug: microsoft-office-365-createmessage-example
- key_count: 6
  name: Microsoft Office 365 Createuser Example
  slug: microsoft-office-365-createuser-example
- key_count: 6
  name: Microsoft Office 365 Declineevent Example
  slug: microsoft-office-365-declineevent-example
- key_count: 6
  name: Microsoft Office 365 Getcalendarview Example
  slug: microsoft-office-365-getcalendarview-example
- key_count: 6
  name: Microsoft Office 365 Getevent Example
  slug: microsoft-office-365-getevent-example
- key_count: 6
  name: Microsoft Office 365 Getgroup Example
  slug: microsoft-office-365-getgroup-example
- key_count: 6
  name: Microsoft Office 365 Getmessage Example
  slug: microsoft-office-365-getmessage-example
- key_count: 6
  name: Microsoft Office 365 Getsignedinuser Example
  slug: microsoft-office-365-getsignedinuser-example
- key_count: 6
  name: Microsoft Office 365 Getuser Example
  slug: microsoft-office-365-getuser-example
- key_count: 6
  name: Microsoft Office 365 Listcalendars Example
  slug: microsoft-office-365-listcalendars-example
- key_count: 6
  name: Microsoft Office 365 Listevents Example
  slug: microsoft-office-365-listevents-example
- key_count: 6
  name: Microsoft Office 365 Listgroupmembers Example
  slug: microsoft-office-365-listgroupmembers-example
- key_count: 6
  name: Microsoft Office 365 Listgroups Example
  slug: microsoft-office-365-listgroups-example
- key_count: 6
  name: Microsoft Office 365 Listmailfoldermessages Example
  slug: microsoft-office-365-listmailfoldermessages-example
- key_count: 6
  name: Microsoft Office 365 Listmailfolders Example
  slug: microsoft-office-365-listmailfolders-example
- key_count: 6
  name: Microsoft Office 365 Listmessages Example
  slug: microsoft-office-365-listmessages-example
- key_count: 6
  name: Microsoft Office 365 Listusers Example
  slug: microsoft-office-365-listusers-example
- key_count: 6
  name: Microsoft Office 365 Sendmail Example
  slug: microsoft-office-365-sendmail-example
- key_count: 6
  name: Microsoft Office 365 Updateevent Example
  slug: microsoft-office-365-updateevent-example
- key_count: 6
  name: Microsoft Office 365 Updategroup Example
  slug: microsoft-office-365-updategroup-example
- key_count: 6
  name: Microsoft Office 365 Updatemessage Example
  slug: microsoft-office-365-updatemessage-example
- key_count: 6
  name: Microsoft Office 365 Updateuser Example
  slug: microsoft-office-365-updateuser-example
features:
- description: Access Microsoft 365 data through a single REST endpoint at graph.microsoft.com covering mail, calendar, files, users, and groups.
  name: Unified API Endpoint
- description: Subscribe to change notifications via webhooks to receive real-time updates when data changes across Microsoft 365 services.
  name: Real-Time Notifications
- description: Combine multiple API requests into a single HTTP call to reduce network overhead and improve performance.
  name: Batch Requests
- description: Track incremental changes to resources efficiently using delta links without polling entire datasets.
  name: Delta Queries
- description: Read, send, reply, forward, and organize email messages with full attachment and folder support.
  name: Rich Mail Management
- description: Create events, manage calendars, check free/busy availability, and handle meeting responses programmatically.
  name: Calendar and Scheduling
- description: Access OneDrive and SharePoint files with upload, download, sharing, and real-time collaboration capabilities.
  name: File Storage and Sharing
- description: Manage Microsoft Teams channels, messages, tabs, and apps for team communication and collaboration.
  name: Team Collaboration
- description: Create, update, and manage users, groups, and organizational directory resources.
  name: User and Group Management
finops:
- name: Microsoft Office 365 Finops
  service_category: Productivity
  slug: microsoft-office-365-finops
image: https://www.microsoft.com/en-us/microsoft-365/blog/wp-content/uploads/sites/2/2020/04/Microsoft-365.png
integrations:
- description: Integrate with Azure AD for user authentication, authorization, and directory management.
  name: Azure Active Directory
- description: Build bots, tabs, and messaging extensions that integrate with Microsoft Teams collaboration platform.
  name: Microsoft Teams
- description: Connect Microsoft Graph data to Power Automate flows for no-code/low-code automation.
  name: Power Automate
- description: Feed Microsoft 365 data into Power BI dashboards for business intelligence and reporting.
  name: Power BI
- description: Access SharePoint sites, lists, and document libraries for enterprise content management.
  name: SharePoint
- description: Integrate with Outlook mail, calendar, and contacts for personal and shared mailbox management.
  name: Outlook
json_schemas:
- name: AssignedLicense
  property_count: 2
  slug: microsoft-graph-assigned-license
- name: Attendee
  property_count: 1
  slug: microsoft-graph-attendee
- name: CalendarCollectionResponse
  property_count: 3
  slug: microsoft-graph-calendar-collection-response
- name: Calendar
  property_count: 13
  slug: microsoft-graph-calendar
- name: DateTimeTimeZone
  property_count: 2
  slug: microsoft-graph-date-time-time-zone
- name: DirectoryObjectCollectionResponse
  property_count: 4
  slug: microsoft-graph-directory-object-collection-response
- name: DirectoryObject
  property_count: 3
  slug: microsoft-graph-directory-object
- name: EmailAddress
  property_count: 2
  slug: microsoft-graph-email-address
- name: EventCollectionResponse
  property_count: 4
  slug: microsoft-graph-event-collection-response
- name: EventCreateRequest
  property_count: 14
  slug: microsoft-graph-event-create-request
- name: Event
  property_count: 26
  slug: microsoft-graph-event
- name: EventUpdateRequest
  property_count: 11
  slug: microsoft-graph-event-update-request
- name: FollowupFlag
  property_count: 1
  slug: microsoft-graph-followup-flag
- name: GroupCollectionResponse
  property_count: 4
  slug: microsoft-graph-group-collection-response
- name: GroupCreateRequest
  property_count: 9
  slug: microsoft-graph-group-create-request
- name: Group
  property_count: 17
  slug: microsoft-graph-group
- name: GroupUpdateRequest
  property_count: 5
  slug: microsoft-graph-group-update-request
- name: ItemBody
  property_count: 2
  slug: microsoft-graph-item-body
- name: Location
  property_count: 5
  slug: microsoft-graph-location
- name: MailFolderCollectionResponse
  property_count: 3
  slug: microsoft-graph-mail-folder-collection-response
- name: MailFolder
  property_count: 7
  slug: microsoft-graph-mail-folder
- name: MessageCollectionResponse
  property_count: 4
  slug: microsoft-graph-message-collection-response
- name: MessageCreateRequest
  property_count: 9
  slug: microsoft-graph-message-create-request
- name: Message
  property_count: 24
  slug: microsoft-graph-message
- name: MessageUpdateRequest
  property_count: 8
  slug: microsoft-graph-message-update-request
- name: ODataError
  property_count: 1
  slug: microsoft-graph-o-data-error
- name: ObjectIdentity
  property_count: 3
  slug: microsoft-graph-object-identity
- name: OnlineMeetingInfo
  property_count: 6
  slug: microsoft-graph-online-meeting-info
- name: OutlookGeoCoordinates
  property_count: 5
  slug: microsoft-graph-outlook-geo-coordinates
- name: PasswordProfile
  property_count: 3
  slug: microsoft-graph-password-profile
- name: PatternedRecurrence
  property_count: 0
  slug: microsoft-graph-patterned-recurrence
- name: PhysicalAddress
  property_count: 5
  slug: microsoft-graph-physical-address
- name: Recipient
  property_count: 0
  slug: microsoft-graph-recipient
- name: RecurrencePattern
  property_count: 7
  slug: microsoft-graph-recurrence-pattern
- name: RecurrenceRange
  property_count: 5
  slug: microsoft-graph-recurrence-range
- name: ResponseStatus
  property_count: 2
  slug: microsoft-graph-response-status
- name: TimeSlot
  property_count: 0
  slug: microsoft-graph-time-slot
- name: UserCollectionResponse
  property_count: 4
  slug: microsoft-graph-user-collection-response
- name: UserCreateRequest
  property_count: 11
  slug: microsoft-graph-user-create-request
- name: User
  property_count: 25
  slug: microsoft-graph-user
- name: UserUpdateRequest
  property_count: 16
  slug: microsoft-graph-user-update-request
- name: AssignedLicense
  property_count: 2
  slug: microsoft-office-365-assignedlicense
- name: Attendee
  property_count: 4
  slug: microsoft-office-365-attendee
- name: Calendar
  property_count: 14
  slug: microsoft-office-365-calendar
- name: CalendarCollectionResponse
  property_count: 3
  slug: microsoft-office-365-calendarcollectionresponse
- name: DateTimeTimeZone
  property_count: 2
  slug: microsoft-office-365-datetimetimezone
- name: DirectoryObject
  property_count: 3
  slug: microsoft-office-365-directoryobject
- name: DirectoryObjectCollectionResponse
  property_count: 4
  slug: microsoft-office-365-directoryobjectcollectionresponse
- name: EmailAddress
  property_count: 2
  slug: microsoft-office-365-emailaddress
- name: Event
  property_count: 34
  slug: microsoft-office-365-event
- name: EventCollectionResponse
  property_count: 4
  slug: microsoft-office-365-eventcollectionresponse
- name: EventCreateRequest
  property_count: 19
  slug: microsoft-office-365-eventcreaterequest
- name: EventUpdateRequest
  property_count: 16
  slug: microsoft-office-365-eventupdaterequest
- name: FollowupFlag
  property_count: 4
  slug: microsoft-office-365-followupflag
- name: Group
  property_count: 17
  slug: microsoft-office-365-group
- name: GroupCollectionResponse
  property_count: 4
  slug: microsoft-office-365-groupcollectionresponse
- name: GroupCreateRequest
  property_count: 9
  slug: microsoft-office-365-groupcreaterequest
- name: GroupUpdateRequest
  property_count: 5
  slug: microsoft-office-365-groupupdaterequest
- name: ItemBody
  property_count: 2
  slug: microsoft-office-365-itembody
- name: Location
  property_count: 7
  slug: microsoft-office-365-location
- name: MailFolder
  property_count: 7
  slug: microsoft-office-365-mailfolder
- name: MailFolderCollectionResponse
  property_count: 3
  slug: microsoft-office-365-mailfoldercollectionresponse
- name: Message
  property_count: 28
  slug: microsoft-office-365-message
- name: MessageCollectionResponse
  property_count: 4
  slug: microsoft-office-365-messagecollectionresponse
- name: MessageCreateRequest
  property_count: 10
  slug: microsoft-office-365-messagecreaterequest
- name: MessageUpdateRequest
  property_count: 10
  slug: microsoft-office-365-messageupdaterequest
- name: ObjectIdentity
  property_count: 3
  slug: microsoft-office-365-objectidentity
- name: ODataError
  property_count: 1
  slug: microsoft-office-365-odataerror
- name: OnlineMeetingInfo
  property_count: 6
  slug: microsoft-office-365-onlinemeetinginfo
- name: OutlookGeoCoordinates
  property_count: 5
  slug: microsoft-office-365-outlookgeocoordinates
- name: PasswordProfile
  property_count: 3
  slug: microsoft-office-365-passwordprofile
- name: PatternedRecurrence
  property_count: 2
  slug: microsoft-office-365-patternedrecurrence
- name: PhysicalAddress
  property_count: 5
  slug: microsoft-office-365-physicaladdress
- name: Recipient
  property_count: 1
  slug: microsoft-office-365-recipient
- name: RecurrencePattern
  property_count: 7
  slug: microsoft-office-365-recurrencepattern
- name: RecurrenceRange
  property_count: 5
  slug: microsoft-office-365-recurrencerange
- name: ResponseStatus
  property_count: 2
  slug: microsoft-office-365-responsestatus
- name: TimeSlot
  property_count: 2
  slug: microsoft-office-365-timeslot
- name: Microsoft Office 365 User
  property_count: 64
  slug: microsoft-office-365-user
- name: UserCollectionResponse
  property_count: 4
  slug: microsoft-office-365-usercollectionresponse
- name: UserCreateRequest
  property_count: 12
  slug: microsoft-office-365-usercreaterequest
- name: UserUpdateRequest
  property_count: 17
  slug: microsoft-office-365-userupdaterequest
json_structures:
- name: Microsoft Graph Assigned License Structure
  property_count: 2
  slug: microsoft-graph-assigned-license-structure
- name: Microsoft Graph Attendee Structure
  property_count: 1
  slug: microsoft-graph-attendee-structure
- name: Microsoft Graph Calendar Collection Response Structure
  property_count: 3
  slug: microsoft-graph-calendar-collection-response-structure
- name: Microsoft Graph Calendar Structure
  property_count: 13
  slug: microsoft-graph-calendar-structure
- name: Microsoft Graph Date Time Time Zone Structure
  property_count: 2
  slug: microsoft-graph-date-time-time-zone-structure
- name: Microsoft Graph Directory Object Collection Response Structure
  property_count: 4
  slug: microsoft-graph-directory-object-collection-response-structure
- name: Microsoft Graph Directory Object Structure
  property_count: 3
  slug: microsoft-graph-directory-object-structure
- name: Microsoft Graph Email Address Structure
  property_count: 2
  slug: microsoft-graph-email-address-structure
- name: Microsoft Graph Event Collection Response Structure
  property_count: 4
  slug: microsoft-graph-event-collection-response-structure
- name: Microsoft Graph Event Create Request Structure
  property_count: 14
  slug: microsoft-graph-event-create-request-structure
- name: Microsoft Graph Event Structure
  property_count: 26
  slug: microsoft-graph-event-structure
- name: Microsoft Graph Event Update Request Structure
  property_count: 11
  slug: microsoft-graph-event-update-request-structure
- name: Microsoft Graph Followup Flag Structure
  property_count: 1
  slug: microsoft-graph-followup-flag-structure
- name: Microsoft Graph Group Collection Response Structure
  property_count: 4
  slug: microsoft-graph-group-collection-response-structure
- name: Microsoft Graph Group Create Request Structure
  property_count: 9
  slug: microsoft-graph-group-create-request-structure
- name: Microsoft Graph Group Structure
  property_count: 17
  slug: microsoft-graph-group-structure
- name: Microsoft Graph Group Update Request Structure
  property_count: 5
  slug: microsoft-graph-group-update-request-structure
- name: Microsoft Graph Item Body Structure
  property_count: 2
  slug: microsoft-graph-item-body-structure
- name: Microsoft Graph Location Structure
  property_count: 5
  slug: microsoft-graph-location-structure
- name: Microsoft Graph Mail Folder Collection Response Structure
  property_count: 3
  slug: microsoft-graph-mail-folder-collection-response-structure
- name: Microsoft Graph Mail Folder Structure
  property_count: 7
  slug: microsoft-graph-mail-folder-structure
- name: Microsoft Graph Message Collection Response Structure
  property_count: 4
  slug: microsoft-graph-message-collection-response-structure
- name: Microsoft Graph Message Create Request Structure
  property_count: 9
  slug: microsoft-graph-message-create-request-structure
- name: Microsoft Graph Message Structure
  property_count: 24
  slug: microsoft-graph-message-structure
- name: Microsoft Graph Message Update Request Structure
  property_count: 8
  slug: microsoft-graph-message-update-request-structure
- name: Microsoft Graph O Data Error Structure
  property_count: 1
  slug: microsoft-graph-o-data-error-structure
- name: Microsoft Graph Object Identity Structure
  property_count: 3
  slug: microsoft-graph-object-identity-structure
- name: Microsoft Graph Online Meeting Info Structure
  property_count: 6
  slug: microsoft-graph-online-meeting-info-structure
- name: Microsoft Graph Outlook Geo Coordinates Structure
  property_count: 5
  slug: microsoft-graph-outlook-geo-coordinates-structure
- name: Microsoft Graph Password Profile Structure
  property_count: 3
  slug: microsoft-graph-password-profile-structure
- name: Microsoft Graph Patterned Recurrence Structure
  property_count: 0
  slug: microsoft-graph-patterned-recurrence-structure
- name: Microsoft Graph Physical Address Structure
  property_count: 5
  slug: microsoft-graph-physical-address-structure
- name: Microsoft Graph Recipient Structure
  property_count: 0
  slug: microsoft-graph-recipient-structure
- name: Microsoft Graph Recurrence Pattern Structure
  property_count: 7
  slug: microsoft-graph-recurrence-pattern-structure
- name: Microsoft Graph Recurrence Range Structure
  property_count: 5
  slug: microsoft-graph-recurrence-range-structure
- name: Microsoft Graph Response Status Structure
  property_count: 2
  slug: microsoft-graph-response-status-structure
- name: Microsoft Graph Time Slot Structure
  property_count: 0
  slug: microsoft-graph-time-slot-structure
- name: Microsoft Graph User Collection Response Structure
  property_count: 4
  slug: microsoft-graph-user-collection-response-structure
- name: Microsoft Graph User Create Request Structure
  property_count: 11
  slug: microsoft-graph-user-create-request-structure
- name: Microsoft Graph User Structure
  property_count: 25
  slug: microsoft-graph-user-structure
- name: Microsoft Graph User Update Request Structure
  property_count: 16
  slug: microsoft-graph-user-update-request-structure
- name: Microsoft Office 365 Structure
  property_count: 0
  slug: microsoft-office-365-structure
jsonld:
- class_count: 0
  name: Microsoft Graph Context
  property_count: 0
  slug: microsoft-graph-context
- class_count: 0
  name: Microsoft Office 365 Context
  property_count: 10
  slug: microsoft-office-365-context
layout: provider
modified: '2026-05-19'
name: Microsoft Office 365
nav: Providers
network: true
overview: 'Microsoft Office 365 publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Calendar API, Groups API, Mail API, and 1 more. Tagged areas include Cloud, Collaboration, Enterprise, Microsoft, and Productivity.


  The Microsoft Office 365 catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Microsoft Office 365''s developer surface includes authentication, support, engineering blog, developer console, changelog, release notes, documentation, and 38 more developer resources.'
plans:
- name: Microsoft Office 365 Plans Pricing
  plan_count: 5
  slug: microsoft-office-365-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 8
  name: Microsoft Office 365 Rate Limits
  slug: microsoft-office-365-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Microsoft Office 365 API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: microsoft-office-365-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Microsoft Office 365 API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: microsoft-office-365-spectral-rules
scopes:
- name: Microsoft Office 365 Scopes
  scope_count: 18
  slug: microsoft-office-365-scopes
  summary_line: 18 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 56.4
  coverage:
    artifact_dirs: 20
    catalog_gap: 60.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 55.3
    commercial_clarity: 55.3
    contract_governance: 13.6
    contract_quality: 77.2
    developer_ergonomics: 76.2
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 26.3
  previous_composite: 57.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/microsoft-office-365/refs/heads/main/screenshots/microsoft-office-365-2026-06-20T185511.png
security:
- kind: authentication
  name: Microsoft Office 365 Authentication
  slug: microsoft-office-365-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Microsoft Office 365 Domain Security
  slug: microsoft-office-365-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Office 365 Vulnerability Disclosure
  slug: microsoft-office-365-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: microsoft-office-365
tags:
- Cloud
- Collaboration
- Enterprise
- Microsoft
- Productivity
use_cases:
- description: Build applications that integrate email, calendar, and file management into unified productivity workflows.
  name: Enterprise Productivity Integration
- description: Generate automated reports by pulling data from mail, calendar, and user profiles across the organization.
  name: Automated Reporting
- description: Manage user provisioning, group membership, and directory synchronization for enterprise identity workflows.
  name: Identity and Access Management
- description: Automate team notifications, channel management, and messaging workflows across Microsoft Teams.
  name: Team Communication Automation
- description: Enable multi-user document editing, sharing, and version tracking through OneDrive and SharePoint APIs.
  name: Document Collaboration
website: https://developer.microsoft.com/en-us/microsoft-365
---
