---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dreamthreads Agentic Access
  operation_count: 4
  slug: dreamthreads-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 2
apis:
- description: Generate a tentative, context-aware dream reflection with a factor trace and provenance.
  name: DreamThreads Dream interpretation API
  slug: dreamthreads-dream-interpretation-api
- description: Turn dream text into structured entities, emotions, actions, agency, threat, outcome, and recurrence.
  name: DreamThreads Dream parsing API
  slug: dreamthreads-dream-parsing-api
artifact_total: 14
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dreamthreads-mcp.yml
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
- description: Parse dreams into structured context and search DreamGraph concepts without storing dream text.
  name: DreamThreads MCP Server
  slug: dreamthreads-mcp-server
- description: ''
  name: Public DreamGraph MCP server (streamable-http, keyless)
  slug: public-dreamgraph-mcp-server-streamable-http-keyless
modified: '2026-08-14'
name: DreamThreads
nav: Providers
network: true
overview: 'DreamThreads publishes 2 APIs on the [APIs.io](https://apis.io/) network: Dream interpretation API and Dream parsing API. Tagged areas include dream analysis, Dream interpretation, natural language processing, structured parsing, and AI Agents.


  DreamThreads'' developer surface includes documentation, API reference, getting-started guide, support, GitHub presence, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Dreamthreads Plans Pricing
  plan_count: 2
  slug: dreamthreads-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 4
  name: Dreamthreads Rate Limits
  slug: dreamthreads-rate-limits
score:
  band: strong
  composite: 57.4
  coverage:
    artifact_dirs: 24
    catalog_gap: 53.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 19.7
    contract_quality: 63.6
    developer_ergonomics: 61.3
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 47.4
  previous_composite: 57.4
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
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- Dream interpretation
- natural language processing
- structured parsing
- AI Agents
- MCP server
- OpenAPI
- wellness / sleep
- research tooling
website: https://mydreamthreads.xyz/dream-interpretation-api
---
