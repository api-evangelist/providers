---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 11.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Screenshot API Documentation — Getting Started
  name: Screenshot API
  slug: screenshot-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/i2dev-com/rate-limits/i2dev-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/i2dev-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/i2dev-com/plans/i2dev-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/i2dev-com-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/i2dev-com/authentication/i2dev-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/i2dev-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/i2dev-com/scopes/i2dev-com-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/i2dev-com-scopes.yml
- group: design
  href: https://artifacts.apis.io/i2dev-com/errors/i2dev-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/i2dev-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/i2dev-com/llms/i2dev-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/i2dev-com-llms.txt
- group: other
  href: https://artifacts.apis.io/i2dev-com/hosts/i2dev-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/i2dev-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/i2dev-com/vendors/i2dev-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/i2dev-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/i2dev-com/security/i2dev-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/i2dev-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://i2dev.com/
- group: docs
  title: ''
  type: Documentation
  url: https://snap.i2dev.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://snap.i2dev.com/docs/api
- group: start
  title: ''
  type: GettingStarted
  url: https://snap.i2dev.com/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://i2dev.com/contact/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/i2Dev-com
- group: commercial
  title: ''
  type: Pricing
  url: https://snap.i2dev.com/pricing
coverage:
  checked: '2026-10-31'
  detail: Public documentation exists at https://snap.i2dev.com/docs but no machine‑readable OpenAPI, AsyncAPI, GraphQL, or other contract is published.
  evidence:
  - status: 200
    url: https://snap.i2dev.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: i2dev is a platform offering a suite of developer tools under a single account, including Snap Visual Regression for automated visual testing in GitHub Actions, Snapdrift open‑source runner, and other utilities. The company focuses on providing small, focused tools that share unified authentication and billing, emphasizing data privacy, no ad‑funding, and transparent pricing. Their services aim to simplify developers' workflows by consolidating multiple tools into one cohesive ecosystem.
image: https://i2dev.com/assets/logo.svg
layout: provider
modified: '2026-10-30'
name: i2dev-com
nav: Providers
network: true
overview: 'i2dev-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeveloperTools, VisualRegression, CI, and OpenSource.


  i2dev-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 10 more developer resources.'
plans:
- name: I2Dev Com Plans Pricing
  plan_count: 1
  slug: i2dev-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: I2Dev Com Rate Limits
  slug: i2dev-com-rate-limits
scopes:
- name: I2Dev Com Scopes
  scope_count: 1
  slug: i2dev-com-scopes
  summary_line: 1 scope
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 20
    catalog_earned: 46.4
    catalog_earned_first_party: 0.0
    catalog_gap: 68.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 29.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 57.1
    operational_transparency: 24.2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: I2Dev Com Authentication
  slug: i2dev-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: I2Dev Com Domain Security
  slug: i2dev-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: i2dev-com
tags:
- Company
- DeveloperTools
- VisualRegression
- CI
- OpenSource
- SaaS
website: https://i2dev.com/
---
