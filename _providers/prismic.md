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
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: The Prismic GraphQL API is a read-only endpoint that allows developers to perform deep and selective fetching of content documents from a Prismic repository. Each repository exposes its own GraphQL en
  name: Prismic GraphQL API
  slug: graphql-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/prismic-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/prismic-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prismic-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://prismic.io/blog
- group: company
  title: ''
  type: Website
  url: https://prismic.io
- group: docs
  title: ''
  type: Documentation
  url: https://prismic.io/docs/graphql-technical-reference
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prismic-io
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prismicio
- group: commercial
  title: ''
  type: Pricing
  url: https://prismic.io/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/prismic-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prismic-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/prismic-finops.md
created: 2026-06-14
description: Prismic is a headless CMS and page builder that empowers marketing teams to create and manage website content independently while developers work in their preferred tech stack. It provides a GraphQL API and REST Content API for fetching structured content from Prismic repositories, enabling fast, CDN-backed delivery for modern web applications.
graphqls:
- description: The Prismic GraphQL API is a read-only endpoint that exposes structured content stored in a Prismic repository. It supports deep and selective content fetching, cursor-based pagination, filtering, and
  name: Prismic GraphQL API
  slug: prismic-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prismic.png
layout: provider
modified: 2026-06-14
name: Prismic
nav: Providers
network: true
overview: 'Prismic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, Headless CMS, Content Management, Page Builder, and JAMstack.


  Prismic''s developer surface includes engineering blog, documentation, pricing, and 9 more developer resources.'
random_paper: 39
score:
  band: emerging
  composite: 26.2
  delta: 0.0
  facets:
    commercial_clarity: 18.4
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 26.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prismic/refs/heads/main/screenshots/prismic-2026-06-20T192117.png
security:
- kind: domain-security
  name: Prismic Domain Security
  slug: prismic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Prismic Vulnerability Disclosure
  slug: prismic-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Prismic Trust Center
  slug: prismic-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, GDPR, CSA STAR
slug: prismic
tags:
- GraphQL
- Headless CMS
- Content Management
- Page Builder
- JAMstack
- Marketing
website: https://prismic.io
---
