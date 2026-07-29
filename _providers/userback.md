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
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Userback Agentic Access
  operation_count: 8
  slug: userback-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 4
apis:
- description: REST API for managing Userback feedback items, projects, users, tags, and account resources. Uses Bearer token authentication; partner integrations use an X-Partner-Code header.
  name: Userback REST API
  slug: rest-api
- description: Feedback items captured by Userback widgets.
  name: Userback Feedback API
  slug: userback-feedback-api
- description: Comments attached to feedback items.
  name: Userback Feedback Comments API
  slug: userback-feedback-comments-api
- description: Userback projects (workspaces grouping feedback widgets).
  name: Userback Projects API
  slug: userback-projects-api
artifact_total: 8
collections:
- collection_type: open
  name: Userback REST API
  slug: open-userback
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/userback-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/userback-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/userback-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/userback
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/userback
- group: company
  title: ''
  type: Website
  url: https://www.userback.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.userback.io
- group: commercial
  title: ''
  type: Pricing
  url: https://www.userback.io/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.userback.io/signup
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.userback.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.userback.io/blog
created: '2026-05-11'
description: Userback is a customer feedback platform that captures visual feedback, screenshots, screen recordings, and bug reports directly from in-product widgets installed on websites and web applications. The platform offers feedback boards, session replays, and integrations with project management and developer tools to streamline customer-driven product development. Userback's REST API uses Bearer token authentication for managing feedback, projects, users, and account data.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/userback.png
layout: provider
modified: '2026-05-11'
name: Userback
nav: Providers
network: true
overview: 'Userback publishes 3 APIs on the [APIs.io](https://apis.io/) network: Feedback API, Feedback Comments API, and Projects API. Tagged areas include Customer Feedback, Bug Reporting, Visual Feedback, Session Replay, and Product Management.


  Userback''s developer surface includes authentication, documentation, pricing, signup flow, engineering blog, and 6 more developer resources.'
random_paper: 38
score:
  band: thin
  composite: 30.0
  delta: -2.2
  facets:
    commercial_clarity: 10.5
    contract_quality: 61.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/userback/refs/heads/main/screenshots/userback-2026-06-20T200723.png
security:
- kind: authentication
  name: Userback Authentication
  slug: userback-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Userback Domain Security
  slug: userback-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: userback
tags:
- Customer Feedback
- Bug Reporting
- Visual Feedback
- Session Replay
- Product Management
- SaaS
website: https://www.userback.io
---
