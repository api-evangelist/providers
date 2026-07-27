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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Ahasend Agentic Access
  operation_count: 44
  slug: ahasend-agentic-access
  summary_line: 44 operations · 25 acting
api_count: 11
apis:
- description: Manage account settings and members
  name: AhaSend Accounts API
  slug: ahasend-accounts-api
- description: Manage API keys for authentication and access control
  name: AhaSend API Keys API
  slug: ahasend-api-keys-api
- description: Manage sending domains
  name: AhaSend Domains API
  slug: ahasend-domains-api
- description: APIs for sending emails
  name: AhaSend Email API
  slug: ahasend-email-api
- description: Send and manage transactional messages
  name: AhaSend Messages API
  slug: ahasend-messages-api
- description: Manage inbound email routing
  name: AhaSend Routes API
  slug: ahasend-routes-api
- description: Manage SMTP authentication credentials
  name: AhaSend SMTP Credentials API
  slug: ahasend-smtp-credentials-api
- description: Access transactional email statistics
  name: AhaSend Statistics API
  slug: ahasend-statistics-api
- description: Manage email suppressions
  name: AhaSend Suppressions API
  slug: ahasend-suppressions-api
- description: Utility endpoints for health checks and diagnostics
  name: AhaSend Utility API
  slug: ahasend-utility-api
- description: Manage webhook notifications
  name: AhaSend Webhooks API
  slug: ahasend-webhooks-api
artifact_total: 233
collections:
- collection_type: open
  name: AhaSend Email API
  slug: open-ahasend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ahasend-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/ahasend-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ahasend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ahasend-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ahasend
- group: commercial
  title: ''
  type: Pricing
  url: https://ahasend.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://ahasend.com/blog
- group: operate
  title: ''
  type: Support
  url: https://ahasend.com/help
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ahasend.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ahasend.com/terms
- group: start
  title: ''
  type: Signup
  url: https://dash.ahasend.com/user/register
- group: start
  title: ''
  type: Login
  url: https://dash.ahasend.com/user/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AhaSend
- group: build
  title: Go SDK
  type: SDKs
  url: https://github.com/AhaSend/ahasend-go
- group: build
  title: ''
  type: CLI
  url: https://github.com/AhaSend/ahasend-cli
- group: build
  title: Java SDK
  type: SDKs
  url: https://github.com/AhaSend/ahasend-java-client
- group: other
  title: ''
  type: Affiliate
  url: https://ahasend.com/affiliates
- group: design
  title: ''
  type: SpectralRules
  url: rules/ahasend-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ahasend-vocabulary.yaml
created: '2025-02-06'
description: AhaSend is a developer-focused transactional email platform providing fast, reliable email delivery via REST API and SMTP relay. It offers features including email tracking, webhooks, email routing, suppression management, domain management, SMTP credentials, and detailed delivery statistics.
examples:
- key_count: 1
  name: Api Access Denied Response Example
  slug: api-access-denied-response-example
- key_count: 4
  name: Api Attachment Example
  slug: api-attachment-example
- key_count: 1
  name: Api Bad Request Response Example
  slug: api-bad-request-response-example
- key_count: 2
  name: Api Contact Example
  slug: api-contact-example
- key_count: 4
  name: Api Content Example
  slug: api-content-example
- key_count: 3
  name: Api Email Example
  slug: api-email-example
- key_count: 4
  name: Api Successful Response Example
  slug: api-successful-response-example
- key_count: 4
  name: Openapi V2 Account Example
  slug: openapi-v2-account-example
- key_count: 2
  name: Openapi V2 Account Members Response Example
  slug: openapi-v2-account-members-response-example
- key_count: 3
  name: Openapi V2 Add Member Request Example
  slug: openapi-v2-add-member-request-example
- key_count: 2
  name: Openapi V2 Address Example
  slug: openapi-v2-address-example
- key_count: 4
  name: Openapi V2 Api Key Example
  slug: openapi-v2-api-key-example
