---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Packagist Agentic Access
  operation_count: 13
  slug: packagist-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 5
apis:
- description: Composer v2 static metadata and change tracking.
  name: Packagist Metadata API
  slug: packagist-metadata-api
- description: Discover and manage Composer packages.
  name: Packagist Packages API
  slug: packagist-packages-api
- description: Search the Packagist registry.
  name: Packagist Search API
  slug: packagist-search-api
- description: PHP security advisory database.
  name: Packagist Security API
  slug: packagist-security-api
- description: Download and registry statistics.
  name: Packagist Statistics API
  slug: packagist-statistics-api
artifact_total: 32
collections:
- collection_type: open
  name: Packagist API
  slug: open-packagist-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/packagist-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/packagist-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/packagist-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://packagist.org
- group: docs
  title: ''
  type: Documentation
  url: https://packagist.org/apidoc
- group: docs
  title: ''
  type: Documentation
  url: https://getcomposer.org/doc/
- group: company
  title: ''
  type: About
  url: https://packagist.org/about
- group: other
  title: ''
  type: Statistics
  url: https://packagist.org/statistics
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/composer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/packagist
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/composer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/satis
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/semver
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/spdx-licenses
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/class-map-generator
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/ca-bundle
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/api-surface-check
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/composer/docker
- group: build
  title: ''
  type: Tools
  url: https://getcomposer.org/
- group: build
  title: ''
  type: Tools
  url: https://github.com/composer/satis
- group: docs
  title: ''
  type: Documentation
  url: https://getcomposer.org/doc/01-basic-usage.md
- group: docs
  title: ''
  type: Documentation
  url: https://getcomposer.org/doc/04-schema.md
- group: docs
  title: ''
  type: Documentation
  url: https://getcomposer.org/doc/articles/versions.md
- group: docs
  title: ''
  type: Documentation
  url: https://packagist.org/about#how-to-update-packages
- group: auth
  title: ''
  type: Authentication
  url: https://packagist.org/apidoc#authentication
- group: start
  title: ''
  type: Signup
  url: https://packagist.org/register/
- group: start
  title: ''
  type: Login
  url: https://packagist.org/login/
- group: auth
  title: ''
  type: APIKeys
  url: https://packagist.org/profile/
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://packagist.org/apidoc#list-security-advisories
- group: auth
  title: ''
  type: SecurityAdvisories
  url: https://github.com/FriendsOfPHP/security-advisories
- group: other
  title: ''
  type: Mirror
  url: https://packagist.org/mirrors
- group: start
  title: ''
  type: Sandbox
  url: https://packagist.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://packagist.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://packagist.com/terms-of-service
- group: commercial
  title: ''
  type: License
  url: https://github.com/composer/packagist/blob/main/LICENSE
- group: company
  title: ''
  type: Blog
  url: https://blog.packagist.com/
- group: operate
  title: ''
  type: Forums
  url: https://github.com/composer/packagist/discussions
- group: operate
  title: ''
  type: Issues
  url: https://github.com/composer/packagist/issues
- group: commercial
  title: ''
  type: Plans
  url: plans/packagist-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/packagist-rate-limits.yml
created: '2026-05-25T00:00:00.000Z'
description: Packagist is the default package repository for Composer, the PHP dependency manager. It indexes over 454,000 open-source PHP packages — versions, dependencies, maintainers, download statistics, security advisories — and exposes them through a free public HTTP API plus a high-throughput static Composer v2 metadata mirror at repo.packagist.org. Packagist is MIT-licensed open source (composer/packagist on GitHub) and is operated by the Composer team, with funding from Private Packagist (the commercial hosted/self-hosted sibling product at packagist.com) and infrastructure sponsorships from Bunny.net and Aikido. Together with the Composer CLI, the SemVer library, the SPDX licenses helper, and the Satis static repository generator, Packagist anchors PHP's modern software supply chain.
examples:
- key_count: 2
  name: Packagist Get Package Example
  slug: packagist-get-package-example
- key_count: 2
  name: Packagist Search Example
  slug: packagist-search-example
- key_count: 2
  name: Packagist Security Advisories Example
  slug: packagist-security-advisories-example
features:
- 454,128 packages, 5.58 million versions, 181 billion+ installs since April 2012
- Default Composer package repository for the PHP ecosystem
- Static Composer v2 metadata mirror at repo.packagist.org with long-lived caching
- Bearer token auth with SAFE (read/update) and MAIN (create/edit) token classes
- 24-hour rolling change feed for mirror operators and dependency scanners
- Security advisories API aggregating FriendsOfPHP, GitHub Advisory Database, and PSA sources
- Webhook-driven auto-updates from GitHub, Bitbucket, GitLab, and Gitea
- Algolia-powered package search across name, tags, and type
- Per-package and per-version download statistics
- Commercial sibling Private Packagist for private/hosted/self-hosted Composer repositories
- MIT-licensed open source codebase (composer/packagist) — operated, not designed for reuse
- Funded by Private Packagist subscriptions plus Bunny.net (CDN) and Aikido (security) sponsorships
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/packagist.png
json_schemas:
- name: Packagist Package
  property_count: 20
  slug: packagist-package
- name: Packagist Security Advisory
  property_count: 11
  slug: packagist-security-advisory
json_structures:
- name: Packagist Package Structure
  property_count: 0
  slug: packagist-package-structure
jsonld:
- class_count: 35
  name: Packagist Context
  property_count: 4
  slug: packagist-context
layout: provider
modified: '2026-05-25'
name: Packagist
nav: Providers
network: true
overview: 'Packagist publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Metadata API, Packages API, Search API, and 2 more. Tagged areas include Composer, PHP, Package Registry, Dependency Management, and Open Source.


  The Packagist catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Packagist''s developer surface includes authentication, developer portal, documentation, tooling, signup flow, sandbox, engineering blog, and 33 more developer resources.'
plans:
- name: Packagist Plans Pricing
  plan_count: 3
  slug: packagist-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 2
  name: Packagist Rate Limits
  slug: packagist-rate-limits
rules:
- name: Packagist API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: packagist-jsonschema-spectral-rules
- name: Packagist API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 3
  slug: packagist-rules
score:
  band: strong
  composite: 56.5
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 72.6
    developer_ergonomics: 37.0
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 56.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/packagist/refs/heads/main/screenshots/packagist-2026-06-20T191311.png
security:
- kind: authentication
  name: Packagist Authentication
  slug: packagist-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Packagist Domain Security
  slug: packagist-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: packagist
tags:
- Composer
- PHP
- Package Registry
- Dependency Management
- Open Source
- Developer Tools
- Software Supply Chain
- Security Advisories
website: https://packagist.org
---
