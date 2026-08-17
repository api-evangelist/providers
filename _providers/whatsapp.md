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
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.3
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Whatsapp Agentic Access
  operation_count: 43
  slug: whatsapp-agentic-access
  summary_line: 43 operations · 27 acting
api_count: 17
apis:
- description: 'API for creating structured, interactive forms and multi-step flows within WhatsApp conversations, enabling appointment booking, surveys, lead capture, and other guided experiences using a JSON-based '
  name: WhatsApp Flows API
  slug: flows-api
- description: 'The self-hosted version of the WhatsApp Business API that allowed businesses to run the API on their own infrastructure. This API was deprecated on October 23, 2025, and all users must migrate to the '
  name: WhatsApp On-Premises API
  slug: on-premises-api
- description: Retrieve conversation and template analytics
  name: WhatsApp Analytics API
  slug: whatsapp-analytics-api
- description: Upload and retrieve flow JSON assets
  name: WhatsApp Assets API
  slug: whatsapp-assets-api
- description: Manage user access to a WABA
  name: WhatsApp Assigned Users API
  slug: whatsapp-assigned-users-api
- description: Manage WhatsApp Business Account information
  name: WhatsApp Business Accounts API
  slug: whatsapp-business-accounts-api
- description: Get and update WhatsApp Business profile information
  name: WhatsApp Business Profile API
  slug: whatsapp-business-profile-api
- description: Publish and deprecate flows
  name: WhatsApp Lifecycle API
  slug: whatsapp-lifecycle-api
- description: Upload, retrieve, and delete media files
  name: WhatsApp Media API
  slug: whatsapp-media-api
- description: Create, update, and delete message templates
  name: WhatsApp Message Templates API
  slug: whatsapp-message-templates-api
- description: Send messages of all types to WhatsApp users
  name: WhatsApp Messages API
  slug: whatsapp-messages-api
- description: List and manage phone numbers on a WABA
  name: WhatsApp Phone Numbers API
  slug: whatsapp-phone-numbers-api
- description: Connect and manage product catalogs
  name: WhatsApp Product Catalogs API
  slug: whatsapp-product-catalogs-api
- description: Create and manage QR codes for customer conversations
  name: WhatsApp QR Codes API
  slug: whatsapp-qr-codes-api
- description: Register and deregister phone numbers
  name: WhatsApp Registration API
  slug: whatsapp-registration-api
- description: Manage webhook subscriptions for a WABA
  name: WhatsApp Subscribed Apps API
  slug: whatsapp-subscribed-apps-api
- description: Manage two-step verification PIN
  name: WhatsApp Two-Step Verification API
  slug: whatsapp-two-step-verification-api
arazzos:
- description: Create a click-to-chat QR code and read back its deep link and image URLs.
  name: WhatsApp Create and Retrieve QR Code
  slug: whatsapp-create-qr-code-workflow
- description: Create a new message template and send it once it is available.
  name: WhatsApp Create Template then Send
  slug: whatsapp-create-template-then-send-workflow
- description: Create a flow, upload its JSON, publish it, and send it as an interactive flow message.
  name: WhatsApp Build, Publish, and Send a Flow
  slug: whatsapp-publish-flow-and-send-workflow
- description: Request a verification code, verify it, then register the phone number.
  name: WhatsApp Verify and Register Phone Number
  slug: whatsapp-register-phone-number-workflow
- description: Send a text message and then apply an emoji reaction to that same message.
  name: WhatsApp Send Message then React to It
  slug: whatsapp-send-and-react-workflow
- description: Confirm the sending number is verified, then send an interactive reply-button message.
  name: WhatsApp Check Number then Send Interactive Buttons
  slug: whatsapp-send-interactive-buttons-workflow
- description: Read the business profile to confirm the sender, then send a location pin.
  name: WhatsApp Confirm Profile then Send Location
  slug: whatsapp-send-location-message-workflow
- description: Look up an approved message template by name and send it to a recipient.
  name: WhatsApp Find Approved Template and Send
  slug: whatsapp-send-template-message-workflow
