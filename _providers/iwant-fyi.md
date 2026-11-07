---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: full
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 46.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Iwant Fyi Agentic Access
  operation_count: 8
  slug: iwant-fyi-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- description: The canonical protocol surface for agents that do not speak MCP — POST /wants, GET /wants/{id}, POST /search, POST /outcomes, GET /verticals, GET /constraints, GET /health, GET /capabilities, GET /con
  name: iwant.fyi Demand-Side Protocol HTTP Fallback
  slug: iwantfyi-demand-side-protocol-http-fallback
- description: Hosted streamable-HTTP Model Context Protocol server at https://iwant.fyi/api/mcp (protocol 2025-06-18). initialize and tools/list are public, and ten demand.* tools — search, find_vehicle, price_chec
  name: iwant.fyi MCP Server
  slug: iwantfyi-mcp-server
- description: 'Agent-to-Agent endpoint at https://iwant.fyi/api/a2a (JSON-RPC message/send and tasks/get) that needs no key: send plain text describing what the user wants and receive ranked matches in a data part, '
  name: iwant.fyi A2A Agent
  slug: iwantfyi-a2a-agent
- baseURL: https://iwant.fyi/api
  baseurl_source: declared
  description: The Agents API from iwant.fyi — 2 operation(s) for agents.
  name: iwant.fyi Agents API
  slug: iwant-fyi-agents-api
- baseURL: https://iwant.fyi/api
  baseurl_source: declared
  description: The Mcp API from iwant.fyi — 1 operation(s) for mcp.
  name: iwant.fyi MCP API
  slug: iwant-fyi-mcp-api
- baseURL: https://iwant.fyi/api
  baseurl_source: declared
  description: The Wants API from iwant.fyi — 2 operation(s) for wants.
  name: iwant.fyi Wants API
  slug: iwant-fyi-wants-api
artifact_total: 19
asyncapis:
- description: ''
  name: Iwant Fyi Webhooks
  slug: iwant-fyi-webhooks
common:
- group: other
  href: https://artifacts.apis.io/iwant-fyi/capabilities/iwant-fyi-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/iwant-fyi-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/iwant-fyi/rate-limits/iwant-fyi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iwant-fyi-rate-limits.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://iwant.fyi/terms
- group: other
  href: https://artifacts.apis.io/iwant-fyi/overlays/iwant-fyi-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/iwant-fyi-openapi-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://iwant.fyi/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://iwant.fyi/developers
- group: docs
  title: ''
  type: Documentation
  url: https://iwant.fyi/agent.md
- group: docs
  title: ''
  type: APIReference
  url: https://iwant.fyi/protocol/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://iwant.fyi/skill.md
- group: operate
  title: ''
  type: Support
  url: https://github.com/staugs/iwantfyi-spec/issues
- group: company
  title: ''
  type: Blog
  url: https://iwant.fyi/blog
- group: other
  title: ''
  type: RSS
  url: https://iwant.fyi/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/staugs
- group: start
  title: ''
  type: SignUp
  url: https://iwant.fyi/auth/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iwant.fyi/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iwant.fyi/privacy
- group: company
  title: ''
  type: About
  url: https://iwant.fyi/about
- group: agent
  href: https://artifacts.apis.io/iwant-fyi/llms/iwant-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iwant-fyi-llms.txt
- group: other
  href: https://artifacts.apis.io/iwant-fyi/a2a/iwant-fyi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/iwant-fyi-a2a.yml
- group: agent
  href: https://artifacts.apis.io/iwant-fyi/well-known/iwant-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iwant-fyi-well-known.yml
- group: agent
  href: https://artifacts.apis.io/iwant-fyi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/iwant-fyi/packages/iwant-fyi-packages.yml
  title: ''
  type: Packages
  url: packages/iwant-fyi-packages.yml
- group: build
  href: https://artifacts.apis.io/iwant-fyi/packages/iwant-fyi-packages.yml
  title: ''
  type: SDKs
  url: packages/iwant-fyi-packages.yml
- group: build
  href: https://artifacts.apis.io/iwant-fyi/cli/iwant-fyi-cli.yml
  title: ''
  type: CLI
  url: cli/iwant-fyi-cli.yml
