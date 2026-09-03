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
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.2
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 160
  human_in_the_loop: 0
  name: Close Agentic Access
  operation_count: 286
  slug: close-agentic-access
  summary_line: 286 operations · 160 acting
api_count: 2
apis:
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activities API from Close — 1 operation(s) for subpackage_activities.
  name: Close subpackage_activities API
  slug: close-subpackage-activities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesCalls API from Close — 2 operation(s) for subpackage_activitiescalls.
  name: Close subpackage_activitiesCalls API
  slug: close-subpackage-activitiescalls-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesCreations API from Close — 2 operation(s) for subpackage_activitiescreations.
  name: Close subpackage_activitiesCreations API
  slug: close-subpackage-activitiescreations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesCustomActivities API from Close — 2 operation(s) for subpackage_activitiescustomactivities.
  name: Close subpackage_activitiesCustomActivities API
  slug: close-subpackage-activitiescustomactivities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesEmails API from Close — 2 operation(s) for subpackage_activitiesemails.
  name: Close subpackage_activitiesEmails API
  slug: close-subpackage-activitiesemails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesEmailThreads API from Close — 2 operation(s) for subpackage_activitiesemailthreads.
  name: Close subpackage_activitiesEmailThreads API
  slug: close-subpackage-activitiesemailthreads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesFormSubmissions API from Close — 2 operation(s) for subpackage_activitiesformsubmissions.
  name: Close subpackage_activitiesFormSubmissions API
  slug: close-subpackage-activitiesformsubmissions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesLeadMerges API from Close — 2 operation(s) for subpackage_activitiesleadmerges.
  name: Close subpackage_activitiesLeadMerges API
  slug: close-subpackage-activitiesleadmerges-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesLeadStatusChanges API from Close — 2 operation(s) for subpackage_activitiesleadstatuschanges.
  name: Close subpackage_activitiesLeadStatusChanges API
  slug: close-subpackage-activitiesleadstatuschanges-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesMeetings API from Close — 3 operation(s) for subpackage_activitiesmeetings.
  name: Close subpackage_activitiesMeetings API
  slug: close-subpackage-activitiesmeetings-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesNotes API from Close — 2 operation(s) for subpackage_activitiesnotes.
  name: Close subpackage_activitiesNotes API
  slug: close-subpackage-activitiesnotes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesOpportunityStatusChanges API from Close — 2 operation(s) for subpackage_activitiesopportunitystatuschanges.
  name: Close subpackage_activitiesOpportunityStatusChanges API
  slug: close-subpackage-activitiesopportunitystatuschanges-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesSms API from Close — 2 operation(s) for subpackage_activitiessms.
  name: Close subpackage_activitiesSms API
  slug: close-subpackage-activitiessms-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesTaskCompletions API from Close — 2 operation(s) for subpackage_activitiestaskcompletions.
  name: Close subpackage_activitiesTaskCompletions API
  slug: close-subpackage-activitiestaskcompletions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_activitiesWhatsappMessages API from Close — 2 operation(s) for subpackage_activitieswhatsappmessages.
  name: Close subpackage_activitiesWhatsappMessages API
  slug: close-subpackage-activitieswhatsappmessages-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_blockedPhoneNumbers API from Close — 3 operation(s) for subpackage_blockedphonenumbers.
  name: Close subpackage_blockedPhoneNumbers API
  slug: close-subpackage-blockedphonenumbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_bulkActionsDelete API from Close — 2 operation(s) for subpackage_bulkactionsdelete.
  name: Close subpackage_bulkActionsDelete API
  slug: close-subpackage-bulkactionsdelete-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_bulkActionsEdit API from Close — 2 operation(s) for subpackage_bulkactionsedit.
  name: Close subpackage_bulkActionsEdit API
  slug: close-subpackage-bulkactionsedit-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_bulkActionsEmail API from Close — 2 operation(s) for subpackage_bulkactionsemail.
  name: Close subpackage_bulkActionsEmail API
  slug: close-subpackage-bulkactionsemail-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_bulkActionsSequenceSubscriptions API from Close — 2 operation(s) for subpackage_bulkactionssequencesubscriptions.
  name: Close subpackage_bulkActionsSequenceSubscriptions API
  slug: close-subpackage-bulkactionssequencesubscriptions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_comments API from Close — 4 operation(s) for subpackage_comments.
  name: Close subpackage_comments API
  slug: close-subpackage-comments-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_connectedAccounts API from Close — 2 operation(s) for subpackage_connectedaccounts.
  name: Close subpackage_connectedAccounts API
  slug: close-subpackage-connectedaccounts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_contacts API from Close — 2 operation(s) for subpackage_contacts.
  name: Close subpackage_contacts API
  slug: close-subpackage-contacts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customActivityTypes API from Close — 2 operation(s) for subpackage_customactivitytypes.
  name: Close subpackage_customActivityTypes API
  slug: close-subpackage-customactivitytypes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsActivity API from Close — 2 operation(s) for subpackage_customfieldsactivity.
  name: Close subpackage_customFieldsActivity API
  slug: close-subpackage-customfieldsactivity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldSchemas API from Close — 1 operation(s) for subpackage_customfieldschemas.
  name: Close subpackage_customFieldSchemas API
  slug: close-subpackage-customfieldschemas-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsContact API from Close — 2 operation(s) for subpackage_customfieldscontact.
  name: Close subpackage_customFieldsContact API
  slug: close-subpackage-customfieldscontact-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsCustomObject API from Close — 2 operation(s) for subpackage_customfieldscustomobject.
  name: Close subpackage_customFieldsCustomObject API
  slug: close-subpackage-customfieldscustomobject-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsLead API from Close — 2 operation(s) for subpackage_customfieldslead.
  name: Close subpackage_customFieldsLead API
  slug: close-subpackage-customfieldslead-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsOpportunity API from Close — 2 operation(s) for subpackage_customfieldsopportunity.
  name: Close subpackage_customFieldsOpportunity API
  slug: close-subpackage-customfieldsopportunity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customFieldsShared API from Close — 4 operation(s) for subpackage_customfieldsshared.
  name: Close subpackage_customFieldsShared API
  slug: close-subpackage-customfieldsshared-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customObjects API from Close — 2 operation(s) for subpackage_customobjects.
  name: Close subpackage_customObjects API
  slug: close-subpackage-customobjects-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_customObjectTypes API from Close — 2 operation(s) for subpackage_customobjecttypes.
  name: Close subpackage_customObjectTypes API
  slug: close-subpackage-customobjecttypes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_dialers API from Close — 2 operation(s) for subpackage_dialers.
  name: Close subpackage_dialers API
  slug: close-subpackage-dialers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_emailTemplates API from Close — 3 operation(s) for subpackage_emailtemplates.
  name: Close subpackage_emailTemplates API
  slug: close-subpackage-emailtemplates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_events API from Close — 2 operation(s) for subpackage_events.
  name: Close subpackage_events API
  slug: close-subpackage-events-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_exports API from Close — 4 operation(s) for subpackage_exports.
  name: Close subpackage_exports API
  slug: close-subpackage-exports-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_fieldEnrichment API from Close — 1 operation(s) for subpackage_fieldenrichment.
  name: Close subpackage_fieldEnrichment API
  slug: close-subpackage-fieldenrichment-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_files API from Close — 1 operation(s) for subpackage_files.
  name: Close subpackage_files API
  slug: close-subpackage-files-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_groups API from Close — 4 operation(s) for subpackage_groups.
  name: Close subpackage_groups API
  slug: close-subpackage-groups-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_integrationLinks API from Close — 2 operation(s) for subpackage_integrationlinks.
  name: Close subpackage_integrationLinks API
  slug: close-subpackage-integrationlinks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_leads API from Close — 3 operation(s) for subpackage_leads.
  name: Close subpackage_leads API
  slug: close-subpackage-leads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_leadStatuses API from Close — 2 operation(s) for subpackage_leadstatuses.
  name: Close subpackage_leadStatuses API
  slug: close-subpackage-leadstatuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_memberships API from Close — 3 operation(s) for subpackage_memberships.
  name: Close subpackage_memberships API
  slug: close-subpackage-memberships-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_opportunities API from Close — 2 operation(s) for subpackage_opportunities.
  name: Close subpackage_opportunities API
  slug: close-subpackage-opportunities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_opportunityStatuses API from Close — 2 operation(s) for subpackage_opportunitystatuses.
  name: Close subpackage_opportunityStatuses API
  slug: close-subpackage-opportunitystatuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_organizations API from Close — 1 operation(s) for subpackage_organizations.
  name: Close subpackage_organizations API
  slug: close-subpackage-organizations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_outcomes API from Close — 2 operation(s) for subpackage_outcomes.
  name: Close subpackage_outcomes API
  slug: close-subpackage-outcomes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_phoneNumbers API from Close — 3 operation(s) for subpackage_phonenumbers.
  name: Close subpackage_phoneNumbers API
  slug: close-subpackage-phonenumbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_pipelines API from Close — 2 operation(s) for subpackage_pipelines.
  name: Close subpackage_pipelines API
  slug: close-subpackage-pipelines-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_playbooks API from Close — 4 operation(s) for subpackage_playbooks.
  name: Close subpackage_playbooks API
  slug: close-subpackage-playbooks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_reporting API from Close — 8 operation(s) for subpackage_reporting.
  name: Close subpackage_reporting API
  slug: close-subpackage-reporting-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_roles API from Close — 2 operation(s) for subpackage_roles.
  name: Close subpackage_roles API
  slug: close-subpackage-roles-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_schedulingLinks API from Close — 8 operation(s) for subpackage_schedulinglinks.
  name: Close subpackage_schedulingLinks API
  slug: close-subpackage-schedulinglinks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_sendAs API from Close — 3 operation(s) for subpackage_sendas.
  name: Close subpackage_sendAs API
  slug: close-subpackage-sendas-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_sequences API from Close — 4 operation(s) for subpackage_sequences.
  name: Close subpackage_sequences API
  slug: close-subpackage-sequences-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_smartViews API from Close — 2 operation(s) for subpackage_smartviews.
  name: Close subpackage_smartViews API
  slug: close-subpackage-smartviews-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_smsTemplates API from Close — 2 operation(s) for subpackage_smstemplates.
  name: Close subpackage_smsTemplates API
  slug: close-subpackage-smstemplates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_tasks API from Close — 2 operation(s) for subpackage_tasks.
  name: Close subpackage_tasks API
  slug: close-subpackage-tasks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_unsubscribedEmails API from Close — 2 operation(s) for subpackage_unsubscribedemails.
  name: Close subpackage_unsubscribedEmails API
  slug: close-subpackage-unsubscribedemails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_users API from Close — 4 operation(s) for subpackage_users.
  name: Close subpackage_users API
  slug: close-subpackage-users-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The subpackage_webhooks API from Close — 2 operation(s) for subpackage_webhooks.
  name: Close subpackage_webhooks API
  slug: close-subpackage-webhooks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities API from Close — 1 operation(s) for activities.
  name: Close Activities API
  slug: close-activities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.calls API from Close — 2 operation(s) for activities.calls.
  name: Close Activities.calls API
  slug: close-activities-calls-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.creations API from Close — 2 operation(s) for activities.creations.
  name: Close Activities.creations API
  slug: close-activities-creations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.custom_activities API from Close — 2 operation(s) for activities.custom_activities.
  name: Close Activities.custom Activities API
  slug: close-activities-custom-activities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.email_threads API from Close — 2 operation(s) for activities.email_threads.
  name: Close Activities.email Threads API
  slug: close-activities-email-threads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.emails API from Close — 2 operation(s) for activities.emails.
  name: Close Activities.emails API
  slug: close-activities-emails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.form_submissions API from Close — 2 operation(s) for activities.form_submissions.
  name: Close Activities.form Submissions API
  slug: close-activities-form-submissions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.import_updates API from Close — 2 operation(s) for activities.import_updates.
  name: Close Activities.import Updates API
  slug: close-activities-import-updates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.lead_merges API from Close — 2 operation(s) for activities.lead_merges.
  name: Close Activities.lead Merges API
  slug: close-activities-lead-merges-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.lead_status_changes API from Close — 2 operation(s) for activities.lead_status_changes.
  name: Close Activities.lead Status Changes API
  slug: close-activities-lead-status-changes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.meetings API from Close — 3 operation(s) for activities.meetings.
  name: Close Activities.meetings API
  slug: close-activities-meetings-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.notes API from Close — 2 operation(s) for activities.notes.
  name: Close Activities.notes API
  slug: close-activities-notes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.opportunity_status_changes API from Close — 2 operation(s) for activities.opportunity_status_changes.
  name: Close Activities.opportunity Status Changes API
  slug: close-activities-opportunity-status-changes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.sms API from Close — 2 operation(s) for activities.sms.
  name: Close Activities.sms API
  slug: close-activities-sms-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.task_completions API from Close — 2 operation(s) for activities.task_completions.
  name: Close Activities.task Completions API
  slug: close-activities-task-completions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The activities.whatsapp_messages API from Close — 2 operation(s) for activities.whatsapp_messages.
  name: Close Activities.whatsapp Messages API
  slug: close-activities-whatsapp-messages-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The blocked_phone_numbers API from Close — 3 operation(s) for blocked_phone_numbers.
  name: Close Blocked Phone Numbers API
  slug: close-blocked-phone-numbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.delete API from Close — 2 operation(s) for bulk_actions.delete.
  name: Close Bulk Actions.delete API
  slug: close-bulk-actions-delete-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.edit API from Close — 2 operation(s) for bulk_actions.edit.
  name: Close Bulk Actions.edit API
  slug: close-bulk-actions-edit-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.email API from Close — 2 operation(s) for bulk_actions.email.
  name: Close Bulk Actions.email API
  slug: close-bulk-actions-email-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The bulk_actions.sequence_subscriptions API from Close — 2 operation(s) for bulk_actions.sequence_subscriptions.
  name: Close Bulk Actions.sequence Subscriptions API
  slug: close-bulk-actions-sequence-subscriptions-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The comments API from Close — 4 operation(s) for comments.
  name: Close Comments API
  slug: close-comments-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The connected_accounts API from Close — 2 operation(s) for connected_accounts.
  name: Close Connected Accounts API
  slug: close-connected-accounts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The contacts API from Close — 2 operation(s) for contacts.
  name: Close Contacts API
  slug: close-contacts-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_activity_types API from Close — 2 operation(s) for custom_activity_types.
  name: Close Custom Activity Types API
  slug: close-custom-activity-types-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_field_schemas API from Close — 1 operation(s) for custom_field_schemas.
  name: Close Custom Field Schemas API
  slug: close-custom-field-schemas-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.activity API from Close — 2 operation(s) for custom_fields.activity.
  name: Close Custom Fields.activity API
  slug: close-custom-fields-activity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.contact API from Close — 2 operation(s) for custom_fields.contact.
  name: Close Custom Fields.contact API
  slug: close-custom-fields-contact-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.custom_object API from Close — 2 operation(s) for custom_fields.custom_object.
  name: Close Custom Fields.custom Object API
  slug: close-custom-fields-custom-object-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.lead API from Close — 2 operation(s) for custom_fields.lead.
  name: Close Custom Fields.lead API
  slug: close-custom-fields-lead-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.opportunity API from Close — 2 operation(s) for custom_fields.opportunity.
  name: Close Custom Fields.opportunity API
  slug: close-custom-fields-opportunity-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_fields.shared API from Close — 4 operation(s) for custom_fields.shared.
  name: Close Custom Fields.shared API
  slug: close-custom-fields-shared-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_object_types API from Close — 2 operation(s) for custom_object_types.
  name: Close Custom Object Types API
  slug: close-custom-object-types-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The custom_objects API from Close — 2 operation(s) for custom_objects.
  name: Close Custom Objects API
  slug: close-custom-objects-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The dialers API from Close — 2 operation(s) for dialers.
  name: Close Dialers API
  slug: close-dialers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The email_templates API from Close — 3 operation(s) for email_templates.
  name: Close Email Templates API
  slug: close-email-templates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The events API from Close — 2 operation(s) for events.
  name: Close Events API
  slug: close-events-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The exports API from Close — 6 operation(s) for exports.
  name: Close Exports API
  slug: close-exports-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The field_enrichment API from Close — 1 operation(s) for field_enrichment.
  name: Close Field Enrichment API
  slug: close-field-enrichment-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The files API from Close — 1 operation(s) for files.
  name: Close Files API
  slug: close-files-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The forms API from Close — 2 operation(s) for forms.
  name: Close Forms API
  slug: close-forms-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The groups API from Close — 4 operation(s) for groups.
  name: Close Groups API
  slug: close-groups-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The integration_links API from Close — 2 operation(s) for integration_links.
  name: Close Integration Links API
  slug: close-integration-links-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The lead_statuses API from Close — 2 operation(s) for lead_statuses.
  name: Close Lead Statuses API
  slug: close-lead-statuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The leads API from Close — 3 operation(s) for leads.
  name: Close Leads API
  slug: close-leads-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The memberships API from Close — 3 operation(s) for memberships.
  name: Close Memberships API
  slug: close-memberships-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The opportunities API from Close — 2 operation(s) for opportunities.
  name: Close Opportunities API
  slug: close-opportunities-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The opportunity_statuses API from Close — 2 operation(s) for opportunity_statuses.
  name: Close Opportunity Statuses API
  slug: close-opportunity-statuses-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The organizations API from Close — 1 operation(s) for organizations.
  name: Close Organizations API
  slug: close-organizations-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The outcomes API from Close — 2 operation(s) for outcomes.
  name: Close Outcomes API
  slug: close-outcomes-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The phone_numbers API from Close — 3 operation(s) for phone_numbers.
  name: Close Phone Numbers API
  slug: close-phone-numbers-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The pipelines API from Close — 2 operation(s) for pipelines.
  name: Close Pipelines API
  slug: close-pipelines-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The playbooks API from Close — 4 operation(s) for playbooks.
  name: Close Playbooks API
  slug: close-playbooks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The reporting API from Close — 8 operation(s) for reporting.
  name: Close Reporting API
  slug: close-reporting-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The roles API from Close — 2 operation(s) for roles.
  name: Close Roles API
  slug: close-roles-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The scheduling_links API from Close — 8 operation(s) for scheduling_links.
  name: Close Scheduling Links API
  slug: close-scheduling-links-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The send_as API from Close — 3 operation(s) for send_as.
  name: Close Send As API
  slug: close-send-as-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The sequences API from Close — 4 operation(s) for sequences.
  name: Close Sequences API
  slug: close-sequences-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The smart_views API from Close — 2 operation(s) for smart_views.
  name: Close Smart Views API
  slug: close-smart-views-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The sms_templates API from Close — 2 operation(s) for sms_templates.
  name: Close Sms Templates API
  slug: close-sms-templates-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The tasks API from Close — 2 operation(s) for tasks.
  name: Close Tasks API
  slug: close-tasks-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The unsubscribed_emails API from Close — 2 operation(s) for unsubscribed_emails.
  name: Close Unsubscribed Emails API
  slug: close-unsubscribed-emails-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The users API from Close — 4 operation(s) for users.
  name: Close Users API
  slug: close-users-api
