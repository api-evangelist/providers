---
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 3
  human_in_the_loop: 1
  name: Monsitools Agentic Access
  operation_count: 5
  slug: monsitools-agentic-access
  summary_line: 5 operations · 3 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Remote MCP server exposing search_calculators, describe_calculator and calculate.
  name: MonsiTools MCP Server
  slug: mcp
- baseURL: https://monsitools.com/mcp
  baseurl_source: declared
  description: The Api Tools.json API from MonsiTools — 1 operation(s) for api tools.json.
  name: MonsiTools Api Tools.json API
  slug: monsitools-api-tools-json-api
- baseURL: https://monsitools.com/mcp
  baseurl_source: declared
  description: The Calculate API from MonsiTools — 1 operation(s) for calculate.
  name: MonsiTools Calculate API
  slug: monsitools-calculate-api
- baseURL: https://monsitools.com/mcp
  baseurl_source: declared
  description: The Keys API from MonsiTools — 1 operation(s) for keys.
  name: MonsiTools Keys API
  slug: monsitools-keys-api
artifact_total: 19
common:
- group: commercial
  href: https://artifacts.apis.io/monsitools/plans/monsitools-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/monsitools-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/monsitools/capabilities/monsitools-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/monsitools-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/monsitools/rate-limits/monsitools-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/monsitools-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/monsitools/mcp/monsitools-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/monsitools-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/monsitools/agentic-access/monsitools-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/monsitools-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/monsitools/rules/monsitools-rules.yml
  title: ''
  type: Spectral
  url: rules/monsitools-rules.yml
- group: design
  href: https://artifacts.apis.io/monsitools/json-ld/monsitools-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/monsitools-context.jsonld
- group: design
  href: https://artifacts.apis.io/monsitools/vocabulary/monsitools-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/monsitools-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/monsitools/data-model/monsitools-data-model.yml
  title: ''
  type: DataModel
  url: data-model/monsitools-data-model.yml
- group: design
  href: https://artifacts.apis.io/monsitools/errors/monsitools-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/monsitools-problem-types.yml
- group: design
  href: https://artifacts.apis.io/monsitools/conformance/monsitools-conformance.yml
  title: ''
  type: Conformance
  url: conformance/monsitools-conformance.yml
- group: agent
  href: https://artifacts.apis.io/monsitools/llms/monsitools-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/monsitools-llms.txt
- group: other
  href: https://artifacts.apis.io/monsitools/hosts/monsitools-hosts.yml
  title: ''
  type: Hosts
  url: hosts/monsitools-hosts.yml
- group: other
  href: https://artifacts.apis.io/monsitools/vendors/monsitools-vendors.yml
  title: ''
  type: Vendors
  url: vendors/monsitools-vendors.yml
- group: auth
  href: https://artifacts.apis.io/monsitools/authentication/monsitools-authentication.yml
  title: ''
  type: Authentication
  url: authentication/monsitools-authentication.yml
- group: auth
  href: https://artifacts.apis.io/monsitools/security/monsitools-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/monsitools-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://monsitools.com
- group: docs
  title: ''
  type: Documentation
  url: https://monsitools.com/developers
- group: start
  title: ''
  type: DeveloperPortal
  url: https://monsitools.com/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://monsitools.com/whats-new
- group: start
  title: ''
  type: Login
  url: https://monsitools.com/login
- group: start
  title: ''
  type: SignUp
  url: https://monsitools.com/login
- group: commercial
  title: ''
  type: Pricing
  url: https://monsitools.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://monsitools.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://monsitools.com/terms
- group: start
  title: ''
  type: GettingStarted
  url: https://monsitools.com/guides
created: '2026-10-09'
description: 'MonsiTools is a calculator and workflow builder: people build calculators by typing a formula in plain words and chain them into workflows. It ships 1262 ready-made browser calculators and data tools for business, finance, SaaS metrics, ecommerce and marketing, plus a JSON Calculation API (premium, 60 requests per minute, Bearer mt_live_ keys) and a remote MCP server at monsitools.com/mcp.'
finops:
- has_sources: true
  method: derived
  name: Monsitools Finops
  primary_unit: week
  service_category: ''
  slug: monsitools-finops
  template: false
image: https://monsitools.com/og/default.png
json_schemas:
- name: ApiKeyCreated
  property_count: 4
  slug: monsitools-api-key-created
- name: ApiKeyStatus
  property_count: 5
  slug: monsitools-api-key-status
- name: CalculateRequest
  property_count: 2
  slug: monsitools-calculate-request
- name: CalculateResult
  property_count: 5
  slug: monsitools-calculate-result
- name: Tool
  property_count: 5
  slug: monsitools-tool
jsonld:
- class_count: 7
  name: Monsitools Context
  property_count: 23
  slug: monsitools-context
layout: provider
mcp_servers:
- description: Remote MCP server at monsitools.com; 3 tools listed.
  name: MonsiTools MCP Server
  slug: monsitools-mcp-server
modified: '2026-10-09'
name: MonsiTools
nav: Providers
network: true
overview: 'MonsiTools publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Api Tools.json API, Calculate API, Keys API, and 1 more. Tagged areas include Company, Calculators, Finance, Workflows, and MCP.


  The MonsiTools catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  MonsiTools'' developer surface includes authentication, documentation, changelog, signup flow, pricing, getting-started guide, and 20 more developer resources.'
plans:
- name: Monsitools Plans Pricing
  plan_count: 4
  slug: monsitools-plans-pricing
- name: Monsitools Price Estimates
  plan_count: 0
  slug: monsitools-price-estimates
random_paper: 7
rate_limits:
- limit_count: 1
  name: Monsitools Rate Limits
  slug: monsitools-rate-limits
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: MonsiTools API Rules
  rule_count: 15
  severity_counts:
    error: 12
    hint: 0
    info: 2
    warn: 1
  slug: monsitools-rules
score:
  band: strong
  composite: 56.0
  coverage:
    artifact_dirs: 22
    catalog_earned: 85.8
    catalog_earned_first_party: 20.0
    catalog_gap: 29.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.9
  facets:
    access_clarity: 84.2
    contract_governance: 22.0
    contract_quality: 61.0
    developer_ergonomics: 42.9
    discoverability: 65.0
    operational_transparency: 36.8
  previous_composite: 48.1
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
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: rising
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/monsitools/monsitools-2026-10-11T111246.png
security:
- kind: authentication
  name: Monsitools Authentication
  slug: monsitools-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Monsitools Domain Security
  slug: monsitools-domain-security
  summary_line: TLSv1.3 · HSTS
slug: monsitools
tags:
- Company
- Calculators
- Finance
- Workflows
- MCP
- Data Tools
website: https://monsitools.com
---
