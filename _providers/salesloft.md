---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.9
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 73
  human_in_the_loop: 4
  name: Salesloft Agentic Access
  operation_count: 176
  slug: salesloft-agentic-access
  summary_line: 176 operations · 73 acting · 4 human-in-the-loop
api_count: 1
apis:
- description: REST API for cadences, people, accounts, emails, calls, tasks, opportunities and analytics.
  name: Salesloft Platform API
  slug: salesloft-platform-api
- description: 'First-party remote Model Context Protocol server exposing fifteen read-only tools over Salesloft accounts, people, users, opportunities, conversations and team data. OAuth 2.1 protected resource with '
  name: Salesloft MCP Server
  slug: salesloft-mcp-server
- description: Subscribe to platform events for real-time updates.
  name: Salesloft Webhooks API
  slug: salesloft-webhooks-api
- description: '[https://developer.salesloft.com/docs/api/account-and-people-redaction/](https://developer.salesloft.com/docs/api/account-and-people-redaction/)'
  name: Salesloft Account and People Redaction API
  slug: salesloft-account-and-people-redaction-api
- description: '[https://developer.salesloft.com/docs/api/account-redaction/](https://developer.salesloft.com/docs/api/account-redaction/)'
  name: Salesloft Account Redaction API
  slug: salesloft-account-redaction-api
- description: '[https://developer.salesloft.com/docs/api/account-stages/](https://developer.salesloft.com/docs/api/account-stages/)'
  name: Salesloft Account Stages API
  slug: salesloft-account-stages-api
- description: '[https://developer.salesloft.com/docs/api/account-team-member-roles-index/](https://developer.salesloft.com/docs/api/account-team-member-roles-index/)'
  name: Salesloft Account Team Member Roles API
  slug: salesloft-account-team-member-roles-api
- description: '[https://developer.salesloft.com/docs/api/account-tiers/](https://developer.salesloft.com/docs/api/account-tiers/)'
  name: Salesloft Account Tiers API
  slug: salesloft-account-tiers-api
- description: '[https://developer.salesloft.com/docs/api/account-upserts/](https://developer.salesloft.com/docs/api/account-upserts/)'
  name: Salesloft Account Upserts API
  slug: salesloft-account-upserts-api
- description: '[https://developer.salesloft.com/docs/api/accounts/](https://developer.salesloft.com/docs/api/accounts/)'
  name: Salesloft Accounts API
  slug: salesloft-accounts-api
- description: '[https://developer.salesloft.com/docs/api/actions/](https://developer.salesloft.com/docs/api/actions/)'
  name: Salesloft Actions API
  slug: salesloft-actions-api
- description: '[https://developer.salesloft.com/docs/api/activities/](https://developer.salesloft.com/docs/api/activities/)'
  name: Salesloft Activities API
  slug: salesloft-activities-api
- description: '[https://developer.salesloft.com/docs/api/activity-histories/](https://developer.salesloft.com/docs/api/activity-histories/)'
  name: Salesloft Activity Histories API
  slug: salesloft-activity-histories-api
- description: '[https://developer.salesloft.com/docs/api/bulk-jobs/](https://developer.salesloft.com/docs/api/bulk-jobs/)'
  name: Salesloft Bulk Jobs API
  slug: salesloft-bulk-jobs-api
- description: '[https://developer.salesloft.com/docs/api/bulk-jobs-job-data/](https://developer.salesloft.com/docs/api/bulk-jobs-job-data/)'
  name: Salesloft Bulk Jobs - Job Data API
  slug: salesloft-bulk-jobs-job-data-api
- description: '[https://developer.salesloft.com/docs/api/bulk-jobs-results/](https://developer.salesloft.com/docs/api/bulk-jobs-results/)'
  name: Salesloft Bulk Jobs - Results API
  slug: salesloft-bulk-jobs-results-api
- description: '[https://developer.salesloft.com/docs/api/bulk-reschedule-tasks/](https://developer.salesloft.com/docs/api/bulk-reschedule-tasks/)'
  name: Salesloft Bulk Reschedule Tasks API
  slug: salesloft-bulk-reschedule-tasks-api
- description: '[https://developer.salesloft.com/docs/api/cadence-exports/](https://developer.salesloft.com/docs/api/cadence-exports/)'
  name: Salesloft Cadence Exports API
  slug: salesloft-cadence-exports-api
