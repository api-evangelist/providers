---
access_model:
  confidence: high
  label: Freemium, self-service
  onboarding: unknown
  pricing: freemium
  public: true
  source:
  - https://www.zoho.com/crm/zohocrm-pricing.html
  - https://www.zoho.com/crm/signup.html
  - https://api-console.zoho.com/
  trial: true
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
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 44.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 247
  human_in_the_loop: 1
  name: Zoho Crm Agentic Access
  operation_count: 405
  slug: zoho-crm-agentic-access
  summary_line: 405 operations · 247 acting · 1 human-in-the-loop
api_count: 105
apis:
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Actions API from Zoho CRM — 36 operation(s) for actions.
  name: Zoho CRM Actions API
  phrasing_intents:
  - id: associateEmail
    intent: Associate emails with a CRM record
    question: How do I link an existing email to a specific contact or lead record?
  - id: postUnenrolFromCadences
    intent: Unenroll records from cadences
    question: How do I take leads out of a follow-up cadence they were enrolled in?
  - id: postEnrolInCadences
    intent: Enroll records into a manual cadence
    question: How do I enroll a batch of leads into a manual cadence in Zoho CRM?
  - id: singleUpdate
    intent: Change the owner of one record
    question: How do I reassign a single deal to a different sales rep?
  - id: bulkChangeOwner
    intent: Change the owner of several chosen records
    question: How do I reassign a hand-picked list of leads to one new owner in a single call?
  - id: fetchFullDataForMultipleRecords
    intent: Fetch full rich text for several records
    question: How do I get the complete, untruncated rich text fields for a batch of records?
  - id: fetchFullDataForSingleRecord
    intent: Fetch full rich text for one record
    question: How can I read the whole content of a long rich text field on one record?
  - id: getMergeJobStatus
    intent: Check the status of a record merge job
    question: How do I find out whether an asynchronous merge of duplicate records has finished?
  phrasing_ops: 48
  slug: zoho-crm-actions-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Appointments S API from Zoho CRM — 2 operation(s) for appointments s.
  name: Zoho CRM Appointments S API
  phrasing_intents:
  - id: getAppointmentsS
    intent: List appointments
    question: How do I list all appointment records in Zoho CRM?
  - id: putAppointmentsS
    intent: Update several appointments at once
    question: Can I reschedule or edit multiple appointments in a single request?
  - id: postAppointmentsS
    intent: Book new appointments
    question: What's the way to book a new appointment record?
  - id: deleteAppointmentsS
    intent: Delete several appointments
    question: Can I delete multiple appointments by passing a list of IDs?
  - id: getAppointmentById
    intent: Get one appointment
    question: Where do I look up the details of a single appointment by its ID?
  - id: updateAppointmentById
    intent: Update a single appointment
    question: Can I edit just one appointment using its ID?
  - id: deleteId
    intent: Delete a single appointment
    question: How do I delete one appointment record?
  phrasing_ops: 7
  slug: zoho-crm-appointments-s-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Attachments API from Zoho CRM — 2 operation(s) for attachments.
  name: Zoho CRM Attachments API
  phrasing_intents:
  - id: getAttachmentById
    intent: Download a record's attachment file
    question: How do I download the actual file attached to a CRM record?
  - id: deleteAttachment
    intent: Delete a link attachment from a record
    question: Can I remove a link attachment from a record?
  - id: getAttachments
    intent: List a record's attachments
    question: What files and links are attached to a particular record?
  - id: uploadAttachment
    intent: Attach a file or URL to a record
    question: How do I attach a file to a contact or deal in Zoho CRM?
  phrasing_ops: 4
  slug: zoho-crm-attachments-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Composite Requests API from Zoho CRM — 1 operation(s) for composite requests.
  name: Zoho CRM Composite Requests API
  phrasing_intents:
  - id: composite
    intent: Run multiple API requests in one call
    question: How do I bundle several CRM API calls into a single HTTP request?
  phrasing_ops: 1
  slug: zoho-crm-composite-requests-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Contact Roles API from Zoho CRM — 2 operation(s) for contact roles.
  name: Zoho CRM Contact Roles API
  phrasing_intents:
  - id: getAssociatedContactRoles
    intent: List contacts and their roles on a deal
    question: Which contacts are involved in a deal and what role does each play?
  - id: upsertContactRoleRelations
    intent: Add or update contact roles on a deal in bulk
    question: Can I add several contacts to a deal with their roles in one request?
  - id: deleteContactRoleRelations
    intent: Remove several contacts from a deal
    question: Can I remove multiple contact role associations from a deal at once?
  - id: getDealContactRoleForContact
    intent: Get one contact's role on a deal
    question: What role does a particular contact hold on a specific deal?
  - id: associateContactRoleToDeal
    intent: Assign a role to one contact on a deal
    question: How do I add a single contact to a deal as the decision maker?
  - id: deleteContactRoleRelation
    intent: Remove one contact from a deal
    question: How do I take one contact off a deal?
  phrasing_ops: 6
  slug: zoho-crm-contact-roles-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Contacts API from Zoho CRM — 4 operation(s) for contacts.
  name: Zoho CRM Contacts API
  phrasing_intents:
  - id: getContactRoles
    intent: List contact roles
    question: What contact roles are defined in my CRM, like Decision Maker or Evaluator?
  - id: createRoles
    intent: Create new contact roles
    question: How do I add a new contact role such as Technical Buyer?
  - id: updateRoles
    intent: Update several contact roles
    question: Can I rename or reorder multiple contact roles at once?
  - id: deleteRoles
    intent: Delete several contact roles
    question: Can I delete multiple contact role definitions by their IDs?
  - id: getRole
    intent: Get a contact role by ID
    question: Where do I look up one contact role definition by its ID?
  - id: updateRole
    intent: Update a single contact role
    question: Can I rename just one contact role by its ID?
  - id: deleteRole
    intent: Delete a single contact role
    question: How do I delete one contact role definition?
  - id: linkEmailsToDeals
    intent: Link a contact's emails to deals
    question: Can I link several emails from a contact to the related deals in the CRM?
  phrasing_ops: 11
  slug: zoho-crm-contacts-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Coql API from Zoho CRM — 1 operation(s) for coql.
  name: Zoho CRM Coql API
  phrasing_intents:
  - id: executeCOQLQuery
    intent: Query records with a COQL select
    question: Can I fetch CRM records with a SQL-like select query?
  phrasing_ops: 1
  slug: zoho-crm-coql-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Deleted API from Zoho CRM — 2 operation(s) for deleted.
  name: Zoho CRM Deleted API
  phrasing_intents:
  - id: getDeletedRecords
    intent: List deleted records in a module
    question: How do I see which records were deleted from a module?
  - id: getDeletedRelatedRecord
    intent: List deleted records once related to a record
    question: Which records that were linked to this account have since been deleted?
  phrasing_ops: 2
  slug: zoho-crm-deleted-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Email Drafts API from Zoho CRM — 2 operation(s) for email drafts.
  name: Zoho CRM Email Drafts API
  phrasing_intents:
  - id: getEmailDrafts
    intent: List email drafts on a record
    question: What email drafts are saved against a given contact?
  - id: createEmailDrafts
    intent: Save an email draft on a record
    question: How do I save an unsent email as a draft on a lead?
  - id: getEmailDraft
    intent: Get one email draft
    question: How do I open a specific saved email draft?
  - id: updateEmailDrafts
    intent: Edit an email draft
    question: How do I change the subject or body of a saved email draft?
  - id: deleteEmailDrafts
    intent: Delete an email draft
    question: How do I discard a saved email draft?
  phrasing_ops: 5
  slug: zoho-crm-email-drafts-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Emails API from Zoho CRM — 2 operation(s) for emails.
  name: Zoho CRM Emails API
  phrasing_intents:
  - id: downloadEmailAttachments
    intent: Download an email attachment on a record
    question: How do I download a file attached to an email linked to a CRM record?
  - id: getDownloadInlineImages
    intent: Download inline images from a record's email
    question: Can I download the images embedded in the body of an email on a record?
  phrasing_ops: 2
  slug: zoho-crm-emails-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Emails Sharing Details API from Zoho CRM — 1 operation(s) for emails sharing details.
  name: Zoho CRM Emails Sharing Details API
  phrasing_intents:
  - id: getEmailSharingDetail
    intent: See who a record's emails can be shared with
    question: Which users can I share a contact's emails with?
  phrasing_ops: 1
  slug: zoho-crm-emails-sharing-details-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Events API from Zoho CRM — 1 operation(s) for events.
  name: Zoho CRM Events API
  phrasing_intents:
  - id: cancelMeetings
    intent: Cancel a meeting
    question: How do I cancel a scheduled meeting in the CRM?
  phrasing_ops: 1
  slug: zoho-crm-events-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Features API from Zoho CRM — 2 operation(s) for features.
  name: Zoho CRM Features API
  phrasing_intents:
  - id: getFeatureDetails
    intent: List features available in my edition
    question: Which features and limits does my Zoho CRM edition include?
  - id: getFeatureSepcificDetails
    intent: Get details of one feature
    question: What are the limits of a specific feature in my edition?
  phrasing_ops: 2
  slug: zoho-crm-features-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Files API from Zoho CRM — 1 operation(s) for files.
  name: Zoho CRM Files API
  phrasing_intents:
  - id: uploadFiles
    intent: Upload files to Zoho File System
    question: Can I upload up to ten files in one request and get back their file IDs?
  - id: getFile
    intent: Download a file from Zoho File System
    question: How do I download a file I previously uploaded to the Zoho File System?
  phrasing_ops: 2
  slug: zoho-crm-files-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Global Picklists API from Zoho CRM — 3 operation(s) for global picklists.
  name: Zoho CRM Global Picklists API
  phrasing_intents:
  - id: replacePicklistValues
    intent: Replace values in a global picklist
    question: How do I swap an old global picklist value for a new one across records?
  - id: getReplacedValues
    intent: See pending global picklist replacements
    question: Which global picklist values are still queued for replacement?
  - id: getGlobalPickListFieldAssociations
    intent: List fields using a global picklist
    question: Which modules, fields and layouts use a given global picklist?
  phrasing_ops: 3
  slug: zoho-crm-global-picklists-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: Operations for managing holidays that affect business hours and shift schedules
  name: Zoho CRM Holidays API
  phrasing_intents:
  - id: getHolidays
    intent: List holidays
    question: Which company holidays are configured for this year?
  - id: createHolidays
    intent: Create holidays
    question: How do I add company holidays to the CRM calendar?
  - id: updateHolidays
    intent: Update several holidays at once
    question: How do I rename or reschedule multiple holidays in one request?
  - id: updateHoliday
    intent: Update one holiday
    question: How do I rename a single holiday or move its date?
  - id: getHoliday
    intent: Get one holiday
    question: How do I see details of one holiday, like its date and shift?
  - id: deleteHoliday
    intent: Delete a holiday
    question: How do I remove a holiday from the calendar?
  phrasing_ops: 6
  slug: zoho-crm-holidays-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Layouts API from Zoho CRM — 1 operation(s) for layouts.
  name: Zoho CRM Layouts API
  phrasing_intents:
  - id: updateLayout
    intent: Update a custom layout
    question: How do I rename a layout or add fields to one of its sections?
  phrasing_ops: 1
  slug: zoho-crm-layouts-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Leads API from Zoho CRM — 3 operation(s) for leads.
  name: Zoho CRM Leads API
  phrasing_intents:
  - id: getLeadConversionOptions
    intent: See conversion options for a lead
    question: Before converting a lead, how do I see which existing contacts or accounts it matches?
  - id: convertLead
    intent: Convert a lead
    question: How do I convert a qualified lead into a contact, account and deal?
  - id: massConvert
    intent: Convert many leads in one job
    question: How do I convert up to 50 leads at once?
  - id: getJobStatus
    intent: Check a mass lead conversion job
    question: How do I find out whether a mass lead conversion finished?
  phrasing_ops: 4
  slug: zoho-crm-leads-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Locking Information S API from Zoho CRM — 2 operation(s) for locking information s.
  name: Zoho CRM Locking Information S API
  phrasing_intents:
  - id: getRecordLockingInformationOfTheRecord
    intent: Get a record's lock details
    question: Is this record locked, and who locked it and why?
  - id: lockRecord
    intent: Lock a record
    question: How do I lock a record so others can't edit it?
  - id: updateReasonofLockedRecord
    intent: Change the reason on a record lock
    question: Can I change the locking reason on a record that's already locked?
  - id: removeLockFromLockedRecord
    intent: Unlock a locked record
    question: How do I unlock a record so it can be edited again?
  phrasing_ops: 4
  slug: zoho-crm-locking-information-s-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Notes API from Zoho CRM — 4 operation(s) for notes.
  name: Zoho CRM Notes API
  phrasing_intents:
  - id: getNotesModule
    intent: List notes across the CRM
    question: How do I pull every note in the CRM regardless of which record it's attached to?
  - id: createNotesModule
    intent: Create notes in the Notes module
    question: Can I create several notes in one request directly in the Notes module?
  - id: updateNotesModule
    intent: Update multiple notes in bulk
    question: Can I edit the titles or content of many notes at once without going through their records?
  - id: deleteNotesModule
    intent: Delete several notes by ID
    question: How do I permanently delete a batch of notes using a comma-separated list of IDs?
  - id: getNoteById
    intent: Get a note by its ID
    question: Where can I read one note when I only know the note ID?
  - id: updateNoteById
    intent: Update a note by its ID
    question: Can I edit a note's title or content knowing only its note ID?
  - id: deleteNoteById
    intent: Delete a note by its ID
    question: How do I permanently delete one note using just its note ID?
  - id: getNotes
    intent: List notes on a specific record
    question: What notes have been added to a particular deal or contact?
  phrasing_ops: 14
  slug: zoho-crm-notes-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Org API from Zoho CRM — 5 operation(s) for org.
  name: Zoho CRM Org API
  phrasing_intents:
  - id: getCurrencies
    intent: List the organization's currencies
    question: Which currencies have been added to my Zoho CRM organization?
  - id: createCurrencies
    intent: Add new currencies to the organization
    question: How do I add a new currency like EUR to the organization?
  - id: updateCurrencies
    intent: Update several non-base currencies
    question: Can I update exchange rates for several currencies in one go?
  - id: getCurrencyById
    intent: Get one currency's details
    question: Where can I see the settings and rate of one specific currency?
  - id: updateCurrencyById
    intent: Update a single currency
    question: Can I change the exchange rate of just one currency by its ID?
  - id: enableCurrency
    intent: Enable multi-currency and set base currency
    question: How do I turn on multi-currency support for the organization?
  - id: updateBaseCurrency
    intent: Update the base currency
    question: Can I edit the details of our existing base currency?
  - id: getOrganization
    intent: Get the organization's company details
    question: What company details does the CRM hold for my organization?
  phrasing_ops: 11
  slug: zoho-crm-org-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Photo API from Zoho CRM — 1 operation(s) for photo.
  name: Zoho CRM Photo API
  phrasing_intents:
  - id: getPhoto
    intent: Get a record's photo
    question: How do I download the profile photo on a contact?
  - id: uploadPhoto
    intent: Upload a record's photo
    question: How do I set a profile picture on a contact?
  - id: deletePhoto
    intent: Remove a record's photo
    question: How do I remove a contact's profile photo?
  phrasing_ops: 3
  slug: zoho-crm-photo-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Read API from Zoho CRM — 3 operation(s) for read.
  name: Zoho CRM Read API
  phrasing_intents:
  - id: createBulkReadJob
    intent: Start a bulk export job
    question: How do I export a large number of CRM records in one background job?
  - id: getBulkReadJobDetails
    intent: Check a bulk export job's status
    question: Has my bulk read job finished yet?
  - id: downloadResult
    intent: Download a bulk export's result file
    question: Where do I download the exported file from a completed bulk read?
  phrasing_ops: 3
  slug: zoho-crm-read-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Records API from Zoho CRM — 3 operation(s) for records.
  name: Zoho CRM Records API
  phrasing_intents:
  - id: getCount
    intent: Count records in a module
    question: How many leads do I have in Zoho CRM right now?
  - id: getRecords
    intent: List records in a module
    question: How do I pull a list of all deals with just a few fields?
  - id: createRecords
    intent: Create records in a module
    question: How do I add a new lead to Zoho CRM from my web form?
  - id: updateRecords
    intent: Update several records in one request
    question: How do I update a batch of existing records in one API call?
  - id: deleteRecords
    intent: Delete several records at once
    question: How do I permanently delete a handful of records by their IDs?
  - id: getRecord
    intent: Get one record by ID
    question: How do I look up all the details of one specific contact?
  - id: updateRecord
    intent: Update one record by ID
    question: How do I change fields on one specific lead?
  - id: deleteRecord
    intent: Delete one record by ID
    question: How do I delete a single contact record?
  phrasing_ops: 8
  slug: zoho-crm-records-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Search API from Zoho CRM — 1 operation(s) for search.
  name: Zoho CRM Search API
  phrasing_intents:
  - id: searchRecords
    intent: Search records in a module
    question: How do I find leads by email address or phone number?
  phrasing_ops: 1
  slug: zoho-crm-search-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Services S API from Zoho CRM — 2 operation(s) for services s.
  name: Zoho CRM Services S API
  phrasing_intents:
  - id: getServicesS
    intent: List service records
    question: What services do we have set up in the Services module?
  - id: putServicesS
    intent: Update several service records
    question: How do I update multiple services in one call?
  - id: postServicesS
    intent: Create service records
    question: How do I add a new service to the Services module?
  - id: deleteServicesS
    intent: Delete several service records
    question: How do I delete multiple services at once?
  - id: getServiceById
    intent: Get one service record
    question: How do I see the details of one service?
  - id: putServiceById
    intent: Update one service record
    question: How do I edit a single service's details?
  - id: deleteServiceById
    intent: Delete one service record
    question: How do I delete a single service?
  phrasing_ops: 7
  slug: zoho-crm-services-s-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Settings API from Zoho CRM — 107 operation(s) for settings.
  name: Zoho CRM Settings API
  phrasing_intents:
  - id: getAppointmentPreference
    intent: Get appointment preferences
    question: What are my current appointment preferences for deal creation and job sheets?
  - id: updateAppointmentPreference
    intent: Update appointment preferences
    question: Can I change how appointments create deals when they are marked complete?
  - id: getAssignmentRules
    intent: List assignment rules
    question: Which assignment rules are set up to route new records to owners?
  - id: getAssignmentRuleById
    intent: Get an assignment rule
    question: What criteria and owners does a specific assignment rule use?
  - id: createAuditLogExport
    intent: Start an audit log export
    question: Can I export the audit log for a date range to review admin changes?
  - id: getAuditLogExports
    intent: List audit log export jobs
    question: What audit log exports have been run and are any still in progress?
  - id: getAuditLogExportsById
    intent: Get an audit log export job
    question: Is a particular audit log export finished yet?
  - id: createBusinessHours
    intent: Set up business hours
    question: How do I define business hours for an organization that has none configured yet?
  phrasing_ops: 213
  slug: zoho-crm-settings-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Timeline API from Zoho CRM — 1 operation(s) for timeline.
  name: Zoho CRM Timeline API
  phrasing_intents:
  - id: getTimelines
    intent: Get a record's activity timeline
    question: How do I see the history of everything that happened on a deal?
  phrasing_ops: 1
  slug: zoho-crm-timeline-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Upload API from Zoho CRM — 1 operation(s) for upload.
  name: Zoho CRM Upload API
  phrasing_intents:
  - id: uploadFile
    intent: Upload a file for a bulk write job
    question: How do I upload a data file before starting a bulk write import?
  phrasing_ops: 1
  slug: zoho-crm-upload-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Upsert API from Zoho CRM — 1 operation(s) for upsert.
  name: Zoho CRM Upsert API
  phrasing_intents:
  - id: upsertRecords
    intent: Insert or update records by duplicate check
    question: How do I create a record only if it doesn't already exist, otherwise update it?
  phrasing_ops: 1
  slug: zoho-crm-upsert-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Users API from Zoho CRM — 10 operation(s) for users.
  name: Zoho CRM Users API
  phrasing_intents:
  - id: getAssociatedGroupsForUser
    intent: List the user groups a user belongs to
    question: Which user groups is a particular CRM user a member of?
  - id: getUsers
    intent: List users in the organization
    question: How do I get a list of every user in my Zoho CRM organization?
  - id: createUser
    intent: Add a new user to the organization
    question: How do I add a new teammate as a user in the CRM?
  - id: updateUser
    intent: Update several users at once
    question: Can I update the details of multiple CRM users in a single request?
  - id: getSingleUser
    intent: Get one user's details
    question: Where can I look up the profile, role and status of one specific user by ID?
  - id: updateSingleUser
    intent: Update a single user by ID
    question: Can I change one user's role or profile using their user ID?
  - id: deleteUser
    intent: Delete a user
    question: How do I remove a user from the CRM organization for good?
  - id: getTerritoriesOfUser
    intent: List territories assigned to a user
    question: Which sales territories are assigned to a given user?
  phrasing_ops: 18
  slug: zoho-crm-users-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Workflow Configurations API from Zoho CRM — 1 operation(s) for workflow configurations.
  name: Zoho CRM Workflow Configurations API
  phrasing_intents:
  - id: getWorkflowConfigurations
    intent: Get workflow triggers and actions for a module
    question: Which workflow triggers and actions are available for a module?
  phrasing_ops: 1
  slug: zoho-crm-workflow-configurations-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Write API from Zoho CRM — 2 operation(s) for write.
  name: Zoho CRM Write API
  phrasing_intents:
  - id: createBulkWriteJob
    intent: Start a bulk import job
    question: How do I import thousands of records from a CSV in one job?
  - id: getJobDetails
    intent: Check a bulk write job
    question: How do I check the progress of a bulk write job?
  phrasing_ops: 2
  slug: zoho-crm-write-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Zia Org Enrichment API from Zoho CRM — 2 operation(s) for zia org enrichment.
  name: Zoho CRM Zia Org Enrichment API
  phrasing_intents:
  - id: submitOrgEnrichmentRequest
    intent: Enrich a record's company data with Zia
    question: How do I have Zia fill in company details for an account from its website?
  - id: getZiaOrgEnrichment
    intent: List Zia organization enrichment jobs
    question: Which organization enrichment requests has Zia processed?
  - id: getOrgEnrichmentById
    intent: Get the result of an organization enrichment
    question: How do I see the enriched company data from one enrichment job?
  phrasing_ops: 3
  slug: zoho-crm-zia-org-enrichment-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Zoho CRM Related Records API API from Zoho CRM — 2 operation(s) for zoho crm related records api.
  name: Zoho CRM Zoho CRM Related Records API
  phrasing_intents:
  - id: getRelatedRecords
    intent: List records in a record's related list
    question: How do I see all the records in a related list, such as the contacts under an account?
  - id: updateRelatedRecords
    intent: Update several related records
    question: Can I update properties on multiple records in one related list at once?
  - id: delinkRelatedRecords
    intent: Unlink several related records
    question: Can I unlink multiple records from a parent without deleting the records themselves?
  - id: getRelatedRecord
    intent: Get one specific related record
    question: Where can I read a single record through its parent's related list?
  - id: updateSpecificRelatedRecord
    intent: Update one specific related record
    question: Can I edit the relation details for just one related record?
  - id: delinkSpecificRelatedRecord
    intent: Unlink one related record
    question: How do I unlink a single record from its parent without deleting it?
  phrasing_ops: 6
  slug: zoho-crm-zoho-crm-related-records-api-api
