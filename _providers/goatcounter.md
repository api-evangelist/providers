---
access_model:
  confidence: high
  label: Free (donation-supported) · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Goatcounter Agentic Access
  operation_count: 32
  slug: goatcounter-agentic-access
  summary_line: 32 operations · 8 acting
api_count: 2
apis:
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Exports API from GoatCounter — 3 operation(s) for exports.
  name: GoatCounter Exports API
  slug: goatcounter-exports-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Pageviews API from GoatCounter — 1 operation(s) for pageviews.
  name: GoatCounter Pageviews API
  slug: goatcounter-pageviews-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Paths API from GoatCounter — 1 operation(s) for paths.
  name: GoatCounter Paths API
  slug: goatcounter-paths-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Sites API from GoatCounter — 2 operation(s) for sites.
  name: GoatCounter Sites API
  slug: goatcounter-sites-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Statistics API from GoatCounter — 5 operation(s) for statistics.
  name: GoatCounter Statistics API
  slug: goatcounter-statistics-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The Users API from GoatCounter — 1 operation(s) for users.
  name: GoatCounter Users API
  slug: goatcounter-users-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The count API from GoatCounter — 1 operation(s) for count.
  name: GoatCounter Count API
  slug: goatcounter-count-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The export API from GoatCounter — 3 operation(s) for export.
  name: GoatCounter Export API
  slug: goatcounter-export-api
- baseURL: https://{code}.goatcounter.com/api/v0
  baseurl_source: declared
  description: The stats API from GoatCounter — 5 operation(s) for stats.
  name: GoatCounter Stats API
  slug: goatcounter-stats-api
artifact_total: 28
collections:
- collection_type: open
  name: GoatCounter Exports API
  slug: open-goatcounter-exports-api
- collection_type: open
  name: GoatCounter Exports Pageviews API
  slug: open-goatcounter-pageviews-api
- collection_type: open
  name: GoatCounter Exports Paths API
  slug: open-goatcounter-paths-api
- collection_type: open
  name: GoatCounter Exports Sites API
  slug: open-goatcounter-sites-api
- collection_type: open
  name: GoatCounter Exports Statistics API
  slug: open-goatcounter-statistics-api
- collection_type: open
  name: GoatCounter Exports Users API
  slug: open-goatcounter-users-api
- collection_type: open
  name: GoatCounter API
  slug: open-goatcounter
common:
- group: other
  href: https://artifacts.apis.io/goatcounter/capabilities/goatcounter-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/goatcounter-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/goatcounter/agentic-access/goatcounter-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/goatcounter-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/goatcounter/security/goatcounter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goatcounter-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/goatcounter/authentication/goatcounter-authentication.yml
  title: ''
  type: Authentication
  url: authentication/goatcounter-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.goatcounter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.goatcounter.com/help/api
- group: start
  title: ''
  type: SignUp
  url: https://www.goatcounter.com/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arp242/goatcounter
- group: docs
  href: https://artifacts.apis.io/goatcounter/openapi/_original/goatcounter-api-swagger20.json
  title: ''
  type: OpenAPI
  url: openapi/_original/goatcounter-api-swagger20.json
- group: docs
  title: ''
  type: APIReference
  url: https://www.goatcounter.com/api2.html
- group: start
  title: ''
  type: GettingStarted
  url: https://www.goatcounter.com/help/start
- group: operate
  title: ''
  type: Support
  url: https://www.goatcounter.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.goatcounter.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goatcounter.com/help/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goatcounter.com/help/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.goatcounter.com/status
- group: auth
  title: ''
  type: Security
  url: https://www.goatcounter.com/security.txt
- group: auth
  href: https://artifacts.apis.io/goatcounter/well-known/goatcounter-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/goatcounter-security.txt
- group: auth
  href: https://artifacts.apis.io/goatcounter/security/goatcounter-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/goatcounter-vulnerability-disclosure.yml
- group: build
  href: https://artifacts.apis.io/goatcounter/packages/goatcounter-packages.yml
  title: ''
  type: Packages
  url: packages/goatcounter-packages.yml
- group: build
  href: https://artifacts.apis.io/goatcounter/cli/goatcounter-cli.yml
  title: ''
  type: CLI
  url: cli/goatcounter-cli.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/components/goatcounter-components.yml
  title: ''
  type: Components
  url: components/goatcounter-components.yml
