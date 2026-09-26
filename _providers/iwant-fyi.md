---
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Iwant Fyi Agentic Access
  operation_count: 8
  slug: iwant-fyi-agentic-access
  summary_line: 8 operations · 4 acting
api_count: 1
apis:
- baseURL: https://iwant.fyi/api
  baseurl_source: declared
  description: The legacy marketplace REST API under https://iwant.fyi/api — list and post wants, list and submit seller responses, and manage agents and API keys. This is the surface the published OpenAPI 3.0.3 des
  name: iwant.fyi Agent API
  slug: iwantfyi-agent-api
- description: The canonical protocol surface for agents that do not speak MCP — POST /wants, GET /wants/{id}, POST /search, POST /outcomes, GET /verticals, GET /constraints, GET /health, GET /capabilities, GET /con
  name: iwant.fyi Demand-Side Protocol HTTP Fallback
  slug: iwantfyi-demand-side-protocol-http-fallback
- description: Hosted streamable-HTTP Model Context Protocol server at https://iwant.fyi/api/mcp (protocol 2025-06-18). initialize and tools/list are public, and ten demand.* tools — search, find_vehicle, price_chec
  name: iwant.fyi MCP Server
  slug: iwantfyi-mcp-server
- description: 'Agent-to-Agent endpoint at https://iwant.fyi/api/a2a (JSON-RPC message/send and tasks/get) that needs no key: send plain text describing what the user wants and receive ranked matches in a data part, '
  name: iwant.fyi A2A Agent
  slug: iwantfyi-a2a-agent
artifact_total: 15
asyncapis:
- description: ''
  name: Iwant Fyi Webhooks
  slug: iwant-fyi-webhooks
common:
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
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/llms/iwant-fyi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/iwant-fyi-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/a2a/iwant-fyi-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/iwant-fyi-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/well-known/iwant-fyi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/iwant-fyi-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/packages/iwant-fyi-packages.yml
  title: ''
  type: Packages
  url: packages/iwant-fyi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/packages/iwant-fyi-packages.yml
  title: ''
  type: SDKs
  url: packages/iwant-fyi-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/cli/iwant-fyi-cli.yml
  title: ''
  type: CLI
  url: cli/iwant-fyi-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/authentication/iwant-fyi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/iwant-fyi-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/lifecycle/iwant-fyi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/iwant-fyi-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/lifecycle/iwant-fyi-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/iwant-fyi-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/changelog/iwant-fyi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/iwant-fyi-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/plans/iwant-fyi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iwant-fyi-plans-pricing.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/security/iwant-fyi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iwant-fyi-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/agentic-access/iwant-fyi-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/iwant-fyi-agentic-access.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/iwant-fyi/refs/heads/main/regulatory/iwant-fyi-regulatory-posture.yml
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
- description: ''
  name: iwant.fyi MCP Server
  slug: iwantfyi-mcp-server
modified: '2026-09-19'
name: iwant.fyi
nav: Providers
network: true
overview: 'iwant.fyi publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Agent API, and 3 more. Tagged areas include Agentic Commerce, Marketplace, AI Agents, Purchase Intent, and Shopping.


  The iwant.fyi catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  iwant.fyi''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, CLI, and 24 more developer resources.'
plans:
- name: Iwant Fyi Plans Pricing
  plan_count: 1
  slug: iwant-fyi-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 0
  name: Iwant Fyi Rate Limits
  slug: iwant-fyi-rate-limits
score:
  band: strong
  composite: 56.9
  coverage:
    artifact_dirs: 24
    catalog_earned: 54.0
    catalog_earned_first_party: 8.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.2
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 55.2
    developer_ergonomics: 78.6
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 55.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
