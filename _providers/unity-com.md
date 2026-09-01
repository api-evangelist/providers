---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
api_count: 19
apis:
- description: Player Authentication for Unity Gaming Services. Anonymous, social (Apple/Google/Facebook/Steam/Oculus/PlayStation/Xbox/Nintendo), username/password, and custom-ID sign-in flows that mint Unity player
  name: Unity Authentication API
  slug: unity-authentication-api
- description: Per-player and per-game-session key/value data persistence with versioning, conflict resolution, and server-authoritative write protection. Includes a Player Data API for player-scoped state and an Ad
  name: Unity Cloud Save API
  slug: unity-cloud-save-api
- description: Server-authoritative JavaScript scripts and C# modules executed in Unity's managed runtime. Bill is per-compute-second ($0.072/compute-hour). Cloud Code exposes both a runtime invocation API (called f
  name: Unity Cloud Code API
  slug: unity-cloud-code-api
- description: Server-authoritative virtual economy primitives — currencies, inventory items, virtual purchases, and real-money purchases — with player balances, inventories, and transaction history. Used to back li
  name: Unity Economy API
  slug: unity-economy-api
- description: Server-authoritative ranked leaderboards with bucketed, partitioned, and tiered scoring strategies. Supports score reset schedules, paginated rankings around a player, and bulk archive/restore.
  name: Unity Leaderboards API
  slug: unity-leaderboards-api
- description: Dynamic configuration delivery — feature flags, balance values, game settings — segmented by audiences and overridden by campaigns. Configs are versioned and can be staged across environments.
  name: Unity Remote Config API
  slug: unity-remote-config-api
- description: NAT-traversal relay service that allows peer-to-peer multiplayer sessions without exposing player IPs. Allocates host/join codes, encrypted DTLS connections, and short-lived relay endpoints across glo
  name: Unity Relay API
  slug: unity-relay-api
- description: 'Player-meeting service for creating, listing, joining, and managing lobbies with custom metadata, host migration, and integration with Relay or Multiplay. Supports private codes, region affinity, and '
  name: Unity Lobby API
  slug: unity-lobby-api
- description: Rule-based matchmaker that places players into game sessions using skill, latency, party, and custom attributes. Integrates with Multiplay or Relay-backed sessions and exposes Admin APIs for queue, po
  name: Unity Matchmaker API
  slug: unity-matchmaker-api
- description: Global dedicated game-server hosting (Multiplay). APIs cover fleets, builds, build configurations, machines, allocations, and queues. Note Unity ended direct operations of Multiplay on 31 March 2026 a
  name: Unity Multiplay (Game Server Hosting) API
  slug: unity-multiplay-api
- description: Vivox in-game voice and text chat with moderation, channel management, and recordings. The Moderation REST API handles user bans, channel mutes, transcript retrieval, and compliance evidence.
  name: Unity Vivox Voice and Text Chat API
  slug: unity-vivox-api
- description: Player social graph — friends, blocks, invitations, and presence — with cross-platform identifiers. Integrates with Player Names and Authentication for display and identity resolution.
  name: Unity Friends API
  slug: unity-friends-api
- description: Game telemetry and live-ops analytics. Client API ingests standard and custom events; reporting surfaces funnels, retention, monetization, and segmentation. Compatible with GDPR/COPPA consent flows.
  name: Unity Analytics API
  slug: unity-analytics-api
- description: Event-driven automation that fires Cloud Code in response to other UGS service events (Cloud Save writes, Economy purchases, Authentication signups, etc.). The Admin API manages triggers, filters, and
  name: Unity Triggers API
  slug: unity-triggers-api
- description: Scheduled execution of Cloud Code scripts/modules. Manage one-shot and recurring jobs with timezone awareness, retries, and execution history.
  name: Unity Scheduler API
  slug: unity-scheduler-api
- description: Versioned asset/bundle distribution. Admin (management) API for buckets, badges, releases, and entries; client API resolves the active release for a player environment and serves signed asset URLs.
  name: Unity Content Delivery API
  slug: unity-content-delivery-api
- description: Programmatic management of Unity's ad-monetization surface (formerly ironSource / LevelPlay). Includes Monetize (publisher placements, mediation), Advertise (user-acquisition campaigns), and Statistic
  name: Unity Monetize and Ads API
  slug: unity-monetize-api
- description: Unity Cloud Asset Manager — a digital asset management API for 3D, image, audio, and animation assets used across game and Unity Industry workflows. Supports collections, versions, transformations, an
  name: Unity Asset Manager API
  slug: unity-assets-manager-api
