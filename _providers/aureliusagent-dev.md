---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Agent-to-Agent (A2A 0.3.0) JSON-RPC surface for Aurelius Agent, WunderCorp's strategic planning and orchestration agent for BuilderStudio. Three published skills (strategic-planning, implementation-co
  name: Aurelius Agent A2A API
  slug: aurelius-agent-a2a-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Paid AI generation utilities.
  name: WunderCorp AI Generation API
  slug: aureliusagent-dev-ai-generation-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Software planning and implementation direction for agent callers.
  name: WunderCorp App Planning API
  slug: aureliusagent-dev-app-planning-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: BuilderStudio preview and app-generation support endpoints.
  name: WunderCorp Builder Studio API
  slug: aureliusagent-dev-builderstudio-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: The Capacity API from WunderCorp — 2 operation(s) for capacity.
  name: WunderCorp Capacity API
  slug: aureliusagent-dev-capacity-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Paid commerce metadata generation utilities.
  name: WunderCorp Commerce API
  slug: aureliusagent-dev-commerce-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Transparent MPP routing to supported model, media, speech, and document intelligence providers.
  name: WunderCorp Inference Gateway API
  slug: aureliusagent-dev-inference-gateway-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Paid Wundership endpoints that agents can invoke after MPP payment.
  name: WunderCorp Machine Payments API
  slug: aureliusagent-dev-machine-payments-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: The Mpp API from WunderCorp — 8 operation(s) for mpp.
  name: WunderCorp Mpp API
  slug: aureliusagent-dev-mpp-api
- baseURL: https://rpc.aureliusagent.dev/a2a
  baseurl_source: declared
  description: Paid access to effective-dated model pricing and cost-weighted allowance estimates.
  name: WunderCorp OpenModel Pricing API
  slug: aureliusagent-dev-openmodel-pricing-api
artifact_total: 20
common:
- group: other
  href: https://artifacts.apis.io/aureliusagent-dev/capabilities/aureliusagent-dev-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/aureliusagent-dev-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/aureliusagent-dev/security/aureliusagent-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aureliusagent-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aureliusagent.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://wundercorp.co/agents/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wundercorp
- group: commercial
  title: ''
  type: Pricing
  url: https://wundercorp.co/agents/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wundercorp.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wundercorp.co/privacy
- group: operate
  title: ''
  type: Support
  url: https://builderstudio.dev/support
- group: other
  href: https://artifacts.apis.io/aureliusagent-dev/a2a/aureliusagent-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aureliusagent-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aureliusagent-dev/llms/aureliusagent-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/aureliusagent-dev/llms/aureliusagent-dev-wundercorp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-wundercorp-llms.txt
- group: agent
  href: https://artifacts.apis.io/aureliusagent-dev/llms/aureliusagent-dev-builderstudio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-builderstudio-llms.txt
- group: build
  href: https://artifacts.apis.io/aureliusagent-dev/packages/aureliusagent-dev-packages.yml
  title: ''
  type: Packages
  url: packages/aureliusagent-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/aureliusagent-dev/cli/aureliusagent-dev-cli.yml
  title: ''
  type: CLI
  url: cli/aureliusagent-dev-cli.yml
- group: agent
  href: https://artifacts.apis.io/aureliusagent-dev/mcp/aureliusagent-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aureliusagent-dev-mcp.yml
- group: design
  href: https://artifacts.apis.io/aureliusagent-dev/conformance/aureliusagent-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aureliusagent-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/aureliusagent-dev/errors/aureliusagent-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aureliusagent-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aureliusagent-dev/lifecycle/aureliusagent-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aureliusagent-dev-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/aureliusagent-dev/lifecycle/aureliusagent-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aureliusagent-dev-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/aureliusagent-dev/authentication/aureliusagent-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aureliusagent-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/aureliusagent-dev/conventions/aureliusagent-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aureliusagent-dev-conventions.yml
- group: other
  href: https://artifacts.apis.io/aureliusagent-dev/regulatory/aureliusagent-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/aureliusagent-dev-regulatory-posture.yml
