---
access_model:
  confidence: high
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 54.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 209
  human_in_the_loop: 5
  name: Sendgrid Agentic Access
  operation_count: 389
  slug: sendgrid-agentic-access
  summary_line: 389 operations · 209 acting · 5 human-in-the-loop
api_count: 63
apis:
- description: Twilio SendGrid Account Provisioning API account operations.
  name: SendGrid Account API
  slug: sendgrid-account-api
- description: Twilio SendGrid Account Provisioning API account state operations.
  name: SendGrid Account State API
  slug: sendgrid-account-state-api
- description: Twilio SendGrid Alerts API.
  name: SendGrid Alerts API
  slug: sendgrid-alerts-api
- description: Twilio SendGrid API Keys API.
  name: SendGrid API Keys API
  slug: sendgrid-api-keys-api
- description: 'Twilio SendGrid Suppressions API: Blocks operations'
  name: SendGrid Blocks API
  slug: sendgrid-blocks-api
- description: 'Twilio SendGrid Suppressions API: Bounces operations'
  name: SendGrid Bounces API
  slug: sendgrid-bounces-api
- description: The Twilio SendGrid Bulk Email Address Validation API
  name: SendGrid Bulk Email Address Validation API
  slug: sendgrid-bulk-email-address-validation-api
- description: 'Legacy Marketing Campaigns: Campaigns API'
  name: SendGrid Campaigns API API
  slug: sendgrid-campaigns-api-api
- description: Twilio SendGrid Category Stats API
  name: SendGrid Categories API
  slug: sendgrid-categories-api
- description: Twilio SendGrid Marketing Campaigns Contacts API
  name: SendGrid Contacts API
  slug: sendgrid-contacts-api
- description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Custom Fields API'
  name: SendGrid Custom Fields API
  slug: sendgrid-custom-fields-api
- description: Twilio SendGrid Marketing Campaigns Designs API
  name: SendGrid Designs API
  slug: sendgrid-designs-api
- description: Twilio SendGrid Domain Authentication API
  name: SendGrid Domain Authentication API
  slug: sendgrid-domain-authentication-api
- description: Twilio SendGrid Email Activity API
  name: SendGrid Email Activity API
  slug: sendgrid-email-activity-api
- description: The Twilio SendGrid Email Address Validation API
  name: SendGrid Email Address Validation API
  slug: sendgrid-email-address-validation-api
- description: The Twilio SendGrid Enforced TLS API
  name: SendGrid Enforced TLS API
  slug: sendgrid-enforced-tls-api
- description: Twilio SendGrid Engagement Quality API
  name: SendGrid Engagement Quality API
  slug: sendgrid-engagement-quality-api
- description: Twilio SendGrid Event Webhook API
  name: SendGrid Event Webhook API
  slug: sendgrid-event-webhook-api
- description: Third-Party Integrations for SendGrid Event Export
  name: SendGrid External Integration Endpoints API
  slug: sendgrid-external-integration-endpoints-api
- description: 'Twilio SendGrid Suppressions API: Global Suppressions operations'
  name: SendGrid Global Suppressions API
  slug: sendgrid-global-suppressions-api
- description: 'Twilio SendGrid Suppressions API: Invalid Emails operations'
  name: SendGrid Invalid Emails API
  slug: sendgrid-invalid-emails-api
- description: Twilio SendGrid IP Access Management API
  name: SendGrid IP Access Management API
  slug: sendgrid-ip-access-management-api
- description: Twilio SendGrid IP Address Management API
  name: SendGrid IP Address Management API
  slug: sendgrid-ip-address-management-api
- description: Twilio SendGrid IP Address API Operations
  name: SendGrid IP Addresses API
  slug: sendgrid-ip-addresses-api
- description: Twilio SendGrid IP Address Pool API Operations
  name: SendGrid IP Pools API
  slug: sendgrid-ip-pools-api
- description: Twilio SendGrid IP Warmup API
  name: SendGrid IP Warmup API
  slug: sendgrid-ip-warmup-api
- description: Twilio SendGrid Link Branding API
  name: SendGrid Link Branding API
  slug: sendgrid-link-branding-api
- description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Lists API'
  name: SendGrid Lists API
  slug: sendgrid-lists-api
- description: Assign batch IDs to a send.
  name: SendGrid Mail Batch API
  slug: sendgrid-mail-batch-api
