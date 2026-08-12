---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-11'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Kontent Ai Agentic Access
  operation_count: 5
  slug: kontent-ai-agentic-access
  summary_line: 5 operations
api_count: 9
apis:
- description: Read-only REST API for retrieving published content and previewing the latest content from a Kontent.ai environment.
  name: Kontent.ai Delivery REST API
  slug: delivery-api
- description: GraphQL API providing the same content delivery capabilities as the Delivery REST API with GraphQL query semantics.
  name: Kontent.ai Delivery GraphQL API
  slug: delivery-graphql-api
- description: API for transforming and optimizing images served via the Delivery API, including resizing, cropping, and format conversion.
  name: Kontent.ai Image Transformation API
  slug: image-transformation-api
- description: REST API for managing content, content models, taxonomy, assets, and environment settings programmatically.
  name: Kontent.ai Management API v2
  slug: management-api-v2
- description: Read-only REST API for checking recent content item changes and keeping consuming applications synchronized with content updates.
  name: Kontent.ai Sync API v2
  slug: sync-api
- description: REST API for managing users, projects, and environments within a Kontent.ai subscription.
  name: Kontent.ai Subscription API
  slug: subscription-api
- description: The Assets API from Kontent AI — 1 operation(s) for assets.
  name: Kontent AI Assets API
  slug: kontent-ai-assets-api
- description: The Items API from Kontent AI — 3 operation(s) for items.
  name: Kontent AI Items API
  slug: kontent-ai-items-api
- description: The Items Feed API from Kontent AI — 1 operation(s) for items feed.
  name: Kontent AI Items Feed API
  slug: kontent-ai-items-feed-api
artifact_total: 18
collections:
- collection_type: open
  name: Kontent.ai Delivery API
  slug: open-kontent-ai
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/kontent-ai-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kontent-ai-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kontent-ai-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/kontent-ai-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/kontent-ai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kontentai
- group: company
  title: ''
  type: Website
  url: https://kontent.ai
- group: docs
  title: ''
  type: Documentation
  url: https://kontent.ai/learn/docs
- group: docs
  title: ''
  type: APIReference
  url: https://kontent.ai/learn/docs/apis
- group: agent
  title: ''
  type: LlmsText
  url: https://kontent.ai/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://kontentai.com/rss
created: '2025-01-08'
description: Kontent.ai is a headless content management system providing REST and GraphQL APIs for delivering, managing, and synchronizing content across digital channels, plus image transformation and subscription management.
finops:
- name: Kontent Ai Finops
  service_category: API
  slug: kontent-ai-finops
graphqls:
- description: GraphQL API providing the same content delivery capabilities as the Delivery REST API with GraphQL query semantics.
  name: Kontent AI GraphQL API
  slug: kontent-ai-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kontent-ai.png
layout: provider
modified: '2026-04-28'
name: Kontent AI
nav: Providers
network: true
overview: 'Kontent AI publishes 3 APIs on the [APIs.io](https://apis.io/) network: Assets API, Items API, and Items Feed API. Tagged areas include CMS, Content, GraphQL, and Headless CMS.


  Kontent AI''s developer surface includes authentication, documentation, API reference, engineering blog, and 7 more developer resources.'
plans:
- name: Kontent Ai Plans Pricing
  plan_count: 3
  slug: kontent-ai-plans-pricing
random_paper: 90
rate_limits:
- limit_count: 5
  name: Kontent Ai Rate Limits
  slug: kontent-ai-rate-limits
score:
  band: thin
  composite: 30.5
  delta: -7.6
  facets:
    commercial_clarity: 15.8
    contract_quality: 54.5
    developer_ergonomics: 28.3
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 13.2
  previous_composite: 38.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/kontent-ai/refs/heads/main/screenshots/kontent-ai-2026-06-20T184133.png
security:
- kind: authentication
  name: Kontent Ai Authentication
  slug: kontent-ai-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Kontent Ai Domain Security
  slug: kontent-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kontent Ai Vulnerability Disclosure
  slug: kontent-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kontent-ai
tags:
- CMS
- Content
- GraphQL
- Headless CMS
website: https://kontent.ai
---
