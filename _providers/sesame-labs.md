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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-01'
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
- description: Notch turns a product page and plain-language brief into a finished video or image ad. Connect it over MCP to create, review, and edit ads from your AI chat. Ads created over MCP land in the user's No
  name: Sesame Labs MCP Server
  slug: sesame-labs-mcp-server
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
random_paper: 9
rate_limits:
- limit_count: 0
  name: Sesame Labs Rate Limits
  slug: sesame-labs-rate-limits
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
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
