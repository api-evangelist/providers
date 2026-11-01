---
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 466
  human_in_the_loop: 13
  name: Indigitall Agentic Access
  operation_count: 808
  slug: indigitall-agentic-access
  summary_line: 808 operations · 466 acting · 13 human-in-the-loop
api_count: 4
apis:
- description: ''
  name: indigitall API
  slug: indigitall-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for A/B Testing
  name: indigitall A/B Testing API
  slug: indigitall-a-b-testing-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for managing account
  name: indigitall Account API
  slug: indigitall-account-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for managing applications
  name: indigitall Application API
  slug: indigitall-application-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for authorising requests
  name: indigitall Auth API
  slug: indigitall-auth-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for managing campaigns
  name: indigitall Campaign API
  slug: indigitall-campaign-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoint for Chat integration functions
  name: indigitall Chat API
  slug: indigitall-chat-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage campaigns for chat-service-v2
  name: indigitall Chat Campaign API
  slug: indigitall-chat-campaign-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center agents for chat-service-v2
  name: indigitall Chat Cc Agent API
  slug: indigitall-chat-cc-agent-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center agent groups for chat-service-v2
  name: indigitall Chat Cc Agent Group API
  slug: indigitall-chat-cc-agent-group-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center contact comments for chat-service-v2
  name: indigitall Chat Cc Contact Comment API
  slug: indigitall-chat-cc-contact-comment-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center conversations for chat-service-v2
  name: indigitall Chat Cc Conversation API
  slug: indigitall-chat-cc-conversation-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center forms for chat-service-v2
  name: indigitall Chat Cc Form API
  slug: indigitall-chat-cc-form-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center permissions profiles for chat-service-v2
  name: indigitall Chat Cc Permissions Profile API
  slug: indigitall-chat-cc-permissions-profile-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center special days schedules for chat-service-v2
  name: indigitall Chat Cc Special Days Schedule API
  slug: indigitall-chat-cc-special-days-schedule-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage Contact Center weekly schedules for chat-service-v2
  name: indigitall Chat Cc Weekly Schedule API
  slug: indigitall-chat-cc-weekly-schedule-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage chat channels for chat-service-v2. The cannels are the different communication ways that chat-service-v2 can use to send and receive messages.
  name: indigitall Chat Channel API
  slug: indigitall-chat-channel-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage chat configurations
  name: indigitall Chat Configuration API
  slug: indigitall-chat-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage contacts for chat-service-v2
  name: indigitall Chat Contact API
  slug: indigitall-chat-contact-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage contact lists for chat-service-v2
  name: indigitall Chat Contact List API
  slug: indigitall-chat-contact-list-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage chat integrations for chat-service-v2. The integrations are used to handle incoming messages.
  name: indigitall Chat Integration API
  slug: indigitall-chat-integration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Internal endpoints for chat-service-v2
  name: indigitall Chat Internal API
  slug: indigitall-chat-internal-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage multimedia for chat-service-v2
  name: indigitall Chat Multimedia API
  slug: indigitall-chat-multimedia-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage messages sending for chat-service-v2
  name: indigitall Chat Send API
  slug: indigitall-chat-send-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage slicing for chat-service-v2
  name: indigitall Chat Slicing API
  slug: indigitall-chat-slicing-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to retrieve statistics and KPIs for chat-service-v2
  name: indigitall Chat Stats API
  slug: indigitall-chat-stats-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoint to check chat-service-v2 status
  name: indigitall Chat Status API
  slug: indigitall-chat-status-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage tags for chat-service-v2
  name: indigitall Chat Tag API
  slug: indigitall-chat-tag-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints to manage tasks for chat-service-v2
  name: indigitall Chat Task API
  slug: indigitall-chat-task-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for checking parameters
  name: indigitall Check API
  slug: indigitall-check-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The cloudapi API from indigitall — 3 operation(s) for cloudapi.
  name: indigitall Cloudapi API
  slug: indigitall-cloudapi-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer API
  slug: indigitall-customer-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Adviser API
  slug: indigitall-customer-service-adviser-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Application API
  slug: indigitall-customer-service-application-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Audience API
  slug: indigitall-customer-service-audience-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Cdpeventtype API
  slug: indigitall-customer-service-cdpeventtype-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Cdpeventtypetemplate API
  slug: indigitall-customer-service-cdpeventtypetemplate-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer API
  slug: indigitall-customer-service-customer-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer CSV API
  slug: indigitall-customer-service-customer-csv-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer Field API
  slug: indigitall-customer-service-customer-field-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer Journey API
  slug: indigitall-customer-service-customer-journey-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer Journey Control API
  slug: indigitall-customer-service-customer-journey-control-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer Journey Template API
  slug: indigitall-customer-service-customer-journey-template-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Customer Send API
  slug: indigitall-customer-service-customer-send-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Journeywaitqueue API
  slug: indigitall-customer-service-journeywaitqueue-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Segment API
  slug: indigitall-customer-service-segment-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Stats API
  slug: indigitall-customer-service-stats-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Task API
  slug: indigitall-customer-service-task-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Customer service endpoints
  name: indigitall Customer Service Webhook Template API
  slug: indigitall-customer-service-webhook-template-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Bulk operations over push devices
  name: indigitall Device API
  slug: indigitall-device-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage campaign attachments
  name: indigitall Es Attachment API
  slug: indigitall-es-attachment-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email audiences
  name: indigitall Es Audience API
  slug: indigitall-es-audience-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email campaigns
  name: indigitall Es Campaign API
  slug: indigitall-es-campaign-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage campaign blocks
  name: indigitall Es Campaign Block API
  slug: indigitall-es-campaign-block-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage campign columns. A column always belongs to a campaign block
  name: indigitall es-campaign block-column API
  slug: indigitall-es-campaign-block-column-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage campign multimedia.
  name: indigitall Es Campaign Multimedia API
  slug: indigitall-es-campaign-multimedia-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email categories
  name: indigitall Es Category API
  slug: indigitall-es-category-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage service configuration
  name: indigitall Es Configuration API
  slug: indigitall-es-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for configure email domains
  name: indigitall Es Configuration Domain API
  slug: indigitall-es-configurationdomain-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email senders for campaigns
  name: indigitall Es Configuration Domain Email API
  slug: indigitall-es-configurationdomainemail-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email contacts
  name: indigitall Es Contact API
  slug: indigitall-es-contact-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email footers
  name: indigitall Es Footer API
  slug: indigitall-es-footer-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage campaign sendings
  name: indigitall Es Shipment API
  slug: indigitall-es-shipment-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email statistics configuration
  name: indigitall Es Statistics API
  slug: indigitall-es-statistics-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage email tasks
  name: indigitall Es Tasks API
  slug: indigitall-es-tasks-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage inapp audiences
  name: indigitall Inapp Audience API
  slug: indigitall-inapp-audience-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-campaign API from indigitall — 3 operation(s) for inapp-campaign.
  name: indigitall Inapp Campaign API
  slug: indigitall-inapp-campaign-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-configuration API from indigitall — 1 operation(s) for inapp-configuration.
  name: indigitall Inapp Configuration API
  slug: indigitall-inapp-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-form API from indigitall — 2 operation(s) for inapp-form.
  name: indigitall Inapp Form API
  slug: indigitall-inapp-form-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-multimedia API from indigitall — 2 operation(s) for inapp-multimedia.
  name: indigitall Inapp Multimedia API
  slug: indigitall-inapp-multimedia-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-schema API from indigitall — 2 operation(s) for inapp-schema.
  name: indigitall Inapp Schema API
  slug: indigitall-inapp-schema-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-stats API from indigitall — 7 operation(s) for inapp-stats.
  name: indigitall Inapp Stats API
  slug: indigitall-inapp-stats-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage inapp tasks
  name: indigitall Inapp Task API
  slug: indigitall-inapp-task-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The inapp-topic API from indigitall — 2 operation(s) for inapp-topic.
  name: indigitall Inapp Topic API
  slug: indigitall-inapp-topic-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for inbox configuration
  name: indigitall Inbox API
  slug: indigitall-inbox-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for integration with other services
  name: indigitall Integration API
  slug: indigitall-integration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage custom short domains
  name: indigitall Link Short Domain API
  slug: indigitall-link-short-domain-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The meta-cloudapi API from indigitall — 6 operation(s) for meta-cloudapi.
  name: indigitall Meta Cloudapi API
  slug: indigitall-meta-cloudapi-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The meta-configuration API from indigitall — 1 operation(s) for meta-configuration.
  name: indigitall Meta Configuration API
  slug: indigitall-meta-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The meta-templates API from indigitall — 1 operation(s) for meta-templates.
  name: indigitall Meta Templates API
  slug: indigitall-meta-templates-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The meta-upload API from indigitall — 2 operation(s) for meta-upload.
  name: indigitall Meta Upload API
  slug: indigitall-meta-upload-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The meta-webhook API from indigitall — 2 operation(s) for meta-webhook.
  name: indigitall Meta Webhook API
  slug: indigitall-meta-webhook-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for Muli Testing
  name: indigitall Multi Testing API
  slug: indigitall-multi-testing-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Notification endpoints
  name: indigitall Notification API
  slug: indigitall-notification-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot agents
  name: indigitall Pathbot Agents API
  slug: indigitall-pathbot-agents-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot applications
  name: indigitall Pathbot Applications API
  slug: indigitall-pathbot-applications-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot documents
  name: indigitall Pathbot Documents API
  slug: indigitall-pathbot-documents-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot evaluation
  name: indigitall Pathbot Evaluation API
  slug: indigitall-pathbot-evaluation-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot flows
  name: indigitall Pathbot Flows API
  slug: indigitall-pathbot-flows-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot ingestion sources
  name: indigitall Pathbot Ingestion Sources API
  slug: indigitall-pathbot-ingestion-sources-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot nodes
  name: indigitall Pathbot Nodes API
  slug: indigitall-pathbot-nodes-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot skills
  name: indigitall Pathbot Skills API
  slug: indigitall-pathbot-skills-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for manage pathbot tools
  name: indigitall Pathbot Tools API
  slug: indigitall-pathbot-tools-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The push-live-activity API from indigitall — 2 operation(s) for push-live-activity.
  name: indigitall Push Live Activity API
  slug: indigitall-push-live-activity-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The push-live-configuration API from indigitall — 1 operation(s) for push-live-configuration.
  name: indigitall Push Live Configuration API
  slug: indigitall-push-live-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The push-live-ios-class API from indigitall — 2 operation(s) for push-live-ios-class.
  name: indigitall Push Live Ios Class API
  slug: indigitall-push-live-ios-class-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The push-live-send API from indigitall — 3 operation(s) for push-live-send.
  name: indigitall Push Live Send API
  slug: indigitall-push-live-send-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for send
  name: indigitall Push Send API
  slug: indigitall-pushsend-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The recommender API from indigitall — 2 operation(s) for recommender.
  name: indigitall Recommender API
  slug: indigitall-recommender-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The send API from indigitall — 2 operation(s) for send.
  name: indigitall Send API
  slug: indigitall-send-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-campaign API from indigitall — 3 operation(s) for sms-campaign.
  name: indigitall Sms Campaign API
  slug: indigitall-sms-campaign-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-configuration API from indigitall — 3 operation(s) for sms-configuration.
  name: indigitall Sms Configuration API
  slug: indigitall-sms-configuration-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-contact API from indigitall — 6 operation(s) for sms-contact.
  name: indigitall Sms Contact API
  slug: indigitall-sms-contact-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-cost API from indigitall — 2 operation(s) for sms-cost.
  name: indigitall Sms Cost API
  slug: indigitall-sms-cost-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-send API from indigitall — 6 operation(s) for sms-send.
  name: indigitall Sms Send API
  slug: indigitall-sms-send-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-stats API from indigitall — 10 operation(s) for sms-stats.
  name: indigitall Sms Stats API
  slug: indigitall-sms-stats-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-topic API from indigitall — 4 operation(s) for sms-topic.
  name: indigitall Sms Topic API
  slug: indigitall-sms-topic-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The sms-webhook API from indigitall — 1 operation(s) for sms-webhook.
  name: indigitall Sms Webhook API
  slug: indigitall-sms-webhook-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The stats API from indigitall — 9 operation(s) for stats.
  name: indigitall Stats API
  slug: indigitall-stats-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The stats-service-chat API from indigitall — 5 operation(s) for stats-service-chat.
  name: indigitall Stats Service Chat API
  slug: indigitall-stats-service-chat-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The stats-service-cs API from indigitall — 3 operation(s) for stats-service-cs.
  name: indigitall Stats Service Cs API
  slug: indigitall-stats-service-cs-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The stats-service-meta API from indigitall — 2 operation(s) for stats-service-meta.
  name: indigitall Stats Service Meta API
  slug: indigitall-stats-service-meta-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The stats-service-report API from indigitall — 3 operation(s) for stats-service-report.
  name: indigitall Stats Service Report API
  slug: indigitall-stats-service-report-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Endpoints for checking service status
  name: indigitall Status API
  slug: indigitall-status-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: Topic operations
  name: indigitall Topics API
  slug: indigitall-topics-api
