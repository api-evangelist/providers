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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.7
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Compabase Agentic Access
  operation_count: 21
  slug: compabase-agentic-access
  summary_line: 21 operations · 2 acting
api_count: 1
apis:
- baseURL: https://compabase.com/api/v1/
  baseurl_source: declared
  description: The Companies API from Compabase — 14 operation(s) for companies.
  name: Compabase Companies API
  slug: compabase-companies-api
- baseURL: https://compabase.com/api/v1/
  baseurl_source: declared
  description: The Health API from Compabase — 1 operation(s) for health.
  name: Compabase Health API
  slug: compabase-health-api
- baseURL: https://compabase.com/api/v1/
  baseurl_source: declared
  description: The Persons API from Compabase — 2 operation(s) for persons.
  name: Compabase Persons API
  slug: compabase-persons-api
- baseURL: https://compabase.com/api/v1/
  baseurl_source: declared
  description: The Usage API from Compabase — 1 operation(s) for usage.
  name: Compabase Usage API
  slug: compabase-usage-api
- baseURL: https://compabase.com/api/v1/
  baseurl_source: declared
  description: The Watchlist API from Compabase — 2 operation(s) for watchlist.
  name: Compabase Watchlist API
  slug: compabase-watchlist-api
artifact_total: 18
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/agentic-access/compabase-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/compabase-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/plans/compabase-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/compabase-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/rules/compabase-rules.yml
  title: ''
  type: Spectral
  url: rules/compabase-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/json-ld/compabase-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/compabase-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/vocabulary/compabase-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/compabase-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/data-model/compabase-data-model.yml
  title: ''
  type: DataModel
  url: data-model/compabase-data-model.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/security/compabase-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/compabase-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/errors/compabase-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/compabase-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/conformance/compabase-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compabase-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/llms/compabase-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compabase-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/mcp/compabase-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/compabase-mcp.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/well-known/compabase-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/compabase-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/well-known/compabase-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compabase-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/hosts/compabase-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compabase-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/vendors/compabase-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compabase-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://compabase.com/status
- group: operate
  title: ''
  type: Roadmap
  url: https://compabase.com/roadmap
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/authentication/compabase-authentication.yml
  title: ''
  type: Authentication
  url: authentication/compabase-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/security/compabase-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/compabase-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/compabase/refs/heads/main/security/compabase-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compabase-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compabase.com
- group: docs
  title: ''
  type: Documentation
  url: https://compabase.com/docs/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://compabase.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://compabase.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://compabase.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://compabase.com/contact?topic=sales
- group: company
  title: ''
  type: Blog
  url: https://compabase.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ContentWriterco/compabase-api
- group: commercial
  title: ''
  type: Pricing
  url: https://compabase.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://compabase.com/join
- group: commercial
  title: ''
  type: TermsOfService
  url: https://compabase.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://compabase.com/privacy
created: '2026-10-08'
description: Compabase provides smart data on Polish companies, offering current financial and registry information sourced from public Polish registries. Users can verify business partners, mitigate risk, and discover trusted partners through searchable company databases filtered by revenue, location, industry, and more. The platform includes AI assistance, detailed company profiles, industry insights, and tools for due diligence, prospecting, market monitoring, and data automation.
image: https://compabase.com/og/home-en.png
json_schemas:
- name: CompanyCountResponse
  property_count: 1
  slug: compabase-company-count-response
- name: CompanyListResponse
  property_count: 2
  slug: compabase-company-list-response
- name: PersonConnectionsResponse
  property_count: 2
  slug: compabase-person-connections-response
- name: PersonSearchItem
  property_count: 4
  slug: compabase-person-search-item
- name: WatchlistAddResponse
  property_count: 4
  slug: compabase-watchlist-add-response
jsonld:
- class_count: 8
  name: Compabase Context
  property_count: 57
  slug: compabase-context
layout: provider
mcp_servers:
- description: Remote MCP server at compabase.com.
  name: Compabase MCP Server
  slug: compabase-mcp-yml
modified: '2026-10-08'
name: Compabase
nav: Providers
network: true
overview: 'Compabase publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Health API, Persons API, and 2 more. Tagged areas include Company, Data, Polish, and Business.


  The Compabase catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Compabase''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 25 more developer resources.'
plans:
- name: Compabase Plans Pricing
  plan_count: 4
  slug: compabase-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Compabase API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: compabase-rules
score:
  band: strong
  composite: 60.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 64.5
    developer_ergonomics: 57.1
    discoverability: 66.7
    operational_transparency: 36.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Compabase Authentication
  slug: compabase-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Compabase Domain Security
  slug: compabase-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Compabase Vulnerability Disclosure
  slug: compabase-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: compabase
tags:
- Company
- Data
- Polish
- Business
website: https://compabase.com
---
