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
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.9
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The free Qlty CLI is a polyglot, Rust-based command-line tool for universal linting, auto-formatting, security scanning, code smells, duplication, and maintainability metrics. It runs 70+ static analy
  name: Qlty CLI
  slug: qlty-cli
- description: Coverage publishing is performed by the Qlty CLI command qlty coverage publish, which uploads test coverage reports to Qlty Cloud from a CI pipeline. It authenticates with a per-project QLTY_COVERAGE_
  name: Qlty Coverage Upload
  slug: qlty-coverage-upload
- description: Qlty Cloud is the hosted platform that analyzes pull requests, posts automated code review comments on newly introduced issues, enforces quality gates, aggregates coverage, and renders trends and dash
  name: Qlty Cloud API
  slug: qlty-cloud
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qlty
  slug: open-qlty
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qlty-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qlty-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/qltysh
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qltysh
- group: company
  title: ''
  type: Website
  url: https://qlty.sh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.qlty.sh
- group: commercial
  title: ''
  type: Plans
  url: plans/qlty-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qlty-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qlty-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://qlty.sh/blog
created: '2026-06-21'
description: Qlty is a code quality and coverage platform from the team behind Code Climate. It pairs the free Qlty CLI - a polyglot Rust tool for universal linting, auto-formatting, security scanning, and maintainability analysis - with Qlty Cloud, a hosted service for automated pull request review, code coverage upload, quality gates, and dashboards.
finops:
- name: Qlty Finops
  service_category: Developer Tools
  slug: qlty-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qlty.png
layout: provider
modified: '2026-06-21'
name: Qlty
nav: Providers
network: true
overview: 'Qlty publishes 3 APIs on the [APIs.io](https://apis.io/) network: CLI, Coverage Upload, and Cloud API. Tagged areas include Code Quality, Code Coverage, Static Analysis, Linting, and Developer Tools.


  Qlty''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Qlty Plans Pricing
  plan_count: 4
  slug: qlty-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 6
  name: Qlty Rate Limits
  slug: qlty-rate-limits
score:
  band: thin
  composite: 32.4
  delta: -0.4
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 31.5
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 32.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qlty Authentication
  slug: qlty-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qlty Domain Security
  slug: qlty-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: qlty
tags:
- Code Quality
- Code Coverage
- Static Analysis
- Linting
- Developer Tools
website: https://qlty.sh/
---
