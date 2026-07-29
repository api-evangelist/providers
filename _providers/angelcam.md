---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 50.2
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 53
  human_in_the_loop: 8
  name: Angelcam Agentic Access
  operation_count: 124
  slug: angelcam-agentic-access
  summary_line: 124 operations · 53 acting · 8 human-in-the-loop
api_count: 29
apis:
- description: 'Endpoints for managing your activated services and assigning them to cameras. A service must first be activated (purchased) for your account, then assigned to a specific camera before it takes effect '
  name: AngelCam active-service API
  slug: angelcam-active-service-api
- description: The angelcameras API from AngelCam — 1 operation(s) for angelcameras.
  name: AngelCam angelcameras API
  slug: angelcam-angelcameras-api
- description: Manage [Arrow clients](https://github.com/angelcam/arrow-client) — pair them with your account, inspect exposed services, and send commands. **Pairing:** restart the device (pairing mode is active for
  name: AngelCam arrow-clients API
  slug: angelcam-arrow-clients-api
- description: Endpoints for managing audio messages. Audio messages are pre-recorded audio clips that can be played through [speakers](#tag/speakers). Audio files are uploaded as Base64-encoded content. Supported f
  name: AngelCam audio-message API
  slug: angelcam-audio-message-api
- description: Endpoints for managing broadcasting settings and retrieving broadcasting streams. If a camera doesn't have the Broadcasting service activated, all camera broadcasting endpoints will return HTTP 404. T
  name: AngelCam broadcasting API
  slug: angelcam-broadcasting-api
- description: 'Manage your cameras and access live streams, snapshots, and recordings. Supported codecs: H.264, H.265 (experimental), MJPEG. Live streams are limited to 10 concurrent consumers per camera — use the ['
  name: AngelCam camera API
  slug: angelcam-camera-api
- description: You can share your camera with a guest, this means, you allow guests to view stream from your camera. There is also an option to share also recordings together with live stream. When you adding new gu
  name: AngelCam camera-guest API
  slug: angelcam-camera-guest-api
- description: Using these endpoints you can verify if there are camera streams available on specified network address. Detection is asynchronous. For this reason there is one endpoint for initializing stream detect
  name: AngelCam camera-stream-detection API
  slug: angelcam-camera-stream-detection-api
- description: 'Endpoints for reseller users to manage their clients. A reseller can create two types of client accounts: * **Full account** — the client has full control over their cameras and services. * **Limited '
  name: AngelCam client API
  slug: angelcam-client-api
- description: A clip is a permanent, downloadable excerpt of recorded footage. Unlike a recording stream — which is a temporary playback session — a clip is processed into a file that can be downloaded or shared wi
  name: AngelCam clip API
  slug: angelcam-clip-api
- description: Events represent detections reported by cameras or sensors — typically motion detected by a camera or a trigger from an external sensor. Events are the building blocks for [RTS incidents](#tag/inciden
  name: AngelCam event API
  slug: angelcam-event-api
- description: Endpoints for managing Real Time Security (RTS) incidents. An incident is a security event that has been detected and may require attention. Incidents are created automatically when sensor events or c
  name: AngelCam incidents API
  slug: angelcam-incidents-api
- description: Endpoints for accessing and managing locations. Locations are used to organize cameras into groups. Every camera belongs to exactly one location, and every user has a root location whose ID is availab
  name: AngelCam location API
  slug: angelcam-location-api
- description: The order API from AngelCam — 3 operation(s) for order.
  name: AngelCam order API
  slug: angelcam-order-api
- description: Endpoints for browsing cameras that are publicly accessible. A camera appears here if it has the Broadcasting service active and has been marked as public — either because it uses free public broadcas
  name: AngelCam public-camera API
  slug: angelcam-public-camera-api
- description: Cloud Recording endpoints. Requires the Cloud Recording service to be active on the camera — otherwise all endpoints return 404. A camera can have multiple simultaneous recordings (e.g. continuous + e
  name: AngelCam recording API
  slug: angelcam-recording-api
- description: Endpoints for managing notifications. Base object is message. We create a message when something important happens. For example, when a camera goes offline, when a sensor detects motion, etc. When a m
  name: AngelCam rts_messages API
  slug: angelcam-rts-messages-api
- description: Manage notification methods — email and HTTP webhook. HTTP methods send a signed POST to your URL with a JSON payload on each notification. See the [Webhooks guide](/guides/webhooks/) for payload fiel
  name: AngelCam rts_notification_methods API
  slug: angelcam-rts-notification-methods-api
- description: 'Endpoints for managing notification rules. Notification rule is a rule that defines when and how we should send message to user. For example, we can create rule that says: "When camera goes offline, s'
  name: AngelCam rts_notification_rules API
  slug: angelcam-rts-notification-rules-api
- description: 'Global Real Time Security (RTS) settings for your account. The main setting is `incident_ttl`, which controls how long (in [ISO 8601 duration format](#section/Angelcam-API/Time-and-duration-formats)) '
  name: AngelCam rts_settings API
  slug: angelcam-rts-settings-api
- description: With sensor endpoints you can view, manage and connect sensors to the user account. Sensor can be bind to one particular already connected [camera](#tag/camera) to mark received [events](#tag/event) o
  name: AngelCam sensor API
  slug: angelcam-sensor-api
- description: A catalog of services available for purchase. Use these endpoints to discover service `code` values before activating a service via the [My services](#tag/active-service) endpoints. Services fall into
  name: AngelCam service API
  slug: angelcam-service-api
- description: 'For access to cameras which somebody shared with you. In general everything is same as in my cameras section, see above, there is only one difference. Together with cameras information you get also a '
  name: AngelCam shared-camera API
  slug: angelcam-shared-camera-api
- description: Recording clips on cameras shared with you. Everything works the same as [My recording clips](#tag/clip) — just replace `cameras` with `shared-cameras` in the endpoint URLs.
  name: AngelCam shared-camera-clip API
  slug: angelcam-shared-camera-clip-api
- description: Everything is same as in recording for my own cameras. Just replace `cameras` by `shared-cameras` in every endpoints url.
  name: AngelCam shared-camera-recording API
  slug: angelcam-shared-camera-recording-api
- description: 'A **space** is the organisational unit in Angelcam — it owns all resources: cameras, locations, recordings, services, and billing. Every API request operates within a space context — by default the us'
  name: AngelCam space API
  slug: angelcam-space-api
- description: Manage speakers and trigger audio playback. See the [Speakers guide](/guides/speakers/) for setup instructions, including how to configure an AngelBox as a speaker.
  name: AngelCam speakers API
  slug: angelcam-speakers-api
- description: 'You normally don''t have to know the `streamer_domain` and `stream_id` path parameter, but use the generated endpoint URLs as reported by the `stream_controls` field in a create-stream response. Those '
  name: AngelCam stream-controls API
  slug: angelcam-stream-controls-api
- description: The user API from AngelCam — 1 operation(s) for user.
  name: AngelCam user API
  slug: angelcam-user-api
arazzos:
- description: ''
  name: _Index
  slug: _index
- description: From a camera, list recordings, read a timeline, create a clip, and share it by email.
  name: Angelcam — create and share a clip
  slug: angelcam-create-and-share-clip
- description: List cameras and retrieve the live-stream URLs for one.
  name: Angelcam — watch a live camera
  slug: angelcam-watch-live-camera
artifact_total: 39
asyncapis:
- description: ''
  name: Angelcam Webhooks
  slug: angelcam-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.angelcam.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.angelcam.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.angelcam.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.angelcam.com/guides/key-concepts/
- group: auth
  title: ''
  type: Authentication
  url: authentication/angelcam-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/angelcam-scopes.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/angelcam-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/angelcam-agentic-access.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/angelcam-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/angelcam-webhooks.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/angelcam-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/angelcam-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/angelcam-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.angelcam.com
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/angelcam-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/angelcam-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/angelcam-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/angelcam-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/angelcam-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://help.angelcam.com
- group: company
  title: ''
  type: Blog
  url: https://angelcam.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/angelcam
- group: start
  title: ''
  type: Login
  url: https://my.angelcam.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://angelcam.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://angelcam.com/privacy/
- group: company
  title: ''
  type: Website
  url: https://angelcam.com
created: '2026-07-17'
description: Angelcam is a cloud video-surveillance platform that connects any IP camera to the cloud — via ONVIF and the open-source Arrow connector — for live viewing, cloud recording, clip creation and sharing, two-way audio, sensors, and Remote Technical Surveillance (RTS) event notifications. The Angelcam RESTful API (HTTPS-only JSON, organised around Spaces, secured with OAuth2 or a Personal Access Token) exposes 90+ endpoints across cameras, recordings, clips, events, Arrow clients, notifications, speakers, and services.
image: https://developers.angelcam.com/assets/logo-angelcam.svg
layout: provider
mcp_servers:
- description: ''
  name: angelcam-mcp.yml
  slug: angelcam-mcpyml
modified: '2026-07-17'
name: AngelCam
nav: Providers
network: true
overview: 'AngelCam publishes 29 APIs on the [APIs.io](https://apis.io/) network, including active-service API, angelcameras API, arrow-clients API, and 26 more. Tagged areas include Company, Video Surveillance, Cameras, IP Camera, and Cloud Recording.


  The AngelCam catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  AngelCam''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, and 21 more developer resources.'
random_paper: 54
rate_limits:
- limit_count: 0
  name: Angelcam Rate Limits
  slug: angelcam-rate-limits
scopes:
- name: Angelcam Scopes
  scope_count: 51
  slug: angelcam-scopes
  summary_line: 51 scopes · authorizationCode/password
score:
  band: developing
  composite: 48.8
  delta: -2.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 67.9
    developer_ergonomics: 56.0
    discoverability: 75.9
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/angelcam/refs/heads/main/screenshots/angelcam-2026-07-25T200231.png
security:
- kind: authentication
  name: Angelcam Authentication
  slug: angelcam-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Angelcam Domain Security
  slug: angelcam-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: angelcam
tags:
- Company
- Video Surveillance
- Cameras
- IP Camera
- Cloud Recording
- Video Streaming
- IoT
- ONVIF
- Security
- Webhooks
website: https://angelcam.com
---
