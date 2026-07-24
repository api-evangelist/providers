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
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: 'Auto-generated GraphQL API providing schema-based access to Craft CMS content including entries, assets, categories, tags, and custom fields. Access is controlled via bearer token authentication tied '
  name: Craft CMS GraphQL API
  slug: graphql-api
- description: Official Craft CMS plugin that creates configurable JSON REST endpoints for any element type (entries, assets, categories, users). Endpoints are defined via a PHP configuration file mapping URL patter
  name: Craft CMS Element API
  slug: element-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/craft-cms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/craft-cms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://craftcms.com
- group: docs
  title: ''
  type: Documentation
  url: https://craftcms.com/docs/5.x/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/craftcms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/craftcms
- group: other
  title: ''
  type: X
  url: https://twitter.com/craftcms
- group: company
  title: ''
  type: Blog
  url: https://craftcms.com/blog
- group: company
  title: ''
  type: BlogFeed
  url: https://craftcms.com/blog.rss
- group: commercial
  title: ''
  type: Pricing
  url: https://craftcms.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.craftcms.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/craft-cms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/craft-cms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/craft-cms-finops.yml
- group: company
  title: ''
  type: Blog
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/craft-cms-context.jsonld
created: '2026-06-12'
description: Craft CMS is a flexible, self-hosted PHP content management system built on Yii 2, designed for creating bespoke digital experiences. It features an auto-generated GraphQL API for headless implementations, enabling queries against entries, assets, categories, and custom fields via token-based authentication. The Element API plugin extends Craft with configurable JSON REST endpoints for any element type, using URL pattern routing and the Fractal transformation library. Craft supports multi-site architecture, unlimited content types, and is deployable on-premise or via Craft Cloud, the official managed hosting platform.
finops:
- name: Craft Cms Finops
  service_category: Developer Tools
  slug: craft-cms-finops
graphqls:
- description: 'Craft CMS includes a built-in, auto-generated GraphQL API available since version 3.3. The schema exposes all content elements — entries, assets, categories, tags, global sets, users, and addresses — '
  name: Craft CMS GraphQL API
  slug: craft-cms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/craft-cms.png
jsonld:
- class_count: 24
  name: Craft Cms Context
  property_count: 0
  slug: craft-cms-context
layout: provider
modified: '2026-06-12'
name: Craft CMS
nav: Providers
network: true
overview: 'Craft CMS publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, GraphQL, REST, and Headless.


  The Craft CMS catalog on APIs.io includes 1 JSON-LD context.


  Craft CMS''s developer surface includes documentation, engineering blog, pricing, and 13 more developer resources.'
plans:
- name: Craft Cms Plans Pricing
  plan_count: 4
  slug: craft-cms-plans-pricing
random_paper: 29
rate_limits:
- limit_count: 2
  name: Craft Cms Rate Limits
  slug: craft-cms-rate-limits
score:
  band: thin
  composite: 30.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 15.1
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 30.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/craft-cms/refs/heads/main/screenshots/craft-cms-2026-06-20T175204.png
security:
- kind: domain-security
  name: Craft Cms Domain Security
  slug: craft-cms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Craft Cms Vulnerability Disclosure
  slug: craft-cms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: craft-cms
tags:
- CMS
- Content Management
- GraphQL
- REST
- Headless
- PHP
website: https://craftcms.com
---
