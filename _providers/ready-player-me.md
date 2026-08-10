---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Ready Player Me Agentic Access
  operation_count: 23
  slug: ready-player-me-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 3
apis:
- description: Create, retrieve, update, and delete Ready Player Me cross-platform avatars. Includes template-based creation, asset equipping, draft management, color palette discovery, and binary glTF (.glb) plus 2
  name: Ready Player Me Avatars API
  slug: ready-player-me-avatars-api
- description: Discover and retrieve avatar wearable assets — hair, outfits, headwear, glasses, facewear, footwear, beards, costumes, and custom assets — scoped to an application and optionally filtered to those vie
  name: Ready Player Me Assets API
  slug: ready-player-me-assets-api
- description: Anonymous user creation, email-code login, token refresh, and avatar access tokens used by the Ready Player Me Avatar Creator and SDKs. Authentication runs through each application's per-studio subdom
  name: Ready Player Me Auth API
  slug: ready-player-me-auth-api
artifact_total: 19
collections:
- collection_type: open
  name: Ready Player Me Assets API
  slug: open-ready-player-me-assets-api
- collection_type: open
  name: Ready Player Me Auth API
  slug: open-ready-player-me-auth-api
- collection_type: open
  name: Ready Player Me Avatars API
  slug: open-ready-player-me-avatars-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ready-player-me-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ready-player-me-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://readyplayer.me/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readyplayer.me/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readyplayer.me/ready-player-me/api-reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.readyplayer.me/ready-player-me/integration-guides
- group: start
  title: ''
  type: Portal
  url: https://studio.readyplayer.me/
- group: start
  title: ''
  type: Portal
  url: https://readyplayer.me/developers
- group: start
  title: ''
  type: Portal
  url: https://readyplayer.me/hub
- group: company
  title: ''
  type: Blog
  url: https://readyplayer.me/blog
- group: build
  title: ''
  type: Github
  url: https://github.com/readyplayerme
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ready-player-me/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/readyplayerme
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@readyplayerme
- group: operate
  title: ''
  type: Discord
  url: https://discord.com/invite/readyplayerme
- group: operate
  title: ''
  type: Support
  url: mailto:support@readyplayer.me
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/rpm-unity-sdk-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/rpm-unreal-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/visage
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/rpm-react-avatar-creator
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/Example-iOS-Swift
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/Example-Android-Kotlin
- group: build
  title: ''
  type: SDKs
  url: https://github.com/readyplayerme/Example-React-Native
- group: docs
  title: ''
  type: JSONSchema
  url: https://github.com/readyplayerme/content-validation-schemas
- group: build
  title: ''
  type: Tools
  url: https://github.com/readyplayerme/animation-library
- group: commercial
  title: ''
  type: Plans
  url: plans/ready-player-me-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ready-player-me-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ready-player-me-finops.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ready-player-me-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/ready-player-me-context.jsonld
examples:
- key_count: 2
  name: Ready Player Me Asset Example
  slug: ready-player-me-asset-example
- key_count: 8
  name: Ready Player Me Avatar Example
  slug: ready-player-me-avatar-example
finops:
- name: Ready Player Me Finops
  service_category: ''
  slug: ready-player-me-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ready-player-me.png
json_schemas:
- name: Ready Player Me Asset
  property_count: 8
  slug: ready-player-me-asset
- name: Ready Player Me Avatar
  property_count: 8
  slug: ready-player-me-avatar
json_structures:
- name: Ready Player Me Avatar Structure
  property_count: 0
  slug: ready-player-me-avatar-structure
jsonld:
- class_count: 13
  name: Ready Player Me Context
  property_count: 8
  slug: ready-player-me-context
layout: provider
name: Ready Player Me
nav: Providers
network: true
overview: 'Ready Player Me publishes 3 APIs on the [APIs.io](https://apis.io/) network: Avatars API, Assets API, and Auth API. Tagged areas include Avatars, 3D, Gaming, VR, and AR.


  The Ready Player Me catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ready Player Me''s developer surface includes authentication, developer portal, documentation, engineering blog, GitHub presence, YouTube channel, support, and 23 more developer resources.'
plans:
- name: Ready Player Me Plans Pricing
  plan_count: 3
  slug: ready-player-me-plans-pricing
random_paper: 94
rate_limits:
- limit_count: 0
  name: Ready Player Me Rate Limits
  slug: ready-player-me-rate-limits
rules:
- name: Ready Player Me API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ready-player-me-jsonschema-spectral-rules
- name: Ready Player Me API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: ready-player-me-rules
score:
  band: developing
  composite: 48.1
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.0
    developer_ergonomics: 50.0
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 0.0
  previous_composite: 48.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Ready Player Me Authentication
  slug: ready-player-me-authentication
  summary_line: apiKey · 1 scheme
slug: ready-player-me
tags:
- Avatars
- 3D
- Gaming
- VR
- AR
- Metaverse
- glTF
- Cross-Platform
- Unity
- Unreal
- Web
- Mobile
website: https://readyplayer.me/
---
