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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Hypertune Agentic Access
  operation_count: 2
  slug: hypertune-agentic-access
  summary_line: 2 operations · 1 acting
api_count: 2
apis:
- description: Programmatic and Git-based management of flags, experiments, and configuration. Hypertune versions all flags, experiments, analytics events, and app configuration together in a single Git-based histor
  name: Hypertune Management API
  slug: hypertune-management-api
- description: The GraphQL API from Hypertune — 1 operation(s) for graphql.
  name: Hypertune GraphQL API
  slug: hypertune-graphql-api
artifact_total: 10
collections:
- collection_type: open
  name: Hypertune Edge API
  slug: open-hypertune
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/hypertune-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hypertune-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hypertune-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hypertunehq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hypertune
- group: company
  title: ''
  type: Website
  url: https://www.hypertune.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hypertune.com
- group: commercial
  title: ''
  type: Plans
  url: plans/hypertune-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hypertune-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hypertune-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.hypertune.com/blog
created: '2026-06-20'
description: Hypertune is a type-safe, Git-based platform for feature flags, A/B testing, experimentation, analytics, and app configuration. Flag logic is authored in Hyperlang and modeled as a GraphQL schema; SDKs use a CLI to generate fully typed clients, fetch flag logic once from Hypertune Edge (Cloudflare CDN) at initialization, then evaluate flags locally and synchronously in memory. A GraphQL Edge API offers a no-SDK path, and analytics events are flushed back to Hypertune Edge in the background.
finops:
- name: Hypertune Finops
  service_category: Developer Tools
  slug: hypertune-finops
graphqls:
- description: Conceptual, representative GraphQL schema for the [Hypertune](https://www.hypertune.com/)
  name: Hypertune GraphQL Schema
  slug: hypertune-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hypertune.png
layout: provider
modified: '2026-06-20'
name: Hypertune
nav: Providers
network: true
overview: 'Hypertune publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Feature Flags, Experimentation, A/B Testing, Analytics, and App Configuration.


  Hypertune''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Hypertune Plans Pricing
  plan_count: 4
  slug: hypertune-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Hypertune Rate Limits
  slug: hypertune-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 58.4
    developer_ergonomics: 21.7
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 37.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hypertune/refs/heads/main/screenshots/hypertune-2026-06-20T183051.png
security:
- kind: authentication
  name: Hypertune Authentication
  slug: hypertune-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Hypertune Domain Security
  slug: hypertune-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: hypertune
tags:
- Feature Flags
- Experimentation
- A/B Testing
- Analytics
- App Configuration
- GraphQL
- Edge
website: https://www.hypertune.com
---
