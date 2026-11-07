---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: true
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Close Agentic Access
  operation_count: 300
  slug: close-agentic-access
  summary_line: 300 operations · 160 acting
api_count: 2
apis:
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities API from Close — 1 operation(s) for activities.
  name: Close Activities API
  phrasing_intents:
  - id: activities_list
    intent: List all activities across types
    question: What is the full activity history for a lead, across calls, emails and notes?
  phrasing_ops: 1
  slug: close-activities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.calls API from Close — 2 operation(s) for activities.calls.
  name: Close Activities.calls API
  phrasing_intents:
  - id: activities.calls_list
    intent: List call activities
    question: Which calls were logged against a particular lead?
  - id: activities.calls_create
    intent: Log an external call
    question: How do I log a call made outside the built-in dialer?
  - id: activities.calls_get
    intent: Get a single call activity
    question: Where can I see the details and notes of one call?
  - id: activities.calls_update
    intent: Update a call's notes or outcome
    question: Can I change the outcome of a call after it ended?
  - id: activities.calls_delete
    intent: Delete a call activity
    question: Can I remove a call that was logged by mistake?
  phrasing_ops: 5
  slug: close-activities-calls-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.creations API from Close — 2 operation(s) for activities.creations.
  name: Close Activities.creations API
  phrasing_intents:
  - id: activities.creations_list
    intent: List record-created activities
    question: When was a lead created and by whom?
  - id: activities.creations_get
    intent: Get a record-created activity
    question: How do I look up a single creation activity?
  phrasing_ops: 2
  slug: close-activities-creations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.custom_activities API from Close — 2 operation(s) for activities.custom_activities.
  name: Close Activities.custom Activities API
  phrasing_intents:
  - id: activities.custom_activities_list
    intent: List custom activity records
    question: Which custom activities have been logged on a particular lead?
  - id: activities.custom_activities_create
    intent: Log a custom activity on a lead
    question: How do I record a custom activity, like a demo form, on a lead?
  - id: activities.custom_activities_get
    intent: Get one custom activity record
    question: What custom field values were recorded on a specific custom activity?
  - id: activities.custom_activities_update
    intent: Update or publish a custom activity
    question: Can I move a custom activity from draft to published?
  - id: activities.custom_activities_delete
    intent: Delete a custom activity record
    question: Can I remove a custom activity that was logged by mistake?
  phrasing_ops: 5
  slug: close-activities-custom-activities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.email_threads API from Close — 2 operation(s) for activities.email_threads.
  name: Close Activities.email Threads API
  phrasing_intents:
  - id: activities.email_threads_list
    intent: List email conversations
    question: What email conversations have we had with a lead?
  - id: activities.email_threads_get
    intent: Get one email thread
    question: What messages are in a particular email thread?
  - id: activities.email_threads_delete
    intent: Delete an email thread and its emails
    question: Does deleting an email thread also delete its emails?
  phrasing_ops: 3
  slug: close-activities-email-threads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.emails API from Close — 2 operation(s) for activities.emails.
  name: Close Activities.emails API
  phrasing_intents:
  - id: activities.emails_list
    intent: List email activities
    question: What emails have been exchanged with a lead?
  - id: activities.emails_create
    intent: Create, draft, schedule or send an email
    question: How do I send an email to a lead through the API?
  - id: activities.emails_get
    intent: Get a single email activity
    question: How do I pull the full body of one email message?
  - id: activities.emails_update
    intent: Edit or send a draft email
    question: Can I finish a draft email and then send it?
  - id: activities.emails_delete
    intent: Delete an email activity
    question: Can I delete an email record from a lead's timeline?
  phrasing_ops: 5
  slug: close-activities-emails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.form_submissions API from Close — 2 operation(s) for activities.form_submissions.
  name: Close Activities.form Submissions API
  phrasing_intents:
  - id: activities.form_submissions_list
    intent: List form submission activities
    question: Which leads submitted a particular form?
  - id: activities.form_submissions_get
    intent: Get a single form submission
    question: What answers were given in one form submission?
  - id: activities.form_submissions_delete
    intent: Delete a form submission
    question: Can I remove a spam form submission from a lead?
  phrasing_ops: 3
  slug: close-activities-form-submissions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.import_updates API from Close — 2 operation(s) for activities.import_updates.
  name: Close Activities.import Updates API
  phrasing_intents:
  - id: activities.import_updates_list
    intent: List import update activities
    question: Which leads were modified by a bulk import?
  - id: activities.import_updates_get
    intent: Get one import update activity
    question: Was a specific import update reverted?
  - id: activities.import_updates_delete
    intent: Delete an import update activity
    question: Can I remove an import update entry from a lead's feed?
  phrasing_ops: 3
  slug: close-activities-import-updates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.lead_merges API from Close — 2 operation(s) for activities.lead_merges.
  name: Close Activities.lead Merges API
  phrasing_intents:
  - id: activities.lead_merges_list
    intent: List lead merge activities
    question: Which leads have been merged into this one?
  - id: activities.lead_merges_get
    intent: Get a lead merge activity
    question: How do I look up one lead merge record?
  phrasing_ops: 2
  slug: close-activities-lead-merges-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.lead_status_changes API from Close — 2 operation(s) for activities.lead_status_changes.
  name: Close Activities.lead Status Changes API
  phrasing_intents:
  - id: activities.lead_status_changes_list
    intent: List lead status change history
    question: When did a lead's status change and who changed it?
  - id: activities.lead_status_changes_create
    intent: Import a historical lead status change
    question: Can I import past lead status changes from another CRM?
  - id: activities.lead_status_changes_get
    intent: Get one lead status change
    question: What were the old and new statuses on a specific lead status change?
  - id: activities.lead_status_changes_delete
    intent: Remove a lead status change from the feed
    question: Can I remove an irrelevant status change from a lead's feed?
  phrasing_ops: 4
  slug: close-activities-lead-status-changes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.meetings API from Close — 3 operation(s) for activities.meetings.
  name: Close Activities.meetings API
  phrasing_intents:
  - id: activities.meetings_list
    intent: List meeting activities
    question: What meetings have been logged with a given lead?
  - id: activities.meetings_get
    intent: Get a meeting and its transcript
    question: Can I get the transcript of a recorded meeting?
  - id: activities.meetings_update
    intent: Update a meeting's notes or outcome
    question: Can I add my own notes to a meeting after it happened?
  - id: activities.meetings_delete
    intent: Delete a meeting activity
    question: Can I remove a meeting from a lead's activity feed?
  - id: activities.meetings_create_integration
    intent: Attach an app's integration tab to a meeting
    question: Can my OAuth app add its own tab to a meeting in the activity feed?
  phrasing_ops: 5
  slug: close-activities-meetings-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.notes API from Close — 2 operation(s) for activities.notes.
  name: Close Activities.notes API
  phrasing_intents:
  - id: activities.notes_list
    intent: List note activities
    question: What notes have been written on a lead?
  - id: activities.notes_create
    intent: Add a note to a lead
    question: How do I add a note with an attachment to a lead?
  - id: activities.notes_get
    intent: Get a single note
    question: How can I read one note's full text?
  - id: activities.notes_update
    intent: Edit, pin or unpin a note
    question: Can I pin an existing note to the top of a lead?
  - id: activities.notes_delete
    intent: Delete a note
    question: Can I remove a note from a lead's history?
  phrasing_ops: 5
  slug: close-activities-notes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.opportunity_status_changes API from Close — 2 operation(s) for activities.opportunity_status_changes.
  name: Close Activities.opportunity Status Changes API
  phrasing_intents:
  - id: activities.opportunity_status_changes_list
    intent: List opportunity status change history
    question: When did a deal move between stages?
  - id: activities.opportunity_status_changes_create
    intent: Import a historical opportunity status change
    question: Can I import past deal stage changes from another system?
  - id: activities.opportunity_status_changes_get
    intent: Get one opportunity status change
    question: What stage did a deal move from and to in a specific change?
  - id: activities.opportunity_status_changes_delete
    intent: Remove an opportunity status change from the feed
    question: Can I remove an irrelevant deal stage change from the feed?
  phrasing_ops: 4
  slug: close-activities-opportunity-status-changes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.sms API from Close — 2 operation(s) for activities.sms.
  name: Close Activities.sms API
  phrasing_intents:
  - id: activities.sms_list
    intent: List SMS activities
    question: What text messages have been exchanged with a lead?
  - id: activities.sms_create
    intent: Send, schedule or log an SMS
    question: How do I send a text message to a lead's contact?
  - id: activities.sms_get
    intent: Get one SMS activity
    question: What did a specific text message say?
  - id: activities.sms_update
    intent: Edit or send a draft SMS
    question: Can I send an SMS I saved as a draft?
  - id: activities.sms_delete
    intent: Delete an SMS activity
    question: Can I delete a text message from a lead's history?
  phrasing_ops: 5
  slug: close-activities-sms-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.task_completions API from Close — 2 operation(s) for activities.task_completions.
  name: Close Activities.task Completions API
  phrasing_intents:
  - id: activities.task_completions_list
    intent: List completed-task activities
    question: Which tasks were completed on a lead?
  - id: activities.task_completions_get
    intent: Get a completed-task activity
    question: How do I look up one task completion record?
  - id: activities.task_completions_delete
    intent: Delete a completed-task activity
    question: Can I remove a task completion entry from the timeline?
  phrasing_ops: 3
  slug: close-activities-task-completions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.whatsapp_messages API from Close — 2 operation(s) for activities.whatsapp_messages.
  name: Close Activities.whatsapp Messages API
  phrasing_intents:
  - id: activities.whatsapp_messages_list
    intent: List WhatsApp message activities
    question: Which WhatsApp messages have been logged for a lead?
  - id: activities.whatsapp_messages_create
    intent: Log a WhatsApp message
    question: How do I sync a WhatsApp conversation into a lead's timeline?
  - id: activities.whatsapp_messages_get
    intent: Get a single WhatsApp message
    question: How can I view one logged WhatsApp message?
  - id: activities.whatsapp_messages_update
    intent: Update a logged WhatsApp message
    question: What if a WhatsApp message was edited after I logged it?
  - id: activities.whatsapp_messages_delete
    intent: Delete a logged WhatsApp message
    question: When a message is deleted in WhatsApp, how do I remove it here too?
  phrasing_ops: 5
  slug: close-activities-whatsapp-messages-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The blocked_phone_numbers API from Close — 3 operation(s) for blocked_phone_numbers.
  name: Close Blocked Phone Numbers API
  phrasing_intents:
  - id: blocked_phone_numbers_list
    intent: List blocked phone numbers
    question: Which phone numbers are blocked in my organization?
  - id: blocked_phone_numbers_create
    intent: Block a phone number
    question: How do I stop a phone number from calling us or being called?
  - id: blocked_phone_numbers_get_settings
    intent: View call blocking settings
    question: Are anonymous inbound calls currently rejected for my organization?
  - id: blocked_phone_numbers_update_settings
    intent: Toggle rejecting anonymous inbound calls
    question: Can I automatically reject calls from anonymous or hidden numbers?
  - id: blocked_phone_numbers_get
    intent: Get one blocked phone number
    question: Why was a specific phone number blocked?
  - id: blocked_phone_numbers_update
    intent: Change the reason a number is blocked
    question: Can I edit the reason recorded on a blocked phone number?
  - id: blocked_phone_numbers_delete
    intent: Unblock a phone number
    question: How can I let a previously blocked number call us again?
  phrasing_ops: 7
  slug: close-blocked-phone-numbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.delete API from Close — 2 operation(s) for bulk_actions.delete.
  name: Close Bulk Actions.delete API
  phrasing_intents:
  - id: bulk_actions.delete_list
    intent: List bulk delete jobs
    question: Which bulk deletes have been run?
  - id: bulk_actions.delete_create
    intent: Bulk delete leads matching a query
    question: How do I delete many leads at once that match a search?
  - id: bulk_actions.delete_get
    intent: Check a bulk delete job
    question: Has my bulk delete finished?
  phrasing_ops: 3
  slug: close-bulk-actions-delete-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.edit API from Close — 2 operation(s) for bulk_actions.edit.
  name: Close Bulk Actions.edit API
  phrasing_intents:
  - id: bulk_actions.edit_list
    intent: List bulk edit jobs
    question: What bulk edits have been run on our leads?
  - id: bulk_actions.edit_create
    intent: Bulk edit many leads at once
    question: How do I change the status of every lead in a search?
  - id: bulk_actions.edit_get
    intent: Check a bulk edit job
    question: Has my bulk edit finished yet?
  phrasing_ops: 3
  slug: close-bulk-actions-edit-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.email API from Close — 2 operation(s) for bulk_actions.email.
  name: Close Bulk Actions.email API
  phrasing_intents:
  - id: bulk_actions.email_list
    intent: List bulk email jobs
    question: Which bulk email sends have gone out?
  - id: bulk_actions.email_create
    intent: Send a bulk email to matching leads
    question: How do I email every lead that matches a search?
  - id: bulk_actions.email_get
    intent: Check a bulk email job
    question: Is my bulk email send complete?
  phrasing_ops: 3
  slug: close-bulk-actions-email-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.sequence_subscriptions API from Close — 2 operation(s) for bulk_actions.sequence_subscriptions.
  name: Close Bulk Actions.sequence Subscriptions API
  phrasing_intents:
  - id: bulk_actions.sequence_subscriptions_list
    intent: List bulk sequence subscription jobs
    question: What bulk sequence enrollments have we run?
  - id: bulk_actions.sequence_subscriptions_create
    intent: Bulk subscribe, pause or resume sequences
    question: How do I enroll every contact in a search into a sequence?
  - id: bulk_actions.sequence_subscriptions_get
    intent: Check a bulk sequence subscription job
    question: Has my bulk sequence enrollment finished?
  phrasing_ops: 3
  slug: close-bulk-actions-sequence-subscriptions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The comments API from Close — 4 operation(s) for comments.
  name: Close Comments API
  phrasing_intents:
  - id: comments_list
    intent: List comments on an object or thread
    question: How can I see all comments left on a lead?
  - id: comments_create
    intent: Add a comment to a record
    question: How do I leave a comment on a lead or activity?
  - id: comments_get
    intent: Get a single comment
    question: Why do I get a 404 fetching a comment I know exists?
  - id: comments_update
    intent: Edit a comment's text
    question: Can I edit a comment someone else wrote?
  - id: comments_delete
    intent: Remove a comment
    question: Does removing a comment delete the whole thread?
  - id: comments_list_threads
    intent: List comment threads
    question: Which records have comment threads on them?
  - id: comments_get_thread
    intent: Get a single comment thread
    question: Can I load one comment thread with all its comments?
  phrasing_ops: 7
  slug: close-comments-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The connected_accounts API from Close — 2 operation(s) for connected_accounts.
  name: Close Connected Accounts API
  phrasing_intents:
  - id: connected_accounts_list
    intent: List connected accounts
    question: Which email and calendar accounts are connected?
  - id: connected_accounts_get
    intent: Fetch a connected account
    question: What are the details of a specific connected account?
  phrasing_ops: 2
  slug: close-connected-accounts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The contacts API from Close — 2 operation(s) for contacts.
  name: Close Contacts API
  phrasing_intents:
  - id: contacts_list
    intent: List contacts
    question: Who are the contacts on a particular lead?
  - id: contacts_create
    intent: Create a contact
    question: How do I add a new person to an existing lead?
  - id: contacts_get
    intent: Fetch a contact
    question: What email and phone numbers do we have for a specific contact?
  - id: contacts_update
    intent: Update a contact
    question: Can I change a contact's job title or phone numbers?
  - id: contacts_delete
    intent: Delete a contact
    question: Can I delete a contact without deleting the lead?
  phrasing_ops: 5
  slug: close-contacts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_activity_types API from Close — 2 operation(s) for custom_activity_types.
  name: Close Custom Activity Types API
  phrasing_intents:
  - id: custom_activity_types_list
    intent: List custom activity types
    question: What custom activity types have we defined?
  - id: custom_activity_types_create
    intent: Create a custom activity type
    question: How do I define a new kind of activity like a demo or site visit?
  - id: custom_activity_types_get
    intent: Get a custom activity type
    question: Which fields belong to a specific custom activity type?
  - id: custom_activity_types_update
    intent: Update a custom activity type
    question: Can I archive a custom activity type or rename it?
  - id: custom_activity_types_delete
    intent: Delete a custom activity type
    question: Can I permanently delete an activity type we no longer track?
  phrasing_ops: 5
  slug: close-custom-activity-types-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_field_schemas API from Close — 1 operation(s) for custom_field_schemas.
  name: Close Custom Field Schemas API
  phrasing_intents:
  - id: custom_field_schemas_get
    intent: Get the custom field order for an object type
    question: In what order do custom fields appear on leads?
  - id: custom_field_schemas_update
    intent: Reorder custom fields for an object type
    question: Can I change the display order of custom fields?
  phrasing_ops: 2
  slug: close-custom-field-schemas-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.activity API from Close — 2 operation(s) for custom_fields.activity.
  name: Close Custom Fields.activity API
  phrasing_intents:
  - id: custom_fields.activity_list
    intent: List activity custom fields
    question: Which custom fields are defined on our custom activities?
  - id: custom_fields.activity_create
    intent: Add a field to a custom activity type
    question: How do I add a new field to a custom activity type?
  - id: custom_fields.activity_get
    intent: Fetch an activity custom field
    question: What type and options does a specific activity custom field have?
  - id: custom_fields.activity_update
    intent: Update an activity custom field
    question: Can I rename an activity custom field or change its choices?
  - id: custom_fields.activity_delete
    intent: Delete an activity custom field
    question: What happens to existing values when I delete an activity custom field?
  phrasing_ops: 5
  slug: close-custom-fields-activity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.contact API from Close — 2 operation(s) for custom_fields.contact.
  name: Close Custom Fields.contact API
  phrasing_intents:
  - id: custom_fields.contact_list
    intent: List contact custom fields
    question: What custom fields exist on contacts?
  - id: custom_fields.contact_create
    intent: Create a contact custom field
    question: How do I add a new custom field to contacts?
  - id: custom_fields.contact_get
    intent: Get a contact custom field
    question: What type is a particular contact custom field?
  - id: custom_fields.contact_update
    intent: Edit a contact custom field
    question: Can I change a contact field's type after creating it?
  - id: custom_fields.contact_delete
    intent: Delete a contact custom field
    question: Will deleting a contact field wipe values on existing contacts?
  phrasing_ops: 5
  slug: close-custom-fields-contact-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.custom_object API from Close — 2 operation(s) for custom_fields.custom_object.
  name: Close Custom Fields.custom Object API
  phrasing_intents:
  - id: custom_fields.custom_object_list
    intent: List custom object custom fields
    question: Which fields are defined on our custom object types?
  - id: custom_fields.custom_object_create
    intent: Add a field to a custom object type
    question: How do I add a field to a custom object type?
  - id: custom_fields.custom_object_get
    intent: Fetch a custom object custom field
    question: What are the settings of a specific custom object field?
  - id: custom_fields.custom_object_update
    intent: Update a custom object custom field
    question: Can I rename a custom object field or change its choice options?
  - id: custom_fields.custom_object_delete
    intent: Delete a custom object custom field
    question: Are values lost when I delete a custom object field?
  phrasing_ops: 5
  slug: close-custom-fields-custom-object-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.lead API from Close — 2 operation(s) for custom_fields.lead.
  name: Close Custom Fields.lead API
  phrasing_intents:
  - id: custom_fields.lead_list
    intent: List lead custom fields
    question: What custom fields do our leads have?
  - id: custom_fields.lead_create
    intent: Create a lead custom field
    question: How do I add a new custom field to leads?
  - id: custom_fields.lead_get
    intent: Get a lead custom field
    question: What are the options of a specific lead custom field?
  - id: custom_fields.lead_update
    intent: Edit a lead custom field
    question: Can I switch a lead field to accept multiple values?
  - id: custom_fields.lead_delete
    intent: Delete a lead custom field
    question: Does deleting a lead field remove its values from every lead?
  phrasing_ops: 5
  slug: close-custom-fields-lead-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.opportunity API from Close — 2 operation(s) for custom_fields.opportunity.
  name: Close Custom Fields.opportunity API
  phrasing_intents:
  - id: custom_fields.opportunity_list
    intent: List opportunity custom fields
    question: Which custom fields do our opportunities have?
  - id: custom_fields.opportunity_create
    intent: Create an opportunity custom field
    question: How do I add a custom field to opportunities?
  - id: custom_fields.opportunity_get
    intent: Fetch an opportunity custom field
    question: What type is a specific opportunity custom field?
  - id: custom_fields.opportunity_update
    intent: Update an opportunity custom field
    question: Can I change the type of an opportunity custom field?
  - id: custom_fields.opportunity_delete
    intent: Delete an opportunity custom field
    question: What happens to deal values when I delete an opportunity custom field?
  phrasing_ops: 5
  slug: close-custom-fields-opportunity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.shared API from Close — 4 operation(s) for custom_fields.shared.
  name: Close Custom Fields.shared API
  phrasing_intents:
  - id: custom_fields.shared_list
    intent: List shared custom fields
    question: Which custom fields are shared across leads, contacts and activities?
  - id: custom_fields.shared_create
    intent: Create a shared custom field
    question: How do I create a custom field that can be reused on several object types?
  - id: custom_fields.shared_get
    intent: Get a shared custom field
    question: Where do I see the type and associations of one shared field?
  - id: custom_fields.shared_update
    intent: Rename or edit a shared custom field
    question: Can I change the type of a shared custom field after creating it?
  - id: custom_fields.shared_delete
    intent: Delete a shared custom field
    question: What happens to stored values when I delete a shared custom field?
  - id: custom_fields.shared_create_association
    intent: Attach a shared field to an object type
    question: How do I make a shared custom field available on contacts?
  - id: custom_fields.shared_get_association
    intent: Get a shared field's object-type association
    question: Is a shared field required on a particular object type?
  - id: custom_fields.shared_update_association
    intent: Change a shared field association's rules
    question: Can I make a shared field required only on leads?
  phrasing_ops: 9
  slug: close-custom-fields-shared-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_object_types API from Close — 2 operation(s) for custom_object_types.
  name: Close Custom Object Types API
  phrasing_intents:
  - id: custom_object_types_list
    intent: List custom object types
    question: What custom object types have we defined?
  - id: custom_object_types_create
    intent: Create a custom object type
    question: How do I define a new custom object like Subscriptions or Properties?
  - id: custom_object_types_get
    intent: Get a custom object type
    question: How do I look up one custom object type's fields?
  - id: custom_object_types_update
    intent: Update a custom object type
    question: Can I rename a custom object type or change its plural name?
  - id: custom_object_types_delete
    intent: Delete a custom object type
    question: Can I permanently delete a custom object type?
  phrasing_ops: 5
  slug: close-custom-object-types-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_objects API from Close — 2 operation(s) for custom_objects.
  name: Close Custom Objects API
  phrasing_intents:
  - id: custom_objects_list
    intent: List a lead's custom object records
    question: Which custom object records are attached to a lead?
  - id: custom_objects_create
    intent: Create a custom object record
    question: How do I create a custom object record on a lead?
  - id: custom_objects_get
    intent: Retrieve a custom object record
    question: What values does a specific custom object record hold?
  - id: custom_objects_update
    intent: Update a custom object record
    question: Can I rename a custom object record?
  - id: custom_objects_delete
    intent: Delete a custom object record
    question: Can I delete a custom object record from a lead?
  phrasing_ops: 5
  slug: close-custom-objects-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The dialers API from Close — 2 operation(s) for dialers.
  name: Close Dialers API
  phrasing_intents:
  - id: dialers_list
    intent: List dialer sessions
    question: Which power dialer sessions are running right now?
  - id: dialers_get
    intent: Get a dialer session
    question: What smart view is a specific dialer session calling through?
  phrasing_ops: 2
  slug: close-dialers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The email_templates API from Close — 3 operation(s) for email_templates.
  name: Close Email Templates API
  phrasing_intents:
  - id: email_templates_list
    intent: List email templates
    question: Which email templates do we have?
  - id: email_templates_create
    intent: Create an email template
    question: How do I save a reusable email template?
  - id: email_templates_get
    intent: Fetch an email template
    question: What's the subject and body of a given email template?
  - id: email_templates_update
    intent: Update an email template
    question: Can I edit an existing email template's wording?
  - id: email_templates_delete
    intent: Delete an email template
    question: Can I permanently remove an email template?
  - id: email_templates_render
    intent: Preview an email template for a lead
    question: What would an email template look like filled in for a specific lead and contact?
  phrasing_ops: 6
  slug: close-email-templates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The events API from Close — 2 operation(s) for events.
  name: Close Events API
  phrasing_intents:
  - id: events_list
    intent: List events from the change log
    question: What changed on a lead recently?
  - id: events_get
    intent: Get a single event
    question: How do I look up one event in the change log?
  phrasing_ops: 2
  slug: close-events-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The exports API from Close — 6 operation(s) for exports.
  name: Close Exports API
  phrasing_intents:
  - id: exports_list
    intent: List all data exports
    question: Which exports has my organization run, of any kind?
  - id: exports_list_lead
    intent: List lead exports
    question: What lead exports have been run recently?
  - id: exports_create_lead
    intent: Export leads matching a search
    question: How do I export leads that match a search query to a file?
  - id: exports_get_lead
    intent: Check a lead export's status
    question: Is my lead export finished yet?
  - id: exports_list_opportunity
    intent: List opportunity exports
    question: Which opportunity exports have been generated?
  - id: exports_create_opportunity
    intent: Export opportunities by filter
    question: Can I export opportunities as CSV or JSON using opportunity filters?
  - id: exports_get_opportunity
    intent: Check an opportunity export's status
    question: Has my opportunity export finished processing?
  - id: exports_get
    intent: Get any export by id
    question: What status is a given export in, whatever its type?
  phrasing_ops: 8
  slug: close-exports-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The field_enrichment API from Close — 1 operation(s) for field_enrichment.
  name: Close Field Enrichment API
  phrasing_intents:
  - id: field_enrichment_create
    intent: Enrich a lead or contact field with AI
    question: Can AI fill in a custom field on a lead or contact for me?
  phrasing_ops: 1
  slug: close-field-enrichment-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The files API from Close — 1 operation(s) for files.
  name: Close Files API
  phrasing_intents:
  - id: files_create
    intent: Get a signed upload for a file
    question: How do I upload a file so I can attach it to a note or email?
  phrasing_ops: 1
  slug: close-files-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The forms API from Close — 2 operation(s) for forms.
  name: Close Forms API
  phrasing_intents:
  - id: forms_list
    intent: List forms
    question: Which forms does my organization have?
  - id: forms_fetch
    intent: Retrieve a form and its fields
    question: What fields are on a specific form?
  phrasing_ops: 2
  slug: close-forms-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The groups API from Close — 4 operation(s) for groups.
  name: Close Groups API
  phrasing_intents:
  - id: groups_list
    intent: List user groups
    question: What user groups exist in my organization?
  - id: groups_create
    intent: Create a user group
    question: How do I create a new team group?
  - id: groups_add_member
    intent: Add a user to a group
    question: Can I add a teammate to an existing group?
  - id: groups_remove_member
    intent: Remove a user from a group
    question: Can I take someone out of a group without removing them from the organization?
  - id: groups_get
    intent: Fetch a group and its members
    question: Who are the members of a particular group?
  - id: groups_update
    intent: Rename a group
    question: Can I rename an existing group?
  - id: groups_delete
    intent: Delete a group
    question: Can I delete a group that's used in a smart view or saved report?
  phrasing_ops: 7
  slug: close-groups-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The integration_links API from Close — 2 operation(s) for integration_links.
  name: Close Integration Links API
  phrasing_intents:
  - id: integration_links_list
    intent: List integration links
    question: Which integration links have we added to records?
  - id: integration_links_create
    intent: Create an integration link
    question: How do I add a link to an external tool on every lead?
  - id: integration_links_get
    intent: Get an integration link
    question: How do I look up one integration link's URL?
  - id: integration_links_update
    intent: Update an integration link
    question: Can I change where an integration link points?
  - id: integration_links_delete
    intent: Delete an integration link
    question: Can I remove an integration link we no longer need?
  phrasing_ops: 5
  slug: close-integration-links-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The lead_statuses API from Close — 2 operation(s) for lead_statuses.
  name: Close Lead Statuses API
  phrasing_intents:
  - id: lead_statuses_list
    intent: List lead statuses
    question: What lead statuses are set up in my organization?
  - id: lead_statuses_create
    intent: Create a lead status
    question: How do I add a new lead status like 'Nurturing'?
  - id: lead_statuses_get
    intent: Fetch a lead status
    question: What's the label and color of a specific lead status?
  - id: lead_statuses_update
    intent: Rename or recolor a lead status
    question: Can I rename a lead status or change its color?
  - id: lead_statuses_delete
    intent: Delete a lead status
    question: Can I delete a lead status that leads are still using?
  phrasing_ops: 5
  slug: close-lead-statuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The leads API from Close — 3 operation(s) for leads.
  name: Close Leads API
  phrasing_intents:
  - id: leads_list
    intent: List leads
    question: How can I pull every lead in my Close account?
  - id: leads_create
    intent: Create a lead
    question: Can I create a lead with its contacts and address in one call?
  - id: leads_merge
    intent: Merge two duplicate leads
    question: How do I merge a duplicate lead into another one?
  - id: leads_get
    intent: Get a single lead
    question: Where can I see everything about one lead?
  - id: leads_update
    intent: Update a lead
    question: Can I change a lead's status or custom fields without replacing the lead?
  - id: leads_delete
    intent: Delete a lead
    question: Can I permanently delete a lead from the CRM?
  phrasing_ops: 6
  slug: close-leads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The memberships API from Close — 3 operation(s) for memberships.
  name: Close Memberships API
  phrasing_intents:
  - id: memberships_create
    intent: Add a user to the organization
    question: How do I provision a new user into my organization by email?
  - id: memberships_bulk_update
    intent: Bulk update several memberships
    question: Can I change the role of many users at once?
  - id: memberships_update
    intent: Update one user's membership
    question: Can I change a single user's role or default caller ID?
  - id: memberships_delete
    intent: Deactivate a user's membership
    question: How do I remove a user from my organization?
  - id: memberships_get_pinned_views
    intent: Get a member's pinned views
    question: Which smart views has a user pinned, and in what order?
  - id: memberships_update_pinned_views
    intent: Set a member's pinned views
    question: Can I choose which saved views are pinned for a teammate?
  phrasing_ops: 6
  slug: close-memberships-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The opportunities API from Close — 2 operation(s) for opportunities.
  name: Close Opportunities API
  phrasing_intents:
  - id: opportunities_list
    intent: List or filter opportunities
    question: Which deals are still open for a given rep?
  - id: opportunities_create
    intent: Create an opportunity
    question: How do I add a new deal to a lead?
  - id: opportunities_get
    intent: Get a single opportunity
    question: Where can I see all details of one deal?
  - id: opportunities_update
    intent: Update an opportunity
    question: How do I mark a deal as won?
  - id: opportunities_delete
    intent: Delete an opportunity
    question: Can I delete a deal that was created by mistake?
  phrasing_ops: 5
  slug: close-opportunities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The opportunity_statuses API from Close — 2 operation(s) for opportunity_statuses.
  name: Close Opportunity Statuses API
  phrasing_intents:
  - id: opportunity_statuses_list
    intent: List opportunity statuses
    question: What deal stages are defined for opportunities?
  - id: opportunity_statuses_create
    intent: Create an opportunity status
    question: How do I add a new deal stage to a pipeline?
  - id: opportunity_statuses_get
    intent: Fetch an opportunity status
    question: Which pipeline does a specific opportunity status belong to?
  - id: opportunity_statuses_update
    intent: Rename an opportunity status
    question: Can I rename a deal stage?
  - id: opportunity_statuses_delete
    intent: Delete an opportunity status
    question: Can I delete a deal stage that opportunities still use?
  phrasing_ops: 5
  slug: close-opportunity-statuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The organizations API from Close — 1 operation(s) for organizations.
  name: Close Organizations API
  phrasing_intents:
  - id: organizations_get
    intent: Get organization details
    question: Who are the active and inactive members of our organization?
  - id: organizations_update
    intent: Update organization settings
    question: How do I change our organization's default currency?
  phrasing_ops: 2
  slug: close-organizations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The outcomes API from Close — 2 operation(s) for outcomes.
  name: Close Outcomes API
  phrasing_intents:
  - id: outcomes_list
    intent: List call and meeting outcomes
    question: What outcomes can reps pick after a call or meeting?
  - id: outcomes_create
    intent: Create an outcome
    question: How do I add a new call outcome like Left Voicemail?
  - id: outcomes_get
    intent: Get a single outcome
    question: How do I look up one outcome's definition?
  - id: outcomes_update
    intent: Edit an outcome
    question: Can I rename an outcome reps are already using?
  - id: outcomes_delete
    intent: Delete an outcome
    question: Do calls keep their outcome if I delete it?
  phrasing_ops: 5
  slug: close-outcomes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The phone_numbers API from Close — 3 operation(s) for phone_numbers.
  name: Close Phone Numbers API
  phrasing_intents:
  - id: phone_numbers_list
    intent: List or search phone numbers
    question: Which phone numbers does my team have?
  - id: phone_numbers_create
    intent: Rent a new phone number
    question: How do I get a new phone number in a given country?
  - id: phone_numbers_get
    intent: Retrieve a phone number
    question: What are the forwarding and voicemail settings on a specific number?
  - id: phone_numbers_update
    intent: Update a phone number's settings
    question: Can I set up call forwarding on my number?
  - id: phone_numbers_delete
    intent: Release a phone number
    question: Can I get rid of a phone number we no longer need?
  phrasing_ops: 5
  slug: close-phone-numbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The pipelines API from Close — 2 operation(s) for pipelines.
  name: Close Pipelines API
  phrasing_intents:
  - id: pipelines_list
    intent: List sales pipelines
    question: Which sales pipelines do we have?
  - id: pipelines_create
    intent: Create a sales pipeline
    question: How do I add a new pipeline for a different sales process?
  - id: pipelines_get
    intent: Get a single pipeline
    question: How do I see the stages of one pipeline?
  - id: pipelines_update
    intent: Rename or reorder a pipeline
    question: Can I reorder the opportunity statuses in a pipeline?
  - id: pipelines_delete
    intent: Delete an empty pipeline
    question: Why can't I delete a pipeline that still has statuses?
  phrasing_ops: 5
  slug: close-pipelines-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The playbooks API from Close — 4 operation(s) for playbooks.
  name: Close Playbooks API
  phrasing_intents:
  - id: playbooks_list
    intent: List call playbooks
    question: Which call playbooks does our team have?
  - id: playbooks_create
    intent: Create a call playbook
    question: How do I create a playbook with outcomes and custom fields?
  - id: playbooks_get
    intent: Get a single playbook
    question: What outcomes and fields are in a specific playbook?
  - id: playbooks_update
    intent: Edit a playbook
    question: Can I change which outcomes a playbook uses?
  - id: playbooks_delete
    intent: Delete a playbook
    question: Is deleting a playbook different from archiving it?
  - id: playbooks_archive
    intent: Archive a playbook
    question: Does archiving a playbook keep its history?
  - id: playbooks_unarchive
    intent: Restore an archived playbook
    question: Can I bring back a playbook I archived?
  phrasing_ops: 7
  slug: close-playbooks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The reporting API from Close — 8 operation(s) for reporting.
  name: Close Reporting API
  phrasing_intents:
  - id: reporting_get_activity
    intent: Run an activity metrics report
    question: How many calls and emails did my team log per week last quarter?
  - id: reporting_list_activity_metrics
    intent: List metrics for activity reports
    question: What predefined metrics can I use in an activity report?
  - id: reporting_get_custom
    intent: Graph arbitrary metrics with Explorer
    question: Can I chart opportunity value by user over time like the Explorer view?
  - id: reporting_get_funnel_stages
    intent: Get pipeline funnel stage metrics
    question: How many opportunities moved through each stage of my pipeline funnel?
  - id: reporting_get_funnel_totals
    intent: Get pipeline funnel totals
    question: What are the overall totals for my opportunity funnel?
  - id: reporting_get_sent_emails
    intent: Report on sent emails
    question: How many emails did a particular rep send last week?
  - id: reporting_get_lead_statuses
    intent: Report on lead status changes
    question: How many leads moved from Potential to Qualified this month?
  - id: reporting_get_opportunity_statuses
    intent: Report on opportunity status changes
    question: How many deals were marked won or lost between two dates?
  phrasing_ops: 8
  slug: close-reporting-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The roles API from Close — 2 operation(s) for roles.
  name: Close Roles API
  phrasing_intents:
  - id: roles_list
    intent: List roles
    question: What permission roles exist in my organization?
  - id: roles_create
    intent: Create a custom role
    question: How do I create a role that can only see leads assigned to them?
  - id: roles_get
    intent: Fetch a role
    question: Which permissions does a specific role have?
  - id: roles_update
    intent: Update a role
    question: Can I change the permissions on an existing role?
  - id: roles_delete
    intent: Delete a custom role
    question: Can I delete a role that users are still assigned to?
  phrasing_ops: 5
  slug: close-roles-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The scheduling_links API from Close — 8 operation(s) for scheduling_links.
  name: Close Scheduling Links API
  phrasing_intents:
  - id: scheduling_links_list
    intent: List my personal scheduling links
    question: Which personal booking links do I have set up in Close?
  - id: scheduling_links_create
    intent: Create a personal scheduling link
    question: How do I add a new personal booking link for my meetings?
  - id: scheduling_links_create_integration
    intent: Upsert a scheduling link from an OAuth app
    question: Can my OAuth integration create or update a user's scheduling link by its source id?
  - id: scheduling_links_delete_integration
    intent: Delete an OAuth app's scheduling link by source id
    question: Can my OAuth app remove a scheduling link it created using its own source id?
  - id: scheduling_links_get
    intent: Fetch one personal scheduling link
    question: What are the details of a specific user scheduling link?
  - id: scheduling_links_update
    intent: Update a personal scheduling link
    question: Can I change the name or URL of an existing personal booking link?
  - id: scheduling_links_delete
    intent: Delete a personal scheduling link
    question: Can I remove one of my own booking links that I no longer use?
  - id: scheduling_links_list_shared
    intent: List team shared scheduling links
    question: Which shared scheduling links exist for my team?
  phrasing_ops: 14
  slug: close-scheduling-links-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The send_as API from Close — 3 operation(s) for send_as.
  name: Close Send As API
  phrasing_intents:
  - id: send_as_list
    intent: List send-as permissions
    question: Who is allowed to send emails as me?
  - id: send_as_create
    intent: Let another user send as you
    question: How do I let a teammate send emails as me?
  - id: send_as_delete_by_user
    intent: Revoke send-as for a specific user
    question: Can I revoke send-as permission by naming the user instead of the association?
  - id: send_as_bulk_create
    intent: Allow and disallow many send-as users
    question: Can I update who can send as me for many users in one request?
  - id: send_as_get
    intent: Get a send-as association
    question: How do I look up one send-as association by ID?
  - id: send_as_delete
    intent: Delete a send-as association by ID
    question: Can I delete a send-as permission using its association ID?
  phrasing_ops: 6
  slug: close-send-as-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The sequences API from Close — 4 operation(s) for sequences.
  name: Close Sequences API
  phrasing_intents:
  - id: sequences_list
    intent: List email sequences
    question: What sequences have we set up for automated outreach?
  - id: sequences_create
    intent: Create an outreach sequence
    question: How do I build a new multi-step outreach sequence in Close?
  - id: sequences_get
    intent: Get one sequence's details
    question: Which steps are in a particular sequence?
  - id: sequences_update
    intent: Update a sequence's steps or settings
    question: If I leave out steps when editing a sequence, are they removed?
  - id: sequences_delete
    intent: Delete a sequence
    question: Can I permanently remove a sequence we no longer use?
  - id: sequences_list_subscriptions
    intent: List who is subscribed to sequences
    question: Which contacts are currently enrolled in a given sequence?
  - id: sequences_create_subscription
    intent: Enroll a contact in a sequence
    question: How do I add a single contact to an outreach sequence?
  - id: sequences_get_subscription
    intent: Get one sequence subscription
    question: How can I check the status of one contact's sequence enrollment?
  phrasing_ops: 10
  slug: close-sequences-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The smart_views API from Close — 2 operation(s) for smart_views.
  name: Close Smart Views API
  phrasing_intents:
  - id: smart_views_list
    intent: List Smart Views
    question: What saved Smart Views does our team have?
  - id: smart_views_create
    intent: Create a Smart View
    question: How do I save a lead search as a Smart View?
  - id: smart_views_get
    intent: Get a single Smart View
    question: What query is behind a particular Smart View?
  - id: smart_views_update
    intent: Update a Smart View
    question: Can I change the filters on a saved Smart View?
  - id: smart_views_delete
    intent: Delete a Smart View
    question: Can I delete a Smart View nobody uses?
  phrasing_ops: 5
  slug: close-smart-views-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The sms_templates API from Close — 2 operation(s) for sms_templates.
  name: Close Sms Templates API
  phrasing_intents:
  - id: sms_templates_list
    intent: List SMS templates
    question: Which text message templates do we have?
  - id: sms_templates_create
    intent: Create an SMS template
    question: How do I save a reusable text message template?
  - id: sms_templates_get
    intent: Fetch an SMS template
    question: What does a specific SMS template say?
  - id: sms_templates_update
    intent: Update an SMS template
    question: Can I change the wording of a text template?
  - id: sms_templates_delete
    intent: Delete an SMS template
    question: Can I delete a text template we don't use anymore?
  phrasing_ops: 5
  slug: close-sms-templates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The tasks API from Close — 2 operation(s) for tasks.
  name: Close Tasks API
  phrasing_intents:
  - id: tasks_list
    intent: List or filter tasks
    question: What incomplete tasks are in my inbox for today?
  - id: tasks_create
    intent: Create a task
    question: How do I create a follow-up task on a lead?
  - id: tasks_bulk_update
    intent: Bulk update matching tasks
    question: Can I mark many tasks complete at once?
  - id: tasks_get
    intent: Fetch a task's details
    question: What are the details of a specific task?
  - id: tasks_update
    intent: Update a single task
    question: Can I reschedule or reassign one task?
  - id: tasks_delete
    intent: Delete a task
    question: Can I delete a task instead of completing it?
  phrasing_ops: 6
  slug: close-tasks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The unsubscribed_emails API from Close — 2 operation(s) for unsubscribed_emails.
  name: Close Unsubscribed Emails API
  phrasing_intents:
  - id: unsubscribed_emails_list
    intent: List unsubscribed email addresses
    question: Which email addresses have unsubscribed?
  - id: unsubscribed_emails_create
    intent: Unsubscribe an email address
    question: How do I stop sending emails to someone who opted out elsewhere?
  - id: unsubscribed_emails_delete
    intent: Resubscribe an email address
    question: Can I resubscribe someone who unsubscribed by mistake?
  phrasing_ops: 3
  slug: close-unsubscribed-emails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The users API from Close — 4 operation(s) for users.
  name: Close Users API
  phrasing_intents:
  - id: users_get_me
    intent: Get your own user profile
    question: How do I find my own user ID and organization ID?
  - id: users_list
    intent: List users in the organization
    question: Who are all the users in our organization?
  - id: users_list_availabilities
    intent: See who is available or on a call
    question: Which reps are on a call right now?
  - id: users_get
    intent: Get a single user
    question: How do I look up a teammate's details by user ID?
  phrasing_ops: 4
  slug: close-users-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The webhooks API from Close — 2 operation(s) for webhooks.
  name: Close Webhooks API
  phrasing_intents:
  - id: webhooks_list
    intent: List webhook subscriptions
    question: Which webhooks are set up for our organization?
  - id: webhooks_create
    intent: Subscribe a URL to CRM events
    question: How do I get notified when a lead is created or updated?
  - id: webhooks_get
    intent: Get a webhook subscription
    question: How do I check which events one webhook listens for?
  - id: webhooks_update
    intent: Update or pause a webhook
    question: Can I pause a webhook without deleting it?
  - id: webhooks_delete
    intent: Delete a webhook subscription
    question: What's the way to stop receiving webhook events for good?
  phrasing_ops: 5
  slug: close-webhooks-api
