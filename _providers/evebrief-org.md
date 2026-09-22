---
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.3
  scored_at: '2026-09-21'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Evebrief Org Agentic Access
  operation_count: 5
  slug: evebrief-org-agentic-access
  summary_line: 5 operations · 1 acting
api_count: 2
apis:
- baseURL: https://oracle.evebrief.org
  baseurl_source: declared
  description: 'The FastAPI-generated OpenAPI 3.1.0 contract (info.title onchain-risk-oracle, version 0.1.0) for the oracle host: five routes — GET /.well-known/agent.json and /.well-known/agent-card.json (the A2A ca'
  name: onchain-risk-oracle API
  slug: onchain-risk-oracle-api
- description: 'Agent2Agent (A2A) protocol surface: an agent card at https://oracle.evebrief.org/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, version 0.1.0, provider "openclaw / evm-lab") ad'
  name: onchain-risk-oracle A2A Agent
  slug: onchain-risk-oracle-a2a-agent
artifact_total: 7
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/agentic-access/evebrief-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/evebrief-org-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/security/evebrief-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/evebrief-org-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/authentication/evebrief-org-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/a2a/evebrief-org-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/evebrief-org-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/well-known/evebrief-org-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/evebrief-org-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/llms/evebrief-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/evebrief-org-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/conformance/evebrief-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/evebrief-org-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/conventions/evebrief-org-conventions.yml
  title: ''
  type: Conventions
  url: conventions/evebrief-org-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/errors/evebrief-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/evebrief-org-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/lifecycle/evebrief-org-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/evebrief-org-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/rate-limits/evebrief-org-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/evebrief-org-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/plans/evebrief-org-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/evebrief-org-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/data-model/evebrief-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/evebrief-org-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/evebrief-org/refs/heads/main/skills/_index.yml
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
overview: 'openclaw / evm-lab publishes 1 API on the [APIs.io](https://apis.io/) network: onchain-risk-oracle API. Tagged areas include Agents, A2A, x402, XRPL, and Blockchain.


  openclaw / evm-lab''s developer surface includes authentication, engineering blog, documentation, API reference, and 14 more developer resources.'
plans:
- name: Evebrief Org Plans Pricing
  plan_count: 1
  slug: evebrief-org-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Evebrief Org Rate Limits
  slug: evebrief-org-rate-limits
score:
  band: thin
  composite: 27.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 43.0
    catalog_earned_first_party: 8.0
    catalog_gap: 72.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 34.7
    developer_ergonomics: 32.7
    discoverability: 64.8
    operational_transparency: 0.0
  previous_composite: 27.4
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Evebrief Org Authentication
  slug: evebrief-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Evebrief Org Domain Security
  slug: evebrief-org-domain-security
  summary_line: TLSv1.3
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
- Fraud Detection
- Risk
- agent-native
- Market Intelligence
website: https://evebrief.org/
---