- baseURL: https://www.zohoapis.com/crm/v8
  baseurl_source: declared
  description: The Apis API from Zoho CRM — 1 operation(s) for apis.
  name: Zoho CRM APIS API
  phrasing_intents:
  - id: getAvailableApis
    intent: List REST APIs available to the user
    question: Which Zoho CRM REST endpoints can my user access in this account?
  phrasing_ops: 1
  slug: zoho-crm-apis-api
artifact_total: 104
asyncapis:
- description: AsyncAPI 2.6 specification for the Zoho CRM Notifications (Instant Notifications) API surface. Subscribers register a notify_url (channel) with Zoho CRM via the REST "actions/watch" endpoint and recei
  name: Zoho CRM Notifications API
  slug: zoho-crm-notifications-asyncapi
common:
- group: design
  href: https://artifacts.apis.io/zoho-crm/conventions/zoho-crm-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/zoho-crm-conventions.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/rules/zoho-crm-rules.yml
  title: ''
  type: Spectral
  url: rules/zoho-crm-rules.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/rules/zoho-crm-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/zoho-crm-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/json-ld/zoho-crm-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/zoho-crm-context.jsonld
- group: design
  href: https://artifacts.apis.io/zoho-crm/vocabulary/zoho-crm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zoho-crm-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/zoho-crm/lifecycle/zoho-crm-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/zoho-crm-lifecycle.yml
