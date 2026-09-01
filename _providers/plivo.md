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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Plivo Agentic Access
  operation_count: 6
  slug: plivo-agentic-access
  summary_line: 6 operations · 2 acting
api_count: 1
apis:
- description: The Plivo Account API exposes account-level details (auth ID, auth token, billing balance, address, account type, max-call configuration) and supports updating account properties.
  name: Plivo Account API
  slug: plivo-account-api
- description: The Plivo Subaccount API supports creating, updating, listing, activating, and deleting subaccounts under a parent Plivo account, enabling multi-tenant isolation of usage and billing.
  name: Plivo Subaccount API
  slug: plivo-subaccount-api
- description: The Plivo Application API manages voice applications — bundles of XML/answer/hangup/fallback URLs (and message URL bindings) used to control inbound and outbound call behavior.
  name: Plivo Application API
  slug: plivo-application-api
- description: The Plivo SIP Authentication API issues per-account credentials used by SIP endpoints to register against Plivo's SIP infrastructure.
  name: Plivo SIP Authentication API
  slug: plivo-sip-authentication-api
- description: The Plivo Voice Call API initiates outbound calls, retrieves details for live and historical calls, and supports active-call control (transfer, record, play, speak, hangup, DTMF send) on in-progress c
  name: Plivo Voice Call API
  slug: plivo-call-api
- description: The Plivo Conference API manages live conference rooms — listing, retrieving members, kicking, muting, deafening, recording, and playing media into a conference.
  name: Plivo Conference API
  slug: plivo-conference-api
- description: The Plivo Multiparty Call API supports building multi-participant calls programmatically — adding/removing participants, managing roles, recording, and barge/whisper supervisory actions.
  name: Plivo Multiparty Call API
  slug: plivo-multiparty-call-api
- description: The Plivo Recording API exposes call and conference recordings — listing, retrieving, downloading, and deleting recorded media.
  name: Plivo Recording API
  slug: plivo-recording-api
- description: The Plivo Endpoint API manages SIP/WebRTC endpoints (username/password/alias) used by softphones, browser SDKs, and devices to register and place/receive calls.
  name: Plivo Endpoint API
  slug: plivo-endpoint-api
- description: The Plivo Audio Stream API attaches a real-time WebSocket audio stream to a live call, enabling AI voice agents, real-time transcription, and analytics. Plivo opens a WSS connection to a customer-oper
  name: Plivo Audio Stream API
  slug: plivo-audio-stream-api
- description: The Plivo Verified Caller ID API allows trial accounts to verify outbound caller IDs for use as the From number in outbound calls.
  name: Plivo Verified Caller ID API
  slug: plivo-verified-caller-id-api
- description: The Plivo Message API sends and receives SMS, MMS, and WhatsApp messages, retrieves delivery status reports, and lists historical messages.
  name: Plivo Message API
  slug: plivo-message-api
- description: The Plivo Media API uploads, lists, retrieves, and deletes media files used as MMS or WhatsApp attachments.
  name: Plivo Media API
  slug: plivo-media-api
- description: The Plivo Powerpack API creates and manages Powerpacks — pools of numbers that distribute outbound messaging traffic for higher throughput, sticky-sender behavior, and improved deliverability.
  name: Plivo Powerpack API
  slug: plivo-powerpack-api
- description: The Plivo 10DLC API registers brands and campaigns with The Campaign Registry for US application-to-person (A2P) SMS compliance.
  name: Plivo 10DLC Brand and Campaign API
  slug: plivo-10dlc-api
- description: The Plivo Toll-Free Verification API submits and tracks toll-free messaging verification cases required for sustained throughput on TFNs.
  name: Plivo Toll-Free Verification API
  slug: plivo-toll-free-verification-api
- description: The Plivo Numbers API searches the global number inventory, rents and releases phone numbers (long codes, toll-free, short codes, mobile numbers), and manages number application bindings.
  name: Plivo Numbers API
  slug: plivo-numbers-api
- description: The Plivo Pricing API retrieves current voice and messaging rates per ISO country code, supporting cost estimation and rate-card synchronization for downstream billing.
  name: Plivo Pricing API
  slug: plivo-pricing-api
- description: The Plivo Verify API delivers OTPs over SMS, voice, WhatsApp, or email and verifies user-supplied codes, supporting 2FA and identity-confirmation flows.
  name: Plivo Verify API
  slug: plivo-verify-api
- description: The Plivo Lookup API validates phone numbers and returns formatting, country, line type, carrier, and reachability metadata to feed cleansing, fraud-prevention, and routing decisions.
  name: Plivo Lookup API
  slug: plivo-lookup-api
- description: The Plivo Zentrunk SIP Trunking API manages termination and origination SIP trunks — outbound trunks (credentials, IP ACLs, dial prefixes) and origination/inbound trunks (URI, source IPs, recording).
  name: Plivo Zentrunk SIP Trunking API
  slug: plivo-zentrunk-sip-trunking-api
