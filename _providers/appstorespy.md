---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
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
  score: 31.5
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Appstorespy Agentic Access
  operation_count: 33
  slug: appstorespy-agentic-access
  summary_line: 33 operations · 7 acting
api_count: 1
apis:
- description: 'Public REST API for App Store and Google Play data: app lookup, search, filter search, reviews, rankings, download/revenue estimates, developer lookup, daily installs, keyword suggestions, LiveOps eve'
  name: AppstoreSpy API
  slug: appstorespy-api
artifact_total: 6
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/appstorespy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/appstorespy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/appstorespy-authentication.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/appstorespy-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/appstorespy-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/appstorespy-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/appstorespy-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/appstorespy-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/appstorespy-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/appstorespy-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/appstorespy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/appstorespy-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/appstorespy-packages.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appstorespy.com/app-store-api
- group: docs
  title: ''
  type: APIReference
  url: https://api.appstorespy.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://appstorespy.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://appstorespy.com/sign_up
- group: start
  title: ''
  type: Login
  url: https://appstorespy.com/sign_in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appstorespy.com/agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appstorespy.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://appstorespy.com/support
- group: company
  title: ''
  type: Blog
  url: https://appstorespy.com/blog
created: '2026-08-21'
description: Mobile-app market-intelligence provider exposing a public REST API for App Store (iOS) and Google Play data, including app metadata, reviews, rankings, download/revenue estimates, developer lookup, keyword suggestions, and LiveOps events. Covers 13 million apps across 100 countries.
image: https://appstorespy.com/s/icons/android-icon-192x192.png
layout: provider
modified: '2026-08-22'
name: AppstoreSpy
nav: Providers
network: true
overview: 'AppstoreSpy publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include mobile-apps, app-store-optimization, market-intelligence, app-analytics, and google-play.


  AppstoreSpy''s developer surface includes authentication, API reference, pricing, signup flow, support, engineering blog, and 17 more developer resources.'
plans:
- name: Appstorespy Plans Pricing
  plan_count: 4
  slug: appstorespy-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Appstorespy Rate Limits
  slug: appstorespy-rate-limits
score:
  band: developing
  composite: 50.3
  delta: 1.9
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 16.7
    contract_quality: 50.7
    developer_ergonomics: 47.0
    discoverability: 68.5
    governance: 16.7
    operational_transparency: 31.6
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Appstorespy Authentication
  slug: appstorespy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appstorespy Domain Security
  slug: appstorespy-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: appstorespy
tags:
- mobile-apps
- app-store-optimization
- market-intelligence
- app-analytics
- google-play
- apple-app-store
- reviews-and-ratings
- download-revenue-estimates
- marketing
website: https://appstorespy.com/app-store-api
---
