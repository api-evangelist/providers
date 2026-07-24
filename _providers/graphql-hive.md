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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 24.0
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: The public GraphQL API for Hive Console allows developers to build custom workflows, administer users and access tokens, retrieve usage metrics, manage schema registries, publish schemas, validate com
  name: GraphQL Hive Console GraphQL API
  slug: graphql-hive-graphql-api
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/graphql-hive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://the-guild.dev/graphql/hive
- group: docs
  title: ''
  type: Documentation
  url: https://the-guild.dev/graphql/hive/docs
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/graphql-hive
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/the-guild-software
- group: company
  title: ''
  type: Blog
  url: https://the-guild.dev/graphql/hive/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://the-guild.dev/graphql/hive/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graphql-hive.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TheGuildDev
- group: commercial
  title: ''
  type: Plans
  url: plans/graphql-hive-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/graphql-hive-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/graphql-hive-finops.yml
created: '2026-06-13'
description: GraphQL Hive is an open-source GraphQL schema registry and observability platform developed by The Guild. It provides a REST and GraphQL API for schema publishing, validation, usage tracking, breaking change detection, and analytics for GraphQL federation and other GraphQL APIs. Available as a managed cloud service or self-hosted deployment.
finops:
- name: Graphql Hive Finops
  service_category: ''
  slug: graphql-hive-finops
graphqls:
- description: GraphQL Hive exposes a public GraphQL API for programmatic management of organizations, projects, targets, and schema registries. Developers use this API to automate schema publishing workflows, retri
  name: GraphQL Hive GraphQL API
  slug: graphql-hive-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/graphql-hive.png
json_schemas:
- name: Report
  property_count: 4
  slug: graphql-hive-usage-report-v2
jsonld:
- class_count: 40
  name: Graphql Hive Context
  property_count: 11
  slug: graphql-hive-context
layout: provider
modified: '2026-06-13'
name: GraphQL Hive
nav: Providers
network: true
overview: 'GraphQL Hive publishes 1 API on the [APIs.io](https://apis.io/) network: Console GraphQL API. Tagged areas include GraphQL, Schema Registry, API Observability, Breaking Change Detection, and Federation.


  The GraphQL Hive catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GraphQL Hive''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Graphql Hive Plans Pricing
  plan_count: 3
  slug: graphql-hive-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Graphql Hive Rate Limits
  slug: graphql-hive-rate-limits
rules:
- name: GraphQL Hive API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: graphql-hive-jsonschema-spectral-rules
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.5
    developer_ergonomics: 10.9
    discoverability: 92.5
    governance: 73.7
    operational_transparency: 52.6
  previous_composite: 51.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/graphql-hive/refs/heads/main/screenshots/graphql-hive-2026-06-20T182334.png
security:
- kind: domain-security
  name: Graphql Hive Domain Security
  slug: graphql-hive-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: graphql-hive
tags:
- GraphQL
- Schema Registry
- API Observability
- Breaking Change Detection
- Federation
- Open Source
- Developer Tools
website: https://the-guild.dev/graphql/hive
---
