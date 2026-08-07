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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 42.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Wideo Agentic Access
  operation_count: 4
  slug: wideo-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: Legacy variable replace and single-video encode flow
  name: Wideo Automation API
  slug: wideo-automation-api
- description: Batch video rendering from a template and a set of variable objects
  name: Wideo Batch API
  slug: wideo-batch-api
artifact_total: 7
asyncapis:
- description: ''
  name: Wideo Events Asyncapi
  slug: wideo-events-asyncapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wideo-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wideo-conventions.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/wideo-events-asyncapi.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wideo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wideo-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/wideo-automation-overlay.yaml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wideo-well-known.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/wideo-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wideo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wideo-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wideo.co
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wideo.co/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://wideo.co/api-documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://wideo.co/api-documentation/
- group: commercial
  title: ''
  type: Pricing
  url: https://wideo.co/pricing-guide/
- group: company
  title: ''
  type: Blog
  url: https://wideo.co/blog/
- group: operate
  title: ''
  type: Support
  url: https://help.wideo.co/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.wideo.co/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://app.wideo.co/en/createAccount/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wideo.co/terms-and-conditions-wideo/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wideo.co/wideo-privacy-policy/
created: '2026-07-17'
description: 'Wideo is an online video creation and automation platform that lets teams produce animated videos, presentations, and marketing content from drag-and-drop templates and AI tools. For developers, Wideo publishes a Video Automation API that renders finished MP4 videos at scale: a rendering batch is created from a reusable template plus a list of per-video variable objects, rendering runs asynchronously, and completion is delivered via a webhook callback and pollable batch status returning signed video and preview URLs. A legacy replace/encode flow supports single-video generation. Wideo also offers a white-label video API for embedding video creation into other products. Wideo was surfaced as a portfolio company of 500 Global.'
image: https://wideo.co
layout: provider
mcp_servers:
- description: ''
  name: wideo-mcp.yml
  slug: wideo-mcpyml
modified: '2026-07-21'
name: Wideo
nav: Providers
network: true
overview: 'Wideo publishes 2 APIs on the [APIs.io](https://apis.io/) network: Automation API and Batch API. Tagged areas include Company, Video, Video Automation, Content Creation, and Media.


  The Wideo catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Wideo''s developer surface includes authentication, documentation, API reference, pricing, engineering blog, support, signup flow, and 15 more developer resources.'
random_paper: 84
score:
  band: developing
  composite: 46.9
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 72.9
    developer_ergonomics: 45.1
    discoverability: 87.0
    governance: 8.3
    operational_transparency: 7.9
  previous_composite: 46.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Wideo Authentication
  slug: wideo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wideo Domain Security
  slug: wideo-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wideo
tags:
- Company
- Video
- Video Automation
- Content Creation
- Media
- Marketing
- Templates
- No-Code
website: https://wideo.co
---
