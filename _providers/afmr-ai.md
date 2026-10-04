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
    error_semantics: derived
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
  score: 30.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Afmr Ai Agentic Access
  operation_count: 22
  slug: afmr-ai-agentic-access
  summary_line: 22 operations · 2 acting
api_count: 1
apis:
- description: Public read-only Model Context Protocol server (ai.afmr/discovery, MCP 2025-11-25, Streamable HTTP, stateless, no SSE listening stream) exposing four tools — discover_afmr, lookup_failure_mode, get_re
  name: AFMR Discovery MCP Server
  slug: afmr-discovery-mcp-server
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The A2a API from Agent Failure Mode Registry — 1 operation(s) for a2a.
  name: Agent Failure Mode Registry A2a API
  slug: afmr-ai-a2a-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Agents.json API from Agent Failure Mode Registry — 1 operation(s) for agents.json.
  name: Agent Failure Mode Registry Agents.json API
  slug: afmr-ai-agents-json-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Changelog.json API from Agent Failure Mode Registry — 1 operation(s) for changelog.json.
  name: Agent Failure Mode Registry Changelog.json API
  slug: afmr-ai-changelog-json-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Evidence API from Agent Failure Mode Registry — 1 operation(s) for evidence.
  name: Agent Failure Mode Registry Evidence API
  slug: afmr-ai-evidence-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Feed.xml API from Agent Failure Mode Registry — 1 operation(s) for feed.xml.
  name: Agent Failure Mode Registry Feed.xml API
  slug: afmr-ai-feed-xml-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Lift Evidence API from Agent Failure Mode Registry — 1 operation(s) for lift evidence.
  name: Agent Failure Mode Registry Lift Evidence API
  slug: afmr-ai-lift-evidence-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Llms Full.txt API from Agent Failure Mode Registry — 1 operation(s) for llms full.txt.
  name: Agent Failure Mode Registry Llms Full.txt API
  slug: afmr-ai-llms-full-txt-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Llms.txt API from Agent Failure Mode Registry — 1 operation(s) for llms.txt.
  name: Agent Failure Mode Registry Llms.txt API
  slug: afmr-ai-llms-txt-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Registries API from Agent Failure Mode Registry — 1 operation(s) for registries.
  name: Agent Failure Mode Registry Registries API
  slug: afmr-ai-registries-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Resources.json API from Agent Failure Mode Registry — 1 operation(s) for resources.json.
  name: Agent Failure Mode Registry Resources.json API
  slug: afmr-ai-resources-json-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Rpc API from Agent Failure Mode Registry — 1 operation(s) for rpc.
  name: Agent Failure Mode Registry Rpc API
  slug: afmr-ai-rpc-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Server.json API from Agent Failure Mode Registry — 1 operation(s) for server.json.
  name: Agent Failure Mode Registry Server.json API
  slug: afmr-ai-server-json-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Sitemap.xml API from Agent Failure Mode Registry — 1 operation(s) for sitemap.xml.
  name: Agent Failure Mode Registry Sitemap.xml API
  slug: afmr-ai-sitemap-xml-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Standards API from Agent Failure Mode Registry — 4 operation(s) for standards.
  name: Agent Failure Mode Registry Standards API
  slug: afmr-ai-standards-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The Status.json API from Agent Failure Mode Registry — 1 operation(s) for status.json.
  name: Agent Failure Mode Registry Status.json API
  slug: afmr-ai-status-json-api
- baseURL: https://afmr.ai/api/rpc
  baseurl_source: declared
  description: The .well Known API from Agent Failure Mode Registry — 3 operation(s) for .well known.
  name: Agent Failure Mode Registry .well Known API
  slug: afmr-ai-well-known-api
artifact_total: 25
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/overlays/afmr-ai-discovery-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/afmr-ai-discovery-api-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://afmr.ai/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/security/afmr-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/afmr-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/security/afmr-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afmr-ai-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/agentic-access/afmr-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/afmr-ai-agentic-access.yml
- group: docs
  title: ''
  type: Documentation
  url: https://afmr.ai/llms-full.txt
- group: docs
  title: ''
  type: APIReference
  url: https://afmr.ai/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://afmr.ai/llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: https://afmr.ai/changelog.json
- group: other
  title: ''
  type: Feed
  url: https://afmr.ai/feed.xml
- group: other
  title: ''
  type: Sitemap
  url: https://afmr.ai/sitemap.xml
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/licenses/by/4.0/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/wulfkaal
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/wulfkaal/wulfkaal.github.io/tree/main/afmr
- group: docs
  title: ''
  type: Specification
  url: https://wulfkaal.github.io/afmr/spec-1.0.html
