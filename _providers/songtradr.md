---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.0
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 8
  human_in_the_loop: 2
  name: Songtradr Agentic Access
  operation_count: 19
  slug: songtradr-agentic-access
  summary_line: 19 operations · 8 acting · 2 human-in-the-loop
api_count: 3
apis:
- description: The allowed-values API from Songtradr — 1 operation(s) for allowed-values.
  name: Songtradr Allowed Values API
  slug: songtradr-allowed-values-api
- description: The similarity-vector-controller API from Songtradr — 1 operation(s) for similarity-vector-controller.
  name: Songtradr Similarity Vector Controller API
  slug: songtradr-similarity-vector-controller-api
- description: The user API from Songtradr — 15 operation(s) for user.
  name: Songtradr User API
  slug: songtradr-user-api
artifact_total: 12
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Songtradr Allowed Values API
  slug: open-songtradr-allowed-values-api
- collection_type: open
  name: Songtradr Similarity Vector Controller API
  slug: open-songtradr-similarity-vector-controller-api
- collection_type: open
  name: Songtradr User API
  slug: open-songtradr-user-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/songtradr-mcp.yml
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
mcp_servers:
- description: ''
  name: songtradr-mcp.yml
  slug: songtradr-mcpyml
modified: '2026-08-02'
name: Songtradr
nav: Providers
network: true
overview: 'Songtradr publishes 3 APIs on the [APIs.io](https://apis.io/) network: Allowed Values API, Similarity Vector Controller API, and User API. Tagged areas include music, music-licensing, sync-licensing, music-metadata, and audio-tagging.


  Songtradr''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 86
rate_limits:
- limit_count: 1
  name: Songtradr Rate Limits
  slug: songtradr-rate-limits
score:
  band: developing
  composite: 49.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.9
    developer_ergonomics: 53.8
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 26.3
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-17'
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
