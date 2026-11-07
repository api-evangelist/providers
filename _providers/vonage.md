---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 101
  human_in_the_loop: 13
  name: Vonage Agentic Access
  operation_count: 170
  slug: vonage-agentic-access
  summary_line: 170 operations · 101 acting · 13 human-in-the-loop
api_count: 22
apis:
- baseURL: https://api.nexmo.com/beta/chatapp-accounts
  baseurl_source: declared
  description: An external-account used as the `from` field in the Messages API and Dispatch API
  name: Vonage Account API
  slug: vonage-account-api
- baseURL: https://api.nexmo.com/ni
  baseurl_source: declared
  description: The Advanced API from Vonage — 2 operation(s) for advanced.
  name: Vonage Advanced API
  slug: vonage-advanced-api
- baseURL: https://api.nexmo.com
  baseurl_source: declared
  description: The application API from Vonage — 4 operation(s) for application.
  name: Vonage Application API
  slug: vonage-application-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Applications API from Vonage — 1 operation(s) for applications.
  name: Vonage Applications API
  slug: vonage-applications-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to working with archives
  name: Vonage Archives API
  slug: vonage-archives-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to audio connector
  name: Vonage Audio Connector API
  slug: vonage-audio-connector-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: This section shows how you can query the current balance of your account, and if you have auto-reload enabled how to trigger a top-up to your account without waiting for the next balance check.
  name: Vonage Balance API
  slug: vonage-balance-api
- baseURL: https://api.nexmo.com/ni
  baseurl_source: declared
  description: The Basic API from Vonage — 1 operation(s) for basic.
  name: Vonage Basic API
  slug: vonage-basic-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to live streaming and broadcasting
  name: Vonage Broadcast API
  slug: vonage-broadcast-api
- baseURL: https://api.nexmo.com/v1/calls
  baseurl_source: declared
  description: Fetch, Create and Modify voice calls
  name: Vonage Calls API
  slug: vonage-calls-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: Manage the settings on your account
  name: Vonage Configuration API
  slug: vonage-configuration-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The conversation API from Vonage — 2 operation(s) for conversation.
  name: Vonage Conversation API
  slug: vonage-conversation-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Dial In Numbers API from Vonage — 1 operation(s) for dial in numbers.
  name: Vonage Dial In Numbers API
  slug: vonage-dial-in-numbers-api
- baseURL: https://api.nexmo.com/v0.1/dispatch
  baseurl_source: declared
  description: The Dispatch API API from Vonage — 1 operation(s) for dispatch api.
  name: Vonage Dispatch API
  slug: vonage-dispatch-api-api
- baseURL: https://api.nexmo.com/v1/calls
  baseurl_source: declared
  description: Send and subscribe to DTMF tones in an active call
  name: Vonage DTMF API
  slug: vonage-dtmf-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The event API from Vonage — 2 operation(s) for event.
  name: Vonage Event API
  slug: vonage-event-api
- baseURL: https://api.nexmo.com/beta/audit
  baseurl_source: declared
  description: The Events API from Vonage — 2 operation(s) for events.
  name: Vonage Events API
  slug: vonage-events-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to Experience Composer
  name: Vonage Experience Composer API
  slug: vonage-experience-composer-api
