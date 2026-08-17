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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/spline-design-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/spline-design-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spline-design-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spline.design
- group: docs
  title: ''
  type: Documentation
  url: https://docs.spline.design
- group: other
  title: ''
  type: Application
  url: https://app.spline.design
- group: commercial
  title: ''
  type: Pricing
  url: https://spline.design/pricing
- group: company
  title: ''
  type: Blog
  url: https://blog.spline.design
- group: operate
  title: ''
  type: Community
  url: https://community.spline.design
- group: learn
  title: ''
  type: Academy
  url: https://academy.spline.design
- group: other
  title: ''
  type: Hana
  url: https://spline.design/hana
- group: other
  title: ''
  type: AI
  url: https://spline.design/ai
- group: design
  title: ''
  type: Webhooks
  url: https://docs.spline.design/interaction-states-events-and-actions/webhooks
- group: other
  title: ''
  type: RealTimeAPI
  url: https://docs.spline.design/interaction-states-events-and-actions/real-time-api
- group: build
  title: ''
  type: CodeAPIWeb
  url: https://docs.spline.design/exporting-your-scene/web/code-api-for-web
- group: build
  title: ''
  type: CodeAPISwiftUI
  url: https://docs.spline.design/exporting-your-scene/apple-platform/code-api-for-swift-ui
- group: build
  title: ''
  type: CodeAPIKotlin
  url: https://docs.spline.design/exporting-your-scene/android/code-api-for-kotlin
- group: build
  title: ''
  type: GitHub
  url: https://github.com/splinetool
- group: build
  title: ''
  type: ReactSDK
  url: https://github.com/splinetool/react-spline
- group: build
  title: ''
  type: R3FSDK
  url: https://github.com/splinetool/r3f-spline
- group: other
  title: ''
  type: iOSRuntime
  url: https://github.com/splinetool/spline-ios
- group: build
  title: ''
  type: NPMRuntime
  url: https://www.npmjs.com/package/@splinetool/runtime
- group: company
  title: ''
  type: Careers
  url: https://www.ycombinator.com/companies/spline/jobs
- group: operate
  title: ''
  type: Contact
  url: mailto:help@spline.design
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/splinetool
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@splinetool
created: '2026-05-25'
description: Spline is a web-based, real-time collaborative 3D design platform used to create interactive 3D scenes, animations, and product experiences for the web, iOS, and Android. The Spline editor runs in the browser and supports multi-user collaboration with comments, link sharing, and team workspaces. Designers build scenes using primitives and modeling tools, a layer-based material system, states, events, timeline animation, game controls, physics, and particles. Scenes can be exported as GLTF/GLB, USDZ, STL, video, image sequences, or as code for the web, SwiftUI, and Kotlin. Spline's developer surface centers on runtime libraries — `@splinetool/runtime`, the `@splinetool/react-spline` React component, the `r3f-spline` hook for react-three-fiber, and `spline-ios` for Apple platforms — plus an embeddable Spline Viewer web component. Inside scenes, Spline exposes a Real-time API for dynamic data binding and webhooks for event-driven integrations. The company also ships Hana, a web-based
  collaborative UI design tool with infinite canvas, vector networks, visual effects, and motion design. Spline's revenue model is SaaS subscription with Free, Starter ($12/mo annual), Professional ($20/mo annual), and Enterprise tiers, plus a Spline AI add-on ($5/seat/month, 2000 AI credits) for prompt-driven 3D generation. There is no publicly documented Spline REST/management API or OpenAPI specification at this time; programmatic surfaces are limited to the runtime SDKs, the Real-time API, and webhooks exposed from within a scene.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spline-design.png
layout: provider
modified: '2026-05-25'
name: Spline
nav: Providers
network: true
overview: 'Spline is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include 3D Design, 3D Modeling, Collaborative Design, Interactive 3D, and Web Embed.


  Spline''s developer surface includes documentation, pricing, engineering blog, academy / training, GitHub presence, YouTube channel, and 20 more developer resources.'
random_paper: 138
score:
  band: emerging
  composite: 13.4
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 13.4
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/spline-design/refs/heads/main/screenshots/spline-design-2026-06-20T194406.png
security:
- kind: domain-security
  name: Spline Design Domain Security
  slug: spline-design-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Spline Design Vulnerability Disclosure
  slug: spline-design-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Spline Design Trust Center
  slug: spline-design-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: spline-design
tags:
- 3D Design
- 3D Modeling
- Collaborative Design
- Interactive 3D
- Web Embed
- WebGL
- Animation
- Motion Design
- Materials
- Physics
- Particles
- SwiftUI
- Kotlin
- React
- React Three Fiber
- GLTF
- USDZ
- Webhooks
- Real-time API
- AI 3D Generation
- Design Tools
website: https://spline.design
---
