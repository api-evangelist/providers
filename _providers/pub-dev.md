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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Search for packages, retrieve package metadata, version details, publisher information, and scoring data from the official Dart and Flutter package registry.
  name: pub.dev Packages API
  slug: pubdev-packages-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pub-dev-vulnerability-disclosure.yml
- group: auth
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
- name: Finops
  service_category: ''
  slug: finops
image: https://pub.dev/favicon.ico
layout: provider
modified: '2026-06-13'
name: pub.dev
nav: Providers
network: true
overview: 'pub.dev publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Dart, Flutter, Package Registry, Package Management, and Open Source.


  pub.dev''s developer surface includes documentation and 8 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 51
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
score:
  band: emerging
  composite: 20.7
  delta: -1.7
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 22.4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
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
website: https://pub.dev/
---
