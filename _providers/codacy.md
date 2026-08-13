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
  band: agent-aware
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
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Codacy Agentic Access
  operation_count: 18
  slug: codacy-agentic-access
  summary_line: 18 operations · 5 acting
api_count: 8
apis:
- description: Authenticated user account and API token operations.
  name: Codacy Account API
  slug: codacy-account-api
- description: Code coverage for pull requests and files.
  name: Codacy Coverage API
  slug: codacy-coverage-api
- description: Static analysis issues for a repository.
  name: Codacy Issues API
  slug: codacy-issues-api
- description: Git provider organizations the account belongs to.
  name: Codacy Organizations API
  slug: codacy-organizations-api
- description: Pull request analysis, files, issues, and AI review.
  name: Codacy Pull Requests API
  slug: codacy-pull-requests-api
- description: Quality and security gating settings for commits and pull requests.
  name: Codacy Quality Settings API
  slug: codacy-quality-settings-api
- description: Repository management and analysis state.
  name: Codacy Repositories API
  slug: codacy-repositories-api
- description: Repository SSH key administration.
  name: Codacy Security API
  slug: codacy-security-api
artifact_total: 15
collections:
- collection_type: open
  name: Codacy API
  slug: open-codacy
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codacy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codacy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codacy-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/codacy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codacy
- group: company
  title: ''
  type: Website
  url: https://www.codacy.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.codacy.com
- group: commercial
  title: ''
  type: Plans
  url: plans/codacy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/codacy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/codacy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.codacy.com/rss.xml
created: '2026-06-21'
description: Codacy is an automated code quality and security platform that analyzes commits and pull requests across 49+ languages, surfacing issues, coverage, and security findings. The Codacy API v3 lets teams manage organizations, repositories, issues, pull requests, coverage, security, and quality settings programmatically.
finops:
- name: Codacy Finops
  service_category: Developer Tools
  slug: codacy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codacy.png
layout: provider
modified: '2026-06-21'
name: Codacy
nav: Providers
network: true
overview: 'Codacy publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Account API, Coverage API, Issues API, and 5 more. Tagged areas include Code Quality, Static Analysis, Security, Code Coverage, and DevOps.


  Codacy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Codacy Plans Pricing
  plan_count: 3
  slug: codacy-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 2
  name: Codacy Rate Limits
  slug: codacy-rate-limits
score:
  band: thin
  composite: 36.5
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 53.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codacy/refs/heads/main/screenshots/codacy-2026-07-25T205855.png
security:
- kind: authentication
  name: Codacy Authentication
  slug: codacy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Codacy Domain Security
  slug: codacy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: codacy
tags:
- Code Quality
- Static Analysis
- Security
- Code Coverage
- DevOps
website: https://www.codacy.com
---
