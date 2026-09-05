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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'OpenArt''s remote Model Context Protocol server, letting AI agents generate and edit images and video, discover models, manage the library and projects, and check account credits — authorized with the '
  name: OpenArt MCP Server
  slug: openart-mcp-server
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/openart-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openart-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/openart-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/openart-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/openart-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/openart-conventions.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/openart-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openart-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://openart.ai/mcp
- group: operate
  title: ''
  type: Support
  url: https://openart.ai/general_faq
- group: company
  title: ''
  type: Blog
  url: https://openart.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openart-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://openart.ai/suite/pricing
- group: start
  title: ''
  type: SignUp
  url: https://openart.ai/home
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openart.ai/suite/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openart.ai/privacy
- group: company
  title: ''
  type: Website
  url: https://openart.ai/
created: '2026-07-17'
description: OpenArt is an all-in-one AI creation platform for generating and editing images, video, audio, and 3D content from a single workspace. It aggregates leading generative models (Seedance, Google Veo, Sora, GPT Image, Kling and others) and adds tools for consistent character creation, world-building, motion and camera control, relighting, background replacement, and cinematic storytelling for creators, brands, and studios. OpenArt exposes its capabilities to AI agents through a hosted remote Model Context Protocol (MCP) server at https://mcp.openart.ai/mcp, authorized with OAuth 2.0 (PKCE + Dynamic Client Registration, scope full_access); it does not publish a conventional REST API. OpenArt was added to the API Evangelist network as a portfolio company of Canaan Partners and DCM Ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openart.png
layout: provider
mcp_servers:
- description: ''
  name: Openart MCP Server
  slug: openart-mcp-server
modified: '2026-07-20'
name: Openart
nav: Providers
network: true
overview: 'Openart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Generative AI, Image-Generation, and Video Generation.


  Openart''s developer surface includes authentication, documentation, support, engineering blog, pricing, signup flow, and 11 more developer resources.'
random_paper: 5
scopes:
- name: Openart Scopes
  scope_count: 1
  slug: openart-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 27.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openart/refs/heads/main/screenshots/openart-2026-08-07T190531.png
security:
- kind: authentication
  name: Openart Authentication
  slug: openart-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Openart Domain Security
  slug: openart-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openart
tags:
- Company
- Artificial Intelligence
- Generative AI
- Image-Generation
- Video Generation
- Creative Tools
- MCP
website: https://openart.ai/
---