- baseURL: https://indigitall.com/en/
  baseurl_source: declared
  description: The users API from indigitall — 10 operation(s) for users.
  name: indigitall Users API
  slug: indigitall-users-api
artifact_total: 126
common:
- group: agent
  href: https://artifacts.apis.io/indigitall/agentic-access/indigitall-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/indigitall-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/indigitall/rules/indigitall-rules.yml
  title: ''
  type: Spectral
  url: rules/indigitall-rules.yml
- group: design
  href: https://artifacts.apis.io/indigitall/json-ld/indigitall-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/indigitall-context.jsonld
- group: design
  href: https://artifacts.apis.io/indigitall/vocabulary/indigitall-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/indigitall-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/indigitall/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/indigitall/data-model/indigitall-data-model.yml
  title: ''
  type: DataModel
  url: data-model/indigitall-data-model.yml
- group: design
  href: https://artifacts.apis.io/indigitall/errors/indigitall-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/indigitall-problem-types.yml
- group: design
  href: https://artifacts.apis.io/indigitall/conformance/indigitall-conformance.yml
  title: ''
  type: Conformance
  url: conformance/indigitall-conformance.yml
- group: other
  href: https://artifacts.apis.io/indigitall/overlays/indigitall-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/indigitall-api-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/indigitall/llms/indigitall-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/indigitall-llms.txt
