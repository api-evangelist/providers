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
  - sandbox
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
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 48.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Whatsapp Agentic Access
  operation_count: 43
  slug: whatsapp-agentic-access
  summary_line: 43 operations · 27 acting
api_count: 3
apis:
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: 'API for creating structured, interactive forms and multi-step flows within WhatsApp conversations, enabling appointment booking, surveys, lead capture, and other guided experiences using a JSON-based '
  name: WhatsApp Flows API
  slug: flows-api
- description: 'The self-hosted version of the WhatsApp Business API that allowed businesses to run the API on their own infrastructure. This API was deprecated on October 23, 2025, and all users must migrate to the '
  name: WhatsApp On-Premises API
  slug: on-premises-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Retrieve conversation and template analytics
  name: WhatsApp Analytics API
  slug: whatsapp-analytics-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Upload and retrieve flow JSON assets
  name: WhatsApp Assets API
  slug: whatsapp-assets-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Manage user access to a WABA
  name: WhatsApp Assigned Users API
  slug: whatsapp-assigned-users-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Manage WhatsApp Business Account information
  name: WhatsApp Business Accounts API
  slug: whatsapp-business-accounts-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Get and update WhatsApp Business profile information
  name: WhatsApp Business Profile API
  slug: whatsapp-business-profile-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Publish and deprecate flows
  name: WhatsApp Lifecycle API
  slug: whatsapp-lifecycle-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Upload, retrieve, and delete media files
  name: WhatsApp Media API
  slug: whatsapp-media-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Create, update, and delete message templates
  name: WhatsApp Message Templates API
  slug: whatsapp-message-templates-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Send messages of all types to WhatsApp users
  name: WhatsApp Messages API
  slug: whatsapp-messages-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: List and manage phone numbers on a WABA
  name: WhatsApp Phone Numbers API
  slug: whatsapp-phone-numbers-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Connect and manage product catalogs
  name: WhatsApp Product Catalogs API
  slug: whatsapp-product-catalogs-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Create and manage QR codes for customer conversations
  name: WhatsApp QR Codes API
  slug: whatsapp-qr-codes-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Register and deregister phone numbers
  name: WhatsApp Registration API
  slug: whatsapp-registration-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Manage webhook subscriptions for a WABA
  name: WhatsApp Subscribed Apps API
  slug: whatsapp-subscribed-apps-api
