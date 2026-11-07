---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: RevoGrid provides a JavaScript data grid component library; it does not expose a public web API.
  name: RevoGrid JavaScript Data Grid API
  slug: revogrid-javascript-data-grid-api
- description: 'rv-grid-com API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: rv-grid-com API
  slug: rv-grid-com-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/rv-grid-com/rules/rv-grid-com-rules.yml
  title: ''
  type: Spectral
  url: rules/rv-grid-com-rules.yml
- group: design
  href: https://artifacts.apis.io/rv-grid-com/json-ld/rv-grid-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rv-grid-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/rv-grid-com/vocabulary/rv-grid-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rv-grid-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/rv-grid-com/data-model/rv-grid-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rv-grid-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/rv-grid-com/conformance/rv-grid-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rv-grid-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rv-grid-com/llms/rv-grid-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rv-grid-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/rv-grid-com/mcp/rv-grid-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rv-grid-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/rv-grid-com/hosts/rv-grid-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rv-grid-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rv-grid-com/vendors/rv-grid-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rv-grid-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/rv-grid-com/packages/rv-grid-com-packages.yml
  title: ''
  type: SDKs
  url: packages/rv-grid-com-packages.yml
- group: build
  href: https://artifacts.apis.io/rv-grid-com/packages/rv-grid-com-packages.yml
  title: ''
  type: Packages
  url: packages/rv-grid-com-packages.yml
- group: auth
  href: https://artifacts.apis.io/rv-grid-com/security/rv-grid-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rv-grid-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rv-grid.com/
- group: company
  title: ''
  type: Blog
  url: https://rv-grid.com/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://rv-grid.com/guide/
- group: start
  title: ''
  type: GettingStarted
  url: https://rv-grid.com/guide/dash/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://rv-grid.com/guide/api/revoGrid
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/revolist/revogrid
- group: commercial
  title: ''
  type: Pricing
  url: https://rv-grid.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rv-grid.com/pro/policies/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rv-grid.com/pro/policies/terms
- group: auth
  title: ''
  type: Security
  url: https://rv-grid.com/pro/policies/security
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/users/revolist/projects/3
coverage:
  checked: '2026-10-30'
  detail: The provider offers a JavaScript data grid library with documentation but no public web API.
  evidence:
  - status: 200
    url: https://rv-grid.com/guide/api/revoGrid
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: RevoGrid (rv-grid.com) provides a high-performance JavaScript data grid component for modern web applications. It supports Vue, React, Angular, Svelte, Dash, Python, and plain JavaScript, offering spreadsheet‑grade features such as virtual scrolling, editing, sorting, filtering, and pivot tables. The platform offers a Pro version with additional features, pricing plans, extensive documentation, and an open‑source core. It targets developers building complex data‑intensive web apps.
image: https://rv-grid.com/og-image.jpg
json_schemas:
- name: GetApiOrdersResponse
  property_count: 1
  slug: rv-grid-com-get-api-orders-response
jsonld:
- class_count: 1
  name: Rv Grid Com Context
  property_count: 1
  slug: rv-grid-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.rv-grid.com.
  name: rv-grid-com MCP Server
  slug: rv-grid-com-mcp-yml
modified: '2026-10-30'
name: rv-grid-com
nav: Providers
network: true
overview: 'rv-grid-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Grid, JavaScript, UI Component, and Open Source.


  The rv-grid-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rv-grid-com''s developer surface includes engineering blog, documentation, getting-started guide, API reference, pricing, and 18 more developer resources.'
plans:
- name: Rv Grid Com Plans Pricing
  plan_count: 1
  slug: rv-grid-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 1
  name: Rv Grid Com Rate Limits
  slug: rv-grid-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: rv-grid-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: rv-grid-com-rules
scopes:
- name: Rv Grid Com Scopes
  scope_count: 0
  slug: rv-grid-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 30
    catalog_earned: 62.6
    catalog_earned_first_party: 0.0
    catalog_gap: 52.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 34.7
    contract_governance: 22.0
    contract_quality: 16.4
    developer_ergonomics: 22.6
    discoverability: 64.3
    operational_transparency: 29.5
  previous_composite: 38.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 26.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/rv-grid-com/rv-grid-com-2026-11-03T142608.png
security:
- kind: authentication
  name: Rv Grid Com Authentication
  slug: rv-grid-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Rv Grid Com Domain Security
  slug: rv-grid-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: rv-grid-com
tags:
- Company
- Data Grid
- JavaScript
- UI Component
- Open Source
- ProVersion
website: https://rv-grid.com/
---
