---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: derived
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Microsoft Azure Communication Services Agentic Access
  operation_count: 5
  slug: microsoft-azure-communication-services-agentic-access
  summary_line: 5 operations · 5 acting
api_count: 10
apis:
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Call Automation API: answer, redirect and create calls, play media, recognize DTMF/speech, record and transfer server-side. 34 operations, data-plane version 2026-03-12, served from the customer''s Com'
  name: Azure Communication Services Call Automation API
  slug: microsoft-azure-communication-services-callautomation-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Chat API: create chat threads, manage participants, send and read messages and receipts. 16 operations, data-plane version 2025-03-15, served from the customer''s Communication Services resource endpoi'
  name: Azure Communication Services Chat API
  slug: microsoft-azure-communication-services-chat-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Email API: send email from verified domains and poll send-operation status. 2 operations, data-plane version 2025-09-01, served from the customer''s Communication Services resource endpoint.'
  name: Azure Communication Services Email API
  slug: microsoft-azure-communication-services-email-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Identity API: create communication identities and issue or revoke access tokens. 9 operations, data-plane version 2026-09-23, served from the customer''s Communication Services resource endpoint.'
  name: Azure Communication Services Identity API
  slug: microsoft-azure-communication-services-identity-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Job Router API: distribution policies, queues, classification policies, exception policies, jobs and workers for routing work. 33 operations, data-plane version 2023-11-01, served from the customer''s '
  name: Azure Communication Services Job Router API
  slug: microsoft-azure-communication-services-jobrouter-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Advanced Messages API: send WhatsApp notification messages, list templates and download media. 3 operations, data-plane version 2024-08-30, served from the customer''s Communication Services resource e'
  name: Azure Communication Services Advanced Messaging API
  slug: microsoft-azure-communication-services-messages-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Phone Numbers API: search, purchase, update capabilities of and release telephone numbers. 20 operations, data-plane version 2025-06-01, served from the customer''s Communication Services resource endp'
  name: Azure Communication Services Phone Numbers API
  slug: microsoft-azure-communication-services-phonenumbers-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'Rooms API: create and manage rooms and their participants for scheduled interactions. 7 operations, data-plane version 2025-03-13, served from the customer''s Communication Services resource endpoint.'
  name: Azure Communication Services Rooms API
  slug: microsoft-azure-communication-services-rooms-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'SIP Routing API: configure direct-routing trunks and voice routes. 2 operations, data-plane version 2023-03-01, served from the customer''s Communication Services resource endpoint.'
  name: Azure Communication Services SIP Routing API
  slug: microsoft-azure-communication-services-siprouting-api
- baseURL: https://{resource}.communication.azure.com/
  baseurl_source: declared
  description: 'SMS API: send SMS messages and manage opt-outs. 5 operations, data-plane version 2026-01-23, served from the customer''s Communication Services resource endpoint.'
  name: Azure Communication Services SMS API
  slug: microsoft-azure-communication-services-sms-api
artifact_total: 76
asyncapis:
- description: ''
  name: Microsoft Azure Communication Services Webhooks
  slug: microsoft-azure-communication-services-webhooks
collections:
- collection_type: open
  name: Azure Communication Services REST Email API
  slug: open-microsoft-azure-communication-services-email-api
- collection_type: open
  name: Azure Communication Services REST Email Identity API
  slug: open-microsoft-azure-communication-services-identity-api
- collection_type: open
  name: Azure Communication Services REST Email SMS API
  slug: open-microsoft-azure-communication-services-sms-api
- collection_type: open
  name: Azure Communication Services REST API
  slug: open-microsoft-azure-communication-services
common:
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/rules/microsoft-azure-communication-services-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-azure-communication-services-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/json-ld/microsoft-azure-communication-services-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-azure-communication-services-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/vocabulary/microsoft-azure-communication-services-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-azure-communication-services-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-communication-services/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/asyncapi/microsoft-azure-communication-services-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/microsoft-azure-communication-services-webhooks.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/data-model/microsoft-azure-communication-services-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-azure-communication-services-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/components/microsoft-azure-communication-services-components.yml
  title: ''
  type: Components
  url: components/microsoft-azure-communication-services-components.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-communication-services/cli/microsoft-azure-communication-services-cli.yml
  title: ''
  type: CLI
  url: cli/microsoft-azure-communication-services-cli.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-communication-services/changelog/microsoft-azure-communication-services-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/microsoft-azure-communication-services-changelog.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/conventions/microsoft-azure-communication-services-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/microsoft-azure-communication-services-conventions.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/conventions/microsoft-azure-communication-services-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-azure-communication-services-conventions.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/azure/communication-services/acs-retirement-and-breaking-changes-guide
