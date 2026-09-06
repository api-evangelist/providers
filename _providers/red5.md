---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 18
  human_in_the_loop: 1
  name: Red5 Agentic Access
  operation_count: 35
  slug: red5-agentic-access
  summary_line: 35 operations · 18 acting · 1 human-in-the-loop
api_count: 3
apis:
- baseURL: https://{streamManagerDomain}/as/v1
  baseurl_source: declared
  description: The Red5 Pro WebRTC SDK is a JavaScript library for integrating low-latency live streaming publish and subscribe capabilities into web applications. It supports WHIP for WebRTC publishing and WHEP for
  name: Red5 Pro WebRTC SDK
  slug: webrtc-sdk
- description: 'The Red5 Core SDK is a native client library for building real-time streaming applications on Linux, Windows, and macOS desktop platforms. It offers interfaces for server connection management, media '
  name: Red5 Core SDK
  slug: core-sdk
- description: The Red5 Pro iOS Streaming SDK is a native iOS library for integrating real-time live streaming publish and subscribe capabilities into iOS applications. It supports H.264 video and AAC/Opus audio enc
  name: Red5 Pro iOS Streaming SDK
  slug: ios-sdk
- description: The Red5 Pro Android Streaming SDK is a native Android library for integrating real-time live streaming publish and subscribe capabilities into Android applications. It supports H.264/H.265 video enco
  name: Red5 Pro Android Streaming SDK
  slug: android-sdk
- baseURL: https://{streamManagerDomain}/as/v1
  baseurl_source: declared
  description: Node metrics, system info, and autoscaling management
  name: Red5 Admin API
  slug: red5-admin-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Restream recorded FLV or MP4 files as pseudo-live streams
  name: Red5 File Restreamer API
  slug: red5-file-restreamer-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Image overlay management for mixer sessions
  name: Red5 Images API
  slug: red5-images-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Input stream management for mixer sessions
  name: Red5 Inputs API
  slug: red5-inputs-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Mixer session lifecycle management
  name: Red5 Mixers API
  slug: red5-mixers-api
- baseURL: https://{streamManagerDomain}/as/v1
  baseurl_source: declared
  description: Stream provisioning, authentication, and configuration
  name: Red5 Provision API
  slug: red5-provision-api
- baseURL: https://{streamManagerDomain}/as/v1
  baseurl_source: declared
  description: WHIP, WHEP, and WebSocket proxy endpoints
  name: Red5 Proxy API
  slug: red5-proxy-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Configure RTMP and RTMPS push/pull restreaming
  name: Red5 RTMP Restreamer API
  slug: red5-rtmp-restreamer-api
- baseURL: http://{host}:5080
  baseurl_source: declared
  description: Server-level restreamer plugin configuration
  name: Red5 Servlet Configuration API
  slug: red5-servlet-configuration-api
- baseURL: https://{streamManagerDomain}/as/v1
  baseurl_source: declared
  description: Live stream enumeration, statistics, and control
  name: Red5 Streams API
  slug: red5-streams-api
- description: REST/JSON API embedded in the Red5 Pro media server providing server info/ping/statistics, applications, streams, recorded content (VOD), shared objects, client control, and log access. Base URL is in
  name: Red5 Pro Server API
  slug: red5-pro-server-api