artifact_total: 155
asyncapis:
- description: ''
  name: Close Webhooks
  slug: close-webhooks
collections:
- collection_type: open
  name: API Endpoints subpackage_activities API
  slug: open-close-subpackage-activities-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesCalls API
  slug: open-close-subpackage-activitiescalls-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesCreations API
  slug: open-close-subpackage-activitiescreations-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesCustomActivities API
  slug: open-close-subpackage-activitiescustomactivities-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesEmails API
  slug: open-close-subpackage-activitiesemails-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesEmailThreads API
  slug: open-close-subpackage-activitiesemailthreads-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesFormSubmissions API
  slug: open-close-subpackage-activitiesformsubmissions-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesLeadMerges API
  slug: open-close-subpackage-activitiesleadmerges-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesLeadStatusChanges API
  slug: open-close-subpackage-activitiesleadstatuschanges-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesMeetings API
  slug: open-close-subpackage-activitiesmeetings-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesNotes API
  slug: open-close-subpackage-activitiesnotes-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesOpportunityStatusChanges API
  slug: open-close-subpackage-activitiesopportunitystatuschanges-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesSms API
  slug: open-close-subpackage-activitiessms-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesTaskCompletions API
  slug: open-close-subpackage-activitiestaskcompletions-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_activitiesWhatsappMessages API
  slug: open-close-subpackage-activitieswhatsappmessages-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_blockedPhoneNumbers API
  slug: open-close-subpackage-blockedphonenumbers-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_bulkActionsDelete API
  slug: open-close-subpackage-bulkactionsdelete-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_bulkActionsEdit API
  slug: open-close-subpackage-bulkactionsedit-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_bulkActionsEmail API
  slug: open-close-subpackage-bulkactionsemail-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_bulkActionsSequenceSubscriptions API
  slug: open-close-subpackage-bulkactionssequencesubscriptions-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_comments API
  slug: open-close-subpackage-comments-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_connectedAccounts API
  slug: open-close-subpackage-connectedaccounts-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_contacts API
  slug: open-close-subpackage-contacts-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customActivityTypes API
  slug: open-close-subpackage-customactivitytypes-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsActivity API
  slug: open-close-subpackage-customfieldsactivity-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldSchemas API
  slug: open-close-subpackage-customfieldschemas-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsContact API
  slug: open-close-subpackage-customfieldscontact-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsCustomObject API
  slug: open-close-subpackage-customfieldscustomobject-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsLead API
  slug: open-close-subpackage-customfieldslead-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsOpportunity API
  slug: open-close-subpackage-customfieldsopportunity-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customFieldsShared API
  slug: open-close-subpackage-customfieldsshared-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customObjects API
  slug: open-close-subpackage-customobjects-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_customObjectTypes API
  slug: open-close-subpackage-customobjecttypes-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_dialers API
  slug: open-close-subpackage-dialers-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_emailTemplates API
  slug: open-close-subpackage-emailtemplates-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_events API
  slug: open-close-subpackage-events-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_exports API
  slug: open-close-subpackage-exports-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_fieldEnrichment API
  slug: open-close-subpackage-fieldenrichment-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_files API
  slug: open-close-subpackage-files-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_groups API
  slug: open-close-subpackage-groups-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_integrationLinks API
  slug: open-close-subpackage-integrationlinks-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_leads API
  slug: open-close-subpackage-leads-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_leadStatuses API
  slug: open-close-subpackage-leadstatuses-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_memberships API
  slug: open-close-subpackage-memberships-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_opportunities API
  slug: open-close-subpackage-opportunities-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_opportunityStatuses API
  slug: open-close-subpackage-opportunitystatuses-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_organizations API
  slug: open-close-subpackage-organizations-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_outcomes API
  slug: open-close-subpackage-outcomes-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_phoneNumbers API
  slug: open-close-subpackage-phonenumbers-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_pipelines API
  slug: open-close-subpackage-pipelines-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_playbooks API
  slug: open-close-subpackage-playbooks-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_reporting API
  slug: open-close-subpackage-reporting-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_roles API
  slug: open-close-subpackage-roles-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_schedulingLinks API
  slug: open-close-subpackage-schedulinglinks-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_sendAs API
  slug: open-close-subpackage-sendas-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_sequences API
  slug: open-close-subpackage-sequences-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_smartViews API
  slug: open-close-subpackage-smartviews-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_smsTemplates API
  slug: open-close-subpackage-smstemplates-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_tasks API
  slug: open-close-subpackage-tasks-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_unsubscribedEmails API
  slug: open-close-subpackage-unsubscribedemails-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_users API
  slug: open-close-subpackage-users-api