- baseURL: https://graph.facebook.com/v21.0
  baseurl_source: declared
  description: Manage two-step verification PIN
  name: WhatsApp Two-Step Verification API
  slug: whatsapp-two-step-verification-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing application connected client business relationships
  name: WhatsApp Application Business Connections API
  slug: whatsapp-application-business-connections-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing assigned WhatsApp Business Accounts for users
  name: WhatsApp Assigned WhatsApp Business Accounts API
  slug: whatsapp-assigned-whatsapp-business-accounts-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Billing API from WhatsApp — 1 operation(s) for billing.
  name: WhatsApp Billing API
  slug: whatsapp-billing-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Block Users API from WhatsApp — 1 operation(s) for block users.
  name: WhatsApp Block Users API
  slug: whatsapp-block-users-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Account compliance information
  name: WhatsApp Business Compliance API
  slug: whatsapp-business-compliance-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Account encryption configuration
  name: WhatsApp Business Encryption API
  slug: whatsapp-business-encryption-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing phone numbers in WhatsApp Business Accounts
  name: WhatsApp Business Phone Numbers API
  slug: whatsapp-business-phone-numbers-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Business Portfolio API from WhatsApp — 1 operation(s) for business portfolio.
  name: WhatsApp Business Portfolio API
  slug: whatsapp-business-portfolio-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: 'Use the **`/{Phone-Number-ID}/call_permissions`** endpoint to check whether you have permission to call a specific WhatsApp user and understand what calling-related actions are available. ## Prerequis'
  name: WhatsApp Call Permissions API
  slug: whatsapp-call-permissions-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: Use the **`/{Phone-Number-ID}/calls`** endpoint to initiate, manage, and terminate WhatsApp calls. This API allows businesses to handle voice calling functionality through the WhatsApp Business Platfo
  name: WhatsApp Calls API
  slug: whatsapp-calls-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing client WhatsApp Business Account relationships
  name: WhatsApp Client WhatsApp Business Accounts API
  slug: whatsapp-client-whatsapp-business-accounts-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Commerce Settings API from WhatsApp — 1 operation(s) for commerce settings.
  name: WhatsApp Commerce Settings API
  slug: whatsapp-commerce-settings-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing conversational automation settings and bot configurations
  name: WhatsApp Conversational Automation API
  slug: whatsapp-conversational-automation-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Create Flow API from WhatsApp — 2 operation(s) for create flow.
  name: WhatsApp Create Flow API
  slug: whatsapp-create-flow-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: Payload encryption provides an additional layer of security on top of existing standard TLS/SSL that secures communication between Cloud API and businesses. When enabled, all message requests and mess
  name: WhatsApp Encrypted Messages API
  slug: whatsapp-encrypted-messages-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Get Endpoint Metrics API from WhatsApp — 1 operation(s) for get endpoint metrics.
  name: WhatsApp Get Endpoint Metrics API
  slug: whatsapp-get-endpoint-metrics-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Groups API from WhatsApp — 1 operation(s) for groups.
  name: WhatsApp Groups API
  slug: whatsapp-groups-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving and deleting individual WhatsApp Business message QR codes
  name: WhatsApp Individual QR Code API
  slug: whatsapp-individual-qr-code-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Invite Link API from WhatsApp — 1 operation(s) for invite link.
  name: WhatsApp Invite Link API
  slug: whatsapp-invite-link-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Join Requests API from WhatsApp — 1 operation(s) for join requests.
  name: WhatsApp Join Requests API
  slug: whatsapp-join-requests-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: Send marketing template messages to WhatsApp users using pre-approved templates.
  name: WhatsApp Marketing Messages API
  slug: whatsapp-marketing-messages-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Account message history and delivery status information
  name: WhatsApp Message History API
  slug: whatsapp-message-history-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Message History Events and delivery status occurrences
  name: WhatsApp Message History Events API
  slug: whatsapp-message-history-events-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Meta Graph API Application Connected Client Businesses API from WhatsApp — 1 operation(s) for meta graph api application connected client businesses.
  name: WhatsApp Meta Graph API Application Connected Client Businesses API
  slug: whatsapp-meta-graph-api-application-connected-client-businesses-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Account migration intent details
  name: WhatsApp Migration Intent API
  slug: whatsapp-migration-intent-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing Multi-Partner MM Lite onboarding requests and business agreements
  name: WhatsApp MM Lite Onboarding API
  slug: whatsapp-mm-lite-onboarding-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing Multi-Partner Solutions that enable collaborative WhatsApp Business messaging between solution owners and partner applications.
  name: WhatsApp Multi-Partner Solutions API
  slug: whatsapp-multi-partner-solutions-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing On-Behalf-Of mobility intent operations for WhatsApp Business Accounts
  name: WhatsApp OBO Mobility Intent API
  slug: whatsapp-obo-mobility-intent-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing Official Business Account status and verification
  name: WhatsApp Official Business Account API
  slug: whatsapp-official-business-account-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Accounts owned by a business
  name: WhatsApp Owned WhatsApp Business Accounts API
  slug: whatsapp-owned-whatsapp-business-accounts-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Participants API from WhatsApp — 1 operation(s) for participants.
  name: WhatsApp Participants API
  slug: whatsapp-participants-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business phone number registration and deregistration
  name: WhatsApp Phone Number Management API
  slug: whatsapp-phone-number-management-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for registering and managing WhatsApp Business phone numbers
  name: WhatsApp Phone Number Registration API
  slug: whatsapp-phone-number-registration-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for WhatsApp Business phone number verification process
  name: WhatsApp Phone Number Verification API
  slug: whatsapp-phone-number-verification-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing partner businesses associated with pre-verified phone numbers
  name: WhatsApp Pre-Verified Phone Number Partners API
  slug: whatsapp-pre-verified-phone-number-partners-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for sharing pre-verified phone numbers between business entities
  name: WhatsApp Pre-Verified Phone Number Sharing API
  slug: whatsapp-pre-verified-phone-number-sharing-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing pre-verified phone numbers for WhatsApp Business messaging
  name: WhatsApp Pre-Verified Phone Numbers API
  slug: whatsapp-pre-verified-phone-numbers-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for listing and creating WhatsApp Business message QR codes
  name: WhatsApp QR Code Collection API
  slug: whatsapp-qr-code-collection-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Account schedules and scheduling configurations
  name: WhatsApp Schedule Management API
  slug: whatsapp-schedule-management-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Send Flow API from WhatsApp — 1 operation(s) for send flow.
  name: WhatsApp Send Flow API
  slug: whatsapp-send-flow-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Settings API from WhatsApp — 1 operation(s) for settings.
  name: WhatsApp Settings API
  slug: whatsapp-settings-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Setup Endpoint Encryption API from WhatsApp — 1 operation(s) for setup endpoint encryption.
  name: WhatsApp Setup Endpoint Encryption API
  slug: whatsapp-setup-endpoint-encryption-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing Multi-Partner Solution migration processes
  name: WhatsApp Solution Migration API
  slug: whatsapp-solution-migration-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Templates API from WhatsApp — 2 operation(s) for templates.
  name: WhatsApp Templates API
  slug: whatsapp-templates-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Update Flow API from WhatsApp — 4 operation(s) for update flow.
  name: WhatsApp Update Flow API
  slug: whatsapp-update-flow-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Account webhook subscriptions
  name: WhatsApp Webhook Subscriptions API
  slug: whatsapp-webhook-subscriptions-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Account Number details and configuration
  name: WhatsApp WhatsApp Account Numbers API
  slug: whatsapp-whatsapp-account-numbers-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for retrieving WhatsApp Business Account activity logs and audit trails
  name: WhatsApp WhatsApp Business Account Activities API
  slug: whatsapp-whatsapp-business-account-activities-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Account details and configuration
  name: WhatsApp WhatsApp Business Account API
  slug: whatsapp-whatsapp-business-account-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Account on-behalf requests and business relationships
  name: WhatsApp WhatsApp Business Account On-Behalf Requests API
  slug: whatsapp-whatsapp-business-account-on-behalf-requests-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing user assignments and permissions for WhatsApp Business Accounts
  name: WhatsApp WhatsApp Business Account Users API
  slug: whatsapp-whatsapp-business-account-users-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: WhatsApp Business Platform APIs for messaging, account management, and partner integrations.
  name: WhatsApp WhatsApp Business API
  slug: whatsapp-whatsapp-business-api-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Bot configuration and details
  name: WhatsApp WhatsApp Business Bot API
  slug: whatsapp-whatsapp-business-bot-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Profile information and settings
  name: WhatsApp WhatsApp Business Profile API
  slug: whatsapp-whatsapp-business-profile-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: APIs for managing WhatsApp Business Profile details and configuration
  name: WhatsApp WhatsApp Business Profiles API
  slug: whatsapp-whatsapp-business-profiles-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: Operations for managing WhatsApp Business Multi-Partner Solutions including lifecycle management, status transitions, and partnership workflows.
  name: WhatsApp WhatsApp Business Solution Management API
  slug: whatsapp-whatsapp-business-solution-management-api
