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
api_count: 1
apis:
- baseURL: https://qlty.sh
  baseurl_source: declared
  description: The free Qlty CLI is a polyglot, Rust-based command-line tool for universal linting, auto-formatting, security scanning, code smells, duplication, and maintainability metrics. It runs 70+ static analy
  name: Qlty CLI
  slug: qlty-cli
- baseURL: https://qlty.sh
  baseurl_source: declared
  description: Coverage publishing is performed by the Qlty CLI command qlty coverage publish, which uploads test coverage reports to Qlty Cloud from a CI pipeline. It authenticates with a per-project QLTY_COVERAGE_
  name: Qlty Coverage Upload
  slug: qlty-coverage-upload
- baseURL: https://qlty.sh
  baseurl_source: declared
  description: Qlty Cloud is the hosted platform that analyzes pull requests, posts automated code review comments on newly introduced issues, enforces quality gates, aggregates coverage, and renders trends and dash
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
screenshot: https://raw.githubusercontent.com/api-evangelist/qlty/refs/heads/main/screenshots/qlty-2026-09-02T152514.png
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
