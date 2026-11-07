---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Dreamthreads Agentic Access
  operation_count: 4
  slug: dreamthreads-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://mydreamthreads.xyz/api/v1/dreamgraph
  baseurl_source: declared
  description: Generate a tentative, context-aware dream reflection with a factor trace and provenance.
  name: DreamThreads Dream interpretation API
  slug: dreamthreads-dream-interpretation-api
- baseURL: https://mydreamthreads.xyz/api/v1/dreamgraph
  baseurl_source: declared
  description: Turn dream text into structured entities, emotions, actions, agency, threat, outcome, and recurrence.
  name: DreamThreads Dream parsing API
  slug: dreamthreads-dream-parsing-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/dreamthreads/mcp/dreamthreads-mcp.yml
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
  href: https://artifacts.apis.io/dreamthreads/collections/dreamthreads-postman.json
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
  href: https://artifacts.apis.io/dreamthreads/llms/dreamthreads-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dreamthreads-llms.txt
- group: agent
  href: https://artifacts.apis.io/dreamthreads/well-known/dreamthreads-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dreamthreads-well-known.yml
- group: auth
  href: https://artifacts.apis.io/dreamthreads/authentication/dreamthreads-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dreamthreads-authentication.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/conventions/dreamthreads-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dreamthreads-conventions.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/lifecycle/dreamthreads-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dreamthreads-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/conformance/dreamthreads-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dreamthreads-conformance.yml
- group: auth
  href: https://artifacts.apis.io/dreamthreads/security/dreamthreads-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dreamthreads-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dreamthreads/security/dreamthreads-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dreamthreads-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://github.com/abdulrahimiqbal/dreamthreads-developer/blob/main/SECURITY.md
- group: operate
  href: https://artifacts.apis.io/dreamthreads/rate-limits/dreamthreads-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dreamthreads-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dreamthreads/plans/dreamthreads-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dreamthreads-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/dreamthreads/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dreamthreads/agentic-access/dreamthreads-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dreamthreads-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/vocabulary/dreamthreads-dreamgraph-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dreamthreads-dreamgraph-vocabulary.yml
- group: docs
  href: https://artifacts.apis.io/dreamthreads/json-schema/_index.yml
  title: ''
  type: JSONSchema
  url: json-schema/_index.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/components/dreamthreads-components.yml
  title: ''
  type: Components
  url: components/dreamthreads-components.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/errors/dreamthreads-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dreamthreads-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dreamthreads/data-model/dreamthreads-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dreamthreads-data-model.yml
- group: build
  href: https://artifacts.apis.io/dreamthreads/examples/_index.yml
  title: ''
  type: Examples
  url: examples/_index.yml
- group: other
  href: https://artifacts.apis.io/dreamthreads/overlays/dreamthreads-dreamgraph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dreamthreads-dreamgraph-overlay.yaml
- group: build
  href: https://artifacts.apis.io/dreamthreads/mcp/dreamthreads-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/dreamthreads-tool-crosswalk.yml
created: '2026-08-13'
description: DreamThreads exposes the DreamGraph API, a context-first dream interpretation and structured parsing platform. It offers a keyless public dream parser, gated partner interpretation endpoints, a hosted MCP server, and full machine-readable contracts. Interpretations are framed as reflective, not diagnostic or predictive.
finops:
- has_sources: true
  method: derived
  name: Dreamthreads Finops
  primary_unit: ''
  service_category: ''
  slug: dreamthreads-finops
  template: true
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
  slug: io-github-abdulrahimiqbal-dreamthreads
modified: '2026-08-14'
name: DreamThreads
nav: Providers
network: true
overview: 'DreamThreads publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Dream interpretation API and Dream parsing API. Tagged areas include dream analysis, Dream interpretation, Natural Language Processing, structured parsing, and AI Agents.


  The DreamThreads catalog on APIs.io includes 1 Spectral governance ruleset.


  DreamThreads'' developer surface includes documentation, API reference, getting-started guide, support, GitHub presence, pricing, signup flow, and 29 more developer resources.'
plans:
- name: Dreamthreads Plans Pricing
  plan_count: 2
  slug: dreamthreads-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 4
  name: Dreamthreads Rate Limits
  slug: dreamthreads-rate-limits
rules:
- authorship: generated
  effective_rule_count: 103
  extends:
  - spectral:oas
  name: DreamThreads API Rules
  rule_count: 62
  severity_counts:
    error: 60
    hint: 0
    info: 1
    warn: 1
  slug: dreamthreads-rules
score:
  band: strong
  composite: 59.0
  coverage:
    artifact_dirs: 29
    catalog_earned: 66.5
    catalog_earned_first_party: 25.0
    catalog_gap: 48.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 57.5
    developer_ergonomics: 61.3
    discoverability: 75.0
    operational_transparency: 47.4
  previous_composite: 59.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/dreamthreads/dreamthreads-2026-08-17T080903.png
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
skill_count: 3
skills:
- name: Connect an agent to the DreamThreads MCP server
  slug: dreamthreads-connect-the-mcp-server
- name: Generate a reflective dream interpretation (partner key)
  slug: dreamthreads-interpret-a-dream-partner
- name: Parse a dream without a key
  slug: dreamthreads-parse-a-dream-keyless
slug: dreamthreads
tags:
- dream analysis
- Dream interpretation
- Natural Language Processing
- structured parsing
- AI Agents
- MCP Server
- OpenAPI
- wellness / sleep
- research tooling
website: https://mydreamthreads.xyz/dream-interpretation-api
---