- description: '[https://developer.salesloft.com/docs/api/cadence-imports/](https://developer.salesloft.com/docs/api/cadence-imports/)'
  name: Salesloft Cadence Imports API
  slug: salesloft-cadence-imports-api
- description: '[https://developer.salesloft.com/docs/api/cadence-memberships/](https://developer.salesloft.com/docs/api/cadence-memberships/)'
  name: Salesloft Cadence Memberships API
  slug: salesloft-cadence-memberships-api
- description: '[https://developer.salesloft.com/docs/api/cadence-stats/](https://developer.salesloft.com/docs/api/cadence-stats/)'
  name: Salesloft Cadence Stats API
  slug: salesloft-cadence-stats-api
- description: '[https://developer.salesloft.com/docs/api/cadences/](https://developer.salesloft.com/docs/api/cadences/)'
  name: Salesloft Cadences API
  slug: salesloft-cadences-api
- description: '[https://developer.salesloft.com/docs/api/calendar-events/](https://developer.salesloft.com/docs/api/calendar-events/)'
  name: Salesloft Calendar Events API
  slug: salesloft-calendar-events-api
- description: '[https://developer.salesloft.com/docs/api/call-data-records/](https://developer.salesloft.com/docs/api/call-data-records/)'
  name: Salesloft Call Data Records API
  slug: salesloft-call-data-records-api
- description: '[https://developer.salesloft.com/docs/api/call-dispositions/](https://developer.salesloft.com/docs/api/call-dispositions/)'
  name: Salesloft Call Dispositions API
  slug: salesloft-call-dispositions-api
- description: '[https://developer.salesloft.com/docs/api/call-instructions/](https://developer.salesloft.com/docs/api/call-instructions/)'
  name: Salesloft Call Instructions API
  slug: salesloft-call-instructions-api
- description: '[https://developer.salesloft.com/docs/api/call-sentiments/](https://developer.salesloft.com/docs/api/call-sentiments/)'
  name: Salesloft Call Sentiments API
  slug: salesloft-call-sentiments-api
- description: '[https://developer.salesloft.com/docs/api/caller-ids/](https://developer.salesloft.com/docs/api/caller-ids/)'
  name: Salesloft Caller Ids API
  slug: salesloft-caller-ids-api
- description: '[https://developer.salesloft.com/docs/api/calls/](https://developer.salesloft.com/docs/api/calls/)'
  name: Salesloft Calls API
  slug: salesloft-calls-api
- description: OAuth 2.0 token endpoint for private Salesloft applications using the client credentials grant. POST /oauth/token on the Salesloft accounts host, not on the v2 API host.
  name: Salesloft Client Credentials Access Token API
  slug: salesloft-client-credentials-access-token-api
- description: '[https://developer.salesloft.com/docs/api/conversations/](https://developer.salesloft.com/docs/api/conversations/)'
  name: Salesloft Conversations API
  slug: salesloft-conversations-api
- description: '[https://developer.salesloft.com/docs/api/conversations-calls/](https://developer.salesloft.com/docs/api/conversations-calls/)'
  name: Salesloft Conversations Calls API
  slug: salesloft-conversations-calls-api
- description: '[https://developer.salesloft.com/docs/api/counts/](https://developer.salesloft.com/docs/api/counts/)'
  name: Salesloft Counts API
  slug: salesloft-counts-api
- description: '[https://developers.salesloft.com/docs/api/crm-account-team-members/](https://developers.salesloft.com/docs/api/crm-account-team-members/)'
  name: Salesloft Crm Account Team Members API
  slug: salesloft-crm-account-team-members-api
- description: '[https://developer.salesloft.com/docs/api/crm-activities/](https://developer.salesloft.com/docs/api/crm-activities/)'
  name: Salesloft Crm Activities API
  slug: salesloft-crm-activities-api
- description: '[https://developer.salesloft.com/docs/api/crm-activity-fields/](https://developer.salesloft.com/docs/api/crm-activity-fields/)'
  name: Salesloft Crm Activity Fields API
  slug: salesloft-crm-activity-fields-api
- description: '[https://developer.salesloft.com/docs/api/crm-users/](https://developer.salesloft.com/docs/api/crm-users/)'
  name: Salesloft Crm Users API
  slug: salesloft-crm-users-api