- group: other
  href: https://artifacts.apis.io/zoho-crm/hosts/zoho-crm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zoho-crm-hosts.yml
- group: build
  href: https://artifacts.apis.io/zoho-crm/integrations/zoho-crm-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/zoho-crm-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/zoho-crm/vendors/zoho-crm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zoho-crm-vendors.yml
- group: other
  href: https://artifacts.apis.io/zoho-crm/capabilities/zoho-crm-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/zoho-crm-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-apis-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-appointment-preference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-appointment-preference-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-appointments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-appointments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-assignment-rules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-assignment-rules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-associate-email-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-associate-email-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-attachments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-attachments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-audit-log-export-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-audit-log-export-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-available-currencies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-available-currencies-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-bulk-read-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-bulk-read-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-bulk-write-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-bulk-write-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-business-hours-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-business-hours-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-cadences-execution-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-cadences-execution-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-cadences-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-cadences-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-call-preferences-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-call-preferences-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-cancel-meetings-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-cancel-meetings-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-change-owner-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-change-owner-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-composite-requests-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-composite-requests-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-contact-roles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-contact-roles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-conversion-option-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-conversion-option-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-convert-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-convert-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-coql-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-coql-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-currencies-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-currencies-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-custom-views-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-custom-views-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-data-sharing-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-data-sharing-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-deal-contact-roles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-deal-contact-roles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-deal-link-emails-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-deal-link-emails-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-download-attachments-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-download-attachments-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-download-inline-images-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-download-inline-images-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-duplicate-check-preference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-duplicate-check-preference-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-email-drafts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-email-drafts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-email-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-email-templates-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-emails-sharing-details-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-emails-sharing-details-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-features-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-features-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-fetch-full-data-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-fetch-full-data-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-field-updates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-field-updates-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-fields-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-fields-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-files-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-files-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-find-and-merge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-find-and-merge-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-fiscal-year-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-fiscal-year-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-from-addresses-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-from-addresses-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-get-related-records-count-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-get-related-records-count-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-global-picklists-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-global-picklists-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-holidays-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-holidays-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-inventory-convert-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-inventory-convert-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-inventory-templates-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-inventory-templates-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-layouts-activate-deactivate-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-layouts-activate-deactivate-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-layouts-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-layouts-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-locking-informations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-locking-informations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mail-merge-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mail-merge-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-map-dependency-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-map-dependency-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mass-change-owner-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mass-change-owner-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mass-convert-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mass-convert-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mass-delete-cvid-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mass-delete-cvid-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mass-delete-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mass-delete-tags-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-mass-update-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-mass-update-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-module-search-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-module-search-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-modules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-modules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-notes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-notes-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-notifications-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-notifications-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-org-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-org-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-org-photo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-org-photo-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-ownership-history-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-ownership-history-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-pick-list-values-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-pick-list-values-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-pipeline-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-pipeline-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-portal-user-type-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-portal-user-type-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-portal-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-portal-users-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-portals-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-portals-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-profiles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-profiles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-record-count-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-record-count-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-record-locking-configurations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-record-locking-configurations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-record-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-record-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-record-photo-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-record-photo-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-record-share-email-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-record-share-email-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-recycle-bin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-recycle-bin-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-related-lists-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-related-lists-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-related-notes-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-related-notes-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-related-records-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-related-records-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-roles-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-roles-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-scoring-rules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-scoring-rules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-send-mail-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-send-mail-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-service-preference-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-service-preference-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-services-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-share-records-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-share-records-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-shift-hours-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-shift-hours-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-tags-actions-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-tags-actions-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-tags-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-territories-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-territories-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-territory-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-territory-users-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-timelines-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-timelines-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-unblock-email-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-unblock-email-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-unsubscribe-links-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-unsubscribe-links-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-upload-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-upload-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-user-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-user-groups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-users-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-users-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-users-territories-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-users-territories-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-users-transfer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-users-transfer-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-variable-groups-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-variable-groups-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-variables-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-variables-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-webhooks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-webhooks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-wizards-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-wizards-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-workflow-configurations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-workflow-configurations-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-workflow-rules-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-workflow-rules-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-workflow-tasks-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-workflow-tasks-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-zia-enrichment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-zia-enrichment-overlay.yaml
