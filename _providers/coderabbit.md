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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Coderabbit Agentic Access
  operation_count: 1
  slug: coderabbit-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 3
apis:
- description: CodeRabbit installs as a Git application on GitHub, GitLab, Bitbucket, and Azure DevOps, subscribing to pull/merge request events to post AI reviews, summaries, and chat replies. Integration is event-
  name: CodeRabbit Git App Integration
  slug: coderabbit-git-app-integration
- description: Per-repository behavior is configured with a .coderabbit.yaml file (validated against a published JSON schema) controlling review tone, path filters, enabled tools/linters, auto-review, and chat behav
  name: CodeRabbit Configuration
  slug: coderabbit-configuration
- description: The Reports API from CodeRabbit — 1 operation(s) for reports.
  name: CodeRabbit Reports API
  slug: coderabbit-reports-api
artifact_total: 11
collections:
- collection_type: open
  name: CodeRabbit API
  slug: open-coderabbit
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coderabbit-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coderabbit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coderabbit-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coderabbit-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coderabbitai
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/coderabbitai
- group: company
  title: ''
  type: Website
  url: https://www.coderabbit.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.coderabbit.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/coderabbit-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/coderabbit-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/coderabbit-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.coderabbit.ai/feed
created: '2026-06-21'
description: CodeRabbit is an AI-powered code review platform that installs as a Git app (GitHub, GitLab, Bitbucket, Azure DevOps) to deliver line-by-line, context-aware reviews and summaries on pull requests, plus IDE and CLI reviews. It exposes a REST API for on-demand developer activity report generation and is configured per-repository with a .coderabbit.yaml file.
finops:
- name: Coderabbit Finops
  service_category: Developer Tools
  slug: coderabbit-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coderabbit.png
layout: provider
modified: '2026-06-21'
name: CodeRabbit
nav: Providers
network: true
overview: 'CodeRabbit publishes 1 API on the [APIs.io](https://apis.io/) network: Reports API. Tagged areas include AI, Code Review, Developer Tools, Pull Requests, and DevOps.


  CodeRabbit''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Coderabbit Plans Pricing
  plan_count: 4
  slug: coderabbit-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 4
  name: Coderabbit Rate Limits
  slug: coderabbit-rate-limits
score:
  band: thin
  composite: 40.3
  delta: -2.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coderabbit/refs/heads/main/screenshots/coderabbit-2026-07-25T205926.png
security:
- kind: authentication
  name: Coderabbit Authentication
  slug: coderabbit-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Coderabbit Domain Security
  slug: coderabbit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Coderabbit Vulnerability Disclosure
  slug: coderabbit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: coderabbit
tags:
- AI
- Code Review
- Developer Tools
- Pull Requests
- DevOps
website: https://www.coderabbit.ai
---
