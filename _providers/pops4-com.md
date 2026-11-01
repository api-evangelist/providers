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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.7
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Pops4 Com Agentic Access
  operation_count: 57
  slug: pops4-com-agentic-access
  summary_line: 57 operations
api_count: 1
apis:
- description: Search 70,000 premium branded products for corporate gifting, executive rewards, events, and brand identity.
  name: POPS4 Luxury Branded Products API
  slug: pops4-luxury-branded-products-api
- baseURL: https://www.pops4.com/boards
  baseurl_source: declared
  description: The only open source of SEC filings that publishes every corporate event the business day after it is filed, from the settled SEC daily index, reads every filer the way an actuary would, and hashes it
  name: Edgar & Edgarette SEC Filing Boards .well-known API
  slug: edgar-edgarette-sec-filing-boards-well-known-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/pops4-com/rules/pops4-com-rules.yml
  title: ''
  type: Spectral
  url: rules/pops4-com-rules.yml
- group: design
  href: https://artifacts.apis.io/pops4-com/json-ld/pops4-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pops4-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/pops4-com/vocabulary/pops4-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pops4-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pops4-com/conformance/pops4-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pops4-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pops4-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/pops4-com/data-model/pops4-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pops4-com-data-model.yml
- group: agent
  href: https://artifacts.apis.io/pops4-com/llms/pops4-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pops4-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/pops4-com/mcp/pops4-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pops4-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pops4-com/well-known/pops4-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pops4-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/pops4-com/hosts/pops4-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pops4-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/pops4-com/vendors/pops4-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pops4-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pops4.com/privacy
- group: docs
  title: ''
  type: Documentation
  url: https://www.pops4.com/guides/the-stash-playbook
- group: docs
  title: ''
  type: APIReference
  url: https://www.pops4.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/pops4-com/security/pops4-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pops4-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pops4.com/
created: '2026-10-30'
description: POPS4 is a wholesale corporate gifts and branded merchandise provider offering a wide range of customizable products for businesses. Established in 1997, POPS4 serves clients across various industries, providing items such as apparel, accessories, and promotional goods. While primarily a retail operation, the company maintains an online platform for ordering and managing corporate branding projects. The site includes sections for product catalogs, pricing, and customer support, reflecting its focus on B2B commerce and brand promotion.
json_schemas:
- name: BoardIndex
  property_count: 7
  slug: pops4-com-board-index
- name: Board
  property_count: 16
  slug: pops4-com-board
- name: CompanyCard
  property_count: 21
  slug: pops4-com-company-card
- name: Status
  property_count: 14
  slug: pops4-com-status
jsonld:
- class_count: 6
  name: Pops4 Com Context
  property_count: 68
  slug: pops4-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.pops4.com.
  name: pops4-com MCP Server
  slug: pops4-com-mcp-yml
modified: '2026-10-30'
name: pops4-com
nav: Providers
network: true
overview: 'pops4-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Edgar & Edgarette SEC Filing Boards .well-known API, and 1 more. Tagged areas include Company, Wholesale, Corporate Gifts, Branding, and B2B.


  The pops4-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pops4-com''s developer surface includes documentation, API reference, and 14 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: pops4-com API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: pops4-com-rules
score:
  band: thin
  composite: 29.6
  coverage:
    artifact_dirs: 27
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 56.5
    developer_ergonomics: 23.1
    discoverability: 61.7
    operational_transparency: 0.0
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
    score: 14.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pops4 Com Authentication
  slug: pops4-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Pops4 Com Domain Security
  slug: pops4-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: get-categories
  slug: pops4-com-get-categories
- name: get-product
  slug: pops4-com-get-product
- name: get-quote
  slug: pops4-com-get-quote
- name: search-products
  slug: pops4-com-search-products
slug: pops4-com
tags:
- Company
- Wholesale
- Corporate Gifts
- Branding
- B2B
website: https://pops4.com/
---