- description: Administrative control plane for Unity organizations, projects, environments, and resource policies. Includes SCIM 2.0 for SSO/identity provisioning, Access for IAM policies, Unity Core for org/projec
  name: Unity Admin and Identity (SCIM, Access, Core) API
  slug: unity-admin-and-iam-api
artifact_total: 50
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/unity-com-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/unity-com-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/unity-com-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://unity.com
- group: start
  title: ''
  type: Portal
  url: https://cloud.unity.com
- group: start
  title: ''
  type: Portal
  url: https://dashboard.unity.com
- group: docs
  title: ''
  type: Documentation
  url: https://unity.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://unity.com/products/unity-engine
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity3d.com/Manual/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity3d.com/ScriptReference/index.html
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/ugs/en-us/manual
- group: docs
  title: ''
  type: Documentation
  url: https://services.docs.unity.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/cloud
- group: learn
  title: ''
  type: Training
  url: https://learn.unity.com
- group: operate
  title: ''
  type: Forums
  url: https://discussions.unity.com
- group: operate
  title: ''
  type: Support
  url: https://support.unity.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.unity.com
- group: operate
  title: ''
  type: ChangeLog
  url: https://unity.com/releases
- group: commercial
  title: ''
  type: TermsOfService
  url: https://unity.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://unity.com/legal/privacy-policy
- group: auth
  title: ''
  type: TrustCenter
  url: https://unity.com/security
- group: start
  title: ''
  type: Signup
  url: https://id.unity.com
- group: start
  title: ''
  type: Signup
  url: https://dashboard.unity.com
- group: company
  title: ''
  type: Blog
  url: https://unity.com/blog
- group: company
  title: ''
  type: Blog
  url: https://blog.unity.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Unity-Technologies
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Unity-Technologies/ml-agents
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Unity-Technologies/com.unity.netcode.gameobjects
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Unity-Technologies/EntityComponentSystemSamples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Unity-Technologies/InputSystem
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Unity-Technologies/arfoundation-samples
- group: build
  title: ''
  type: SDKs
  url: https://github.com/Unity-Technologies/UnityCsReference
- group: build
  title: ''
  type: CodeExamples
  url: https://github.com/Unity-Technologies/com.unity.multiplayer.samples.coop
- group: build
  title: ''
  type: CLI
  url: https://docs.unity.com/ugs-overview/manual/ugs-cli/install
- group: start
  title: ''
  type: Portal
  url: https://unity.com/products/gaming-services
- group: commercial
  title: ''
  type: Pricing
  url: https://unity.com/products/gaming-services/pricing
- group: commercial
  title: ''
  type: Pricing
  url: https://unity.com/products/pricing-updates
- group: commercial
  title: ''
  type: Plans
  url: https://unity.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/ugs/en-us/manual/authentication/manual/rest-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/ugs/en-us/manual/cloud-save/manual/tutorials/rest-api
- group: docs
  title: ''
  type: Documentation
  url: https://docs.unity.com/ugs/en-us/manual/cloud-code/manual/modules/how-to-guides/write-modules/rest-api
- group: commercial
  title: ''
  type: Plans
  url: plans/unity-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/unity-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/unity-finops.yml