- description: '[https://developer.salesloft.com/docs/api/custom-fields/](https://developer.salesloft.com/docs/api/custom-fields/)'
  name: Salesloft Custom Fields API
  slug: salesloft-custom-fields-api
- description: '[https://developer.salesloft.com/docs/api/custom-roles/](https://developer.salesloft.com/docs/api/custom-roles/)'
  name: Salesloft Custom Roles API
  slug: salesloft-custom-roles-api
- description: '[https://developer.salesloft.com/docs/api/email-missing-tags/](https://developer.salesloft.com/docs/api/email-missing-tags/)'
  name: Salesloft Email Missing Tags API
  slug: salesloft-email-missing-tags-api
- description: '[https://developer.salesloft.com/docs/api/email-template-attachments/](https://developer.salesloft.com/docs/api/email-template-attachments/)'
  name: Salesloft Email Template Attachments API
  slug: salesloft-email-template-attachments-api
- description: '[https://developer.salesloft.com/docs/api/email-templates/](https://developer.salesloft.com/docs/api/email-templates/)'
  name: Salesloft Email Templates API
  slug: salesloft-email-templates-api
- description: '[https://developer.salesloft.com/docs/api/emails/](https://developer.salesloft.com/docs/api/emails/)'
  name: Salesloft Emails API
  slug: salesloft-emails-api
- description: '[https://developer.salesloft.com/docs/api/external-emails/](https://developer.salesloft.com/docs/api/external-emails/)'
  name: Salesloft External Emails API
  slug: salesloft-external-emails-api
- description: '[https://developer.salesloft.com/docs/api/external-id-configuration/](https://developer.salesloft.com/docs/api/external-id-configuration/)'
  name: Salesloft External Id Configuration API
  slug: salesloft-external-id-configuration-api
- description: '[https://developer.salesloft.com/docs/api/external-id-mapping/](https://developer.salesloft.com/docs/api/external-id-mapping/)'
  name: Salesloft External Id Mapping API
  slug: salesloft-external-id-mapping-api
- description: '[https://developer.salesloft.com/docs/api/groups/](https://developer.salesloft.com/docs/api/groups/)'
  name: Salesloft Groups API
  slug: salesloft-groups-api
- description: '[https://developer.salesloft.com/docs/api/imports/](https://developer.salesloft.com/docs/api/imports/)'
  name: Salesloft Imports API
  slug: salesloft-imports-api
- description: '[https://developer.salesloft.com/docs/api/live-feed-items/](https://developer.salesloft.com/docs/api/live-feed-items/)'
  name: Salesloft Live Feed Items API
  slug: salesloft-live-feed-items-api
- description: '[https://developer.salesloft.com/docs/api/live-website-tracking-parameters/](https://developer.salesloft.com/docs/api/live-website-tracking-parameters/)'
  name: Salesloft Live Website Tracking Parameters API
  slug: salesloft-live-website-tracking-parameters-api
- description: '[https://developer.salesloft.com/docs/api/me/](https://developer.salesloft.com/docs/api/me/)'
  name: Salesloft Me API
  slug: salesloft-me-api
- description: '[https://developer.salesloft.com/docs/api/meetings/](https://developer.salesloft.com/docs/api/meetings/)'
  name: Salesloft Meetings API
  slug: salesloft-meetings-api
- description: '[https://developer.salesloft.com/docs/api/mime-email-payloads/](https://developer.salesloft.com/docs/api/mime-email-payloads/)'
  name: Salesloft Mime Email Payloads API
  slug: salesloft-mime-email-payloads-api
- description: '[https://developer.salesloft.com/docs/api/notes/](https://developer.salesloft.com/docs/api/notes/)'
  name: Salesloft Notes API
  slug: salesloft-notes-api
- description: '[https://developer.salesloft.com/docs/api/ongoing-actions/](https://developer.salesloft.com/docs/api/ongoing-actions/)'
  name: Salesloft Ongoing Actions API
  slug: salesloft-ongoing-actions-api
- description: '[https://developers.salesloft.com/docs/api/opportunities/](https://developers.salesloft.com/docs/api/opportunities/)'
  name: Salesloft Opportunities API
  slug: salesloft-opportunities-api
- description: '[https://developers.salesloft.com/docs/api/opportunity-people/](https://developers.salesloft.com/docs/api/opportunity-people/)'
  name: Salesloft Opportunity People API
  slug: salesloft-opportunity-people-api
