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
api_count: 2
apis:
- description: Command-based REST API for managing Fibery workspace entities, databases, views, files, and automation via a single POST endpoint that accepts batches of commands.
  name: Fibery HTTP API
  slug: fibery-http-api
- description: GraphQL API for querying and mutating Fibery workspace data, with an interactive IDE for schema exploration, and support for filtering, pagination, and nested entity operations.
  name: Fibery GraphQL API
  slug: fibery-graphql-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/fibery-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fibery-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fibery.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.fibery.com
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Fibery-inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fibery
- group: company
  title: ''
  type: Blog
  url: https://fibery.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://fibery.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fibery.io
- group: other
  title: ''
  type: X
  url: https://x.com/fibery_io
- group: commercial
  title: ''
  type: Plans
  url: plans/fibery-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/fibery-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/fibery-finops.yml
created: '2026-06-13'
description: Fibery is a connected work management platform with a REST API and GraphQL API for managing entities, databases, automation rules, collaborative documents, and custom workflow views. It supports webhooks, file uploads, rich text operations, and real-time change history for building integrations and automating workflows.
finops:
- name: Fibery Finops
  service_category: ''
  slug: fibery-finops
graphqls:
- description: 'The Fibery GraphQL API provides a flexible interface for reading and mutating data in your Fibery workspace. The schema is dynamically generated from your workspace structure: every Database you creat'
  name: Fibery GraphQL API
  slug: fibery-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fibery.png
layout: provider
modified: '2026-06-13'
name: Fibery
nav: Providers
network: true
overview: 'Fibery publishes 1 API on the [APIs.io](https://apis.io/) network: HTTP API. Tagged areas include Work Management, Project Management, Collaboration, No-Code, and Automation.


  Fibery''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Fibery Plans Pricing
  plan_count: 4
  slug: fibery-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fibery Rate Limits
  slug: fibery-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 0.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fibery/refs/heads/main/screenshots/fibery-2026-06-20T181149.png
security:
- kind: domain-security
  name: Fibery Domain Security
  slug: fibery-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: trust-center
  name: Fibery Trust Center
  slug: fibery-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: fibery
tags:
- Work Management
- Project Management
- Collaboration
- No-Code
- Automation
- GraphQL
- Webhooks
website: https://fibery.com
---