- key_count: 4
  name: Openapi V2 Api Key Scope Example
  slug: openapi-v2-api-key-scope-example
- key_count: 4
  name: Openapi V2 Attachment Example
  slug: openapi-v2-attachment-example
- key_count: 2
  name: Openapi V2 Bounce Example
  slug: openapi-v2-bounce-example
- key_count: 3
  name: Openapi V2 Bounce Statistics Example
  slug: openapi-v2-bounce-statistics-example
- key_count: 2
  name: Openapi V2 Bounce Statistics Response Example
  slug: openapi-v2-bounce-statistics-response-example
- key_count: 2
  name: Openapi V2 Create Api Key Request Example
  slug: openapi-v2-create-api-key-request-example
- key_count: 4
  name: Openapi V2 Create Conversation Message Request Example
  slug: openapi-v2-create-conversation-message-request-example
- key_count: 4
  name: Openapi V2 Create Domain Request Example
  slug: openapi-v2-create-domain-request-example
- key_count: 4
  name: Openapi V2 Create Message Request Example
  slug: openapi-v2-create-message-request-example
- key_count: 2
  name: Openapi V2 Create Message Response Example
  slug: openapi-v2-create-message-response-example
- key_count: 4
  name: Openapi V2 Create Route Request Example
  slug: openapi-v2-create-route-request-example
- key_count: 4
  name: Openapi V2 Create Single Message Response Example
  slug: openapi-v2-create-single-message-response-example
- key_count: 4
  name: Openapi V2 Create Smtp Credential Request Example
  slug: openapi-v2-create-smtp-credential-request-example
- key_count: 4
  name: Openapi V2 Create Suppression Request Example
  slug: openapi-v2-create-suppression-request-example
- key_count: 2
  name: Openapi V2 Create Suppression Response Example
  slug: openapi-v2-create-suppression-response-example
- key_count: 4
  name: Openapi V2 Create Webhook Request Example
  slug: openapi-v2-create-webhook-request-example
- key_count: 4
  name: Openapi V2 Deliverability Statistics Example
  slug: openapi-v2-deliverability-statistics-example
- key_count: 2
  name: Openapi V2 Deliverability Statistics Response Example
  slug: openapi-v2-deliverability-statistics-response-example
- key_count: 3
  name: Openapi V2 Delivery Event Example
  slug: openapi-v2-delivery-event-example
- key_count: 2
  name: Openapi V2 Delivery Time Example
  slug: openapi-v2-delivery-time-example
- key_count: 4
  name: Openapi V2 Delivery Time Statistics Example
  slug: openapi-v2-delivery-time-statistics-example
- key_count: 2
  name: Openapi V2 Delivery Time Statistics Response Example
  slug: openapi-v2-delivery-time-statistics-response-example
- key_count: 4
  name: Openapi V2 Dns Record Example
  slug: openapi-v2-dns-record-example
- key_count: 4
  name: Openapi V2 Domain Example
  slug: openapi-v2-domain-example
- key_count: 4
  name: Openapi V2 Message Attachment Example
  slug: openapi-v2-message-attachment-example
- key_count: 3
  name: Openapi V2 Message Content Parsed Example
  slug: openapi-v2-message-content-parsed-example
- key_count: 2
  name: Openapi V2 Message Content Part Example
  slug: openapi-v2-message-content-part-example
- key_count: 2
  name: Openapi V2 Message Schedule Example
  slug: openapi-v2-message-schedule-example
- key_count: 4
  name: Openapi V2 Message Summary Example
  slug: openapi-v2-message-summary-example
- key_count: 3
  name: Openapi V2 Paginated Api Keys Response Example
  slug: openapi-v2-paginated-api-keys-response-example
- key_count: 3
  name: Openapi V2 Paginated Domains Response Example
  slug: openapi-v2-paginated-domains-response-example
- key_count: 3
  name: Openapi V2 Paginated Messages Response Example
  slug: openapi-v2-paginated-messages-response-example
