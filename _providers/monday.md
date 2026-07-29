---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.0
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Programmatically access and update data inside a monday.com account
  name: Monday
  slug: monday
artifact_total: 4
common:
- group: other
  title: ''
  type: AgentCard
  url: a2a/monday-a2a.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/monday-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/monday-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://api.developer.monday.com/docs
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://monday.com/blog
created: '2026-05-28'
description: Programmatically access and update data inside a monday.com account
graphqls:
- description: 'Monday.com exposes a native GraphQL API that provides full programmatic access to boards, items, columns, users, workspaces, updates, webhooks, and other platform resources. All API requests are sent '
  name: Monday.com GraphQL API
  slug: monday-graphql
layout: provider
modified: '2026-05-28'
name: Monday
nav: Providers
network: true
overview: 'Monday publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Documents And Productivity and Public APIs.


  Monday''s developer surface includes engineering blog and 5 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 18.2
  delta: 9.4
  facets:
    commercial_clarity: 7.9
    contract_quality: 43.2
    developer_ergonomics: 2.2
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: domain-security
  name: Monday Domain Security
  slug: monday-domain-security
  summary_line: DMARC
- kind: trust-center
  name: Monday Trust Center
  slug: monday-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, HIPAA, FedRAMP, GDPR, CSA STAR
slug: monday
tags:
- Documents And Productivity
- Public APIs
website: https://api.developer.monday.com/docs
---
