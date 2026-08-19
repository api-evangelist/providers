---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 39.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dreamthreads Agentic Access
  operation_count: 4
  slug: dreamthreads-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- description: REST API for dream text parsing and interpretation. Includes a keyless public parser and liveness endpoint, plus gated partner endpoints for structured parsing and reflective interpretation. Also expo
  name: DreamGraph API
  slug: dreamgraph-api
artifact_total: 13
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://mydreamthreads.xyz/dream-interpretation-api
- group: docs
  title: ''
  type: Documentation
  url: https://mydreamthreads.xyz/dream-interpretation-api
- group: docs
  title: ''
  type: APIReference
  url: https://abdulrahimiqbal.github.io/dreamthreads-developer/
- group: start
  title: ''
  type: GettingStarted
  url: https://mydreamthreads.xyz/dream-interpretation-api#free-parser
- group: operate
  title: ''
  type: Support
  url: mailto:ariqbal@mun.ca
- group: build
  title: ''
  type: GitHub
  url: https://github.com/abdulrahimiqbal/dreamthreads-developer
- group: commercial
  title: ''
  type: Pricing
  url: https://mydreamthreads.xyz/dream-interpretation-api#request-access
- group: commercial
  title: ''
  type: Pricing
  url: https://mydreamthreads.xyz/pricing
- group: start
  title: ''
  type: SignUp
  url: https://mydreamthreads.xyz/dream-interpretation-api#request-access
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mydreamthreads.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mydreamthreads.xyz/privacy
- group: build
  title: ''
  type: Postman
  url: collections/dreamthreads-postman.json
- group: other
  title: ''
  type: APIsJSON
  url: https://mydreamthreads.xyz/apis.json
- group: agent
  title: ''
  type: MCPServer
  url: https://mydreamthreads.xyz/mcp
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dreamthreads-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/dreamthreads-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dreamthreads-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dreamthreads-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dreamthreads-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dreamthreads-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dreamthreads-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamthreads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/abdulrahimiqbal/dreamthreads-developer/blob/main/SECURITY.md
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dreamthreads-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/dreamthreads-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dreamthreads-agentic-access.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/dreamthreads-dreamgraph-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: design
  title: ''
  type: Components
  url: components/dreamthreads-components.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dreamthreads-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dreamthreads-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dreamthreads-dreamgraph-overlay.yaml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/dreamthreads-tool-crosswalk.yml
created: '2026-08-13'
description: DreamThreads exposes the DreamGraph API, a context-first dream interpretation and structured parsing platform. It offers a keyless public dream parser, gated partner interpretation endpoints, a hosted MCP server, and full machine-readable contracts. Interpretations are framed as reflective, not diagnostic or predictive.
image: https://mydreamthreads.xyz/opengraph-image
json_schemas:
- name: Dreamthreads Mcp Parse Dream Input.Schema
  property_count: 2
  slug: dreamthreads-mcp-parse-dream-input.schema
- name: Dreamthreads Mcp Parse Dream Output.Schema
  property_count: 3
  slug: dreamthreads-mcp-parse-dream-output.schema
- name: Dreamthreads Mcp Search Dream Concepts Input.Schema
  property_count: 2
  slug: dreamthreads-mcp-search-dream-concepts-input.schema
- name: Dreamthreads Mcp Search Dream Concepts Output.Schema
  property_count: 3
  slug: dreamthreads-mcp-search-dream-concepts-output.schema
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: DreamGraph MCP server manifest
  slug: dreamgraph-mcp-server-manifest
modified: '2026-08-14'
name: DreamThreads
nav: Providers
network: true
overview: 'DreamThreads publishes 1 API on the [APIs.io](https://apis.io/) network: DreamGraph API. Tagged areas include dream analysis, dream interpretation, natural language processing, structured parsing, and AI agents.


  DreamThreads'' developer surface includes documentation, API reference, getting-started guide, support, GitHub presence, pricing, signup flow, and 28 more developer resources.'
plans:
- name: Dreamthreads Plans Pricing
  plan_count: 2
  slug: dreamthreads-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 4
  name: Dreamthreads Rate Limits
  slug: dreamthreads-rate-limits
score:
  band: developing
  composite: 52.1
  delta: -0.6
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 31.8
    contract_quality: 36.6
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 31.8
    operational_transparency: 47.4
  previous_composite: 52.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dreamthreads/refs/heads/main/screenshots/dreamthreads-2026-08-17T080903.png
security:
- kind: authentication
  name: Dreamthreads Authentication
  slug: dreamthreads-authentication
  summary_line: http/none · 2 schemes
- kind: domain-security
  name: Dreamthreads Domain Security
  slug: dreamthreads-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Dreamthreads Vulnerability Disclosure
  slug: dreamthreads-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: dreamthreads
tags:
- dream analysis
- dream interpretation
- natural language processing
- structured parsing
- AI agents
- MCP server
- OpenAPI
- wellness / sleep
- research tooling
website: https://mydreamthreads.xyz/dream-interpretation-api
---
