---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 1.9
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Kratos is a Go framework for building cloud-native microservices, originally created at Bilibili. It provides built-in support for HTTP and gRPC transports, service discovery, configuration management
  name: Kratos
  slug: kratos
artifact_total: 7
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kratos/refs/heads/main/plans/kratos-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kratos-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kratos/refs/heads/main/rate-limits/kratos-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kratos-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kratos/refs/heads/main/finops/kratos-finops.yml
  title: ''
  type: FinOps
  url: finops/kratos-finops.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/go-kratos/kratos/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/go-kratos/kratos/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/go-kratos/kratos/blob/main/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/go-kratos/kratos/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/go-kratos/kratos/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/go-kratos/kratos/blob/main/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kratos/refs/heads/main/security/kratos-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kratos-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/oryorg
- group: company
  title: ''
  type: Website
  url: https://go-kratos.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://go-kratos.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://go-kratos.dev/docs/getting-started/start/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/go-kratos
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/go-kratos/kratos
- group: company
  title: ''
  type: Blog
  url: https://go-kratos.dev/blog/
- group: build
  title: ''
  type: Examples
  url: https://github.com/go-kratos/examples
created: '2026-03-26'
description: Kratos is a Go framework for building cloud-native microservices, originally created at Bilibili. It provides built-in support for HTTP and gRPC transports, service discovery, configuration management, logging, metrics, and tracing, following a clean architecture approach with Protocol Buffers for API definitions.
finops:
- has_sources: false
  method: generated
  name: Kratos Finops
  primary_unit: ''
  service_category: API
  slug: kratos-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kratos.png
json_schemas:
- name: Kratos Service Configuration
  property_count: 5
  slug: kratos-configuration
layout: provider
modified: '2026-04-28'
name: Kratos
nav: Providers
network: true
overview: 'Kratos is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Framework, Go, gRPC, and Microservices.


  The Kratos catalog on APIs.io includes 1 Spectral governance ruleset.


  Kratos'' developer surface includes documentation, getting-started guide, engineering blog, code examples, and 14 more developer resources.'
plans:
- name: Kratos Plans Pricing
  plan_count: 3
  slug: kratos-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Kratos Rate Limits
  slug: kratos-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Kratos — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: kratos-jsonschema-spectral-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 10
    catalog_earned: 46.7
    catalog_earned_first_party: 0.0
    catalog_gap: 68.4
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.4
  facets:
    access_clarity: 7.9
    contract_governance: 9.8
    contract_quality: 13.7
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 29.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/kratos/refs/heads/main/screenshots/kratos-2026-06-20T184150.png
security:
- kind: domain-security
  name: Kratos Domain Security
  slug: kratos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: kratos
tags:
- Cloud-Native
- Framework
- Go
- gRPC
- Microservices
- Protocol Buffers
- Service Discovery
website: https://go-kratos.dev/
---