- group: other
  href: https://artifacts.apis.io/zoho-crm/overlays/zoho-crm-zia-org-enrichment-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/zoho-crm-zia-org-enrichment-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/crm/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/crm/developer/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/crm/developer/docs/api/v8/
- group: docs
  title: ''
  type: APIReference
  url: https://www.zoho.com/crm/developer/docs/api/v8/list-available-rest-apis.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.zoho.com/crm/developer/docs/api/v8/oauth-overview.html
- group: operate
  title: ''
  type: Support
  url: https://help.zoho.com/portal/en/community/zoho-crm
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/crm/blog/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/zoho/crm-oas
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohocrm
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/crm/zohocrm-pricing.html
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/crm/signup.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/zohocrmdevelopers/zoho-crm-developers/overview
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/zohocrmdevelopers/zoho-crm-developers/overview
- group: start
  title: ''
  type: Console
  url: https://api-console.zoho.com/
- group: auth
  href: https://artifacts.apis.io/zoho-crm/authentication/zoho-crm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zoho-crm-authentication.yml
- group: auth
  href: https://artifacts.apis.io/zoho-crm/scopes/zoho-crm-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/zoho-crm-scopes.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/conventions/zoho-crm-conventions.yml
  title: ''
  type: Conventions
  url: conventions/zoho-crm-conventions.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/errors/zoho-crm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zoho-crm-problem-types.yml
