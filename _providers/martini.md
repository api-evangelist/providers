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
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
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
  score: 14.7
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Hosted, OAuth-secured Model Context Protocol server that lets supported AI assistants work inside Martini projects using the signed-in user''s account permissions — browse projects, canvases, subjects '
  name: Martini MCP Connector
  slug: martini-mcp-connector
artifact_total: 5
common:
- group: docs
  title: ''
  type: Documentation
  url: https://www.martini.film/docs/mcp
- group: docs
  title: ''
  type: APIReference
  url: https://www.martini.film/docs/mcp
- group: commercial
  title: ''
  type: Pricing
  url: https://www.martini.film/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.martini.film/waitlist
- group: start
  title: ''
  type: Login
  url: https://www.martini.film/login
- group: operate
  title: ''
  type: Support
  url: https://www.martini.film/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.martini.film/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.martini.film/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/martini-film
- group: other
  title: ''
  type: Download
  url: https://www.martini.film/download
- group: agent
  title: ''
  type: MCPServer
  url: mcp/martini-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/martini-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/martini-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/martini-conformance.yml
- group: auth
  title: ''
  type: Security
  url: https://www.martini.film/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/martini-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/martini-domain-security.yml
created: '2026-07-17'
description: Martini is a collaborative, AI-native filmmaking platform — "Figma for filmmaking" — that lets teams generate, direct, and edit AI video in real time and export to professional editing software (Adobe Premiere Pro, DaVinci Resolve) via XML. Filmmakers compose shots with virtual camera control, keep characters consistent across shots using reusable Subjects, and generate footage across leading models (Google Veo 3.1, Kling 3.0 Pro, OpenAI Sora 2, MiniMax Hailuo 02, ByteDance Seedance, Nano Banana Pro, Flux 2). Its developer surface is a hosted, OAuth-secured Model Context Protocol (MCP) connector at https://www.martini.film/mcp that lets AI assistants (Claude Desktop/Code, Gemini CLI, ChatGPT, Cursor) browse projects, organize canvases and subjects, upload references, and run approved generation inside a user's own account. Martini also publishes open Agent Skills on GitHub, including a Blender-to-Martini camera-faithful handoff. Built by C47 Inc.; Y Combinator Winter 2026.
image: https://www.martini.film/marketing/uisample-3.jpg
layout: provider
mcp_servers:
- description: ''
  name: Martini MCP Server
  slug: martini-mcp-server
modified: '2026-07-20'
name: Martini
nav: Providers
network: true
overview: 'Martini publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Filmmaking, and Generative AI.


  Martini''s developer surface includes documentation, API reference, pricing, signup flow, support, authentication, and 12 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 13.6
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/martini/refs/heads/main/screenshots/martini-2026-07-25T230407.png
security:
- kind: authentication
  name: Martini Authentication
  slug: martini-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Martini Domain Security
  slug: martini-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Martini Vulnerability Disclosure
  slug: martini-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: martini
tags:
- Company
- Artificial Intelligence
- Video
- Filmmaking
- Generative AI
- Creative Tools
- MCP
- Agents
- Collaboration
- Media Production
---
