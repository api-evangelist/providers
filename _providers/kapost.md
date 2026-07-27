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
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 15.4
  scored_at: '2026-07-27'
api_count: 1
apis:
- description: Versioned REST Content API for managing content, collections, ideas, initiatives, custom fields, tasks, users, and insights. HTTP Basic auth with a per-user API token (password ignored); JSON response
  name: Kapost Content API
  slug: kapost-content-api
artifact_total: 4
asyncapis:
- description: ''
  name: Kapost Webhooks
  slug: kapost-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://kapost.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.kapost.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.kapost.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.kapost.com/content-api-responses
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.kapost.com/api-getting-started
- group: start
  title: ''
  type: Login
  url: https://app.kapost.com/users/sign_in
- group: operate
  title: ''
  type: Support
  url: https://support.uplandsoftware.com/portal/ss/login
- group: company
  title: ''
  type: Blog
  url: https://uplandsoftware.com/kapost/resources/blog/
- group: auth
  title: ''
  type: Authentication
  url: authentication/kapost-authentication.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/kapost-webhooks.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kapost-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/kapost-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kapost-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kapost-llms.txt
created: '2026-07-17'
description: Kapost is a content operations platform — now part of Upland Software — that lets B2B marketing teams plan, produce, distribute, and analyze content across the customer journey through its Canvas, Studio, Gallery, and Insights modules. Kapost exposes a versioned REST Content API (/api/v1) secured with HTTP Basic authentication using a per-user API token and returning JSON, plus outbound content webhooks (create/update/publish/delete), an XML-RPC interface, and a first-party WordPress plugin for publishing content from Kapost to WordPress sites. This profile was enriched from Kapost's live developer portal.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kapost.png
layout: provider
modified: '2026-07-19'
name: Kapost
nav: Providers
network: true
overview: 'Kapost publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Content Operations, Content Marketing, Content Management, Marketing, and Sales Enablement.


  The Kapost catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Kapost''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, authentication, and 8 more developer resources.'
random_paper: 46
score:
  band: emerging
  composite: 29.0
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 22.6
    developer_ergonomics: 52.2
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 29.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kapost/refs/heads/main/screenshots/kapost-2026-07-25T223456.png
security:
- kind: authentication
  name: Kapost Authentication
  slug: kapost-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kapost Domain Security
  slug: kapost-domain-security
  summary_line: TLSv1.2
slug: kapost
tags:
- Content Operations
- Content Marketing
- Content Management
- Marketing
- Sales Enablement
- Webhooks
- REST API
- B2B
- Upland Software
website: https://kapost.com/
---