- baseURL: https://graph.facebook.com
  baseurl_source: declared
  description: The Whats App API from WhatsApp — 1 operation(s) for whats app.
  name: WhatsApp Whats App API
  slug: whatsapp-whats-app-api
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
artifact_total: 245
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
- group: operate
  href: https://artifacts.apis.io/whatsapp/rate-limits/whatsapp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/whatsapp-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/rules/whatsapp-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsapp-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/rules/whatsapp-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsapp-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/rules/whatsapp-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsapp-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/rules/whatsapp-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/whatsapp-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/vocabulary/whatsapp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/whatsapp-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/whatsapp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/asyncapi/whatsapp-webhooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/whatsapp-webhooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/data-model/whatsapp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/whatsapp-data-model.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/components/whatsapp-components.yml
  title: ''
  type: Components
  url: components/whatsapp-components.yml
- group: operate
  href: https://artifacts.apis.io/whatsapp/changelog/whatsapp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/whatsapp-changelog.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/conventions/whatsapp-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/whatsapp-conventions.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/conventions/whatsapp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/whatsapp-conventions.yml
- group: auth
  href: https://artifacts.apis.io/whatsapp/scopes/whatsapp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/whatsapp-scopes.yml
- group: operate
  href: https://artifacts.apis.io/whatsapp/lifecycle/whatsapp-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/whatsapp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/lifecycle/whatsapp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/whatsapp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/errors/whatsapp-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/whatsapp-error-codes.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/errors/whatsapp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/whatsapp-problem-types.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/conformance/whatsapp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/whatsapp-conformance.yml