- key_count: 3
  name: Openapi V2 Paginated Routes Response Example
  slug: openapi-v2-paginated-routes-response-example
- key_count: 3
  name: Openapi V2 Paginated Smtp Credentials Response Example
  slug: openapi-v2-paginated-smtp-credentials-response-example
- key_count: 3
  name: Openapi V2 Paginated Suppressions Response Example
  slug: openapi-v2-paginated-suppressions-response-example
- key_count: 3
  name: Openapi V2 Paginated Webhooks Response Example
  slug: openapi-v2-paginated-webhooks-response-example
- key_count: 3
  name: Openapi V2 Pagination Info Example
  slug: openapi-v2-pagination-info-example
- key_count: 3
  name: Openapi V2 Recipient Example
  slug: openapi-v2-recipient-example
- key_count: 2
  name: Openapi V2 Retention Example
  slug: openapi-v2-retention-example
- key_count: 4
  name: Openapi V2 Route Example
  slug: openapi-v2-route-example
- key_count: 4
  name: Openapi V2 Smtp Credential Example
  slug: openapi-v2-smtp-credential-example
- key_count: 4
  name: Openapi V2 Suppression Example
  slug: openapi-v2-suppression-example
- key_count: 2
  name: Openapi V2 Tracking Example
  slug: openapi-v2-tracking-example
- key_count: 4
  name: Openapi V2 Update Account Request Example
  slug: openapi-v2-update-account-request-example
- key_count: 2
  name: Openapi V2 Update Api Key Request Example
  slug: openapi-v2-update-api-key-request-example
- key_count: 4
  name: Openapi V2 Update Domain Request Example
  slug: openapi-v2-update-domain-request-example
- key_count: 4
  name: Openapi V2 Update Route Request Example
  slug: openapi-v2-update-route-request-example
- key_count: 4
  name: Openapi V2 Update Webhook Request Example
  slug: openapi-v2-update-webhook-request-example
- key_count: 4
  name: Openapi V2 User Account Example
  slug: openapi-v2-user-account-example
- key_count: 4
  name: Openapi V2 Webhook Example
  slug: openapi-v2-webhook-example
features:
- description: Fast delivery of transactional emails including OTPs and confirmations, targeting sub-2-second delivery to Gmail at 99th percentile.
  name: Transactional Email Delivery
- description: Track email opens and link clicks with real-time analytics.
  name: Email Tracking
- description: Real-time webhook events for delivery, bounces, opens, clicks, and account alerts.
  name: Webhook Notifications
- description: Route incoming emails to HTTP endpoints with automatic parsing of signatures and quoted replies.
  name: Email Routing
- description: Automated handling of bounces, complaints, and unsubscribes with suppression lists.
  name: Suppression Management
- description: Manage sending domains including DNS validation, DKIM rotation, and whitelabeling.
  name: Domain Management
- description: Compatible SMTP relay supporting any programming language or software.
  name: SMTP Relay
- description: Free dedicated IPs for high-volume senders exceeding 300k emails per month.
  name: Dedicated IPs
- description: Archive emails to S3-compatible storage with configurable retention policies.
  name: S3-Compatible Archiving
- description: Enterprise single sign-on via OpenID Connect with granular API credential scoping.
  name: SSO with OIDC
finops:
- name: Ahasend Finops
  service_category: API
  slug: ahasend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ahasend.png
integrations:
- description: Native Node.js integration with code examples and SDK support.
  name: Node.js
- description: Python integration examples for sending emails via API or SMTP.
  name: Python
- description: PHP integration including Symfony Mailer transport support.
  name: PHP / Symfony
- description: Ruby integration with Rails ActionMailer transport.
  name: Ruby on Rails
- description: Official Go SDK for the AhaSend API.
  name: Go
- description: WordPress plugin for routing site emails through AhaSend.
  name: WordPress
- description: Java client generated from OpenAPI spec.
  name: Java
