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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.2
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Brevo Agentic Access
  operation_count: 75
  slug: brevo-agentic-access
  summary_line: 75 operations · 47 acting
api_count: 23
apis:
- description: Manage agent online status for conversation availability.
  name: brevo Agent Status API
  slug: brevo-agent-status-api
- description: Create, manage, and retrieve automated messages pushed to visitors.
  name: brevo Automated Messages API
  slug: brevo-automated-messages-api
- description: Retrieve performance metrics and statistics for email campaigns.
  name: brevo Campaign Statistics API
  slug: brevo-campaign-statistics-api
- description: Manage product categories for organizing the catalog.
  name: brevo Categories API
  slug: brevo-categories-api
- description: Define and manage custom attributes for contact profiles.
  name: brevo Contact Attributes API
  slug: brevo-contact-attributes-api
- description: Manage contact lists for organizing and segmenting audiences.
  name: brevo Contact Lists API
  slug: brevo-contact-lists-api
- description: Create, retrieve, update, and delete individual contacts.
  name: brevo Contacts API
  slug: brevo-contacts-api
- description: Track and retrieve transactional email activity including delivery status, opens, clicks, and bounces.
  name: brevo Email Activity API
  slug: brevo-email-activity-api
- description: Create, update, send, and manage marketing email campaigns.
  name: brevo Email Campaigns API
  slug: brevo-email-campaigns-api
- description: Create and manage reusable email templates for transactional messaging.
  name: brevo Email Templates API
  slug: brevo-email-templates-api
- description: Organize contact lists into folders for better management.
  name: brevo Folders API
  slug: brevo-folders-api
- description: Bulk import contacts from files or data payloads.
  name: brevo Import API
  slug: brevo-import-api
- description: Send and manage chat messages as an agent or automated bot within conversations.
  name: brevo Messages API
  slug: brevo-messages-api
- description: Create and manage eCommerce order data for revenue attribution and purchase tracking.
  name: brevo Orders API
  slug: brevo-orders-api
- description: Import, manage, and retrieve eCommerce product data.
  name: brevo Products API
  slug: brevo-products-api
- description: Manage sender identities used for transactional email sending.
  name: brevo Senders API
  slug: brevo-senders-api
- description: Retrieve delivery reports and activity statistics for transactional SMS messages.
  name: brevo SMS Statistics API
  slug: brevo-sms-statistics-api
- description: Send and manage transactional emails including order confirmations, password resets, and account notifications.
  name: brevo Transactional Emails API
  slug: brevo-transactional-emails-api
- description: Send transactional SMS messages for notifications, verifications, and alerts.
  name: brevo Transactional SMS API
  slug: brevo-transactional-sms-api
- description: Create, manage, and configure webhook subscriptions for receiving real-time event notifications.
  name: brevo Webhooks API
  slug: brevo-webhooks-api
- description: Create, manage, and send WhatsApp marketing campaigns.
  name: brevo WhatsApp Campaigns API
  slug: brevo-whatsapp-campaigns-api
- description: Send transactional WhatsApp messages to recipients using approved templates or plain text.
  name: brevo WhatsApp Messages API
  slug: brevo-whatsapp-messages-api
- description: Create and manage WhatsApp message templates that require Meta approval before use.
  name: brevo WhatsApp Templates API
  slug: brevo-whatsapp-templates-api
artifact_total: 106
asyncapis:
- description: Brevo delivers real-time event notifications via webhooks for transactional emails, marketing campaigns, transactional SMS, and conversations. When configured, Brevo sends HTTP POST requests to your s
  name: Brevo Webhook Events
  slug: brevo-webhooks-asyncapi
collections:
- collection_type: open
  name: Brevo Contacts API
  slug: open-brevo-contacts
- collection_type: open
  name: Brevo Conversations API
  slug: open-brevo-conversations
- collection_type: open
  name: Brevo eCommerce API
  slug: open-brevo-ecommerce
