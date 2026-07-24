---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 11.5
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/lovable-dev-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/lovable-dev-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lovable-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lovable.dev
- group: docs
  title: ''
  type: Documentation
  url: https://docs.lovable.dev
- group: commercial
  title: ''
  type: Pricing
  url: https://lovable.dev/pricing
- group: other
  title: ''
  type: BuildWithURL
  url: https://docs.lovable.dev/integrations/build-with-url
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.lovable.dev
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://docs.lovable.dev/integrations/lovable-mcp-server
- group: other
  title: ''
  type: GPTEngineerHistory
  url: https://lovable.dev/gpt-engineer
- group: build
  title: ''
  type: GitHubApp
  url: https://github.com/apps/lovable-dev
- group: build
  title: ''
  type: GitHubOrgUserProjects
  url: https://github.com/GPT-Engineer-App
- group: build
  title: ''
  type: GitHubOrgDev
  url: https://github.com/GPT-Engineer-App-Dev
- group: other
  title: ''
  type: GPTEngineerRepo
  url: https://github.com/AntonOsika/gpt-engineer
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/lovable-dev
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/lovable_dev
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/lovable-dev
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@lovable-dev
- group: other
  title: ''
  type: Reddit
  url: https://www.reddit.com/r/lovable
- group: company
  title: ''
  type: Blog
  url: https://lovable.dev/blog
created: '2026-05-25'
description: Lovable is a Stockholm-based AI app builder ("vibe coding") platform that turns natural-language prompts into full-stack web applications. Founded in late 2023 by Anton Osika (CEO) and Fabian Hedin (CTO), Lovable grew out of the founders' open-source GPT Engineer project (originally a CLI codegen tool that crossed 50,000+ GitHub stars) and was relaunched as a commercial product targeting non-technical builders, product managers, designers, and founders. Users chat with Lovable's agent to scaffold React/Tailwind front-ends backed by a managed Postgres ("Lovable Cloud") and authentication layer; projects can sync to GitHub or GitLab, deploy to lovable.app subdomains or custom domains, and integrate with Supabase, Stripe/Paddle, Resend, Mailgun, AWS S3, BigQuery, and Snowflake. The platform's developer surface is intentionally small — there is no traditional REST/SDK developer API. Programmatic entry points are limited to the "Build with URL" pattern (passing a prompt via querystring/hash
  to https://lovable.dev/?autosubmit=true) and a hosted Model Context Protocol server at https://mcp.lovable.dev that lets AI clients (Claude, Cursor, Claude Code) create projects, message the building agent, inspect diffs, provision Postgres databases, and read analytics on behalf of an authenticated Lovable account. Lovable raised a $200M Series A (Accel) in July 2025 and a $330M Series B (CapitalG, Menlo Anthology) in December 2025 at a $6.6B valuation, with reported ARR growing from $100M (July 2025) to $400M+ (February 2026) and roughly 8 million users.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lovable-dev.png
layout: provider
mcp_servers:
- description: ''
  name: mcp.lovable.dev
  slug: mcplovabledev
modified: '2026-05-25'
name: Lovable
nav: Providers
network: true
overview: 'Lovable is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Generative AI, AI App Builder, Vibe Coding, and Low Code.


  Lovable''s developer surface includes documentation, pricing, YouTube channel, engineering blog, and 16 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 14.4
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 0.0
    developer_ergonomics: 19.6
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 14.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lovable-dev/refs/heads/main/screenshots/lovable-dev-2026-06-20T184741.png
security:
- kind: domain-security
  name: Lovable Dev Domain Security
  slug: lovable-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Lovable Dev Vulnerability Disclosure
  slug: lovable-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Lovable Dev Trust Center
  slug: lovable-dev-trust-center
  summary_line: SOC 2, GDPR
slug: lovable-dev
tags:
- AI
- Generative AI
- AI App Builder
- Vibe Coding
- Low Code
- No Code
- Text to App
- Application Development
- Web Development
- Frontend
- Full Stack
- Model Context Protocol
- MCP
- Stockholm
- Sweden
website: https://lovable.dev
---
