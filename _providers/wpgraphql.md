---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: Extendable GraphQL API for WordPress that exposes posts, pages, custom post types, users, menus, taxonomies, media, and settings as GraphQL types and connections. Supports queries, mutations, and subs
  name: WPGraphQL API
  slug: wpgraphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wpgraphql-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.wpgraphql.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.wpgraphql.com/docs/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wp-graphql
- group: company
  title: ''
  type: Blog
  url: https://www.wpgraphql.com/blog
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/in/jason-bahl/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wpgraphql.com/
- group: build
  title: ''
  type: WordPressPlugin
  url: https://wordpress.org/plugins/wp-graphql/
- group: other
  title: ''
  type: OpenCollective
  url: https://opencollective.com/wp-graphql
- group: commercial
  title: ''
  type: Plans
  url: plans/wpgraphql-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wpgraphql-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/wpgraphql-finops.md
created: '2026-06-14'
description: Open-source WordPress plugin that exposes a full-featured extendable GraphQL API for WordPress data including posts, pages, users, menus, taxonomies, media, and plugins. Created by Jason Bahl and now supported by Automattic as a Canonical Plugin, WPGraphQL enables headless WordPress development with modern JavaScript frameworks like Next.js, Svelte, and Astro. The plugin ships with a GraphiQL IDE in the WordPress dashboard and supports custom post types, ACF fields, WooCommerce, and dozens of extension plugins through a flexible schema registration system.
graphqls:
- description: 'WPGraphQL is an open-source WordPress plugin that adds a full-featured, extendable GraphQL API to any WordPress installation. It exposes WordPress content — including posts, pages, custom post types, '
  name: WPGraphQL GraphQL API
  slug: wpgraphql-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wpgraphql.png
layout: provider
modified: '2026-06-14'
name: WPGraphQL
nav: Providers
network: true
overview: 'WPGraphQL publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, WordPress, Headless CMS, Content Management, and Open Source.


  WPGraphQL''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
random_paper: 78
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 23.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wpgraphql/refs/heads/main/screenshots/wpgraphql-2026-06-20T201626.png
security:
- kind: domain-security
  name: Wpgraphql Domain Security
  slug: wpgraphql-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wpgraphql
tags:
- GraphQL
- WordPress
- Headless CMS
- Content Management
- Open Source
- Plugin
- Decoupled WordPress
website: https://www.wpgraphql.com/
---
