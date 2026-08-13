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
- description: GraphQL Federation API powering the Erxes XOS platform. Built on Apollo Router with microservices architecture, it exposes endpoints for contacts, companies, conversations, tickets, tasks, deals, auto
  name: Erxes GraphQL API
  slug: graphql-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/erxes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://erxes.io
- group: docs
  title: ''
  type: Documentation
  url: https://erxes.io/docs/introduction
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/erxes
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/erxes
- group: commercial
  title: ''
  type: Pricing
  url: https://erxes.io/pricing/self-service/frontline
- group: commercial
  title: ''
  type: Plans
  url: plans/erxes-plans.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/erxes-rate-limits.md
- group: commercial
  title: ''
  type: FinOps
  url: finops/erxes-finops.md
created: 2026-06-14
description: Open-source experience operating system (XOS) that unifies marketing, sales, operations, and support — replacing tools like HubSpot, Zendesk, and Linear. Provides a GraphQL API covering contacts, companies, conversations, tasks, tickets, deals, team inboxes, and automation workflows.
graphqls:
- description: 'Erxes is an open-source experience operating system (XOS) built on a GraphQL Federation architecture using Apollo Router. The API is organized as a microservices monorepo where each plugin (contacts, '
  name: Erxes GraphQL API
  slug: erxes-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/erxes.png
layout: provider
modified: 2026-06-14
name: Erxes
nav: Providers
network: true
overview: 'Erxes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include GraphQL, CRM, Customer Experience, Open Source, and Marketing Automation.


  Erxes'' developer surface includes documentation, pricing, and 7 more developer resources.'
random_paper: 71
score:
  band: emerging
  composite: 22.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 43.2
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/erxes/refs/heads/main/screenshots/erxes-2026-06-20T180818.png
security:
- kind: domain-security
  name: Erxes Domain Security
  slug: erxes-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: erxes
tags:
- GraphQL
- CRM
- Customer Experience
- Open Source
- Marketing Automation
- Sales Pipeline
website: https://erxes.io
---