- collection_type: open
  name: API Endpoints subpackage_activities subpackage_webhooks API
  slug: open-close-subpackage-webhooks-api
- collection_type: open
  name: API Endpoints
  slug: open-close
common:
- group: other
  href: https://artifacts.apis.io/close/capabilities/close-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/close-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/close/agentic-access/close-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/close-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/close/security/close-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/close-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/close/security/close-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/close-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/close/authentication/close-authentication.yml
  title: ''
  type: Authentication
  url: authentication/close-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/close-crm
- group: company
  title: ''
  type: Website
  url: https://www.close.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.close.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.close.com/api/resources/leads
- group: commercial
  title: ''
  type: Pricing
  url: https://www.close.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.close.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.close.com/
- group: company
  title: ''
  type: Blog
  url: https://www.close.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.close.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/closeio
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.close.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.close.com/terms
- group: auth
  title: ''
  type: Authentication
  url: https://developer.close.com/api/overview/api-key-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.close.com/api/overview/rate-limits.md
- group: design
  title: ''
  type: Webhooks
  url: https://developer.close.com/api/resources/webhooks
- group: commercial
  href: https://artifacts.apis.io/close/plans/close-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/close-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/close/rate-limits/close-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/close-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/close/finops/close-finops.yml
  title: ''
  type: FinOps
  url: finops/close-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.close.com/llms.txt
