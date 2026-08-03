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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: A GraphQL API generated from your TinaCMS schema that serves Markdown and JSON content stored in Git repositories. Available locally via the tinacms dev CLI (localhost:4001) or hosted via TinaCloud wi
  name: TinaCMS GraphQL Content API
  slug: graphql-content-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tinacms-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tinacms-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tina.io
- group: docs
  title: ''
  type: Documentation
  url: https://tina.io/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tinacms
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/tinacms
- group: company
  title: ''
  type: Blog
  url: https://tina.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tina.io/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/tinacms
- group: commercial
  title: ''
  type: Plans
  url: plans/tinacms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tinacms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/tinacms-finops.yml
created: '2026-06-13'
description: TinaCMS is an open-source, Git-backed headless CMS that provides a GraphQL Content API for managing Markdown, MDX, and JSON content stored in Git repositories. It enables real-time visual editing for Next.js, Astro, and other frameworks, with TinaCloud offering a hosted Data Layer that indexes and serves content via per-project GraphQL endpoints with editorial workflow, media management, and authentication support.
finops:
- name: Tinacms Finops
  service_category: ''
  slug: tinacms-finops
graphqls:
- description: TinaCMS generates a GraphQL Content API from your schema definitions in `tina/config.ts`. The API exposes every content collection you define as both single-document queries (`<collection>(relativePat
  name: TinaCMS GraphQL API
  slug: tinacms-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tinacms.png
layout: provider
modified: '2026-06-13'
name: TinaCMS
nav: Providers
network: true
overview: 'TinaCMS publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL Content API. Tagged areas include CMS, Headless CMS, GraphQL, Git, and Content Management.


  TinaCMS''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Tinacms Plans Pricing
  plan_count: 5
  slug: tinacms-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 3
  name: Tinacms Rate Limits
  slug: tinacms-rate-limits
score:
  band: thin
  composite: 34.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 42.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 34.3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tinacms/refs/heads/main/screenshots/tinacms-2026-06-20T195408.png
security:
- kind: domain-security
  name: Tinacms Domain Security
  slug: tinacms-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tinacms Vulnerability Disclosure
  slug: tinacms-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: tinacms
tags:
- CMS
- Headless CMS
- GraphQL
- Git
- Content Management
- Visual Editing
- Markdown
- Open Source
website: https://tina.io
---
