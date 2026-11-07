---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
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
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
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
    mcp_server: verified
    mcp_tool_quality: full
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appstorespy Agentic Access
  operation_count: 36
  slug: appstorespy-agentic-access
  summary_line: 36 operations · 1 acting
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
artifact_total: 38
common:
- group: commercial
  href: https://artifacts.apis.io/appstorespy/finops/appstorespy-finops.yml
  title: ''
  type: FinOps
  url: finops/appstorespy-finops.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/rules/appstorespy-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/appstorespy-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/rules/appstorespy-rules.yml
  title: ''
  type: Spectral
  url: rules/appstorespy-rules.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/json-ld/appstorespy-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appstorespy-context.jsonld
- group: design
  href: https://artifacts.apis.io/appstorespy/vocabulary/appstorespy-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appstorespy-vocabulary.yml
- group: operate
  href: https://artifacts.apis.io/appstorespy/changelog/appstorespy-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/appstorespy-changelog.yml
- group: auth
  href: https://artifacts.apis.io/appstorespy/security/appstorespy-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/appstorespy-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/appstorespy/a2a/appstorespy-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/appstorespy-a2a.yml
- group: build
  href: https://artifacts.apis.io/appstorespy/mcp/appstorespy-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/appstorespy-tool-crosswalk.yml
- group: auth
  href: https://artifacts.apis.io/appstorespy/well-known/appstorespy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/appstorespy-security.txt
- group: other
  href: https://artifacts.apis.io/appstorespy/hosts/appstorespy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appstorespy-hosts.yml
- group: other
  href: https://artifacts.apis.io/appstorespy/vendors/appstorespy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appstorespy-vendors.yml
- group: build
  title: ''
  type: SDKs
  url: https://appstorespy.com/sdk
- group: start
  title: ''
  type: GettingStarted
  url: https://api.appstorespy.com/getting-started
- group: auth
  href: https://artifacts.apis.io/appstorespy/security/appstorespy-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/appstorespy-vulnerability-disclosure.yml
- group: other
  href: https://artifacts.apis.io/appstorespy/capabilities/appstorespy-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/appstorespy-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://www.appstorespy.com/
- group: agent
  href: https://artifacts.apis.io/appstorespy/agentic-access/appstorespy-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appstorespy-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/appstorespy/security/appstorespy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appstorespy-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/appstorespy/authentication/appstorespy-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appstorespy-authentication.yml
- group: agent
  href: https://artifacts.apis.io/appstorespy/llms/appstorespy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appstorespy-llms.txt
- group: other
  href: https://artifacts.apis.io/appstorespy/overlays/appstorespy-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/appstorespy-openapi-overlay.yaml
- group: design
  href: https://artifacts.apis.io/appstorespy/conformance/appstorespy-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appstorespy-conformance.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/errors/appstorespy-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appstorespy-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/lifecycle/appstorespy-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/appstorespy-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/conventions/appstorespy-conventions.yml
  title: ''
  type: Conventions
  url: conventions/appstorespy-conventions.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/data-model/appstorespy-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appstorespy-data-model.yml
- group: agent
  href: https://artifacts.apis.io/appstorespy/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/appstorespy/plans/appstorespy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appstorespy-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/appstorespy/rate-limits/appstorespy-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/appstorespy-rate-limits.yml
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
- group: agent
  title: ''
  type: MCPServer
  url: https://api.appstorespy.com/mcp
- group: other
  title: ''
  type: APICatalog
  url: https://api.appstorespy.com/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: https://api.appstorespy.com/.well-known/security.txt
- group: agent
  href: https://artifacts.apis.io/appstorespy/well-known/appstorespy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appstorespy-well-known.yml
- group: other
  title: ''
  type: APIsJSON
  url: https://api.appstorespy.com/apis.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.appstorespy.com/changelog
- group: operate
  title: ''
  type: StatusPage
  url: https://api.appstorespy.com/status
- group: operate
  title: ''
  type: Deprecation
  url: https://api.appstorespy.com/deprecation-policy
- group: operate
  title: ''
  type: Roadmap
  url: https://api.appstorespy.com/roadmap
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/romamo/appstorespy-api-docs
- group: build
  title: ''
  type: PostmanCollection
  url: https://raw.githubusercontent.com/romamo/appstorespy-api-docs/main/postman/appstorespy.postman_collection.json
- group: build
  title: ''
  type: Examples
  url: https://github.com/romamo/appstorespy-api-docs/tree/main/examples
- group: design
  href: https://artifacts.apis.io/appstorespy/rules/appstorespy-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/appstorespy-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/appstorespy/vocabulary/appstorespy-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/appstorespy-vocabulary.yaml