- group: operate
  href: https://artifacts.apis.io/zoho-crm/rate-limits/zoho-crm-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/zoho-crm-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/zoho-crm/plans/zoho-crm-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/zoho-crm-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/lifecycle/zoho-crm-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/zoho-crm-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.zoho.com/
- group: operate
  href: https://artifacts.apis.io/zoho-crm/changelog/zoho-crm-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/zoho-crm-changelog.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/data-model/zoho-crm-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zoho-crm-data-model.yml
- group: build
  href: https://artifacts.apis.io/zoho-crm/packages/zoho-crm-packages.yml
  title: ''
  type: Packages
  url: packages/zoho-crm-packages.yml
- group: build
  href: https://artifacts.apis.io/zoho-crm/packages/zoho-crm-packages.yml
  title: ''
  type: SDKs
  url: packages/zoho-crm-packages.yml
- group: build
  href: https://artifacts.apis.io/zoho-crm/cli/zoho-crm-cli.yml
  title: ''
  type: CLI
  url: cli/zoho-crm-cli.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/components/zoho-crm-components.yml
  title: ''
  type: Components
  url: components/zoho-crm-components.yml
- group: start
  href: https://artifacts.apis.io/zoho-crm/sandbox/zoho-crm-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/zoho-crm-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/zoho-crm/well-known/zoho-crm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zoho-crm-well-known.yml
