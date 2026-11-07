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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 58.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Statable Stats Api Agentic Access
  operation_count: 35
  slug: statable-stats-api-agentic-access
  summary_line: 35 operations · 20 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://statable.com/api/v1
  baseurl_source: declared
  description: Register an account and obtain its first API key without a browser. The only operations in this spec that take NO bearer token. Behind the server-side `API_BOOTSTRAP_ENABLED` flag; while it is off bot
  name: Statable Stats API Bootstrap API
  slug: statable-stats-api-bootstrap-api
- baseURL: https://statable.com/api/v1
  baseurl_source: declared
  description: Manage API keys (write surface). Requires the `keys:manage` scope and the server-side `API_WRITE_ENABLED` flag; while the flag is off every route here answers 404 `write_disabled`. See docs/api-v1-wri
  name: Statable Stats API Keys API
  slug: statable-stats-api-keys-api
- baseURL: https://statable.com/api/v1
  baseurl_source: declared
  description: Create, change and delete sites (write surface). Requires the `sites:write` scope and the server-side `API_WRITE_ENABLED` flag; the snippet route needs only `read`. See docs/api-v1-write-surface.md §5
  name: Statable Stats API Sites API
  slug: statable-stats-api-sites-api
- baseURL: https://statable.com/api/v1
  baseurl_source: declared
  description: Read analytics data.
  name: Statable Stats API Stats API
  slug: statable-stats-api-stats-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Blog
  url: https://statable.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://statable.com/blog/feed.xml
- group: agent
  title: ''
  type: MCPServer
  url: https://mcp.statable.com/mcp
- group: company
  title: ''
  type: Website
  url: https://statable.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://statable.com/docs/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://statable.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://statable.com/docs/getting-started/quick-start/
- group: operate
  title: ''
  type: Support
  url: https://statable.com/docs/help/service-status/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/key-arg
- group: commercial
  title: ''
  type: Pricing
  url: https://statable.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://statable.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://statable.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://statable.com/privacy
- group: auth
  title: ''
  type: Security
  url: https://statable.com/security
- group: auth
  title: ''
  type: Compliance
  url: https://statable.com/gdpr
- group: operate
  title: ''
  type: StatusPage
  url: https://status.statable.com
- group: agent
  href: https://artifacts.apis.io/statable-stats-api/agentic-access/statable-stats-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/statable-stats-api-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/statable-stats-api/authentication/statable-stats-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/statable-stats-api-authentication.yml
- group: auth
  href: https://artifacts.apis.io/statable-stats-api/scopes/statable-stats-api-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/statable-stats-api-scopes.yml
- group: auth
  href: https://artifacts.apis.io/statable-stats-api/security/statable-stats-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statable-stats-api-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/statable-stats-api/security/statable-stats-api-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/statable-stats-api-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/statable-stats-api/security/statable-stats-api-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/statable-stats-api-trust-center.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/conformance/statable-stats-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/statable-stats-api-conformance.yml
- group: agent
  href: https://artifacts.apis.io/statable-stats-api/well-known/statable-stats-api-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statable-stats-api-well-known.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/errors/statable-stats-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/statable-stats-api-problem-types.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/lifecycle/statable-stats-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/statable-stats-api-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/statable-stats-api/rate-limits/statable-stats-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/statable-stats-api-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/conventions/statable-stats-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/statable-stats-api-conventions.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/conventions/statable-stats-api-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/statable-stats-api-conventions.yml
- group: build
  href: https://artifacts.apis.io/statable-stats-api/packages/statable-stats-api-packages.yml
  title: ''
  type: Packages
  url: packages/statable-stats-api-packages.yml
- group: build
  href: https://artifacts.apis.io/statable-stats-api/packages/statable-stats-api-packages.yml
  title: ''
  type: SDKs
  url: packages/statable-stats-api-packages.yml
