---
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
  schema_version: '0.2'
  score: 4.1
  scored_at: '2026-09-21'
api_count: 4
apis:
- description: LeapC is the native C API of the Ultraleap Hand Tracking Software. A client opens a connection to the locally running tracking service and polls it for tracking frames (hands, palms, digits, bones), d
  name: LeapC Tracking API
  slug: leapc-tracking-api
- description: An implicit Khronos OpenXR API layer, installed with the Hand Tracking Software, that serves XR_EXT_hand_tracking, XR_EXT_hand_joints_motion_range, XR_EXT_hand_tracking_data_source, XR_MSFT_hand_inter
  name: Ultraleap OpenXR API Layer
  slug: openxr-api-layer
- description: An open-source WebSocket server from Ultraleap that restores the LeapJS-compatible surface removed when Leap Motion Orion V4 was replaced by Ultraleap Gemini V5. It streams tracking data over the lega
  name: Ultraleap Tracking WebSocket
  slug: tracking-websocket
- description: 'TouchFree turns Ultraleap hand tracking into touchless cursor and gesture input for kiosks, digital signage and existing 2D user interfaces. The TouchFree Service runs locally and the Tooling for Web '
  name: TouchFree Tooling
  slug: touchfree-tooling
artifact_total: 5
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ultraleap/UltraleapTrackingWebSocket/issues
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/errors/ultraleap-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/ultraleap-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/conventions/ultraleap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ultraleap-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/data-model/ultraleap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ultraleap-data-model.yml
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
  url: https://www.ultraleap.com/legal/enterprise-tracking-licence/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.ultraleap.com/openxr/changelog/index.html
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/changelog/ultraleap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/ultraleap-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/packages/ultraleap-packages.yml
  title: ''
  type: Packages
  url: packages/ultraleap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/packages/ultraleap-packages.yml
  title: ''
  type: SDKs
  url: packages/ultraleap-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/components/ultraleap-components.yml
  title: ''
  type: Components
  url: components/ultraleap-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/conformance/ultraleap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ultraleap-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/conformance/ultraleap-conformance.yml
  title: ''
  type: Compliance
  url: conformance/ultraleap-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/lifecycle/ultraleap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ultraleap-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/llms/ultraleap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ultraleap-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ultraleap/refs/heads/main/security/ultraleap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ultraleap-domain-security.yml
created: '2026-09-18'
description: Ultraleap Limited (Bristol, UK) is the hand-tracking and mid-air haptics company formed in 2019 when Ultrahaptics acquired Leap Motion. It ships the Leap Motion Controller 2 and Stereo IR 170 / 3Di hand-tracking cameras, the Ultraleap Hand Tracking Software (Gemini V5, now Hyperion V6) with its native LeapC C API, first-party Unity and Unreal plugins, an implicit OpenXR API layer implementing XR_EXT_hand_tracking, Python bindings, a LeapJS-compatible tracking WebSocket server, and the TouchFree touchless interaction tooling for web and Unity. Its ultrasonic haptics SDK is supplied on request rather than published. The developer surface is a locally installed SDK and service, not a hosted HTTP API, so there is no OpenAPI or base URL. In 2025 the company announced it is joining ROLI, the music-technology company.
image: https://avatars.githubusercontent.com/u/51484212?v=4
layout: provider
modified: '2026-09-18'
name: Ultraleap
nav: Providers
network: true
overview: 'Ultraleap publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hand Tracking, Computer-Vision, Spatial Computing, and Haptics.


  Ultraleap''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, changelog, and 22 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 29.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 6.7
    developer_ergonomics: 52.4
    discoverability: 72.2
    operational_transparency: 18.4
  previous_composite: 29.7
  provenance:
    conformance: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Ultraleap Domain Security
  slug: ultraleap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: ultraleap
tags:
- Company
- Hand Tracking
- Computer-Vision
- Spatial Computing
- Haptics
- Augmented Reality
- Virtual Reality
- XR
- Gesture Recognition
- OpenXR
- SDK
- Hardware
- Human-Computer Interaction
website: https://www.ultraleap.com/
---
