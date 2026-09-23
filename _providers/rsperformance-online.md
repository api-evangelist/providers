---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: derived
    agentic_access: true
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.2
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Rsperformance Online Agentic Access
  operation_count: 3
  slug: rsperformance-online-agentic-access
  summary_line: 3 operations
api_count: 2
apis:
- baseURL: https://ai.rsperformance.online
  baseurl_source: declared
  description: 'Three-operation REST gateway on ai.rsperformance.online (OpenAPI 3.1.0, info.version 1.3.0): POST /api/search runs answer-first semantic retrieval over services, symptom pages, DTC references, repair '
  name: RS Performance AI Gateway API
  slug: rs-performance-ai-gateway-api
- description: Public A2A agent for automotive intents — OBD DTC lookup, vehicle diagnostics, repair services, EV/hybrid and climate/HVAC knowledge, a 19-service catalog, ten Gdańsk district routes, booking and gate
  name: RS Performance A2A Agent
  slug: rs-performance-a2a-agent
- description: Remote Model Context Protocol server (FastMCP, protocol 2025-06-18, Streamable HTTP with a session header, legacy SSE at /mcp) at https://mcp.rs3d.pl/ — a host the provider's own /.well-known/mcp.json
  name: Diagnosta RS MCP Server
  slug: diagnosta-rs-mcp-server
artifact_total: 11
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/security/rsperformance-online-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/rsperformance-online-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/security/rsperformance-online-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rsperformance-online-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/agentic-access/rsperformance-online-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rsperformance-online-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://rsperformance.online/
- group: docs
  title: ''
  type: Documentation
  url: https://rsperformance.online/llms-full.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://ai.rsperformance.online/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://ai.rsperformance.online/.well-known/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://rsperformance.online/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://rsperformance.online/feed.xml
- group: operate
  title: ''
  type: Support
  url: https://rsperformance.online/#kontakt
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rsperformance.online/polityka-prywatnosci
- group: company
  title: ''
  type: About
  url: https://rsperformance.online/o-nas
- group: operate
  title: ''
  type: FAQ
  url: https://rsperformance.online/faq
- group: other
  title: ''
  type: Sitemap
  url: https://rsperformance.online/sitemap.xml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/llms/rsperformance-online-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rsperformance-online-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://rsperformance.online/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/a2a/rsperformance-online-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/rsperformance-online-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/mcp/rsperformance-online-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rsperformance-online-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/mcp/rsperformance-online-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/rsperformance-online-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/well-known/rsperformance-online-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/rsperformance-online-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/well-known/rsperformance-online-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/rsperformance-online-security.txt
- group: auth
  title: ''
  type: Security
  url: https://rsperformance.online/.well-known/security.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/well-known/rsperformance-online-ai-plugin.json
  title: ''
  type: AIPlugin
  url: well-known/rsperformance-online-ai-plugin.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/conformance/rsperformance-online-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rsperformance-online-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/errors/rsperformance-online-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rsperformance-online-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/lifecycle/rsperformance-online-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/rsperformance-online-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/authentication/rsperformance-online-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rsperformance-online-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/conventions/rsperformance-online-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rsperformance-online-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/overlays/rsperformance-online-ai-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/rsperformance-online-ai-gateway-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/plans/rsperformance-online-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rsperformance-online-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/rate-limits/rsperformance-online-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rsperformance-online-rate-limits.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/changelog/rsperformance-online-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/rsperformance-online-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://rsperformance.online/feeds/changes.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/packages/rsperformance-online-packages.yml
  title: ''
  type: Packages
  url: packages/rsperformance-online-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/rsperformance-online/refs/heads/main/regulatory/rsperformance-online-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/rsperformance-online-regulatory-posture.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://rsperformance.online/polityka-prywatnosci
- group: other
  title: ''
  type: Subprocessors
  url: https://rsperformance.online/polityka-prywatnosci
- group: other
  title: ''
  type: DataResidency
  url: https://rsperformance.online/polityka-prywatnosci
- group: other
  title: ''
  type: AITransparency
  url: https://rsperformance.online/
created: '2026-09-19'
description: 'RS Performance Sp. z o.o. is a single-location automotive diagnostics and repair workshop at Al. Grunwaldzka 303B in Gdańsk, Poland (the Premio Ring site, rebranded 2021-09-14), serving Gdańsk, Sopot, Gdynia and the Tricity with 19 workshop services from computer diagnostics, DPF/AdBlue, turbo and gearbox work to tyre storage and B2B fleet service. What makes it an API provider is the machine-readable layer it has built over its knowledge base: an anonymous A2A agent (nine skills, JSON-RPC 2.0 and HTTP+JSON on rsperformance.online, agent card at the canonical well-known path), a remote FastMCP server "Diagnosta RS" with 14 tools over a Qdrant vector store of services, FAQ, repair reports and 12,000+ OBD-II fault codes, and a three-operation OpenAPI 3.1 "AI Gateway" on ai.rsperformance.online for answer-first semantic search, freshness and answer routing — plus llms.txt, security.txt, an ai-plugin manifest, JSON/Atom change feeds and a DTC JSON feed. Every surface is free and
  unauthenticated under a fair-use, attribution-required policy.'
image: https://rsperformance.online/images/rs_logo_new.png
layout: provider
mcp_servers:
- description: ''
  name: RS Performance MCP Server
  slug: rs-performance-mcp-server
- description: ''
  name: Diagnosta RS (remote, live)
  slug: diagnosta-rs-remote-live
modified: '2026-09-19'
name: RS Performance
nav: Providers
network: true
overview: 'RS Performance publishes 1 API on the [APIs.io](https://apis.io/) network: AI Gateway API. Tagged areas include Automotive, Auto Repair, Vehicle Diagnostics, OBD-II, and Fault Codes.


  RS Performance''s developer surface includes documentation, getting-started guide, API reference, engineering blog, support, FAQ, authentication, and 33 more developer resources.'
plans:
- name: Rsperformance Online Plans Pricing
  plan_count: 0
  slug: rsperformance-online-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 2
  name: Rsperformance Online Rate Limits
  slug: rsperformance-online-rate-limits
score:
  band: developing
  composite: 39.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 49.4
    discoverability: 75.9
    operational_transparency: 47.4
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  previous_composite: 39.6
  provenance:
    agentic_access: first-party
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Rsperformance Online Authentication
  slug: rsperformance-online-authentication
  summary_line: none · 1 scheme
- kind: domain-security
  name: Rsperformance Online Domain Security
  slug: rsperformance-online-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Rsperformance Online Vulnerability Disclosure
  slug: rsperformance-online-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: rsperformance-online
tags:
- Automotive
- Auto Repair
- Vehicle Diagnostics
- OBD-II
- Fault Codes
- Knowledge Base
- Semantic Search
- A2A
- MCP
- Agent-Native
- Local Business
- Poland
website: https://rsperformance.online/
---
