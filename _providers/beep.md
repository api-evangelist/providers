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
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 10.8
  scored_at: '2026-08-11'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://justbeepit.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.justbeepit.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://web.justbeepit.com/auth?active=signup
- group: start
  title: ''
  type: Login
  url: https://web.justbeepit.com/auth
- group: operate
  title: ''
  type: Support
  url: https://help.justbeepit.com/
- group: company
  title: ''
  type: Blog
  url: https://www.justbeepit.com/blog
- group: operate
  title: ''
  type: Roadmap
  url: https://www.justbeepit.com/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.justbeepit.com/privacypolicy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.justbeepit.com/eusa-terms-of-use
- group: agent
  title: ''
  type: MCPServer
  url: mcp/beep-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/beep-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/beep-domain-security.yml
created: '2026-07-17'
description: Beep (Just Beep It!) is a visual feedback and web collaboration platform that helps teams review live websites, report bugs, run user testing, and collect ideas directly on the page. Delivered primarily as a browser extension, it lets users annotate any web page, leave comments, attach files, and record their screen so feedback moves faster and projects ship sooner. The product targets agencies, product teams, and builders, offers a free tier plus a paid SuperBeeper plan and enterprise pricing, and is built on Wix. It exposes no bespoke developer REST API, but its Wix-powered site publishes an llms.txt and a public Wix Site MCP endpoint for agentic AI access. Surfaced as a portfolio company of 500 Global and added to the API Evangelist network.
image: https://static.wixstatic.com/media/40f9cb_6f4f76340b2b4f9d93a0e87d1d6913d6~mv2.png/v1/fill/w_1152,h_648,al_c/40f9cb_6f4f76340b2b4f9d93a0e87d1d6913d6~mv2.png
layout: provider
mcp_servers:
- description: ''
  name: beep-mcp.yml
  slug: beep-mcpyml
modified: '2026-07-18'
name: Beep
nav: Providers
network: true
overview: 'Beep is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Collaboration, Feedback, Bug Reporting, and Website Review.


  Beep''s developer surface includes pricing, signup flow, support, engineering blog, and 8 more developer resources.'
random_paper: 64
score:
  band: emerging
  composite: 18.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 0.0
    developer_ergonomics: 15.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.4
  provenance:
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/beep/refs/heads/main/screenshots/beep-2026-07-25T202635.png
security:
- kind: domain-security
  name: Beep Domain Security
  slug: beep-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: beep
tags:
- Company
- Collaboration
- Feedback
- Bug Reporting
- Website Review
- Productivity
- Browser Extension
- MCP
website: https://justbeepit.com
---
