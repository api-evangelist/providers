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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Google Play Console Agentic Access
  operation_count: 4
  slug: google-play-console-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: The V1alpha1 API from Google Play Console Developer Reporting — 4 operation(s) for v1alpha1.
  name: Google Play Console Developer Reporting V1alpha1 API
  slug: google-play-console-v1alpha1-api
artifact_total: 12
collections:
- collection_type: postman
  name: Google Play Console Developer Reporting Google Play Developer Reporting V1alpha1 API
  slug: postman-google-play-console-v1alpha1-api
- collection_type: open
  name: Google Play Console Developer Reporting Google Play Developer Reporting API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-play-console-developer-reporting/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-play-console-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-play-console-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-play-console-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-play-console-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-play-console-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://play.google.com/console
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/play/developer/reporting/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://developers.google.com/play/developer/reporting
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/play/developer/reporting/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://play.google.com/console/about/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://play.google.com/about/developer-distribution-agreement.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/play/developer/reporting/support
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google Play Developer Reporting API provides programmatic access to Play Console data for app performance metrics, error reports, and quality insights. It enables developers to build automated workflows and integrate Play Console analytics into internal business reporting and analysis systems.
finops:
- name: Google Play Console Finops
  service_category: API
  slug: google-play-console-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-play-console.png
layout: provider
modified: '2026-05-19'
name: Google Play Console Developer Reporting
nav: Providers
network: true
overview: 'Google Play Console Developer Reporting publishes 1 API on the [APIs.io](https://apis.io/) network: V1alpha1 API. Tagged areas include Analytics, Android, Apps, Google Play Console, and Quality.


  The Google Play Console Developer Reporting catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Play Console Developer Reporting''s developer surface includes authentication, developer portal, getting-started guide, documentation, pricing, support, and 10 more developer resources.'
plans:
- name: Google Play Console Plans Pricing
  plan_count: 3
  slug: google-play-console-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Google Play Console Rate Limits
  slug: google-play-console-rate-limits
rules:
- name: Google Play Console Developer Reporting API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-play-console-jsonschema-spectral-rules
scopes:
- name: Google Play Console Scopes
  scope_count: 1
  slug: google-play-console-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: strong
  composite: 60.5
  delta: 0.0
  facets:
    commercial_clarity: 71.1
    contract_quality: 66.7
    developer_ergonomics: 47.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 47.4
  previous_composite: 60.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-play-console/refs/heads/main/screenshots/google-play-console-2026-06-20T182226.png
security:
- kind: authentication
  name: Google Play Console Authentication
  slug: google-play-console-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Play Console Domain Security
  slug: google-play-console-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Play Console Vulnerability Disclosure
  slug: google-play-console-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-play-console
tags:
- Analytics
- Android
- Apps
- Google Play Console
- Quality
- Reporting
website: https://play.google.com/console
---