- group: operate
  title: ''
  type: StatusPage
  url: https://azure.status.microsoft/en-us/status
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/lifecycle/microsoft-azure-communication-services-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-azure-communication-services-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/errors/microsoft-azure-communication-services-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-communication-services-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/errors/microsoft-azure-communication-services-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-azure-communication-services-problem-types.yml
- group: design
  href: https://artifacts.apis.io/microsoft-azure-communication-services/conformance/microsoft-azure-communication-services-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-azure-communication-services-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-communication-services/llms/microsoft-azure-communication-services-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-azure-communication-services-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-azure-communication-services/mcp/microsoft-azure-communication-services-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-azure-communication-services-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-communication-services/mcp/microsoft-azure-communication-services-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-azure-communication-services-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/well-known/microsoft-azure-communication-services-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-azure-communication-services-www-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-communication-services/well-known/microsoft-azure-communication-services-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-azure-communication-services-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-communication-services/hosts/microsoft-azure-communication-services-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-azure-communication-services-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-azure-communication-services/vendors/microsoft-azure-communication-services-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-azure-communication-services-vendors.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-communication-services/packages/microsoft-azure-communication-services-packages.yml
  title: ''
  type: SDKs
  url: packages/microsoft-azure-communication-services-packages.yml
- group: build
  href: https://artifacts.apis.io/microsoft-azure-communication-services/packages/microsoft-azure-communication-services-packages.yml
  title: ''
  type: Packages
  url: packages/microsoft-azure-communication-services-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/scopes/microsoft-azure-communication-services-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-azure-communication-services-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://azure.microsoft.com/en-us/products/communication-services
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/security/microsoft-azure-communication-services-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-azure-communication-services-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/security/microsoft-azure-communication-services-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-azure-communication-services-vulnerability-disclosure.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-communication-services/plans/microsoft-azure-communication-services-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-azure-communication-services-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/microsoft-azure-communication-services/rate-limits/microsoft-azure-communication-services-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-azure-communication-services-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-azure-communication-services/finops/microsoft-azure-communication-services-finops.yml
  title: ''
  type: FinOps
  url: finops/microsoft-azure-communication-services-finops.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-azure-communication-services/agentic-access/microsoft-azure-communication-services-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-azure-communication-services-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/security/microsoft-azure-communication-services-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-azure-communication-services-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-azure-communication-services/authentication/microsoft-azure-communication-services-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-azure-communication-services-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Azure
- group: start
  title: ''
  type: Portal
  url: https://portal.azure.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://azure.microsoft.com/en-us/pricing/details/communication-services/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://privacy.microsoft.com/en-us/privacystatement
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/
- group: company
  title: ''
  type: Blog
  url: https://azure.microsoft.com/en-us/blog/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/azure/communication-services/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/rest/api/communication/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/azure/communication-services/quickstarts/create-communication-resource
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/azure/communication-services/whats-new
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/Azure/azure-rest-api-specs/tree/main/specification/communication/data-plane
created: '2026-03-13'
description: Azure Communication Services is Microsoft Azure's cloud communications platform-as-a-service, exposing data-plane REST APIs for SMS, email, chat, voice and video calling (Call Automation), Rooms, Job Router, phone number management, SIP direct routing, WhatsApp Advanced Messaging and identity/token issuance, authenticated by HMAC-SHA256 access keys or Microsoft Entra ID, with SDKs for .NET, Java, JavaScript, Python, iOS and Android.
finops:
- has_sources: false
  method: generated
  name: Microsoft Azure Communication Services Finops
  primary_unit: request
  service_category: API
  slug: microsoft-azure-communication-services-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-azure-communication-services.png
json_schemas:
- name: AddParticipantRequest
  property_count: 7
  slug: microsoft-azure-communication-services-add-participant-request
- name: CallConnectionProperties
  property_count: 13
  slug: microsoft-azure-communication-services-call-connection-properties