- group: auth
  href: https://artifacts.apis.io/zoho-crm/well-known/zoho-crm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zoho-crm-security.txt
- group: auth
  href: https://artifacts.apis.io/zoho-crm/security/zoho-crm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-crm-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: auth
  href: https://artifacts.apis.io/zoho-crm/security/zoho-crm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zoho-crm-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/zoho-crm/security/zoho-crm-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/zoho-crm-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.zoho.com/compliance.html
- group: design
  href: https://artifacts.apis.io/zoho-crm/conformance/zoho-crm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zoho-crm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/zoho-crm/mcp/zoho-crm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/zoho-crm-mcp.yml
- group: agent
  href: https://artifacts.apis.io/zoho-crm/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/zoho-crm/agentic-access/zoho-crm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-crm-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/zoho-crm/llms/zoho-crm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zoho-crm-llms.txt
- group: docs
  href: https://artifacts.apis.io/zoho-crm/asyncapi/zoho-crm-notifications-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/zoho-crm-notifications-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/asyncapi/zoho-crm-notifications-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/zoho-crm-notifications-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/zoho-crm/rules/zoho-crm-asyncapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/zoho-crm-asyncapi-spectral-rules.yml
created: '2026-05-11'
description: Zoho CRM is Zoho Corporation's AI-powered sales and customer relationship management platform, used to manage leads, contacts, accounts, deals, activities and customer engagement across channels. Its REST API is currently at v8 and is published as first-party OpenAPI 3.1.0 — 105 specification files covering 405 operations, hosted by Zoho at github.com/zoho/crm-oas and linked from the developer documentation. Authentication is OAuth 2.0 authorization-code against accounts.zoho.com with 458 distinct scopes, and every specification templates both the data centre and the API version into the server URL (https://zohoapis.{dc}/crm/{version}, dc one of com, eu, in, cn, au). Usage is metered in API credits on a rolling 24-hour window rather than in requests, alongside an org-level concurrency cap. Zoho additionally ships server-side SDKs for Node.js, TypeScript, Python, PHP, C#, Java, Ruby and Scala, a widget/extension CLI (ZET), a documented webhook surface (Instant Notifications),
  and a hosted MCP product that names Zoho CRM as a supported app.