- description: Send a text reply and mark the customer's inbound message as read.
  name: WhatsApp Send Text and Mark Inbound Read
  slug: whatsapp-send-text-and-mark-read-workflow
- description: Confirm the WABA is active, subscribe the app to webhooks, then list subscriptions.
  name: WhatsApp Subscribe App to WABA Webhooks
  slug: whatsapp-subscribe-webhooks-workflow
- description: Read the current business profile, then apply updates to it.
  name: WhatsApp Read and Update Business Profile
  slug: whatsapp-update-business-profile-workflow
- description: Locate a template by name and edit its body, when it is in an editable state.
  name: WhatsApp Find and Update Message Template
  slug: whatsapp-update-template-workflow
- description: Upload a document file and send it to a recipient with a display filename.
  name: WhatsApp Upload and Send Document
  slug: whatsapp-upload-media-send-document-workflow
- description: Upload an image to WhatsApp servers and send it to a recipient by media ID.
  name: WhatsApp Upload Media and Send Image Message
  slug: whatsapp-upload-media-send-image-workflow
artifact_total: 194
asyncapis:
- description: 'WhatsApp Business Platform webhooks deliver real-time notifications for incoming messages, message status updates, template status changes, account updates, phone number quality changes, and security '
  name: WhatsApp Webhooks
  slug: whatsapp-webhooks-asyncapi
collections:
- collection_type: postman
  name: WhatsApp Business Management API
  slug: postman-whatsapp-business-management-api
- collection_type: postman
  name: WhatsApp Cloud API
  slug: postman-whatsapp-cloud-api
- collection_type: postman
  name: WhatsApp Flows API
  slug: postman-whatsapp-flows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: WhatsApp Business Management Analytics API
  slug: open-whatsapp-analytics-api
- collection_type: open
  name: WhatsApp Business Management Analytics Assets API
  slug: open-whatsapp-assets-api
- collection_type: open
  name: WhatsApp Business Management Analytics Assigned Users API
  slug: open-whatsapp-assigned-users-api
- collection_type: open
  name: WhatsApp Business Management Analytics Business Accounts API
  slug: open-whatsapp-business-accounts-api
- collection_type: open
  name: WhatsApp Business Management API
  slug: open-whatsapp-business-management-api
- collection_type: open
  name: WhatsApp Business Management Analytics Business Profile API
  slug: open-whatsapp-business-profile-api
- collection_type: open
  name: WhatsApp Cloud API
  slug: open-whatsapp-cloud-api
- collection_type: open
  name: WhatsApp Business Management Analytics Flows API
  slug: open-whatsapp-flows-api
- collection_type: open
  name: WhatsApp Business Management Analytics Lifecycle API
  slug: open-whatsapp-lifecycle-api
- collection_type: open
  name: WhatsApp Business Management Analytics Media API
  slug: open-whatsapp-media-api
- collection_type: open
  name: WhatsApp Business Management Analytics Message Templates API
  slug: open-whatsapp-message-templates-api
- collection_type: open
  name: WhatsApp Business Management Analytics Messages API
  slug: open-whatsapp-messages-api
- collection_type: open
  name: WhatsApp Business Management Analytics Phone Numbers API
  slug: open-whatsapp-phone-numbers-api
- collection_type: open
  name: WhatsApp Business Management Analytics Product Catalogs API
  slug: open-whatsapp-product-catalogs-api
- collection_type: open
  name: WhatsApp Business Management Analytics QR Codes API
  slug: open-whatsapp-qr-codes-api
- collection_type: open
  name: WhatsApp Business Management Analytics Registration API
  slug: open-whatsapp-registration-api
- collection_type: open
  name: WhatsApp Business Management Analytics Subscribed Apps API
  slug: open-whatsapp-subscribed-apps-api