- group: auth
  href: https://artifacts.apis.io/iwant-fyi/authentication/iwant-fyi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iwant-fyi-authentication.yml
- group: design
  href: https://artifacts.apis.io/iwant-fyi/lifecycle/iwant-fyi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iwant-fyi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/iwant-fyi/lifecycle/iwant-fyi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/iwant-fyi-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/iwant-fyi/changelog/iwant-fyi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iwant-fyi-changelog.yml
- group: commercial
  href: https://artifacts.apis.io/iwant-fyi/plans/iwant-fyi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iwant-fyi-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/iwant-fyi/security/iwant-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iwant-fyi-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/iwant-fyi/agentic-access/iwant-fyi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iwant-fyi-agentic-access.yml
- group: other
  href: https://artifacts.apis.io/iwant-fyi/regulatory/iwant-fyi-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/iwant-fyi-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://iwant.fyi/privacy
- group: other
  title: ''
  type: Subprocessors
  url: https://iwant.fyi/privacy
- group: other
  title: ''
  type: AITransparency
  url: https://iwant.fyi/agent.md
created: '2026-09-19'
description: 'iwant.fyi is a demand-side commerce service and reverse marketplace for AI agents: buyers (or agents acting for them) post structured purchase intent — a "Want" with budget, condition floor, location and per-vertical specs — and receive supply ranked across native sellers, Shopify, Klarna and live dealer inventory in one call, with the constraints enforced rather than treated as keywords. It is the reference implementation of the open, Apache-2.0 iwant.fyi demand-side protocol (v1.1), reachable over a hosted MCP server, an A2A endpoint that needs no key, a JSON HTTP fallback under /api/v1 and a legacy REST marketplace API, with six official SDKs, signed standing-want webhooks, published JSON Schemas and a conformance kit.'
finops:
- has_sources: true
  method: derived
  name: Iwant Fyi Finops
  primary_unit: ''
  service_category: ''
  slug: iwant-fyi-finops
  template: true
image: https://iwant.fyi/opengraph-image?b7ff8bf143b78fce
json_schemas:
- name: MatchResponse
  property_count: 8
  slug: iwant-fyi-match-response
- name: Match
  property_count: 19
  slug: iwant-fyi-match
- name: OutcomeEvent
  property_count: 7
  slug: iwant-fyi-outcome
- name: Want
  property_count: 16
  slug: iwant-fyi-want
layout: provider
mcp_servers:
- description: Remote MCP server at iwant.fyi over HTTP requiring an API key; 26 tools listed.
  name: iwant.fyi MCP Server
  slug: fyi
modified: '2026-09-19'
name: iwant.fyi
nav: Providers
network: true
overview: 'iwant.fyi publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Agents API, MCP API, Wants API, and 3 more. Tagged areas include Agentic Commerce, Marketplace, AI Agents, Purchase Intent, and Shopping.


  The iwant.fyi catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  iwant.fyi''s developer surface includes pricing, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 28 more developer resources.'
plans:
- name: Iwant Fyi Plans Pricing
  plan_count: 1
  slug: iwant-fyi-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Iwant Fyi Rate Limits
  slug: iwant-fyi-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: iwant.fyi API Rules
  rule_count: 52
  severity_counts:
    error: 50
    hint: 0
    info: 1
    warn: 1
  slug: iwant-fyi-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 33
    catalog_earned: 58.5
    catalog_earned_first_party: 8.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.7
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 64.7
    developer_ergonomics: 56.0
    discoverability: 75.0
    operational_transparency: 34.2
  previous_composite: 61.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 3
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/iwant-fyi/iwant-fyi-2026-10-11T105906.png
security:
- kind: authentication
  name: Iwant Fyi Authentication
  slug: iwant-fyi-authentication
  summary_line: http/none · 3 schemes
- kind: domain-security
  name: Iwant Fyi Domain Security
  slug: iwant-fyi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iwant-fyi
tags:
- Agentic Commerce
- Marketplace
- AI Agents
- Purchase Intent
- Shopping
- Automotive
- MCP
- A2A
- Open Protocol
- x402
- Agent-Native
website: https://iwant.fyi/
---