json_schemas:
- name: AccessDeniedResponse
  property_count: 1
  slug: api-access-denied-response
- name: Attachment
  property_count: 5
  slug: api-attachment
- name: BadRequestResponse
  property_count: 1
  slug: api-bad-request-response
- name: Contact
  property_count: 2
  slug: api-contact
- name: Content
  property_count: 6
  slug: api-content
- name: Email
  property_count: 3
  slug: api-email
- name: SuccessfulResponse
  property_count: 4
  slug: api-successful-response
- name: AccountMembersResponse
  property_count: 2
  slug: openapi-v2-account-members-response
- name: Account
  property_count: 13
  slug: openapi-v2-account
- name: AddMemberRequest
  property_count: 3
  slug: openapi-v2-add-member-request
- name: Address
  property_count: 2
  slug: openapi-v2-address
- name: APIKey
  property_count: 10
  slug: openapi-v2-api-key
- name: APIKeyScope
  property_count: 6
  slug: openapi-v2-api-key-scope
- name: Attachment
  property_count: 6
  slug: openapi-v2-attachment
- name: Bounce
  property_count: 2
  slug: openapi-v2-bounce
- name: BounceStatisticsResponse
  property_count: 2
  slug: openapi-v2-bounce-statistics-response
- name: BounceStatistics
  property_count: 3
  slug: openapi-v2-bounce-statistics
- name: CreateAPIKeyRequest
  property_count: 2
  slug: openapi-v2-create-api-key-request
- name: CreateConversationMessageRequest
  property_count: 17
  slug: openapi-v2-create-conversation-message-request
- name: CreateDomainRequest
  property_count: 7
  slug: openapi-v2-create-domain-request
- name: CreateMessageRequest
  property_count: 16
  slug: openapi-v2-create-message-request
- name: CreateMessageResponse
  property_count: 2
  slug: openapi-v2-create-message-response
- name: CreateRouteRequest
  property_count: 8
  slug: openapi-v2-create-route-request
- name: CreateSingleMessageResponse
  property_count: 6
  slug: openapi-v2-create-single-message-response
- name: CreateSMTPCredentialRequest
  property_count: 4
  slug: openapi-v2-create-smtp-credential-request
- name: CreateSuppressionRequest
  property_count: 4
  slug: openapi-v2-create-suppression-request
- name: CreateSuppressionResponse
  property_count: 2
  slug: openapi-v2-create-suppression-response
- name: CreateWebhookRequest
  property_count: 15
  slug: openapi-v2-create-webhook-request
- name: DeliverabilityStatisticsResponse
  property_count: 2
  slug: openapi-v2-deliverability-statistics-response
- name: DeliverabilityStatistics
  property_count: 10
  slug: openapi-v2-deliverability-statistics
- name: DeliveryEvent
  property_count: 3
  slug: openapi-v2-delivery-event
- name: DeliveryTime
  property_count: 2
  slug: openapi-v2-delivery-time
- name: DeliveryTimeStatisticsResponse
  property_count: 2
  slug: openapi-v2-delivery-time-statistics-response
- name: DeliveryTimeStatistics
  property_count: 5
  slug: openapi-v2-delivery-time-statistics
- name: DNSRecord
  property_count: 5
  slug: openapi-v2-dns-record
- name: Domain
  property_count: 15
  slug: openapi-v2-domain
- name: MessageAttachment
  property_count: 4
  slug: openapi-v2-message-attachment
- name: MessageContentParsed
  property_count: 3
  slug: openapi-v2-message-content-parsed
- name: MessageContentPart
  property_count: 2
  slug: openapi-v2-message-content-part
- name: MessageSchedule
  property_count: 2
  slug: openapi-v2-message-schedule
- name: Message
  property_count: 0
  slug: openapi-v2-message
- name: MessageSummary
  property_count: 23
  slug: openapi-v2-message-summary
- name: PaginatedAPIKeysResponse
  property_count: 3
  slug: openapi-v2-paginated-api-keys-response