- baseURL: https://api.close.com/api/v1
  baseurl_source: declared
  description: The webhooks API from Close — 2 operation(s) for webhooks.
  name: Close Webhooks API
  slug: close-webhooks-api
artifact_total: 211
asyncapis:
- description: ''
  name: Close Webhooks
  slug: close-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: CapabilityMap
  url: capabilities/close-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/close-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/close-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/close-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/close-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/close-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/close-finops.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.close.com/llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/close-api-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/close-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/close-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/close-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/close-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/close-well-known.yml
- group: other
  title: ''
  type: ContentSignal
  url: well-known/close-robots.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/close-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/close-api-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/close-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://close.com/security
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/close-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/close-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.close.com/api/overview/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/close-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/close-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/close-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/close-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/close-components.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/close-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://close.com/security/submit-report
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/close-webhooks.yml
- group: agent
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
- name: Close Finops
  service_category: CRM
  slug: close-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/close.png
layout: provider
mcp_servers:
- description: ''
  name: Close MCP Server
  slug: close-mcp-server
modified: '2026-08-13'
name: Close
nav: Providers
network: true
overview: 'Close publishes 126 APIs on the [APIs.io](https://apis.io/) network, including subpackage_activities API, subpackage_activitiesCalls API, subpackage_activitiesCreations API, and 123 more. Tagged areas include CRM, Sales Engagement, Inside Sales, Calling, and SMS.


  The Close catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Close''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, changelog, and 45 more developer resources.'
plans:
- name: Close Plans Pricing
  plan_count: 7
  slug: close-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Close Rate Limits
  slug: close-rate-limits
scopes:
- name: Close Scopes
  scope_count: 5
  slug: close-scopes
  summary_line: 5 scopes · authorizationCode
score:
  band: exemplar
  composite: 76.2
  coverage:
    artifact_dirs: 26
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 18.2
    contract_quality: 63.1
    developer_ergonomics: 66.1
    discoverability: 70.4
    governance: 18.2
    operational_transparency: 97.4
  previous_composite: 76.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 126
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
    score: 73.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/close/refs/heads/main/screenshots/close-2026-06-20T174533.png
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
