---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 45.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Housingfeed Com Agentic Access
  operation_count: 1
  slug: housingfeed-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://housingfeed.com
  baseurl_source: declared
  description: The Sample API from housingfeed-com — 1 operation(s) for sample.
  name: housingfeed-com Sample API
  slug: housingfeed-com-sample-api
artifact_total: 10
common:
- group: design
  href: https://artifacts.apis.io/housingfeed-com/vocabulary/housingfeed-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/housingfeed-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/housingfeed-com/agentic-access/housingfeed-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/housingfeed-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/housingfeed-com/rate-limits/housingfeed-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/housingfeed-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/housingfeed-com/plans/housingfeed-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/housingfeed-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/housingfeed-com/rules/housingfeed-com-rules.yml
  title: ''
  type: Spectral
  url: rules/housingfeed-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/housingfeed-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/housingfeed-com/conventions/housingfeed-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/housingfeed-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/housingfeed-com/authentication/housingfeed-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/housingfeed-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/housingfeed-com/lifecycle/housingfeed-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/housingfeed-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/housingfeed-com/errors/housingfeed-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/housingfeed-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/housingfeed-com/conformance/housingfeed-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/housingfeed-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/housingfeed-com/llms/housingfeed-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/housingfeed-com-llms.txt
- group: build
  href: https://artifacts.apis.io/housingfeed-com/mcp/housingfeed-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/housingfeed-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/housingfeed-com/mcp/housingfeed-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/housingfeed-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/housingfeed-com/well-known/housingfeed-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/housingfeed-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/housingfeed-com/hosts/housingfeed-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/housingfeed-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/housingfeed-com/vendors/housingfeed-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/housingfeed-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.apify.com/v2/acts/housingfeed~rental-listings-api
- group: auth
  href: https://artifacts.apis.io/housingfeed-com/security/housingfeed-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/housingfeed-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://housingfeed.com/
- group: docs
  title: ''
  type: Documentation
  url: https://housingfeed.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://housingfeed.com/real-estate-api
- group: start
  title: ''
  type: GettingStarted
  url: https://housingfeed.com/docs#getting-started
- group: operate
  title: ''
  type: Support
  url: https://housingfeed.com/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://housingfeed.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://housingfeed.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://housingfeed.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iljbrands-boop/housingfeed
created: '2026-10-30'
description: HousingFeed provides a US rental listings data feed and API, aggregating property manager and owner listings directly from their websites and leasing software. The listings are verified weekly, licensed for display in third‑party products, and include detailed fields such as photos, coordinates, and pricing. HousingFeed also offers a separate Data API for internal research and analysis, billed per row. The service targets developers building housing‑related applications, offering free sample data and a transparent pricing model.
image: https://housingfeed.com/assets/housingfeed-icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at housingfeed.com.
  name: housingfeed-com MCP Server
  slug: housingfeed-com-mcp-yml
modified: '2026-10-30'
name: housingfeed-com
nav: Providers
network: true
overview: 'housingfeed-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Sample API. Tagged areas include Real Estate, Rentals, Data API, US, and Listings.


  The housingfeed-com catalog on APIs.io includes 1 Spectral governance ruleset.


  housingfeed-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 22 more developer resources.'
plans:
- name: Housingfeed Com Plans Pricing
  plan_count: 5
  slug: housingfeed-com-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Housingfeed Com Rate Limits
  slug: housingfeed-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: housingfeed-com API Rules
  rule_count: 47
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 1
  slug: housingfeed-com-rules
scopes:
- name: Housingfeed Com Scopes
  scope_count: 0
  slug: housingfeed-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.8
    catalog_earned_first_party: 20.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 47.4
    contract_governance: 35.6
    contract_quality: 44.7
    developer_ergonomics: 35.1
    discoverability: 65.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/housingfeed-com/housingfeed-com-2026-11-03T133500.png
security:
- kind: authentication
  name: Housingfeed Com Authentication
  slug: housingfeed-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Housingfeed Com Domain Security
  slug: housingfeed-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: get-live-sample
  slug: housingfeed-com-get-live-sample
slug: housingfeed-com
tags:
- Real Estate
- Rentals
- Data API
- US
- Listings
website: https://housingfeed.com/
---
