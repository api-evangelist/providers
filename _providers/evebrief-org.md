---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Paid · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Evebrief Org Agentic Access
  operation_count: 5
  slug: evebrief-org-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 1
apis:
- description: 'Agent2Agent (A2A) protocol surface: an agent card at https://oracle.evebrief.org/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 0.1.0, provider "openclaw / evm-lab") ad'
  name: onchain-risk-oracle A2A Agent
  slug: onchain-risk-oracle-a2a-agent
- baseURL: https://oracle.evebrief.org
  baseurl_source: declared
  description: The Healthz API from openclaw / evm-lab — 1 operation(s) for healthz.
  name: openclaw / evm-lab Healthz API
  slug: evebrief-org-healthz-api
- baseURL: https://oracle.evebrief.org
  baseurl_source: declared
  description: The Onchain Risk Oracle API from openclaw / evm-lab — 1 operation(s) for onchain risk oracle.
  name: openclaw / evm-lab Onchain Risk Oracle API
  slug: evebrief-org-onchain-risk-oracle-api
- baseURL: https://oracle.evebrief.org
  baseurl_source: declared
  description: The .well Known API from openclaw / evm-lab — 3 operation(s) for .well known.
  name: openclaw / evm-lab .well Known API
  slug: evebrief-org-well-known-api
artifact_total: 11
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://oracle.evebrief.org/.well-known/x402
- group: other
  href: https://artifacts.apis.io/evebrief-org/overlays/evebrief-org-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/evebrief-org-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/evebrief-org/agentic-access/evebrief-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evebrief-org-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/evebrief-org/security/evebrief-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evebrief-org-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/evebrief-org/authentication/evebrief-org-authentication.yml
  title: ''
  type: Authentication
  url: authentication/evebrief-org-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://evebrief.org/
- group: company
  title: ''
  type: Blog
  url: https://evebrief.org/blog/
- group: docs
  title: ''
  type: Documentation
  url: https://oracle.evebrief.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://oracle.evebrief.org/redoc
- group: other
  href: https://artifacts.apis.io/evebrief-org/a2a/evebrief-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/evebrief-org-a2a.yml
- group: agent
  href: https://artifacts.apis.io/evebrief-org/well-known/evebrief-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evebrief-org-well-known.yml
- group: agent
  href: https://artifacts.apis.io/evebrief-org/llms/evebrief-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evebrief-org-llms.txt
- group: design
  href: https://artifacts.apis.io/evebrief-org/conformance/evebrief-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evebrief-org-conformance.yml
- group: design
  href: https://artifacts.apis.io/evebrief-org/conventions/evebrief-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/evebrief-org-conventions.yml
- group: design
  href: https://artifacts.apis.io/evebrief-org/errors/evebrief-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evebrief-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/evebrief-org/lifecycle/evebrief-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evebrief-org-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/evebrief-org/rate-limits/evebrief-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/evebrief-org-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/evebrief-org/plans/evebrief-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evebrief-org-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/evebrief-org/data-model/evebrief-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evebrief-org-data-model.yml
- group: agent
  href: https://artifacts.apis.io/evebrief-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-09-19'
description: 'openclaw / evm-lab is the operator name on an A2A agent card served from oracle.evebrief.org, a subdomain of evebrief.org. The apex site is EveBrief, a waitlist-stage market and competitor intelligence briefing product for boutique agencies and independent consultants (indicative tiers Free / $19 / $39 a month; no API of its own). The oracle subdomain runs onchain-risk-oracle: a pay-per-task agent that checks an EVM address (eth, base, bsc, arb, op, polygon) against a curated rug-pull feed (114,110 records at probe time) and returns a none / low / high / critical risk verdict with labels, reasons and evidence. It is published as an A2A 0.3.0 JSON-RPC agent at https://oracle.evebrief.org/ (agent card at /.well-known/agent-card.json and the legacy /.well-known/agent.json), gated by x402 v2 payment of 0.01 RLUSD on the XRP Ledger mainnet through the t54 facilitator, and described by a FastAPI-generated OpenAPI 3.1.0 at /openapi.json with Swagger UI at /docs and ReDoc at /redoc.
  The card''s provider.url credits the OpenClaw open-source agent framework (github.com/openclaw/openclaw); that organization is the software the agent runs on, not this operator.'
layout: provider
modified: '2026-09-19'
name: openclaw / evm-lab
nav: Providers
network: true
overview: 'openclaw / evm-lab publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Healthz API, Onchain Risk Oracle API, .well Known API, and 1 more. Tagged areas include Agents, A2A, x402, XRPL, and Blockchain.


  The openclaw / evm-lab catalog on APIs.io includes 1 Spectral governance ruleset.


  openclaw / evm-lab''s developer surface includes pricing, authentication, engineering blog, documentation, API reference, and 15 more developer resources.'
plans:
- name: Evebrief Org Plans Pricing
  plan_count: 1
  slug: evebrief-org-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Evebrief Org Rate Limits
  slug: evebrief-org-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: openclaw / evm-lab API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: evebrief-org-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 47.5
    catalog_earned_first_party: 8.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.0
  facets:
    access_clarity: 26.3
    contract_governance: 31.8
    contract_quality: 37.4
    developer_ergonomics: 23.2
    discoverability: 62.5
    operational_transparency: 0.0
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/evebrief-org/evebrief-org-2026-10-11T104312.png
security:
- kind: authentication
  name: Evebrief Org Authentication
  slug: evebrief-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Evebrief Org Domain Security
  slug: evebrief-org-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: Check an EVM address for rug-pull risk (paid, A2A + x402 on XRPL)
  slug: evebrief-org-onchain-risk-check
slug: evebrief-org
tags:
- Agents
- A2A
- x402
- XRPL
- Blockchain
- DeFi
- EVM
- Security
- Fraud Prevention
- Risk Management
- Agent-Native
- Market Intelligence
website: https://evebrief.org/
---