- description: '[https://developers.salesloft.com/docs/api/opportunity-stages/](https://developers.salesloft.com/docs/api/opportunity-stages/)'
  name: Salesloft Opportunity Stages API
  slug: salesloft-opportunity-stages-api
- description: '[https://developer.salesloft.com/docs/api/pending-emails/](https://developer.salesloft.com/docs/api/pending-emails/)'
  name: Salesloft Pending Emails API
  slug: salesloft-pending-emails-api
- description: '[https://developer.salesloft.com/docs/api/people/](https://developer.salesloft.com/docs/api/people/)'
  name: Salesloft People API
  slug: salesloft-people-api
- description: '[https://developer.salesloft.com/docs/api/people-soft-deletion/](https://developer.salesloft.com/docs/api/people-soft-deletion/)'
  name: Salesloft People Soft Deletion API
  slug: salesloft-people-soft-deletion-api
- description: '[https://developer.salesloft.com/docs/api/person-stages/](https://developer.salesloft.com/docs/api/person-stages/)'
  name: Salesloft Person Stages API
  slug: salesloft-person-stages-api
- description: '[https://developer.salesloft.com/docs/api/person-upserts/](https://developer.salesloft.com/docs/api/person-upserts/)'
  name: Salesloft Person Upserts API
  slug: salesloft-person-upserts-api
- description: '[https://developer.salesloft.com/docs/api/phone-number-assignments/](https://developer.salesloft.com/docs/api/phone-number-assignments/)'
  name: Salesloft Phone Number Assignments API
  slug: salesloft-phone-number-assignments-api
- description: '[https://developer.salesloft.com/docs/api/play-registrations/](https://developer.salesloft.com/docs/api/play-registrations/)'
  name: Salesloft Play Registrations API
  slug: salesloft-play-registrations-api
- description: '[https://developers.salesloft.com/docs/api/profiles/](https://developers.salesloft.com/docs/api/profiles/)'
  name: Salesloft Profiles API
  slug: salesloft-profiles-api
- description: '[https://developer.salesloft.com/docs/api/recording-settings/](https://developer.salesloft.com/docs/api/recording-settings/)'
  name: Salesloft Recording Settings API
  slug: salesloft-recording-settings-api
- description: '[https://developer.salesloft.com/docs/api/requests/](https://developer.salesloft.com/docs/api/requests/)'
  name: Salesloft Requests API
  slug: salesloft-requests-api
- description: '[https://developer.salesloft.com/docs/api/reschedule-links/](https://developer.salesloft.com/docs/api/reschedule-links/)'
  name: Salesloft Reschedule Links API
  slug: salesloft-reschedule-links-api
- description: '[https://developer.salesloft.com/docs/api/right-to-be-forgotten/](https://developer.salesloft.com/docs/api/right-to-be-forgotten/)'
  name: Salesloft Right to Be Forgotten API
  slug: salesloft-right-to-be-forgotten-api
- description: '[https://developer.salesloft.com/docs/api/saved-list-views/](https://developer.salesloft.com/docs/api/saved-list-views/)'
  name: Salesloft Saved List Views API
  slug: salesloft-saved-list-views-api
- description: '[https://developer.salesloft.com/docs/api/searches/](https://developer.salesloft.com/docs/api/searches/)'
  name: Salesloft Searches API
  slug: salesloft-searches-api
- description: '[https://developer.salesloft.com/docs/api/settings/](https://developer.salesloft.com/docs/api/settings/)'
  name: Salesloft Settings API
  slug: salesloft-settings-api
- description: '[https://developer.salesloft.com/docs/api/signal-registrations/](https://developer.salesloft.com/docs/api/signal-registrations/)'
  name: Salesloft Signal Registrations API
  slug: salesloft-signal-registrations-api
- description: '[https://developer.salesloft.com/docs/api/signals/](https://developer.salesloft.com/docs/api/signals/)'
  name: Salesloft Signals API
  slug: salesloft-signals-api
- description: '[https://developer.salesloft.com/docs/api/steps/](https://developer.salesloft.com/docs/api/steps/)'
  name: Salesloft Steps API
  slug: salesloft-steps-api
- description: '[https://developer.salesloft.com/docs/api/successes/](https://developer.salesloft.com/docs/api/successes/)'
  name: Salesloft Successes API
  slug: salesloft-successes-api
