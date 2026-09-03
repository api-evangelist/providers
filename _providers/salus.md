---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/salus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.usesalus.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.usesalus.ai/pricing
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.usesalus.ai/trust
created: '2026-07-17'
description: Salus provides runtime validation and governance for AI agents. It sits between an agent and its tools as a policy-aware proxy that intercepts each action before it executes, then clarifies, rewrites, escalates for human review, or blocks it against organizational policies — managing commit-time risk on financial transfers, appointment changes, and data modifications before they alter customer data, finances, or records. Integration requires only an endpoint URL change (no agent rewrite), and Salus works across OpenAI, Anthropic, Gemini, LangChain, LangGraph, CrewAI, Retell, Vapi, and custom tools. Capabilities include evidence-based validation, PII detection, budget and loop protection, idempotency checks, human-in-the-loop escalation, self-repair of blocked actions, and integrated evals and observability. Salus is a Y Combinator (Winter 2026) company based in San Francisco.
image: https://www.usesalus.ai/og.svg
layout: provider
modified: '2026-07-21'
name: Salus
nav: Providers
network: true
overview: 'Salus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Runtime Validation, Agent Governance, and AI Safety.


  Salus'' developer surface includes pricing and 3 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/salus/refs/heads/main/screenshots/salus-2026-09-02T154332.png
security:
- kind: domain-security
  name: Salus Domain Security
  slug: salus-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: salus
tags:
- Company
- AI Agents
- Runtime Validation
- Agent Governance
- AI Safety
- Guardrails
- Developer Tools
- Infrastructure
website: https://www.usesalus.ai/
---