- group: docs
  href: https://artifacts.apis.io/close/openapi/_original/close-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/close-api-openapi.json
- group: build
  href: https://artifacts.apis.io/close/packages/close-packages.yml
  title: ''
  type: Packages
  url: packages/close-packages.yml
- group: build
  href: https://artifacts.apis.io/close/packages/close-packages.yml
  title: ''
  type: SDKs
  url: packages/close-packages.yml
- group: agent
  href: https://artifacts.apis.io/close/mcp/close-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/close-mcp.yml
- group: build
  href: https://artifacts.apis.io/close/mcp/close-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/close-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/close/well-known/close-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/close-well-known.yml
- group: other
  href: https://artifacts.apis.io/close/well-known/close-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/close-robots.txt
- group: agent
  href: https://artifacts.apis.io/close/llms/close-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/close-llms.txt
- group: other
  href: https://artifacts.apis.io/close/overlays/close-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/close-api-overlay.yaml
- group: design
  href: https://artifacts.apis.io/close/conformance/close-conformance.yml
  title: ''
  type: Conformance
  url: conformance/close-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://close.com/security
- group: design
  href: https://artifacts.apis.io/close/errors/close-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/close-problem-types.yml
- group: design
  href: https://artifacts.apis.io/close/lifecycle/close-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/close-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.close.com/api/overview/changelog