created: '2026-08-21'
description: Mobile-app market-intelligence provider exposing a public REST API for App Store (iOS) and Google Play data, including app metadata, reviews, rankings, download/revenue estimates, developer lookup, keyword suggestions, and LiveOps events. Covers 13 million apps across 100 countries.
finops:
- has_sources: true
  method: derived
  name: Appstorespy Finops
  primary_unit: 1 user
  service_category: ''
  slug: appstorespy-finops
  template: false
image: https://appstorespy.com/s/icons/android-icon-192x192.png
json_schemas:
- name: Event
  property_count: 13
  slug: appstorespy-event
- name: IosAppListResponse
  property_count: 3
  slug: appstorespy-ios-app-list-response
- name: IosApp
  property_count: 50
  slug: appstorespy-ios-app
- name: IosAppSearchBody
  property_count: 7
  slug: appstorespy-ios-app-search-body
- name: IosDev
  property_count: 15
  slug: appstorespy-ios-dev
- name: IosDevSearchBody
  property_count: 5
  slug: appstorespy-ios-dev-search-body
- name: IosReview
  property_count: 8
  slug: appstorespy-ios-review
- name: IosSimilarSearchBody
  property_count: 9
  slug: appstorespy-ios-similar-search-body
- name: PlayApp
  property_count: 57
  slug: appstorespy-play-app
- name: PlayAppSearchBody
  property_count: 7
  slug: appstorespy-play-app-search-body
- name: PlayDev
  property_count: 22
  slug: appstorespy-play-dev
- name: PlayListing
  property_count: 15
  slug: appstorespy-play-listing
- name: PlayReview
  property_count: 12
  slug: appstorespy-play-review
- name: SearchCreate
  property_count: 8
  slug: appstorespy-search-create
- name: SearchResult
  property_count: 11
  slug: appstorespy-search-result
- name: SimilarSearchBody
  property_count: 9
  slug: appstorespy-similar-search-body
- name: SuggestLite
  property_count: 6
  slug: appstorespy-suggest-lite
- name: Suggest
  property_count: 9
  slug: appstorespy-suggest
- name: SummaryResponse
  property_count: 6
  slug: appstorespy-summary-response
jsonld:
- class_count: 59
  name: Appstorespy Context
  property_count: 158
  slug: appstorespy-context
layout: provider
mcp_servers:
- description: ''
  name: AppstoreSpy MCP Server
  slug: mcp
modified: '2026-08-22'
name: AppstoreSpy
nav: Providers
network: true
overview: 'AppstoreSpy publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including App Store API, Events API, Google Play API, and 3 more. Tagged areas include Mobile App, App Store Optimization, Market Intelligence, App Analytics, and Google Play.


  The AppstoreSpy catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  AppstoreSpy''s developer surface includes changelog, getting-started guide, authentication, API reference, pricing, signup flow, support, and 46 more developer resources.'
plans:
- name: Appstorespy Plans Pricing
  plan_count: 4
  slug: appstorespy-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 4
  name: Appstorespy Rate Limits
  slug: appstorespy-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: AppstoreSpy API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: appstorespy-rules
- authorship: provider
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AppstoreSpy API Rules
  rule_count: 12
  severity_counts:
    error: 3
    hint: 0
    info: 4
    warn: 5
  slug: appstorespy-spectral-rules
score:
  band: exemplar
  composite: 69.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 93.0
    catalog_earned_first_party: 24.0
    catalog_gap: 22.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.4
  facets:
    access_clarity: 84.2
    contract_governance: 31.8
    contract_quality: 69.4
    developer_ergonomics: 64.9
    discoverability: 78.3
    operational_transparency: 69.7
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 50.0
      total: 12
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/appstorespy/appstorespy-2026-09-02T144124.png
security:
- kind: authentication
  name: Appstorespy Authentication
  slug: appstorespy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Appstorespy Domain Security
  slug: appstorespy-domain-security
  summary_line: TLSv1.2 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Appstorespy Vulnerability Disclosure
  slug: appstorespy-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 2
skills:
- name: appstorespy-app-intelligence-lookup
  slug: appstorespy-app-intelligence-lookup
- name: appstorespy-market-discovery
  slug: appstorespy-market-discovery
slug: appstorespy
tags:
- Mobile App
- App Store Optimization
- Market Intelligence
- App Analytics
- Google Play
- apple-app-store
- Reviews and Ratings
- download-revenue-estimates
- Marketing
website: https://www.appstorespy.com/
---
