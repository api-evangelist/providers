---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.6
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Suggix Agentic Access
  operation_count: 17
  slug: suggix-agentic-access
  summary_line: 17 operations
api_count: 1
apis:
- description: Connect your AI client to Suggix feedback, roadmap, changelog, and workspace data through MCP.
  name: Suggix MCP
  slug: suggix-mcp
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: Indicator definitions and time series
  name: Suggix Indicators API
  slug: suggix-indicators-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: ISIC Rev.4 classification
  name: Suggix Industries API
  slug: suggix-industries-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: Countries and supranational groupings
  name: Suggix Regions API
  slug: suggix-regions-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: Full-text search
  name: Suggix Search API
  slug: suggix-search-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: Publishing organisations and their documents
  name: Suggix Sources API
  slug: suggix-sources-api
- baseURL: https://statorigin.org/api/v1
  baseurl_source: spec
  description: Data points with full provenance
  name: Suggix Statistics API
  slug: suggix-statistics-api
artifact_total: 14
common:
- group: other
  href: https://artifacts.apis.io/suggix/capabilities/suggix-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/suggix-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/suggix/agentic-access/suggix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/suggix-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/suggix/plans/suggix-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/suggix-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/suggix/rules/suggix-rules.yml
  title: ''
  type: Spectral
  url: rules/suggix-rules.yml
- group: design
  href: https://artifacts.apis.io/suggix/json-ld/suggix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/suggix-context.jsonld
- group: design
  href: https://artifacts.apis.io/suggix/vocabulary/suggix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/suggix-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/suggix/data-model/suggix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/suggix-data-model.yml
- group: auth
  href: https://artifacts.apis.io/suggix/authentication/suggix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/suggix-authentication.yml
- group: design
  href: https://artifacts.apis.io/suggix/errors/suggix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/suggix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/suggix/conformance/suggix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/suggix-conformance.yml
- group: agent
  href: https://artifacts.apis.io/suggix/llms/suggix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/suggix-llms.txt
- group: other
  href: https://artifacts.apis.io/suggix/a2a/suggix-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/suggix-a2a.yml
- group: other
  href: https://artifacts.apis.io/suggix/hosts/suggix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/suggix-hosts.yml
- group: other
  href: https://artifacts.apis.io/suggix/vendors/suggix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/suggix-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.suggix.com/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://help.suggix.com/mcp/claude-code
- group: auth
  href: https://artifacts.apis.io/suggix/security/suggix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/suggix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.suggix.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.suggix.com/mcp/overview
- group: company
  title: ''
  type: Blog
  url: https://www.suggix.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.suggix.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.suggix.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.suggix.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.suggix.com/privacy
- group: operate
  title: ''
  type: Roadmap
  url: https://feedback.suggix.com/roadmap
- group: operate
  title: ''
  type: Support
  url: https://help.suggix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.suggix.com
- group: docs
  title: ''
  type: APIReference
  url: https://help.suggix.com/mcp/overview
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: null
    url: https://help.suggix.com/mcp
  - status: 200
    url: https://www.suggix.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: Suggix provides a SaaS platform for collecting and managing customer feedback, roadmaps, and changelogs. It enables product teams to centralize user suggestions, prioritize features, and communicate updates through a public changelog. The service includes tools for tagging, voting, discussion threads, and advanced filtering, helping companies turn raw feedback into actionable product decisions. A 14‑day free trial is available without a credit card.
finops:
- has_sources: true
  method: derived
  name: Suggix Finops
  primary_unit: seat
  service_category: ''
  slug: suggix-finops
  template: false
image: https://res.suggix.com/common/og.png
jsonld:
- class_count: 3
  name: Suggix Context
  property_count: 30
  slug: suggix-context
layout: provider
modified: '2026-10-14'
name: Suggix
nav: Providers
network: true
overview: 'Suggix publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Indicators API, Industries API, Regions API, and 4 more. Tagged areas include Software-as-a-Service, Feedback, Roadmaps, Changelog, and Product Management.


  The Suggix catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Suggix''s developer surface includes authentication, changelog, getting-started guide, documentation, engineering blog, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Suggix Plans Pricing
  plan_count: 4
  slug: suggix-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Suggix API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: suggix-rules
score:
  band: developing
  composite: 53.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 60.8
    catalog_earned_first_party: 12.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.5
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 51.9
    developer_ergonomics: 57.1
    discoverability: 57.1
    operational_transparency: 21.1
  previous_composite: 52.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
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
security:
- kind: authentication
  name: Suggix Authentication
  slug: suggix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Suggix Domain Security
  slug: suggix-domain-security
  summary_line: TLSv1.3 · DMARC
slug: suggix
tags:
- Software-as-a-Service
- Feedback
- Roadmaps
- Changelog
- Product Management
website: https://www.suggix.com
---
