---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP Rating provides a meta‑server gateway to discover and connect to MCP servers via a single endpoint.
  name: MCP Rating API
  slug: mcp-rating-api
- description: 'mcprating-io API as documented publicly: 5 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: mcprating-io API
  slug: mcprating-io-api
artifact_total: 5
common:
- group: design
  href: https://artifacts.apis.io/mcprating-io/rules/mcprating-io-rules.yml
  title: ''
  type: Spectral
  url: rules/mcprating-io-rules.yml
- group: design
  href: https://artifacts.apis.io/mcprating-io/vocabulary/mcprating-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/mcprating-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/mcprating-io/conformance/mcprating-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mcprating-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/mcprating-io/mcp/mcprating-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/mcprating-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/mcprating-io/hosts/mcprating-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/mcprating-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/mcprating-io/vendors/mcprating-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/mcprating-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/mcprating-io/packages/mcprating-io-packages.yml
  title: ''
  type: SDKs
  url: packages/mcprating-io-packages.yml
- group: build
  href: https://artifacts.apis.io/mcprating-io/packages/mcprating-io-packages.yml
  title: ''
  type: Packages
  url: packages/mcprating-io-packages.yml
- group: auth
  title: ''
  type: Security
  url: https://mcprating.io/category/security
- group: auth
  href: https://artifacts.apis.io/mcprating-io/security/mcprating-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mcprating-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mcprating.io/
- group: docs
  title: ''
  type: Documentation
  url: https://mcprating.io/docs
- group: start
  title: ''
  type: Quickstart
  url: https://mcprating.io/quickstart
- group: company
  title: ''
  type: Blog
  url: https://mcprating.io/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mcprating.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mcprating.io/privacy
coverage:
  checked: '2026-10-30'
  detail: Documentation pages are HTML without a machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://mcprating.io/docs/overview
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-30'
description: MCP Rating is a platform that discovers, scores, and runs MCP servers safely. It provides a searchable catalog of over 86,000 MCP servers across categories such as developer tools, finance, AI, and more. Users can browse servers, view quality signals, and connect to them via the MCP Gateway with built-in security and compliance checks. The service offers quickstart guides, documentation, and a blog to help developers integrate MCP servers into their workflows.
layout: provider
mcp_servers:
- description: Remote MCP server at mcprating.io.
  name: mcprating-io MCP Server
  slug: mcprating-io-mcp-yml
modified: '2026-10-30'
name: mcprating-io
nav: Providers
network: true
overview: 'mcprating-io is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, MCP, Platform, Catalog, and Security.


  The mcprating-io catalog on APIs.io includes 1 Spectral governance ruleset.


  mcprating-io''s developer surface includes documentation, quickstart, engineering blog, and 13 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: mcprating-io API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: mcprating-io-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 64.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 28.6
    contract_governance: 35.6
    contract_quality: 9.4
    developer_ergonomics: 19.0
    discoverability: 56.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 31.8
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/mcprating-io/mcprating-io-2026-11-03T135414.png
security:
- kind: domain-security
  name: Mcprating Io Domain Security
  slug: mcprating-io-domain-security
  summary_line: TLSv1.3 · HSTS
slug: mcprating-io
tags:
- Company
- MCP
- Platform
- Catalog
- Security
website: https://mcprating.io/
---