- group: operate
  href: https://artifacts.apis.io/close/changelog/close-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/close-changelog.yml
- group: auth
  href: https://artifacts.apis.io/close/scopes/close-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/close-scopes.yml
- group: design
  href: https://artifacts.apis.io/close/conventions/close-conventions.yml
  title: ''
  type: Conventions
  url: conventions/close-conventions.yml
- group: design
  href: https://artifacts.apis.io/close/data-model/close-data-model.yml
  title: ''
  type: DataModel
  url: data-model/close-data-model.yml
- group: design
  href: https://artifacts.apis.io/close/components/close-components.yml
  title: ''
  type: Components
  url: components/close-components.yml
- group: auth
  href: https://artifacts.apis.io/close/security/close-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/close-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://close.com/security/submit-report
- group: design
  href: https://artifacts.apis.io/close/asyncapi/close-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/close-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/close/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.close.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.close.com/api/overview
- group: start
  title: ''
  type: SignUp
  url: https://app.close.com/signup/
- group: operate
  title: ''
  type: Roadmap
  url: https://close.com/changelog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.close.com/
created: '2026-05-08'
description: Close is an inside-sales CRM with calling, email, SMS, and WhatsApp built in. The Close API exposes leads, contacts, opportunities, tasks, activities (calls, emails, SMS, meetings, notes), pipelines, custom objects, sequences, smart views, scheduling, phone numbers, reporting, and webhooks for sales automation.
features:
- REST API at https://api.close.com/api/v1/
- HTTP Basic auth with API key, plus OAuth 2.0 for marketplace apps
- Solo $9/mo, Essentials $35, Growth $99, Scale $139 per seat (annual)
- Premium phone numbers $19/mo per line
- AI Call Assistant $50/month + $0.02/min
- Additional organizations $50/mo (1 included with Growth/Scale)
- Per-endpoint-group rate limits; org limits 3x individual key limits
- RateLimit header (limit / remaining / reset) on every response
- 30-day Event Log for change tracking
- Webhooks with advanced filtering and HMAC-signed deliveries
finops:
- has_sources: true
  method: derived
  name: Close Finops
  primary_unit: user
  service_category: ''
  slug: close-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/close.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.close.com over HTTP requiring OAuth; 107 tools listed.
  name: Close MCP Server
  slug: close