- group: other
  href: https://artifacts.apis.io/whatsapp/overlays/whatsapp-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/whatsapp-analytics-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/whatsapp/llms/whatsapp-reference-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/whatsapp-reference-llms.txt
- group: build
  href: https://artifacts.apis.io/whatsapp/mcp/whatsapp-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/whatsapp-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/whatsapp/mcp/whatsapp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/whatsapp-mcp.yml
- group: auth
  href: https://artifacts.apis.io/whatsapp/well-known/whatsapp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/whatsapp-security.txt
- group: agent
  href: https://artifacts.apis.io/whatsapp/well-known/whatsapp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/whatsapp-well-known.yml
- group: other
  href: https://artifacts.apis.io/whatsapp/hosts/whatsapp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/whatsapp-hosts.yml
- group: build
  href: https://artifacts.apis.io/whatsapp/integrations/whatsapp-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/whatsapp-integration-edges.yml
- group: build
  href: https://artifacts.apis.io/whatsapp/packages/whatsapp-packages.yml
  title: ''
  type: SDKs
  url: packages/whatsapp-packages.yml
- group: build
  href: https://artifacts.apis.io/whatsapp/packages/whatsapp-packages.yml
  title: ''
  type: Packages
  url: packages/whatsapp-packages.yml
- group: auth
  href: https://artifacts.apis.io/whatsapp/security/whatsapp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/whatsapp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/whatsapp/security/whatsapp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/whatsapp-domain-security.yml
- group: other
  href: https://artifacts.apis.io/whatsapp/capabilities/whatsapp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/whatsapp-capability-edges.yml
- group: commercial
  href: https://artifacts.apis.io/whatsapp/plans/whatsapp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/whatsapp-plans-pricing.yml
- group: commercial
  href: https://artifacts.apis.io/whatsapp/finops/whatsapp-finops.yml
  title: ''
  type: FinOps
  url: finops/whatsapp-finops.yml