- name: PaginatedDomainsResponse
  property_count: 3
  slug: openapi-v2-paginated-domains-response
- name: PaginatedMessagesResponse
  property_count: 3
  slug: openapi-v2-paginated-messages-response
- name: PaginatedRoutesResponse
  property_count: 3
  slug: openapi-v2-paginated-routes-response
- name: PaginatedSMTPCredentialsResponse
  property_count: 3
  slug: openapi-v2-paginated-smtp-credentials-response
- name: PaginatedSuppressionsResponse
  property_count: 3
  slug: openapi-v2-paginated-suppressions-response
- name: PaginatedWebhooksResponse
  property_count: 3
  slug: openapi-v2-paginated-webhooks-response
- name: PaginationInfo
  property_count: 3
  slug: openapi-v2-pagination-info
- name: Recipient
  property_count: 3
  slug: openapi-v2-recipient
- name: Retention
  property_count: 2
  slug: openapi-v2-retention
- name: Route
  property_count: 16
  slug: openapi-v2-route
- name: SMTPCredential
  property_count: 9
  slug: openapi-v2-smtp-credential
- name: Suppression
  property_count: 8
  slug: openapi-v2-suppression
- name: Tracking
  property_count: 2
  slug: openapi-v2-tracking
- name: UpdateAccountRequest
  property_count: 9
  slug: openapi-v2-update-account-request
- name: UpdateAPIKeyRequest
  property_count: 2
  slug: openapi-v2-update-api-key-request
- name: UpdateDomainRequest
  property_count: 5
  slug: openapi-v2-update-domain-request
- name: UpdateRouteRequest
  property_count: 8
  slug: openapi-v2-update-route-request
- name: UpdateWebhookRequest
  property_count: 15
  slug: openapi-v2-update-webhook-request
- name: UserAccount
  property_count: 6
  slug: openapi-v2-user-account
- name: Webhook
  property_count: 23
  slug: openapi-v2-webhook
json_structures:
- name: Api Access Denied Response Structure
  property_count: 1
  slug: api-access-denied-response-structure
- name: Api Attachment Structure
  property_count: 5
  slug: api-attachment-structure
- name: Api Bad Request Response Structure
  property_count: 1
  slug: api-bad-request-response-structure
- name: Api Contact Structure
  property_count: 2
  slug: api-contact-structure
- name: Api Content Structure
  property_count: 6
  slug: api-content-structure
- name: Api Email Structure
  property_count: 3
  slug: api-email-structure
- name: Api Successful Response Structure
  property_count: 4
  slug: api-successful-response-structure
- name: Openapi V2 Account Members Response Structure
  property_count: 2
  slug: openapi-v2-account-members-response-structure
- name: Openapi V2 Account Structure
  property_count: 13
  slug: openapi-v2-account-structure
- name: Openapi V2 Add Member Request Structure
  property_count: 3
  slug: openapi-v2-add-member-request-structure
- name: Openapi V2 Address Structure
  property_count: 2
  slug: openapi-v2-address-structure
- name: Openapi V2 Api Key Scope Structure
  property_count: 6
  slug: openapi-v2-api-key-scope-structure
- name: Openapi V2 Api Key Structure
  property_count: 10
  slug: openapi-v2-api-key-structure
- name: Openapi V2 Attachment Structure
  property_count: 6
  slug: openapi-v2-attachment-structure
- name: Openapi V2 Bounce Statistics Response Structure
  property_count: 2
  slug: openapi-v2-bounce-statistics-response-structure
- name: Openapi V2 Bounce Statistics Structure
  property_count: 3
  slug: openapi-v2-bounce-statistics-structure
- name: Openapi V2 Bounce Structure
  property_count: 2
  slug: openapi-v2-bounce-structure
- name: Openapi V2 Create Api Key Request Structure
  property_count: 2
  slug: openapi-v2-create-api-key-request-structure
- name: Openapi V2 Create Conversation Message Request Structure
  property_count: 17
  slug: openapi-v2-create-conversation-message-request-structure
