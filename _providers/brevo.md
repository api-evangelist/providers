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
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 52.8
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 218
  human_in_the_loop: 4
  name: Brevo Agentic Access
  operation_count: 360
  slug: brevo-agentic-access
  summary_line: 360 operations · 218 acting · 4 human-in-the-loop
api_count: 21
apis:
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage agent online status for conversation availability.
  name: brevo Agent Status API
  slug: brevo-agent-status-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and retrieve automated messages pushed to visitors.
  name: brevo Automated Messages API
  slug: brevo-automated-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Retrieve performance metrics and statistics for email campaigns.
  name: brevo Campaign Statistics API
  slug: brevo-campaign-statistics-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage product categories for organizing the catalog.
  name: brevo Categories API
  slug: brevo-categories-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Define and manage custom attributes for contact profiles.
  name: brevo Contact Attributes API
  slug: brevo-contact-attributes-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage contact lists for organizing and segmenting audiences.
  name: brevo Contact Lists API
  slug: brevo-contact-lists-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, retrieve, update, and delete individual contacts.
  name: brevo Contacts API
  slug: brevo-contacts-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Track and retrieve transactional email activity including delivery status, opens, clicks, and bounces.
  name: brevo Email Activity API
  slug: brevo-email-activity-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, update, send, and manage marketing email campaigns.
  name: brevo Email Campaigns API
  slug: brevo-email-campaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage reusable email templates for transactional messaging.
  name: brevo Email Templates API
  slug: brevo-email-templates-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Organize contact lists into folders for better management.
  name: brevo Folders API
  slug: brevo-folders-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Bulk import contacts from files or data payloads.
  name: brevo Import API
  slug: brevo-import-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send and manage chat messages as an agent or automated bot within conversations.
  name: brevo Messages API
  slug: brevo-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage eCommerce order data for revenue attribution and purchase tracking.
  name: brevo Orders API
  slug: brevo-orders-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Import, manage, and retrieve eCommerce product data.
  name: brevo Products API
  slug: brevo-products-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Manage sender identities used for transactional email sending.
  name: brevo Senders API
  slug: brevo-senders-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Retrieve delivery reports and activity statistics for transactional SMS messages.
  name: brevo SMS Statistics API
  slug: brevo-sms-statistics-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send and manage transactional emails including order confirmations, password resets, and account notifications.
  name: brevo Transactional Emails API
  slug: brevo-transactional-emails-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send transactional SMS messages for notifications, verifications, and alerts.
  name: brevo Transactional SMS API
  slug: brevo-transactional-sms-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and configure webhook subscriptions for receiving real-time event notifications.
  name: brevo Webhooks API
  slug: brevo-webhooks-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create, manage, and send WhatsApp marketing campaigns.
  name: brevo WhatsApp Campaigns API
  slug: brevo-whatsapp-campaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Send transactional WhatsApp messages to recipients using approved templates or plain text.
  name: brevo WhatsApp Messages API
  slug: brevo-whatsapp-messages-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: Create and manage WhatsApp message templates that require Meta approval before use.
  name: brevo WhatsApp Templates API
  slug: brevo-whatsapp-templates-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The account API from Brevo — 2 operation(s) for account.
  name: Brevo Account API
  slug: brevo-account-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The balance API from Brevo — 12 operation(s) for balance.
  name: Brevo Balance API
  slug: brevo-balance-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The companies API from Brevo — 6 operation(s) for companies.
  name: Brevo Companies API
  slug: brevo-companies-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The consentGroups API from Brevo — 2 operation(s) for consentgroups.
  name: Brevo Consent Groups API
  slug: brevo-consentgroups-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The conversations API from Brevo — 6 operation(s) for conversations.
  name: Brevo Conversations API
  slug: brevo-conversations-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The coupons API from Brevo — 3 operation(s) for coupons.
  name: Brevo Coupons API
  slug: brevo-coupons-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The customObjects API from Brevo — 3 operation(s) for customobjects.
  name: Brevo Custom Objects API
  slug: brevo-customobjects-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The deals API from Brevo — 8 operation(s) for deals.
  name: Brevo Deals API
  slug: brevo-deals-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The domains API from Brevo — 3 operation(s) for domains.
  name: Brevo Domains API
  slug: brevo-domains-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The ecommerce API from Brevo — 15 operation(s) for ecommerce.
  name: Brevo Ecommerce API
  slug: brevo-ecommerce-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The emailCampaigns API from Brevo — 10 operation(s) for emailcampaigns.
  name: Brevo Email Campaigns API
  slug: brevo-emailcampaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The event API from Brevo — 2 operation(s) for event.
  name: Brevo Event API
  slug: brevo-event-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The externalFeeds API from Brevo — 2 operation(s) for externalfeeds.
  name: Brevo External Feeds API
  slug: brevo-externalfeeds-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The files API from Brevo — 3 operation(s) for files.
  name: Brevo Files API
  slug: brevo-files-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The inboundParsing API from Brevo — 3 operation(s) for inboundparsing.
  name: Brevo Inbound Parsing API
  slug: brevo-inboundparsing-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The masterAccount API from Brevo — 21 operation(s) for masteraccount.
  name: Brevo Master Account API
  slug: brevo-masteraccount-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The notes API from Brevo — 2 operation(s) for notes.
  name: Brevo Notes API
  slug: brevo-notes-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The payments API from Brevo — 2 operation(s) for payments.
  name: Brevo Payments API
  slug: brevo-payments-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The process API from Brevo — 2 operation(s) for process.
  name: Brevo Process API
  slug: brevo-process-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The program API from Brevo — 7 operation(s) for program.
  name: Brevo Program API
  slug: brevo-program-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The reward API from Brevo — 9 operation(s) for reward.
  name: Brevo Reward API
  slug: brevo-reward-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The smsCampaigns API from Brevo — 7 operation(s) for smscampaigns.
  name: Brevo Sms Campaigns API
  slug: brevo-smscampaigns-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The tasks API from Brevo — 3 operation(s) for tasks.
  name: Brevo Tasks API
  slug: brevo-tasks-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The tier API from Brevo — 6 operation(s) for tier.
  name: Brevo Tier API
  slug: brevo-tier-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The transactionalEmails API from Brevo — 18 operation(s) for transactionalemails.
  name: Brevo Transactional Emails API
  slug: brevo-transactionalemails-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The transactionalSms API from Brevo — 4 operation(s) for transactionalsms.
  name: Brevo Transactional Sms API
  slug: brevo-transactionalsms-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The transactionalWhatsApp API from Brevo — 2 operation(s) for transactionalwhatsapp.
  name: Brevo Transactional Whats App API
  slug: brevo-transactionalwhatsapp-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The user API from Brevo — 6 operation(s) for user.
  name: Brevo User API
  slug: brevo-user-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The wallet API from Brevo — 1 operation(s) for wallet.
  name: Brevo Wallet API
  slug: brevo-wallet-api
