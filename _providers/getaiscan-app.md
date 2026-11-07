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
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 34.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 19
  human_in_the_loop: 1
  name: Getaiscan App Agentic Access
  operation_count: 20
  slug: getaiscan-app-agentic-access
  summary_line: 20 operations · 19 acting · 1 human-in-the-loop
api_count: 3
apis:
- description: 'Agent2Agent (A2A) protocol surface: an agent card served from https://getaiscan.app/.well-known/agent-card.json (protocolVersion 0.3.0, JSONRPC transport, card version 5.9.1) advertising 18 skills — t'
  name: AIScan A2A Agent
  slug: aiscan-a2a-agent
- baseURL: https://api.getaiscan.app
  baseurl_source: declared
  description: The Agent API from AIScan — 2 operation(s) for agent.
  name: AIScan Agent API
  slug: getaiscan-app-agent-api
- baseURL: https://api.getaiscan.app
  baseurl_source: declared
  description: The AI Visibility API from AIScan — 19 operation(s) for ai visibility.
  name: AIScan AI Visibility API
  slug: getaiscan-app-ai-visibility-api
artifact_total: 12
common:
- group: company
  title: ''
  type: Blog
  url: https://getaiscan.app/blog/
- group: other
  href: https://artifacts.apis.io/getaiscan-app/overlays/getaiscan-app-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getaiscan-app-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/getaiscan-app/a2a/getaiscan-app-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/getaiscan-app-a2a.yml
- group: agent
  href: https://artifacts.apis.io/getaiscan-app/well-known/getaiscan-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getaiscan-app-well-known.yml
- group: agent
  href: https://artifacts.apis.io/getaiscan-app/llms/getaiscan-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getaiscan-app-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://getaiscan.app/llms.txt
- group: auth
  href: https://artifacts.apis.io/getaiscan-app/authentication/getaiscan-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getaiscan-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/getaiscan-app/conventions/getaiscan-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getaiscan-app-conventions.yml
- group: design
  href: https://artifacts.apis.io/getaiscan-app/errors/getaiscan-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/getaiscan-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/getaiscan-app/data-model/getaiscan-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getaiscan-app-data-model.yml
- group: operate
  href: https://artifacts.apis.io/getaiscan-app/rate-limits/getaiscan-app-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getaiscan-app-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/getaiscan-app/plans/getaiscan-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getaiscan-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/getaiscan-app/conformance/getaiscan-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getaiscan-app-conformance.yml
- group: design
  href: https://artifacts.apis.io/getaiscan-app/lifecycle/getaiscan-app-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getaiscan-app-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/getaiscan-app/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/getaiscan-app/security/getaiscan-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getaiscan-app-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/getaiscan-app/agentic-access/getaiscan-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getaiscan-app-agentic-access.yml
- group: build
  href: https://artifacts.apis.io/getaiscan-app/packages/getaiscan-app-packages.yml
  title: ''
  type: Packages
  url: packages/getaiscan-app-packages.yml
created: '2026-09-19'
description: AIScan is an AI-visibility auditing service at getaiscan.app that scans any website in about 60 seconds and returns four 0-100 scores — AEO (AI search visibility), GEO (citation readiness), Agent Readiness and MCP Readiness — from 80+ checks, plus a Brand Visibility measurement of how often AI assistants actually name a brand across 30 realistic niche prompts. Humans buy a full report on the site for 60 USDC; software agents buy 19 individual capabilities pay-per-call (0.06-3.50 USDC) through the x402 protocol on Base (eip155:8453) with no API key and no account, via a 20-operation OpenAPI 3.1.0 REST contract served from api.getaiscan.app, an A2A 0.3.0 agent card with 18 skills at /.well-known/agent-card.json, an ai-plugin.json manifest and an MCP discovery descriptor at /.well-known/mcp.json. Every paid route answers an unpaid call with a real HTTP 402 x402 V2 challenge; the capability catalog at GET /api/agent/index is free.
image: https://getaiscan.app/og-image.jpg
layout: provider
modified: '2026-10-06'
name: AIScan
nav: Providers
network: true
overview: 'AIScan publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agent API, AI Visibility API, and 1 more. Tagged areas include AI Visibility, Website Auditing, SEO, Answer Engine Optimization, and Generative Engine Optimization.


  The AIScan catalog on APIs.io includes 1 Spectral governance ruleset.


  AIScan''s developer surface includes engineering blog, documentation, API reference, pricing, authentication, and 17 more developer resources.'
plans:
- name: Getaiscan App Plans Pricing
  plan_count: 20
  slug: getaiscan-app-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 0
  name: Getaiscan App Rate Limits
  slug: getaiscan-app-rate-limits
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: AIScan API Rules
  rule_count: 49
  severity_counts:
    error: 40
    hint: 0
    info: 1
    warn: 8
  slug: getaiscan-app-rules
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 26
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.1
  facets:
    access_clarity: 36.8
    contract_governance: 31.8
    contract_quality: 51.2
    developer_ergonomics: 24.4
    discoverability: 78.6
    operational_transparency: 0.0
  previous_composite: 38.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 50.0
      total: 2
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
screenshot: https://apis.io/screenshots/getaiscan-app/getaiscan-app-2026-10-11T104848.png
security:
- kind: authentication
  name: Getaiscan App Authentication
  slug: getaiscan-app-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Getaiscan App Domain Security
  slug: getaiscan-app-domain-security
  summary_line: TLSv1.3
skill_count: 3
skills:
- name: getaiscan-app-audit-and-fix-site
  slug: getaiscan-app-audit-and-fix-site
- name: getaiscan-app-compare-competitors
  slug: getaiscan-app-compare-competitors
- name: getaiscan-app-measure-brand-visibility
  slug: getaiscan-app-measure-brand-visibility
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