- description: Twilio Mail Send API.
  name: SendGrid Mail Send API
  slug: sendgrid-mail-send-api
- description: Twilio SendGrid Mail Settings API
  name: SendGrid Mail Settings API
  slug: sendgrid-mail-settings-api
- description: Twilio SendGrid Account Provisioning API offerings operations.
  name: SendGrid Offering API
  slug: sendgrid-offering-api
- description: Twilio SendGrid Parse Webhook API
  name: SendGrid Parse Webhook API
  slug: sendgrid-parse-webhook-api
- description: Twilio SendGrid Partner Settings API
  name: SendGrid Partner Settings API
  slug: sendgrid-partner-settings-api
- description: Twilio SendGrid Recipients' Data Erasure API
  name: SendGrid Point Delete System API
  slug: sendgrid-point-delete-system-api
- description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Recipients API'
  name: SendGrid Recipients API
  slug: sendgrid-recipients-api
- description: Twilio SendGrid Reverse DNS API
  name: SendGrid Reverse DNS API
  slug: sendgrid-reverse-dns-api
- description: Twilio SendGrid Scheduled Sends API
  name: SendGrid Scheduled Sends API
  slug: sendgrid-scheduled-sends-api
- description: Twilio SendGrid Scopes API
  name: SendGrid Scopes API
  slug: sendgrid-scopes-api
- description: Twilio SendGrid Marketing Campaigns Segments API
  name: SendGrid Segmenting Contacts API
  slug: sendgrid-segmenting-contacts-api
- description: Twilio SendGrid Marketing Campaigns Segments API V2
  name: SendGrid Segmenting Contacts V2 API
  slug: sendgrid-segmenting-contacts-v2-api
- description: 'Twilio SendGrid Legacy Marketing Campaigns Contacts: Segments API'
  name: SendGrid Segments API
  slug: sendgrid-segments-api
- description: Twilio SendGrid Marketing Campaigns Send Test Email API
  name: SendGrid Send Test Email API
  slug: sendgrid-send-test-email-api
- description: Twilio SendGrid Legacy Marketing Campaigns Sender Identities API
  name: SendGrid Sender Identities API
  slug: sendgrid-sender-identities-api
- description: Twilio SendGrid Sender Verification API
  name: SendGrid Sender Verification API
  slug: sendgrid-sender-verification-api
- description: Twilio SendGrid Marketing Campaigns Senders API
  name: SendGrid Senders API
  slug: sendgrid-senders-api
- description: Twilio SendGrid Marketing Campaigns Single Sends API
  name: SendGrid Single Sends API
  slug: sendgrid-single-sends-api
- description: 'Twilio SendGrid Suppressions API: Spam Reports operations'
  name: SendGrid Spam Reports API
  slug: sendgrid-spam-reports-api
- description: Twilio SendGrid Single Sign-On Certificate Operations
  name: SendGrid SSO Certificates API
  slug: sendgrid-sso-certificates-api
- description: Twilio SendGrid Single Sign-On Settings Operations
  name: SendGrid SSO Settings API
  slug: sendgrid-sso-settings-api
- description: Twilio SendGrid Single Sign-On Teammates Operations
  name: SendGrid SSO Teammates API
  slug: sendgrid-sso-teammates-api
- description: Twilio SendGrid Marketing Campaigns Stats API
  name: SendGrid Stats API
  slug: sendgrid-stats-api
- description: 'Twilio SendGrid Subusers API: Statistics Operations'
  name: SendGrid Subuser Statistics API
  slug: sendgrid-subuser-statistics-api
- description: The Subuser Website Access API from SendGrid — 1 operation(s) for subuser website access.
  name: SendGrid Subuser Website Access API
  slug: sendgrid-subuser-website-access-api
- description: Twilio SendGrid Subusers API
  name: SendGrid Subusers API
  slug: sendgrid-subusers-api
- description: Twilio SendGrid Suppressions API
  name: SendGrid Suppressions API
  slug: sendgrid-suppressions-api
- description: Twilio SendGrid Teammates API
  name: SendGrid Teammates API
  slug: sendgrid-teammates-api
- description: Twilio SendGrid Templates API
  name: SendGrid Templates API
  slug: sendgrid-templates-api
- description: 'Twilio SendGrid Templates API: Versions operations'
  name: SendGrid Templates Versions API
  slug: sendgrid-templates-versions-api