- baseURL: https://api.brevo.com/v3
  baseurl_source: declared
  description: The whatsAppCampaigns API from Brevo — 6 operation(s) for whatsappcampaigns.
  name: Brevo Whats App Campaigns API
  slug: brevo-whatsappcampaigns-api
artifact_total: 174
asyncapis:
- description: Brevo delivers real-time event notifications via webhooks for transactional emails, marketing campaigns, transactional SMS, and conversations. When configured, Brevo sends HTTP POST requests to your s
  name: Brevo Webhook Events
  slug: brevo-webhooks-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Accounts and Settings
  slug: open-brevo-accounts-and-settings
- collection_type: open
  name: Brevo Contacts Agent Status API
  slug: open-brevo-agent-status-api
- collection_type: open
  name: Brevo Contacts Agent Status Automated Messages API
  slug: open-brevo-automated-messages-api
- collection_type: open
  name: Brevo Contacts Agent Status Campaign Statistics API
  slug: open-brevo-campaign-statistics-api
- collection_type: open
  name: Brevo Contacts Agent Status Categories API
  slug: open-brevo-categories-api
- collection_type: open
  name: Brevo Contacts Agent Status Contact Attributes API
  slug: open-brevo-contact-attributes-api
- collection_type: open
  name: Brevo Contacts Agent Status Contact Lists API
  slug: open-brevo-contact-lists-api