- description: The Tags API from Salesloft — 1 operation(s) for tags.
  name: Salesloft Tags API
  slug: salesloft-tags-api
- description: '[https://developer.salesloft.com/docs/api/tasks/](https://developer.salesloft.com/docs/api/tasks/)'
  name: Salesloft Tasks API
  slug: salesloft-tasks-api
- description: '[https://developer.salesloft.com/docs/api/team/](https://developer.salesloft.com/docs/api/team/)'
  name: Salesloft Team API
  slug: salesloft-team-api
- description: '[https://developer.salesloft.com/docs/api/team-template-attachments/](https://developer.salesloft.com/docs/api/team-template-attachments/)'
  name: Salesloft Team Template Attachments API
  slug: salesloft-team-template-attachments-api
- description: '[https://developer.salesloft.com/docs/api/team-templates/](https://developer.salesloft.com/docs/api/team-templates/)'
  name: Salesloft Team Templates API
  slug: salesloft-team-templates-api
- description: '[https://developer.salesloft.com/docs/api/transcriptions/](https://developer.salesloft.com/docs/api/transcriptions/)'
  name: Salesloft Transcriptions API
  slug: salesloft-transcriptions-api
- description: '[https://developer.salesloft.com/docs/api/users/](https://developer.salesloft.com/docs/api/users/)'
  name: Salesloft Users API
  slug: salesloft-users-api
- description: '[https://developer.salesloft.com/docs/api/webhook-subscriptions/](https://developer.salesloft.com/docs/api/webhook-subscriptions/)'
  name: Salesloft Webhook Subscriptions API
  slug: salesloft-webhook-subscriptions-api
artifact_total: 189
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Salesloft Account and People Redaction API
  slug: open-salesloft-account-and-people-redaction-api
- collection_type: open
  name: Salesloft Account and People Redaction Account Redaction API
  slug: open-salesloft-account-redaction-api
- collection_type: open
  name: Salesloft Account and People Redaction Account Stages API
  slug: open-salesloft-account-stages-api
- collection_type: open
  name: Salesloft Account and People Redaction Account Team Member Roles API
  slug: open-salesloft-account-team-member-roles-api
- collection_type: open
  name: Salesloft Account and People Redaction Account Tiers API
  slug: open-salesloft-account-tiers-api
- collection_type: open
  name: Salesloft Account and People Redaction Account Upserts API
  slug: open-salesloft-account-upserts-api
- collection_type: open
  name: Salesloft Account and People Redaction Accounts API
  slug: open-salesloft-accounts-api
- collection_type: open
  name: Salesloft Account and People Redaction Actions API
  slug: open-salesloft-actions-api
- collection_type: open
  name: Salesloft Account and People Redaction Activities API
  slug: open-salesloft-activities-api
- collection_type: open
  name: Salesloft Account and People Redaction Activity Histories API
  slug: open-salesloft-activity-histories-api
- collection_type: open
  name: Salesloft Account and People Redaction Bulk Jobs API
  slug: open-salesloft-bulk-jobs-api
- collection_type: open
  name: Salesloft Account and People Redaction Bulk Jobs - Job Data API
  slug: open-salesloft-bulk-jobs-job-data-api
- collection_type: open
  name: Salesloft Account and People Redaction Bulk Jobs - Results API
  slug: open-salesloft-bulk-jobs-results-api
- collection_type: open
  name: Salesloft Account and People Redaction Bulk Reschedule Tasks API
  slug: open-salesloft-bulk-reschedule-tasks-api
- collection_type: open
  name: Salesloft Account and People Redaction Cadence Exports API
  slug: open-salesloft-cadence-exports-api
- collection_type: open
  name: Salesloft Account and People Redaction Cadence Imports API
  slug: open-salesloft-cadence-imports-api
- collection_type: open
  name: Salesloft Account and People Redaction Cadence Memberships API
  slug: open-salesloft-cadence-memberships-api
- collection_type: open
  name: Salesloft Account and People Redaction Cadence Stats API
  slug: open-salesloft-cadence-stats-api
- collection_type: open
  name: Salesloft Account and People Redaction Cadences API
  slug: open-salesloft-cadences-api
- collection_type: open
  name: Salesloft Account and People Redaction Calendar Events API
  slug: open-salesloft-calendar-events-api
- collection_type: open
  name: Salesloft Account and People Redaction Call Data Records API
  slug: open-salesloft-call-data-records-api