- description: Twilio SendGrid Tracking Settings API
  name: SendGrid Tracking API
  slug: sendgrid-tracking-api
- description: 'Twilio SendGrid Suppressions API: Unsubscribe Group operations'
  name: SendGrid Unsubscribe Groups API
  slug: sendgrid-unsubscribe-groups-api
- description: Twilio SendGrid Users API.
  name: SendGrid Users API API
  slug: sendgrid-users-api-api
- description: Twilio SendGrid Webhook Security API
  name: SendGrid Webhook Security API
  slug: sendgrid-webhook-security-api
arazzos:
- description: Create a campaign, send a test to yourself, and send the campaign for real.
  name: SendGrid Campaign Test Then Send
  slug: sendgrid-campaign-test-then-send-workflow
- description: Create a marketing list, upsert contacts directly into it, and confirm they landed.
  name: SendGrid Create List and Add Contacts
  slug: sendgrid-create-list-add-contacts-workflow
- description: Create a legacy Marketing Campaign targeting lists and schedule it for delivery.
  name: SendGrid Create and Schedule Campaign
  slug: sendgrid-create-schedule-campaign-workflow
- description: Create a Single Send draft, schedule it for delivery, and read it back.
  name: SendGrid Create and Schedule Single Send
  slug: sendgrid-create-schedule-singlesend-workflow
- description: Create a marketing list, build a segment filtered on that list, and refresh it.
  name: SendGrid Create Segment From List
  slug: sendgrid-create-segment-from-list-workflow
- description: Create a Marketing Campaigns sender and resend its verification when not auto-verified.
  name: SendGrid Create Sender and Resend Verification
  slug: sendgrid-create-sender-resend-verification-workflow
- description: Create a Single Sender identity and check whether sender verification has completed.
  name: SendGrid Create Verified Sender
  slug: sendgrid-create-verified-sender-workflow
- description: Create a reusable design, create a recipient list, and build a Single Send that uses both.
  name: SendGrid Design to Single Send
  slug: sendgrid-design-to-singlesend-workflow
- description: Duplicate an existing transactional template and read the new copy back.
  name: SendGrid Duplicate Template
  slug: sendgrid-duplicate-template-workflow
- description: Create a dynamic transactional template, add a version, and send mail using it.
  name: SendGrid Dynamic Template Send
  slug: sendgrid-dynamic-template-send-workflow
- description: Add an address to the global suppression list and read it back to confirm.
  name: SendGrid Global Suppress and Check
  slug: sendgrid-global-suppress-check-workflow
- description: Create a list, upsert contacts into it, and branch on the list's contact count.
  name: SendGrid List Add Contacts and Count
  slug: sendgrid-list-add-contacts-count-workflow
- description: Create a segment, manually refresh it, then read it back to inspect its membership.
  name: SendGrid Refresh Segment and Get
  slug: sendgrid-refresh-segment-get-workflow
- description: Find contacts with an SGQL query and add the matched address to the global suppression list.
  name: SendGrid Search Contacts and Suppress
  slug: sendgrid-search-contacts-suppress-workflow
- description: Send a single transactional email and branch on whether it was accepted.
  name: SendGrid Send Transactional Mail
  slug: sendgrid-send-transactional-mail-workflow
- description: List Single Sends, branch on whether any exist, and pull aggregate stats for one.
  name: SendGrid Single Send Stats
  slug: sendgrid-singlesend-stats-workflow
- description: Create an unsubscribe suppression group, add addresses to it, and list its suppressions.
  name: SendGrid Suppression Group Add
  slug: sendgrid-suppression-group-add-workflow
- description: Create a template, add a version, activate that version, and read the template back.
  name: SendGrid Template Version Activate
  slug: sendgrid-template-version-activate-workflow
- description: Upsert contacts asynchronously and branch on whether they can be confirmed yet.
  name: SendGrid Upsert Contacts and Confirm
  slug: sendgrid-upsert-contacts-confirm-workflow
artifact_total: 221
asyncapis:
- description: The SendGrid Event Webhook delivers near real-time event data about your email activity via HTTP POST requests. SendGrid batches events into arrays and sends them to your configured webhook URL. Event
  name: SendGrid Event Webhook
  slug: sendgrid-event-webhook-asyncapi
