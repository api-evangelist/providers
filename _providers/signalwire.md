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
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.6
  scored_at: '2026-09-05'
api_count: 4
apis:
- description: An OpenRPC 1.3.2 contract for real-time control of live calls over RELAY — 8 methods (calling.dial, calling.update, calling.end, calling.ai_hold, calling.ai_unhold, calling.ai_message, calling.live_tr
  name: SignalWire Calling API (JSON-RPC)
  slug: signalwire-calling-rpc
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage SignalWire projects and subprojects.
  name: SignalWire Accounts API
  slug: signalwire-accounts-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: 'Client-side endpoints for listing and retrieving resource addresses using [subscriber](/docs/platform/subscribers) access tokens (SAT). Intended for use with the Browser SDK to resolve addresses from '
  name: SignalWire Addresses API
  slug: signalwire-addresses-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing SignalWire AI Agents
  name: 'SignalWire AI Agents: Custom API'
  slug: signalwire-ai-agents-custom-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing Dialogflow Agents
  name: 'SignalWire AI Agents: Dialogflow API'
  slug: signalwire-ai-agents-dialogflow-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to holding a text conversation with an AI agent
  name: SignalWire AI Chat API
  slug: signalwire-ai-chat-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Callbacks an AI agent sends to your server. The same payloads apply to every surface an agent runs on — voice calls, Amazon Bedrock agents, sidecar agents, and text conversations.
  name: SignalWire AI Webhooks API
  slug: signalwire-ai-webhooks-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage cXML applications for handling voice and messaging.
  name: SignalWire Applications API
  slug: signalwire-applications-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Search for available phone numbers to purchase.
  name: SignalWire Available Phone Numbers API
  slug: signalwire-available-phone-numbers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing Call Flows
  name: SignalWire Call Flows API
  slug: signalwire-call-flows-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: 'Callbacks about a call: the SWML document request sent when a call arrives, and the progress of work you started on it such as a transcription or a background audio stream.'
  name: SignalWire Calling Webhooks API
  slug: signalwire-calling-webhooks-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage voice calls and call recordings.
  name: SignalWire Calls API
  slug: signalwire-calls-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Register and manage brands for 10DLC campaign registration.
  name: 'SignalWire Campaign Registry: Brands API'
  slug: signalwire-campaign-registry-brands-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Create and manage 10DLC campaigns for A2P messaging compliance.
  name: 'SignalWire Campaign Registry: Campaigns API'
  slug: signalwire-campaign-registry-campaigns-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Assign and manage phone numbers within 10DLC campaigns.
  name: 'SignalWire Campaign Registry: Phone Number Assignments API'
  slug: signalwire-campaign-registry-phone-number-assignments-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage Chat tokens.
  name: SignalWire Chat Tokens API
  slug: signalwire-chat-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage chunks within Datasphere documents.
  name: SignalWire Chunks API
  slug: signalwire-chunks-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage and query conference log data.
  name: SignalWire Conference Logs API
  slug: signalwire-conference-logs-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage participants in conference calls.
  name: SignalWire Conference Participants API
  slug: signalwire-conference-participants-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage recordings for conference calls.
  name: SignalWire Conference Recordings API
  slug: signalwire-conference-recordings-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing Conference Rooms
  name: SignalWire Conference Rooms API
  slug: signalwire-conference-rooms-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage media streams for conferences.
  name: SignalWire Conference Streams API
  slug: signalwire-conference-streams-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage conference tokens
  name: SignalWire Conference Tokens API
  slug: signalwire-conference-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage conference calls.
  name: SignalWire Conferences API
  slug: signalwire-conferences-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing cXML Applications
  name: SignalWire cXML Applications API
  slug: signalwire-cxml-applications-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage cXML scripts for storing XML instructions.
  name: SignalWire CXML Scripts API
  slug: signalwire-cxml-scripts-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing cXML Webhooks
  name: SignalWire cXML Webhook API
  slug: signalwire-cxml-webhook-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage Datasphere documents.
  name: SignalWire Documents API
  slug: signalwire-documents-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to managing Domain Applications
  name: SignalWire Domain Applications API
  slug: signalwire-domain-applications-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage E911 addresses for regulatory compliance and phone number provisioning.
  name: SignalWire E911 Addresses API
  slug: signalwire-e911-addresses-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to accessing fax logs
  name: SignalWire Fax Logs API
  slug: signalwire-fax-logs-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage fax media files.
  name: SignalWire Fax Media API
  slug: signalwire-fax-media-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Send and manage faxes.
  name: SignalWire Faxes API
  slug: signalwire-faxes-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing FreeSWITCH Connectors
  name: SignalWire FreeSWITCH Connector API
  slug: signalwire-freeswitch-connector-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Import phone numbers hosted elsewhere into your SignalWire Space.
  name: SignalWire Imported Phone Numbers API
  slug: signalwire-imported-phone-numbers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage phone numbers in your project.
  name: SignalWire Incoming Phone Numbers API
  slug: signalwire-incoming-phone-numbers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to accessing message logs
  name: SignalWire Message Logs API
  slug: signalwire-message-logs-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage media files attached to messages.
  name: SignalWire Message Media API
  slug: signalwire-message-media-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Send and manage SMS/MMS messages.
  name: SignalWire Messages API
  slug: signalwire-messages-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: 'Callbacks about a message: the SWML document request sent when a message arrives, delivery state for messages you send, and 10DLC registration state.'
  name: SignalWire Messaging Webhooks API
  slug: signalwire-messaging-webhooks-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Multi-factor authentication adds security to your application by requesting a user to be verified via voice or via text message. It can also be used for One Time Password flows (OTP).
  name: SignalWire Multi-Factor Authentication API
  slug: signalwire-multi-factor-authentication-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage phone number memberships within number groups.
  name: SignalWire Number Group Membership API
  slug: signalwire-number-group-membership-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage number groups for organizing phone numbers.
  name: SignalWire Number Groups API
  slug: signalwire-number-groups-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Look up information about phone numbers.
  name: SignalWire Phone Number Lookup API
  slug: signalwire-phone-number-lookup-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage phone numbers for your SignalWire project.
  name: SignalWire Phone Numbers API
  slug: signalwire-phone-numbers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to managing Phone Routes
  name: SignalWire Phone Routes API
  slug: signalwire-phone-routes-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage API tokens for authentication.
  name: SignalWire Project Tokens API
  slug: signalwire-project-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage projects and subprojects under the authenticated root project.
  name: SignalWire Projects API
  slug: signalwire-projects-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing PubSub Tokens
  name: SignalWire PubSub Tokens API
  slug: signalwire-pubsub-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage members in call queues.
  name: SignalWire Queue Members API
  slug: signalwire-queue-members-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage call queues.
  name: SignalWire Queues API
  slug: signalwire-queues-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage transcriptions of recordings.
  name: SignalWire Recording Transcriptions API
  slug: signalwire-recording-transcriptions-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage call recordings.
  name: SignalWire Recordings API
  slug: signalwire-recordings-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing Relay Applications
  name: SignalWire Relay Application API
  slug: signalwire-relay-application-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing Resources
  name: SignalWire Resources API
  slug: signalwire-resources-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage room recordings
  name: SignalWire Room Recordings API
  slug: signalwire-room-recordings-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage room sessions
  name: SignalWire Room Sessions API
  slug: signalwire-room-sessions-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage room tokens
  name: SignalWire Room Tokens API
  slug: signalwire-room-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage video rooms
  name: SignalWire Rooms API
  slug: signalwire-rooms-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage short codes for SMS and MMS messaging.
  name: SignalWire Short Codes API
  slug: signalwire-short-codes-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing SIP Addresses — the SIP configuration (username, Domain, codecs, ciphers, encryption, IP authentication, registration password) for the resource that handles c
  name: SignalWire SIP Addresses API
  slug: signalwire-sip-addresses-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage SIP credentials for authenticating SIP endpoints.
  name: SignalWire SIP Credentials API
  slug: signalwire-sip-credentials-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage SIP endpoints for voice communication. Use SIP Credentials for new integrations.
  name: SignalWire SIP Endpoints (Legacy) API
  slug: signalwire-sip-endpoints-legacy-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing SIP Gateways
  name: SignalWire SIP Gateway API
  slug: signalwire-sip-gateway-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage SIP profile settings.
  name: SignalWire SIP Profile API
  slug: signalwire-sip-profile-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage domain applications for call handling configuration.
  name: SignalWire Space Domain Applications API
  slug: signalwire-space-domain-applications-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage media streams for calls.
  name: SignalWire Streams API
  slug: signalwire-streams-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing [Subscriber](/docs/platform/subscribers) SIP Endpoints.
  name: SignalWire Subscriber SIP Credentials API
  slug: signalwire-subscriber-sip-credentials-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing [Subscriber](/docs/platform/subscribers) tokens.
  name: SignalWire Subscriber Tokens API
  slug: signalwire-subscriber-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing [Subscribers](/docs/platform/subscribers).
  name: SignalWire Subscribers API
  slug: signalwire-subscribers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing SWML Scripts
  name: SignalWire SWML Scripts API
  slug: signalwire-swml-scripts-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to creating & managing SWML Webhooks
  name: SignalWire SWML Webhook API
  slug: signalwire-swml-webhook-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage API tokens for authentication.
  name: SignalWire Tokens API
  slug: signalwire-tokens-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage verified caller IDs for phone numbers not purchased through SignalWire.
  name: SignalWire Verified Caller ID API
  slug: signalwire-verified-caller-id-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Manage video conferences
  name: SignalWire Video Conferences API
  slug: signalwire-video-conferences-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: View video logs
  name: SignalWire Video Logs API
  slug: signalwire-video-logs-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Endpoints related to accessing voice logs
  name: SignalWire Voice Logs API
  slug: signalwire-voice-logs-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: List the WhatsApp Business Accounts connected to your Space.
  name: SignalWire WhatsApp Businesses API
  slug: signalwire-whatsapp-businesses-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: List and retrieve the WhatsApp numbers connected to your Space.
  name: SignalWire WhatsApp Numbers API
  slug: signalwire-whatsapp-numbers-api
- baseURL: https://{space_name}.signalwire.com
  baseurl_source: declared
  description: Create and manage the Meta-approved templates required to start WhatsApp conversations.
  name: SignalWire WhatsApp Templates API
  slug: signalwire-whatsapp-templates-api
artifact_total: 89
asyncapis:
- description: ''
  name: Signalwire Webhooks
  slug: signalwire-webhooks
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/signalwire-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/signalwire-rest-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/signalwire-compatibility-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://signalwire.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://signalwire.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://signalwire.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://signalwire.com/docs/apis
- group: start
  title: ''
  type: GettingStarted
  url: https://signalwire.com/docs/platform/getting-started
- group: operate
  title: ''
  type: Support
  url: https://support.signalwire.com/portal/en/home
- group: company
  title: ''
  type: Blog
  url: https://signalwire.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/signalwire
- group: build
  title: ''
  type: Postman
  url: https://signalwire.com/docs/apis#try-it-in-postman
- group: commercial
  title: ''
  type: Pricing
  url: https://signalwire.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://signalwire.com/signup
- group: start
  title: ''
  type: Login
  url: https://id.signalwire.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://signalwire.com/legal
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://signalwire.com/legal
- group: operate
  title: ''
  type: StatusPage
  url: https://status.signalwire.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://compliance.signalwire.com
- group: auth
  title: ''
  type: Compliance
  url: security/signalwire-trust-center.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/signalwire-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/signalwire-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/signalwire-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/signalwire-cli.yml
- group: design
  title: ''
  type: Components
  url: components/signalwire-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/signalwire-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/signalwire-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/signalwire-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signalwire-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/signalwire-docs-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/signalwire-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/signalwire-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/signalwire-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/signalwire-webhooks.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/signalwire-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/signalwire-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/signalwire-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/signalwire-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/signalwire-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/signalwire-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/signalwire-vulnerability-disclosure.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/signalwire-swml.json
- group: other
  title: ''
  type: OpenRPC
  url: openapi/signalwire-calling-openrpc.yml
created: '2026-08-27'
description: SignalWire is a Programmable Unified Communications (PUC) platform for voice, messaging, video, fax, SIP and AI voice agents, built by the team behind FreeSWITCH. It publishes two first-party OpenAPI 3.1 contracts from its public documentation repository — a 253-operation SignalWire REST API covering calling, messaging, video rooms, phone number management, Campaign Registry/10DLC, WhatsApp, Datasphere, SIP resources, subscribers, AI agents and logs, and a 79-operation Twilio-compatible Compatibility (LaML) API at /api/laml/2010-04-01 — plus an OpenRPC 1.3.2 JSON-RPC contract for live call control, a JSON Schema for SWML (SignalWire Markup Language), and 19 OpenAPI 3.1 webhook definitions covering AI/SWAIG, calling and messaging callbacks. Every request is served from a per-customer Space subdomain, {space_name}.signalwire.com, over HTTPS only.
image: https://framerusercontent.com/images/51HrN1SGYsDuDnTD4zDO4buJMM.png
json_schemas:
- name: SWML Object
  property_count: 2
  slug: signalwire-swml
layout: provider
mcp_servers:
- description: ''
  name: SignalWire Documentation MCP Server
  slug: signalwire-documentation-mcp-server
modified: '2026-08-27'
name: SignalWire
nav: Providers
network: true
overview: 'SignalWire publishes 79 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, AI Agents: Custom API, and 76 more. Tagged areas include Company, Communications, CPaaS, Voice, and Messaging.


  The SignalWire catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  SignalWire''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 37 more developer resources.'
plans:
- name: Signalwire Plans Pricing
  plan_count: 0
  slug: signalwire-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 10
  name: Signalwire Rate Limits
  slug: signalwire-rate-limits
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 25
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.1
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 67.7
    developer_ergonomics: 90.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 68.5
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 79
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 56.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/signalwire/refs/heads/main/screenshots/signalwire-2026-09-02T155435.png
security:
- kind: authentication
  name: Signalwire Authentication
  slug: signalwire-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Signalwire Domain Security
  slug: signalwire-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Signalwire Vulnerability Disclosure
  slug: signalwire-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Signalwire Trust Center
  slug: signalwire-trust-center
  summary_line: SOC 2 Type II, PCI DSS, HIPAA
slug: signalwire
tags:
- Company
- Communications
- CPaaS
- Voice
- Messaging
- SMS
- Video
- WebRTC
- SIP
- Telephony
- Fax
- AI Agents
- Conversational AI
- Contact Center
website: https://signalwire.com
---
