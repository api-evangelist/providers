---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.6
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Search for packages, retrieve package metadata, version details, publisher information, and scoring data from the official Dart and Flutter package registry.
  name: pub.dev Packages API
  slug: pubdev-packages-api
artifact_total: 6
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/plans/plans.yml
  title: ''
  type: Plans
  url: plans/plans.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/rate-limits/rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/finops/finops.yml
  title: ''
  type: FinOps
  url: finops/finops.yml
- group: company
  title: ''
  type: Website
  url: https://pub.dev
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/dart-lang/pub-dev/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/dart-lang/pub-dev/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/dart-lang/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/dart-lang/pub-dev/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/dart-lang/pub-dev/blob/master/LICENSE
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/security/pub-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pub-dev-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/security/pub-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pub-dev-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://pub.dev/help/api
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.google.com/intl/en/policies/privacy/
- group: auth
  title: ''
  type: Security
  url: https://pub.dev/security
- group: operate
  title: ''
  type: Contact
  url: mailto:support@pub.dev
- group: other
  title: ''
  type: Feed
  url: https://pub.dev/feed.atom
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/dart-lang/pub-dev
created: '2026-06-13'
description: The official package repository for Dart and Flutter apps, maintained by Google. Provides a REST API for searching packages, retrieving package metadata and version information, downloading package archives, and accessing publisher and scoring information.
finops:
- has_sources: false
  method: generated
  name: Finops
  primary_unit: ''
  service_category: ''
  slug: finops
  template: true
image: https://pub.dev/favicon.ico
layout: provider
modified: '2026-09-16'
name: pub.dev
nav: Providers
network: true
overview: 'pub.dev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dart, Flutter, Package Registry, Package Management, and Open Source.


  pub.dev''s developer surface includes documentation and 17 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 9
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 24.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.8
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 73.2
    operational_transparency: 39.5
  open_source:
    applies: true
    score: 65.0
  previous_composite: 28.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/pub-dev/refs/heads/main/screenshots/pub-dev-2026-06-20T192237.png
security:
- kind: domain-security
  name: Pub Dev Domain Security
  slug: pub-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pub Dev Vulnerability Disclosure
  slug: pub-dev-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: pub-dev
tags:
- Dart
- Flutter
- Package Registry
- Package Management
- Open Source
website: https://pub.dev
---
