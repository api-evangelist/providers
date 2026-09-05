---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Published applications and self-hostable app downloads.
  name: PlayCanvas Apps API
  slug: playcanvas-apps-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Project asset create/read/update/delete.
  name: PlayCanvas Assets API
  slug: playcanvas-assets-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Version-control branches.
  name: PlayCanvas Branches API
  slug: playcanvas-branches-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Branch checkpoints (snapshots).
  name: PlayCanvas Checkpoints API
  slug: playcanvas-checkpoints-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Asynchronous job polling.
  name: PlayCanvas Jobs API
  slug: playcanvas-jobs-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Project-level operations.
  name: PlayCanvas Projects API
  slug: playcanvas-projects-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Account rate-limit inspection.
  name: PlayCanvas RateLimits API
  slug: playcanvas-ratelimits-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Project scenes.
  name: PlayCanvas Scenes API
  slug: playcanvas-scenes-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: SuperSplat Gaussian-splat publishing.
  name: PlayCanvas Splats API
  slug: playcanvas-splats-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: PlayCanvas REST Apps API
  slug: open-playcanvas-apps-api
- collection_type: open
  name: PlayCanvas REST Apps Assets API
  slug: open-playcanvas-assets-api
- collection_type: open
  name: PlayCanvas REST Apps Branches API
  slug: open-playcanvas-branches-api
- collection_type: open
  name: PlayCanvas REST Apps Checkpoints API
  slug: open-playcanvas-checkpoints-api
- collection_type: open
  name: PlayCanvas REST Apps Jobs API
  slug: open-playcanvas-jobs-api
- collection_type: open
  name: PlayCanvas REST Apps Projects API
  slug: open-playcanvas-projects-api
- collection_type: open
  name: PlayCanvas REST Apps RateLimits API
  slug: open-playcanvas-ratelimits-api
- collection_type: open
  name: PlayCanvas REST Apps Scenes API
  slug: open-playcanvas-scenes-api
- collection_type: open
  name: PlayCanvas REST Apps Splats API
  slug: open-playcanvas-splats-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/playcanvas-rest-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://playcanvas.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.playcanvas.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.playcanvas.com/user-manual/
- group: docs
  title: ''
  type: APIReference
  url: https://api.playcanvas.com
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.playcanvas.com/user-manual/getting-started/
- group: company
  title: ''
  type: Blog
  url: https://blog.playcanvas.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/playcanvas
- group: operate
  title: ''
  type: Support
  url: https://forum.playcanvas.com
- group: commercial
  title: ''
  type: Pricing
  url: https://playcanvas.com/plans
- group: start
  title: ''
  type: SignUp
  url: https://login.playcanvas.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://playcanvas.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://playcanvas.com/privacy
- group: auth
  title: ''
  type: Authentication
  url: authentication/playcanvas-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/playcanvas-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/playcanvas-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/playcanvas-packages.yml
- group: design
  title: ''
  type: Components
  url: components/playcanvas-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/playcanvas-well-known.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/playcanvas-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/playcanvas-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/playcanvas-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/playcanvas-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/playcanvas-changelog.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/playcanvas-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/playcanvas-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/playcanvas-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/playcanvas-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: PlayCanvas is an open-source WebGL/WebGPU 3D engine and cloud platform for building games, product configurators, and interactive 3D experiences that run in any web browser. It offers a browser-based collaborative Editor, a standalone engine on npm/CDN, React components, and Web Components, plus the SuperSplat toolchain for Gaussian-splat capture and publishing. PlayCanvas exposes a REST API (beta) for automating the platform — managing project assets, version-control branches and checkpoints, listing scenes, exporting projects, downloading self-hostable apps, polling asynchronous jobs, and publishing splats — authenticated with Bearer access tokens over HTTPS.
image: https://playcanvas.com/static-assets/images/social/playcanvas.png
layout: provider
modified: '2026-07-20'
name: PlayCanvas
nav: Providers
network: true
overview: 'PlayCanvas publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Assets API, Branches API, and 6 more. Tagged areas include Company, 3D, Game Engine, WebGL, and WebGPU.


  PlayCanvas'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 22 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 6
  name: Playcanvas Rate Limits
  slug: playcanvas-rate-limits
score:
  band: developing
  composite: 51.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 4.5
    contract_quality: 59.2
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 51.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/playcanvas/refs/heads/main/screenshots/playcanvas-2026-08-17T081259.png
security:
- kind: authentication
  name: Playcanvas Authentication
  slug: playcanvas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Playcanvas Domain Security
  slug: playcanvas-domain-security
  summary_line: TLSv1.3
slug: playcanvas
tags:
- Company
- 3D
- Game Engine
- WebGL
- WebGPU
- Graphics
- Developer Tools
- Gaussian Splatting
- Rendering
website: https://playcanvas.com
---