- baseURL: https://api.nexmo.com/beta/chatapp-accounts
  baseurl_source: declared
  description: Managing your [Facebook Messenger](https://developer.nexmo.com/messages/concepts/facebook) account
  name: Vonage Facebook Messenger API
  slug: vonage-facebook-messenger-api
- baseURL: https://api.nexmo.com/verify
  baseurl_source: declared
  description: Fraud Management
  name: Vonage Fraud Management API
  slug: vonage-fraud-management-api
- baseURL: https://api.nexmo.com/v3/media
  baseurl_source: declared
  description: The Id API from Vonage — 2 operation(s) for id.
  name: Vonage ID API
  slug: vonage-id-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: Provides real-time intelligence about a phone number.
  name: Vonage Identity Insights API
  slug: vonage-identity-insights-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to live captioning
  name: Vonage Live Captions API
  slug: vonage-live-captions-api
- baseURL: https://api-eu.vonage.com/network-location/v0.1
  baseurl_source: declared
  description: Retrieve the location of a device
  name: Vonage Location retrieval API
  slug: vonage-location-retrieval-api
- baseURL: https://api.nexmo.com/v3/media
  baseurl_source: declared
  description: The Media API API from Vonage — 1 operation(s) for media api.
  name: Vonage Media API
  slug: vonage-media-api-api
- baseURL: https://api.nexmo.com
  baseurl_source: declared
  description: The Media API from Vonage — 1 operation(s) for media.
  name: Vonage Media API
  slug: vonage-media-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The member API from Vonage — 3 operation(s) for member.
  name: Vonage Member API
  slug: vonage-member-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: Send message Operation
  name: Vonage Messages API
  slug: vonage-messages-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to moderating participants
  name: Vonage Moderation API
  slug: vonage-moderation-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: The Number API from Vonage — 4 operation(s) for number.
  name: Vonage Number API
  slug: vonage-number-api
- baseURL: https://api.nexmo.com/v1/calls
  baseurl_source: declared
  description: Start or stop playing Text to Speech in to an active call
  name: Vonage Play TTS API
  slug: vonage-play-tts-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: The Pricing API from Vonage — 3 operation(s) for pricing.
  name: Vonage Pricing API
  slug: vonage-pricing-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The record API from Vonage — 1 operation(s) for record.
  name: Vonage Record API
  slug: vonage-record-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Recordings API from Vonage — 1 operation(s) for recordings.
  name: Vonage Recordings API
  slug: vonage-recordings-api
- baseURL: https://api.nexmo.com
  baseurl_source: declared
  description: The Reports API from Vonage — 3 operation(s) for reports.
  name: Vonage Reports API
  slug: vonage-reports-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Rooms API from Vonage — 2 operation(s) for rooms.
  name: Vonage Rooms API
  slug: vonage-rooms-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: Many of the Vonage APIs are accessed using an API key and secret. It is recommended that you change or "rotate" your secrets from time to time for security purposes. This section provides the API inte
  name: Vonage Secret Management API
  slug: vonage-secret-management-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Sessions API from Vonage — 6 operation(s) for sessions.
  name: Vonage Sessions API
  slug: vonage-sessions-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to sending and recieving Signals
  name: Vonage Signaling API
  slug: vonage-signaling-api
- baseURL: https://video.api.vonage.com
  baseurl_source: declared
  description: APIs relating to working with SIP calls in a video session
  name: Vonage SIP API
  slug: vonage-sip-api
- baseURL: https://rest.nexmo.com
  baseurl_source: declared
  description: The Sms API from Vonage — 1 operation(s) for sms.
  name: Vonage Sms API
  slug: vonage-sms-api
- baseURL: https://api.nexmo.com/ni
  baseurl_source: declared
  description: The Standard API from Vonage — 1 operation(s) for standard.
  name: Vonage Standard API
  slug: vonage-standard-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The stream API from Vonage — 1 operation(s) for stream.
  name: Vonage Stream API
  slug: vonage-stream-api
- baseURL: https://api.nexmo.com/v1/calls
  baseurl_source: declared
  description: Start or stop streaming audio in to an active call
  name: Vonage Stream Audio API
  slug: vonage-stream-audio-api
- baseURL: https://api.nexmo.com/accounts
  baseurl_source: declared
  description: This section shows how you can create, retrieve and modify subaccounts of a primary account.
  name: Vonage Subaccount Management API
  slug: vonage-subaccount-management-api
- baseURL: https://api.nexmo.com/v1
  baseurl_source: declared
  description: The talk API from Vonage — 1 operation(s) for talk.
  name: Vonage Talk API
  slug: vonage-talk-api
- baseURL: https://api.nexmo.com/v2/verify
  baseurl_source: declared
  description: Create and modify custom template fragments in Verify
  name: Vonage Template Fragments API
  slug: vonage-template-fragments-api
- baseURL: https://api.nexmo.com/v2/verify
  baseurl_source: declared
  description: Create and modify custom templates in Verify
  name: Vonage Templates API
  slug: vonage-templates-api
- baseURL: https://api-eu.vonage.com/v1/meetings
  baseurl_source: declared
  description: The Themes API from Vonage — 5 operation(s) for themes.
  name: Vonage Themes API
  slug: vonage-themes-api
- baseURL: https://api.nexmo.com/v1/redact
  baseurl_source: declared
  description: The Transaction API from Vonage — 1 operation(s) for transaction.
  name: Vonage Transaction API
  slug: vonage-transaction-api
- baseURL: https://api.nexmo.com/accounts
  baseurl_source: declared
  description: This section shows how you execute credit, balance and number transfers, as well as viewing past transactions.
  name: Vonage Transfers API
  slug: vonage-transfers-api
- baseURL: https://api.nexmo.com
  baseurl_source: declared
  description: The user API from Vonage — 3 operation(s) for user.
  name: Vonage User API
  slug: vonage-user-api
- baseURL: https://api.nexmo.com/v2/verify
  baseurl_source: declared
  description: Provides 2FA authentication for end-users.
  name: Vonage Verify API
  slug: vonage-verify-api
- baseURL: https://api.nexmo.com/verify
  baseurl_source: declared
  description: Verify Check
  name: Vonage Verify Check API
  slug: vonage-verify-check-api
- baseURL: https://api.nexmo.com/verify
  baseurl_source: declared
  description: Verify Control
  name: Vonage Verify Control API
  slug: vonage-verify-control-api
- baseURL: https://api.nexmo.com/verify
  baseurl_source: declared
  description: Verify Requests
  name: Vonage Verify Requests API
  slug: vonage-verify-requests-api
- baseURL: https://api.nexmo.com/verify
  baseurl_source: declared
  description: Verify Search
  name: Vonage Verify Search API
  slug: vonage-verify-search-api
- baseURL: https://api.nexmo.com/beta/chatapp-accounts
  baseurl_source: declared
  description: Managing your [Viber Service Message](https://developer.nexmo.com/messages/concepts/viber) account
  name: Vonage Viber Service Message API
  slug: vonage-viber-service-message-api
- baseURL: https://api.nexmo.com/beta/chatapp-accounts
  baseurl_source: declared
  description: The Whats App API from Vonage — 1 operation(s) for whats app.
  name: Vonage Whats App API
  slug: vonage-whats-app-api
artifact_total: 170
asyncapis:
- description: 'AsyncAPI 2.6 description of Vonage''s publicly-documented WebSocket surface. The only Vonage product whose realtime protocol is publicly specified frame-by-frame is the Voice API WebSocket endpoint: th'
  name: Vonage Voice WebSocket API
  slug: vonage-asyncapi
- description: ''
  name: Vonage Webhooks
  slug: vonage-webhooks
collections:
- collection_type: postman
  name: Vonage Communications Applications API
  slug: postman-vonage-applications-api
- collection_type: postman
  name: Vonage Communications Applications Messages API
  slug: postman-vonage-messages-api
- collection_type: postman
  name: Vonage Communications Applications Numbers API
  slug: postman-vonage-numbers-api
- collection_type: postman
  name: Vonage Communications Applications SMS API
  slug: postman-vonage-sms-api
- collection_type: postman
  name: Vonage Communications Applications Verify API
  slug: postman-vonage-verify-api
- collection_type: postman
  name: Vonage Communications Applications Voice API
  slug: postman-vonage-voice-api
- collection_type: open
  name: Vonage Communications Applications API
  slug: open-vonage-applications-api
- collection_type: open
  name: Vonage Communications Applications Messages API
  slug: open-vonage-messages-api
- collection_type: open
  name: Vonage Communications Applications Numbers API
  slug: open-vonage-numbers-api
- collection_type: open
  name: Vonage Communications Applications SMS API
  slug: open-vonage-sms-api
- collection_type: open
  name: Vonage Communications Applications Verify API
  slug: open-vonage-verify-api
- collection_type: open
  name: Vonage Communications Applications Voice API
  slug: open-vonage-voice-api
- collection_type: open
  name: Vonage Communications API
  slug: open-vonage
common:
- group: auth
  href: https://artifacts.apis.io/vonage/well-known/vonage-vonageapi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/vonage-vonageapi-security.txt
- group: build
  href: https://artifacts.apis.io/vonage/integrations/vonage-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/vonage-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/vonage/well-known/vonage-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/vonage-well-known.yml
- group: build
  href: https://artifacts.apis.io/vonage/cli/vonage-cli.yml
  title: ''
  type: CLI
  url: cli/vonage-cli.yml
- group: design
  href: https://artifacts.apis.io/vonage/conventions/vonage-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vonage-conventions.yml
- group: start
  href: https://artifacts.apis.io/vonage/sandbox/vonage-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vonage-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/vonage/lifecycle/vonage-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/vonage-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://vonageapi.statuspage.io
- group: design
  href: https://artifacts.apis.io/vonage/lifecycle/vonage-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vonage-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vonage/errors/vonage-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/vonage-error-codes.yml
- group: design
  href: https://artifacts.apis.io/vonage/errors/vonage-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vonage-problem-types.yml
- group: build
  href: https://artifacts.apis.io/vonage/mcp/vonage-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/vonage-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/vonage/mcp/vonage-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/vonage-mcp.yml
- group: commercial
  href: https://artifacts.apis.io/vonage/finops/vonage-finops.yml
  title: ''
  type: FinOps
  url: finops/vonage-finops.yml
- group: operate
  href: https://artifacts.apis.io/vonage/rate-limits/vonage-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vonage-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/vonage/plans/vonage-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vonage-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/vonage/rules/vonage-rules.yml
  title: ''
  type: Spectral
  url: rules/vonage-rules.yml
- group: design
  href: https://artifacts.apis.io/vonage/rules/vonage-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/vonage-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/vonage/rules/vonage-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/vonage-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/vonage/json-ld/vonage-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/vonage-context.jsonld
- group: design
  href: https://artifacts.apis.io/vonage/vocabulary/vonage-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/vonage-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/vonage/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/vonage/asyncapi/vonage-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vonage-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/vonage/asyncapi/vonage-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/vonage-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/vonage/data-model/vonage-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vonage-data-model.yml
- group: operate
  href: https://artifacts.apis.io/vonage/changelog/vonage-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vonage-changelog.yml
- group: design
  href: https://artifacts.apis.io/vonage/conformance/vonage-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vonage-conformance.yml
- group: other
  href: https://artifacts.apis.io/vonage/overlays/vonage-sms-overlay.yml
  title: ''
  type: Overlay
  url: overlays/vonage-sms-overlay.yml
- group: agent
  href: https://artifacts.apis.io/vonage/llms/vonage-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vonage-llms.txt
- group: other
  href: https://artifacts.apis.io/vonage/hosts/vonage-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vonage-hosts.yml
- group: other
  href: https://artifacts.apis.io/vonage/vendors/vonage-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vonage-vendors.yml
- group: build
  href: https://artifacts.apis.io/vonage/packages/vonage-packages.yml
  title: ''
  type: Packages
  url: packages/vonage-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.vonage.com/security/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.vonage.com/resources/customers/roadmap/
- group: company
  title: ''
  type: Newsroom
  url: https://www.vonage.com/about-us/newsroom/
- group: start
  title: ''
  type: Login
  url: https://www.vonage.com/log-in/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.vonage.com/en/getting-started/overview
- group: company
  title: ''
  type: Website
  url: https://www.vonage.com/
- group: other
  href: https://artifacts.apis.io/vonage/capabilities/vonage-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vonage-capability-edges.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/vonage/overview
- group: agent
  href: https://artifacts.apis.io/vonage/agentic-access/vonage-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vonage-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vonage/security/vonage-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vonage-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/vonage/authentication/vonage-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vonage-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vonage
- group: start
  title: ''
  type: Portal
  url: https://developer.vonage.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vonage.com/en/documentation
- group: operate
  title: ''
  type: Support
  url: https://api.support.vonage.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Vonage
- group: start
  title: ''
  type: Portal
  url: https://www.vonage.com/developer-center/
- group: company
  title: ''
  type: Blog
  url: https://developer.vonage.com/en/blog
- group: operate
  title: ''
  type: Community
  url: https://vonage-community.slack.com/
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-node-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-python-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-java-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-php-sdk-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-ruby-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-dotnet-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-go-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Vonage/vonage-kotlin-sdk
- group: build
  title: ''
  type: CLI
  url: https://github.com/Vonage/vonage-cli
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vonage.com/legal/communications-apis/terms-of-use/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vonage.com/communications-apis/pricing
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.vonage.com/llms.txt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vonage.com/legal/privacy-policy
- group: docs
  title: ''
  type: APIReference
  url: https://developer.vonage.com/en/api
- group: start
  title: ''
  type: SignUp
  url: https://ui.idp.vonage.com/sign-up/dashboard
created: '2025-02-08'
description: Vonage (part of Ericsson) provides cloud communications APIs for voice, SMS, messaging, video, and verification. The Vonage API platform enables businesses to embed communication capabilities into applications including voice calls, SMS, multi-channel messaging (WhatsApp, Messenger, Viber, RCS), video conferencing, and two-factor authentication. SDKs are available for Node.js, Python, Java, PHP, Ruby, .NET, Go, and Kotlin.
examples:
- key_count: 4
  name: Vonage Createcall Example
  slug: vonage-createCall-example
- key_count: 4
  name: Vonage Requestverification Example
  slug: vonage-requestVerification-example
- key_count: 4
  name: Vonage Sendmessage Example
  slug: vonage-sendMessage-example
- key_count: 4
  name: Vonage Sendsms Example
  slug: vonage-sendSms-example
finops:
- has_sources: true
  method: derived
  name: Vonage Finops
  primary_unit: ''
  service_category: ''
  slug: vonage-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vonage.png
json_schemas:
- name: AccountResponse
  property_count: 6
  slug: vonage-account-response
- name: Add-Stream-To-Archive
  property_count: 3
  slug: vonage-add-stream-to-archive
- name: AggregatedInsightRequest
  property_count: 3
  slug: vonage-aggregated-insight-request
- name: AnyAsyncRequestParams
  property_count: 0
  slug: vonage-any-async-request-params
- name: ApplicationResponseCollection
  property_count: 5
  slug: vonage-application-response-collection
- name: ApplicationResponse
  property_count: 4
  slug: vonage-application-response
- name: AuditEvent
  property_count: 13
  slug: vonage-audit-event
- name: AuditResp
  property_count: 3
  slug: vonage-audit-resp
- name: available-numbers
  property_count: 2
  slug: vonage-available-numbers
- name: channel
  property_count: 0
  slug: vonage-channel
- name: checkErrorResponse
  property_count: 3
  slug: vonage-check-error-response
- name: Circle
  property_count: 2
  slug: vonage-circle
- name: CodeSubmitSuccess
  property_count: 2
  slug: vonage-code-submit-success
- name: controlErrorResponse
  property_count: 2
  slug: vonage-control-error-response
- name: conversation
  property_count: 9
  slug: vonage-conversation
- name: conversation_user
  property_count: 9
  slug: vonage-conversation-user
- name: CreateCallRequestAnswerUrl
  property_count: 11
  slug: vonage-create-call-request-answer-url
- name: createWorkflow
  property_count: 2
  slug: vonage-create-workflow
- name: Error
  property_count: 2
  slug: vonage-error
- name: ErrorXml
  property_count: 1
  slug: vonage-error-xml
- name: GetCallResponse
  property_count: 13
  slug: vonage-get-call-response
- name: GetCallsResponse
  property_count: 5
  slug: vonage-get-calls-response
- name: HAL
  property_count: 4
  slug: vonage-hal
- name: inbound-numbers
  property_count: 2
  slug: vonage-inbound-numbers
- name: Layout
  property_count: 3
  slug: vonage-layout
- name: ListFragmentsResponse
  property_count: 6
  slug: vonage-list-fragments-response
- name: ListTemplatesResponse
  property_count: 6
  slug: vonage-list-templates-response
- name: Max-Bitrate
  property_count: 0
  slug: vonage-max-bitrate
- name: media
  property_count: 2
  slug: vonage-media
- name: member
  property_count: 11
  slug: vonage-member
- name: NewMessage
  property_count: 20
  slug: vonage-new-message
- name: NewSubaccountRequest
  property_count: 3
  slug: vonage-new-subaccount-request
- name: niResponseJsonAdvancedRoamingUnknown
  property_count: 21
  slug: vonage-ni-response-json-advanced-roaming-unknown
- name: niResponseJsonAdvancedSync
  property_count: 22
  slug: vonage-ni-response-json-advanced-sync
- name: niResponseJsonStandard
  property_count: 20
  slug: vonage-ni-response-json-standard
- name: niResponseXmlAdvanced
  property_count: 19
  slug: vonage-ni-response-xml-advanced
- name: niResponseXmlBasic
  property_count: 4
  slug: vonage-ni-response-xml-basic
- name: niResponseXmlStandard
  property_count: 10
  slug: vonage-ni-response-xml-standard
- name: number-details
  property_count: 3
  slug: vonage-number-details
- name: number-details-update
  property_count: 10
  slug: vonage-number-details-update
- name: Polygon
  property_count: 2
  slug: vonage-polygon
- name: PricingCountriesResponse
  property_count: 2
  slug: vonage-pricing-countries-response
- name: PricingCountryResponse
  property_count: 7
  slug: vonage-pricing-country-response
- name: psd2Request
  property_count: 9
  slug: vonage-psd2-request
- name: Recording
  property_count: 6
  slug: vonage-recording
- name: RedactTransaction
  property_count: 3
  slug: vonage-redact-transaction
- name: Remove-Stream-From-Archive
  property_count: 1
  slug: vonage-remove-stream-from-archive
- name: requestErrorResponse
  property_count: 4
  slug: vonage-request-error-response
- name: response
  property_count: 2
  slug: vonage-response
- name: RetrievalLocationRequest
  property_count: 2
  slug: vonage-retrieval-location-request
- name: Room
  property_count: 17
  slug: vonage-room
- name: searchResponse
  property_count: 14
  slug: vonage-search-response
- name: SilentAuthConfirmationSuccess
  property_count: 2
  slug: vonage-silent-auth-confirmation-success
- name: SMS
  property_count: 2
  slug: vonage-sms
- name: SMSXml
  property_count: 1
  slug: vonage-smsxml
- name: StartStreamRequest
  property_count: 3
  slug: vonage-start-stream-request
- name: StartTalkRequest
  property_count: 7
  slug: vonage-start-talk-request
- name: SubaccountResponse
  property_count: 8
  slug: vonage-subaccount-response
- name: TemplateFragment
  property_count: 7
  slug: vonage-template-fragment
- name: Template
  property_count: 4
  slug: vonage-template
- name: Theme
  property_count: 14
  slug: vonage-theme
- name: TransferBalanceOrCreditRequest
  property_count: 4
  slug: vonage-transfer-balance-or-credit-request
- name: TransferBalanceResponse
  property_count: 6
  slug: vonage-transfer-balance-response
- name: TransferCreditResponse
  property_count: 6
  slug: vonage-transfer-credit-response
- name: TransferNumberResponse
  property_count: 4
  slug: vonage-transfer-number-response
- name: Transfer with Answer URL
  property_count: 2
  slug: vonage-update-call-request-transfer-answer-url
- name: Transfer with NCCO
  property_count: 2
  slug: vonage-update-call-request-transfer-ncco
- name: UpdateRoomRequest
  property_count: 1
  slug: vonage-update-room-request
- name: UploadUrlForTheme
  property_count: 2
  slug: vonage-upload-url-for-theme
- name: user_channels
  property_count: 9
  slug: vonage-user-channels
- name: user
  property_count: 7
  slug: vonage-user
- name: verifyRequest
  property_count: 10
  slug: vonage-verify-request
- name: VideoResponse
  property_count: 2
  slug: vonage-video-response
- name: VoiceRegion
  property_count: 0
  slug: vonage-voice-region
json_structures:
- name: Vonage Message Structure
  property_count: 0
  slug: vonage-message-structure
- name: Vonage Structure
  property_count: 0
  slug: vonage-structure
jsonld:
- class_count: 120
  name: Vonage Context
  property_count: 133
  slug: vonage-context
layout: provider
mcp_servers:
- description: Remote MCP server at documentation-mcp.vonage.dev; 21 tools listed.
  name: Vonage MCP Servers
  slug: vonage-documentation-mcp-server
modified: '2026-10-08'
name: Vonage
nav: Providers
network: true
overview: 'Vonage publishes 59 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Advanced API, Application API, and 56 more. Tagged areas include Communications, Messaging, Telecommunications, Video Conferencing, and Voice.


  The Vonage catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Vonage''s developer surface includes CLI, sandbox, changelog, getting-started guide, authentication, developer portal, documentation, and 59 more developer resources.'
plans:
- name: Vonage Plans Pricing
  plan_count: 0
  slug: vonage-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 12
  name: Vonage Rate Limits
  slug: vonage-rate-limits
rules:
- authorship: generated
  effective_rule_count: 32
  extends:
  - spectral:asyncapi
  name: Vonage — asyncapi rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: vonage-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Vonage — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: vonage-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Vonage API Rules
  rule_count: 64
  severity_counts:
    error: 41
    hint: 0
    info: 6
    warn: 17
  slug: vonage-rules
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 41
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 32.9
    contract_governance: 22.0
    contract_quality: 70.7
    developer_ergonomics: 81.5
    discoverability: 80.8
    operational_transparency: 84.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 70.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 28.8
      derived: 0
      marker_coverage: 0.0
      total: 59
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 19.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/vonage/vonage-2026-06-20T165933.png
security:
- kind: authentication
  name: Vonage Authentication
  slug: vonage-authentication
  summary_line: http basic/http bearer (JWT RS256)/request signature/digest (SIP) · 5 schemes
- kind: domain-security
  name: Vonage Domain Security
  slug: vonage-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vonage Vulnerability Disclosure
  slug: vonage-vulnerability-disclosure
  summary_line: Hackerone
skill_count: 4
skills:
- name: vonage-provision-number
  slug: vonage-provision-number
- name: vonage-send-message-with-failover
  slug: vonage-send-message-with-failover
- name: vonage-verify-user
  slug: vonage-verify-user
- name: vonage-voice-outbound-call-with-audio
  slug: vonage-voice-outbound-call-with-audio
slug: vonage
tags:
- Communications
- Messaging
- Telecommunications
- Video Conferencing
- Voice
- SMS
- Verification
- Real-Time
website: https://www.vonage.com/
---
