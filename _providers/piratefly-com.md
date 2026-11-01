---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.2
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Piratefly Com Agentic Access
  operation_count: 1
  slug: piratefly-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: 'Is today''s fare cheap? One endpoint compares the live cheapest fare on a route against that route''s own observed price history and returns a verdict, the best months to fly and how far ahead to book. '
  name: Flight Price Verdict API
  slug: price-verdict-api
artifact_total: 15
common:
- group: agent
  href: https://artifacts.apis.io/piratefly-com/agentic-access/piratefly-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/piratefly-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/piratefly-com/rate-limits/piratefly-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/piratefly-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/piratefly-com/plans/piratefly-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/piratefly-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/piratefly-com/rules/piratefly-com-rules.yml
  title: ''
  type: Spectral
  url: rules/piratefly-com-rules.yml
- group: design
  href: https://artifacts.apis.io/piratefly-com/json-ld/piratefly-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/piratefly-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/piratefly-com/vocabulary/piratefly-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/piratefly-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/piratefly-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/piratefly-com/data-model/piratefly-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/piratefly-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/piratefly-com/authentication/piratefly-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/piratefly-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/piratefly-com/errors/piratefly-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/piratefly-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/piratefly-com/conformance/piratefly-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/piratefly-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/piratefly-com/llms/piratefly-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/piratefly-com-llms.txt
- group: build
  href: https://artifacts.apis.io/piratefly-com/mcp/piratefly-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/piratefly-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/piratefly-com/mcp/piratefly-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/piratefly-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/piratefly-com/hosts/piratefly-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/piratefly-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/piratefly-com/vendors/piratefly-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/piratefly-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://piratefly.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://piratefly.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/piratefly-com/security/piratefly-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/piratefly-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://piratefly.com/
- group: docs
  title: ''
  type: Documentation
  url: https://piratefly.com/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://piratefly.com/v1/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://piratefly.com/api
- group: operate
  title: ''
  type: Support
  url: https://piratefly.com/contact
- group: company
  title: ''
  type: Blog
  url: https://piratefly.com/blog
created: '2026-10-30'
description: Piratefly is a free travel-price advisory service that tells users whether a flight price is a good deal right now (Buy/Wait/Your call) by comparing current fares to historical price observations. It monitors fare data across millions of routes, provides verdicts based on median and spread, and offers tools such as a fare index, CSV datasets, and an API for developers. The platform does not sell tickets but links out to airline or partner sites for booking.
image: https://piratefly.com/favicon.svg
json_schemas:
- name: Analisi
  property_count: 8
  slug: piratefly-com-analisi
jsonld:
- class_count: 1
  name: Piratefly Com Context
  property_count: 8
  slug: piratefly-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at piratefly.com.
  name: piratefly-com MCP Server
  slug: piratefly-com-mcp-yml
modified: '2026-10-30'
name: piratefly-com
nav: Providers
network: true
overview: 'piratefly-com is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Flights, Price-Tracking, Data-Analytics, and Free-Tool.


  The piratefly-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  piratefly-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Piratefly Com Plans Pricing
  plan_count: 2
  slug: piratefly-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Piratefly Com Rate Limits
  slug: piratefly-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: piratefly-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: piratefly-com-rules
scopes:
- name: Piratefly Com Scopes
  scope_count: 0
  slug: piratefly-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 69.2
    catalog_earned_first_party: 16.0
    catalog_gap: 45.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 22.0
    contract_quality: 13.9
    developer_ergonomics: 54.0
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
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
  name: Piratefly Com Authentication
  slug: piratefly-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Piratefly Com Domain Security
  slug: piratefly-com-domain-security
  summary_line: TLSv1.3
skill_count: 4
skills:
- name: cheapest-months
  slug: piratefly-com-cheapest-months
- name: flight-price-verdict
  slug: piratefly-com-flight-price-verdict
- name: watched-routes
  slug: piratefly-com-watched-routes
- name: when-to-book
  slug: piratefly-com-when-to-book
slug: piratefly-com
tags:
- Travel
- Flights
- Price-Tracking
- Data-Analytics
- Free-Tool
website: https://piratefly.com/
---
