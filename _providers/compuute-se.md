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
  band: agent-native
  dimensions:
    agent_card: near-conformant
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
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 9
  human_in_the_loop: 1
  name: Compuute Se Agentic Access
  operation_count: 17
  slug: compuute-se-agentic-access
  summary_line: 17 operations · 9 acting · 1 human-in-the-loop
api_count: 2
apis:
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The auth API from compuute-se — 2 operation(s) for auth.
  name: compuute-se Auth API
  slug: compuute-se-auth-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The billing API from compuute-se — 3 operation(s) for billing.
  name: compuute-se Billing API
  slug: compuute-se-billing-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The health API from compuute-se — 1 operation(s) for health.
  name: compuute-se Health API
  slug: compuute-se-health-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The scan API from compuute-se — 2 operation(s) for scan.
  name: compuute-se Scan API
  slug: compuute-se-scan-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The scan-x402 API from compuute-se — 1 operation(s) for scan-x402.
  name: compuute-se Scan X402 API
  slug: compuute-se-scan-x402-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The search API from compuute-se — 1 operation(s) for search.
  name: compuute-se Search API
  slug: compuute-se-search-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The subscribe API from compuute-se — 3 operation(s) for subscribe.
  name: compuute-se Subscribe API
  slug: compuute-se-subscribe-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The usage API from compuute-se — 1 operation(s) for usage.
  name: compuute-se Usage API
  slug: compuute-se-usage-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The validate API from compuute-se — 1 operation(s) for validate.
  name: compuute-se Validate API
  slug: compuute-se-validate-api
- baseURL: https://scan.compuute.se
  baseurl_source: declared
  description: The x402 API from compuute-se — 1 operation(s) for x402.
  name: compuute-se X402 API
  slug: compuute-se-x402-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/compuute-se/agentic-access/compuute-se-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/compuute-se-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/compuute-se/rules/compuute-se-rules.yml
  title: ''
  type: Spectral
  url: rules/compuute-se-rules.yml
- group: design
  href: https://artifacts.apis.io/compuute-se/json-ld/compuute-se-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/compuute-se-context.jsonld
- group: design
  href: https://artifacts.apis.io/compuute-se/vocabulary/compuute-se-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/compuute-se-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/compuute-se/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/compuute-se/data-model/compuute-se-data-model.yml
  title: ''
  type: DataModel
  url: data-model/compuute-se-data-model.yml
- group: design
  href: https://artifacts.apis.io/compuute-se/errors/compuute-se-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/compuute-se-problem-types.yml
- group: design
  href: https://artifacts.apis.io/compuute-se/conformance/compuute-se-conformance.yml
  title: ''
  type: Conformance
  url: conformance/compuute-se-conformance.yml
- group: agent
  href: https://artifacts.apis.io/compuute-se/llms/compuute-se-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/compuute-se-llms.txt
- group: other
  href: https://artifacts.apis.io/compuute-se/a2a/compuute-se-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/compuute-se-a2a.yml
- group: build
  href: https://artifacts.apis.io/compuute-se/mcp/compuute-se-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/compuute-se-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/compuute-se/mcp/compuute-se-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/compuute-se-mcp.yml
- group: agent
  href: https://artifacts.apis.io/compuute-se/well-known/compuute-se-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/compuute-se-well-known.yml
- group: other
  href: https://artifacts.apis.io/compuute-se/hosts/compuute-se-hosts.yml
  title: ''
  type: Hosts
  url: hosts/compuute-se-hosts.yml
- group: other
  href: https://artifacts.apis.io/compuute-se/vendors/compuute-se-vendors.yml
  title: ''
  type: Vendors
  url: vendors/compuute-se-vendors.yml
- group: auth
  href: https://artifacts.apis.io/compuute-se/security/compuute-se-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/compuute-se-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://compuute.se/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.compuute.se/
- group: docs
  title: ''
  type: Documentation
  url: https://www.compuute.se/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.compuute.se/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.compuute.se/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Compuute
created: '2026-10-29'
description: 'Compuute AB provides agentic AI security services, focusing on MCP server audits, vulnerability assessments, and compliance mapping for organizations deploying AI agents in regulated industries. Their offerings include static and manual code review of MCP server implementations, AI procurement risk audits, NIS2 & DORA compliance gap analysis, and an open‑source security scanner compuute‑scan. Based in Stockholm, Sweden, they target enterprise AI deployments with services such as prompt injection testing, tool poisoning analysis, and supply‑chain review. Contact: daniel@compuute.se.'
json_schemas:
- name: BillingStatusResponse
  property_count: 4
  slug: compuute-se-billing-status-response
- name: ScanRequest
  property_count: 1
  slug: compuute-se-scan-request
- name: ScanResponse
  property_count: 11
  slug: compuute-se-scan-response
- name: SearchRequest
  property_count: 4
  slug: compuute-se-search-request
- name: SearchResponse
  property_count: 5
  slug: compuute-se-search-response
- name: SubscribeRequest
  property_count: 5
  slug: compuute-se-subscribe-request
- name: UsageSummary
  property_count: 7
  slug: compuute-se-usage-summary
- name: ValidateResponse
  property_count: 6
  slug: compuute-se-validate-response
jsonld:
- class_count: 36
  name: Compuute Se Context
  property_count: 123
  slug: compuute-se-context
layout: provider
mcp_servers:
- description: Remote MCP server at leads.compuute.se.
  name: compuute-se MCP Server
  slug: compuute-se-mcp-yml
modified: '2026-10-29'
name: compuute-se
nav: Providers
network: true
overview: 'compuute-se publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Billing API, Health API, and 7 more. Tagged areas include Company, Artificial Intelligence, Security, MCP, and Compliance.


  The compuute-se catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  compuute-se''s developer surface includes documentation, getting-started guide, pricing, and 19 more developer resources.'
plans:
- name: Compuute Se Plans Pricing
  plan_count: 0
  slug: compuute-se-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: compuute-se API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: compuute-se-rules
scopes:
- name: Compuute Se Scopes
  scope_count: 0
  slug: compuute-se-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.2
  coverage:
    artifact_dirs: 31
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 54.9
    developer_ergonomics: 21.9
    discoverability: 71.7
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - sweden
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - nordics
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 33.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/compuute-se/compuute-se-2026-11-03T125027.png
security:
- kind: authentication
  name: Compuute Se Authentication
  slug: compuute-se-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Compuute Se Domain Security
  slug: compuute-se-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
skill_count: 1
skills:
- name: search-leads
  slug: compuute-se-search-leads
slug: compuute-se
tags:
- Company
- Artificial Intelligence
- Security
- MCP
- Compliance
- Sweden
- AI Agents
website: https://compuute.se/
---
