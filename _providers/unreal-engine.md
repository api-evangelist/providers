---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 6
apis:
- description: The Unreal Engine C++ API is the primary programmatic surface of the engine. It is shipped as engine source on GitHub (under the Unreal Engine EULA) and documented as a per-module class reference cove
  name: Unreal Engine C++ API
  slug: unreal-engine-cpp-api
- description: Blueprints are Unreal Engine's visual scripting system. Blueprint nodes wrap the underlying C++ API, letting designers and programmers build gameplay, UI, and tooling logic without writing C++. The Bl
  name: Unreal Blueprint Visual Scripting
  slug: blueprint-visual-scripting
- description: The Online Subsystem is Unreal's abstraction over platform online backends (Steam, PlayStation, Xbox Live, Nintendo, EOS, Google Play, Apple GameCenter, Discord). It exposes a consistent C++ interface
  name: Unreal Online Subsystem (OSS / OSSv2)
  slug: online-subsystem
- description: Pixel Streaming streams an Unreal Engine application running on a server to remote browser clients over WebRTC. The framework includes a Pixel Streaming plugin in the engine, a signalling and matchmak
  name: Unreal Pixel Streaming
  slug: pixel-streaming
- description: The Render Hardware Interface is Unreal's abstraction over graphics APIs (Direct3D 11/12, Vulkan, Metal, OpenGL ES). Engine and plugin developers write rendering code against the RHI rather than direc
  name: Unreal Render Hardware Interface (RHI)
  slug: render-hardware-interface
- description: Unreal Engine has a first-class plugin architecture and a content and code marketplace. The historical Unreal Engine Marketplace was consolidated into Fab, Epic's unified content marketplace for Unrea
  name: Unreal Plugins and Fab Marketplace
  slug: unreal-plugins-and-fab
artifact_total: 11
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unreal-engine-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unreal-engine-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.unrealengine.com
- group: docs
  title: ''
  type: Documentation
  url: https://dev.epicgames.com/documentation/en-us/unreal-engine
- group: operate
  title: ''
  type: Community
  url: https://dev.epicgames.com/community/unreal-engine
- group: learn
  title: ''
  type: Learning
  url: https://dev.epicgames.com/community/unreal-engine/learning
- group: operate
  title: ''
  type: Forums
  url: https://forums.unrealengine.com
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/EpicGames/UnrealEngine
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EpicGamesExt
- group: other
  title: ''
  type: Marketplace
  url: https://www.fab.com
- group: docs
  title: ''
  type: Guidelines
  url: https://www.unrealengine.com/marketplace-guidelines
- group: commercial
  title: ''
  type: License
  url: https://www.unrealengine.com/eula
- group: company
  title: ''
  type: Blog
  url: https://www.unrealengine.com/blog
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://www.unrealengine.com/release-notes
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.unrealengine.com
- group: operate
  title: ''
  type: Support
  url: https://www.unrealengine.com/support
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@UnrealEngine
- group: other
  title: ''
  type: X
  url: https://x.com/UnrealEngine
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/UnrealEngine
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/unreal-engine
created: '2024-01-01'
description: Unreal Engine is Epic Games' real-time 3D engine for games, film, broadcast, architecture, simulation, automotive, and live events. The engine is shipped as a downloadable editor, source on GitHub (under the Unreal Engine EULA), and a deep C++ and Blueprint API surface rather than a public REST API. The developer-facing surface includes the Unreal C++ API reference, the Blueprint visual scripting API, the Online Subsystem (OSS) abstraction over platform backends, the Pixel Streaming framework for streaming Unreal apps over WebRTC, the Render Hardware Interface (RHI), the Slate UI framework, and a plugin and Marketplace ecosystem (now Fab). Programmatic backend integration for Unreal-built games is typically delivered via Epic Online Services (EOS), profiled separately. This profile documents Unreal Engine as an SDK and tooling surface rather than as a REST API.
finops:
- name: Unreal Engine Finops
  service_category: API
  slug: unreal-engine-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unreal-engine.png
layout: provider
modified: '2026-05-23'
name: Unreal Engine
nav: Providers
network: true
overview: 'Unreal Engine publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include 3D, Blueprints, C++, Game Development, and Game Engine.


  Unreal Engine''s developer surface includes documentation, engineering blog, release notes, support, YouTube channel, and 15 more developer resources.'
plans:
- name: Unreal Engine Plans Pricing
  plan_count: 1
  slug: unreal-engine-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Unreal Engine Rate Limits
  slug: unreal-engine-rate-limits
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 59.0
    catalog_earned_first_party: 0.0
    catalog_gap: 56.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 24.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
security:
- kind: domain-security
  name: Unreal Engine Domain Security
  slug: unreal-engine-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unreal Engine Vulnerability Disclosure
  slug: unreal-engine-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: unreal-engine
tags:
- 3D
- Blueprints
- C++
- Game Development
- Game Engine
- Pixel Streaming
- Plugin
- Real-Time
- Rendering
- RHI
- SDK
- Unreal Engine
- WebRTC
website: https://www.unrealengine.com
---