- description: REST/JSON API used by both Red5 Pro clusters and Red5 Cloud for Auth, Admin, Proxy, Streams, Streams Provision, Streams Mixer, and Scheduling NodeGroups. Base URL is instance-specific ({streamManagerH
  name: Stream Manager 2.0 API
  slug: stream-manager-20-api
- description: Publicly hosted llms.txt providing a structured index of Red5 products, use cases, and documentation for AI agents.
  name: Red5 Agent-Native Surface
  slug: red5-agent-native-surface
artifact_total: 51
asyncapis:
- description: 'Red5 Pro''s webhook subsystem calls a customer-supplied REST endpoint when streaming events occur. Events are grouped into six categories — CONNECT, PUBLISH, SUBSCRIBE, WEBSOCKET, MEDIA and USER — and '
  name: Red5 Pro Webhooks
  slug: red5-webhooks-asyncapi
- description: AsyncAPI specification for the Red5 Pro WebRTC streaming event system, covering WebSocket signaling messages exchanged during publish and subscribe sessions. Red5 Pro WebRTC uses WebSocket connections
  name: Red5 Pro WebRTC Streaming Events
  slug: red5-webrtc-streaming-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Red5 Pro Brew Mixer Admin API
  slug: open-red5-admin-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Applications API
  slug: open-red5-applications-api
- collection_type: open
  name: Red5 Pro Brew Mixer API
  slug: open-red5-brew-mixer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin File Restreamer API
  slug: open-red5-file-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Images API
  slug: open-red5-images-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Inputs API
  slug: open-red5-inputs-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Logs API
  slug: open-red5-logs-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Mixers API
  slug: open-red5-mixers-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Provision API
  slug: open-red5-provision-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Proxy API
  slug: open-red5-proxy-api
- collection_type: open
  name: Red5 Pro Restreamer API
  slug: open-red5-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin RTMP Restreamer API
  slug: open-red5-rtmp-restreamer-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Server API
  slug: open-red5-server-api
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Servlet Configuration API
  slug: open-red5-servlet-configuration-api
- collection_type: open
  name: Red5 Pro Stream Manager 2.0 API
  slug: open-red5-stream-manager-2
- collection_type: open
  name: Red5 Pro Brew Mixer Admin Streams API
  slug: open-red5-streams-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/red5-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/red5-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/red5-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/red5-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/red5pro
- group: company
  title: ''
  type: Website
  url: https://www.red5.net/
- group: docs
  title: ''
  type: Documentation
  url: https://www.red5.net/docs/red5-pro/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/red5pro
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Red5
- group: build
  title: ''
  type: SDKs
  url: https://www.red5.net/live-streaming-sdks/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.red5.net/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.red5.net/blog/
- group: operate
  title: ''
  type: Contact
  url: https://www.red5.net/contact/
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/red5-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red5-stream-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/red5-restream-provision-schema.json
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_superseded/red5-server-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-stream-manager-2-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-brew-mixer-api-openapi.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/red5-restreamer-api-openapi.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/red5-webrtc-streaming-asyncapi.yml
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/red5-stream-structure.json
- group: design
  title: ''
  type: SpectralRuleset
  url: rules/red5-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/red5-vocabulary.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/red5-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/red5-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/red5-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/red5-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/red5-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.red5.net/legal/data-processing-addendum/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/red5-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/red5-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.red5.net/
- group: design
  title: ''
  type: Conventions
  url: conventions/red5-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/red5-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.red5.net/docs/red5-pro/resources/release-notes/
- group: design
  title: ''
  type: Components
  url: components/red5-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/red5-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/red5-sandbox.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/red5-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: https://www.red5.net/docs/red5-pro/users-guide/red5-pro-webhooks-overview/
- group: commercial
  title: ''
  type: Plans
  url: plans/red5-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/red5-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/red5-finops.yml
- group: build
  title: ''
  type: Examples
  url: examples/red5-server-api-list-streams-example.json
- group: build
  title: ''
  type: Examples
  url: examples/red5-stream-manager-create-provision-example.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.red5.net/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.red5.net/docs/red5-pro/development/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.red5.net/docs/red5-cloud/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://customer.support.red5.net/servicedesk/customer/portals
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.red5.net/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.red5.net/legal/privacy-policy/
- group: start
  title: ''
  type: SignUp
  url: https://cloud.red5.net/signup
- group: start
  title: ''
  type: Login
  url: https://account.red5.net/login
- group: commercial
  title: ''
  type: ServiceLevelAgreement
  url: https://www.red5.net/legal/service-level-agreement/
created: '2026-03-01'
description: Red5 provides real-time streaming infrastructure for live video and audio delivery at scale. The Red5 Pro platform includes a media server, Stream Manager 2.0 for autoscaling cloud deployments, the Brew Mixer for composite stream production, a Restreamer for pushing live streams to social media and RTMP destinations, and WebRTC and native SDKs for browser and mobile integration. Red5 APIs enable programmatic management of streams, mixers, restreaming, cluster orchestration, and node monitoring. Use cases include live events, sports broadcasting, interactive video, gaming, surveillance, and enterprise communications requiring ultra-low latency streaming.
examples:
- key_count: 2
  name: Red5 Server Api List Streams Example
  slug: red5-server-api-list-streams-example
- key_count: 2
  name: Red5 Stream Manager Create Provision Example
  slug: red5-stream-manager-create-provision-example
finops:
- name: Red5 Finops
  service_category: Streaming Media
  slug: red5-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/red5.png
json_schemas:
- name: Red5 Pro Restream Provision
  property_count: 8
  slug: red5-restream-provision
- name: Red5 Pro Stream
  property_count: 12
  slug: red5-stream
json_structures:
- name: Red5 Stream Structure
  property_count: 0
  slug: red5-stream-structure
jsonld:
- class_count: 0
  name: Red5 Context
  property_count: 9
  slug: red5-context
layout: provider
modified: '2026-09-04'
name: Red5
nav: Providers
network: true
overview: 'Red5 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Pro WebRTC SDK, Admin API, File Restreamer API, and 8 more. Tagged areas include Live Streaming, Media, Real-Time, RTMP, and Streaming.


  The Red5 catalog on APIs.io includes 2 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Red5''s developer surface includes authentication, documentation, pricing, engineering blog, changelog, sandbox, code examples, and 49 more developer resources.'
plans:
- name: Red5 Plans Pricing
  plan_count: 8
  slug: red5-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Red5 Rate Limits
  slug: red5-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Red5 API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: red5-asyncapi-spectral-rules
- effective_rule_count: 6
  extends: []
  name: Red5 API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: red5-jsonschema-spectral-rules
- effective_rule_count: 52
  extends:
  - spectral:oas
  name: Red5 API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 8
  slug: red5-rules
score:
  band: strong
  composite: 66.3
  coverage:
    artifact_dirs: 32
    catalog_earned: 69.5
    catalog_earned_first_party: 12.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.6
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 33.3
    contract_quality: 63.4
    developer_ergonomics: 78.6
    discoverability: 81.5
    governance: 33.3
    operational_transparency: 42.1
  previous_composite: 66.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 13
    mcp: derived
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/red5/refs/heads/main/screenshots/red5-2026-06-20T192724.png
security:
- kind: authentication
  name: Red5 Authentication
  slug: red5-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Red5 Domain Security
  slug: red5-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: red5
tags:
- Live Streaming
- Media
- Real-Time
- RTMP
- Streaming
- Video
- WebRTC
website: https://www.red5.net/
---
