---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.3
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Aplusz App Agentic Access
  operation_count: 4
  slug: aplusz-app-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- baseURL: https://aplusz.app
  baseurl_source: declared
  description: The Cities API from aplusz-app — 1 operation(s) for cities.
  name: aplusz-app Cities API
  slug: aplusz-app-cities-api
- baseURL: https://aplusz.app
  baseurl_source: declared
  description: The Fare API from aplusz-app — 1 operation(s) for fare.
  name: aplusz-app Fare API
  slug: aplusz-app-fare-api
- baseURL: https://aplusz.app
  baseurl_source: declared
  description: The Health API from aplusz-app — 1 operation(s) for health.
  name: aplusz-app Health API
  slug: aplusz-app-health-api
- baseURL: https://aplusz.app
  baseurl_source: declared
  description: The Routes API from aplusz-app — 1 operation(s) for routes.
  name: aplusz-app Routes API
  slug: aplusz-app-routes-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/aplusz-app/agentic-access/aplusz-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/aplusz-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/aplusz-app/plans/aplusz-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aplusz-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aplusz-app/rules/aplusz-app-rules.yml
  title: ''
  type: Spectral
  url: rules/aplusz-app-rules.yml
- group: design
  href: https://artifacts.apis.io/aplusz-app/json-ld/aplusz-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/aplusz-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/aplusz-app/vocabulary/aplusz-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/aplusz-app-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/aplusz-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/aplusz-app/data-model/aplusz-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aplusz-app-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://aplusz.app/legal/
- group: design
  href: https://artifacts.apis.io/aplusz-app/errors/aplusz-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aplusz-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aplusz-app/conformance/aplusz-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aplusz-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aplusz-app/llms/aplusz-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aplusz-app-llms.txt
- group: other
  href: https://artifacts.apis.io/aplusz-app/a2a/aplusz-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aplusz-app-a2a.yml
- group: build
  href: https://artifacts.apis.io/aplusz-app/mcp/aplusz-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/aplusz-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/aplusz-app/mcp/aplusz-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aplusz-app-mcp.yml
- group: auth
  href: https://artifacts.apis.io/aplusz-app/well-known/aplusz-app-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/aplusz-app-security.txt
- group: agent
  href: https://artifacts.apis.io/aplusz-app/well-known/aplusz-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aplusz-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/aplusz-app/hosts/aplusz-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aplusz-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aplusz-app/vendors/aplusz-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aplusz-app-vendors.yml
- group: auth
  href: https://artifacts.apis.io/aplusz-app/security/aplusz-app-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/aplusz-app-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/aplusz-app/security/aplusz-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aplusz-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aplusz.app/
- group: docs
  title: ''
  type: Documentation
  url: https://aplusz.app/docs
- group: docs
  title: ''
  type: APIReference
  url: https://aplusz.app/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://aplusz.app/support
- group: company
  title: ''
  type: Blog
  url: https://aplusz.app/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aplusz.app/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aplusz.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aplusz.app/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dagrang-repository/aplusz
created: '2026-10-29'
description: AplusZ is a travel search platform that helps users find the absolute lowest air ticket price for any route on any day. It offers free unlimited searches, exact best date and price, saved routes, reminders, calendar export, offline functionality, and a Pro plan with unlimited route sets and swaps. The service provides a public fare API (OpenAPI) at https://aplusz.app/openapi.json for developers to query flight pricing data programmatically.
image: https://aplusz.app/assets/icons/icon-192.png
json_schemas:
- name: Fare
  property_count: 17
  slug: aplusz-app-fare
jsonld:
- class_count: 2
  name: Aplusz App Context
  property_count: 19
  slug: aplusz-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at aplusz.app.
  name: aplusz-app MCP Server
  slug: aplusz-app-mcp-yml
modified: '2026-10-29'
name: aplusz-app
nav: Providers
network: true
overview: 'aplusz-app publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cities API, Fare API, Health API, and 1 more. Tagged areas include Company, Travel, Airfare, Search, and Free.


  The aplusz-app catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  aplusz-app''s developer surface includes documentation, API reference, support, engineering blog, pricing, and 24 more developer resources.'
plans:
- name: Aplusz App Plans Pricing
  plan_count: 1
  slug: aplusz-app-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aplusz App Rate Limits
  slug: aplusz-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: aplusz-app API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: aplusz-app-rules
scopes:
- name: Aplusz App Scopes
  scope_count: 0
  slug: aplusz-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 64.2
    catalog_earned_first_party: 8.0
    catalog_gap: 50.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 51.7
    developer_ergonomics: 30.2
    discoverability: 65.0
    operational_transparency: 15.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: unknown
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
  name: Aplusz App Authentication
  slug: aplusz-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aplusz App Domain Security
  slug: aplusz-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aplusz App Vulnerability Disclosure
  slug: aplusz-app-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 3
skills:
- name: find-cheapest-fare
  slug: aplusz-app-find-cheapest-fare
- name: list-routes-from
  slug: aplusz-app-list-routes-from
- name: resolve-city
  slug: aplusz-app-resolve-city
slug: aplusz-app
tags:
- Company
- Travel
- Airfare
- Search
- Free
- Booking
website: https://aplusz.app/
---
