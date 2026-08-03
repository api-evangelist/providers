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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.3
  scored_at: '2026-08-03'
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
  name: martini-mcp.yml
  slug: martini-mcpyml
modified: '2026-07-20'
name: Martini
nav: Providers
network: true
overview: 'Martini publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Video, Filmmaking, and Generative AI.


  Martini''s developer surface includes documentation, API reference, pricing, signup flow, support, authentication, and 12 more developer resources.'
random_paper: 91
score:
  band: thin
  composite: 29.2
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 15.8
  previous_composite: 29.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
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
- Model Context Protocol
- Agents
- Collaboration
- Media Production
---
