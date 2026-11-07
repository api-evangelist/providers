---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - sandbox
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Single GraphQL endpoint for the whole Uthana platform - text-to-motion, video-to-motion, locomotion, stitch/loop, character upload with auto-rigging, asset management, account, subscription, and pay-a
  name: Uthana GraphQL API
  slug: uthana-graphql-api
- description: REST endpoints for downloading generated motions and characters as FBX, GLB, BVH, or Unitree G1 CSV - /motion/file/ (with character mesh), /motion/animation/ (animation track only, not counted against
  name: Uthana Motion Download API
  slug: uthana-motion-download-api
artifact_total: 10
common:
- group: auth
  href: https://artifacts.apis.io/uthana/security/uthana-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/uthana-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://uthana.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://uthana.com/docs/api
- group: docs
  title: ''
  type: Documentation
  url: https://uthana.com/docs/api
- group: docs
  title: ''
  type: APIReference
  url: https://uthana.com/docs/api/graphql
- group: start
  title: ''
  type: GettingStarted
  url: https://uthana.com/docs/api/
- group: operate
  title: ''
  type: Support
  url: https://uthana.com/docs/api/support
- group: company
  title: ''
  type: Blog
  url: https://uthana.com/blog
- group: operate
  title: ''
  type: FAQ
  url: https://uthana.com/faq
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Uthana
- group: commercial
  title: ''
  type: Pricing
  url: https://uthana.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://uthana.com/user/signup
- group: start
  title: ''
  type: Login
  url: https://uthana.com/user/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://uthana.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://uthana.com/privacy
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/PbMzMPSyTG
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@UthanaInc
- group: company
  title: ''
  type: X (Twitter)
  url: https://x.com/Uthana_Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uthanainc/
- group: operate
  title: ''
  type: RateLimits
  url: https://uthana.com/docs/api/rate-limits
- group: operate
  href: https://artifacts.apis.io/uthana/changelog/uthana-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/uthana-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://uthana.com/docs/api/changelog
- group: agent
  href: https://artifacts.apis.io/uthana/llms/uthana-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/uthana-llms.txt
- group: build
  href: https://artifacts.apis.io/uthana/packages/uthana-packages.yml
  title: ''
  type: Packages
  url: packages/uthana-packages.yml
- group: build
  href: https://artifacts.apis.io/uthana/packages/uthana-packages.yml
  title: ''
  type: SDKs
  url: packages/uthana-packages.yml
- group: agent
  href: https://artifacts.apis.io/uthana/mcp/uthana-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/uthana-mcp.yml
- group: agent
  href: https://artifacts.apis.io/uthana/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/uthana/authentication/uthana-authentication.yml
  title: ''
  type: Authentication
  url: authentication/uthana-authentication.yml
- group: design
  href: https://artifacts.apis.io/uthana/conformance/uthana-conformance.yml
  title: ''
  type: Conformance
  url: conformance/uthana-conformance.yml
- group: design
  href: https://artifacts.apis.io/uthana/errors/uthana-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/uthana-problem-types.yml
- group: design
  href: https://artifacts.apis.io/uthana/lifecycle/uthana-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/uthana-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://uthana.com/docs/api/changelog
- group: start
  href: https://artifacts.apis.io/uthana/sandbox/uthana-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/uthana-sandbox.yml
- group: design
  href: https://artifacts.apis.io/uthana/conventions/uthana-conventions.yml
  title: ''
  type: Conventions
  url: conventions/uthana-conventions.yml
- group: design
  href: https://artifacts.apis.io/uthana/data-model/uthana-data-model.yml
  title: ''
  type: DataModel
  url: data-model/uthana-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/uthana/plans/uthana-plans.yml
  title: ''
  type: Plans
  url: plans/uthana-plans.yml
created: '2026-07-17'
description: Uthana builds foundation models for human motion — generative AI that creates lifelike 3D character animation from text prompts, 2D reference video, or real-time input, instantly retargeted to any rig (with auto-rigging for unrigged characters). Founded in 2023, Uthana exposes its platform through a GraphQL API at uthana.com/graphql with official Python and JavaScript/TypeScript clients, React hooks, Blender and Maya plugins, ComfyUI nodes, and REST endpoints for downloading motions in FBX, GLB, BVH, and Unitree G1 CSV formats for games, film, AI-native platforms, and robotics.
finops:
- has_sources: true
  method: derived
  name: Uthana Finops
  primary_unit: second of generated output
  service_category: ''
  slug: uthana-finops
  template: false
graphqls:
- description: 'generated: ''2026-07-21'''
  name: Uthana GraphQL API
  slug: uthana-graphql
image: https://cdn.prod.website-files.com/67a3a4768bd61958d5872829/67aa15d7488c26c0dfdb3ab7_thumb.png
layout: provider
modified: '2026-07-21'
name: Uthana
nav: Providers
network: true
overview: 'Uthana is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Animation, 3D Characters, Generative AI, Motion Capture, and Gaming.


  Uthana''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, FAQ, pricing, and 29 more developer resources.'
plans:
- name: Uthana Plans
  plan_count: 9
  slug: uthana-plans
random_paper: 17
score:
  band: developing
  composite: 52.3
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 35.1
    developer_ergonomics: 73.2
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 52.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/uthana/uthana-2026-08-17T082703.png
security:
- kind: authentication
  name: Uthana Authentication
  slug: uthana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uthana Domain Security
  slug: uthana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Generate a motion from text and download it
  slug: uthana-text-to-motion
- name: Upload and auto-rig a character
  slug: uthana-upload-and-autorig-character
- name: Generate a motion from a reference video
  slug: uthana-video-to-motion
slug: uthana
tags:
- Animation
- 3D Characters
- Generative AI
- Motion Capture
- Gaming
- Robotics
- Foundation Models
- GraphQL
website: https://uthana.com
---