- collection_type: open
  name: Salesloft Account and People Redaction Call Dispositions API
  slug: open-salesloft-call-dispositions-api
- collection_type: open
  name: Salesloft Account and People Redaction Call Instructions API
  slug: open-salesloft-call-instructions-api
- collection_type: open
  name: Salesloft Account and People Redaction Call Sentiments API
  slug: open-salesloft-call-sentiments-api
- collection_type: open
  name: Salesloft Account and People Redaction Caller Ids API
  slug: open-salesloft-caller-ids-api
- collection_type: open
  name: Salesloft Account and People Redaction Calls API
  slug: open-salesloft-calls-api
- collection_type: open
  name: Salesloft Account and People Redaction Client Credentials Access Token API
  slug: open-salesloft-client-credentials-access-token-api
- collection_type: open
  name: Salesloft Account and People Redaction Conversations API
  slug: open-salesloft-conversations-api
- collection_type: open
  name: Salesloft Account and People Redaction Conversations Calls API
  slug: open-salesloft-conversations-calls-api
- collection_type: open
  name: Salesloft Account and People Redaction Counts API
  slug: open-salesloft-counts-api
- collection_type: open
  name: Salesloft Account and People Redaction Crm Account Team Members API
  slug: open-salesloft-crm-account-team-members-api
- collection_type: open
  name: Salesloft Account and People Redaction Crm Activities API
  slug: open-salesloft-crm-activities-api
- collection_type: open
  name: Salesloft Account and People Redaction Crm Activity Fields API
  slug: open-salesloft-crm-activity-fields-api
- collection_type: open
  name: Salesloft Account and People Redaction Crm Users API
  slug: open-salesloft-crm-users-api
- collection_type: open
  name: Salesloft Account and People Redaction Custom Fields API
  slug: open-salesloft-custom-fields-api
- collection_type: open
  name: Salesloft Account and People Redaction Custom Roles API
  slug: open-salesloft-custom-roles-api
- collection_type: open
  name: Salesloft Account and People Redaction Email Missing Tags API
  slug: open-salesloft-email-missing-tags-api
- collection_type: open
  name: Salesloft Account and People Redaction Email Template Attachments API
  slug: open-salesloft-email-template-attachments-api
- collection_type: open
  name: Salesloft Account and People Redaction Email Templates API
  slug: open-salesloft-email-templates-api
- collection_type: open
  name: Salesloft Account and People Redaction Emails API
  slug: open-salesloft-emails-api
- collection_type: open
  name: Salesloft Account and People Redaction External Emails API
  slug: open-salesloft-external-emails-api
- collection_type: open
  name: Salesloft Account and People Redaction External Id Configuration API
  slug: open-salesloft-external-id-configuration-api
- collection_type: open
  name: Salesloft Account and People Redaction External Id Mapping API
  slug: open-salesloft-external-id-mapping-api
- collection_type: open
  name: Salesloft Account and People Redaction Groups API
  slug: open-salesloft-groups-api
- collection_type: open
  name: Salesloft Account and People Redaction Imports API
  slug: open-salesloft-imports-api
- collection_type: open
  name: Salesloft Account and People Redaction Live Feed Items API
  slug: open-salesloft-live-feed-items-api
- collection_type: open
  name: Salesloft Account and People Redaction Live Website Tracking Parameters API
  slug: open-salesloft-live-website-tracking-parameters-api
- collection_type: open
  name: Salesloft Account and People Redaction Me API
  slug: open-salesloft-me-api
- collection_type: open
  name: Salesloft Account and People Redaction Meetings API
  slug: open-salesloft-meetings-api
- collection_type: open
  name: Salesloft Account and People Redaction Mime Email Payloads API
  slug: open-salesloft-mime-email-payloads-api
- collection_type: open
  name: Salesloft Account and People Redaction Notes API
  slug: open-salesloft-notes-api
- collection_type: open
  name: Salesloft Account and People Redaction Ongoing Actions API
  slug: open-salesloft-ongoing-actions-api
- collection_type: open
  name: Salesloft Account and People Redaction Opportunities API
  slug: open-salesloft-opportunities-api
- collection_type: open
  name: Salesloft Account and People Redaction Opportunity People API
  slug: open-salesloft-opportunity-people-api
- collection_type: open
  name: Salesloft Account and People Redaction Opportunity Stages API
  slug: open-salesloft-opportunity-stages-api