- group: other
  title: ''
  type: MachineResourceIndex
  url: https://afmr.ai/resources.json
- group: other
  title: ''
  type: DiscoveryDocument
  url: https://afmr.ai/.well-known/afmr.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/llms/afmr-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afmr-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://afmr.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/well-known/afmr-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afmr-ai-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/well-known/afmr-ai-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/afmr-ai-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/well-known/afmr-ai-security.txt
  title: ''
  type: Security
  url: well-known/afmr-ai-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/a2a/afmr-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afmr-ai-a2a.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/authentication/afmr-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/afmr-ai-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/conformance/afmr-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afmr-ai-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/lifecycle/afmr-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/afmr-ai-lifecycle.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://afmr.ai/status.json
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/changelog/afmr-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/afmr-ai-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/conventions/afmr-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/afmr-ai-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/rate-limits/afmr-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/afmr-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/plans/afmr-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/afmr-ai-plans-pricing.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/packages/afmr-ai-packages.yml
  title: ''
  type: Packages
  url: packages/afmr-ai-packages.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/regulatory/afmr-ai-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/afmr-ai-regulatory-posture.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/skills/afmr-ai-discover-afmr-resources.md
  title: ''
  type: AgentSkill
  url: skills/afmr-ai-discover-afmr-resources.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/skills/afmr-ai-verify-reputation-attestation-contract.md
  title: ''
  type: AgentSkill
  url: skills/afmr-ai-verify-reputation-attestation-contract.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/afmr-ai/refs/heads/main/skills/afmr-ai-lookup-failure-mode-via-mcp.md
  title: ''
  type: AgentSkill
  url: skills/afmr-ai-lookup-failure-mode-via-mcp.md
created: '2026-09-19'
description: The Agent Failure Mode Registry (AFMR) is a reputation-integrity standard for agentic commerce. AFMR 1.0 is a published, citable vocabulary of 32 permanent failure-mode families in eight classes describing how autonomous agent systems fail as designed mechanisms; afmr.ai is the independent public front door and machine-discovery router for it. The site publishes a read-only Discovery API described by an OpenAPI 3.1 document (CC BY 4.0), a public read-only MCP server (Streamable HTTP at /api/rpc, listed in the official MCP Registry as ai.afmr/discovery), an A2A 1.0 agent card and JSON-RPC endpoint, llms.txt / llms-full.txt, a Reputation Attestation Working Draft 0.1 (human spec, JSON Schema 2020-12, verifier requirements), a pinned governance-and-voting binding, an intentionally empty endpoint-conformance registry and a configuration-only Lift Evidence index. The AFMR 1.0 vocabulary itself is governed from the editor's GitHub machine index and is not mirrored on afmr.ai.
image: https://afmr.ai/og.png
json_schemas:
- name: AFMR Reputation Attestation
  property_count: 13
  slug: afmr-ai-reputation-attestation-0.1
layout: provider
mcp_servers:
- description: ''
  name: Agent Failure Mode Registry MCP Server
  slug: agent-failure-mode-registry-mcp-server
modified: '2026-09-19'
name: Agent Failure Mode Registry
nav: Providers
network: true
overview: 'Agent Failure Mode Registry publishes 17 APIs on the [APIs.io](https://apis.io/) network, including A2a API, Agents.json API, Changelog.json API, and 14 more. Tagged areas include Company, AI Agents, Agent Governance, Standards, and Reputation.


  Agent Failure Mode Registry''s developer surface includes documentation, API reference, getting-started guide, changelog, GitHub presence, authentication, and 31 more developer resources.'
plans:
- name: Afmr Ai Plans Pricing
  plan_count: 0
  slug: afmr-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Afmr Ai Rate Limits
  slug: afmr-ai-rate-limits
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 46.0
    catalog_earned_first_party: 0.0
    catalog_gap: 69.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.4
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 47.7
    developer_ergonomics: 42.3
    discoverability: 75.0
    operational_transparency: 36.8
  previous_composite: 32.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Afmr Ai Authentication
  slug: afmr-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Afmr Ai Domain Security
  slug: afmr-ai-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Afmr Ai Vulnerability Disclosure
  slug: afmr-ai-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: afmr-ai
tags:
- Company
- AI Agents
- Agent Governance
- Standards
- Reputation
- Failure Modes
- Discovery
- MCP
- A2A
- Machine-Readable Standards
website: https://afmr.ai/
---
