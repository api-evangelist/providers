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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 37.2
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Getaiscan App Agentic Access
  operation_count: 20
  slug: getaiscan-app-agentic-access
  summary_line: 20 operations · 19 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.getaiscan.app
  baseurl_source: declared
  description: 'Pay-per-capability REST API for AI-visibility auditing: five cheap HTTP checks (site health and AI-crawler access, llms.txt, Schema.org JSON-LD, agent files, MCP discoverability), four category scores'
  name: AIScan Agent API
  slug: aiscan-agent-api
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://getaiscan.app/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, card version 5.9.1) advertising 18 skills — t'
  name: AIScan A2A Agent
  slug: aiscan-a2a-agent
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://getaiscan.app/
- group: docs
  title: ''
  type: Documentation
  url: https://getaiscan.app/llms.txt
- group: docs
  title: ''
  type: APIReference
  url: https://api.getaiscan.app/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://api.getaiscan.app/api/agent/index
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/a2a/getaiscan-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getaiscan-app-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/well-known/getaiscan-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getaiscan-app-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/llms/getaiscan-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getaiscan-app-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://getaiscan.app/llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/authentication/getaiscan-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getaiscan-app-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/conventions/getaiscan-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getaiscan-app-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/errors/getaiscan-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getaiscan-app-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/data-model/getaiscan-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getaiscan-app-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/rate-limits/getaiscan-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getaiscan-app-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/plans/getaiscan-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getaiscan-app-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/conformance/getaiscan-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getaiscan-app-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/lifecycle/getaiscan-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getaiscan-app-lifecycle.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/security/getaiscan-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getaiscan-app-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/agentic-access/getaiscan-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getaiscan-app-agentic-access.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getaiscan-app/refs/heads/main/packages/getaiscan-app-packages.yml
  title: ''
  type: Packages
  url: packages/getaiscan-app-packages.yml
created: '2026-09-19'
description: AIScan is an AI-visibility auditing service at getaiscan.app that scans any website in about 60 seconds and returns four 0-100 scores — AEO (AI search visibility), GEO (citation readiness), Agent Readiness and MCP Readiness — from 80+ checks, plus a Brand Visibility measurement of how often AI assistants actually name a brand across 30 realistic niche prompts. Humans buy a full report on the site for 60 USDC; software agents buy 19 individual capabilities pay-per-call (0.06-3.50 USDC) through the x402 protocol on Base (eip155:8453) with no API key and no account, via a 20-operation OpenAPI 3.1.0 REST contract served from api.getaiscan.app, an A2A 0.3.0 agent card with 18 skills at /.well-known/agent-card.json, an ai-plugin.json manifest and an MCP discovery descriptor at /.well-known/mcp.json. Every paid route answers an unpaid call with a real HTTP 402 x402 V2 challenge; the capability catalog at GET /api/agent/index is free.
image: https://getaiscan.app/og-image.jpg
layout: provider
modified: '2026-09-19'
name: AIScan
nav: Providers
network: true
overview: 'AIScan publishes 1 API on the [APIs.io](https://apis.io/) network: Agent API. Tagged areas include AI Visibility, Website Auditing, SEO, Answer Engine Optimization, and Generative Engine Optimization.


  AIScan''s developer surface includes documentation, API reference, pricing, authentication, and 16 more developer resources.'
plans:
- name: Getaiscan App Plans Pricing
  plan_count: 20
  slug: getaiscan-app-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Getaiscan App Rate Limits
  slug: getaiscan-app-rate-limits
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 53.9
    developer_ergonomics: 30.4
    discoverability: 75.9
    operational_transparency: 0.0
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Getaiscan App Authentication
  slug: getaiscan-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Getaiscan App Domain Security
  slug: getaiscan-app-domain-security
  summary_line: TLSv1.3
slug: getaiscan-app
tags:
- AI Visibility
- Website Auditing
- SEO
- Answer Engine Optimization
- Generative Engine Optimization
- Agents
- Agentic Commerce
- A2A
- MCP
- x402
- Agent-Native
website: https://getaiscan.app/
---