- collection_type: open
  name: Salesloft Account and People Redaction Pending Emails API
  slug: open-salesloft-pending-emails-api
- collection_type: open
  name: Salesloft Account and Redaction People API
  slug: open-salesloft-people-api
- collection_type: open
  name: Salesloft Account and People Redaction People Soft Deletion API
  slug: open-salesloft-people-soft-deletion-api
- collection_type: open
  name: Salesloft Account and People Redaction Person Stages API
  slug: open-salesloft-person-stages-api
- collection_type: open
  name: Salesloft Account and People Redaction Person Upserts API
  slug: open-salesloft-person-upserts-api
- collection_type: open
  name: Salesloft Account and People Redaction Phone Number Assignments API
  slug: open-salesloft-phone-number-assignments-api
- collection_type: open
  name: Salesloft Account and People Redaction Play Registrations API
  slug: open-salesloft-play-registrations-api
- collection_type: open
  name: Salesloft Account and People Redaction Profiles API
  slug: open-salesloft-profiles-api
- collection_type: open
  name: Salesloft Account and People Redaction Recording Settings API
  slug: open-salesloft-recording-settings-api
- collection_type: open
  name: Salesloft Account and People Redaction Requests API
  slug: open-salesloft-requests-api
- collection_type: open
  name: Salesloft Account and People Redaction Reschedule Links API
  slug: open-salesloft-reschedule-links-api
- collection_type: open
  name: Salesloft Account and People Redaction Right to Be Forgotten API
  slug: open-salesloft-right-to-be-forgotten-api
- collection_type: open
  name: Salesloft Account and People Redaction Saved List Views API
  slug: open-salesloft-saved-list-views-api
- collection_type: open
  name: Salesloft Account and People Redaction Searches API
  slug: open-salesloft-searches-api
- collection_type: open
  name: Salesloft Account and People Redaction Settings API
  slug: open-salesloft-settings-api
- collection_type: open
  name: Salesloft Account and People Redaction Signal Registrations API
  slug: open-salesloft-signal-registrations-api
- collection_type: open
  name: Salesloft Account and People Redaction Signals API
  slug: open-salesloft-signals-api
- collection_type: open
  name: Salesloft Account and People Redaction Steps API
  slug: open-salesloft-steps-api
- collection_type: open
  name: Salesloft Account and People Redaction Successes API
  slug: open-salesloft-successes-api
- collection_type: open
  name: Salesloft Account and People Redaction Tags API
  slug: open-salesloft-tags-api
- collection_type: open
  name: Salesloft Account and People Redaction Tasks API
  slug: open-salesloft-tasks-api
- collection_type: open
  name: Salesloft Account and People Redaction Team API
  slug: open-salesloft-team-api
- collection_type: open
  name: Salesloft Account and People Redaction Team Template Attachments API
  slug: open-salesloft-team-template-attachments-api
- collection_type: open
  name: Salesloft Account and People Redaction Team Templates API
  slug: open-salesloft-team-templates-api
- collection_type: open
  name: Salesloft Account and People Redaction Transcriptions API
  slug: open-salesloft-transcriptions-api
- collection_type: open
  name: Salesloft Account and People Redaction Users API
  slug: open-salesloft-users-api
- collection_type: open
  name: Salesloft Account and People Redaction Webhook Subscriptions API
  slug: open-salesloft-webhook-subscriptions-api
- collection_type: open
  name: Salesloft
  slug: open-salesloft
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/salesloft-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/salesloft-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/salesloft-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salesloft-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/salesloft-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SalesLoft
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/salesloft
- group: company
  title: ''
  type: Website
  url: https://salesloft.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/salesloft-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/salesloft-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/salesloft-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/salesloft-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/salesloft-tool-crosswalk.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/salesloft-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/salesloft-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/salesloft-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/salesloft-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.salesloft.com/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/salesloft-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/salesloft-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.salesloft.com/
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/salesloft-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/salesloft-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/salesloft-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/salesloft-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/salesloft-data-model.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/salesloft-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.salesloft.com/security
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.salesloft.com/docs/platform/webhooks/
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.salesloft.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.salesloft.com/docs/platform/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.salesloft.com/docs/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.salesloft.com/docs/platform/intro/
- group: operate
  title: ''
  type: Support
  url: https://help.salesloft.com/
