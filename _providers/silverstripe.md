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
  scored_at: '2026-07-23'
api_count: 2
apis:
- description: 'SilverStripe''s GraphQL API provides a content API layer for getting data in and out of the CMS. It supports schema generation from DataObject models, custom types and queries, and extensible schemas. '
  name: SilverStripe GraphQL API
  slug: graphql-api
- description: SilverStripe provides REST API capabilities via the restfulserver module, allowing CRUD operations on DataObject models over HTTP. Authentication supports API token headers (x-api-token) and session-b
  name: SilverStripe REST API
  slug: rest-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/silverstripe-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.silverstripe.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.silverstripe.org/
- group: docs
  title: ''
  type: APIReference
  url: https://api.silverstripe.org/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/silverstripe
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/silverstripe/
- group: company
  title: ''
  type: Blog
  url: https://www.silverstripe.org/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.silverstripe.org/software/
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/silverstripe/platform-status-page
- group: other
  title: ''
  type: X
  url: https://twitter.com/silverstripe
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.silverstripe.org/en/6/changelogs/
- group: commercial
  title: ''
  type: Plans
  url: plans/silverstripe-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/silverstripe-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/silverstripe-finops.yml
created: '2026-06-13'
description: SilverStripe is an open-source PHP content management system and framework with a GraphQL and REST API for managing pages, assets, versioning, and custom data objects. It powers 50,000+ live sites and provides a flexible, extensible platform for developers to build content-driven web applications with enterprise-level security and an intuitive editing experience.
finops:
- name: Silverstripe Finops
  service_category: ''
  slug: silverstripe-finops
graphqls:
- description: SilverStripe CMS provides a GraphQL API via the optional `silverstripe/graphql` module. The schema is code-generated at build time from DataObject models configured in YAML. Types, queries, and mutati
  name: SilverStripe GraphQL API
  slug: silverstripe-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/silverstripe.png
layout: provider
modified: '2026-06-13'
name: SilverStripe
nav: Providers
network: true
overview: 'SilverStripe publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include CMS, Content Management, GraphQL, REST API, and PHP.


  SilverStripe''s developer surface includes documentation, API reference, engineering blog, pricing, changelog, and 9 more developer resources.'
plans:
- name: Silverstripe Plans Pricing
  plan_count: 2
  slug: silverstripe-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 3
  name: Silverstripe Rate Limits
  slug: silverstripe-rate-limits
score:
  band: emerging
  composite: 29.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 17.4
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 68.4
  previous_composite: 29.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/silverstripe/refs/heads/main/screenshots/silverstripe-2026-06-20T193925.png
security:
- kind: domain-security
  name: Silverstripe Domain Security
  slug: silverstripe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: silverstripe
tags:
- CMS
- Content Management
- GraphQL
- REST API
- PHP
- Open Source
- Framework
- Pages
- Assets
- Versioning
website: https://www.silverstripe.org/
---