- name: Openapi V2 Create Domain Request Structure
  property_count: 7
  slug: openapi-v2-create-domain-request-structure
- name: Openapi V2 Create Message Request Structure
  property_count: 16
  slug: openapi-v2-create-message-request-structure
- name: Openapi V2 Create Message Response Structure
  property_count: 2
  slug: openapi-v2-create-message-response-structure
- name: Openapi V2 Create Route Request Structure
  property_count: 8
  slug: openapi-v2-create-route-request-structure
- name: Openapi V2 Create Single Message Response Structure
  property_count: 6
  slug: openapi-v2-create-single-message-response-structure
- name: Openapi V2 Create Smtp Credential Request Structure
  property_count: 4
  slug: openapi-v2-create-smtp-credential-request-structure
- name: Openapi V2 Create Suppression Request Structure
  property_count: 4
  slug: openapi-v2-create-suppression-request-structure
- name: Openapi V2 Create Suppression Response Structure
  property_count: 2
  slug: openapi-v2-create-suppression-response-structure
- name: Openapi V2 Create Webhook Request Structure
  property_count: 15
  slug: openapi-v2-create-webhook-request-structure
- name: Openapi V2 Deliverability Statistics Response Structure
  property_count: 2
  slug: openapi-v2-deliverability-statistics-response-structure
- name: Openapi V2 Deliverability Statistics Structure
  property_count: 10
  slug: openapi-v2-deliverability-statistics-structure
- name: Openapi V2 Delivery Event Structure
  property_count: 3
  slug: openapi-v2-delivery-event-structure
- name: Openapi V2 Delivery Time Statistics Response Structure
  property_count: 2
  slug: openapi-v2-delivery-time-statistics-response-structure
- name: Openapi V2 Delivery Time Statistics Structure
  property_count: 5
  slug: openapi-v2-delivery-time-statistics-structure
- name: Openapi V2 Delivery Time Structure
  property_count: 2
  slug: openapi-v2-delivery-time-structure
- name: Openapi V2 Dns Record Structure
  property_count: 5
  slug: openapi-v2-dns-record-structure
- name: Openapi V2 Domain Structure
  property_count: 15
  slug: openapi-v2-domain-structure
- name: Openapi V2 Message Attachment Structure
  property_count: 4
  slug: openapi-v2-message-attachment-structure
- name: Openapi V2 Message Content Parsed Structure
  property_count: 3
  slug: openapi-v2-message-content-parsed-structure
- name: Openapi V2 Message Content Part Structure
  property_count: 2
  slug: openapi-v2-message-content-part-structure
- name: Openapi V2 Message Schedule Structure
  property_count: 2
  slug: openapi-v2-message-schedule-structure
- name: Openapi V2 Message Structure
  property_count: 0
  slug: openapi-v2-message-structure
- name: Openapi V2 Message Summary Structure
  property_count: 23
  slug: openapi-v2-message-summary-structure
- name: Openapi V2 Paginated Api Keys Response Structure
  property_count: 3
  slug: openapi-v2-paginated-api-keys-response-structure
- name: Openapi V2 Paginated Domains Response Structure
  property_count: 3
  slug: openapi-v2-paginated-domains-response-structure
- name: Openapi V2 Paginated Messages Response Structure
  property_count: 3
  slug: openapi-v2-paginated-messages-response-structure
- name: Openapi V2 Paginated Routes Response Structure
  property_count: 3
  slug: openapi-v2-paginated-routes-response-structure
- name: Openapi V2 Paginated Smtp Credentials Response Structure
  property_count: 3
  slug: openapi-v2-paginated-smtp-credentials-response-structure
- name: Openapi V2 Paginated Suppressions Response Structure
  property_count: 3
  slug: openapi-v2-paginated-suppressions-response-structure
- name: Openapi V2 Paginated Webhooks Response Structure
  property_count: 3
  slug: openapi-v2-paginated-webhooks-response-structure
