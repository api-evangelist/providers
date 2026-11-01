---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
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
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mspsoftware Net Agentic Access
  operation_count: 10
  slug: mspsoftware-net-agentic-access
  summary_line: 10 operations
api_count: 1
apis:
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Categories API from MSP Software — 2 operation(s) for categories.
  name: MSP Software Categories API
  slug: mspsoftware-net-categories-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Compare API from MSP Software — 1 operation(s) for compare.
  name: MSP Software Compare API
  slug: mspsoftware-net-compare-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The MSP Software API API from MSP Software — 1 operation(s) for msp software api.
  name: MSP Software MSP Software API
  slug: mspsoftware-net-msp-software-api-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Posts API from MSP Software — 2 operation(s) for posts.
  name: MSP Software Posts API
  slug: mspsoftware-net-posts-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Recent API from MSP Software — 1 operation(s) for recent.
  name: MSP Software Recent API
  slug: mspsoftware-net-recent-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Software API from MSP Software — 2 operation(s) for software.
  name: MSP Software Software API
  slug: mspsoftware-net-software-api
- baseURL: https://mspsoftware.net/api/v1
  baseurl_source: declared
  description: The Vendors API from MSP Software — 1 operation(s) for vendors.
  name: MSP Software Vendors API
  slug: mspsoftware-net-vendors-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/mspsoftware-net/agentic-access/mspsoftware-net-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/mspsoftware-net-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/rules/mspsoftware-net-rules.yml
  title: ''
  type: Spectral
  url: rules/mspsoftware-net-rules.yml
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/json-ld/mspsoftware-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/mspsoftware-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/vocabulary/mspsoftware-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mspsoftware-net-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/mspsoftware-net/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/data-model/mspsoftware-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mspsoftware-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/errors/mspsoftware-net-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mspsoftware-net-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mspsoftware-net/conformance/mspsoftware-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mspsoftware-net-conformance.yml
- group: other
  href: https://artifacts.apis.io/mspsoftware-net/overlays/mspsoftware-net-directory-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mspsoftware-net-directory-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/mspsoftware-net/llms/mspsoftware-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mspsoftware-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/mspsoftware-net/mcp/mspsoftware-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mspsoftware-net-mcp.yml
- group: other
  href: https://artifacts.apis.io/mspsoftware-net/hosts/mspsoftware-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mspsoftware-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/mspsoftware-net/vendors/mspsoftware-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mspsoftware-net-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://mspsoftware.net/sign-in
- group: auth
  href: https://artifacts.apis.io/mspsoftware-net/security/mspsoftware-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mspsoftware-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mspsoftware.net
- group: docs
  title: ''
  type: Documentation
  url: https://mspsoftware.net/api
- group: docs
  title: ''
  type: APIReference
  url: https://mspsoftware.net/api
- group: company
  title: ''
  type: Blog
  url: https://mspsoftware.net/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mspsoftware.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mspsoftware.net/privacy
created: '2026-10-29'
description: MSP Software (mspsoftware.net) is a directory of software for managed service providers, listing 256 products across 20 categories such as PSA, RMM, backup, and security. Each listing includes vendor‑published facts, pricing details, reviews from other MSPs, and FAQs. The site provides a read‑only JSON API (OpenAPI 3.1) for programmatic access to categories, listings, comparisons, recent updates, and blog posts. No authentication is required.
image: https://mspsoftware.net/brand/og-default.png
json_schemas:
- name: CategoryDetail
  property_count: 0
  slug: mspsoftware-net-category-detail
- name: Comparison
  property_count: 5
  slug: mspsoftware-net-comparison
- name: RecentUpdates
  property_count: 2
  slug: mspsoftware-net-recent-updates
- name: SoftwareDetail
  property_count: 27
  slug: mspsoftware-net-software-detail
- name: SoftwareSummary
  property_count: 17
  slug: mspsoftware-net-software-summary
- name: Vendor
  property_count: 10
  slug: mspsoftware-net-vendor
jsonld:
- class_count: 15
  name: Mspsoftware Net Context
  property_count: 75
  slug: mspsoftware-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at mspsoftware.net.
  name: MSP Software MCP Server
  slug: mspsoftware-net-mcp-yml
modified: '2026-10-29'
name: MSP Software
nav: Providers
network: true
overview: 'MSP Software publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Categories API, Compare API, MSP Software API, and 4 more. Tagged areas include Directory, MSP, Software, Comparison, and Reviews.


  The MSP Software catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MSP Software''s developer surface includes documentation, API reference, engineering blog, and 18 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: MSP Software API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: mspsoftware-net-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 57.0
    developer_ergonomics: 37.4
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Mspsoftware Net Domain Security
  slug: mspsoftware-net-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: search-software
  slug: mspsoftware-net-search-software
slug: mspsoftware-net
tags:
- Directory
- MSP
- Software
- Comparison
- Reviews
- OpenAPI
website: https://mspsoftware.net
---
