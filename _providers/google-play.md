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
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.8
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Google Play Agentic Access
  operation_count: 4
  slug: google-play-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- description: The Androidpublisher API from Google Play Developer — 4 operation(s) for androidpublisher.
  name: Google Play Developer Androidpublisher API
  slug: google-play-androidpublisher-api
artifact_total: 13
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Play Developer Androidpublisher API
  slug: open-google-play-androidpublisher-api
- collection_type: open
  name: Google Play Developer API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-play-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-play-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-play-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-play-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-play-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/google
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/google-play
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/android-publisher/getting_started
- group: commercial
  title: ''
  type: Pricing
  url: https://play.google.com/console/about/pricing/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.yml
created: '2026-03-13'
description: The Google Play Developer API allows developers to perform publishing and app-management tasks for Android applications. It includes the Publishing API for uploading and distributing apps, and the Subscriptions and In-App Purchases API for managing in-app products, subscriptions, and purchase verification.
finops:
- name: Google Play Finops
  service_category: API
  slug: google-play-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-play.png
layout: provider
modified: '2026-05-19'
name: Google Play Developer
nav: Providers
network: true
overview: 'Google Play Developer publishes 1 API on the [APIs.io](https://apis.io/) network: Androidpublisher API. Tagged areas include Android, Application, Google Play, In-App Purchases, and Mobile.


  The Google Play Developer catalog on APIs.io includes 1 Spectral governance ruleset.


  Google Play Developer''s developer surface includes authentication, getting-started guide, pricing, and 7 more developer resources.'
plans:
- name: Google Play Plans Pricing
  plan_count: 3
  slug: google-play-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 5
  name: Google Play Rate Limits
  slug: google-play-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Play Developer API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-play-jsonschema-spectral-rules
scopes:
- name: Google Play Scopes
  scope_count: 1
  slug: google-play-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 32.4
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 60.5
    developer_ergonomics: 23.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 32.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-play/refs/heads/main/screenshots/google-play-2026-06-20T182225.png
security:
- kind: authentication
  name: Google Play Authentication
  slug: google-play-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Play Domain Security
  slug: google-play-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Play Vulnerability Disclosure
  slug: google-play-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-play
tags:
- Android
- Application
- Google Play
- In-App Purchases
- Mobile
- Publishing
- Subscription
---