- group: operate
  title: ''
  type: Community
  url: https://champions.salesloft.com/
- group: company
  title: ''
  type: Blog
  url: https://www.salesloft.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.salesloft.com/pricing
- group: start
  title: ''
  type: Login
  url: https://accounts.salesloft.com/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.salesloft.com/legal/msa
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.salesloft.com/legal/platform-privacy-notice
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/salesloft-dev/salesloft
created: '2026-05-08'
description: Salesloft is a sales engagement and revenue orchestration platform, now combined with Clari, Drift and Groove, used by more than 4,000 sales teams to run cadences, dial and email prospects, capture and analyse conversations, and forecast pipeline. The Salesloft Platform API v2 at https://api.salesloft.com/v2 covers accounts, people, cadences, steps and actions, tasks, calls, emails, meetings, notes, opportunities, conversation intelligence, bulk jobs, imports, CRM mirroring, data-redaction governance and Rhythm signals, authenticated with OAuth 2.0 (authorization code and client credentials) or scoped API keys and priced against a 600-cost-per-minute per-team budget. Salesloft also publishes a documented webhook surface with HMAC-signed deliveries and a first-party remote MCP server at https://mcp.salesloft.com/mcp exposing fifteen read-only tools to AI agents.
examples:
- key_count: 2
  name: Salesloft Create Person Example
  slug: salesloft-create-person-example
- key_count: 2
  name: Salesloft List Accounts Example
  slug: salesloft-list-accounts-example
finops:
- name: Salesloft Finops
  service_category: Sales
  slug: salesloft-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/salesloft.png
json_schemas:
- name: Salesloft Account
  property_count: 30
  slug: salesloft-account
- name: Salesloft Cadence
  property_count: 15
  slug: salesloft-cadence
- name: Salesloft Person
  property_count: 38
  slug: salesloft-person
json_structures:
- name: Salesloft Account Structure
  property_count: 0
  slug: salesloft-account-structure
- name: Salesloft Person Structure
  property_count: 0
  slug: salesloft-person-structure
jsonld:
- class_count: 0
  name: Salesloft Context
  property_count: 5
  slug: salesloft-context
layout: provider
mcp_servers:
- description: Salesloft operates a first-party remote MCP server at https://mcp.salesloft.com. The server root (GET /) publishes the complete tool manifest ANONYMOUSLY — 15 tools with full JSON Schema inputSchema A
  name: Salesloft MCP Server
  slug: salesloft-mcp-server
modified: '2026-08-13'
name: Salesloft
nav: Providers
network: true
overview: 'Salesloft publishes 83 APIs on the [APIs.io](https://apis.io/) network, including Webhooks API, Account and People Redaction API, Account Redaction API, and 80 more. Tagged areas include Sales, Sales Engagement, Cadences, CRM, and Email.


  The Salesloft catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Salesloft''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 36 more developer resources.'
plans:
- name: Salesloft Plans Pricing
  plan_count: 0
  slug: salesloft-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Salesloft Rate Limits
  slug: salesloft-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Salesloft API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: salesloft-jsonschema-spectral-rules
- effective_rule_count: 53
  extends:
  - spectral:oas
  name: Salesloft API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 4
    info: 0
    warn: 5
  slug: salesloft-rules
scopes:
- name: Salesloft Scopes
  scope_count: 57
  slug: salesloft-scopes
  summary_line: 57 scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 30
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 53.9
    commercial_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 58.9
    developer_ergonomics: 58.9
    discoverability: 63.0
    governance: 31.8
    operational_transparency: 84.2
  previous_composite: 58.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 82
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salesloft/refs/heads/main/screenshots/salesloft-2026-06-20T193352.png
security:
- kind: authentication
  name: Salesloft Authentication
  slug: salesloft-authentication
  summary_line: oauth2/openIdConnect/apiKey · 5 schemes
- kind: domain-security
  name: Salesloft Domain Security
  slug: salesloft-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Salesloft Vulnerability Disclosure
  slug: salesloft-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Salesloft Trust Center
  slug: salesloft-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: salesloft
tags:
- Sales
- Sales Engagement
- Cadences
- CRM
- Email
- Revenue Intelligence
- Conversation Intelligence
- Sales Automation
- Webhook
- MCP
- Agents
- Dialer
- Pipeline
- Forecasting
website: https://salesloft.com/
---
