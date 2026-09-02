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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Goatcounter Agentic Access
  operation_count: 16
  slug: goatcounter-agentic-access
  summary_line: 16 operations · 5 acting
api_count: 2
apis:
- description: The Exports API from GoatCounter — 3 operation(s) for exports.
  name: GoatCounter Exports API
  slug: goatcounter-exports-api
- description: The Pageviews API from GoatCounter — 1 operation(s) for pageviews.
  name: GoatCounter Pageviews API
  slug: goatcounter-pageviews-api
- description: The Paths API from GoatCounter — 1 operation(s) for paths.
  name: GoatCounter Paths API
  slug: goatcounter-paths-api
- description: The Sites API from GoatCounter — 2 operation(s) for sites.
  name: GoatCounter Sites API
  slug: goatcounter-sites-api
- description: The Statistics API from GoatCounter — 5 operation(s) for statistics.
  name: GoatCounter Statistics API
  slug: goatcounter-statistics-api
- description: The Users API from GoatCounter — 1 operation(s) for users.
  name: GoatCounter Users API
  slug: goatcounter-users-api
- description: The count API from GoatCounter — 1 operation(s) for count.
  name: GoatCounter Count API
  slug: goatcounter-count-api
- description: The export API from GoatCounter — 3 operation(s) for export.
  name: GoatCounter Export API
  slug: goatcounter-export-api
- description: The stats API from GoatCounter — 5 operation(s) for stats.
  name: GoatCounter Stats API
  slug: goatcounter-stats-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/goatcounter-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goatcounter-domain-security.yml
- group: auth
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
  title: ''
  type: SecurityTxt
  url: well-known/goatcounter-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/goatcounter-vulnerability-disclosure.yml
- group: build
  title: ''
  type: Packages
  url: packages/goatcounter-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/goatcounter-cli.yml
- group: design
  title: ''
  type: Components
  url: components/goatcounter-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/goatcounter-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goatcounter-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goatcounter-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goatcounter-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goatcounter-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/goatcounter-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goatcounter-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/goatcounter-api-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goatcounter-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/goatcounter-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goatcounter-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/goatcounter-finops.yml
created: '2025-02-08'
description: GoatCounter is open-source, privacy-friendly web analytics from Martin Tournoij, offered both as a free donation-supported hosted service at goatcounter.com and as a self-hostable Go binary backed by SQLite or PostgreSQL. It tracks pageviews without cookies or persistent personal identifiers. The unversioned JSON API, prefixed /api/v0 and served from each account's own subdomain, covers counting pageviews and events from a backend, reading dashboard statistics (totals, per-path hits, referrals, browser/system/location breakdowns), running asynchronous CSV and JSON exports with an incremental hit-ID cursor, and managing sites and users. Authentication is a per-site API key sent as an HTTP bearer token, and the provider publishes its own OpenAPI 2.0 contract at https://www.goatcounter.com/api.json.
finops:
- name: Goatcounter Finops
  service_category: API
  slug: goatcounter-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/goatcounter.png
layout: provider
modified: '2026-08-13'
name: GoatCounter
nav: Providers
network: true
overview: 'GoatCounter publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Exports API, Pageviews API, Paths API, and 6 more. Tagged areas include Analytics, Page Views, Privacy, Statistics, and Web Analytics.


  GoatCounter''s developer surface includes authentication, documentation, signup flow, API reference, getting-started guide, support, pricing, and 27 more developer resources.'
plans:
- name: Goatcounter Plans Pricing
  plan_count: 1
  slug: goatcounter-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Goatcounter Rate Limits
  slug: goatcounter-rate-limits
score:
  band: developing
  composite: 52.7
  coverage:
    artifact_dirs: 24
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.2
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 4.5
    contract_quality: 50.0
    developer_ergonomics: 61.3
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 52.6
  previous_composite: 52.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 66.7
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/goatcounter/refs/heads/main/screenshots/goatcounter-2026-06-20T181940.png
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
slug: goatcounter
tags:
- Analytics
- Page Views
- Privacy
- Statistics
- Web Analytics
- Open-Source
- Self-Hosted
- Event
- Data Export
- Developer Tools
website: https://www.goatcounter.com/
---
