---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Thirdtrail Life Agentic Access
  operation_count: 26
  slug: thirdtrail-life-agentic-access
  summary_line: 26 operations · 8 acting
api_count: 1
apis:
- baseURL: https://thirdtrail.life
  baseurl_source: declared
  description: Sun and moon rise, set, transit, twilight and phase.
  name: thirdtrail-life Ephemerides API
  slug: thirdtrail-life-ephemerides-api
- baseURL: https://thirdtrail.life
  baseurl_source: declared
  description: The mcp API from thirdtrail-life — 1 operation(s) for mcp.
  name: thirdtrail-life MCP API
  slug: thirdtrail-life-mcp-api
- baseURL: https://thirdtrail.life
  baseurl_source: declared
  description: Solar position and clear-sky irradiance (NREL SPA-equivalent, Bird model).
  name: thirdtrail-life Solar API
  slug: thirdtrail-life-solar-api
- baseURL: https://thirdtrail.life
  baseurl_source: declared
  description: Astronomical tides from the FES2022 global atlas.
  name: thirdtrail-life Tides API
  slug: thirdtrail-life-tides-api
- baseURL: https://thirdtrail.life
  baseurl_source: declared
  description: Connectivity and key-verification helpers.
  name: thirdtrail-life Utility API
  slug: thirdtrail-life-utility-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/thirdtrail-life/agentic-access/thirdtrail-life-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/thirdtrail-life-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/thirdtrail-life/rate-limits/thirdtrail-life-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/thirdtrail-life-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/thirdtrail-life/plans/thirdtrail-life-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/thirdtrail-life-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/thirdtrail-life/rules/thirdtrail-life-rules.yml
  title: ''
  type: Spectral
  url: rules/thirdtrail-life-rules.yml
- group: design
  href: https://artifacts.apis.io/thirdtrail-life/vocabulary/thirdtrail-life-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/thirdtrail-life-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/thirdtrail-life/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/thirdtrail-life/authentication/thirdtrail-life-authentication.yml
  title: ''
  type: Authentication
  url: authentication/thirdtrail-life-authentication.yml
- group: design
  href: https://artifacts.apis.io/thirdtrail-life/conformance/thirdtrail-life-conformance.yml
  title: ''
  type: Conformance
  url: conformance/thirdtrail-life-conformance.yml
- group: build
  href: https://artifacts.apis.io/thirdtrail-life/mcp/thirdtrail-life-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/thirdtrail-life-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/thirdtrail-life/mcp/thirdtrail-life-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/thirdtrail-life-mcp.yml
- group: other
  href: https://artifacts.apis.io/thirdtrail-life/hosts/thirdtrail-life-hosts.yml
  title: ''
  type: Hosts
  url: hosts/thirdtrail-life-hosts.yml
- group: other
  href: https://artifacts.apis.io/thirdtrail-life/vendors/thirdtrail-life-vendors.yml
  title: ''
  type: Vendors
  url: vendors/thirdtrail-life-vendors.yml
- group: auth
  href: https://artifacts.apis.io/thirdtrail-life/security/thirdtrail-life-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/thirdtrail-life-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thirdtrail.life/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://thirdtrail.life/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://thirdtrail.life/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://thirdtrail.life/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://thirdtrail.life/docs/
- group: operate
  title: ''
  type: Support
  url: https://thirdtrail.life/support/
- group: company
  title: ''
  type: Blog
  url: https://thirdtrail.life/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://thirdtrail.life/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://thirdtrail.life/accounts/signup/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thirdtrail.life/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thirdtrail.life/privacy/
created: '2026-10-31'
description: Third Trail provides REST APIs delivering precise astronomical and tidal data for any location on Earth. Their services include sunrise and sunset times, twilight phases, moon phases, solar irradiance, and tide heights, all corrected for elevation. The platform offers a free tier with flat monthly pricing, catering to developers building weather, navigation, photography, and marine applications. Detailed documentation, quickstart guides, and SDKs are available to help integrate the data quickly.
layout: provider
mcp_servers:
- description: Remote MCP server at thirdtrail.life.
  name: thirdtrail-life MCP Server
  slug: thirdtrail-life-mcp-yml
modified: '2026-10-31'
name: thirdtrail-life
nav: Providers
network: true
overview: 'thirdtrail-life publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Ephemerides API, MCP API, Solar API, and 2 more. Tagged areas include Company, Astronomy, Tides, Solar, and API.


  The thirdtrail-life catalog on APIs.io includes 1 Spectral governance ruleset.


  thirdtrail-life''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 17 more developer resources.'
plans:
- name: Thirdtrail Life Plans Pricing
  plan_count: 4
  slug: thirdtrail-life-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 6
  name: Thirdtrail Life Rate Limits
  slug: thirdtrail-life-rate-limits
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: thirdtrail-life API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: thirdtrail-life-rules
scopes:
- name: Thirdtrail Life Scopes
  scope_count: 0
  slug: thirdtrail-life-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 60.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 77.3
    catalog_earned_first_party: 0.0
    catalog_gap: 37.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 43.5
    developer_ergonomics: 63.6
    discoverability: 61.7
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Thirdtrail Life Authentication
  slug: thirdtrail-life-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Thirdtrail Life Domain Security
  slug: thirdtrail-life-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: ephemerides
  slug: thirdtrail-life-ephemerides
slug: thirdtrail-life
tags:
- Company
- Astronomy
- Tides
- Solar
- API
website: https://thirdtrail.life/
---
