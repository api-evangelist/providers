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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Flutter Agentic Access
  operation_count: 5
  slug: google-flutter-agentic-access
  summary_line: 5 operations
api_count: 3
apis:
- description: The Dart Analysis Server provides a JSON-based protocol for IDE integration, enabling code analysis, completion, navigation, refactoring, and diagnostics for Dart and Flutter projects.
  name: Dart Analysis Server Protocol
  slug: dart-analysis-server-protocol
- description: Package documentation endpoints
  name: Google Flutter Documentation API
  slug: google-flutter-documentation-api
- description: Operations for searching and retrieving package information
  name: Google Flutter Packages API
  slug: google-flutter-packages-api
artifact_total: 18
collections:
- collection_type: postman
  name: Google Flutter Pub.dev Documentation API
  slug: postman-google-flutter-documentation-api
- collection_type: postman
  name: Google Flutter Pub.dev Documentation Packages API
  slug: postman-google-flutter-packages-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Flutter Pub.dev API
  slug: open-flutter-pub-dev
- collection_type: open
  name: Google Flutter Pub.dev Documentation API
  slug: open-google-flutter-documentation-api
- collection_type: open
  name: Google Flutter Pub.dev Documentation Packages API
  slug: open-google-flutter-packages-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-flutter/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-flutter-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-flutter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-flutter-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/flutterdevofficial
- group: start
  title: ''
  type: Portal
  url: https://flutter.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.flutter.dev/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://docs.flutter.dev
- group: auth
  title: ''
  type: Authentication
  url: https://pub.dev/help/api#authentication
- group: build
  title: ''
  type: SDKs
  url: https://docs.flutter.dev/get-started/install
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://github.com/flutter/flutter/wiki
- group: operate
  title: ''
  type: Support
  url: https://flutter.dev/community
- group: design
  title: ''
  type: JSONLD
  url: json-ld/google-flutter-context.jsonld
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.flutter.dev/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://medium.com/feed/flutter
created: '2026-03-13'
description: Google Flutter is an open-source UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase, with developer tools including the Pub.dev package API and Dart analysis APIs.
finops:
- name: Google Flutter Finops
  service_category: API
  slug: google-flutter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-flutter.png
json_schemas:
- name: Pub.dev Package
  property_count: 3
  slug: google-flutter-pub-package
jsonld:
- class_count: 0
  name: Google Flutter Context
  property_count: 3
  slug: google-flutter-context
layout: provider
modified: '2026-05-19'
name: Google Flutter
nav: Providers
network: true
overview: 'Google Flutter publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documentation API and Packages API. Tagged areas include Cross-Platform, Dart, Google, Mobile Development, and Open-Source.


  The Google Flutter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Flutter''s developer surface includes developer portal, getting-started guide, documentation, authentication, support, engineering blog, and 11 more developer resources.'
plans:
- name: Google Flutter Plans Pricing
  plan_count: 3
  slug: google-flutter-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Flutter Rate Limits
  slug: google-flutter-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Flutter API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: google-flutter-jsonschema-spectral-rules
score:
  band: developing
  composite: 49.5
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 9.8
    contract_quality: 56.8
    developer_ergonomics: 61.9
    discoverability: 72.2
    governance: 9.8
    operational_transparency: 23.7
  previous_composite: 49.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-flutter/refs/heads/main/screenshots/google-flutter-2026-06-20T182202.png
security:
- kind: domain-security
  name: Google Flutter Domain Security
  slug: google-flutter-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Flutter Vulnerability Disclosure
  slug: google-flutter-vulnerability-disclosure
  summary_line: disclosure policy published
slug: google-flutter
tags:
- Cross-Platform
- Dart
- Google
- Mobile Development
- Open-Source
- UI Framework
website: https://flutter.dev
---