- name: Openapi V2 Pagination Info Structure
  property_count: 3
  slug: openapi-v2-pagination-info-structure
- name: Openapi V2 Recipient Structure
  property_count: 3
  slug: openapi-v2-recipient-structure
- name: Openapi V2 Retention Structure
  property_count: 2
  slug: openapi-v2-retention-structure
- name: Openapi V2 Route Structure
  property_count: 16
  slug: openapi-v2-route-structure
- name: Openapi V2 Smtp Credential Structure
  property_count: 9
  slug: openapi-v2-smtp-credential-structure
- name: Openapi V2 Suppression Structure
  property_count: 8
  slug: openapi-v2-suppression-structure
- name: Openapi V2 Tracking Structure
  property_count: 2
  slug: openapi-v2-tracking-structure
- name: Openapi V2 Update Account Request Structure
  property_count: 9
  slug: openapi-v2-update-account-request-structure
- name: Openapi V2 Update Api Key Request Structure
  property_count: 2
  slug: openapi-v2-update-api-key-request-structure
- name: Openapi V2 Update Domain Request Structure
  property_count: 5
  slug: openapi-v2-update-domain-request-structure
- name: Openapi V2 Update Route Request Structure
  property_count: 8
  slug: openapi-v2-update-route-request-structure
- name: Openapi V2 Update Webhook Request Structure
  property_count: 15
  slug: openapi-v2-update-webhook-request-structure
- name: Openapi V2 User Account Structure
  property_count: 6
  slug: openapi-v2-user-account-structure
- name: Openapi V2 Webhook Structure
  property_count: 23
  slug: openapi-v2-webhook-structure
jsonld:
- class_count: 9
  name: Ahasend Api Context
  property_count: 19
  slug: ahasend-api-context
- class_count: 60
  name: Ahasend Openapi V2 Context
  property_count: 129
  slug: ahasend-openapi-v2-context
layout: provider
modified: '2026-04-19'
name: AhaSend
nav: Providers
network: true
overview: 'AhaSend publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, API Keys API, Domains API, and 8 more. Tagged areas include Email, Transactional Email, Developer Tools, SMTP, and Webhooks.


  The AhaSend catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  AhaSend''s developer surface includes authentication, pricing, engineering blog, support, signup flow, CLI, and 13 more developer resources.'
plans:
- name: Ahasend Plans Pricing
  plan_count: 3
  slug: ahasend-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Ahasend Rate Limits
  slug: ahasend-rate-limits
rules:
- name: AhaSend API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: ahasend-jsonschema-spectral-rules
- name: AhaSend API Rules
  rule_count: 38
  severity_counts:
    error: 11
    hint: 0
    info: 3
    warn: 24
  slug: ahasend-spectral-rules
score:
  band: strong
  composite: 64.9
  delta: 2.0
  facets:
    commercial_clarity: 84.2
    contract_quality: 72.0
    developer_ergonomics: 30.4
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 36.8
  previous_composite: 62.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ahasend/refs/heads/main/screenshots/ahasend-2026-06-20T170542.png
security:
- kind: authentication
  name: Ahasend Authentication
  slug: ahasend-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Ahasend Domain Security
  slug: ahasend-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Ahasend Vulnerability Disclosure
  slug: ahasend-vulnerability-disclosure
  summary_line: disclosure policy published
slug: ahasend
tags:
- Email
- Transactional Email
- Developer Tools
- SMTP
- Webhooks
use_cases:
- description: Send secure one-time password and password reset links with guaranteed fast delivery.
  name: Password Reset Emails
- description: Deliver account verification emails for new user signups.
  name: Email Verification
- description: Transactional order and shipping confirmation emails for e-commerce.
  name: Order Confirmation Emails
- description: Programmatic email alerts and notifications from applications and infrastructure.
  name: System Alerts
- description: Route and process incoming emails in applications using email routing.
  name: Inbound Email Processing
---
