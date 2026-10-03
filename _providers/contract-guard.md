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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-10-03'
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
artifact_total: 9
asyncapis:
- description: ''
  name: Contract Guard Webhooks
  slug: contract-guard-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/agentic-access/contract-guard-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/contract-guard-agentic-access.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/plans/contract-guard-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contract-guard-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/rules/contract-guard-rules.yml
  title: ''
  type: Spectral
  url: rules/contract-guard-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/asyncapi/contract-guard-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/contract-guard-webhooks.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/cli/contract-guard-cli.yml
  title: ''
  type: CLI
  url: cli/contract-guard-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.railway.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/authentication/contract-guard-authentication.yml
  title: ''
  type: Authentication
  url: authentication/contract-guard-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/errors/contract-guard-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/contract-guard-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/conformance/contract-guard-conformance.yml
  title: ''
  type: Conformance
  url: conformance/contract-guard-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/overlays/contract-guard-openapi-overlay.yml
  title: ''
  type: Overlay
  url: overlays/contract-guard-openapi-overlay.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/llms/contract-guard-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contract-guard-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/mcp/contract-guard-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/contract-guard-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/well-known/contract-guard-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contract-guard-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/hosts/contract-guard-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contract-guard-hosts.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.railway.com/quick-start
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/security/contract-guard-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/contract-guard-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/contract-guard/refs/heads/main/security/contract-guard-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contract-guard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contract-guard-production.up.railway.app/
- group: docs
  title: ''
  type: Documentation
  url: https://contract-guard-production.up.railway.app/openapi.json
- group: docs
  title: ''
  type: APIReference
  url: https://contract-guard-production.up.railway.app/mcp
- group: build
  title: ''
  type: Postman
  url: https://contract-guard-production.up.railway.app/postman_collection.json
- group: commercial
  title: ''
  type: Pricing
  url: https://contract-guard-production.up.railway.app/v1/products
- group: other
  title: ''
  type: Health
  url: https://contract-guard-production.up.railway.app/healthz
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
layout: provider
mcp_servers:
- description: ''
  name: Contract Guard / Autonomous Utility Factory MCP Server
  slug: contract-guard-autonomous-utility-factory-mcp-server
modified: '2026-10-02'
name: Contract Guard / Autonomous Utility Factory
nav: Providers
network: true
overview: 'Contract Guard / Autonomous Utility Factory publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include JSON Validation and AI Trust.


  The Contract Guard / Autonomous Utility Factory catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Contract Guard / Autonomous Utility Factory''s developer surface includes CLI, authentication, getting-started guide, documentation, API reference, pricing, and 17 more developer resources.'
plans:
- name: Contract Guard Plans Pricing
  plan_count: 4
  slug: contract-guard-plans-pricing
random_paper: 8
rules:
- effective_rule_count: 48
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
  band: developing
  composite: 43.9
  coverage:
    artifact_dirs: 15
    catalog_earned: 46.5
    catalog_earned_first_party: 12.0
    catalog_gap: 68.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 57.9
    contract_governance: 31.8
    contract_quality: 39.0
    developer_ergonomics: 52.4
    discoverability: 63.3
    operational_transparency: 7.9
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
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