- collection_type: open
  name: Contact Management
  slug: open-brevo-contact-management
- collection_type: open
  name: Brevo Agent Status Contacts API
  slug: open-brevo-contacts-api
- collection_type: open
  name: Brevo Contacts API
  slug: open-brevo-contacts
- collection_type: open
  name: Conversations
  slug: open-brevo-conversations
- collection_type: open
  name: Ecommerce
  slug: open-brevo-ecommerce
- collection_type: open
  name: Brevo Contacts Agent Status Email Activity API
  slug: open-brevo-email-activity-api
- collection_type: open
  name: Email API
  slug: open-brevo-email-api
- collection_type: open
  name: Brevo Contacts Agent Status Email Campaigns API
  slug: open-brevo-email-campaigns-api
- collection_type: open
  name: Brevo Email Campaigns API
  slug: open-brevo-email-campaigns
- collection_type: open
  name: Brevo Contacts Agent Status Email Templates API
  slug: open-brevo-email-templates-api
- collection_type: open
  name: Events
  slug: open-brevo-events
- collection_type: open
  name: Brevo Contacts Agent Status Folders API
  slug: open-brevo-folders-api
- collection_type: open
  name: Brevo Contacts Agent Status Import API
  slug: open-brevo-import-api
- collection_type: open
  name: Loyalty
  slug: open-brevo-loyalty
- collection_type: open
  name: Marketing Campaigns
  slug: open-brevo-marketing-campaigns
- collection_type: open
  name: Brevo Contacts Agent Status Messages API
  slug: open-brevo-messages-api
- collection_type: open
  name: Object Management
  slug: open-brevo-object-management
- collection_type: open
  name: Brevo Contacts Agent Status Orders API
  slug: open-brevo-orders-api
- collection_type: open
  name: Brevo Contacts Agent Status Products API
  slug: open-brevo-products-api
- collection_type: open
  name: Sales CRM
  slug: open-brevo-sales-crm
- collection_type: open
  name: Brevo Contacts Agent Status Senders API
  slug: open-brevo-senders-api
- collection_type: open
  name: Brevo Contacts Agent Status SMS Statistics API
  slug: open-brevo-sms-statistics-api
- collection_type: open
  name: Brevo Transactional Email API
  slug: open-brevo-transactional-email
- collection_type: open
  name: Brevo Contacts Agent Status Transactional Emails API
  slug: open-brevo-transactional-emails-api
- collection_type: open
  name: Brevo Contacts Agent Status Transactional SMS API
  slug: open-brevo-transactional-sms-api
- collection_type: open
  name: Transactional SMS
  slug: open-brevo-transactional-sms
- collection_type: open
  name: Transactional WhatsApp
  slug: open-brevo-transactional-whatsapp
- collection_type: open
  name: Wallet
  slug: open-brevo-wallet
- collection_type: open
  name: Brevo Contacts Agent Status Webhooks API
  slug: open-brevo-webhooks-api
- collection_type: open
  name: Brevo Webhooks API
  slug: open-brevo-webhooks
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Campaigns API
  slug: open-brevo-whatsapp-campaigns-api
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Messages API
  slug: open-brevo-whatsapp-messages-api
- collection_type: open
  name: Brevo Contacts Agent Status WhatsApp Templates API
  slug: open-brevo-whatsapp-templates-api
- collection_type: open
  name: Brevo WhatsApp API
  slug: open-brevo-whatsapp
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/brevo-capability-edges.yml
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
- group: docs
  title: ''
  type: OpenAPI
  url: https://developers.brevo.com/.well-known/api-catalog
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brevo-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/brevo-api-catalog.json
- group: build
  title: ''
  type: Packages
  url: packages/brevo-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/brevo-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/brevo-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brevo-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/brevo-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brevo-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/brevo-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/brevo-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brevo-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brevo-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brevo.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://developers.brevo.com/changelog/2026/5/12
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brevo-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.brevo.com/changelog
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brevo-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/brevo-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.brevo.com/features/data-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/brevo-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brevo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.brevo.com/legal/responsible-disclosure/
- group: start
  title: ''
  type: Sandbox
  url: sandbox/brevo-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/brevo-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brevo-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/brevo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/brevo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/brevo-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/brevo-vocabulary.yml
