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
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: The Llms Full.txt API from Bounti — 1 operation(s) for llms full.txt.
  name: Bounti Llms Full.txt API
  slug: bounti-llms-full-txt-api
- description: The Llms.txt API from Bounti — 1 operation(s) for llms.txt.
  name: Bounti Llms.txt API
  slug: bounti-llms-txt-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://bounti.ai/
- group: company
  title: ''
  type: About
  url: https://bounti.ai/about
- group: company
  title: ''
  type: Blog
  url: https://bounti.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://bounti.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://claw.bounti.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://re.bounti.ai/real-estate/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bounti.ai/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bounti.ai/privacy-policy
- group: operate
  title: ''
  type: Support
  url: mailto:support@bounti.ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bounti-ai
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bounti-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bounti-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bounti-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bounti-domain-security.yml
created: '2026-07-17'
description: Bounti (Bounti Labs, bounti.ai) is an AI-powered real estate visualization and automation platform founded in 2023 by Ashar Rizqi and Matt Cooley and backed by GV (Google Ventures), Bloomberg Beta, Floodgate, Haystack, Octave Ventures and MS&AD. Its products include AI virtual staging and photo enhancement, cinematic listing-photo animation, automated marketing-video creation, before/after reveal videos, collaborative client studios, and B.Claw — an AI operating system that consolidates 13+ real estate tools (Gmail, calendar, CRM, WhatsApp, website builder) into one conversational interface. Bounti does not publish a general integration API, but it does expose an agent-facing, unauthenticated Content API (advertised via an AI-plugin manifest at /.well-known/ai-plugin.json) plus /llms.txt and /llms-full.txt so AI assistants can accurately answer questions about its products, pricing, and content.
image: https://bounti.ai/favicon.png
layout: provider
mcp_servers:
- description: ''
  name: bounti-mcp.yml
  slug: bounti-mcpyml
modified: '2026-07-18'
name: Bounti
nav: Providers
network: true
overview: 'Bounti publishes 2 APIs on the [APIs.io](https://apis.io/) network: Llms Full.txt API and Llms.txt API. Tagged areas include Company, Real Estate, Artificial Intelligence, Marketing, and Sales Enablement.


  Bounti''s developer surface includes engineering blog, pricing, signup flow, support, and 11 more developer resources.'
random_paper: 41
score:
  band: thin
  composite: 33.0
  delta: -1.3
  facets:
    commercial_clarity: 44.7
    contract_quality: 49.2
    developer_ergonomics: 10.3
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 0.0
  previous_composite: 34.3
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bounti/refs/heads/main/screenshots/bounti-2026-07-25T203646.png
security:
- kind: domain-security
  name: Bounti Domain Security
  slug: bounti-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bounti
tags:
- Company
- Real Estate
- Artificial Intelligence
- Marketing
- Sales Enablement
- Virtual Staging
- Content Generation
- AI Agents
website: https://bounti.ai/
---
