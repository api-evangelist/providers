---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Motion Elements Agentic Access
  operation_count: 21
  slug: motion-elements-agentic-access
  summary_line: 21 operations · 1 acting
api_count: 4
apis:
- description: Authenticated account details.
  name: Motion Elements Account API
  slug: motion-elements-account-api
- description: Retrieve individual marketplace elements.
  name: Motion Elements Elements API
  slug: motion-elements-elements-api
- description: 'Reference metadata: media types, categories, software versions, and music facets.'
  name: Motion Elements Media types API
  slug: motion-elements-media-types-api
- description: Search the marketplace across media types.
  name: Motion Elements Search API
  slug: motion-elements-search-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motion-elements-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/motion-elements-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motion-elements-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://motionelements.com
- group: design
  title: ''
  type: Conventions
  url: conventions/motion-elements-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motion-elements-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motion-elements-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/motion-elements-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motion-elements-llms.txt
- group: design
  title: ''
  type: DataModel
  url: data-model/motion-elements-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.motionelements.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.motionelements.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.motionelements.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.motionelements.com/developer
- group: operate
  title: ''
  type: Support
  url: https://help.motionelements.com/
- group: company
  title: ''
  type: Blog
  url: https://www.motionelements.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/motionelements
- group: commercial
  title: ''
  type: Pricing
  url: https://www.motionelements.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.motionelements.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.motionelements.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.motionelements.com/legal/privacy
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://api-docs.motionelements.com/
created: '2026-07-17'
description: 'MotionElements is a global creative-asset marketplace and AI production platform offering an unlimited-download subscription catalog of 26M+ royalty-free assets: stock video, music, sound effects, motion and editing templates (After Effects, Premiere Pro, Final Cut / Apple Motion, DaVinci Resolve, .mogrt), photos, vectors, GIFs and Lottie animations, plus Studio AI generative tools. Its Marketplace API v2 lets platforms search, retrieve, license and download from the catalog using HTTP Basic authentication (API secret key as username) over HTTPS.'
image: https://static.moele.me/img/motionelements-og-en.220830.jpg
layout: provider
mcp_servers:
- description: ''
  name: motion-elements-mcp.yml
  slug: motion-elements-mcpyml
modified: '2026-07-20'
name: Motion Elements
nav: Providers
network: true
overview: 'Motion Elements publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Account API, Elements API, Media types API, and 1 more. Tagged areas include Media, Stock Media, Video, Music, and Sound Effects.


  Motion Elements'' developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 67
score:
  band: developing
  composite: 47.4
  delta: -1.4
  facets:
    commercial_clarity: 44.7
    contract_quality: 60.2
    developer_ergonomics: 60.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 48.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Motion Elements Authentication
  slug: motion-elements-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Motion Elements Domain Security
  slug: motion-elements-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: motion-elements
tags:
- Media
- Stock Media
- Video
- Music
- Sound Effects
- Templates
- Marketplace
- Creative Assets
- Generative AI
- Search
- Company
website: https://motionelements.com
---