created: '2026-05-25T00:00:00.000Z'
description: Unity is a real-time 3D content creation platform — the Unity engine powers cross-platform games, simulations, XR experiences, and digital twins, while Unity Gaming Services (UGS) and Unity Cloud provide a production backend for live games and 3D pipelines. UGS exposes a coherent set of 30+ REST APIs at services.api.unity.com covering authentication, cloud save, cloud code, economy, leaderboards, remote config, relay, lobby, matchmaker, game-server hosting (Multiplay), voice/text chat (Vivox), friends, analytics, triggers, scheduler, content delivery, monetization/LevelPlay, asset management, and organization administration. Unity also ships open-source frameworks including ML-Agents, Netcode for GameObjects, and the Input System, and hosts the canonical Unity C# reference source on GitHub.
features:
- Unity Engine — cross-platform real-time 3D engine for games, simulations, XR, automotive, and industrial digital twins
- Unity 6 (current) and 6.3 LTS — latest LTS release line with HDRP, URP, DOTS/ECS, Burst, and Job System
- C# scripting with hot-reload, the Unity Scripting API, and full source available via UnityCsReference
- Deployments to 25+ platforms — Windows, macOS, Linux, iOS, Android, WebGL, PlayStation, Xbox, Nintendo Switch, Meta Quest, Apple Vision Pro, HoloLens, and embedded targets
- Unity Gaming Services (UGS) — production-grade backend for live games covering identity, persistence, economy, multiplayer, voice, content delivery, analytics, automation, and monetization
- 30+ Unity Services REST APIs documented at services.docs.unity.com with consistent /service/version/ paths and OAuth2 bearer auth (Authentication, Cloud Save, Cloud Code, Economy, Leaderboards, Remote Config, Relay, Lobby, Matchmaker, Multiplay, Vivox, Friends, Analytics, Triggers, Scheduler, Content Delivery, Asset Manager, Monetize/Advertise, SCIM, Access, Unity Core, Releases, Observability, Collaboration, Annotations, Presence, QoS, Distributed Authority, Session Observability, Workflow Engine, Storage, App Linking, Automation, Data Streaming)
- Cloud Code — server-authoritative JavaScript scripts and C# modules at $0.072/compute-hour
- Multiplay (Game Server Hosting) — global dedicated server fleets, transitioning to Rocket Science Group as of March 31 2026
- Vivox — embedded voice and text chat with built-in moderation
- LevelPlay (formerly ironSource) — mediation, user acquisition, and statistics APIs for monetized games
- Unity Cloud — Asset Manager, Version Control (Plastic SCM), Build Automation, Collaboration, Annotations, and Workflow Engine for asset, source-control, and DevOps pipelines
- Unity Industry — Pixyz, CAD ingest, AR/VR enablement, and digital-twin tooling for non-game verticals
- ML-Agents — open-source deep-reinforcement-learning toolkit for training AI agents in Unity environments
- Netcode for GameObjects, Netcode for Entities, Distributed Authority, and Relay/Multiplay for multiplayer architectures from peer-to-peer to authoritative dedicated servers
- AR Foundation for cross-platform AR (ARKit, ARCore, Magic Leap, HoloLens, Vision Pro)
- Render pipelines — Built-in, Universal (URP), High Definition (HDRP) — with Shader Graph and Visual Effect Graph
- DOTS / Entity Component System — data-oriented runtime with Burst compiler and the Jobs System for high-perf simulations and large worlds
- Addressables and Cloud Content Delivery for live asset updates without app re-submission
- Unity Version Control (UVCS / Plastic SCM) with free 25GB tier from Q1 2026 and seat-free public-cloud hosting
- Unity Pro and Enterprise plans on 6.3 LTS no longer include Havok Physics; Personal remains free under $200K annual revenue or funding
- 2026 pricing: Pro $210/seat/mo or $2,310/seat/yr (5% increase from 2025); Enterprise custom; Industry custom
- 100+ official C#/.NET packages distributed via Unity Package Manager (UPM)
- Postman, OpenAPI-style REST docs, and the UGS CLI as primary integration surfaces for the backend services
- Unity Authentication tokens (player JWTs) are the universal bearer for all client-facing UGS APIs
finops:
- name: Unity Finops
  service_category: Developer Tools and Gaming Backend
  slug: unity-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/unity-com.png
jsonld:
- class_count: 11
  name: Unity Com Context
  property_count: 53
  slug: unity-com-context
layout: provider
modified: '2026-05-25'
name: Unity
nav: Providers
network: true
overview: 'Unity publishes 19 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Real-Time 3D, Game Engine, Gaming, Multiplayer, and Cloud.


  The Unity catalog on APIs.io includes 1 JSON-LD context.


  Unity''s developer surface includes developer portal, documentation, training material, support, changelog, signup flow, engineering blog, and 38 more developer resources.'
plans:
- name: Unity Plans Pricing
  plan_count: 8
  slug: unity-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Unity Rate Limits
  slug: unity-rate-limits
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 8
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 0.0
    contract_quality: 21.3
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 45.0
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/unity-com/refs/heads/main/screenshots/unity-com-2026-06-20T200110.png
security:
- kind: domain-security
  name: Unity Com Domain Security
  slug: unity-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Unity Com Vulnerability Disclosure
  slug: unity-com-vulnerability-disclosure
  summary_line: Bugcrowd
- kind: trust-center
  name: Unity Com Trust Center
  slug: unity-com-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: unity-com
tags:
- Real-Time 3D
- Game Engine
- Gaming
- Multiplayer
- Cloud
- Live Operations
- Digital Twins
- XR
- ML-Agents
- Asset Pipeline
website: https://unity.com
---