- group: operate
  href: https://artifacts.apis.io/aureliusagent-dev/changelog/aureliusagent-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aureliusagent-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/aureliusagent-dev/data-model/aureliusagent-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aureliusagent-dev-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/aureliusagent-dev/plans/aureliusagent-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aureliusagent-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/aureliusagent-dev/rate-limits/aureliusagent-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aureliusagent-dev-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/aureliusagent-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/aureliusagent-dev/overlays/aureliusagent-dev-wundership-mpp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aureliusagent-dev-wundership-mpp-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/aureliusagent-dev/overlays/aureliusagent-dev-walton-capacity-mpp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aureliusagent-dev-walton-capacity-mpp-api-overlay.yaml
created: '2026-09-19'
description: 'WunderCorp, Inc. is the agentic-software company behind BuilderStudio, a local-first agentic coding IDE, and a family of agent-payable APIs. Aurelius Agent (aureliusagent.dev) is its A2A orchestration agent: a containerized runtime that plans complex software work, delegates implementation lanes to Hermes Agent workers and reviews the evidence, published with a conformant A2A 0.3.0 agent card and a JSON-RPC endpoint at rpc.aureliusagent.dev/a2a. The same host serves the Wundership MPP API, an OpenAPI 3.1 contract for machine-paid app planning, BuilderStudio previews, image generation, commerce listings and a unified inference gateway that passes HTTP 402 Machine Payments Protocol challenges through from upstream model providers, plus the Walton Capacity MPP API for buying GPU, inference, edge-compute and workspace capacity. Discovery is machine-first: /.well-known/mpp.json, llms.txt, agent-products.json and machine-payments.json on every API host.'
finops:
- has_sources: true
  method: derived
  name: Aureliusagent Dev Finops
  primary_unit: ''
  service_category: ''
  slug: aureliusagent-dev-finops
  template: true
image: https://aureliusagent.dev/assets/aurelius-logo.png
layout: provider
mcp_servers:
- description: 'WunderCorp ships NO Model Context Protocol server for the Aurelius Agent, the Wundership MPP API or the Walton Capacity API. Searched 2026-09-19: POST tools/list to https://rpc.aureliusagent.dev/mcp, '
  name: WunderCorp MCP Server
  slug: aureliusagent-dev
modified: '2026-09-19'
name: WunderCorp
nav: Providers
network: true
overview: 'WunderCorp publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI Generation API, App Planning API, Builder Studio API, and 7 more. Tagged areas include Company, Agents, A2A, Machine Payments, and MPP.


  The WunderCorp catalog on APIs.io includes 1 Spectral governance ruleset.


  WunderCorp''s developer surface includes documentation, pricing, support, CLI, authentication, changelog, and 24 more developer resources.'
plans:
- name: Aureliusagent Dev Plans Pricing
  plan_count: 5
  slug: aureliusagent-dev-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Aureliusagent Dev Rate Limits
  slug: aureliusagent-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: WunderCorp API Rules
  rule_count: 57
  severity_counts:
    error: 47
    hint: 0
    info: 3
    warn: 7
  slug: aureliusagent-dev-rules
score:
  band: developing
  composite: 41.3
  coverage:
    artifact_dirs: 29
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.4
  facets:
    access_clarity: 47.4
    contract_governance: 31.8
    contract_quality: 50.5
    developer_ergonomics: 28.0
    discoverability: 73.2
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 77.8
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/aureliusagent-dev/aureliusagent-dev-2026-10-11T100849.png
security:
- kind: authentication
  name: Aureliusagent Dev Authentication
  slug: aureliusagent-dev-authentication
  summary_line: none/http · 5 schemes
- kind: domain-security
  name: Aureliusagent Dev Domain Security
  slug: aureliusagent-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Buy a Wundership app plan through an MPP 402 challenge
  slug: aureliusagent-dev-buy-an-app-plan
- name: Call the OpenModel MPP inference gateway
  slug: aureliusagent-dev-call-the-inference-gateway
- name: Quote, pay for and hand off a capacity session
  slug: aureliusagent-dev-reserve-capacity
slug: aureliusagent-dev
tags:
- Company
- Agents
- A2A
- Machine Payments
- MPP
- HTTP 402
- Artificial Intelligence
- Inference Gateway
- Code Generation
- Developer Tools
- Compute Capacity
- Orchestration
website: https://aureliusagent.dev/
---
