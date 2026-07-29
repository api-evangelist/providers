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
- acting_count: 6
  human_in_the_loop: 0
  name: Gemfury Agentic Access
  operation_count: 15
  slug: gemfury-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 5
apis:
- description: Retrieve account information
  name: Gemfury Accounts API
  slug: gemfury-accounts-api
- description: Manage collaborators and members
  name: Gemfury Members API
  slug: gemfury-members-api
- description: Manage packages in a Gemfury repository
  name: Gemfury Packages API
  slug: gemfury-packages-api
- description: Manage API tokens
  name: Gemfury Tokens API
  slug: gemfury-tokens-api
- description: Manage package versions
  name: Gemfury Versions API
  slug: gemfury-versions-api
artifact_total: 23
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gemfury-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gemfury-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gemfury-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://gemfury.com
- group: docs
  title: ''
  type: Documentation
  url: https://gemfury.com/help/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/gemfury
- group: company
  title: ''
  type: Blog
  url: https://fury.blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://fury.blog/changelog
- group: commercial
  title: ''
  type: Pricing
  url: https://fury.co/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.fury.co/
- group: other
  title: ''
  type: X
  url: https://x.com/Gemfury
- group: build
  title: ''
  type: CLI
  url: https://gemfury.com/guide/cli/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/gemfury/gemfury
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/gemfury/cli
- group: commercial
  title: ''
  type: Plans
  url: plans/gemfury-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gemfury-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gemfury-finops.yml
created: '2026-06-13'
description: Gemfury is a private package repository service with a REST API for pushing and managing gems, npm, pip, composer, and other language packages for teams and organizations. It supports Gem, npm, PyPI, Go Modules, Composer, Maven, DEB, RPM, Bower, NuGet, and Rust Crates.
examples:
- key_count: 6
  name: Gemfury Create Token Example
  slug: gemfury-create-token-example
- key_count: 1
  name: Gemfury Error Example
  slug: gemfury-error-example
- key_count: 4
  name: Gemfury Get Account Example
  slug: gemfury-get-account-example
- key_count: 10
  name: Gemfury Get Version Example
  slug: gemfury-get-version-example
- key_count: 4
  name: Gemfury List Packages Example
  slug: gemfury-list-packages-example
finops:
- name: Gemfury Finops
  service_category: ''
  slug: gemfury-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gemfury.png
json_schemas:
- name: Account
  property_count: 4
  slug: gemfury-account
- name: Member
  property_count: 5
  slug: gemfury-member
- name: Package
  property_count: 7
  slug: gemfury-package
- name: Token
  property_count: 6
  slug: gemfury-token
- name: Version
  property_count: 10
  slug: gemfury-version
jsonld:
- class_count: 6
  name: Gemfury Context
  property_count: 2
  slug: gemfury-context
layout: provider
modified: '2026-06-13'
name: Gemfury
nav: Providers
network: true
overview: 'Gemfury publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Members API, Packages API, and 2 more. Tagged areas include Package Repository, Private Packages, Gem, npm, and PyPI.


  The Gemfury catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gemfury''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, CLI, and 11 more developer resources.'
plans:
- name: Gemfury Plans Pricing
  plan_count: 14
  slug: gemfury-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Gemfury Rate Limits
  slug: gemfury-rate-limits
rules:
- name: Gemfury API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gemfury-jsonschema-spectral-rules
score:
  band: developing
  composite: 54.9
  delta: -4.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 69.4
    developer_ergonomics: 28.3
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 59.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gemfury/refs/heads/main/screenshots/gemfury-2026-06-20T181711.png
security:
- kind: authentication
  name: Gemfury Authentication
  slug: gemfury-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Gemfury Domain Security
  slug: gemfury-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gemfury
tags:
- Package Repository
- Private Packages
- Gem
- npm
- PyPI
- Composer
- NuGet
- Go Modules
- Maven
- DEB
- RPM
- Bower
- Rust Crates
- Developer Tools
website: https://gemfury.com
---
