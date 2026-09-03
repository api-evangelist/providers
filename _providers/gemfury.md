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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Gemfury Agentic Access
  operation_count: 15
  slug: gemfury-agentic-access
  summary_line: 15 operations · 6 acting
api_count: 1
apis:
- baseURL: https://api.fury.io
  baseurl_source: declared
  description: Retrieve account information
  name: Gemfury Accounts API
  slug: gemfury-accounts-api
- baseURL: https://api.fury.io
  baseurl_source: declared
  description: Manage collaborators and members
  name: Gemfury Members API
  slug: gemfury-members-api
- baseURL: https://api.fury.io
  baseurl_source: declared
  description: Manage packages in a Gemfury repository
  name: Gemfury Packages API
  slug: gemfury-packages-api
- baseURL: https://api.fury.io
  baseurl_source: declared
  description: Manage API tokens
  name: Gemfury Tokens API
  slug: gemfury-tokens-api
- baseURL: https://api.fury.io
  baseurl_source: declared
  description: Manage package versions
  name: Gemfury Versions API
  slug: gemfury-versions-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Gemfury Developer Accounts API
  slug: open-gemfury-accounts-api
- collection_type: open
  name: Gemfury Developer Accounts Members API
  slug: open-gemfury-members-api
- collection_type: open
  name: Gemfury Developer Accounts Packages API
  slug: open-gemfury-packages-api
- collection_type: open
  name: Gemfury Developer Accounts Tokens API
  slug: open-gemfury-tokens-api
- collection_type: open
  name: Gemfury Developer Accounts Versions API
  slug: open-gemfury-versions-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/gemfury/gemfury/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/gemfury/gemfury/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/gemfury/gemfury/blob/main/LICENSE
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


  Gemfury''s developer surface includes authentication, documentation, engineering blog, changelog, pricing, CLI, and 14 more developer resources.'
plans:
- name: Gemfury Plans Pricing
  plan_count: 14
  slug: gemfury-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 2
  name: Gemfury Rate Limits
  slug: gemfury-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Gemfury API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: gemfury-jsonschema-spectral-rules
score:
  band: developing
  composite: 47.4
  coverage:
    artifact_dirs: 15
    catalog_gap: 43.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 63.2
    developer_ergonomics: 42.9
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 25.0
  previous_composite: 47.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