- name: ChatMessageReadReceiptsCollection
  property_count: 2
  slug: microsoft-azure-communication-services-chat-message-read-receipts-collection
- name: ChatMessage
  property_count: 11
  slug: microsoft-azure-communication-services-chat-message
- name: ChatThreadProperties
  property_count: 7
  slug: microsoft-azure-communication-services-chat-thread-properties
- name: ClassificationPolicy
  property_count: 7
  slug: microsoft-azure-communication-services-classification-policy
- name: CommunicationIdentityAccessTokenRequest
  property_count: 2
  slug: microsoft-azure-communication-services-communication-identity-access-token-request
- name: CommunicationIdentityAccessTokenResult
  property_count: 2
  slug: microsoft-azure-communication-services-communication-identity-access-token-result
- name: CommunicationIdentityCreateRequest
  property_count: 2
  slug: microsoft-azure-communication-services-communication-identity-create-request
- name: CreateCallRequest
  property_count: 10
  slug: microsoft-azure-communication-services-create-call-request
- name: CreateChatThreadRequest
  property_count: 4
  slug: microsoft-azure-communication-services-create-chat-thread-request
- name: CreateRoomRequest
  property_count: 4
  slug: microsoft-azure-communication-services-create-room-request
- name: DeliveryReport
  property_count: 9
  slug: microsoft-azure-communication-services-delivery-report
- name: EmailMessage
  property_count: 7
  slug: microsoft-azure-communication-services-email-message
- name: EmailSendResult
  property_count: 3
  slug: microsoft-azure-communication-services-email-send-result
- name: OptOutRequest
  property_count: 2
  slug: microsoft-azure-communication-services-opt-out-request
- name: OptOutResponse
  property_count: 1
  slug: microsoft-azure-communication-services-opt-out-response
- name: PagedMessageTemplateItem
  property_count: 2
  slug: microsoft-azure-communication-services-paged-message-template-item
- name: ParticipantsCollection
  property_count: 2
  slug: microsoft-azure-communication-services-participants-collection
- name: PhoneNumberOperation
  property_count: 7
  slug: microsoft-azure-communication-services-phone-number-operation
- name: PhoneNumberSearchRequest
  property_count: 5
  slug: microsoft-azure-communication-services-phone-number-search-request
- name: PhoneNumberSearchResult
  property_count: 10
  slug: microsoft-azure-communication-services-phone-number-search-result
- name: PhoneNumbersBrowseRequest
  property_count: 4
  slug: microsoft-azure-communication-services-phone-numbers-browse-request
- name: PhoneNumbersReservation
  property_count: 4
  slug: microsoft-azure-communication-services-phone-numbers-reservation
- name: PlayRequest
  property_count: 6
  slug: microsoft-azure-communication-services-play-request
- name: PurchasedPhoneNumber
  property_count: 8
  slug: microsoft-azure-communication-services-purchased-phone-number
- name: RecognizeRequest
  property_count: 7
  slug: microsoft-azure-communication-services-recognize-request
- name: RoomModel
  property_count: 5
  slug: microsoft-azure-communication-services-room-model
- name: RoomsCollection
  property_count: 2
  slug: microsoft-azure-communication-services-rooms-collection
- name: RouterJobCreateOrUpdate
  property_count: 11
  slug: microsoft-azure-communication-services-router-job-create-or-update
- name: RouterJob
  property_count: 18
  slug: microsoft-azure-communication-services-router-job
- name: RouterQueue
  property_count: 6
  slug: microsoft-azure-communication-services-router-queue
- name: RouterWorkerCreateOrUpdate
  property_count: 6
  slug: microsoft-azure-communication-services-router-worker-create-or-update
- name: RouterWorker
  property_count: 12
  slug: microsoft-azure-communication-services-router-worker
- name: SendChatMessageRequest
  property_count: 4
  slug: microsoft-azure-communication-services-send-chat-message-request
- name: SendMessageRequest
  property_count: 4
  slug: microsoft-azure-communication-services-send-message-request
- name: SendMessageResult
  property_count: 1
  slug: microsoft-azure-communication-services-send-message-result
- name: SipConfiguration
  property_count: 2
  slug: microsoft-azure-communication-services-sip-configuration
- name: SipConfigurationUpdate
  property_count: 2
  slug: microsoft-azure-communication-services-sip-configuration-update
