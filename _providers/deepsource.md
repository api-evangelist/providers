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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.0
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Deepsource Agentic Access
  operation_count: 1
  slug: deepsource-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: The GraphQL API from DeepSource — 1 operation(s) for graphql.
  name: DeepSource GraphQL API
  slug: deepsource-graphql-api
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: DeepSource GraphQL API
  slug: open-deepsource-graphql-api
- collection_type: open
  name: DeepSource GraphQL API
  slug: open-deepsource
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/deepsource-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/deepsource-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/deepsource-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/deepsourcecorp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/deepsource
- group: company
  title: ''
  type: Website
  url: https://deepsource.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.deepsource.com/docs/developers/api
- group: commercial
  title: ''
  type: Plans
  url: plans/deepsource-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/deepsource-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/deepsource-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://deepsource.com/blog
created: '2026-06-21'
description: DeepSource is a code-quality and security platform that performs static analysis, SCA, secrets detection, AI code review, and Autofix across repositories. Its developer platform is a GraphQL API at https://api.deepsource.com/graphql/ exposing repositories, analysis runs, issues, checks, analyzers, and quality-gate management, authenticated with a Personal Access Token Bearer credential.
finops:
- name: Deepsource Finops
  service_category: Developer Tools
  slug: deepsource-finops
graphqls:
- description: The [DeepSource](https://deepsource.com) developer platform is a single **GraphQL API**
  name: DeepSource GraphQL API
  slug: deepsource-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/deepsource.png
layout: provider
modified: '2026-06-21'
name: DeepSource
nav: Providers
network: true
overview: 'DeepSource publishes 1 API on the [APIs.io](https://apis.io/) network: GraphQL API. Tagged areas include Code Quality, Static Analysis, Code Review, Security, and GraphQL.


  DeepSource''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Deepsource Plans Pricing
  plan_count: 3
  slug: deepsource-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 1
  name: Deepsource Rate Limits
  slug: deepsource-rate-limits
score:
  band: thin
  composite: 38.2
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 62.3
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/deepsource/refs/heads/main/screenshots/deepsource-2026-07-25T211607.png
security:
- kind: authentication
  name: Deepsource Authentication
  slug: deepsource-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Deepsource Domain Security
  slug: deepsource-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: deepsource
tags:
- Code Quality
- Static Analysis
- Code Review
- Security
- GraphQL
website: https://deepsource.com
---
