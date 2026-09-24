---
agent_readiness:
  band: agent-ready
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
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.1
  scored_at: '2026-09-24'
api_count: 1
apis:
- baseURL: https://agentcheck.care
  baseurl_source: declared
  description: 'REST API behind agentcheck.care - start free or paid diagnostic checkups of an AI bot, validate a target URL, read the tier catalog and the shared weekly free-scan pool, follow a running checkup over '
  name: AgentCheck Checkup API
  slug: agentcheck-checkup-api
- description: Agent2Agent (A2A 0.3.0) surface of the same service - a conformant agent card at /.well-known/agent-card.json declaring two text/plain skills, free-scan and paid-checkup, and an anonymous JSON-RPC 2.0
  name: AgentCheck A2A Agent
  slug: agentcheck-a2a-agent
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://agentcheck.care/
- group: docs
  title: ''
  type: Documentation
  url: https://agentcheck.care/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agentcheck.care/redoc
- group: commercial
  title: ''
  type: Pricing
  url: https://agentcheck.care/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentcheck.care/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentcheck.care/privacy
- group: operate
  title: ''
  type: Support
  url: mailto:hello@agentcheck.care
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/a2a/agentcheck-care-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentcheck-care-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/well-known/agentcheck-care-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentcheck-care-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/mcp/agentcheck-care-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentcheck-care-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/llms/agentcheck-care-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentcheck-care-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/overlays/agentcheck-care-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentcheck-care-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/conformance/agentcheck-care-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentcheck-care-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/errors/agentcheck-care-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentcheck-care-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/lifecycle/agentcheck-care-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentcheck-care-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/authentication/agentcheck-care-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentcheck-care-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/conventions/agentcheck-care-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentcheck-care-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/security/agentcheck-care-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentcheck-care-domain-security.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/regulatory/agentcheck-care-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/agentcheck-care-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://agentcheck.care/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://agentcheck.care/privacy
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/data-model/agentcheck-care-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentcheck-care-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/plans/agentcheck-care-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentcheck-care-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/rate-limits/agentcheck-care-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentcheck-care-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentcheck-care/refs/heads/main/packages/agentcheck-care-packages.yml
  title: ''
  type: Packages
  url: packages/agentcheck-care-packages.yml
created: '2026-09-19'
description: 'AgentCheck is an AI-agent diagnostic service at agentcheck.care: give it the URL of a bot - an A2A agent or an OpenAI-compatible chat endpoint - and it runs synthetic-persona conversations, OWASP LLM Top 10 prompt-injection tests, PII-leakage scans, hallucination, over-refusal, bias and brand-alignment checks across ten modules, then delivers a scored report by magic link. A free scan needs no login; paid one-off tiers (Quick Check $10, Full Check $25, Deep Check $75) are bought through Stripe Checkout. The service is published as a 35-operation FastAPI OpenAPI 3.1.0 contract with Swagger UI and ReDoc, a machine-readable tier catalog and live free-scan quota endpoint, and is itself a conformant A2A 0.3.0 agent with two skills (free-scan, paid-checkup) served from the same host.'
image: https://agentcheck.care/static/images/logo-ac-care.webp
layout: provider
mcp_servers:
- description: ''
  name: AgentCheck MCP Server
  slug: agentcheck-mcp-server
modified: '2026-09-19'
name: AgentCheck
nav: Providers
network: true
overview: 'AgentCheck publishes 1 API on the [APIs.io](https://apis.io/) network: Checkup API. Tagged areas include AI Agents, AI Safety, Security Testing, Prompt Injection, and LLM Evaluation.


  AgentCheck''s developer surface includes documentation, API reference, pricing, support, authentication, and 21 more developer resources.'
plans:
- name: Agentcheck Care Plans Pricing
  plan_count: 4
  slug: agentcheck-care-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Agentcheck Care Rate Limits
  slug: agentcheck-care-rate-limits
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.9
    contract_governance: 18.2
    contract_quality: 44.2
    developer_ergonomics: 35.1
    discoverability: 68.5
    operational_transparency: 21.1
  previous_composite: 40.7
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Agentcheck Care Authentication
  slug: agentcheck-care-authentication
  summary_line: apiKey/token-in-path/token-in-query · 5 schemes
- kind: domain-security
  name: Agentcheck Care Domain Security
  slug: agentcheck-care-domain-security
  summary_line: TLSv1.3
slug: agentcheck-care
tags:
- AI Agents
- AI Safety
- Security Testing
- Prompt Injection
- LLM Evaluation
- A2A
- Agent-Native
- Chatbots
- Compliance
- Developer Tools
website: https://agentcheck.care/
---