- name: SmsSendResponse
  property_count: 1
  slug: microsoft-azure-communication-services-sms-send-response
- name: StartCallRecordingRequest
  property_count: 10
  slug: microsoft-azure-communication-services-start-call-recording-request
- name: TeamsExtensionAssignmentCreateOrUpdateRequest
  property_count: 2
  slug: microsoft-azure-communication-services-teams-extension-assignment-create-or-update-request
- name: TeamsExtensionAssignmentResponse
  property_count: 4
  slug: microsoft-azure-communication-services-teams-extension-assignment-response
- name: TeamsUserExchangeTokenRequest
  property_count: 3
  slug: microsoft-azure-communication-services-teams-user-exchange-token-request
- name: UpdateChatThreadRequest
  property_count: 3
  slug: microsoft-azure-communication-services-update-chat-thread-request
- name: UpdateParticipantsRequest
  property_count: 1
  slug: microsoft-azure-communication-services-update-participants-request
- name: UpdateRoomRequest
  property_count: 3
  slug: microsoft-azure-communication-services-update-room-request
jsonld:
- class_count: 120
  name: Microsoft Azure Communication Services Context
  property_count: 147
  slug: microsoft-azure-communication-services-context
layout: provider
mcp_servers:
- description: MCP server requiring OAuth; 2 tools listed.
  name: Azure MCP Server - Azure Communication Services tools
  slug: azure-mcp-server---azure-communication-services-tools
modified: '2026-11-05'
name: Microsoft Azure Communication Services
nav: Providers
network: true
overview: 'Microsoft Azure Communication Services publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Azure Communication Services Call Automation API, Azure Communication Services Chat API, Azure Communication Services Email API, and 7 more. Tagged areas include Microsoft Azure, CPaaS, Calling, Chat, and Communications.


  The Microsoft Azure Communication Services catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Microsoft Azure Communication Services'' developer surface includes CLI, changelog, authentication, developer portal, pricing, support, engineering blog, and 44 more developer resources.'
plans:
- name: Microsoft Azure Communication Services Plans Pricing
  plan_count: 3
  slug: microsoft-azure-communication-services-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 24
  name: Microsoft Azure Communication Services Rate Limits
  slug: microsoft-azure-communication-services-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Microsoft Azure Communication Services API Rules
  rule_count: 57
  severity_counts:
    error: 42
    hint: 0
    info: 7
    warn: 8
  slug: microsoft-azure-communication-services-rules
scopes:
- name: Microsoft Azure Communication Services Scopes
  scope_count: 2
  slug: microsoft-azure-communication-services-scopes
  summary_line: 2 scopes · authorizationCode/implicit
score:
  band: exemplar
  composite: 71.2
  coverage:
    artifact_dirs: 35
    catalog_earned: 89.8
    catalog_earned_first_party: 24.0
    catalog_gap: 25.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.2
  facets:
    access_clarity: 78.9
    contract_governance: 22.0
    contract_quality: 62.0
    developer_ergonomics: 73.2
    discoverability: 78.3
    operational_transparency: 92.1
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-azure-communication-services/microsoft-azure-communication-services-2026-06-20T185404.png
security:
- kind: authentication
  name: Microsoft Azure Communication Services Authentication
  slug: microsoft-azure-communication-services-authentication
  summary_line: apiKey/oauth2 · 4 schemes
- kind: domain-security
  name: Microsoft Azure Communication Services Domain Security
  slug: microsoft-azure-communication-services-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Azure Communication Services Vulnerability Disclosure
  slug: microsoft-azure-communication-services-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Azure Communication Services Trust Center
  slug: microsoft-azure-communication-services-trust-center
  summary_line: GDPR
skill_count: 2
skills:
- name: send-email
  slug: microsoft-azure-communication-services-send-email
- name: send-sms
  slug: microsoft-azure-communication-services-send-sms
slug: microsoft-azure-communication-services
tags:
- Microsoft Azure
- CPaaS
- Calling
- Chat
- Communications
- Contact Center
- Email
- Identity
- Messaging
- Phone Numbers
- Rooms
- Routing
- SIP
- SMS
- Telephony
- Tokens
- Video
- Voice
- WhatsApp
website: https://azure.microsoft.com/en-us/products/communication-services
---