- description: The SendGrid Inbound Parse Webhook processes all incoming email for a domain or subdomain, parses the contents and attachments, and then POSTs multipart/form-data to a URL that you specify. You can us
  name: SendGrid Inbound Parse Webhook
  slug: sendgrid-inbound-parse-asyncapi
collections:
- collection_type: postman
  name: Twilio SendGrid Account Provisioning API
  slug: postman-tsg_account_provisioning_v3
- collection_type: postman
  name: Twilio SendGrid Alerts API
  slug: postman-tsg_alerts_v3
- collection_type: postman
  name: Twilio SendGrid API Keys API
  slug: postman-tsg_api_keys_v3
- collection_type: postman
  name: Twilio SendGrid Domain Authentication API
  slug: postman-tsg_domain_authentication_v3
- collection_type: postman
  name: Twilio SendGrid Email Activity API
  slug: postman-tsg_email_activity_v3
- collection_type: postman
  name: Twilio SendGrid Email Address Validation API
  slug: postman-tsg_email_validation_v3
- collection_type: postman
  name: Twilio SendGrid Enforced TLS API
  slug: postman-tsg_enforced_tls_v3
- collection_type: postman
  name: Twilio SendGrid Integrations API
  slug: postman-tsg_integrations_v3
- collection_type: postman
  name: Twilio SendGrid IP Access Management API
  slug: postman-tsg_ip_access_management_v3
- collection_type: postman
  name: Twilio SendGrid IP Address Management API
  slug: postman-tsg_ip_address_management_v3
- collection_type: postman
  name: Twilio SendGrid IP Warmup API
  slug: postman-tsg_ip_warmup_v3
- collection_type: postman
  name: Twilio SendGrid IP Address API
  slug: postman-tsg_ips_v3
- collection_type: postman
  name: Twilio SendGrid Link Branding API
  slug: postman-tsg_link_branding_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Campaigns API
  slug: postman-tsg_lmc_campaigns_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Contacts API
  slug: postman-tsg_lmc_contactdb_v3
- collection_type: postman
  name: Twilio SendGrid Legacy Marketing Campaigns Sender Identities API
  slug: postman-tsg_lmc_senders_v3
- collection_type: postman
  name: Twilio SendGrid Mail Settings API
  slug: postman-tsg_mail_settings_v3
- collection_type: postman
  name: Twilio SendGrid Mail API
  slug: postman-tsg_mail_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Contacts API
  slug: postman-tsg_mc_contacts_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Custom Fields API
  slug: postman-tsg_mc_custom_fields_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Designs
  slug: postman-tsg_mc_designs_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Lists API
  slug: postman-tsg_mc_lists_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Segments 2.0 API
  slug: postman-tsg_mc_segments_2
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Segments API
  slug: postman-tsg_mc_segments_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Senders API
  slug: postman-tsg_mc_senders_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Single Sends API
  slug: postman-tsg_mc_singlesends_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Statistics API
  slug: postman-tsg_mc_stats_v3
- collection_type: postman
  name: Twilio SendGrid Marketing Campaigns Send Test Email API
  slug: postman-tsg_mc_test_v3
- collection_type: postman
  name: Twilio SendGrid Partner API
  slug: postman-tsg_partner_v3
- collection_type: postman
  name: Twilio SendGrid Recipients' Data Erasure API
  slug: postman-tsg_recipients_data_erasure_v3
- collection_type: postman
  name: Twilio SendGrid Reverse DNS API
  slug: postman-tsg_reverse_dns_v3
- collection_type: postman
  name: Twilio SendGrid Scheduled Sends API
  slug: postman-tsg_scheduled_sends_v3
- collection_type: postman
  name: Twilio SendGrid Scopes API
  slug: postman-tsg_scopes_v3
- collection_type: postman
  name: Twilio SendGrid Engagement Quality API
  slug: postman-tsg_seq_v3
- collection_type: postman
  name: Twilio SendGrid Single Sign-On API
  slug: postman-tsg_sso_v3
- collection_type: postman
  name: Twilio SendGrid Statistics API
  slug: postman-tsg_stats_v3
- collection_type: postman
  name: Twilio SendGrid Subusers
  slug: postman-tsg_subusers_v3
- collection_type: postman
  name: Twilio SendGrid Suppressions API
  slug: postman-tsg_suppressions_v3