- group: start
  href: https://artifacts.apis.io/goatcounter/sandbox/goatcounter-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/goatcounter-sandbox.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/conventions/goatcounter-conventions.yml
  title: ''
  type: Conventions
  url: conventions/goatcounter-conventions.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/errors/goatcounter-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/goatcounter-problem-types.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/data-model/goatcounter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/goatcounter-data-model.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/lifecycle/goatcounter-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/goatcounter-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/goatcounter/changelog/goatcounter-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goatcounter-changelog.yml
- group: design
  href: https://artifacts.apis.io/goatcounter/conformance/goatcounter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goatcounter-conformance.yml
- group: other
  href: https://artifacts.apis.io/goatcounter/overlays/goatcounter-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/goatcounter-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/goatcounter/llms/goatcounter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/goatcounter-llms.txt
- group: agent
  href: https://artifacts.apis.io/goatcounter/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://artifacts.apis.io/goatcounter/plans/goatcounter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goatcounter-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/goatcounter/rate-limits/goatcounter-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/goatcounter-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/goatcounter/finops/goatcounter-finops.yml
  title: ''
  type: FinOps
  url: finops/goatcounter-finops.yml
created: '2025-02-08'
description: GoatCounter is open-source, privacy-friendly web analytics from Martin Tournoij, offered both as a free donation-supported hosted service at goatcounter.com and as a self-hostable Go binary backed by SQLite or PostgreSQL. It tracks pageviews without cookies or persistent personal identifiers. The unversioned JSON API, prefixed /api/v0 and served from each account's own subdomain, covers counting pageviews and events from a backend, reading dashboard statistics (totals, per-path hits, referrals, browser/system/location breakdowns), running asynchronous CSV and JSON exports with an incremental hit-ID cursor, and managing sites and users. Authentication is a per-site API key sent as an HTTP bearer token, and the provider publishes its own OpenAPI 2.0 contract at https://www.goatcounter.com/api.json.
finops:
- has_sources: true
  method: derived
  name: Goatcounter Finops
  primary_unit: ''
  service_category: ''
  slug: goatcounter-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goatcounter.png
layout: provider
modified: '2026-08-13'
name: GoatCounter
nav: Providers
network: true
overview: 'GoatCounter publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Exports API, Pageviews API, Paths API, and 6 more. Tagged areas include Analytics, Page Views, Privacy, Statistics, and Web Analytics.


  The GoatCounter catalog on APIs.io includes 1 Spectral governance ruleset.


  GoatCounter''s developer surface includes authentication, documentation, signup flow, API reference, getting-started guide, support, pricing, and 28 more developer resources.'
plans:
- name: Goatcounter Plans Pricing
  plan_count: 1
  slug: goatcounter-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Goatcounter Rate Limits
  slug: goatcounter-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: GoatCounter API Rules
  rule_count: 52
  severity_counts:
    error: 46
    hint: 0
    info: 1
    warn: 5
  slug: goatcounter-rules
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.5
    catalog_earned_first_party: 16.0
    catalog_gap: 57.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 46.6
    developer_ergonomics: 61.3
    discoverability: 66.1
    operational_transparency: 52.6
  previous_composite: 52.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 33.3
      total: 9
    mcp: derived
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
screenshot: https://apis.io/screenshots/goatcounter/goatcounter-2026-06-20T181940.png
security:
- kind: authentication
  name: Goatcounter Authentication
  slug: goatcounter-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Goatcounter Domain Security
  slug: goatcounter-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Goatcounter Vulnerability Disclosure
  slug: goatcounter-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 4
skills:
- name: Build a custom dashboard from GoatCounter statistics
  slug: goatcounter-build-a-custom-dashboard
- name: Count pageviews from a backend
  slug: goatcounter-count-pageviews-from-a-backend
- name: Export and incrementally sync raw pageview data
  slug: goatcounter-export-and-sync-raw-data
- name: Manage GoatCounter sites and verify API key permissions
  slug: goatcounter-manage-sites-and-keys
slug: goatcounter
tags:
- Analytics
- Page Views
- Privacy
- Statistics
- Web Analytics
- Open Source
- Self-Hosted
- Event
- Data Export
- Developer Tools
website: https://www.goatcounter.com/
---
