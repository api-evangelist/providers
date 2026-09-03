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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.1
  scored_at: '2026-09-02'
api_count: 2
apis:
- description: LeapC is the native C API for Ultraleap / Leap Motion hand tracking. A client opens a LEAP_CONNECTION to the locally running Ultraleap Hand Tracking Service and drives a message pump with LeapPollConn
  name: LeapC Tracking API
  slug: leapc-tracking-api
- description: An open-source WebSocket server from Ultraleap that restores the LeapJS-compatible websocket surface removed when Leap Motion Orion V4 was replaced by Ultraleap Gemini V5. It streams tracking data ove
  name: Ultraleap Tracking WebSocket
  slug: tracking-websocket
artifact_total: 3
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ultraleap/UltraleapTrackingWebSocket/issues
- group: auth
  title: ''
  type: DomainSecurity
  url: security/leap-motion-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ultraleap.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.ultraleap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.ultraleap.com/hand-tracking/index.html
- group: docs
  title: ''
  type: APIReference
  url: https://docs.ultraleap.com/api-reference/tracking-api/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.ultraleap.com/hand-tracking/getting-started.html
- group: other
  title: ''
  type: Downloads
  url: https://www.ultraleap.com/downloads/
- group: other
  title: ''
  type: Products
  url: https://www.ultraleap.com/products/
- group: company
  title: ''
  type: Blog
  url: https://docs.ultraleap.com/ultralab/index.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ultraleap
- group: operate
  title: ''
  type: Support
  url: https://www.ultraleap.com/contact/
- group: operate
  title: ''
  type: Community
  url: https://discord.com/invite/3VCndThqxS
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ultraleap.com/legal/ultraleap-ltd-terms-conditions-of-business/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ultraleap.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: License
  url: https://www.ultraleap.com/legal/
- group: auth
  title: ''
  type: Compliance
  url: https://www.ultraleap.com/legal/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ultraleap.com/openxr/changelog/index.html
- group: build
  title: ''
  type: Packages
  url: packages/leap-motion-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/leap-motion-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/leap-motion-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/leap-motion-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/leap-motion-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/leap-motion-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/leap-motion-data-model.yml
- group: design
  title: ''
  type: Components
  url: components/leap-motion-components.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/leap-motion-llms.txt
created: '2026-07-17'
description: 'Leap Motion is the hand-tracking company behind the Leap Motion Controller. It merged with Ultrahaptics in 2019 to form Ultraleap, and the Leap Motion brand now continues as Ultraleap''s hardware line (Leap Motion Controller 2) and as the "Leap" naming across the tracking SDK. The developer surface is not a hosted web API: it is LeapC, a native C API that connects a local client to the Ultraleap Hand Tracking Service and delivers tracked hands, digits, bones, images and device events as polled messages, plus first-party plugins for Unity, Unreal, OpenXR and Python. The original leapmotion.com and developer.leapmotion.com domains no longer resolve; docs.ultraleap.com and github.com/ultraleap are the live developer surfaces.'
image: https://avatars.githubusercontent.com/u/51484212?v=4
layout: provider
modified: '2026-07-20'
name: Leap Motion
nav: Providers
network: true
overview: 'Leap Motion publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hand Tracking, Computer-Vision, Spatial Computing, and Augmented Reality.


  Leap Motion''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, and 21 more developer resources.'
random_paper: 12
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 12
    catalog_gap: 83.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 4.5
    contract_quality: 6.7
    developer_ergonomics: 52.4
    discoverability: 66.7
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 27.5
  provenance:
    conformance: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/leap-motion/refs/heads/main/screenshots/leap-motion-2026-07-25T224749.png
security:
- kind: domain-security
  name: Leap Motion Domain Security
  slug: leap-motion-domain-security
  summary_line: TLSv1.3 · DMARC
slug: leap-motion
tags:
- Company
- Hand Tracking
- Computer-Vision
- Spatial Computing
- Augmented Reality
- Virtual Reality
- XR
- Gesture Recognition
- SDK
- Hardware
- Human-Computer Interaction
- OpenXR
website: https://www.ultraleap.com/
---