- group: company
  title: ''
  type: Website
  url: https://www.whatsapp.com/
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/WhatsApp/WhatsApp-Flows-Tools/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/WhatsApp/WhatsApp-Flows-Tools/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/WhatsApp/WhatsApp-Flows-Tools/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/WhatsApp/WhatsApp-Flows-Tools/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/whatsapp/agentic-access/whatsapp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/whatsapp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/whatsapp/authentication/whatsapp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/whatsapp-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/whatsapp/overview
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-create-qr-code-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-create-qr-code-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-create-template-then-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-create-template-then-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-publish-flow-and-send-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-publish-flow-and-send-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-register-phone-number-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-register-phone-number-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-send-and-react-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-and-react-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-send-interactive-buttons-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-interactive-buttons-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-send-location-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-location-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-send-template-message-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-template-message-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-send-text-and-mark-read-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-send-text-and-mark-read-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-subscribe-webhooks-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-subscribe-webhooks-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-update-business-profile-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-update-business-profile-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-update-template-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-update-template-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-upload-media-send-document-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/whatsapp-upload-media-send-document-workflow.yml
- group: design
  href: https://artifacts.apis.io/whatsapp/arazzo/whatsapp-upload-media-send-image-workflow.yml
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
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.facebook.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/get-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://metastatus.com/
- group: company
  title: ''
  type: Blog
  url: https://whatsappbusiness.com/blog/
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
  url: https://whatsappbusiness.com/developers/developer-hub/
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
  url: https://whatsappbusiness.com/products/platform-pricing/
- group: design
  href: https://artifacts.apis.io/whatsapp/json-ld/whatsapp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/whatsapp-context.jsonld
- group: docs
  href: https://artifacts.apis.io/whatsapp/json-schema/whatsapp-webhook-payload-schema.json
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
  url: https://whatsappbusiness.com/policy/
- group: commercial
  title: ''
  type: Meta Terms
  url: https://www.facebook.com/legal/Meta-Terms-for-WhatsApp-Business-Platform
- group: operate
  title: ''
  type: FAQ
  url: https://whatsappbusiness.com/resources/faq/
- group: start
  title: ''
  type: Sandbox
  url: https://whatsappbusiness.com/developers/developer-hub/
- group: design
  title: ''
  type: Versioning
  url: https://developers.facebook.com/docs/graph-api/guides/versioning
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/about-the-platform#throughput
- group: design
  title: ''
  type: ErrorCodes
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/support/error-codes
- group: docs
  title: ''
  type: Documentation
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/overview
- group: docs
  title: ''
  type: APIReference
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-phone-number/message-api
- group: start
  title: ''
  type: SignUp
  url: https://developers.facebook.com/products/whatsapp/onboard/direct
- group: operate
  title: ''
  type: HelpCenter
  url: https://faq.whatsapp.com/
- group: operate
  title: ''
  type: Forum
  url: https://developers.facebook.com/community
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/messaging-limits
- group: operate
  title: ''
  type: StatusPage
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/support/api-status-page
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://www.whatsapp.com/security/advisories
- group: auth
  title: ''
  type: TrustAndSafety
  url: https://whatsappbusiness.com/trust-and-safety/
- group: company
  title: ''
  type: Blog
  url: https://blog.whatsapp.com/
- group: commercial
  title: ''
  type: Legal
  url: https://www.whatsapp.com/legal/
- group: company
  title: ''
  type: Website
  url: https://whatsappbusiness.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.facebook.com/documentation/business-messaging/whatsapp/support
created: '2024-01-15'
description: 'WhatsApp, owned by Meta Platforms, is a free, end-to-end encrypted messaging and calling app used by more than two billion people. For developers it offers the WhatsApp Business Platform: the Cloud API (hosted on Meta''s Graph API at graph.facebook.com) for sending and receiving messages, media, interactive and template messages, plus the Business Management API, WhatsApp Flows, webhooks, and per-conversation pricing. The self-hosted On-Premises API was sunset on October 23, 2025.'
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
finops:
- has_sources: true
  method: derived
  name: Whatsapp Finops
  primary_unit: 1m tokens
  service_category: ''
  slug: whatsapp-finops
  template: false
image: /assets/icons/whatsapp.png
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
- name: CallPermissionCheckResponsePayload
  property_count: 3
  slug: whatsapp-call-permission-check-response-payload
- name: CallRequestPayload
  property_count: 5
  slug: whatsapp-call-request-payload
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
- name: PhoneNumberInfo
  property_count: 6
  slug: whatsapp-phone-number-info
