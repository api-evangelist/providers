---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.2
  scored_at: '2026-11-06'
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
  description: Project scenes.
  name: PlayCanvas Scenes API
  slug: playcanvas-scenes-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: SuperSplat Gaussian-splat publishing.
  name: PlayCanvas Splats API
  slug: playcanvas-splats-api
- baseURL: https://playcanvas.com/api
  baseurl_source: declared
  description: Account rate-limit inspection.
  name: PlayCanvas Rate Limits API
  slug: playcanvas-rate-limits-api
artifact_total: 28
collections:
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
- group: commercial
  href: https://artifacts.apis.io/playcanvas/plans/playcanvas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/playcanvas-plans-pricing.yml
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.playcanvas.com/rss.xml
- group: other
  href: https://artifacts.apis.io/playcanvas/overlays/playcanvas-rest-overlay.yaml
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
  href: https://artifacts.apis.io/playcanvas/authentication/playcanvas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/playcanvas-authentication.yml
- group: auth
  href: https://artifacts.apis.io/playcanvas/security/playcanvas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/playcanvas-domain-security.yml
- group: build
  href: https://artifacts.apis.io/playcanvas/packages/playcanvas-packages.yml
  title: ''
  type: Packages
  url: packages/playcanvas-packages.yml
- group: build
  href: https://artifacts.apis.io/playcanvas/packages/playcanvas-packages.yml
  title: ''
  type: SDKs
  url: packages/playcanvas-packages.yml
- group: design
  href: https://artifacts.apis.io/playcanvas/components/playcanvas-components.yml
  title: ''
  type: Components
  url: components/playcanvas-components.yml
- group: agent
  href: https://artifacts.apis.io/playcanvas/well-known/playcanvas-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/playcanvas-well-known.yml
- group: agent
  href: https://artifacts.apis.io/playcanvas/mcp/playcanvas-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/playcanvas-mcp.yml
- group: agent
  href: https://artifacts.apis.io/playcanvas/llms/playcanvas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/playcanvas-llms.txt
- group: design
  href: https://artifacts.apis.io/playcanvas/conformance/playcanvas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/playcanvas-conformance.yml
- group: design
  href: https://artifacts.apis.io/playcanvas/lifecycle/playcanvas-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/playcanvas-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/playcanvas/changelog/playcanvas-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/playcanvas-changelog.yml
- group: operate
  href: https://artifacts.apis.io/playcanvas/rate-limits/playcanvas-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/playcanvas-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/playcanvas/conventions/playcanvas-conventions.yml
  title: ''
  type: Conventions
  url: conventions/playcanvas-conventions.yml
- group: design
  href: https://artifacts.apis.io/playcanvas/errors/playcanvas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/playcanvas-problem-types.yml
- group: design
  href: https://artifacts.apis.io/playcanvas/data-model/playcanvas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/playcanvas-data-model.yml
- group: agent
  href: https://artifacts.apis.io/playcanvas/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: PlayCanvas is an open-source WebGL/WebGPU 3D engine and cloud platform for building games, product configurators, and interactive 3D experiences that run in any web browser. It offers a browser-based collaborative Editor, a standalone engine on npm/CDN, React components, and Web Components, plus the SuperSplat toolchain for Gaussian-splat capture and publishing. PlayCanvas exposes a REST API (beta) for automating the platform — managing project assets, version-control branches and checkpoints, listing scenes, exporting projects, downloading self-hostable apps, polling asynchronous jobs, and publishing splats — authenticated with Bearer access tokens over HTTPS.
finops:
- has_sources: true
  method: derived
  name: Playcanvas Finops
  primary_unit: seat
  service_category: ''
  slug: playcanvas-finops
  template: false
image: https://playcanvas.com/static-assets/images/social/playcanvas.png
layout: provider
modified: '2026-10-06'
name: PlayCanvas
nav: Providers
network: true
overview: 'PlayCanvas publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Apps API, Assets API, Branches API, and 6 more. Tagged areas include Company, 3D, Game Engine, WebGL, and WebGPU.


  The PlayCanvas catalog on APIs.io includes 1 Spectral governance ruleset.


  PlayCanvas'' developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Playcanvas Plans Pricing
  plan_count: 3
  slug: playcanvas-plans-pricing
- name: Playcanvas Price Estimates
  plan_count: 0
  slug: playcanvas-price-estimates
random_paper: 18
rate_limits:
- limit_count: 6
  name: Playcanvas Rate Limits
  slug: playcanvas-rate-limits
rules:
- authorship: generated
  effective_rule_count: 113
  extends:
  - spectral:oas
  name: PlayCanvas API Rules
  rule_count: 72
  severity_counts:
    error: 65
    hint: 0
    info: 3
    warn: 4
  slug: playcanvas-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 28
    catalog_earned: 68.5
    catalog_earned_first_party: 24.0
    catalog_gap: 46.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 53.5
    developer_ergonomics: 66.1
    discoverability: 73.2
    operational_transparency: 50.0
  previous_composite: 60.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/playcanvas/playcanvas-2026-08-17T081259.png
security:
- kind: authentication
  name: Playcanvas Authentication
  slug: playcanvas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Playcanvas Domain Security
  slug: playcanvas-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: Branch and checkpoint a PlayCanvas project
  slug: playcanvas-branch-and-checkpoint
- name: Export a project and download a self-hostable app
  slug: playcanvas-export-and-download
- name: Manage PlayCanvas project assets
  slug: playcanvas-manage-assets
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
