---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.6
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Hosted, remote Model Context Protocol server that lets an AI assistant create finished video and image ads from a plain-language brief. Streamable HTTP transport with browser-based OAuth 2.0 (PKCE + d
  name: Notch MCP Server
  slug: notch-mcp-server
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.usenotch.ai
- group: docs
  title: ''
  type: Documentation
  url: https://app.usenotch.ai/mcp/setup
- group: start
  title: ''
  type: GettingStarted
  url: https://app.usenotch.ai/mcp/setup
- group: commercial
  title: ''
  type: Pricing
  url: https://app.usenotch.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.usenotch.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.usenotch.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.usenotch.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/7ekcRhWFYa
- group: company
  title: ''
  type: Blog
  url: https://www.usenotch.ai/blog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sesame-labs-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sesame-labs-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sesame-labs-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sesame-labs-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sesame-labs-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sesame-labs-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sesame-labs-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sesame-labs-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sesame-labs-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sesame-labs-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sesame-labs-lifecycle.yml
created: '2026-07-17'
description: 'Sesame Labs is the San Francisco company behind Notch (usenotch.ai), an AI-powered advertising platform that generates finished, ready-to-run video and image ads from a plain-language brief — script, AI avatar, voiceover, b-roll footage, captions, and the full edit — rather than isolated clips. Notch is distributed to agents primarily as a hosted, remote Model Context Protocol (MCP) connector at app.usenotch.ai/mcp: any MCP-capable client (Claude, Claude Code, ChatGPT) connects over streamable HTTP with browser-based OAuth 2.0 sign-in and no API keys, then briefs Notch like a teammate to produce ads that land in the user''s workspace. Sesame Labs is a portfolio company of Wing Venture Capital.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sesame-labs.png
layout: provider
mcp_servers:
- description: ''
  name: sesame-labs-mcp.yml
  slug: sesame-labs-mcpyml
modified: '2026-08-13'
name: Sesame Labs
nav: Providers
network: true
overview: 'Sesame Labs publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Advertising, Video, and Marketing.


  Sesame Labs'' developer surface includes documentation, getting-started guide, pricing, signup flow, support, engineering blog, authentication, and 13 more developer resources.'
plans:
- name: Sesame Labs Plans Pricing
  plan_count: 4
  slug: sesame-labs-plans-pricing
random_paper: 58
rate_limits:
- limit_count: 0
  name: Sesame Labs Rate Limits
  slug: sesame-labs-rate-limits
score:
  band: thin
  composite: 34.6
  delta: 6.8
  facets:
    commercial_clarity: 76.3
    contract_quality: 0.0
    developer_ergonomics: 45.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 27.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: authentication
  name: Sesame Labs Authentication
  slug: sesame-labs-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Sesame Labs Domain Security
  slug: sesame-labs-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sesame-labs
tags:
- Company
- Artificial Intelligence
- Advertising
- Video
- Marketing
- Generative AI
- MCP
- Agents
website: https://www.usenotch.ai
---