modified: '2026-08-13'
name: Close
nav: Providers
network: true
overview: 'Close publishes 64 API contracts indexed on the [APIs.io](https://apis.io/) network, including Activities API, Activities.calls API, Activities.creations API, and 61 more. Tagged areas include CRM, Sales Engagement, Inside Sales, Calling, and SMS.


  The Close catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Close''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, changelog, and 45 more developer resources.'
plans:
- name: Close Plans Pricing
  plan_count: 11
  slug: close-plans-pricing
- name: Close Price Estimates
  plan_count: 0
  slug: close-price-estimates
random_paper: 6
rate_limits:
- limit_count: 4
  name: Close Rate Limits
  slug: close-rate-limits
rules:
- authorship: generated
  effective_rule_count: 95
  extends:
  - spectral:oas
  name: Close API Rules
  rule_count: 54
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 7
  slug: close-rules
scopes:
- name: Close Scopes
  scope_count: 5
  slug: close-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 78.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.4
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 64.8
    developer_ergonomics: 66.1
    discoverability: 75.0
    operational_transparency: 97.4
  previous_composite: 76.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 64
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/close/close-2026-06-20T174533.png
security:
- kind: authentication
  name: Close Authentication
  slug: close-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: domain-security
  name: Close Domain Security
  slug: close-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Close Vulnerability Disclosure
  slug: close-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Close Trust Center
  slug: close-trust-center
  summary_line: SOC 2 Type 2, GDPR, CCPA
skill_count: 5
skills:
- name: Page through and bulk-extract Close data without hitting the ceilings
  slug: close-bulk-extract-and-paginate
- name: Connect an agent to the Close MCP server at the right privilege level
  slug: close-connect-the-mcp-server
- name: Create a Close lead and log the first touch
  slug: close-create-lead-and-log-first-touch
- name: Open and advance a Close opportunity through a pipeline
  slug: close-manage-opportunity-pipeline
- name: Subscribe to Close webhooks and verify deliveries
  slug: close-subscribe-to-webhooks
slug: close
tags:
- CRM
- Sales Engagement
- Inside Sales
- Calling
- SMS
- WhatsApp
- Sales Automation
- Pipeline Management
- AI Agents
- MCP
- Webhook
- Software-as-a-Service
website: https://www.close.com/
---