- collection_type: open
  name: Brevo Email Campaigns API
  slug: open-brevo-email-campaigns
- collection_type: open
  name: Brevo Transactional Email API
  slug: open-brevo-transactional-email
- collection_type: open
  name: Brevo Transactional SMS API
  slug: open-brevo-transactional-sms
- collection_type: open
  name: Brevo Webhooks API
  slug: open-brevo-webhooks
- collection_type: open
  name: Brevo WhatsApp API
  slug: open-brevo-whatsapp
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/brevo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brevo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brevo-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getbrevo
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brevo
- group: design
  title: ''
  type: JSONLD
  url: json-ld/brevo-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/brevo-contact-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/brevo-email-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/brevo-order-schema.json
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.brevo.com/llms.txt
description: Send transactional emails with static or dynamic content using the Messaging API.
finops:
- name: Brevo Finops
  service_category: Email & Marketing Automation
  slug: brevo-finops
graphqls:
- description: This document describes the conceptual GraphQL schema for the Brevo (formerly Sendinblue) API v3. Brevo is an all-in-one marketing platform providing email campaigns, transactional email, SMS messagin
  name: Brevo (Sendinblue) GraphQL Schema
  slug: brevo-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brevo.png
json_schemas:
- name: AggregatedEmailReport
  property_count: 13
  slug: brevo-aggregatedemailreport
- name: AggregatedSmsReport
  property_count: 7
  slug: brevo-aggregatedsmsreport
- name: AutomatedMessageResponse
  property_count: 5
  slug: brevo-automatedmessageresponse
- name: Category
  property_count: 5
  slug: brevo-category
- name: CategoryList
  property_count: 2
  slug: brevo-categorylist
- name: Brevo Contact
  property_count: 10
  slug: brevo-contact
- name: ContactAttributeList
  property_count: 1
  slug: brevo-contactattributelist
- name: ContactList
  property_count: 2
  slug: brevo-contactlist
- name: ContactListCollection
  property_count: 2
  slug: brevo-contactlistcollection
- name: ContactListDetail
  property_count: 6
  slug: brevo-contactlistdetail
- name: CreateAutomatedMessage
  property_count: 4
  slug: brevo-createautomatedmessage
- name: CreateContact
  property_count: 5
  slug: brevo-createcontact
- name: CreateContactAttribute
  property_count: 3
  slug: brevo-createcontactattribute
- name: CreateContactList
  property_count: 2
  slug: brevo-createcontactlist
- name: CreateEmailCampaign
  property_count: 9
  slug: brevo-createemailcampaign
- name: CreateSender
  property_count: 2
  slug: brevo-createsender
- name: CreateSenderResponse
  property_count: 1
  slug: brevo-createsenderresponse
- name: CreateSmtpTemplate
  property_count: 6
  slug: brevo-createsmtptemplate
- name: CreateTemplateResponse
  property_count: 1
  slug: brevo-createtemplateresponse
- name: CreateUpdateCategory
  property_count: 3
  slug: brevo-createupdatecategory
- name: CreateUpdateOrder
  property_count: 8
  slug: brevo-createupdateorder
- name: CreateUpdateProduct
  property_count: 8
  slug: brevo-createupdateproduct
- name: CreateWebhook
  property_count: 5
  slug: brevo-createwebhook
- name: CreateWhatsAppCampaign
  property_count: 4
  slug: brevo-createwhatsappcampaign
- name: CreateWhatsAppTemplate
  property_count: 6
  slug: brevo-createwhatsapptemplate
- name: Brevo Email Event
  property_count: 14
  slug: brevo-email-event
- name: EmailCampaign
  property_count: 11
  slug: brevo-emailcampaign
- name: EmailCampaignList
  property_count: 2
  slug: brevo-emailcampaignlist
- name: EmailEventReport
  property_count: 1
  slug: brevo-emaileventreport
- name: ErrorResponse
  property_count: 2
  slug: brevo-errorresponse
- name: FolderList
  property_count: 2
  slug: brevo-folderlist