- collection_type: open
  name: WhatsApp Business Management Analytics Two-Step Verification API
  slug: open-whatsapp-two-step-verification-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/WhatsApp/WhatsApp-Flows-Tools/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whatsapp-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whatsapp-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/whatsapp/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-create-qr-code-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-create-template-then-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-publish-flow-and-send-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-register-phone-number-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-and-react-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-interactive-buttons-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-location-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-template-message-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-text-and-mark-read-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-subscribe-webhooks-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-update-business-profile-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-update-template-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-upload-media-send-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-upload-media-send-image-workflow.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.whatsapp.com/legal/business-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.whatsapp.com/legal/privacy-policy-eea
- group: other
  title: ''
  type: Commerce Policy
  url: https://www.whatsapp.com/legal/commerce-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.facebook.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/docs/whatsapp/business-management-api/get-started
- group: other
  title: ''
  type: Best Practices
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/best-practices
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://metastatus.com/
- group: company
  title: ''
  type: Blog
  url: https://business.whatsapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/support/
- group: start
  title: ''
  type: Console
  url: https://developers.facebook.com/apps/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/WhatsApp
- group: operate
  title: ''
  type: Community
  url: https://business.whatsapp.com/developers/developer-hub
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/whatsapp-cloud-api
- group: auth
  title: ''
  type: Security
  url: https://www.whatsapp.com/security/WhatsApp-Security-Whitepaper.pdf
- group: build
  title: ''
  type: PostmanCollection
  url: https://www.postman.com/meta/whatsapp-business-platform/overview
- group: commercial
  title: ''
  type: Pricing
  url: https://business.whatsapp.com/products/platform-pricing
- group: design
  title: ''
  type: JSONLD
  url: json-ld/whatsapp-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/whatsapp-webhook-payload-schema.json
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/WhatsApp/WhatsApp-Nodejs-SDK
- group: build
  title: ''
  type: ApiExamples
  url: https://github.com/fbsamples/whatsapp-api-examples
- group: other
  title: ''
  type: Business Messaging Policy
  url: https://business.whatsapp.com/policy
- group: commercial
  title: ''
  type: Meta Terms
  url: https://www.whatsapp.com/legal/meta-terms-whatsapp-business
- group: operate
  title: ''
  type: FAQ
  url: https://business.whatsapp.com/resources/faq
- group: start
  title: ''
  type: Sandbox
  url: https://business.whatsapp.com/developers/developer-hub
- group: design
  title: ''
  type: Versioning
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- group: docs
  title: ''
  type: Migration Guide
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/migrate-to-cloud-api
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.facebook.com/docs/whatsapp/cloud-api/support/error-codes
created: '2024-01-15'
description: APIs for the WhatsApp messaging platform, enabling businesses to communicate with customers through the world's most popular messaging app.
examples:
- key_count: 1
  name: Whatsapp Business Management Api Conversation Analytics Example
  slug: whatsapp-business-management-api-conversation-analytics-example
- key_count: 5
  name: Whatsapp Business Management Api Create Template Request Example
  slug: whatsapp-business-management-api-create-template-request-example
- key_count: 3
  name: Whatsapp Business Management Api Cursor Paging Example
  slug: whatsapp-business-management-api-cursor-paging-example
- key_count: 8
  name: Whatsapp Business Management Api Message Template Example
  slug: whatsapp-business-management-api-message-template-example
- key_count: 10
  name: Whatsapp Business Management Api Phone Number Example
  slug: whatsapp-business-management-api-phone-number-example
- key_count: 1
  name: Whatsapp Business Management Api Success Response Example
  slug: whatsapp-business-management-api-success-response-example
- key_count: 1
  name: Whatsapp Business Management Api Template Analytics Example
  slug: whatsapp-business-management-api-template-analytics-example
- key_count: 8
  name: Whatsapp Business Management Api Template Button Example
  slug: whatsapp-business-management-api-template-button-example
- key_count: 7
  name: Whatsapp Business Management Api Template Component Definition Example
  slug: whatsapp-business-management-api-template-component-definition-example
