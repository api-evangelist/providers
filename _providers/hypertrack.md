---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: Obtain and use access tokens for the HyperTrack API.
  name: HyperTrack Authentication API
  slug: hypertrack-authentication-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Export API from HyperTrack — 2 operation(s) for export.
  name: HyperTrack Export API
  slug: hypertrack-export-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Geotags API from HyperTrack — 2 operation(s) for geotags.
  name: HyperTrack Geotags API
  slug: hypertrack-geotags-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Nearby API from HyperTrack — 2 operation(s) for nearby.
  name: HyperTrack Nearby API
  slug: hypertrack-nearby-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Orders API from HyperTrack — 32 operation(s) for orders.
  name: HyperTrack Orders API
  slug: hypertrack-orders-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Places API from HyperTrack — 7 operation(s) for places.
  name: HyperTrack Places API
  slug: hypertrack-places-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Tracking API from HyperTrack — 1 operation(s) for tracking.
  name: HyperTrack Tracking API
  slug: hypertrack-tracking-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Visits API from HyperTrack — 4 operation(s) for visits.
  name: HyperTrack Visits API
  slug: hypertrack-visits-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The WorkerExport API from HyperTrack — 2 operation(s) for workerexport.
  name: HyperTrack Worker Export API
  slug: hypertrack-workerexport-api
- baseURL: https://v3.api.hypertrack.com
  baseurl_source: declared
  description: The Workers API from HyperTrack — 14 operation(s) for workers.
  name: HyperTrack Workers API
  slug: hypertrack-workers-api
artifact_total: 19
asyncapis:
- description: ''
  name: Hypertrack Events Webhooks
  slug: hypertrack-events-webhooks
common:
- group: other
  href: https://artifacts.apis.io/hypertrack/capabilities/hypertrack-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/hypertrack-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/hypertrack/overlays/hypertrack-hypertrack-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/hypertrack-hypertrack-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://hypertrack.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hypertrack.com/docs/introduction
- group: docs
  title: ''
  type: Documentation
  url: https://hypertrack.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://hypertrack.com/reference/get-orders
- group: start
  title: ''
  type: GettingStarted
  url: https://hypertrack.com/docs/build-your-app
- group: operate
  title: ''
  type: Support
  url: https://hypertrack.com/contact
- group: company
  title: ''
  type: Blog
  url: https://stories.hypertrack.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://stories.hypertrack.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hypertrack
- group: commercial
  title: ''
  type: Pricing
  url: https://hypertrack.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.hypertrack.com/signup
- group: start
  title: ''
  type: Login
  url: https://dashboard.hypertrack.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hypertrack.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hypertrack.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.hypertrack.com/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/hypertrack/hypertrack/documentation/krztgzd/hypertrack-api
- group: build
  href: https://artifacts.apis.io/hypertrack/packages/hypertrack-packages.yml
  title: ''
  type: Packages
  url: packages/hypertrack-packages.yml
- group: build
  href: https://artifacts.apis.io/hypertrack/packages/hypertrack-packages.yml
  title: ''
  type: SDKs
  url: packages/hypertrack-packages.yml
- group: agent
  href: https://artifacts.apis.io/hypertrack/llms/hypertrack-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hypertrack-llms.txt
- group: agent
  href: https://artifacts.apis.io/hypertrack/mcp/hypertrack-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/hypertrack-mcp.yml
- group: agent
  href: https://artifacts.apis.io/hypertrack/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hypertrack/lifecycle/hypertrack-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hypertrack-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hypertrack/conformance/hypertrack-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hypertrack-conformance.yml
- group: auth
  href: https://artifacts.apis.io/hypertrack/security/hypertrack-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hypertrack-domain-security.yml
- group: commercial
  href: https://artifacts.apis.io/hypertrack/plans/hypertrack-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/hypertrack-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/hypertrack/rate-limits/hypertrack-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/hypertrack-rate-limits.yml
- group: start
  href: https://artifacts.apis.io/hypertrack/sandbox/hypertrack-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/hypertrack-sandbox.yml
- group: operate
  href: https://artifacts.apis.io/hypertrack/changelog/hypertrack-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/hypertrack-changelog.yml
- group: design
  href: https://artifacts.apis.io/hypertrack/components/hypertrack-components.yml
  title: ''
  type: Components
  url: components/hypertrack-components.yml
created: '2026-08-22'
description: HyperTrack is a location-intelligence platform for shift work, field service and last-mile delivery. Its mobile SDKs (iOS, Android, React Native, Flutter, Expo, Ionic Capacitor and .NET MAUI) collect ground-truth location from a worker's device, and its REST API — the HyperTrack API at https://v3.api.hypertrack.com — turns that stream into Orders, Workers, Places, Routes, Visits, Geotags and Nearby search, plus webhooks for order, route, worker, geofence, outage and trip events. Companies use it to verify time and attendance, detect no-call-no-show risk, plan and optimise routes, and close out shifts for pay and billing. HyperTrack publishes a machine-readable OpenAPI 3.0.3 definition, an llms.txt index, an npm-distributed MCP server, and an open-source Agent Skill for coding agents.
finops:
- has_sources: true
  method: derived
  name: Hypertrack Finops
  primary_unit: user
  service_category: ''
  slug: hypertrack-finops
  template: false
image: https://hypertrack.com/images/og-home.png
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 21 tools listed.
  name: HyperTrack MCP Server
  slug: hypertrack-mcp-server
modified: '2026-08-22'
name: HyperTrack
nav: Providers
network: true
overview: 'HyperTrack publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Authentication API, Export API, Geotags API, and 7 more. Tagged areas include Company, Location, Geolocation, Tracking, and Logistics.


  The HyperTrack catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  HyperTrack''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 24 more developer resources.'
plans:
- name: Hypertrack Plans Pricing
  plan_count: 8
  slug: hypertrack-plans-pricing
- name: Hypertrack Price Estimates
  plan_count: 0
  slug: hypertrack-price-estimates
random_paper: 5
rate_limits:
- limit_count: 0
  name: Hypertrack Rate Limits
  slug: hypertrack-rate-limits
score:
  band: strong
  composite: 62.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 4.5
    contract_quality: 59.1
    developer_ergonomics: 83.3
    discoverability: 65.0
    operational_transparency: 44.7
  previous_composite: 61.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/hypertrack/hypertrack-2026-09-02T145808.png
security:
- kind: authentication
  name: Hypertrack Authentication
  slug: hypertrack-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Hypertrack Domain Security
  slug: hypertrack-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: hypertrack-integration
  slug: hypertrack-SKILL
slug: hypertrack
tags:
- Company
- Location
- Geolocation
- Tracking
- Logistics
- Last Mile Delivery
- Field Service Management
- Workforce
- Time and Attendance
- Mobile SDK
- Geofencing
- Routing
website: https://hypertrack.com/
---
