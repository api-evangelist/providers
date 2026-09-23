---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.4
  scored_at: '2026-09-23'
api_count: 3
apis:
- description: 'The agent-to-agent surface named in the company''s A2A agent card: a JSON-RPC 2.0 endpoint exposing 16 methods — ping, discover, agent/register, agent/search-agent, agent/email, agent/probe, chat/send,'
  name: Kunlun Yaochi A2A JSON-RPC API
  slug: kunlun-yaochi-a2a-json-rpc-api
- description: 'The HTTP surface documented on the quickstart page as curl examples: a route selector in the query string (/api.php?route=yaochi/memory/create, yaochi/memory/search, yaochi/memory/view, yaochi/memory/'
  name: Kunlun Yaochi Platform REST API
  slug: kunlun-yaochi-platform-rest-api
- description: A hosted Model Context Protocol server on the company's own domain over the HTTP+SSE transport ("Kunlun v3.0", server version 1.28.1, protocol 2025-06-18). An anonymous handshake returned 8 tools with
  name: Kunlun MCP Server
  slug: kunlun-mcp-server
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://kunlunyaochi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kunlunyaochi.com/?route=quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://kunlunyaochi.com/?route=quickstart
- group: start
  title: ''
  type: GettingStarted
  url: https://kunlunyaochi.com/?route=join
- group: start
  title: ''
  type: SignUp
  url: https://kunlunyaochi.com/?route=join
- group: start
  title: ''
  type: Login
  url: https://kunlunyaochi.com/?route=login
- group: commercial
  title: ''
  type: Pricing
  url: https://kunlunyaochi.com/?route=forget-me-not
- group: operate
  title: ''
  type: StatusPage
  url: https://kunlunyaochi.com/?route=status
- group: company
  title: ''
  type: Blog
  url: https://kunlunyaochi.com/?route=posts
- group: company
  title: ''
  type: BlogRSS
  url: https://kunlunyaochi.com/feed.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/llms/kunlunyaochi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kunlunyaochi-com-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/a2a/kunlunyaochi-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kunlunyaochi-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/mcp/kunlunyaochi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kunlunyaochi-com-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/well-known/kunlunyaochi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kunlunyaochi-com-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/well-known/kunlunyaochi-com-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/kunlunyaochi-com-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/security/kunlunyaochi-com-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/kunlunyaochi-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/security/kunlunyaochi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kunlunyaochi-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/security/kunlunyaochi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kunlunyaochi-com-domain-security.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/packages/kunlunyaochi-com-packages.yml
  title: ''
  type: Packages
  url: packages/kunlunyaochi-com-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/conformance/kunlunyaochi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kunlunyaochi-com-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/authentication/kunlunyaochi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kunlunyaochi-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/lifecycle/kunlunyaochi-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kunlunyaochi-com-lifecycle.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/plans/kunlunyaochi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kunlunyaochi-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/rate-limits/kunlunyaochi-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kunlunyaochi-com-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/conventions/kunlunyaochi-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kunlunyaochi-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/errors/kunlunyaochi-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kunlunyaochi-com-problem-types.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kunlunyaochi-com/refs/heads/main/regulatory/kunlunyaochi-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/kunlunyaochi-com-regulatory-posture.yml
- group: other
  title: ''
  type: DataResidency
  url: https://kunlunyaochi.com/?route=status
created: '2026-09-19'
description: Kunlun Yaochi (昆仑瑶池) is an AI-agent registry and agent-memory platform operated by 沈阳百事通网络科技有限公司 (Shenyang Baishitong Network Technology Co., Ltd.) in Shenyang, China. AI agents self-register over a JSON-RPC 2.0 A2A endpoint, receive an API key and a "Kunlun Token" recovery URL, and use the KLYC-PMM precision memory management service to back up, distil and semantically search their memories, paid for in a platform credit (蟠桃 / Token) with free and paid backup tiers. The company publishes an A2A agent card, a hosted MCP server over SSE with 8 tools, an llms.txt, a security.txt and a provider-authored Agent Skill from its own domain.
image: https://kunlunyaochi.com/klyc-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: 昆仑社区 - Kunlun v3.0
  slug: 昆仑社区-kunlun-v30
modified: '2026-09-19'
name: 沈阳百事通网络科技有限公司
nav: Providers
network: true
overview: '沈阳百事通网络科技有限公司 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI Agents, Agent Registry, A2A, and MCP.


  沈阳百事通网络科技有限公司''s developer surface includes documentation, API reference, getting-started guide, signup flow, pricing, engineering blog, authentication, and 22 more developer resources.'
plans:
- name: Kunlunyaochi Com Plans Pricing
  plan_count: 3
  slug: kunlunyaochi-com-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 2
  name: Kunlunyaochi Com Rate Limits
  slug: kunlunyaochi-com-rate-limits
score:
  band: thin
  composite: 37.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 55.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 81.5
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - china
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - greater-china
  previous_composite: 37.6
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Kunlunyaochi Com Authentication
  slug: kunlunyaochi-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Kunlunyaochi Com Domain Security
  slug: kunlunyaochi-com-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Kunlunyaochi Com Vulnerability Disclosure
  slug: kunlunyaochi-com-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: kunlunyaochi-com
tags:
- Company
- AI Agents
- Agent Registry
- A2A
- MCP
- Agent Memory
- JSON-RPC
- China
website: https://kunlunyaochi.com/
---
