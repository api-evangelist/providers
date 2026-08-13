---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.6
  scored_at: '2026-08-12'
api_count: 10
apis:
- description: Browser-side JavaScript API (also called the External API) that embeds a Jitsi Meet conference into any web page through an iframe. Exposes the JitsiMeetExternalAPI constructor with commands (executeC
  name: Jitsi Meet IFrame (External) API
  slug: jitsi-meet-iframe-api
- description: 'Low-level JavaScript library for building entirely custom video conferencing experiences on top of the Jitsi infrastructure. Exposes JitsiConnection, JitsiConference, JitsiTrack, and the XMPP/Colibri '
  name: lib-jitsi-meet (Low-Level JavaScript API)
  slug: lib-jitsi-meet-api
- description: Administrative HTTP API exposed by Jitsi Videobridge for operators to read bridge state, list active conferences, inspect endpoints, gracefully drain a bridge, and scrape Prometheus metrics. Typically
  name: Jitsi Videobridge REST API
  slug: jitsi-videobridge-rest-api
- description: Operations REST API exposed by Jicofo (Jitsi Conference Focus) for inspecting in-progress conferences, listing the bridge selection state, and triggering graceful shutdowns. Used by operators and orch
  name: Jicofo REST API
  slug: jicofo-rest-api
- description: HTTP control API exposed by Jibri (Jitsi BRoadcasting Infrastructure) for starting and stopping recording or live-streaming sessions, reporting health, and surfacing the busy/idle state of a Jibri ins
  name: Jibri REST API
  slug: jibri-rest-api
- description: Managed Jitsi as a Service offering from 8x8 that fronts the open-source Jitsi stack with a JWT-secured REST surface for issuing meeting tokens, managing rooms, fetching recordings, controlling partic
  name: JaaS (Jitsi as a Service) REST API
  slug: jaas-rest-api
- description: JaaS-flavoured IFrame API that loads external_api.js from 8x8-vc.com (the managed Jitsi domain) and authenticates each meeting with a signed JWT issued for the tenant. Provides the same JitsiMeetExter
  name: JaaS IFrame API
  slug: jaas-iframe-api
- description: 'Native mobile SDKs that embed the full Jitsi Meet experience inside Android and iOS applications, plus a React Native module published from the jitsi-meet repository. Each SDK exposes a meeting view, '
  name: Jitsi Meet Mobile SDK (Android, iOS, React Native)
  slug: jitsi-meet-mobile-sdk
- description: Electron toolkit for embedding Jitsi Meet inside a desktop application, including remote control, always-on-top thumbnails, screen sharing, and native window integration. Powers the official Jitsi Mee
  name: Jitsi Meet Electron SDK
  slug: jitsi-meet-electron-sdk
- description: React component wrapper around the Jitsi Meet IFrame API that provides idiomatic <JitsiMeeting /> and <JaaSMeeting /> components, type definitions, hooks for events, and ref-based command dispatch — u
  name: Jitsi Meet React SDK
  slug: jitsi-meet-react-sdk
artifact_total: 41
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/jitsi/jitsi-meet/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/jitsi/jitsi-meet/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/jitsi/jitsi-meet/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/jitsi/jitsi-meet/blob/master/CONTRIBUTING.md
- group: auth
  title: ''
  type: DomainSecurity
  url: security/jitsi-org-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://jitsi.org
- group: company
  title: ''
  type: Website
  url: https://jitsi.org
- group: start
  title: ''
  type: Sandbox
  url: https://meet.jit.si
- group: docs
  title: ''
  type: Documentation
  url: https://jitsi.github.io/handbook/
- group: start
  title: ''
  type: GettingStarted
  url: https://jitsi.github.io/handbook/docs/intro
- group: docs
  title: ''
  type: Documentation
  url: https://jitsi.org/projects/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.8x8.com/jaas/docs
- group: start
  title: ''
  type: Signup
  url: https://jaas.8x8.vc/
- group: commercial
  title: ''
  type: Pricing
  url: https://jaas.8x8.vc/#/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jitsi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jitsi-meet
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jitsi-videobridge
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/lib-jitsi-meet
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jicofo
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jigasi
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jibri
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/docker-jitsi-meet
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/handbook
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jitsi-meet-electron
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jitsi/jitsi-meet-sdk-samples
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/lib-jitsi-meet
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@jitsi/react-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/jitsi/jitsi-meet
- group: build
  title: ''
  type: Tools
  url: https://github.com/jitsi/docker-jitsi-meet
- group: build
  title: ''
  type: Tools
  url: https://github.com/jitsi/jitsi-meet-electron
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/jitsi/jitsi-meet-sdk-samples
- group: operate
  title: ''
  type: Support
  url: https://community.jitsi.org/
- group: operate
  title: ''
  type: Forums
  url: https://community.jitsi.org/
- group: company
  title: ''
  type: Blog
  url: https://jitsi.org/blog/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/jitsi/jitsi-meet-release-notes
- group: commercial
  title: ''
  type: License
  url: https://github.com/jitsi/jitsi-meet/blob/master/LICENSE
- group: auth
  title: ''
  type: Authentication
  url: https://developer.8x8.com/jaas/docs/jwt-overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://8x8.com/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.8x8.com/terms-and-conditions/privacy-policy
- group: other
  title: ''
  type: Company
  url: https://www.8x8.com
created: '2026-05-25'
description: Jitsi is a collection of free and open-source projects for secure, simple, and scalable real-time video conferencing, maintained by 8x8. The Jitsi stack combines a browser-based meeting application (Jitsi Meet), a WebRTC selective forwarding unit (Jitsi Videobridge), conference focus (Jicofo), SIP gateway (Jigasi), and broadcasting infrastructure (Jibri), along with web, mobile, desktop, and low-level SDKs for embedding meetings into other applications. Jitsi is also available as a fully managed offering — Jitsi as a Service (JaaS) — that exposes the same conferencing surface through a JWT-secured API and the Jitsi IFrame/External API.
features:
- description: WebRTC-compatible selective forwarding unit able to scale to hundreds of concurrent conferences per server.
  name: Open-source WebRTC SFU (Jitsi Videobridge)
- description: Full-featured meeting client (chat, screen share, breakout rooms, raise hand, polls, e2ee, virtual backgrounds, tile view) running entirely in the browser.
  name: Browser-first Jitsi Meet client
- description: One-line embed of a fully functioning Jitsi meeting into any web page, with a rich JS surface for commands, events, and functions.
  name: IFrame / External API
- description: Build a completely custom UI on top of Jitsi's signaling and media plumbing.
  name: lib-jitsi-meet low-level API
- description: Native Android, iOS, and React Native SDKs derived from the same jitsi-meet codebase, plus a community Flutter plugin.
  name: Mobile SDKs
- description: Cross-platform Electron application and reusable Electron SDK.
  name: Desktop client
- description: Jibri provides server-side recording and RTMP streaming to YouTube/Twitch from any Jitsi meeting.
  name: Recording and live streaming
- description: Jigasi bridges Jitsi meetings to SIP/PSTN endpoints and produces transcripts via pluggable speech-to-text engines.
  name: SIP gateway and transcription
- description: Full stack deployable via Debian packages, Docker Compose (docker-jitsi-meet), Kubernetes, or cloud images.
  name: Self-hostable
- description: Hosted Jitsi from 8x8 with JWT-secured tenants, recording, streaming, dial-in, and a developer console at jaas.8x8.vc.
  name: JaaS managed service
- description: Insertable-stream-based E2EE for supported browsers and SDK builds.
  name: End-to-end encryption
- description: Open-source AI core services for Jitsi (transcription, summarization) shipped via the jitsi/skynet project and the opus-transcriber-proxy bridge to OpenAI.
  name: AI features (Skynet)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/jitsi-org.png
integrations:
- description: Element uses Jitsi as the default group-call backend in the Matrix ecosystem.
  name: Matrix / Element
- description: First-class Jitsi integrations for team chat and collaboration platforms.
  name: Rocket.Chat, Mattermost, Nextcloud
- description: Many education stacks embed Jitsi for synchronous classes.
  name: Moodle, BigBlueButton-adjacent LMS deployments
- description: JaaS is part of 8x8's experience-communications platform alongside voice, contact center, and SMS APIs.
  name: 8x8 XCaaS
- description: Bridges to any SIP-capable provider for dial-in / dial-out.
  name: SIP / PSTN providers via Jigasi
- description: Live-streaming targets supported by Jibri.
  name: YouTube Live / Twitch / custom RTMP
- description: First-class Prometheus metrics exposed by Videobridge and Jicofo.
  name: Prometheus + Grafana
- description: Official docker-jitsi-meet images and community Helm charts.
  name: Docker / Kubernetes
layout: provider
modified: '2026-05-25'
name: Jitsi
nav: Providers
network: true
overview: 'Jitsi publishes 10 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Video Conferencing, WebRTC, Real-Time Communication, Open Source, and Voice.


  Jitsi''s developer surface includes developer portal, sandbox, documentation, getting-started guide, signup flow, pricing, tooling, and 33 more developer resources.'
random_paper: 80
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 67.4
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.0
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/jitsi-org/refs/heads/main/screenshots/jitsi-org-2026-06-20T183736.png
security:
- kind: domain-security
  name: Jitsi Org Domain Security
  slug: jitsi-org-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jitsi-org
solutions:
- description: meet.jit.si — anonymous, no-account video meetings on 8x8-operated infrastructure.
  name: Jitsi Meet (free, hosted)
- description: Full open-source stack deployable by anyone under Apache 2.0.
  name: Self-hosted Jitsi
- description: Free JaaS tier for low-volume embedded usage with a generous monthly minute allowance.
  name: JaaS Free
- description: Metered pricing tiers and custom enterprise contracts for production embedded video.
  name: JaaS Paid / Custom
tags:
- Video Conferencing
- WebRTC
- Real-Time Communication
- Open Source
- Voice
- Video
- SIP
- Streaming
- Recording
- Self-Hosted
use_cases:
- description: Drop Jitsi Meet into a product (HR, healthcare, education, support) via the IFrame API or React SDK.
  name: Embedded video meetings in SaaS apps
- description: Self-host the full stack on infrastructure you control to meet data-residency or regulatory requirements.
  name: Privacy-focused / sovereign video calling
- description: HIPAA/FERPA-aligned deployments using self-hosted Jitsi or JaaS with recording disabled.
  name: Telehealth and online education
- description: Use Jibri for server-side recording and one-click RTMP streaming to YouTube, Twitch, or a custom ingest.
  name: Webinars and live streaming
- description: Use Jigasi to dial regular phones into Jitsi meetings or bring SIP room systems into a Jitsi conference.
  name: SIP/PSTN bridging
- description: Build a bespoke conferencing UX on top of lib-jitsi-meet without operating XMPP or WebRTC primitives yourself.
  name: Custom video apps
website: https://jitsi.org
---
