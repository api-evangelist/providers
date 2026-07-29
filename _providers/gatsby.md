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
  band: human-only
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
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Local, build-time GraphQL data layer exposed by the Gatsby framework to query content sourced from plugins (CMSs, filesystem, APIs). This is not a hosted public API; it runs inside a developer's Gatsb
  name: Gatsby GraphQL Data Layer
  slug: graphql-data-layer
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gatsby-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gatsbyjs
- group: company
  title: ''
  type: Website
  url: https://www.gatsbyjs.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.gatsbyjs.com/docs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gatsbyjs
- group: other
  title: ''
  type: Netlify (Successor Hosting)
  url: https://www.netlify.com/gatsby/
- group: operate
  title: ''
  type: Community
  url: https://www.gatsbyjs.com/contributing/community/
created: '2026-05-11'
description: Gatsby is an open-source, React-based framework for building fast, secure, content-driven websites and applications using GraphQL data sourcing, static site generation (SSG), server-side rendering (SSR), and deferred static generation (DSG). Gatsby is now stewarded by Netlify, which acquired the company in 2023 and sunset the hosted Gatsby Cloud build and preview service, migrating customers to Netlify's unified platform. Gatsby itself is a build-time framework and does not expose a public hosted REST API; integrations are performed locally through its GraphQL data layer and plugin ecosystem.
graphqls:
- description: Local, build-time GraphQL data layer exposed by the Gatsby framework to query content sourced from plugins (CMSs, filesystem, APIs). This is not a hosted public API; it runs inside a developer's Gatsb
  name: Gatsby GraphQL API
  slug: gatsby-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gatsby.png
layout: provider
modified: '2026-05-11'
name: Gatsby
nav: Providers
network: true
overview: 'Gatsby publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Static Site Generator, JAMstack, React, GraphQL, and Build Tool.


  Gatsby''s developer surface includes documentation and 6 more developer resources.'
random_paper: 34
score:
  band: minimal
  composite: 10.1
  delta: -2.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 12.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gatsby/refs/heads/main/screenshots/gatsby-2026-06-20T181654.png
security:
- kind: domain-security
  name: Gatsby Domain Security
  slug: gatsby-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gatsby
tags:
- Static Site Generator
- JAMstack
- React
- GraphQL
- Build Tool
- Frontend Framework
- Web Development
website: https://www.gatsbyjs.com
---
