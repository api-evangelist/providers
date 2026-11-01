---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 9.2
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: MCP tools list providing business valuation and Shopify audit utilities.
  name: Instilus MCP
  slug: instilus-mcp
artifact_total: 10
common:
- group: operate
  href: https://artifacts.apis.io/instilus-com/rate-limits/instilus-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/instilus-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/instilus-com/rules/instilus-com-rules.yml
  title: ''
  type: Spectral
  url: rules/instilus-com-rules.yml
- group: design
  href: https://artifacts.apis.io/instilus-com/json-ld/instilus-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instilus-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/instilus-com/vocabulary/instilus-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instilus-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/instilus-com/data-model/instilus-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instilus-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/instilus-com/authentication/instilus-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instilus-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/instilus-com/errors/instilus-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instilus-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/instilus-com/conformance/instilus-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instilus-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/instilus-com/llms/instilus-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instilus-com-llms.txt
- group: build
  href: https://artifacts.apis.io/instilus-com/mcp/instilus-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/instilus-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/instilus-com/mcp/instilus-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/instilus-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/instilus-com/hosts/instilus-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instilus-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instilus.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instilus.com/privacy
- group: auth
  href: https://artifacts.apis.io/instilus-com/security/instilus-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instilus-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://instilus.com/
created: '2026-10-30'
description: Instilus provides free online tools for eCommerce merchants and business owners, including a Shopify store scoring tool, business valuation calculators, break‑even and margin calculators, and downloadable spreadsheets, guides and briefs. The platform helps sellers assess store performance, estimate business value, and improve online operations without requiring email or account registration.
examples:
- key_count: 3
  name: Instilus Com Mcp
  slug: instilus-com-mcp
image: https://www.instilus.com/brand/instilus-logo.png
jsonld:
- class_count: 22
  name: Instilus Com Context
  property_count: 88
  slug: instilus-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.instilus.com.
  name: instilus-com MCP Server
  slug: instilus-com-mcp-yml
modified: '2026-10-30'
name: instilus-com
nav: Providers
network: true
overview: 'instilus-com publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include eCommerce, Valuation, Shopify, Tools, and Finance.


  The instilus-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  instilus-com''s developer surface includes authentication and 15 more developer resources.'
plans:
- name: Instilus Com Plans Pricing
  plan_count: 0
  slug: instilus-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 2
  name: Instilus Com Rate Limits
  slug: instilus-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: instilus-com API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 2
  slug: instilus-com-rules
scopes:
- name: Instilus Com Scopes
  scope_count: 0
  slug: instilus-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 26.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 61.8
    catalog_earned_first_party: 8.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 20.7
    developer_ergonomics: 11.9
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Instilus Com Authentication
  slug: instilus-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Instilus Com Domain Security
  slug: instilus-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: instilus-com
tags:
- eCommerce
- Valuation
- Shopify
- Tools
- Finance
website: https://instilus.com/
---
