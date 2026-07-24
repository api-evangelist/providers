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
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.1
  score: 15.4
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mona-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.mona-ai.de
- group: company
  title: ''
  type: Blog
  url: https://www.mona-ai.de/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://www.mona-ai.de/blog-feed.xml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mona-ai.de/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.mona-ai.de/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mona-ai.de/datenschutz
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.mona-ai.de/impressum
- group: start
  title: ''
  type: Login
  url: https://agents.monaai.de/login
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mona-ai-gmbh
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mona-ai-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mona-ai-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/mona-ai-well-known.yml
created: '2026-07-17'
description: 'Mona AI GmbH (mona-ai.de) is a German AI recruiting-automation company backed by Earlybird. Its platform combines AI agents and digital avatars to automate recruiting and HR processes for staffing agencies and enterprises: 24/7 candidate outreach, automated pre-qualification and candidate-profile generation, and "digital branch" structures — built to be fully GDPR- and EU-AI-Act-compliant. Products include MONA Recruiting, MONA Recruiting Light, MONA Agents, MONA Digital Branch, MONA Consulting and MONA ARS, an autonomous prompt-driven recruiting system that sources, screens, schedules and reports automatically. The website is Wix-hosted and exposes a Wix Site MCP endpoint plus an llms.txt for AI-agent access; the recruiting product itself runs behind a login and does not publish a public developer API, SDK or OpenAPI.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mona-ai.png
layout: provider
mcp_servers:
- description: ''
  name: mona-ai-mcp.yml
  slug: mona-ai-mcpyml
modified: '2026-07-20'
name: Mona Ai
nav: Providers
network: true
overview: 'Mona Ai is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Recruiting, Human Resources, HR Tech, and AI Agents.


  Mona Ai''s developer surface includes engineering blog, pricing, support, and 10 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 16.6
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Mona Ai Domain Security
  slug: mona-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mona-ai
tags:
- Company
- Recruiting
- Human Resources
- HR Tech
- AI Agents
- Automation
- Germany
- MCP
website: https://www.mona-ai.de
---
