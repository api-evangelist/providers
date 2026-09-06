---
access_model:
  confidence: high
  label: Retired - public platform shut down 2026-01-31
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - lifecycle
  - dns-probe
  trial: false
  try_now: false
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
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 12
  human_in_the_loop: 0
  name: Ready Player Me Agentic Access
  operation_count: 23
  slug: ready-player-me-agentic-access
  summary_line: 23 operations · 12 acting
api_count: 3
apis:
- baseURL: https://api.readyplayer.me/
  baseurl_source: declared
  description: Create, retrieve, update, and delete Ready Player Me cross-platform avatars. Includes template-based creation, asset equipping, draft management, color palette discovery, and binary glTF (.glb) plus 2
  name: Ready Player Me Avatars API
  slug: ready-player-me-avatars-api
- baseURL: https://api.readyplayer.me/
  baseurl_source: declared
  description: Discover and retrieve avatar wearable assets — hair, outfits, headwear, glasses, facewear, footwear, beards, costumes, and custom assets — scoped to an application and optionally filtered to those vie
  name: Ready Player Me Assets API
  slug: ready-player-me-assets-api
- baseURL: https://api.readyplayer.me/
  baseurl_source: declared
  description: Anonymous user creation, email-code login, token refresh, and avatar access tokens used by the Ready Player Me Avatar Creator and SDKs. Authentication runs through each application's per-studio subdom
  name: Ready Player Me Auth API
  slug: ready-player-me-auth-api
artifact_total: 20
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ready Player Me Assets API
  slug: open-ready-player-me-assets-api
- collection_type: open
  name: Ready Player Me Assets Auth API
  slug: open-ready-player-me-auth-api
- collection_type: open
  name: Ready Player Me Assets Avatars API
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
- group: build
  title: ''
  type: GitHubOrganization
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
- group: build
  title: ''
  type: Packages
  url: packages/ready-player-me-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/ready-player-me-packages.yml
- group: design
  title: ''
  type: Components
  url: components/ready-player-me-components.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ready-player-me-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ready-player-me-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ready-player-me-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ready-player-me-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ready-player-me-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Netflix acquired Ready Player Me in December 2025 and shut the public platform down on 2026-01-31; the retirement is now complete at the DNS layer, so readyplayer.me, api.readyplayer.me, docs.readyplayer.me and studio.readyplayer.me all fail to resolve and there is no first-party surface left to read.
  evidence:
  - status: 0
    url: https://api.readyplayer.me/openapi.json
  - status: 0
    url: https://docs.readyplayer.me/
  - status: 0
    url: https://readyplayer.me/developers
  - status: 0
    url: https://api.readyplayer.me/.well-known/agent-card.json
  - status: 200
    url: https://api.github.com/orgs/readyplayerme
  reason: defunct
  state: none
created: '2026-05-25'
description: 'Ready Player Me was a cross-game avatar platform: a hosted Avatar Creator plus REST APIs that produced interoperable 3D character avatars as binary glTF (.glb) and 2D PNG renders for Unity, Unreal, web, iOS and Android. The Avatars, Assets and Auth APIs covered draft/save avatar creation, template-based creation, wearable-asset equipping and discovery, colour palettes, render precompilation and anonymous/email-code user authentication, all scoped to a studio application via an X-APP-ID header. Netflix acquired the company in December 2025 and the public platform - Avatar Creator, PlayerZero and the developer APIs at api.readyplayer.me - was shut down on 31 January 2026. As of 26 August 2026 readyplayer.me publishes MX and TXT records but no A record, and api.readyplayer.me, docs.readyplayer.me and studio.readyplayer.me are NXDOMAIN, so every first-party developer surface is gone. Avatars already exported as .glb files still load in any glTF 2.0 engine; the readyplayerme GitHub
  organization and two npm packages remain public.'
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
modified: '2026-08-26'
name: Ready Player Me
nav: Providers
network: true
overview: 'Ready Player Me publishes 3 APIs on the [APIs.io](https://apis.io/) network: Avatars API, Assets API, and Auth API. Tagged areas include Avatars, 3D, Gaming, VR, and AR.


  The Ready Player Me catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Ready Player Me''s developer surface includes authentication, YouTube channel, support, tooling, and 26 more developer resources.'
plans:
- name: Ready Player Me Plans Pricing
  plan_count: 3
  slug: ready-player-me-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Ready Player Me Rate Limits
  slug: ready-player-me-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Ready Player Me API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: ready-player-me-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Ready Player Me API Rules
  rule_count: 7
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 6
  slug: ready-player-me-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 63.5
    catalog_earned_first_party: 0.0
    catalog_gap: 51.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 54.8
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 28.8
    operational_transparency: 5.3
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
---
