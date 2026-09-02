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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.8
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Single GraphQL endpoint for the whole Uthana platform - text-to-motion, video-to-motion, locomotion, stitch/loop, character upload with auto-rigging, asset management, account, subscription, and pay-a
  name: Uthana GraphQL API
  slug: uthana-graphql-api
- description: REST endpoints for downloading generated motions and characters as FBX, GLB, BVH, or Unitree G1 CSV - /motion/file/ (with character mesh), /motion/animation/ (animation track only, not counted against
  name: Uthana Motion Download API
  slug: uthana-motion-download-api
artifact_total: 7
common:
- group: auth
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
  title: ''
  type: ChangeLog
  url: changelog/uthana-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://uthana.com/docs/api/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uthana-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/uthana-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/uthana-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uthana-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uthana-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uthana-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/uthana-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/uthana-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://uthana.com/docs/api/changelog
- group: start
  title: ''
  type: Sandbox
  url: sandbox/uthana-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/uthana-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/uthana-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/uthana-plans.yml
created: '2026-07-17'
description: Uthana builds foundation models for human motion — generative AI that creates lifelike 3D character animation from text prompts, 2D reference video, or real-time input, instantly retargeted to any rig (with auto-rigging for unrigged characters). Founded in 2023, Uthana exposes its platform through a GraphQL API at uthana.com/graphql with official Python and JavaScript/TypeScript clients, React hooks, Blender and Maya plugins, ComfyUI nodes, and REST endpoints for downloading motions in FBX, GLB, BVH, and Unitree G1 CSV formats for games, film, AI-native platforms, and robotics.
graphqls:
- description: 'generated: ''2026-07-21'''
  name: Uthana GraphQL API
  slug: uthana-graphql
image: https://cdn.prod.website-files.com/67a3a4768bd61958d5872829/67aa15d7488c26c0dfdb3ab7_thumb.png
layout: provider
mcp_servers:
- description: ''
  name: Uthana MCP Server
  slug: uthana-mcp-server
modified: '2026-07-21'
name: Uthana
nav: Providers
network: true
overview: 'Uthana publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Animation, 3D Characters, Generative AI, Motion Capture, and Gaming.


  Uthana''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, FAQ, pricing, and 29 more developer resources.'
plans:
- name: Uthana Plans
  plan_count: 7
  slug: uthana-plans
random_paper: 11
score:
  band: developing
  composite: 50.7
  coverage:
    artifact_dirs: 18
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 26.3
  previous_composite: 50.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uthana/refs/heads/main/screenshots/uthana-2026-08-17T082703.png
security:
- kind: authentication
  name: Uthana Authentication
  slug: uthana-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Uthana Domain Security
  slug: uthana-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