- name: WhatsApp Webhook Payload
  property_count: 2
  slug: whatsapp-webhook-payload
- name: WhatsAppAccountNumber
  property_count: 13
  slug: whatsapp-whats-app-account-number
- name: WhatsAppBusinessAccount
  property_count: 17
  slug: whatsapp-whats-app-business-account
- name: WhatsAppBusinessProfileNode
  property_count: 11
  slug: whatsapp-whats-app-business-profile-node
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
mcp_servers:
- description: Remote MCP server at mcp.facebook.com over streamable HTTP requiring OAuth; 18 tools listed.
  name: WhatsApp Business Tools
  slug: whatsapp-business-tools
modified: '2026-11-05'
name: WhatsApp
nav: Providers
network: true
overview: 'WhatsApp publishes 74 API contracts indexed on the [APIs.io](https://apis.io/) network, including Flows API, On-Premises API, Analytics API, and 71 more. Tagged areas include Messaging, Analytics, WhatsApp, Business Messaging, and Meta.


  The WhatsApp catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 4 Spectral governance rulesets.


  WhatsApp''s developer surface includes changelog, authentication, getting-started guide, engineering blog, support, developer console, Stack Overflow tag, and 89 more developer resources.'
plans:
- name: Whatsapp Plans Pricing
  plan_count: 2
  slug: whatsapp-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 9
  name: Whatsapp Rate Limits
  slug: whatsapp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: WhatsApp — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: whatsapp-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: WhatsApp — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: whatsapp-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 112
  extends:
  - spectral:oas
  name: WhatsApp API Rules
  rule_count: 71
  severity_counts:
    error: 46
    hint: 0
    info: 6
    warn: 19
  slug: whatsapp-rules
- authorship: generated
  effective_rule_count: 63
  extends:
  - spectral:oas
  name: WhatsApp API Rules
  rule_count: 22
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 8
  slug: whatsapp-spectral-rules
scopes:
- name: Whatsapp Scopes
  scope_count: 5
  slug: whatsapp-scopes
  summary_line: 5 scopes
score:
  band: exemplar
  composite: 68.0
  coverage:
    artifact_dirs: 43
    catalog_earned: 87.0
    catalog_earned_first_party: 20.0
    catalog_gap: 28.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.6
  facets:
    access_clarity: 73.7
    contract_governance: 31.8
    contract_quality: 74.0
    developer_ergonomics: 78.0
    discoverability: 61.7
    operational_transparency: 68.4
  open_source:
    applies: true
    score: 40.0
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 73
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/whatsapp/whatsapp-2026-06-20T201434.png
security:
- kind: authentication
  name: Whatsapp Authentication
  slug: whatsapp-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Whatsapp Domain Security
  slug: whatsapp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Whatsapp Vulnerability Disclosure
  slug: whatsapp-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 10
skills:
- name: whatsapp-create-qr-code
  slug: whatsapp-create-qr-code
- name: whatsapp-create-template-then-send
  slug: whatsapp-create-template-then-send
- name: whatsapp-publish-flow-and-send
  slug: whatsapp-publish-flow-and-send
- name: whatsapp-register-phone-number
  slug: whatsapp-register-phone-number
- name: whatsapp-reply-and-mark-read
  slug: whatsapp-reply-and-mark-read
- name: whatsapp-send-template-message
  slug: whatsapp-send-template-message
- name: whatsapp-subscribe-webhooks
  slug: whatsapp-subscribe-webhooks
- name: whatsapp-update-business-profile
  slug: whatsapp-update-business-profile
- name: whatsapp-upload-media-send-document
  slug: whatsapp-upload-media-send-document
- name: whatsapp-upload-media-send-image
  slug: whatsapp-upload-media-send-image
slug: whatsapp
tags:
- Messaging
- Analytics
- WhatsApp
- Business Messaging
- Meta
website: https://www.whatsapp.com/
---
