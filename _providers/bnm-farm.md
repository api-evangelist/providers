---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Bnm Farm Agentic Access
  operation_count: 462
  slug: bnm-farm-agentic-access
  summary_line: 462 operations · 2 acting
api_count: 1
apis:
- baseURL: https://ticks.bnm.farm
  baseurl_source: declared
  description: The free API from BNM Data Shop — 153 operation(s) for free.
  name: BNM Data Shop Free API
  slug: bnm-farm-free-api
- baseURL: https://ticks.bnm.farm
  baseurl_source: declared
  description: The paid API from BNM Data Shop — 77 operation(s) for paid.
  name: BNM Data Shop Paid API
  slug: bnm-farm-paid-api
artifact_total: 7
common:
- group: agent
  href: https://artifacts.apis.io/bnm-farm/agentic-access/bnm-farm-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bnm-farm-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bnm-farm/rules/bnm-farm-rules.yml
  title: ''
  type: Spectral
  url: rules/bnm-farm-rules.yml
- group: design
  href: https://artifacts.apis.io/bnm-farm/vocabulary/bnm-farm-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bnm-farm-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bnm-farm/errors/bnm-farm-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bnm-farm-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bnm-farm/conformance/bnm-farm-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bnm-farm-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bnm-farm/llms/bnm-farm-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bnm-farm-llms.txt
- group: agent
  href: https://artifacts.apis.io/bnm-farm/mcp/bnm-farm-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bnm-farm-mcp.yml
- group: other
  href: https://artifacts.apis.io/bnm-farm/hosts/bnm-farm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bnm-farm-hosts.yml
- group: other
  href: https://artifacts.apis.io/bnm-farm/vendors/bnm-farm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bnm-farm-vendors.yml
- group: auth
  href: https://artifacts.apis.io/bnm-farm/authentication/bnm-farm-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bnm-farm-authentication.yml
- group: auth
  href: https://artifacts.apis.io/bnm-farm/security/bnm-farm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnm-farm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bnm.farm/
- group: docs
  title: ''
  type: Documentation
  url: https://bnm.farm/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://bnm.farm/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bnm.farm/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bnm.farm/privacy
- group: company
  title: ''
  type: Blog
  url: https://bnm.farm/blog
- group: operate
  title: ''
  type: Support
  url: https://bnm.farm/support
created: '2026-11-02'
description: BNM Data Shop provides official data access for agents, offering tables such as ticks and import alerts with a pay‑per‑use pricing model. Users can retrieve documents via simple GET requests, with pricing per door and per document. The service includes free search endpoints and cross‑door firm checks covering regulatory filings and enforcement actions. It aims to be a transparent, low‑cost data marketplace for compliance and research purposes.
layout: provider
mcp_servers:
- description: Remote MCP server at ticks.bnm.farm.
  name: BNM Data Shop MCP Server
  slug: bnm-farm-mcp-yml
modified: '2026-11-02'
name: BNM Data Shop
nav: Providers
network: true
overview: 'BNM Data Shop publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Free API and Paid API. Tagged areas include Data, Marketplace, Compliance, and Agents.


  The BNM Data Shop catalog on APIs.io includes 1 Spectral governance ruleset.


  BNM Data Shop''s developer surface includes authentication, documentation, pricing, engineering blog, support, and 13 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: BNM Data Shop API Rules
  rule_count: 47
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 2
  slug: bnm-farm-rules
score:
  band: thin
  composite: 28.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 22.0
    contract_quality: 50.5
    developer_ergonomics: 20.2
    discoverability: 53.3
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bnm Farm Authentication
  slug: bnm-farm-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Bnm Farm Domain Security
  slug: bnm-farm-domain-security
  summary_line: TLSv1.3
slug: bnm-farm
tags:
- Data
- Marketplace
- Compliance
- Agents
website: https://bnm.farm/
---
