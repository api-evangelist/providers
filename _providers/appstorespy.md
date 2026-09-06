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
  - rate-limits
  - security
  trial: false
  try_now: true
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Appstorespy Agentic Access
  operation_count: 33
  slug: appstorespy-agentic-access
  summary_line: 33 operations · 7 acting
api_count: 1
apis:
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The App Store API from AppstoreSpy — 14 operation(s) for app store.
  name: AppstoreSpy App Store API
  slug: appstorespy-app-store-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Events API from AppstoreSpy — 1 operation(s) for events.
  name: AppstoreSpy Events API
  slug: appstorespy-events-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Google Play API from AppstoreSpy — 17 operation(s) for google play.
  name: AppstoreSpy Google Play API
  slug: appstorespy-google-play-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Jobs API from AppstoreSpy — 1 operation(s) for jobs.
  name: AppstoreSpy Jobs API
  slug: appstorespy-jobs-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Search Filter v.2 API from AppstoreSpy — 1 operation(s) for search filter v.2.
  name: AppstoreSpy Search Filter v.2 API
  slug: appstorespy-search-filter-v-2-api
- baseURL: https://api.appstorespy.com/v1
  baseurl_source: declared
  description: The Suggestions API from AppstoreSpy — 1 operation(s) for suggestions.
  name: AppstoreSpy Suggestions API
  slug: appstorespy-suggestions-api
artifact_total: 11
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
overview: 'AppstoreSpy publishes 6 APIs on the [APIs.io](https://apis.io/) network, including App Store API, Events API, Google Play API, and 3 more. Tagged areas include Mobile Apps, App Store Optimization, Market Intelligence, App Analytics, and Google Play.


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
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 4.5
    contract_quality: 53.7
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 50.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/appstorespy/refs/heads/main/screenshots/appstorespy-2026-09-02T144124.png
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
- Mobile Apps
- App Store Optimization
- Market Intelligence
- App Analytics
- Google Play
- apple-app-store
- Reviews and Ratings
- download-revenue-estimates
- Marketing
website: https://appstorespy.com/app-store-api
---
