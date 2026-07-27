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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 5.8
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: 'Public REST API for the Favro planning and collaboration platform: manage organizations, collections, widgets, columns, cards, tasks, tasklists, comments, tags, custom fields, groups, users, and webho'
  name: Favro API
  slug: favro-api
artifact_total: 6
asyncapis:
- description: ''
  name: Favro Webhooks
  slug: favro-webhooks
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/favro-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://www.favro.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://favro.com/developer
- group: docs
  title: ''
  type: Documentation
  url: https://favro.com/developer
- group: company
  title: ''
  type: Blog
  url: https://www.favro.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.favro.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://favro.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.favro.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://help.favro.com/en/articles/1024895-favro-s-terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://help.favro.com/en/articles/1019861-favro-s-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.favro.com
- group: auth
  title: ''
  type: Security
  url: https://www.favro.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://www.favro.com/security
- group: auth
  title: ''
  type: DomainSecurity
  url: security/favro-domain-security.yml
created: '2026-07-17'
description: Favro is a cloud planning and collaboration platform for agile teams, combining planning boards, backlogs, sprint/kanban widgets, roadmaps, and OKR/portfolio management in a single organization-scoped workspace. Its public REST API (https://favro.com/api/v1) exposes organizations, collections, widgets, columns, cards, tasks, tasklists, comments, tags, custom fields, groups, users, and webhooks, authenticated with HTTP Basic auth using an email plus a revocable API token. The API supports request-id cursor pagination, per-plan token-bucket rate limiting with X-RateLimit-* headers, backend-affinity routing via the X-Favro-Backend-Identifier header, outbound webhooks for card and comment events, and SCIM 1.1/2.0 user and group provisioning. Favro is SaaS, backed by Creandum.
image: https://cdn.prod.website-files.com/5eb8d3f3c300199312debf24/6036cf2c15bbbca169cec61a_meta2.png
layout: provider
mcp_servers:
- description: ''
  name: favro-mcp.yml
  slug: favro-mcpyml
modified: '2026-07-19'
name: Favro
nav: Providers
network: true
overview: 'Favro publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Saas, Project Management, Collaboration, and Agile.


  The Favro catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Favro''s developer surface includes documentation, engineering blog, pricing, signup flow, support, and 9 more developer resources.'
random_paper: 66
score:
  band: thin
  composite: 35.2
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 22.6
    developer_ergonomics: 23.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 35.2
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/favro/refs/heads/main/screenshots/favro-2026-07-25T214254.png
security:
- kind: authentication
  name: Favro Authentication
  slug: favro-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Favro Domain Security
  slug: favro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Favro Trust Center
  slug: favro-trust-center
  summary_line: ISO 27001, PCI DSS
slug: favro
tags:
- Company
- Saas
- Project Management
- Collaboration
- Agile
- Planning
- Task Management
- Kanban
- Productivity
website: https://www.favro.com/
---