- key_count: 10
  name: Whatsapp Business Management Api Whats App Business Account Example
  slug: whatsapp-business-management-api-whats-app-business-account-example
- key_count: 2
  name: Whatsapp Cloud Api Audio Object Example
  slug: whatsapp-cloud-api-audio-object-example
- key_count: 7
  name: Whatsapp Cloud Api Contact Object Example
  slug: whatsapp-cloud-api-contact-object-example
- key_count: 4
  name: Whatsapp Cloud Api Document Object Example
  slug: whatsapp-cloud-api-document-object-example
- key_count: 5
  name: Whatsapp Cloud Api Interactive Message Example
  slug: whatsapp-cloud-api-interactive-message-example
- key_count: 2
  name: Whatsapp Cloud Api List Section Example
  slug: whatsapp-cloud-api-list-section-example
- key_count: 4
  name: Whatsapp Cloud Api Location Message Example
  slug: whatsapp-cloud-api-location-message-example
- key_count: 3
  name: Whatsapp Cloud Api Media Object Example
  slug: whatsapp-cloud-api-media-object-example
- key_count: 2
  name: Whatsapp Cloud Api Reaction Message Example
  slug: whatsapp-cloud-api-reaction-message-example
- key_count: 10
  name: Whatsapp Cloud Api Send Message Request Example
  slug: whatsapp-cloud-api-send-message-request-example
- key_count: 3
  name: Whatsapp Cloud Api Send Message Response Example
  slug: whatsapp-cloud-api-send-message-response-example
- key_count: 2
  name: Whatsapp Cloud Api Sticker Object Example
  slug: whatsapp-cloud-api-sticker-object-example
- key_count: 4
  name: Whatsapp Cloud Api Template Component Example
  slug: whatsapp-cloud-api-template-component-example
- key_count: 3
  name: Whatsapp Cloud Api Template Message Example
  slug: whatsapp-cloud-api-template-message-example
- key_count: 10
  name: Whatsapp Cloud Api Template Parameter Example
  slug: whatsapp-cloud-api-template-parameter-example
- key_count: 2
  name: Whatsapp Cloud Api Text Message Example
  slug: whatsapp-cloud-api-text-message-example
- key_count: 4
  name: Whatsapp Flow Json Example
  slug: whatsapp-flow-json-example
- key_count: 4
  name: Whatsapp Flows Api Create Flow Request Example
  slug: whatsapp-flows-api-create-flow-request-example
- key_count: 2
  name: Whatsapp Flows Api Cursor Paging Example
  slug: whatsapp-flows-api-cursor-paging-example
- key_count: 10
  name: Whatsapp Flows Api Flow Example
  slug: whatsapp-flows-api-flow-example
- key_count: 8
  name: Whatsapp Flows Api Flow Validation Error Example
  slug: whatsapp-flows-api-flow-validation-error-example
- key_count: 1
  name: Whatsapp Flows Api Success Response Example
  slug: whatsapp-flows-api-success-response-example
- key_count: 4
  name: Whatsapp Flows Api Update Flow Request Example
  slug: whatsapp-flows-api-update-flow-request-example
- key_count: 10
  name: Whatsapp Message Example
  slug: whatsapp-message-example
- key_count: 5
  name: Whatsapp Message Template Example
  slug: whatsapp-message-template-example
- key_count: 2
  name: Whatsapp Webhook Payload Example
  slug: whatsapp-webhook-payload-example
features:
- description: Send and receive messages, media, and interactive content through Meta-hosted WhatsApp infrastructure.
  name: Cloud API
- description: Pre-approved message templates for proactive customer communication with variable substitution.
  name: Message Templates
- description: Buttons, lists, product catalogs, and flows for rich customer engagement.
  name: Interactive Messages
- description: Send and receive images, videos, documents, audio, stickers, and location data.
  name: Media Messaging
- description: Real-time notifications for incoming messages, delivery status, and account events.
  name: Webhooks
- description: Manage WhatsApp Business accounts, phone numbers, and messaging limits.
  name: Business Management API
