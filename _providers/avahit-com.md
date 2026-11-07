---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Avahit Com Agentic Access
  operation_count: 2
  slug: avahit-com-agentic-access
  summary_line: 2 operations
api_count: 1
apis:
- baseURL: https://avahit.com
  baseurl_source: declared
  description: The Catalog API from Avahit — 1 operation(s) for catalog.
  name: Avahit Catalog API
  slug: avahit-com-catalog-api
- baseURL: https://avahit.com
  baseurl_source: declared
  description: The Lookup API from Avahit — 1 operation(s) for lookup.
  name: Avahit Lookup API
  slug: avahit-com-lookup-api
artifact_total: 12
common:
- group: agent
  href: https://artifacts.apis.io/avahit-com/agentic-access/avahit-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/avahit-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/avahit-com/rules/avahit-com-rules.yml
  title: ''
  type: Spectral
  url: rules/avahit-com-rules.yml
- group: design
  href: https://artifacts.apis.io/avahit-com/json-ld/avahit-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/avahit-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/avahit-com/vocabulary/avahit-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/avahit-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/avahit-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/avahit-com/data-model/avahit-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/avahit-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/avahit-com/errors/avahit-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/avahit-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/avahit-com/conformance/avahit-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/avahit-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/avahit-com/llms/avahit-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avahit-com-llms.txt
- group: build
  href: https://artifacts.apis.io/avahit-com/mcp/avahit-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/avahit-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/avahit-com/mcp/avahit-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/avahit-com-mcp.yml
- group: auth
  href: https://artifacts.apis.io/avahit-com/well-known/avahit-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avahit-com-security.txt
- group: agent
  href: https://artifacts.apis.io/avahit-com/well-known/avahit-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avahit-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/avahit-com/hosts/avahit-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avahit-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/avahit-com/vendors/avahit-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avahit-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://avahit.com/security
- group: company
  title: ''
  type: Newsroom
  url: https://avahit.com/press
- group: start
  title: ''
  type: Login
  url: https://avahit.com/login
- group: auth
  href: https://artifacts.apis.io/avahit-com/security/avahit-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avahit-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/avahit-com/security/avahit-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avahit-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://avahit.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://avahit.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://avahit.com/privacy
created: '2026-11-02'
description: Avahit is an affiliate-driven e‑commerce platform that curates Amazon product listings by category and brand. It helps shoppers discover items across beauty, fashion, home, tech and more, providing direct links to Amazon for current pricing and availability. The site also offers trend reports, such as Black Friday discount analyses, and participates in affiliate programs like Awin, earning commissions without influencing rankings.
image: https://avahit.com/opengraph-image
json_schemas:
- name: CatalogPage
  property_count: 6
  slug: avahit-com-catalog-page
jsonld:
- class_count: 3
  name: Avahit Com Context
  property_count: 23
  slug: avahit-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at avahit.com.
  name: Avahit MCP Server
  slug: avahit-com-mcp-yml
modified: '2026-11-02'
name: Avahit
nav: Providers
network: true
overview: 'Avahit publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Catalog API and Lookup API. Tagged areas include Affiliates, E-Commerce, Shopping, Amazon, and Product Discovery.


  The Avahit catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Avahit API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: avahit-com-rules
scopes:
- name: Avahit Com Scopes
  scope_count: 0
  slug: avahit-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 29
    catalog_earned: 56.2
    catalog_earned_first_party: 0.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.8
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 50.1
    developer_ergonomics: 6.4
    discoverability: 65.8
    operational_transparency: 5.3
  previous_composite: 34.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Avahit Com Authentication
  slug: avahit-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Avahit Com Domain Security
  slug: avahit-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avahit Com Vulnerability Disclosure
  slug: avahit-com-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: avahit-com-catalog
  slug: avahit-com-catalog
slug: avahit-com
tags:
- Affiliates
- E-Commerce
- Shopping
- Amazon
- Product Discovery
website: https://avahit.com/
---