- group: agent
  href: https://artifacts.apis.io/indigitall/well-known/indigitall-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/indigitall-well-known.yml
- group: other
  href: https://artifacts.apis.io/indigitall/hosts/indigitall-hosts.yml
  title: ''
  type: Hosts
  url: hosts/indigitall-hosts.yml
- group: other
  href: https://artifacts.apis.io/indigitall/vendors/indigitall-vendors.yml
  title: ''
  type: Vendors
  url: vendors/indigitall-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://indigitall.com/en/legal-notice/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://indigitall.com/en/privacy-policy/
- group: company
  title: ''
  type: Blog
  url: https://indigitall.com/en/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.indigitall.com/docs/onboarding-with-indigitall/llms.txt
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.indigitall.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/indigitall
- group: auth
  href: https://artifacts.apis.io/indigitall/authentication/indigitall-authentication.yml
  title: ''
  type: Authentication
  url: authentication/indigitall-authentication.yml
- group: auth
  href: https://artifacts.apis.io/indigitall/security/indigitall-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/indigitall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://indigitall.com
created: '2026-10-21'
description: indigitall is the only AI‑powered all‑in‑one customer engagement platform that unifies outbound and inbound digital channels, enabling businesses to manage interactions across messaging, email, voice, and social media from a single interface. The solution leverages artificial intelligence to personalize communications, automate workflows, and provide analytics that help improve customer experience and drive growth. Founded with backing from venture partners, indigitall serves enterprises seeking to streamline engagement and boost conversion rates through a unified, intelligent platform.
jsonld:
- class_count: 120
  name: Indigitall Context
  property_count: 207
  slug: indigitall-context
