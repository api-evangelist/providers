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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Une Education Agentic Access
  operation_count: 5
  slug: une-education-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- baseURL: https://customs.une.education
  baseurl_source: declared
  description: The Api.php API from une-education — 3 operation(s) for api.php.
  name: une-education Api.php API
  slug: une-education-api-php-api
- baseURL: https://customs.une.education
  baseurl_source: declared
  description: The Calculate Duties API from une-education — 1 operation(s) for calculate duties.
  name: une-education Calculate Duties API
  slug: une-education-calculate-duties-api
- baseURL: https://customs.une.education
  baseurl_source: declared
  description: The Restrictions API from une-education — 1 operation(s) for restrictions.
  name: une-education Restrictions API
  slug: une-education-restrictions-api
artifact_total: 8
common:
- group: agent
  href: https://artifacts.apis.io/une-education/agentic-access/une-education-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/une-education-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/une-education/rules/une-education-rules.yml
  title: ''
  type: Spectral
  url: rules/une-education-rules.yml
- group: design
  href: https://artifacts.apis.io/une-education/json-ld/une-education-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/une-education-context.jsonld
- group: design
  href: https://artifacts.apis.io/une-education/vocabulary/une-education-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/une-education-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/une-education/data-model/une-education-data-model.yml
  title: ''
  type: DataModel
  url: data-model/une-education-data-model.yml
- group: design
  href: https://artifacts.apis.io/une-education/conformance/une-education-conformance.yml
  title: ''
  type: Conformance
  url: conformance/une-education-conformance.yml
- group: agent
  href: https://artifacts.apis.io/une-education/llms/une-education-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/une-education-llms.txt
- group: agent
  href: https://artifacts.apis.io/une-education/mcp/une-education-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/une-education-mcp.yml
- group: agent
  href: https://artifacts.apis.io/une-education/well-known/une-education-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/une-education-well-known.yml
- group: other
  href: https://artifacts.apis.io/une-education/hosts/une-education-hosts.yml
  title: ''
  type: Hosts
  url: hosts/une-education-hosts.yml
- group: auth
  href: https://artifacts.apis.io/une-education/security/une-education-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/une-education-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://une.education/
- group: docs
  title: ''
  type: APIReference
  url: https://customs.une.education/openapi.json
created: '2026-10-30'
description: UNE (Unified Norms Engine) provides deterministic cross‑border computation and compliance infrastructure for autonomous agents. It offers multiple nodes covering customs tariffs, trade regulations, maritime fuel compliance, standards, legal dispute resolution, and sanctions screening, each accessible via Model Context Protocol (MCP) endpoints with OpenAPI 3.1 specifications. The platform delivers cryptographic proof of calculations, zero‑entropy query results, and supports public anonymous access as well as paid developer passes.
jsonld:
- class_count: 1
  name: Une Education Context
  property_count: 2
  slug: une-education-context
layout: provider
mcp_servers:
- description: Remote MCP server at maritime.une.education.
  name: une-education MCP Server
  slug: une-education-mcp-yml
modified: '2026-10-30'
name: une-education
nav: Providers
network: true
overview: 'une-education publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Api.php API, Calculate Duties API, and Restrictions API. Tagged areas include Company, Compliance, Trade, and Automation.


  The une-education catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  une-education''s developer surface includes API reference and 12 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: une-education API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: une-education-rules
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.6
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 45.2
    developer_ergonomics: 3.6
    discoverability: 63.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/une-education/une-education-2026-11-03T145415.png
security:
- kind: domain-security
  name: Une Education Domain Security
  slug: une-education-domain-security
  summary_line: TLSv1.3 · DNSSEC
slug: une-education
tags:
- Company
- Compliance
- Trade
- Automation
website: https://une.education/
---
