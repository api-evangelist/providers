---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: MCP (Model Context Protocol) server providing tools for supply chain risk data.
  name: SupplyMaven MCP API
  slug: supplymaven-mcp-api
- description: 'supplymaven-com API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: supplymaven-com API
  slug: supplymaven-com-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/supplymaven-com/rate-limits/supplymaven-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/supplymaven-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/supplymaven-com/plans/supplymaven-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/supplymaven-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/supplymaven-com/rules/supplymaven-com-rules.yml
  title: ''
  type: Spectral
  url: rules/supplymaven-com-rules.yml
- group: design
  href: https://artifacts.apis.io/supplymaven-com/json-ld/supplymaven-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/supplymaven-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/supplymaven-com/vocabulary/supplymaven-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/supplymaven-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/supplymaven-com/data-model/supplymaven-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/supplymaven-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/supplymaven-com/authentication/supplymaven-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/supplymaven-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/supplymaven-com/errors/supplymaven-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/supplymaven-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/supplymaven-com/conformance/supplymaven-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/supplymaven-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/supplymaven-com/llms/supplymaven-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/supplymaven-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/supplymaven-com/mcp/supplymaven-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/supplymaven-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/supplymaven-com/hosts/supplymaven-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/supplymaven-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/supplymaven-com/vendors/supplymaven-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/supplymaven-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/supplymaven-com/security/supplymaven-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/supplymaven-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://supplymaven.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://supplymaven.com/developers
- group: docs
  title: ''
  type: Documentation
  url: https://supplymaven.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://supplymaven.com/developers
- group: operate
  title: ''
  type: Support
  url: https://supplymaven.com/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://supplymaven.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://supplymaven.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://supplymaven.com/subscribe
- group: start
  title: ''
  type: SignUp
  url: https://supplymaven.com/subscribe
created: '2026-10-30'
description: SupplyMaven provides supply chain risk intelligence, delivering real‑time monitoring of port congestion, border delays, commodity prices, and macroeconomic indicators across global trade networks. Users can access a free status board or upgrade to Dashboard Pro for $99 / month, gaining detailed disruption maps, a Global Disruption Index, and AI‑powered briefs. The platform also offers a REST API and MCP tools for integration, covering over 30 data signals and predictive analytics.
examples:
- key_count: 1
  name: Mcp Tools List
  slug: mcp-tools-list
json_schemas:
- name: GetApiMcpResponse
  property_count: 3
  slug: supplymaven-com-get-api-mcp-response
- name: PostApiMcpRequest
  property_count: 3
  slug: supplymaven-com-post-api-mcp-request
jsonld:
- class_count: 2
  name: Supplymaven Com Context
  property_count: 5
  slug: supplymaven-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at supplymaven.com.
  name: supplymaven-com MCP Server
  slug: supplymaven-com-mcp-yml
modified: '2026-10-30'
name: supplymaven-com
nav: Providers
network: true
overview: 'supplymaven-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Risk Intelligence, Data Platform, Analytics, and Logistics.


  The supplymaven-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  supplymaven-com''s developer surface includes authentication, documentation, API reference, support, pricing, signup flow, and 17 more developer resources.'
plans:
- name: Supplymaven Com Plans Pricing
  plan_count: 2
  slug: supplymaven-com-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 3
  name: Supplymaven Com Rate Limits
  slug: supplymaven-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: supplymaven-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: supplymaven-com-rules
scopes:
- name: Supplymaven Com Scopes
  scope_count: 0
  slug: supplymaven-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.8
    catalog_earned_first_party: 20.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 20.1
    developer_ergonomics: 27.4
    discoverability: 63.3
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 42.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/supplymaven-com/supplymaven-com-2026-11-03T144056.png
security:
- kind: authentication
  name: Supplymaven Com Authentication
  slug: supplymaven-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Supplymaven Com Domain Security
  slug: supplymaven-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: supplymaven-com
tags:
- Supply Chain
- Risk Intelligence
- Data Platform
- Analytics
- Logistics
website: https://supplymaven.com/
---
