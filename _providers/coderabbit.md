---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Coderabbit Agentic Access
  operation_count: 1
  slug: coderabbit-agentic-access
  summary_line: 1 operation · 1 acting
api_count: 1
apis:
- description: CodeRabbit installs as a Git application on GitHub, GitLab, Bitbucket, and Azure DevOps, subscribing to pull/merge request events to post AI reviews, summaries, and chat replies. Integration is event-
  name: CodeRabbit Git App Integration
  slug: coderabbit-git-app-integration
- description: Per-repository behavior is configured with a .coderabbit.yaml file (validated against a published JSON schema) controlling review tone, path filters, enabled tools/linters, auto-review, and chat behav
  name: CodeRabbit Configuration
  slug: coderabbit-configuration
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Audit Logs API from CodeRabbit — 1 operation(s) for audit logs.
  name: CodeRabbit Audit Logs API
  slug: coderabbit-audit-logs-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Learnings API from CodeRabbit — 2 operation(s) for learnings.
  name: CodeRabbit Learnings API
  slug: coderabbit-learnings-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Metrics API from CodeRabbit — 3 operation(s) for metrics.
  name: CodeRabbit Metrics API
  slug: coderabbit-metrics-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Organizations API from CodeRabbit — 2 operation(s) for organizations.
  name: CodeRabbit Organizations API
  slug: coderabbit-organizations-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Report.generate API from CodeRabbit — 1 operation(s) for report.generate.
  name: CodeRabbit Report.generate API
  slug: coderabbit-report-generate-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Role Management API from CodeRabbit — 3 operation(s) for role management.
  name: CodeRabbit Role Management API
  slug: coderabbit-role-management-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Security API from CodeRabbit — 1 operation(s) for security.
  name: CodeRabbit Security API
  slug: coderabbit-security-api
- baseURL: https://app.coderabbit.ai
  baseurl_source: declared
  description: The Users API from CodeRabbit — 4 operation(s) for users.
  name: CodeRabbit Users API
  slug: coderabbit-users-api
artifact_total: 20
collections:
- collection_type: open
  name: CodeRabbit Reports API
  slug: open-coderabbit-reports-api
- collection_type: open
  name: CodeRabbit API
  slug: open-coderabbit
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.coderabbit.ai/pricing
- group: agent
  href: https://artifacts.apis.io/coderabbit/agentic-access/coderabbit-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/coderabbit-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/coderabbit/security/coderabbit-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/coderabbit-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/coderabbit/security/coderabbit-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coderabbit-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/coderabbit/authentication/coderabbit-authentication.yml
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
  href: https://artifacts.apis.io/coderabbit/plans/coderabbit-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/coderabbit-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/coderabbit/rate-limits/coderabbit-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/coderabbit-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/coderabbit/finops/coderabbit-finops.yml
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
- has_sources: true
  method: generated
  name: Coderabbit Finops
  primary_unit: ''
  service_category: Developer Tools
  slug: coderabbit-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coderabbit.png
layout: provider
modified: '2026-06-21'
name: CodeRabbit
nav: Providers
network: true
overview: 'CodeRabbit publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audit Logs API, Learnings API, Metrics API, and 7 more. Tagged areas include Artificial Intelligence, Code Review, Developer Tools, Pull Requests, and DevOps.


  The CodeRabbit catalog on APIs.io includes 1 Spectral governance ruleset.


  CodeRabbit''s developer surface includes pricing, authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Coderabbit Plans Pricing
  plan_count: 9
  slug: coderabbit-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Coderabbit Rate Limits
  slug: coderabbit-rate-limits
rules:
- authorship: generated
  effective_rule_count: 99
  extends:
  - spectral:oas
  name: CodeRabbit API Rules
  rule_count: 58
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 8
  slug: coderabbit-rules
score:
  band: developing
  composite: 40.5
  coverage:
    artifact_dirs: 16
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.1
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 55.3
    developer_ergonomics: 44.0
    discoverability: 66.1
    operational_transparency: 21.1
  previous_composite: 40.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 80.0
      total: 10
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/coderabbit/coderabbit-2026-07-25T205926.png
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
- Artificial Intelligence
- Code Review
- Developer Tools
- Pull Requests
- DevOps
website: https://www.coderabbit.ai
---