- description: The Plivo CNAM and Branded Calling API manages caller-name lookup and branded outbound caller-display configurations on outbound voice calls.
  name: Plivo CNAM Lookup and Branded Calling API
  slug: plivo-cnam-api
- description: Account-level configuration and details.
  name: Plivo Account API
  slug: plivo-account-api
- description: Send and retrieve SMS, MMS, and WhatsApp messages.
  name: Plivo Message API
  slug: plivo-message-api
artifact_total: 40
asyncapis:
- description: The Plivo Audio Streaming API delivers near real-time raw audio from active Plivo voice calls to a customer-operated WebSocket server, and (when bidirectional streaming is enabled) accepts audio and c
  name: Plivo Audio Streaming WebSocket API
  slug: plivo-asyncapi
collections:
- collection_type: postman
  name: Plivo Account API
  slug: postman-plivo-account-api
- collection_type: postman
  name: Plivo Account Message API
  slug: postman-plivo-message-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Plivo Account API
  slug: open-plivo-account-api
- collection_type: open
  name: Plivo Account Message API
  slug: open-plivo-message-api
- collection_type: open
  name: Plivo API
  slug: open-plivo
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/plivo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plivo-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/plivo-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plivo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plivo-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plivo-inc
- group: company
  title: ''
  type: Website
  url: https://www.plivo.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.plivo.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.plivo.com/docs/sms/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.plivo.com/docs/getting-started/
- group: auth
  title: ''
  type: Authentication
  url: https://www.plivo.com/docs/account/api/account/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.plivo.com/pricing/
- group: build
  title: ''
  type: SDKs
  url: https://www.plivo.com/docs/sdks/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.plivo.com/
- group: start
  title: ''
  type: Signup
  url: https://console.plivo.com/accounts/register/
- group: start
  title: ''
  type: Login
  url: https://console.plivo.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/plivo
- group: build
  title: ''
  type: Node.js SDK
  url: https://github.com/plivo/plivo-node
- group: build
  title: ''
  type: Python SDK
  url: https://github.com/plivo/plivo-python
- group: build
  title: ''
  type: PHP SDK
  url: https://github.com/plivo/plivo-php
- group: build
  title: ''
  type: Ruby SDK
  url: https://github.com/plivo/plivo-ruby
- group: build
  title: ''
  type: Java SDK
  url: https://github.com/plivo/plivo-java
- group: build
  title: ''
  type: Go SDK
  url: https://github.com/plivo/plivo-go
- group: build
  title: ''
  type: .NET SDK
  url: https://github.com/plivo/plivo-dotnet
- group: build
  title: ''
  type: Browser SDK
  url: https://www.plivo.com/docs/sdk/web/
- group: build
  title: ''
  type: iOS SDK
  url: https://www.plivo.com/docs/sdk/ios/
- group: build
  title: ''
  type: Android SDK
  url: https://www.plivo.com/docs/sdk/android/
- group: company
  title: ''
  type: Blog
  url: https://www.plivo.com/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.plivo.com/changelog/
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/plivo
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/c/Plivo
- group: commercial
  title: ''
  type: Plans
  url: plans/plivo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plivo-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plivo-finops.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/plivo/mcp
created: '2026-05-08'
description: Plivo is a global communications platform offering programmable Voice, Messaging (SMS/MMS/WhatsApp), SIP Trunking, Verify, and Lookup APIs, plus an AI Voice Agent platform. The HTTP API is available at https://api.plivo.com/v1/ with HTTP Basic Auth using Auth ID and Auth Token credentials.
finops:
- name: Plivo Finops
  service_category: Communications
  slug: plivo-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plivo.png
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-29'
name: Plivo
nav: Providers
network: true
overview: 'Plivo publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Account API, Audio Stream API, Message API, and 2 more. Tagged areas include Communications, CPaaS, Voice, SMS, and Messaging.


  The Plivo catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Plivo''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, and 28 more developer resources.'
plans:
- name: Plivo Plans Pricing
  plan_count: 3
  slug: plivo-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Plivo Rate Limits
  slug: plivo-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Plivo API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: plivo-asyncapi-spectral-rules
score:
  band: developing
  composite: 43.5
  coverage:
    artifact_dirs: 13
    catalog_gap: 74.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 40.8
    commercial_clarity: 40.8
    contract_governance: 13.6
    contract_quality: 60.2
    developer_ergonomics: 45.2
    discoverability: 50.0
    governance: 13.6
    operational_transparency: 42.1
  previous_composite: 43.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plivo/refs/heads/main/screenshots/plivo-2026-06-20T191841.png
security:
- kind: authentication
  name: Plivo Authentication
  slug: plivo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plivo Domain Security
  slug: plivo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Plivo Trust Center
  slug: plivo-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR, CSA STAR
slug: plivo
tags:
- Communications
- CPaaS
- Voice
- SMS
- Messaging
- WhatsApp
- SIP Trunking
- Verify
website: https://www.plivo.com/
---
