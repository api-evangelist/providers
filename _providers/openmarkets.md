---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: API documentation is provided at the OpenMarkets developer portal. No machine-readable contract was found despite probing known spec locations and documentation pages.
  name: OpenMarkets API
  slug: openmarkets-api-2
- baseURL: https://test-oms-api.openmarkets.com.au
  baseurl_source: declared
  description: 'OpenMarkets Group API as documented publicly: 56 operations. Contract generated from the documentation by API Evangelist (2026-10-21); not the provider''s own document.'
  name: OpenMarkets Group API
  slug: openmarkets-api
artifact_total: 9
common:
- group: design
  href: https://artifacts.apis.io/openmarkets/rules/openmarkets-rules.yml
  title: ''
  type: Spectral
  url: rules/openmarkets-rules.yml
- group: design
  href: https://artifacts.apis.io/openmarkets/json-ld/openmarkets-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/openmarkets-context.jsonld
- group: design
  href: https://artifacts.apis.io/openmarkets/vocabulary/openmarkets-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/openmarkets-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/openmarkets/data-model/openmarkets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/openmarkets-data-model.yml
- group: auth
  href: https://artifacts.apis.io/openmarkets/authentication/openmarkets-authentication.yml
  title: ''
  type: Authentication
  url: authentication/openmarkets-authentication.yml
- group: design
  href: https://artifacts.apis.io/openmarkets/conformance/openmarkets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/openmarkets-conformance.yml
- group: agent
  href: https://artifacts.apis.io/openmarkets/llms/openmarkets-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/openmarkets-llms.txt
- group: build
  href: https://artifacts.apis.io/openmarkets/mcp/openmarkets-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/openmarkets-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/openmarkets/mcp/openmarkets-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/openmarkets-mcp.yml
- group: agent
  href: https://artifacts.apis.io/openmarkets/well-known/openmarkets-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/openmarkets-well-known.yml
- group: other
  href: https://artifacts.apis.io/openmarkets/hosts/openmarkets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/openmarkets-hosts.yml
- group: other
  href: https://artifacts.apis.io/openmarkets/vendors/openmarkets-vendors.yml
  title: ''
  type: Vendors
  url: vendors/openmarkets-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.openmarkets.com.au/
- group: operate
  title: ''
  type: Support
  url: https://openmarkets.com.au/support/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://openmarkets.com.au/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://openmarkets.com.au/category/news/
- group: other
  title: ''
  type: Leadership
  url: https://openmarkets.com.au/team/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://openmarkets.com.au/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://openmarkets.com.au/onboarding/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.openmarkets.com.au/
- group: auth
  href: https://artifacts.apis.io/openmarkets/security/openmarkets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/openmarkets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://openmarkets.com.au/
coverage:
  checked: '2026-10-21'
  detail: Documentation pages are served as HTML with no machine‑readable OpenAPI or other spec discovered.
  evidence:
  - status: 200
    url: https://docs.openmarkets.com.au/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-21'
description: 'OpenMarkets Group is a company surfaced via the API Evangelist harvest backlog (source: g2-catalog) and added to the network as a stub for full-pipeline profiling.'
image: https://openmarkets.com.au/wp-content/uploads/2025/10/Openmarkets-icon.png
json_schemas:
- name: GetAccountsV1Response
  property_count: 1
  slug: openmarkets-get-accounts-v1-response
- name: GetExchangesInformationV1Response
  property_count: 1
  slug: openmarkets-get-exchanges-information-v1-response
jsonld:
- class_count: 2
  name: Openmarkets Context
  property_count: 1
  slug: openmarkets-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.openmarkets.com.au.
  name: OpenMarkets Group MCP Server
  slug: openmarkets-mcp-yml
modified: '2026-10-21'
name: OpenMarkets Group
nav: Providers
network: true
overview: 'OpenMarkets Group is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  The OpenMarkets Group catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OpenMarkets Group''s developer surface includes authentication, support, getting-started guide, documentation, and 18 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: OpenMarkets Group API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: openmarkets-rules
score:
  band: thin
  composite: 27.1
  coverage:
    artifact_dirs: 15
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 18.4
    contract_governance: 22.0
    contract_quality: 21.5
    developer_ergonomics: 47.6
    discoverability: 43.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 17
      marker_coverage: 100.0
      total: 17
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Openmarkets Authentication
  slug: openmarkets-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Openmarkets Domain Security
  slug: openmarkets-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: openmarkets
tags:
- Company
website: https://openmarkets.com.au/
---
