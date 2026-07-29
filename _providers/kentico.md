---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: Auto-generated GraphQL API endpoint for each headless channel in Xperience by Kentico. Supports querying content items with filtering, sorting, pagination, linked items, language variants, taxonomy ta
  name: Kentico Headless GraphQL API
  slug: kentico-headless-graphql-api
- description: Built-in REST service for reading, creating, updating, and deleting pages and CMS objects within Xperience by Kentico. Requests use HTTP Basic authentication with Base64-encoded credentials or hash pa
  name: Kentico Management REST API
  slug: kentico-management-rest-api
- description: Server-side .NET API for content item queries, object queries, file system operations, and database access within Xperience by Kentico applications. Includes ContentRetriever API, ObjectQuery API, Fil
  name: Kentico .NET Content API
  slug: kentico-dotnet-content-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/kentico-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kentico-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kentico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kentico.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.kentico.com/documentation/developers-and-admins/api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Kentico
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kenticosoftware
- group: company
  title: ''
  type: Blog
  url: https://www.kentico.com/discover/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kentico.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.xperience-portal.com
- group: other
  title: ''
  type: X
  url: https://x.com/kentico
- group: commercial
  title: ''
  type: Plans
  url: plans/kentico-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kentico-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kentico-finops.yml
created: '2026-06-13'
description: Kentico is an enterprise .NET CMS and digital experience platform offering REST and GraphQL APIs for managing web content, e-commerce, digital marketing, and personalization. Xperience by Kentico provides headless channel GraphQL endpoints auto-generated per channel, a content item .NET API, file storage APIs supporting Azure Blob and Amazon S3, and a management REST service for CRUD operations on CMS objects. The platform supports ASP.NET Core with channel-based licensing covering website, email, and headless channels.
finops:
- name: Kentico Finops
  service_category: ''
  slug: kentico-finops
graphqls:
- description: Xperience by Kentico provides a per-channel headless GraphQL API whose schema is **auto-generated** at runtime from the content types configured in each headless channel. There is no single static sch
  name: Kentico Xperience GraphQL API
  slug: kentico-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kentico.png
layout: provider
modified: '2026-06-13'
name: Kentico
nav: Providers
network: true
overview: 'Kentico publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, Digital Experience Platform, GraphQL, and REST.


  Kentico''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Kentico Plans Pricing
  plan_count: 5
  slug: kentico-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Kentico Rate Limits
  slug: kentico-rate-limits
score:
  band: thin
  composite: 34.4
  delta: 7.9
  facets:
    commercial_clarity: 57.9
    contract_quality: 42.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 26.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/kentico/refs/heads/main/screenshots/kentico-2026-06-20T183955.png
security:
- kind: domain-security
  name: Kentico Domain Security
  slug: kentico-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Kentico Vulnerability Disclosure
  slug: kentico-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kentico Trust Center
  slug: kentico-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kentico
tags:
- CMS
- Content Management
- Digital Experience Platform
- GraphQL
- REST
- .NET
- Headless
- E-commerce
- Digital Marketing
- Personalization
website: https://www.kentico.com
---
