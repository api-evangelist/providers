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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Slab Agentic Access
  operation_count: 1
  slug: slab-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from Slab — 1 operation(s) for graphql.
  name: Slab GraphQL API
  slug: slab-graphql-api
artifact_total: 10
collections:
- collection_type: open
  name: Slab GraphQL API
  slug: open-slab
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/slab-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/slab-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/slab-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/slab-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/slab
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/slab-inc
- group: company
  title: ''
  type: Website
  url: https://slab.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.slab.com/en/articles/6545629-developer-tools-api-webhooks
- group: commercial
  title: ''
  type: Plans
  url: plans/slab-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/slab-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/slab-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://slab.com/blog/
created: '2026-06-21'
description: Slab is an internal knowledge base and team wiki for the modern workplace, pairing a clean editor and fast search with dozens of integrations. Slab exposes a single GraphQL API at https://api.slab.com/v1/graphql for programmatic access to posts, topics, users, and organization data, available to Business and Enterprise customers.
finops:
- name: Slab Finops
  service_category: Collaboration and Productivity
  slug: slab-finops
graphqls:
- description: Conceptual GraphQL schema for the [Slab](https://slab.com/) knowledge base and team wiki platform.
  name: Slab GraphQL Schema
  slug: slab-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/slab.png
layout: provider
modified: '2026-06-21'
name: Slab
nav: Providers
network: true
overview: 'Slab publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Knowledge Base, Wiki, Documentation, Collaboration, and GraphQL.


  Slab''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Slab Plans Pricing
  plan_count: 4
  slug: slab-plans-pricing
random_paper: 79
rate_limits:
- limit_count: 2
  name: Slab Rate Limits
  slug: slab-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.9
    developer_ergonomics: 21.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Slab Authentication
  slug: slab-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Slab Domain Security
  slug: slab-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Slab Vulnerability Disclosure
  slug: slab-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: slab
tags:
- Knowledge Base
- Wiki
- Documentation
- Collaboration
- GraphQL
website: https://slab.com/
---