- group: design
  title: ''
  type: Webhooks
  url: https://developers.brevo.com/docs/how-to-use-webhooks
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/brevo-webhooks-asyncapi.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-email-api-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-transactional-sms-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-transactional-whatsapp-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-marketing-campaigns-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-contact-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-events-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-object-management-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-accounts-and-settings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-sales-crm-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-conversations-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-ecommerce-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-loyalty-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/brevo-wallet-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.brevo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.brevo.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://developers.brevo.com/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.brevo.com/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://help.brevo.com/
- group: company
  title: ''
  type: Blog
  url: https://www.brevo.com/blog/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/sib-apiv3/workspace/sendinblue
- group: commercial
  title: ''
  type: Pricing
  url: https://www.brevo.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://onboarding.brevo.com/account/register
- group: start
  title: ''
  type: Login
  url: https://app.brevo.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.brevo.com/legal/termsofuse/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.brevo.com/legal/privacypolicy/
- group: company
  title: ''
  type: Website
  url: https://www.brevo.com/
created: '2026-05-04'
description: Brevo (formerly Sendinblue) is a French customer-relationship platform that combines email marketing, transactional email and SMTP relay, transactional and campaign SMS, WhatsApp messaging, web and mobile push, live chat, a sales CRM, an ecommerce attribution layer and a loyalty and rewards engine behind a single REST API at api.brevo.com/v3. Brevo publishes thirteen OpenAPI 3.1 definitions covering 285 operations, advertises them through an RFC 9727 API catalog at its developer portal, ships seven official SDKs and a first-party CLI for OAuth app management, and operates a hosted MCP server exposing 27 modules to AI agents.
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
mcp_servers:
- description: Brevo ships a hosted, remote MCP server at https://mcp.brevo.com. An agent POSTs directly to the endpoint with a Bearer MCP token minted in the Brevo dashboard (Account > SMTP & API > API Keys, with t
  name: Brevo MCP Server
  slug: brevo-mcp-server
modified: '2026-08-13'
name: Brevo
nav: Providers
network: true
overview: 'Brevo publishes 53 APIs on the [APIs.io](https://apis.io/) network, including Agent Status API, Automated Messages API, Campaign Statistics API, and 50 more. Tagged areas include Marketing, Marketing Automation, Email Marketing, Transactional Email, and SMS Marketing.


  The Brevo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Brevo''s developer surface includes authentication, CLI, changelog, sandbox, documentation, API reference, getting-started guide, and 63 more developer resources.'
plans:
- name: Brevo Plans Pricing
  plan_count: 5
  slug: brevo-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 30
  name: Brevo Rate Limits
  slug: brevo-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Brevo API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: brevo-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Brevo API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: brevo-jsonschema-spectral-rules
scopes:
- name: Brevo Scopes
  scope_count: 37
  slug: brevo-scopes
  summary_line: 37 scopes · authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 84.2
  coverage:
    artifact_dirs: 35
    catalog_gap: 30.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 93.4
    commercial_clarity: 93.4
    contract_governance: 33.3
    contract_quality: 74.8
    developer_ergonomics: 80.4
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 92.1
  previous_composite: 84.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 53
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 73.6
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brevo/refs/heads/main/screenshots/brevo-2026-06-20T173653.png
security:
- kind: authentication
  name: Brevo Authentication
  slug: brevo-authentication
  summary_line: apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Brevo Domain Security
  slug: brevo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Brevo Vulnerability Disclosure
  slug: brevo-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Brevo Trust Center
  slug: brevo-trust-center
  summary_line: ISO/IEC 27001:2022
slug: brevo
tags:
- Marketing
- Marketing Automation
- Email Marketing
- Transactional Email
- SMS Marketing
- WhatsApp
- Campaigns
- CRM
- Sales
- E-Commerce
- Loyalty
- Event
- Live Chat
- Email
- SMS
- Automation
- Messaging
- Contacts
website: https://www.brevo.com/
---