finops:
- has_sources: true
  method: derived
  name: Zoho Crm Finops
  primary_unit: seat
  service_category: ''
  slug: zoho-crm-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-crm.png
json_schemas:
- name: ActionResponse
  property_count: 1
  slug: zoho-crm-action-response
- name: ApiName
  property_count: 0
  slug: zoho-crm-api-name
- name: AttachmentListResponse
  property_count: 2
  slug: zoho-crm-attachment-list-response
- name: AttachmentSuccessResponse
  property_count: 1
  slug: zoho-crm-attachment-success-response
- name: BulkOperationResponse
  property_count: 1
  slug: zoho-crm-bulk-operation-response
- name: ConversionRequestWrapper
  property_count: 1
  slug: zoho-crm-conversion-request-wrapper
- name: ConversionScheduledWrapper
  property_count: 1
  slug: zoho-crm-conversion-scheduled-wrapper
- name: ConversionSuccessWrapper
  property_count: 1
  slug: zoho-crm-conversion-success-wrapper
- name: CoqlFieldSchema
  property_count: 74
  slug: zoho-crm-coql-field-schema
- name: DataError
  property_count: 4
  slug: zoho-crm-data-error
- name: DeleteRelationsSuccessResponse
  property_count: 1
  slug: zoho-crm-delete-relations-success-response
- name: Delete207SuccessResponse
  property_count: 4
  slug: zoho-crm-delete207-success-response
- name: Error Response Core
  property_count: 4
  slug: zoho-crm-error-response-core1168955151
- name: Error Response Core
  property_count: 4
  slug: zoho-crm-error-response-core1544688711
- name: Error Response Core
  property_count: 4
  slug: zoho-crm-error-response-core2137699283
- name: Error Response Core
  property_count: 4
  slug: zoho-crm-error-response-core297287888
- name: FieldLabel
  property_count: 0
  slug: zoho-crm-field-label
- name: FieldRequestBodySchema
  property_count: 1
  slug: zoho-crm-field-request-body-schema
- name: FieldSchema
  property_count: 72
  slug: zoho-crm-field-schema
- name: FieldUpdateRequestBodySchema
  property_count: 1
  slug: zoho-crm-field-update-request-body-schema
- name: GetservicessResponse200
  property_count: 1
  slug: zoho-crm-getservicess-response200
- name: GetworkflowconfigurationsResponse200
  property_count: 1
  slug: zoho-crm-getworkflowconfigurations-response200
- name: HolidaysSuccessResponse
  property_count: 1
  slug: zoho-crm-holidays-success-response
- name: Id
  property_count: 0
  slug: zoho-crm-id
- name: Info
  property_count: 4
  slug: zoho-crm-info
- name: ModulepluralLabel
  property_count: 0
  slug: zoho-crm-moduleplural-label
- name: OrgDetails
  property_count: 37
  slug: zoho-crm-org-details
- name: PickListDisplayValue
  property_count: 0
  slug: zoho-crm-pick-list-display-value