- name: ImportContacts
  property_count: 9
  slug: brevo-importcontacts
- name: MessageResponse
  property_count: 7
  slug: brevo-messageresponse
- name: Brevo eCommerce Order
  property_count: 8
  slug: brevo-order
- name: OrderList
  property_count: 1
  slug: brevo-orderlist
- name: OrderProduct
  property_count: 4
  slug: brevo-orderproduct
- name: Product
  property_count: 10
  slug: brevo-product
- name: ProductList
  property_count: 2
  slug: brevo-productlist
- name: SendEmailResponse
  property_count: 1
  slug: brevo-sendemailresponse
- name: SenderList
  property_count: 1
  slug: brevo-senderlist
- name: SendMessage
  property_count: 4
  slug: brevo-sendmessage
- name: SendSmsResponse
  property_count: 5
  slug: brevo-sendsmsresponse
- name: SendTransactionalEmail
  property_count: 14
  slug: brevo-sendtransactionalemail
- name: SendTransactionalSms
  property_count: 6
  slug: brevo-sendtransactionalsms
- name: SendWhatsAppMessage
  property_count: 3
  slug: brevo-sendwhatsappmessage
- name: SendWhatsAppResponse
  property_count: 1
  slug: brevo-sendwhatsappresponse
- name: SmsEventReport
  property_count: 1
  slug: brevo-smseventreport
- name: SmsStatisticsReport
  property_count: 1
  slug: brevo-smsstatisticsreport
- name: SmtpTemplate
  property_count: 9
  slug: brevo-smtptemplate
- name: TemplateList
  property_count: 2
  slug: brevo-templatelist
- name: TransactionalEmailContent
  property_count: 5
  slug: brevo-transactionalemailcontent
- name: UpdateAutomatedMessage
  property_count: 1
  slug: brevo-updateautomatedmessage
- name: UpdateContact
  property_count: 5
  slug: brevo-updatecontact
- name: UpdateContactList
  property_count: 2
  slug: brevo-updatecontactlist
- name: UpdateEmailCampaign
  property_count: 6
  slug: brevo-updateemailcampaign
- name: UpdateSmtpTemplate
  property_count: 6
  slug: brevo-updatesmtptemplate
- name: UpdateWebhook
  property_count: 4
  slug: brevo-updatewebhook
- name: UpdateWhatsAppCampaign
  property_count: 4
  slug: brevo-updatewhatsappcampaign
- name: Webhook
  property_count: 8
  slug: brevo-webhook
- name: WebhookList
  property_count: 1
  slug: brevo-webhooklist
- name: WhatsAppCampaign
  property_count: 9
  slug: brevo-whatsappcampaign
- name: WhatsAppCampaignList
  property_count: 2
  slug: brevo-whatsappcampaignlist
- name: WhatsAppTemplateList
  property_count: 2
  slug: brevo-whatsapptemplatelist
json_structures:
- name: Brevo Structure
  property_count: 0
  slug: brevo-structure
jsonld:
- class_count: 0
  name: Brevo Context
  property_count: 10
  slug: brevo-context
layout: provider
modified: '2026-05-19'
name: brevo
nav: Providers
network: true
overview: 'brevo publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Agent Status API, Automated Messages API, Campaign Statistics API, and 20 more.


  The brevo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  brevo''s developer surface includes authentication and 9 more developer resources.'
plans:
- name: Brevo Plans Pricing
  plan_count: 4
  slug: brevo-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 10
  name: Brevo Rate Limits
  slug: brevo-rate-limits
rules:
- name: brevo API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: brevo-asyncapi-spectral-rules
- name: brevo API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: brevo-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 83.1
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 47.9
    operational_transparency: 36.8
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brevo/refs/heads/main/screenshots/brevo-2026-06-20T173653.png
security:
- kind: authentication
  name: Brevo Authentication
  slug: brevo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Brevo Domain Security
  slug: brevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: brevo
---