- description: Build interactive multi-step forms and workflows within WhatsApp conversations.
  name: Flows
- description: Share product catalogs and enable in-chat commerce experiences.
  name: Catalogs and Commerce
- description: End-to-end encryption for all messages and media.
  name: Encryption
- description: Route conversations to multiple agents with conversation assignment.
  name: Multi-Agent Support
finops:
- name: Whatsapp Finops
  service_category: Business Messaging
  slug: whatsapp-finops
image: /assets/icons/whatsapp.png
integrations:
- description: Manage WhatsApp alongside Facebook and Instagram from a unified dashboard.
  name: Meta Business Suite
- description: CRM integration for managing customer conversations and contact history.
  name: Salesforce
- description: E-commerce integration for order notifications and customer messaging.
  name: Shopify
- description: Marketing and sales integration for lead nurturing via WhatsApp.
  name: HubSpot
- description: Help desk integration for ticketed WhatsApp customer support.
  name: Zendesk
json_schemas:
- name: ConversationAnalytics
  property_count: 1
  slug: whatsapp-business-management-api-conversation-analytics
- name: CreateTemplateRequest
  property_count: 5
  slug: whatsapp-business-management-api-create-template-request
- name: CursorPaging
  property_count: 3
  slug: whatsapp-business-management-api-cursor-paging
- name: MessageTemplate
  property_count: 8
  slug: whatsapp-business-management-api-message-template
- name: PhoneNumber
  property_count: 11
  slug: whatsapp-business-management-api-phone-number
- name: SuccessResponse
  property_count: 1
  slug: whatsapp-business-management-api-success-response
- name: TemplateAnalytics
  property_count: 1
  slug: whatsapp-business-management-api-template-analytics
- name: TemplateButton
  property_count: 8
  slug: whatsapp-business-management-api-template-button
- name: TemplateComponentDefinition
  property_count: 7
  slug: whatsapp-business-management-api-template-component-definition
- name: WhatsAppBusinessAccount
  property_count: 11
  slug: whatsapp-business-management-api-whats-app-business-account
- name: AudioObject
  property_count: 2
  slug: whatsapp-cloud-api-audio-object
- name: ContactObject
  property_count: 7
  slug: whatsapp-cloud-api-contact-object
- name: DocumentObject
  property_count: 4
  slug: whatsapp-cloud-api-document-object
- name: InteractiveMessage
  property_count: 5
  slug: whatsapp-cloud-api-interactive-message
- name: ListSection
  property_count: 2
  slug: whatsapp-cloud-api-list-section
- name: LocationMessage
  property_count: 4
  slug: whatsapp-cloud-api-location-message
- name: MediaObject
  property_count: 3
  slug: whatsapp-cloud-api-media-object
- name: ReactionMessage
  property_count: 2
  slug: whatsapp-cloud-api-reaction-message
- name: SendMessageRequest
  property_count: 19
  slug: whatsapp-cloud-api-send-message-request
- name: SendMessageResponse
  property_count: 3
  slug: whatsapp-cloud-api-send-message-response
- name: StickerObject
  property_count: 2
  slug: whatsapp-cloud-api-sticker-object
- name: TemplateComponent
  property_count: 4
  slug: whatsapp-cloud-api-template-component
- name: TemplateMessage
  property_count: 3
  slug: whatsapp-cloud-api-template-message
- name: TemplateParameter
  property_count: 10
  slug: whatsapp-cloud-api-template-parameter
- name: TextMessage
  property_count: 2
  slug: whatsapp-cloud-api-text-message
- name: WhatsApp Flow JSON
  property_count: 4
  slug: whatsapp-flow-json
- name: CreateFlowRequest
  property_count: 4
  slug: whatsapp-flows-api-create-flow-request
- name: CursorPaging
  property_count: 2
  slug: whatsapp-flows-api-cursor-paging
- name: Flow
  property_count: 10
  slug: whatsapp-flows-api-flow
- name: FlowValidationError
  property_count: 8
  slug: whatsapp-flows-api-flow-validation-error
