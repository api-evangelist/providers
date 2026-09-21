---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.1
  scored_at: '2026-09-20'
api_count: 2
apis:
- description: Agent-to-Agent (A2A 0.3.0) JSON-RPC surface for Aurelius Agent, WunderCorp's strategic planning and orchestration agent for BuilderStudio. Three published skills (strategic-planning, implementation-co
  name: Aurelius Agent A2A API
  slug: aurelius-agent-a2a-api
- baseURL: https://mpp.openmodel.sh
  baseurl_source: declared
  description: 'WunderCorp''s agent-payable REST API (OpenAPI 3.1.0, info.version 2026-07-15, contact WunderCorp, Inc. hello@wundercorp.co). Five fixed-price machine-payment products (app plan USD 1.00, BuilderStudio '
  name: Wundership MPP API
  slug: wundership-mpp-api
- baseURL: https://api.walton.bot
  baseurl_source: declared
  description: 'Walton capacity marketplace (OpenAPI 3.1.0, version 4.0.0, servers[] https://api.walton.bot): buy and sell GPU capacity, hosted model inference, edge compute, shared workspaces, service-robot time and'
  name: Walton Capacity MPP API
  slug: walton-capacity-mpp-api
artifact_total: 8
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/security/aureliusagent-dev-domain-security.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/a2a/aureliusagent-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aureliusagent-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/llms/aureliusagent-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/llms/aureliusagent-dev-wundercorp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-wundercorp-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/llms/aureliusagent-dev-builderstudio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aureliusagent-dev-builderstudio-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/packages/aureliusagent-dev-packages.yml
  title: ''
  type: Packages
  url: packages/aureliusagent-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/cli/aureliusagent-dev-cli.yml
  title: ''
  type: CLI
  url: cli/aureliusagent-dev-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/mcp/aureliusagent-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/aureliusagent-dev-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/conformance/aureliusagent-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aureliusagent-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/errors/aureliusagent-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aureliusagent-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/lifecycle/aureliusagent-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/aureliusagent-dev-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/lifecycle/aureliusagent-dev-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/aureliusagent-dev-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/authentication/aureliusagent-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/aureliusagent-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/conventions/aureliusagent-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/aureliusagent-dev-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/regulatory/aureliusagent-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/aureliusagent-dev-regulatory-posture.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/changelog/aureliusagent-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/aureliusagent-dev-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/data-model/aureliusagent-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/aureliusagent-dev-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/plans/aureliusagent-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aureliusagent-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/rate-limits/aureliusagent-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/aureliusagent-dev-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/overlays/aureliusagent-dev-wundership-mpp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aureliusagent-dev-wundership-mpp-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aureliusagent-dev/refs/heads/main/overlays/aureliusagent-dev-walton-capacity-mpp-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/aureliusagent-dev-walton-capacity-mpp-api-overlay.yaml
created: '2026-09-19'
description: 'WunderCorp, Inc. is the agentic-software company behind BuilderStudio, a local-first agentic coding IDE, and a family of agent-payable APIs. Aurelius Agent (aureliusagent.dev) is its A2A orchestration agent: a containerized runtime that plans complex software work, delegates implementation lanes to Hermes Agent workers and reviews the evidence, published with a conformant A2A 0.3.0 agent card and a JSON-RPC endpoint at rpc.aureliusagent.dev/a2a. The same host serves the Wundership MPP API, an OpenAPI 3.1 contract for machine-paid app planning, BuilderStudio previews, image generation, commerce listings and a unified inference gateway that passes HTTP 402 Machine Payments Protocol challenges through from upstream model providers, plus the Walton Capacity MPP API for buying GPU, inference, edge-compute and workspace capacity. Discovery is machine-first: /.well-known/mpp.json, llms.txt, agent-products.json and machine-payments.json on every API host.'
image: https://aureliusagent.dev/assets/aurelius-logo.png
layout: provider
mcp_servers:
- description: 'WunderCorp ships NO Model Context Protocol server for the Aurelius Agent, the Wundership MPP API or the Walton Capacity API. Searched 2026-09-19: POST tools/list to https://rpc.aureliusagent.dev/mcp, '
  name: WunderCorp MCP Server
  slug: wundercorp-mcp-server
modified: '2026-09-19'
name: WunderCorp
nav: Providers
network: true
overview: 'WunderCorp publishes 2 APIs on the [APIs.io](https://apis.io/) network: Wundership MPP API and Walton Capacity MPP API. Tagged areas include Company, Agents, A2A, Machine Payments, and MPP.


  WunderCorp''s developer surface includes documentation, pricing, support, CLI, authentication, changelog, and 23 more developer resources.'
plans:
- name: Aureliusagent Dev Plans Pricing
  plan_count: 5
  slug: aureliusagent-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Aureliusagent Dev Rate Limits
  slug: aureliusagent-dev-rate-limits
score:
  band: developing
  composite: 45.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 40.7
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 35.1
    discoverability: 75.9
    operational_transparency: 28.9
  previous_composite: 5.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Aureliusagent Dev Authentication
  slug: aureliusagent-dev-authentication
  summary_line: none/http · 5 schemes
- kind: domain-security
  name: Aureliusagent Dev Domain Security
  slug: aureliusagent-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
