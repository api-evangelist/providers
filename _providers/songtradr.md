---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.3
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Songtradr Agentic Access
  operation_count: 19
  slug: songtradr-agentic-access
  summary_line: 19 operations · 8 acting · 2 human-in-the-loop
api_count: 1
apis:
- description: 'JWT-authenticated REST API for deep music metadata and auto-tagging. Log in via POST /api/v1/user/login to obtain a bearer JWT, then manage your account and musicube cloud data, initiate presigned-S3 '
  name: Songtradr API
  slug: songtradr-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/songtradr-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/songtradr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.songtradr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.songtradr.com/swagger-ui.html
- group: docs
  title: ''
  type: APIReference
  url: https://api.songtradr.com/v3/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://api.songtradr.com/swagger-ui.html
- group: operate
  title: ''
  type: Support
  url: https://support.songtradr.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://helpdesk.songtradr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.songtradr.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/songtradr
- group: commercial
  title: ''
  type: Pricing
  url: https://www.songtradr.com/pro
- group: start
  title: ''
  type: SignUp
  url: https://www.songtradr.com/signup/personal
- group: start
  title: ''
  type: Login
  url: https://www.songtradr.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.songtradr.com/legals/termsofuse
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.songtradr.com/legals/privacypolicy
- group: build
  title: ''
  type: Packages
  url: packages/songtradr-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/songtradr-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/songtradr-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/songtradr-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/songtradr-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/songtradr-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/songtradr-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/songtradr-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/songtradr-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/songtradr-api-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/songtradr-rate-limits.yml
created: '2026-08-02'
description: 'Songtradr is a Santa Monica, California B2B music company that builds licensing, rights and music-data infrastructure for brands, agencies, digital platforms, artists and rightsholders. Founded in 2014, it operates a global sync-licensing marketplace alongside acquired businesses including Bandcamp, 7digital, MassiveMusic, Big Sync Music and the AI music-metadata company Musicube. Its public developer surface is the Songtradr API — a JWT-authenticated REST API, documented with a live OpenAPI 3.1 description, that returns deep music metadata (musical features, genre predictions, tags, taggrams, tag strengths, contributors, similarity vectors) and drives auto-tagging: rightsholders upload audio through a presigned S3 link and Songtradr''s models classify it against a taxonomy of 350+ descriptive tags across 30+ categories, then expose semantic search over the results. First-party API clients are published for Python, JavaScript/Node and Ruby.'
image: https://avatars.githubusercontent.com/u/61609417?v=4
layout: provider
modified: '2026-08-02'
name: Songtradr
nav: Providers
network: true
overview: 'Songtradr publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include music, music-licensing, sync-licensing, music-metadata, and audio-tagging.


  Songtradr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
random_paper: 76
rate_limits:
- limit_count: 1
  name: Songtradr Rate Limits
  slug: songtradr-rate-limits
score:
  band: developing
  composite: 48.7
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 63.6
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 48.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Songtradr Authentication
  slug: songtradr-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Songtradr Domain Security
  slug: songtradr-domain-security
  summary_line: TLSv1.3 · DMARC
slug: songtradr
tags:
- music
- music-licensing
- sync-licensing
- music-metadata
- audio-tagging
- semantic-search
- machine-learning
- media
- entertainment
- rights-management
- audio
website: https://www.songtradr.com/
---