- name: SuccessResponse
  property_count: 1
  slug: whatsapp-flows-api-success-response
- name: UpdateFlowRequest
  property_count: 4
  slug: whatsapp-flows-api-update-flow-request
- name: WhatsApp Message
  property_count: 17
  slug: whatsapp-message
- name: WhatsApp Message Template
  property_count: 5
  slug: whatsapp-message-template
- name: WhatsApp Webhook Payload
  property_count: 2
  slug: whatsapp-webhook-payload
json_structures:
- name: Whatsapp Business Management Api Conversation Analytics Structure
  property_count: 1
  slug: whatsapp-business-management-api-conversation-analytics-structure
- name: Whatsapp Business Management Api Create Template Request Structure
  property_count: 5
  slug: whatsapp-business-management-api-create-template-request-structure
- name: Whatsapp Business Management Api Cursor Paging Structure
  property_count: 3
  slug: whatsapp-business-management-api-cursor-paging-structure
- name: Whatsapp Business Management Api Message Template Structure
  property_count: 8
  slug: whatsapp-business-management-api-message-template-structure
- name: Whatsapp Business Management Api Phone Number Structure
  property_count: 11
  slug: whatsapp-business-management-api-phone-number-structure
- name: Whatsapp Business Management Api Success Response Structure
  property_count: 1
  slug: whatsapp-business-management-api-success-response-structure
- name: Whatsapp Business Management Api Template Analytics Structure
  property_count: 1
  slug: whatsapp-business-management-api-template-analytics-structure
- name: Whatsapp Business Management Api Template Button Structure
  property_count: 8
  slug: whatsapp-business-management-api-template-button-structure
- name: Whatsapp Business Management Api Template Component Definition Structure
  property_count: 7
  slug: whatsapp-business-management-api-template-component-definition-structure
- name: Whatsapp Business Management Api Whats App Business Account Structure
  property_count: 11
  slug: whatsapp-business-management-api-whats-app-business-account-structure
- name: Whatsapp Cloud Api Audio Object Structure
  property_count: 2
  slug: whatsapp-cloud-api-audio-object-structure
- name: Whatsapp Cloud Api Contact Object Structure
  property_count: 7
  slug: whatsapp-cloud-api-contact-object-structure
- name: Whatsapp Cloud Api Document Object Structure
  property_count: 4
  slug: whatsapp-cloud-api-document-object-structure
- name: Whatsapp Cloud Api Interactive Message Structure
  property_count: 5
  slug: whatsapp-cloud-api-interactive-message-structure
- name: Whatsapp Cloud Api List Section Structure
  property_count: 2
  slug: whatsapp-cloud-api-list-section-structure
- name: Whatsapp Cloud Api Location Message Structure
  property_count: 4
  slug: whatsapp-cloud-api-location-message-structure
- name: Whatsapp Cloud Api Media Object Structure
  property_count: 3
  slug: whatsapp-cloud-api-media-object-structure
- name: Whatsapp Cloud Api Reaction Message Structure
  property_count: 2
  slug: whatsapp-cloud-api-reaction-message-structure
- name: Whatsapp Cloud Api Send Message Request Structure
  property_count: 19
  slug: whatsapp-cloud-api-send-message-request-structure
- name: Whatsapp Cloud Api Send Message Response Structure
  property_count: 3
  slug: whatsapp-cloud-api-send-message-response-structure
- name: Whatsapp Cloud Api Sticker Object Structure
  property_count: 2
  slug: whatsapp-cloud-api-sticker-object-structure
- name: Whatsapp Cloud Api Template Component Structure
  property_count: 4
  slug: whatsapp-cloud-api-template-component-structure
- name: Whatsapp Cloud Api Template Message Structure
  property_count: 3
  slug: whatsapp-cloud-api-template-message-structure
- name: Whatsapp Cloud Api Template Parameter Structure
  property_count: 10
  slug: whatsapp-cloud-api-template-parameter-structure
