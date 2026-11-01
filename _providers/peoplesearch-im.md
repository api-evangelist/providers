---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Peoplesearch Im Agentic Access
  operation_count: 6
  slug: peoplesearch-im-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 1
apis:
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Credits API from PeopleSearch.im — 1 operation(s) for credits.
  name: PeopleSearch.im Credits API
  slug: peoplesearch-im-credits-api
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Deliver API from PeopleSearch.im — 1 operation(s) for deliver.
  name: PeopleSearch.im Deliver API
  slug: peoplesearch-im-deliver-api
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Email API from PeopleSearch.im — 1 operation(s) for email.
  name: PeopleSearch.im Email API
  slug: peoplesearch-im-email-api
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Reveal API from PeopleSearch.im — 1 operation(s) for reveal.
  name: PeopleSearch.im Reveal API
  slug: peoplesearch-im-reveal-api
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Search API from PeopleSearch.im — 1 operation(s) for search.
  name: PeopleSearch.im Search API
  slug: peoplesearch-im-search-api
- baseURL: https://peoplesearch.im
  baseurl_source: spec
  description: The Tools API from PeopleSearch.im — 1 operation(s) for tools.
  name: PeopleSearch.im Tools API
  slug: peoplesearch-im-tools-api
artifact_total: 15
common:
- group: other
  href: https://artifacts.apis.io/peoplesearch-im/capabilities/peoplesearch-im-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/peoplesearch-im-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/peoplesearch-im/agentic-access/peoplesearch-im-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/peoplesearch-im-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/peoplesearch-im/plans/peoplesearch-im-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/peoplesearch-im-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/rules/peoplesearch-im-rules.yml
  title: ''
  type: Spectral
  url: rules/peoplesearch-im-rules.yml
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/json-ld/peoplesearch-im-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/peoplesearch-im-context.jsonld
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/vocabulary/peoplesearch-im-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/peoplesearch-im-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/data-model/peoplesearch-im-data-model.yml
  title: ''
  type: DataModel
  url: data-model/peoplesearch-im-data-model.yml
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/errors/peoplesearch-im-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/peoplesearch-im-problem-types.yml
- group: design
  href: https://artifacts.apis.io/peoplesearch-im/conformance/peoplesearch-im-conformance.yml
  title: ''
  type: Conformance
  url: conformance/peoplesearch-im-conformance.yml
- group: agent
  href: https://artifacts.apis.io/peoplesearch-im/llms/peoplesearch-im-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/peoplesearch-im-llms.txt
- group: build
  href: https://artifacts.apis.io/peoplesearch-im/mcp/peoplesearch-im-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/peoplesearch-im-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/peoplesearch-im/mcp/peoplesearch-im-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/peoplesearch-im-mcp.yml
- group: agent
  href: https://artifacts.apis.io/peoplesearch-im/well-known/peoplesearch-im-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/peoplesearch-im-well-known.yml
- group: other
  href: https://artifacts.apis.io/peoplesearch-im/hosts/peoplesearch-im-hosts.yml
  title: ''
  type: Hosts
  url: hosts/peoplesearch-im-hosts.yml
- group: other
  href: https://artifacts.apis.io/peoplesearch-im/vendors/peoplesearch-im-vendors.yml
  title: ''
  type: Vendors
  url: vendors/peoplesearch-im-vendors.yml
- group: auth
  href: https://artifacts.apis.io/peoplesearch-im/authentication/peoplesearch-im-authentication.yml
  title: ''
  type: Authentication
  url: authentication/peoplesearch-im-authentication.yml
- group: auth
  href: https://artifacts.apis.io/peoplesearch-im/security/peoplesearch-im-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/peoplesearch-im-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://peoplesearch.im
- group: docs
  title: ''
  type: Documentation
  url: https://peoplesearch.im/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://peoplesearch.im/pricing
- group: company
  title: ''
  type: Blog
  url: https://peoplesearch.im/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://peoplesearch.im/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://peoplesearch.im/legal/privacy
- group: start
  title: ''
  type: SignUp
  url: https://peoplesearch.im/login?mode=signup
- group: start
  title: ''
  type: Login
  url: https://peoplesearch.im/login
created: '2026-10-12'
description: PeopleSearch.im provides AI-powered people search and verified professional email lookup. Users can describe a target person or role in natural language and receive profile details and work emails, paying per credit. The service offers tools for email verification, format checking, and reverse lookup, with a free starter credit and tiered pricing.
finops:
- has_sources: true
  method: derived
  name: Peoplesearch Im Finops
  primary_unit: seat
  service_category: ''
  slug: peoplesearch-im-finops
  template: false
image: https://peoplesearch.im/opengraph-image
json_schemas:
- name: PeopleFilters
  property_count: 19
  slug: peoplesearch-im-people-filters
jsonld:
- class_count: 1
  name: Peoplesearch Im Context
  property_count: 19
  slug: peoplesearch-im-context
layout: provider
mcp_servers:
- description: Remote MCP server at peoplesearch.im requiring OAuth.
  name: PeopleSearch.im MCP Server
  slug: peoplesearch-im-mcp-yml
modified: '2026-10-12'
name: PeopleSearch.im
nav: Providers
network: true
overview: 'PeopleSearch.im publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Credits API, Deliver API, Email API, and 3 more. Tagged areas include Company, People Search, Email Lookup, Artificial Intelligence, and Software-as-a-Service.


  The PeopleSearch.im catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  PeopleSearch.im''s developer surface includes authentication, documentation, pricing, engineering blog, signup flow, and 20 more developer resources.'
plans:
- name: Peoplesearch Im Plans Pricing
  plan_count: 3
  slug: peoplesearch-im-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: PeopleSearch.im API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: peoplesearch-im-rules
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 66.2
    catalog_earned_first_party: 12.0
    catalog_gap: 48.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 58.5
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 44.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Peoplesearch Im Authentication
  slug: peoplesearch-im-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Peoplesearch Im Domain Security
  slug: peoplesearch-im-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: peoplesearch-im
tags:
- Company
- People Search
- Email Lookup
- Artificial Intelligence
- Software-as-a-Service
website: https://peoplesearch.im
---