- name: PickListReferenceValue
  property_count: 0
  slug: zoho-crm-pick-list-reference-value
- name: Post207multistatusResponse207
  property_count: 4
  slug: zoho-crm-post207multistatus-response207
- name: PostappointmentssRequest
  property_count: 1
  slug: zoho-crm-postappointmentss-request
- name: PostservicessRequest
  property_count: 2
  slug: zoho-crm-postservicess-request
- name: RecordGETSucessResponse
  property_count: 2
  slug: zoho-crm-record-getsucess-response
- name: RecordSuccessResponse
  property_count: 1
  slug: zoho-crm-record-success-response
- name: RecordsInputSchema
  property_count: 4
  slug: zoho-crm-records-input-schema
- name: RelatedList
  property_count: 21
  slug: zoho-crm-related-list
- name: SendMailRequest
  property_count: 1
  slug: zoho-crm-send-mail-request
- name: SuccessResponse
  property_count: 1
  slug: zoho-crm-success-response
- name: TerritoryGetResponse
  property_count: 2
  slug: zoho-crm-territory-get-response
- name: TerritoryGETSchema
  property_count: 14
  slug: zoho-crm-territory-getschema
- name: TerritorySchedueledSuccessCode
  property_count: 1
  slug: zoho-crm-territory-schedueled-success-code
- name: UpdateLayoutRequest
  property_count: 1
  slug: zoho-crm-update-layout-request
- name: UpdateLayoutSuccessResponse
  property_count: 1
  slug: zoho-crm-update-layout-success-response
- name: UpsertRelationsRequest
  property_count: 1
  slug: zoho-crm-upsert-relations-request
- name: UpsertRelationsSuccessResponse
  property_count: 1
  slug: zoho-crm-upsert-relations-success-response
- name: UserDetails
  property_count: 54
  slug: zoho-crm-user-details
- name: User
  property_count: 46
  slug: zoho-crm-user
- name: ValidationErrorWrapper
  property_count: 1
  slug: zoho-crm-validation-error-wrapper
jsonld:
- class_count: 120
  name: Zoho Crm Context
  property_count: 75
  slug: zoho-crm-context
layout: provider
mcp_servers:
- description: Remote MCP server over HTTP requiring OAuth.
  name: Zoho MCP
  slug: zoho-mcp
modified: '2026-08-13'
name: Zoho CRM
nav: Providers
network: true
overview: 'Zoho CRM publishes 36 API contracts indexed on the [APIs.io](https://apis.io/) network, including Actions API, Appointments S API, Attachments API, and 33 more. Tagged areas include CRM, Sales, Marketing Automation, Lead Management, and Customer Engagement.


  The Zoho CRM catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Zoho CRM''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 155 more developer resources.'
plans:
- name: Zoho Crm Plans Pricing
  plan_count: 5
  slug: zoho-crm-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 12
  name: Zoho Crm Rate Limits
  slug: zoho-crm-rate-limits
rules:
- authorship: generated
  effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Zoho CRM — asyncapi rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: zoho-crm-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: Zoho CRM API Rules
  rule_count: 15
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 4
  slug: zoho-crm-rules
scopes:
- name: Zoho Crm Scopes
  scope_count: 458
  slug: zoho-crm-scopes
  summary_line: 458 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 86.0
  coverage:
    artifact_dirs: 37
    catalog_earned: 92.8
    catalog_earned_first_party: 24.0
    catalog_gap: 22.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 35.6
    contract_quality: 73.8
    developer_ergonomics: 82.7
    discoverability: 76.7
    operational_transparency: 92.1
  previous_composite: 86.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 36
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
    score: 33.3
screenshot: https://apis.io/screenshots/zoho-crm/zoho-crm-2026-06-20T201938.png
security:
- kind: authentication
  name: Zoho Crm Authentication
  slug: zoho-crm-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Zoho Crm Domain Security
  slug: zoho-crm-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Crm Vulnerability Disclosure
  slug: zoho-crm-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Zoho Crm Trust Center
  slug: zoho-crm-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO/IEC 27701, ISO 9001, ISO/IEC 20000-1, ISO 22301, SOC 1 Type 2 (SSAE 18 / ISAE 3402), SOC 2 Type 2, SOC 2 + HIPAA Type 2, PCI DSS (SAQ-D), CSA STAR Self-Assessment, Cyber Essentials Plus, TX-RAMP, ENS (Esquema Nacional de Seguridad, Spain), NCA Class B (Saudi Arabia), NHS DSPT (UK) v8, GoBD (Germany), 21 CFR Part 11 / EudraLex Annex 11, WCAG 2.2 AA
skill_count: 6
skills:
- name: bulk-export-and-import
  slug: zoho-crm-bulk-export-and-import
- name: convert-a-lead
  slug: zoho-crm-convert-a-lead
- name: create-and-update-records-safely
  slug: zoho-crm-create-and-update-records-safely
- name: discover-modules-and-fields
  slug: zoho-crm-discover-modules-and-fields
- name: query-and-search
  slug: zoho-crm-query-and-search
- name: subscribe-to-record-notifications
  slug: zoho-crm-subscribe-to-record-notifications
slug: zoho-crm
tags:
- CRM
- Sales
- Marketing Automation
- Lead Management
- Customer Engagement
- Sales Automation
- Contact Management
- Pipeline Management
- Software-as-a-Service
- OpenAPI
- Authentication
website: https://www.zoho.com/crm/
---