- collection_type: postman
  name: Twilio SendGrid Teammates API
  slug: postman-tsg_teammates_v3
- collection_type: postman
  name: Twilio SendGrid Templates API
  slug: postman-tsg_templates_v3
- collection_type: postman
  name: Twilio SendGrid Tracking Settings API
  slug: postman-tsg_tracking_settings_v3
- collection_type: postman
  name: Twilio SendGrid User API
  slug: postman-tsg_user_v3
- collection_type: postman
  name: Twilio SendGrid Verified Senders API
  slug: postman-tsg_verified_senders_v3
- collection_type: postman
  name: Twilio SendGrid Webhook Configuration API
  slug: postman-tsg_webhooks_v3
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Twilio SendGrid Provisioning Account API
  slug: open-sendgrid-account-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Account State API
  slug: open-sendgrid-account-state-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Alerts API
  slug: open-sendgrid-alerts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account API Keys API
  slug: open-sendgrid-api-keys-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Blocks API
  slug: open-sendgrid-blocks-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Bounces API
  slug: open-sendgrid-bounces-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Bulk Email Address Validation API
  slug: open-sendgrid-bulk-email-address-validation-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Campaigns API API
  slug: open-sendgrid-campaigns-api-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Categories API
  slug: open-sendgrid-categories-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Contacts API
  slug: open-sendgrid-contacts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Custom Fields API
  slug: open-sendgrid-custom-fields-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Designs API
  slug: open-sendgrid-designs-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Domain Authentication API
  slug: open-sendgrid-domain-authentication-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Email Activity API
  slug: open-sendgrid-email-activity-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Email Address Validation API
  slug: open-sendgrid-email-address-validation-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Enforced TLS API
  slug: open-sendgrid-enforced-tls-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Engagement Quality API
  slug: open-sendgrid-engagement-quality-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Event Webhook API
  slug: open-sendgrid-event-webhook-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account External Integration Endpoints API
  slug: open-sendgrid-external-integration-endpoints-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Global Suppressions API
  slug: open-sendgrid-global-suppressions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Invalid Emails API
  slug: open-sendgrid-invalid-emails-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Access Management API
  slug: open-sendgrid-ip-access-management-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Address Management API
  slug: open-sendgrid-ip-address-management-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Addresses API
  slug: open-sendgrid-ip-addresses-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Pools API
  slug: open-sendgrid-ip-pools-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account IP Warmup API
  slug: open-sendgrid-ip-warmup-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Link Branding API
  slug: open-sendgrid-link-branding-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Lists API
  slug: open-sendgrid-lists-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Batch API
  slug: open-sendgrid-mail-batch-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Send API
  slug: open-sendgrid-mail-send-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Mail Settings API
  slug: open-sendgrid-mail-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Offering API
  slug: open-sendgrid-offering-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Parse Webhook API
  slug: open-sendgrid-parse-webhook-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Partner Settings API
  slug: open-sendgrid-partner-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Point Delete System API
  slug: open-sendgrid-point-delete-system-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Recipients API
  slug: open-sendgrid-recipients-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Reverse DNS API
  slug: open-sendgrid-reverse-dns-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Scheduled Sends API
  slug: open-sendgrid-scheduled-sends-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Scopes API
  slug: open-sendgrid-scopes-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segmenting Contacts API
  slug: open-sendgrid-segmenting-contacts-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segmenting Contacts V2 API
  slug: open-sendgrid-segmenting-contacts-v2-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Segments API
  slug: open-sendgrid-segments-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Send Test Email API
  slug: open-sendgrid-send-test-email-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Sender Identities API
  slug: open-sendgrid-sender-identities-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Sender Verification API
  slug: open-sendgrid-sender-verification-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Senders API
  slug: open-sendgrid-senders-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Single Sends API
  slug: open-sendgrid-single-sends-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Spam Reports API
  slug: open-sendgrid-spam-reports-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Certificates API
  slug: open-sendgrid-sso-certificates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Settings API
  slug: open-sendgrid-sso-settings-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account SSO Teammates API
  slug: open-sendgrid-sso-teammates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Stats API
  slug: open-sendgrid-stats-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subuser Statistics API
  slug: open-sendgrid-subuser-statistics-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subuser Website Access API
  slug: open-sendgrid-subuser-website-access-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Subusers API
  slug: open-sendgrid-subusers-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Suppressions API
  slug: open-sendgrid-suppressions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Teammates API
  slug: open-sendgrid-teammates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Templates API
  slug: open-sendgrid-templates-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Templates Versions API
  slug: open-sendgrid-templates-versions-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Tracking API
  slug: open-sendgrid-tracking-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Unsubscribe Groups API
  slug: open-sendgrid-unsubscribe-groups-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Users API API
  slug: open-sendgrid-users-api-api