- name: Whatsapp Cloud Api Text Message Structure
  property_count: 2
  slug: whatsapp-cloud-api-text-message-structure
- name: Whatsapp Flow Json Structure
  property_count: 4
  slug: whatsapp-flow-json-structure
- name: Whatsapp Flows Api Create Flow Request Structure
  property_count: 4
  slug: whatsapp-flows-api-create-flow-request-structure
- name: Whatsapp Flows Api Cursor Paging Structure
  property_count: 2
  slug: whatsapp-flows-api-cursor-paging-structure
- name: Whatsapp Flows Api Flow Structure
  property_count: 10
  slug: whatsapp-flows-api-flow-structure
- name: Whatsapp Flows Api Flow Validation Error Structure
  property_count: 8
  slug: whatsapp-flows-api-flow-validation-error-structure
- name: Whatsapp Flows Api Success Response Structure
  property_count: 1
  slug: whatsapp-flows-api-success-response-structure
- name: Whatsapp Flows Api Update Flow Request Structure
  property_count: 4
  slug: whatsapp-flows-api-update-flow-request-structure
- name: Whatsapp Message Structure
  property_count: 17
  slug: whatsapp-message-structure
- name: Whatsapp Message Template Structure
  property_count: 5
  slug: whatsapp-message-template-structure
- name: Whatsapp Webhook Payload Structure
  property_count: 2
  slug: whatsapp-webhook-payload-structure
jsonld:
- class_count: 33
  name: Whatsapp Context
  property_count: 109
  slug: whatsapp-context
layout: provider
modified: '2026-05-19'
name: WhatsApp
nav: Providers
network: true
overview: 'WhatsApp publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Flows API, On-Premises API, Analytics API, and 14 more.


  The WhatsApp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  WhatsApp''s developer surface includes authentication, getting-started guide, changelog, engineering blog, support, developer console, Stack Overflow tag, and 41 more developer resources.'
plans:
- name: Whatsapp Plans Pricing
  plan_count: 2
  slug: whatsapp-plans-pricing
random_paper: 127
rate_limits:
- limit_count: 6
  name: Whatsapp Rate Limits
  slug: whatsapp-rate-limits
rules:
- name: WhatsApp API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: whatsapp-asyncapi-spectral-rules
- name: WhatsApp API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: whatsapp-jsonschema-spectral-rules
- name: WhatsApp API Rules
  rule_count: 23
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 8
  slug: whatsapp-spectral-rules
score:
  band: strong
  composite: 57.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 85.4
    developer_ergonomics: 54.3
    discoverability: 40.7
    governance: 41.7
    operational_transparency: 55.3
  previous_composite: 57.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whatsapp/refs/heads/main/screenshots/whatsapp-2026-06-20T201434.png
security:
- kind: authentication
  name: Whatsapp Authentication
  slug: whatsapp-authentication
  summary_line: http · 1 scheme
slug: whatsapp
solutions:
- description: Cloud API and On-Premises API for medium and large businesses at scale.
  name: WhatsApp Business Platform
- description: Free mobile app for small businesses with basic messaging features.
  name: WhatsApp Business App
- description: Interactive forms and workflows within WhatsApp conversations.
  name: WhatsApp Flows
use_cases:
- description: Provide real-time customer service and support through WhatsApp messaging.
  name: Customer Support
- description: Send order confirmations, shipping updates, and delivery notifications.
  name: Order Notifications
- description: Send appointment reminders and allow rescheduling via interactive messages.
  name: Appointment Reminders
- description: Send promotional messages using approved templates to opted-in customers.
  name: Marketing Campaigns
- description: Send OTP codes and verification messages for account security.
  name: Two-Factor Authentication
- description: Build automated conversational bots for FAQs and self-service workflows.
  name: Chatbot Integration
- description: Share product catalogs, process orders, and send payment reminders.
  name: E-commerce
- description: Send appointment reminders, test results, and health tips to patients.
  name: Healthcare Communication
website: https://developers.facebook.com/
---
