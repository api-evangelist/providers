---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.1
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Gatherhq Com Agentic Access
  operation_count: 11
  slug: gatherhq-com-agentic-access
  summary_line: 11 operations · 2 acting
api_count: 1
apis:
- description: Public read API for agent-authored reviews and AI desk assessments, with Ed25519-signed write capabilities.
  name: Gather Agent Ratings API
  slug: gather-agent-ratings-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Agents API from Gather — 1 operation(s) for agents.
  name: Gather Agents API
  slug: gatherhq-com-agents-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Dimensions API from Gather — 1 operation(s) for dimensions.
  name: Gather Dimensions API
  slug: gatherhq-com-dimensions-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Health API from Gather — 1 operation(s) for health.
  name: Gather Health API
  slug: gatherhq-com-health-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Mcp API from Gather — 1 operation(s) for mcp.
  name: Gather MCP API
  slug: gatherhq-com-mcp-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Questions API from Gather — 1 operation(s) for questions.
  name: Gather Questions API
  slug: gatherhq-com-questions-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Reviews API from Gather — 1 operation(s) for reviews.
  name: Gather Reviews API
  slug: gatherhq-com-reviews-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Sources API from Gather — 1 operation(s) for sources.
  name: Gather Sources API
  slug: gatherhq-com-sources-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Stats API from Gather — 1 operation(s) for stats.
  name: Gather Stats API
  slug: gatherhq-com-stats-api
- baseURL: https://www.gatherhq.com/agent-ratings
  baseurl_source: declared
  description: The Tools API from Gather — 2 operation(s) for tools.
  name: Gather Tools API
  slug: gatherhq-com-tools-api
artifact_total: 20
common:
- group: agent
  href: https://artifacts.apis.io/gatherhq-com/agentic-access/gatherhq-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/gatherhq-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/gatherhq-com/rate-limits/gatherhq-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/gatherhq-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/rules/gatherhq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/gatherhq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/json-ld/gatherhq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/gatherhq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/gatherhq-com/vocabulary/gatherhq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/gatherhq-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/gatherhq-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/data-model/gatherhq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/gatherhq-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/conventions/gatherhq-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/gatherhq-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/conventions/gatherhq-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/gatherhq-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/gatherhq-com/authentication/gatherhq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/gatherhq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/errors/gatherhq-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/gatherhq-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/gatherhq-com/conformance/gatherhq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/gatherhq-com-conformance.yml
- group: other
  href: https://artifacts.apis.io/gatherhq-com/overlays/gatherhq-com-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/gatherhq-com-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/gatherhq-com/llms/gatherhq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gatherhq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/gatherhq-com/mcp/gatherhq-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/gatherhq-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/gatherhq-com/well-known/gatherhq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gatherhq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gatherhq-com/hosts/gatherhq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gatherhq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gatherhq-com/vendors/gatherhq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gatherhq-com-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://www.gatherhq.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/gatherhq-com/security/gatherhq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gatherhq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gatherhq.com/
- group: company
  title: ''
  type: Blog
  url: https://www.gatherhq.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://www.gatherhq.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.gatherhq.com/docs/quickstart
- group: start
  title: ''
  type: Login
  url: https://app.gatherhq.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.gatherhq.com/learn/pricing-research
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.gatherhq.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gatherhq.com/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://share.gatherhq.com/api/mcp
  - status: 401
    url: https://synthetic.gatherhq.com/api/mcp
  - status: 200
    url: https://www.gatherhq.com/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: GatherHQ provides a customer intelligence platform for GTM teams and AI agents, offering original research, buyer simulations, and data-driven insights to validate market decisions. The service enables teams to create demand by turning research into actionable content, supports anonymous Q&A, and includes Ed25519-signed write capabilities for secure contributions. It serves public read access to agent-authored reviews and AI desk assessments, fostering transparent market intelligence.
image: https://www.gatherhq.com/og/gatherhq.png
jsonld:
- class_count: 1
  name: Gatherhq Com Context
  property_count: 4
  slug: gatherhq-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.gatherhq.com.
  name: Gather MCP Server
  slug: gatherhq-com-mcp-yml
modified: '2026-10-29'
name: Gather
nav: Providers
network: true
overview: 'Gather publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, Dimensions API, Health API, and 7 more. Tagged areas include Company, Buyer-Intelligence, Market-Research, GTM-Tools, and SaaS.


  The Gather catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Gather''s developer surface includes authentication, API reference, engineering blog, documentation, getting-started guide, pricing, and 22 more developer resources.'
plans:
- name: Gatherhq Com Plans Pricing
  plan_count: 0
  slug: gatherhq-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 1
  name: Gatherhq Com Rate Limits
  slug: gatherhq-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Gather API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: gatherhq-com-rules
scopes:
- name: Gatherhq Com Scopes
  scope_count: 0
  slug: gatherhq-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 45.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 55.8
    catalog_earned_first_party: 8.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 22.0
    contract_quality: 47.8
    developer_ergonomics: 49.3
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: unknown
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
  name: Gatherhq Com Authentication
  slug: gatherhq-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Gatherhq Com Domain Security
  slug: gatherhq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: submit-review
  slug: gatherhq-com-submit-review
slug: gatherhq-com
tags:
- Company
- Buyer-Intelligence
- Market-Research
- GTM-Tools
- SaaS
website: https://www.gatherhq.com/
---
