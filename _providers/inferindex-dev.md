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
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Public API providing pricing data for LLMs.
  name: InferIndex API
  slug: inferindex-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/inferindex-dev/rate-limits/inferindex-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/inferindex-dev-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/inferindex-dev/cli/inferindex-dev-cli.yml
  title: ''
  type: CLI
  url: cli/inferindex-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/inferindex-dev/changelog/inferindex-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/inferindex-dev-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://api.inferindex.dev/terms
- group: auth
  href: https://artifacts.apis.io/inferindex-dev/authentication/inferindex-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/inferindex-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/inferindex-dev/lifecycle/inferindex-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/inferindex-dev-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/inferindex-dev/errors/inferindex-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/inferindex-dev-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/inferindex-dev/llms/inferindex-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/inferindex-dev-llms.txt
- group: auth
  href: https://artifacts.apis.io/inferindex-dev/well-known/inferindex-dev-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inferindex-dev-security.txt
- group: auth
  href: https://artifacts.apis.io/inferindex-dev/well-known/inferindex-dev-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/inferindex-dev-api-security.txt
- group: agent
  href: https://artifacts.apis.io/inferindex-dev/well-known/inferindex-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/inferindex-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/inferindex-dev/hosts/inferindex-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/inferindex-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/inferindex-dev/vendors/inferindex-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/inferindex-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.inferindex.dev
- group: auth
  href: https://artifacts.apis.io/inferindex-dev/security/inferindex-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/inferindex-dev-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/inferindex-dev/security/inferindex-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/inferindex-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inferindex.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/InferIndex/inferindex-docs
- group: docs
  title: ''
  type: APIReference
  url: https://inferindex.dev/en/api
- group: start
  title: ''
  type: GettingStarted
  url: https://inferindex.dev/en/self-host
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inferindex.dev/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://inferindex.dev/en/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InferIndex
created: '2026-10-30'
description: InferIndex is an independent service that aggregates and indexes the pricing of large language model (LLM) APIs from a wide range of providers. It offers up‑to‑date price tables, historical price changes, promotions, and usage conditions for each model, enabling developers and businesses to compare costs across the ecosystem. The platform also provides a free public API that returns structured pricing data, supporting programmatic access for integration into cost‑analysis tools and applications.
image: https://api.inferindex.dev/icon-400.png
layout: provider
modified: '2026-10-30'
name: inferindex-dev
nav: Providers
network: true
overview: 'inferindex-dev is listed with 1 API on the [APIs.io](https://apis.io/) network: InferIndex API. Tagged areas include LLM, Pricing, Index, API, and Data.


  inferindex-dev''s developer surface includes CLI, changelog, authentication, documentation, API reference, getting-started guide, and 17 more developer resources.'
plans:
- name: Inferindex Dev Plans Pricing
  plan_count: 0
  slug: inferindex-dev-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Inferindex Dev Rate Limits
  slug: inferindex-dev-rate-limits
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 44.2
    catalog_earned_first_party: 0.0
    catalog_gap: 70.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 24.0
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 66.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Inferindex Dev Authentication
  slug: inferindex-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Inferindex Dev Domain Security
  slug: inferindex-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Inferindex Dev Vulnerability Disclosure
  slug: inferindex-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: inferindex-dev
tags:
- LLM
- Pricing
- Index
- API
- Data
website: https://inferindex.dev/
---