layout: provider
modified: '2026-10-21'
name: indigitall
nav: Providers
network: true
overview: 'indigitall publishes 116 API contracts indexed on the [APIs.io](https://apis.io/) network, including A/B Testing API, Account API, Application API, and 113 more. Tagged areas include Company, AI, Customer Engagement, Platform, and SaaS.


  The indigitall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  indigitall''s developer surface includes engineering blog, getting-started guide, documentation, authentication, and 18 more developer resources.'
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: indigitall API Rules
  rule_count: 14
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 7
  slug: indigitall-rules
score:
  band: thin
  composite: 36.3
  coverage:
    artifact_dirs: 18
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 53.4
    developer_ergonomics: 37.5
    discoverability: 67.9
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 98.3
      derived: 0
      marker_coverage: 100.0
      total: 115
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Indigitall Authentication
  slug: indigitall-authentication
  summary_line: apiKey · 4 schemes
- kind: domain-security
  name: Indigitall Domain Security
  slug: indigitall-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 5
skills:
- name: indigitall-create-and-retrieve-cdp-event-type
  slug: indigitall-create-and-retrieve-cdp-event-type
- name: indigitall-create-and-retrieve-customer
  slug: indigitall-create-and-retrieve-customer
- name: indigitall-create-and-simulate-webhook-template
  slug: indigitall-create-and-simulate-webhook-template
- name: indigitall-create-journey-and-get-stats
  slug: indigitall-create-journey-and-get-stats
- name: indigitall-export-customer-segment
  slug: indigitall-export-customer-segment
slug: indigitall
tags:
- Company
- AI
- Customer Engagement
- Platform
- SaaS
website: https://indigitall.com
---
