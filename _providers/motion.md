---
access_model:
  confidence: high
  label: Trial with sales-assisted onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://motionapp.com/pricing
  - https://help.motionapp.com/en/articles/14315735-motion-mcp
  trial: true
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.3
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Motion's official hosted remote MCP server. Read-only, OAuth 2.0 gated, and documented with 13 tools across six categories — auth context, creative performance (ranked creatives, AI creative summaries
  name: Motion MCP
  slug: motion-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://motionapp.com
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/motion-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/motion-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/motion-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/motion-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/motion-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/motion-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/motion-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/motion-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/motion-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/motion-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/motion-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.motionapp.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/motion-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: Documentation
  url: https://help.motionapp.com/
- group: docs
  title: ''
  type: APIReference
  url: https://help.motionapp.com/en/articles/14315735-motion-mcp
- group: company
  title: ''
  type: Blog
  url: https://motionapp.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.motionapp.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://motionapp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://projects.motionapp.com/signup
- group: start
  title: ''
  type: Login
  url: https://projects.motionapp.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://motionapp.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://motionapp.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://motionapp.com/releases
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/motion-changelog.yml
- group: operate
  title: ''
  type: FAQ
  url: https://motionapp.com/faq
- group: other
  title: ''
  type: Glossary
  url: https://motionapp.com/glossary
created: '2026-07-17'
description: Motion is a creative analytics platform for performance marketing and creative teams, headquartered in Toronto and founded in 2021 by Reza Khadjavi, Alexander Sloan, and David Berglas. Motion connects a brand's Meta, TikTok, YouTube, and LinkedIn ad accounts — plus Google Analytics 4 and Northbeam attribution — into a single command center where marketers and agencies identify which creative elements drive performance, run comparative and launch analysis, auto-tag ads with AI across multiple dimensions, and research competitor ads via its Inspo tool. The company also offers Runneth by Motion, an AI layer for marketing. Motion serves 2,100+ teams analyzing over $14B in annual ad spend and is backed by Threshold Ventures, Inovia Capital, Headline, Abstract Ventures, and Sugar Capital. Motion publishes no REST API, OpenAPI, GraphQL endpoint or webhook surface; its one machine-callable product is the Motion MCP server at https://projects.motionapp.com/mcp, a read-only OAuth 2.0
  Model Context Protocol server exposing 13 documented tools over creative performance, video transcripts, AI tags, demographics, saved reports and the Inspo competitor ad library to Claude, ChatGPT, Cursor and any MCP client.
image: https://cdn.prod.website-files.com/61ba3b439a672312697272c7/68e427f46591f0bafce36ab7_motion_meta_2025.jpg
layout: provider
mcp_servers:
- description: Motion's official hosted, remote MCP server. It exposes Motion Creative Analytics — ad creative performance, AI-generated creative summaries and video transcripts, demographic breakdowns, workspace br
  name: Motion MCP
  slug: motion-mcp
modified: '2026-08-12'
name: Motion
nav: Providers
network: true
overview: 'Motion publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creative Analytics, Advertising, Marketing Analytics, and Performance Marketing.


  Motion''s developer surface includes authentication, documentation, API reference, engineering blog, support, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Motion Plans Pricing
  plan_count: 4
  slug: motion-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Motion Rate Limits
  slug: motion-rate-limits
scopes:
- name: Motion Scopes
  scope_count: 11
  slug: motion-scopes
  summary_line: 11 scopes
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 17
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 31.6
  previous_composite: 35.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/motion/refs/heads/main/screenshots/motion-2026-08-07T184326.png
security:
- kind: authentication
  name: Motion Authentication
  slug: motion-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Motion Domain Security
  slug: motion-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: motion
tags:
- Company
- Creative Analytics
- Advertising
- Marketing Analytics
- Performance Marketing
- Ad Reporting
- Creative Strategy
- Software-as-a-Service
- MCP
- Agent Surface
website: https://motionapp.com
---
