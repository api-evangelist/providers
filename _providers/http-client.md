---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: JetBrains HTTP Client lets developers compose, edit, and execute HTTP, gRPC, WebSocket, and GraphQL requests directly within IntelliJ-based IDEs using .http and .rest files, with environment variables
  name: HTTP Client
  slug: http-client
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/http-client-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/http-client-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
- group: docs
  title: ''
  type: Documentation
  url: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JetBrains
- group: other
  title: ''
  type: Company
  url: https://www.jetbrains.com
- group: company
  title: ''
  type: Blog
  url: https://blog.jetbrains.com/idea/feed/
created: '2026-03-27'
description: HTTP Client is JetBrains' built-in tool for creating, editing, and executing HTTP requests directly from the IDE. Requests are stored in .http and .rest files alongside source code, with code highlighting, completion for hosts and methods, code folding, inline documentation, and live templates accelerating composition. The client supports HTTP/1.1 and HTTP/2 requests, gRPC unary and server-streaming calls, WebSocket connections, GraphQL operations, server-sent events, and imports from cURL and Postman collections. Environment files define reusable variables across global, request, and secured scopes; the cookie jar, request history, run/debug configurations, and Services tool window response viewer round out a workflow tightly integrated with the IntelliJ-based IDE family.
finops:
- name: Http Client Finops
  service_category: API
  slug: http-client-finops
graphqls:
- description: ''
  name: HTTP Client GraphQL API
  slug: http-client-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/http-client.png
layout: provider
modified: '2026-04-28'
name: HTTP Client
nav: Providers
network: true
overview: 'HTTP Client publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, Clients, Developer Tools, HTTP Client, and IDE Extension.


  HTTP Client''s developer surface includes documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Http Client Plans Pricing
  plan_count: 3
  slug: http-client-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 5
  name: Http Client Rate Limits
  slug: http-client-rate-limits
score:
  band: emerging
  composite: 22.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 80.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 22.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/http-client/refs/heads/main/screenshots/http-client-2026-06-20T182910.png
security:
- kind: domain-security
  name: Http Client Domain Security
  slug: http-client-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Http Client Vulnerability Disclosure
  slug: http-client-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: http-client
tags:
- API Testing
- Clients
- Developer Tools
- HTTP Client
- IDE Extension
- IntelliJ
- JetBrains
- REST Client
website: https://www.jetbrains.com/help/idea/http-client-in-product-code-editor.html
---