- collection_type: open
  name: Twilio SendGrid Provisioning Account Webhook Security API
  slug: open-sendgrid-webhook-security-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sendgrid-tsg_account_provisioning_v3-overlay.yaml
- group: build
  title: ''
  type: Packages
  url: packages/sendgrid-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sendgrid-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendgrid-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/sendgrid-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sendgrid-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sendgrid-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sendgrid-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sendgrid-changelog.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sendgrid-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/sendgrid-sandbox.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sendgrid-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sendgrid-trust-center.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sendgrid-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendgrid-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sendgrid-authentication.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/sendgrid-graphql.md
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sendgrid/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-campaign-test-then-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-list-add-contacts-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-schedule-campaign-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-schedule-singlesend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-segment-from-list-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-sender-resend-verification-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-create-verified-sender-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-design-to-singlesend-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-duplicate-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-dynamic-template-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-global-suppress-check-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-list-add-contacts-count-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-refresh-segment-get-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-search-contacts-suppress-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-send-transactional-mail-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-singlesend-stats-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-suppression-group-add-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-template-version-activate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sendgrid-upsert-contacts-confirm-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendgrid
- group: start
  title: ''
  type: Portal
  url: https://app.sendgrid.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.twilio.com/docs/sendgrid
- group: docs
  title: ''
  type: APIReference
  url: https://www.twilio.com/docs/sendgrid/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/api-getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/authentication
- group: start
  title: ''
  type: Signup
  url: https://signup.sendgrid.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://sendgrid.com/en-us/pricing
- group: operate
  title: ''
  type: Support
  url: https://support.sendgrid.com/hc/en-us
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sendgrid.com/
- group: company
  title: ''
  type: Blog
  url: https://sendgrid.com/blog/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sendgrid
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/sendgrid/sendgrid-python
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/sendgrid/sendgrid-nodejs
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/sendgrid/sendgrid-java
- group: build
  title: ''
  type: C# SDK
  url: https://github.com/sendgrid/sendgrid-csharp
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/sendgrid/sendgrid-go
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/sendgrid/sendgrid-ruby
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/sendgrid/sendgrid-php
- group: build
  title: ''
  type: Libraries
  url: https://www.twilio.com/docs/sendgrid/for-developers/sending-email/libraries
- group: start
  title: ''
  type: GettingStarted
  url: https://sendgrid.com/en-us/solutions/email-api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sendgrid.com/policies/tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sendgrid.com/policies/privacy/
- group: auth
  title: ''
  type: Security
  url: https://sendgrid.com/en-us/policies/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.twilio.com/en-us/changelog?product=sendgrid-email-api,twilio-sendgrid-platform
- group: operate
  title: ''
  type: RateLimits
  url: https://www.twilio.com/docs/sendgrid/api-reference/how-to-use-the-sendgrid-v3-api/rate-limits
- group: company
  title: ''
  type: Website
  url: https://sendgrid.com/en-us
- group: start
  title: ''
  type: Login
  url: https://login.sendgrid.com/
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/sendgrid
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/sendgrid
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-email-send.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-webhooks.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-suppressions.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-account-setup.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-email-settings.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-engagement-quality.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-inbound-parse.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/sendgrid-deliverability-advisor.md
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sendgrid-tool-crosswalk.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sendgrid-event-webhook-asyncapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/sendgrid-inbound-parse-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sendgrid-event-webhook-asyncapi.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sendgrid-scopes.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sendgrid-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sendgrid-rate-limits.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sendgrid-packages.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/sendgrid-lifecycle.yml
- group: auth
  title: ''
  type: Compliance
  url: security/sendgrid-trust-center.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sendgrid-finops.yml
- group: design
  title: ''
  type: Rules
  url: rules/sendgrid-spectral-rules.yml