- group: build
  href: https://artifacts.apis.io/statable-stats-api/cli/statable-stats-api-cli.yml
  title: ''
  type: CLI
  url: cli/statable-stats-api-cli.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/components/statable-stats-api-components.yml
  title: ''
  type: Components
  url: components/statable-stats-api-components.yml
- group: design
  href: https://artifacts.apis.io/statable-stats-api/data-model/statable-stats-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/statable-stats-api-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/statable-stats-api/plans/statable-stats-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/statable-stats-api-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/statable-stats-api/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/statable-stats-api/overlays/statable-stats-api-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/statable-stats-api-openapi-overlay.yaml
created: '2026-09-18'
description: Privacy-first, cookieless web analytics from Statable (Key Arg B.V.), EU-hosted in the Netherlands with GDPR compliance and a ~2 KB tracking script. Exposes a server-side REST HTTP API with a public OpenAPI 3.1 contract, a hosted MCP server, an llms.txt, and a CLI for querying visitors, pages, sources, goals, funnels, custom events and live visitors.
finops:
- has_sources: true
  method: derived
  name: Statable Stats Api Finops
  primary_unit: pageviews
  service_category: ''
  slug: statable-stats-api-finops
  template: false
image: https://statable.com/thumbnail.png
layout: provider
mcp_servers:
- description: ''
  name: Statable Stats API MCP Server
  slug: mcp
modified: '2026-10-06'
name: Statable Stats API
nav: Providers
network: true
overview: 'Statable Stats API publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bootstrap API, Keys API, Sites API, and 1 more. Tagged areas include Analytics, Web Analytics, Cookieless, Privacy, and GDPR.


  The Statable Stats API catalog on APIs.io includes 1 Spectral governance ruleset.


  Statable Stats API''s developer surface includes engineering blog, documentation, getting-started guide, support, pricing, signup flow, authentication, and 30 more developer resources.'
plans:
- name: Statable Stats Api Plans Pricing
  plan_count: 18
  slug: statable-stats-api-plans-pricing
- name: Statable Stats Api Price Estimates
  plan_count: 0
  slug: statable-stats-api-price-estimates
random_paper: 11
rate_limits:
- limit_count: 0
  name: Statable Stats Api Rate Limits
  slug: statable-stats-api-rate-limits
rules:
- authorship: generated
  effective_rule_count: 101
  extends:
  - spectral:oas
  name: Statable Stats API API Rules
  rule_count: 60
  severity_counts:
    error: 52
    hint: 0
    info: 1
    warn: 7
  slug: statable-stats-api-rules
scopes:
- name: Statable Stats Api Scopes
  scope_count: 2
  slug: statable-stats-api-scopes
  summary_line: 2 scopes
score:
  band: exemplar
  composite: 69.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 53.0
    developer_ergonomics: 73.2
    discoverability: 75.0
    operational_transparency: 21.1
  previous_composite: 69.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 38.9
screenshot: https://apis.io/screenshots/statable-stats-api/statable-stats-api-2026-10-11T130348.png
security:
- kind: authentication
  name: Statable Stats Api Authentication
  slug: statable-stats-api-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Statable Stats Api Domain Security
  slug: statable-stats-api-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Statable Stats Api Vulnerability Disclosure
  slug: statable-stats-api-vulnerability-disclosure
  summary_line: contact published
- kind: trust-center
  name: Statable Stats Api Trust Center
  slug: statable-stats-api-trust-center
  summary_line: trust center published
skill_count: 4
skills:
- name: Create goals and funnels and run a funnel report
  slug: statable-stats-api-goals-and-funnels
- name: Manage API keys over HTTP
  slug: statable-stats-api-manage-keys
- name: Query a site's analytics
  slug: statable-stats-api-query-analytics
- name: Register and provision a site without a browser
  slug: statable-stats-api-register-and-provision
slug: statable-stats-api
tags:
- Analytics
- Web Analytics
- Cookieless
- Privacy
- GDPR
- OpenAPI
- MCP
- Llms.txt
- EU-hosted
website: https://statable.com
---
