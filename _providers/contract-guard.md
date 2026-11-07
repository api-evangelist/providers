---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Contract Guard Agentic Access
  operation_count: 10
  slug: contract-guard-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- description: Deterministic JSON Schema validation API with explicit violations.
  name: Contract Guard API
  slug: contract-guard-api
artifact_total: 11
asyncapis:
- description: ''
  name: Contract Guard Webhooks
  slug: contract-guard-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/contract-guard/finops/contract-guard-finops.yml
  title: ''
  type: FinOps
  url: finops/contract-guard-finops.yml
- group: agent
  href: https://artifacts.apis.io/contract-guard/agentic-access/contract-guard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contract-guard-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/contract-guard/plans/contract-guard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contract-guard-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/contract-guard/rules/contract-guard-rules.yml
  title: ''
  type: Spectral
  url: rules/contract-guard-rules.yml
- group: design
  href: https://artifacts.apis.io/contract-guard/asyncapi/contract-guard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contract-guard-webhooks.yml
- group: build
  href: https://artifacts.apis.io/contract-guard/cli/contract-guard-cli.yml
  title: ''
  type: CLI
  url: cli/contract-guard-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.railway.com/
- group: auth
  href: https://artifacts.apis.io/contract-guard/authentication/contract-guard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contract-guard-authentication.yml
- group: design
  href: https://artifacts.apis.io/contract-guard/errors/contract-guard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contract-guard-problem-types.yml
- group: design
  href: https://artifacts.apis.io/contract-guard/conformance/contract-guard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contract-guard-conformance.yml
- group: other
  href: https://artifacts.apis.io/contract-guard/overlays/contract-guard-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/contract-guard-openapi-overlay.yml
- group: agent
  href: https://artifacts.apis.io/contract-guard/llms/contract-guard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contract-guard-llms.txt
- group: agent
  href: https://artifacts.apis.io/contract-guard/mcp/contract-guard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contract-guard-mcp.yml
- group: agent
  href: https://artifacts.apis.io/contract-guard/well-known/contract-guard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contract-guard-well-known.yml
- group: other
  href: https://artifacts.apis.io/contract-guard/hosts/contract-guard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contract-guard-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.railway.com/quick-start
- group: auth
  href: https://artifacts.apis.io/contract-guard/security/contract-guard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contract-guard-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/contract-guard/security/contract-guard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contract-guard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contract-guard-production.up.railway.app/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://contract-guard-production.up.railway.app/openapi.json
  - status: 401
    url: https://contract-guard-production.up.railway.app/mcp
  reason: partner-login
  state: gated
created: '2026-10-02'
description: Contract Guard provides a deterministic JSON Schema validation API for software and AI workflows. It returns exact validation violations and optional conservative type normalization. The service is operated by WOODS HOLDING GROUP LLC and is currently in an experimental live state with billing disabled. It offers a public demo, OpenAPI 3.1 spec, MCP endpoint, ARD manifest, Postman collection, and product registry.
finops:
- has_sources: true
  method: derived
  name: Contract Guard Finops
  primary_unit: subscription
  service_category: ''
  slug: contract-guard-finops
  template: false
layout: provider
mcp_servers:
- description: Remote MCP server at contract-guard-production.up.railway.app.
  name: Contract Guard / Autonomous Utility Factory MCP Server
  slug: contract-guard-mcp-yml
modified: '2026-10-02'
name: Contract Guard / Autonomous Utility Factory
nav: Providers
network: true
overview: 'Contract Guard / Autonomous Utility Factory is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include JSON Validation and AI Trust.


  The Contract Guard / Autonomous Utility Factory catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Contract Guard / Autonomous Utility Factory''s developer surface includes CLI, authentication, getting-started guide, and 16 more developer resources.'
plans:
- name: Contract Guard Plans Pricing
  plan_count: 4
  slug: contract-guard-plans-pricing
- name: Contract Guard Price Estimates
  plan_count: 0
  slug: contract-guard-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 48
  extends:
  - spectral:oas
  name: Contract Guard / Autonomous Utility Factory API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: contract-guard-rules
score:
  band: thin
  composite: 36.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 49.5
    catalog_earned_first_party: 12.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 51.3
    contract_governance: 31.8
    contract_quality: 39.0
    developer_ergonomics: 25.0
    discoverability: 63.3
    operational_transparency: 7.9
  previous_composite: 45.5
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/contract-guard/contract-guard-2026-10-11T103244.png
security:
- kind: authentication
  name: Contract Guard Authentication
  slug: contract-guard-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Contract Guard Domain Security
  slug: contract-guard-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Contract Guard Trust Center
  slug: contract-guard-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: contract-guard
tags:
- JSON Validation
- AI Trust
website: https://contract-guard-production.up.railway.app/
---