- group: design
  title: ''
  type: Rules
  url: rules/sendgrid-asyncapi-spectral-rules.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sendgrid
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sendgrid-twilio-docs-llms.txt
created: '2025-08-14'
description: SendGrid is a cloud-based email delivery platform, acquired by Twilio in 2019, that provides transactional and marketing email at scale over an HTTP v3 REST API and an SMTP relay. The platform spans Mail Send, dynamic transactional templates, Marketing Campaigns (contacts, lists, Segments 2.0, Single Sends), email address validation, suppression management, domain authentication (SPF/DKIM/DMARC), dedicated IP management and warm-up, subusers, Engagement Quality scoring, and detailed delivery statistics. Event data is delivered asynchronously through the Event Webhook and inbound mail through Inbound Parse. All APIs authenticate with a scoped bearer API key against api.sendgrid.com, with an EU data-residency host at api.eu.sendgrid.com. Developer documentation and the API reference are published on the Twilio documentation site.
features:
- Mail Send v3 API for transactional email
- SMTP Relay for legacy app integration
- Marketing Campaigns API and UI
- Contacts API with custom fields and segments
- Email Validation API
- Inbound Parse webhook
- 'Free Trial: 100 emails/day for 60 days'
- Essentials at $19.95/mo for 100k emails
- Pro at $89.95/mo for 2.5M emails with dedicated IP
- Premier custom pricing with $12k/year minimum
- 'Mail Send rate limit: 100/min Free, 600/min Paid'
- Subusers for billing and access isolation
- SPF, DKIM, DMARC authentication
- Activity Feed (3-day Essentials, 7-day Pro)
- Send Time Optimization (Pro+)
- Tiered IP warm-up service (Premier)
finops:
- name: Sendgrid Finops
  service_category: Email Delivery
  slug: sendgrid-finops
graphqls:
- description: SendGrid Conceptual GraphQL Schema
  name: SendGrid GraphQL
  slug: sendgrid-graphql
image: https://sendgrid.com/brand/sg-logo-300.png
layout: provider
mcp_servers:
- description: ''
  name: sendgrid-mcp.yml
  slug: sendgrid-mcpyml
modified: '2026-08-13'
name: SendGrid
nav: Providers
network: true
overview: 'SendGrid publishes 63 APIs on the [APIs.io](https://apis.io/) network, including Account API, Account State API, Alerts API, and 60 more. Tagged areas include Email, Email API, Marketing Email, SMTP, and T1.


  The SendGrid catalog on APIs.io includes 2 event-driven AsyncAPI specifications and 2 Spectral governance rulesets.


  SendGrid''s developer surface includes changelog, sandbox, authentication, developer portal, documentation, API reference, getting-started guide, and 84 more developer resources.'
plans:
- name: Sendgrid Plans Pricing
  plan_count: 4
  slug: sendgrid-plans-pricing
random_paper: 103
rate_limits:
- limit_count: 0
  name: Sendgrid Rate Limits
  slug: sendgrid-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: SendGrid API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 6
  slug: sendgrid-asyncapi-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: SendGrid API Rules
  rule_count: 10
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 9
  slug: sendgrid-spectral-rules
scopes:
- name: Sendgrid Scopes
  scope_count: 0
  slug: sendgrid-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: exemplar
  composite: 77.4
  delta: 4.2
  facets:
    access_clarity: 100.0
    commercial_clarity: 100.0
    contract_governance: 41.7
    contract_quality: 73.5
    developer_ergonomics: 92.9
    discoverability: 75.9
    governance: 41.7
    operational_transparency: 60.5
  previous_composite: 73.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 63
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendgrid/refs/heads/main/screenshots/sendgrid-2026-06-20T193652.png
security:
- kind: authentication
  name: Sendgrid Authentication
  slug: sendgrid-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sendgrid Domain Security
  slug: sendgrid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sendgrid Vulnerability Disclosure
  slug: sendgrid-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sendgrid Trust Center
  slug: sendgrid-trust-center
  summary_line: SOC 2 Type II, SOC 2 Type I, ISO/IEC 27001:2013, ISO/IEC 27017:2015, ISO/IEC 27018:2019, PCI DSS Level 1, PCI DSS Level 4, HIPAA (eligible products & services), Binding Corporate Rules
slug: sendgrid
tags:
- Email
- Email API
- Marketing Email
- SMTP
- T1
- Transactional Email
- Email Marketing
- Deliverability
- Marketing
website: https://sendgrid.com/en-us
---
