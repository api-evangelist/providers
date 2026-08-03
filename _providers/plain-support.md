---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Plain Support Agentic Access
  operation_count: 1
  slug: plain-support-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Plain — 1 operation(s) for graphql.
  name: Plain GraphQL API
  slug: plain-support-graphql-api
artifact_total: 9
collections:
- collection_type: open
  name: Plain GraphQL API
  slug: open-plain-support
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/plain-support-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plain-support-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/plain-support-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/team-plain
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/plain-support
- group: company
  title: ''
  type: Website
  url: https://www.plain.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.plain.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/plain-support-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/plain-support-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/plain-support-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.plain.com/blog
created: '2026-06-20'
description: Plain is an API-first customer support platform built around a single GraphQL API. Everything in the product - customers, threads, timeline entries, messages, labels, tiers, and webhooks - is exposed through the same GraphQL endpoint the Plain UI consumes, letting teams build support into their own products with threads, customer context, and a unified timeline.
finops:
- name: Plain Support Finops
  service_category: Customer Support and Engagement
  slug: plain-support-finops
graphqls:
- description: Representative GraphQL schema for the [Plain](https://www.plain.com/) API-first customer
  name: Plain GraphQL API
  slug: plain-support-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/plain-support.png
layout: provider
modified: '2026-06-20'
name: Plain
nav: Providers
network: true
overview: 'Plain publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Customer Support, Help Desk, GraphQL, Threads, and Customer Communication.


  Plain''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Plain Support Plans Pricing
  plan_count: 4
  slug: plain-support-plans-pricing
random_paper: 44
rate_limits:
- limit_count: 3
  name: Plain Support Rate Limits
  slug: plain-support-rate-limits
score:
  band: thin
  composite: 40.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 68.2
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 40.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/plain-support/refs/heads/main/screenshots/plain-support-2026-06-20T191749.png
security:
- kind: authentication
  name: Plain Support Authentication
  slug: plain-support-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Plain Support Domain Security
  slug: plain-support-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plain-support
tags:
- Customer Support
- Help Desk
- GraphQL
- Threads
- Customer Communication
- API First
website: https://www.plain.com
---
