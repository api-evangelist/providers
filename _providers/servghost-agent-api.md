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
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 5
  human_in_the_loop: 1
  name: Servghost Agent Api Agentic Access
  operation_count: 14
  slug: servghost-agent-api-agentic-access
  summary_line: 14 operations · 5 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://servghost.com
  baseurl_source: declared
  description: REST API for provisioning VPS, dedicated servers, Windows RDP, GPU AI hosting, and anonymous domains. Bearer-token auth (auto-issued on first topup/order), balance funded via crypto-only top-ups, x402
  name: ServGhost Agent API
  slug: servghost-agent-api
artifact_total: 9
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/agentic-access/servghost-agent-api-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/servghost-agent-api-agentic-access.yml
- group: company
  title: ''
  type: Newsroom
  url: https://servghost.com/press
- group: docs
  title: ''
  type: Documentation
  url: https://servghost.com/guides
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/rate-limits/servghost-agent-api-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/servghost-agent-api-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/plans/servghost-agent-api-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/servghost-agent-api-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/rules/servghost-agent-api-rules.yml
  title: ''
  type: Spectral
  url: rules/servghost-agent-api-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/json-ld/servghost-agent-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/servghost-agent-api-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/vocabulary/servghost-agent-api-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/servghost-agent-api-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/data-model/servghost-agent-api-data-model.yml
  title: ''
  type: DataModel
  url: data-model/servghost-agent-api-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/conventions/servghost-agent-api-conventions.yml
  title: ''
  type: Conventions
  url: conventions/servghost-agent-api-conventions.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/sandbox/servghost-agent-api-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/servghost-agent-api-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/authentication/servghost-agent-api-authentication.yml
  title: ''
  type: Authentication
  url: authentication/servghost-agent-api-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/lifecycle/servghost-agent-api-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/servghost-agent-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://servghost.com/status
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/lifecycle/servghost-agent-api-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/servghost-agent-api-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/errors/servghost-agent-api-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/servghost-agent-api-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/conformance/servghost-agent-api-conformance.yml
  title: ''
  type: Conformance
  url: conformance/servghost-agent-api-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/llms/servghost-agent-api-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/servghost-agent-api-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/mcp/servghost-agent-api-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/servghost-agent-api-tool-crosswalk.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/servghost-agent-api/refs/heads/main/security/servghost-agent-api-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/servghost-agent-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://servghost.com
- group: commercial
  title: ''
  type: Pricing
  url: https://servghost.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://servghost.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://servghost.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://servghost.com/contact
created: '2026-09-21'
description: Agent-native offshore hosting provider offering Linux VPS, dedicated servers, Windows RDP, GPU AI compute, and anonymous domain registration across 7 jurisdictions. No-KYC, no-logs, crypto-only with instant automated deployment designed for end-to-end purchase by AI agents. Exposes a REST API (OpenAPI 3.1), a hosted MCP server, llms.txt, an agent.json discovery file, and x402 USDC payment support.
image: https://servghost.com/ServGhost.webp
jsonld:
- class_count: 2
  name: Servghost Agent Api Context
  property_count: 10
  slug: servghost-agent-api-context
layout: provider
mcp_servers:
- description: ''
  name: ServGhost Agent API MCP Server
  slug: servghost-agent-api-mcp-server
modified: '2026-09-21'
name: ServGhost Agent API
nav: Providers
network: true
overview: 'ServGhost Agent API publishes 1 API on the [APIs.io](https://apis.io/) network: ServGhost Agent API. Tagged areas include Cloud Infrastructure, VPS hosting, Dedicated Servers, GPU Compute, and AI Compute.


  The ServGhost Agent API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ServGhost Agent API''s developer surface includes documentation, sandbox, authentication, pricing, support, and 20 more developer resources.'
plans:
- name: Servghost Agent Api Plans Pricing
  plan_count: 4
  slug: servghost-agent-api-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Servghost Agent Api Rate Limits
  slug: servghost-agent-api-rate-limits
rules:
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: ServGhost Agent API API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: servghost-agent-api-rules
score:
  band: developing
  composite: 48.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 67.8
    catalog_earned_first_party: 20.0
    catalog_gap: 47.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 51.9
    developer_ergonomics: 33.3
    discoverability: 70.4
    operational_transparency: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Servghost Agent Api Authentication
  slug: servghost-agent-api-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Servghost Agent Api Domain Security
  slug: servghost-agent-api-domain-security
  summary_line: TLSv1.3 · DMARC
slug: servghost-agent-api
tags:
- Cloud Infrastructure
- VPS hosting
- Dedicated Servers
- GPU Compute
- AI Compute
- Domain Registration
- Privacy
- anonymous hosting
- offshore hosting
- Crypto Payments
- agent-native
- MCP
- x402
website: https://servghost.com
---
