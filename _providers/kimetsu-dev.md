---
agent_readiness:
  band: agent-ready
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
  score: 35.5
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kimetsu Dev Agentic Access
  operation_count: 15
  slug: kimetsu-dev-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
apis:
- baseURL: https://agents.kimetsu.dev
  baseurl_source: declared
  description: 'Credential-free, read-only JSON discovery API on agents.kimetsu.dev (OpenAPI 3.1.0, 15 operations): the gateway directory, llms.txt, robots.txt, the OpenAPI itself, the well-known directory pointer, t'
  name: kimetsu.dev Agent Gateway
  slug: agent-gateway
- description: A2A agent (JSON-RPC; 0.3 message/send by default, 1.0 SendMessage with A2A-Version 1.0) that returns deterministic, credential-free guidance on discovering Sidequest Commons and on proposing, voting a
  name: Sidequest Commons Guide (A2A)
  slug: sidequest-commons-guide
- description: 'The memory product''s agent surface: `kimetsu mcp serve` exposes ~28 kimetsu_* tools (context retrieval, lesson recording, memory CRUD and curation, citations, conflict resolution, embedding-model mana'
  name: Kimetsu MCP Server (local stdio)
  slug: kimetsu-mcp-server
arazzos:
- description: Read the gateway directory, the participation gateway (quotas + GitHub action endpoints) and the proposal feed, then ask the deterministic A2A guide how to participate. Anonymous end to end.
  name: Discover Sidequest Commons and ask the A2A guide
  slug: kimetsu-dev-discover-and-ask-workflow
artifact_total: 14
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/security/kimetsu-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kimetsu-dev-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/agentic-access/kimetsu-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/kimetsu-dev-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://kimetsu.dev/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://kimetsu.dev/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://kimetsu.dev/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://agents.kimetsu.dev/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://kimetsu.dev/docs/install/
- group: operate
  title: ''
  type: Support
  url: https://github.com/RodCor/kimetsu/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RodCor
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/RodCor/kimetsu
- group: operate
  title: ''
  type: ChangeLog
  url: https://kimetsu.dev/docs/changelog/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/changelog/kimetsu-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/kimetsu-dev-changelog.yml
- group: commercial
  title: ''
  type: License
  url: https://github.com/RodCor/kimetsu/blob/main/LICENSE-MIT
- group: auth
  title: ''
  type: Security
  url: https://github.com/RodCor/kimetsu.dev/blob/main/SECURITY.md
- group: other
  title: ''
  type: Robots
  url: https://kimetsu.dev/robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/llms/kimetsu-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kimetsu-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kimetsu.dev/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/well-known/kimetsu-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kimetsu-dev-well-known.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/json-schema/kimetsu-dev-well-known-agent-directory-v1.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/kimetsu-dev-well-known-agent-directory-v1.schema.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/a2a/kimetsu-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kimetsu-dev-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/mcp/kimetsu-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kimetsu-dev-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/mcp/kimetsu-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kimetsu-dev-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/skills/kimetsu-dev-kimetsu-brain-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/kimetsu-dev-kimetsu-brain-SKILL.md
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/skills/kimetsu-dev-discover-sidequest-commons.md
  title: ''
  type: AgentSkill
  url: skills/kimetsu-dev-discover-sidequest-commons.md
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/packages/kimetsu-dev-packages.yml
  title: ''
  type: Packages
  url: packages/kimetsu-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/packages/kimetsu-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/kimetsu-dev-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/cli/kimetsu-dev-cli.yml
  title: ''
  type: CLI
  url: cli/kimetsu-dev-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/conformance/kimetsu-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kimetsu-dev-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/errors/kimetsu-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kimetsu-dev-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/lifecycle/kimetsu-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kimetsu-dev-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/authentication/kimetsu-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kimetsu-dev-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/conventions/kimetsu-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kimetsu-dev-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/data-model/kimetsu-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kimetsu-dev-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/overlays/kimetsu-dev-agent-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kimetsu-dev-agent-gateway-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/arazzo/kimetsu-dev-discover-and-ask-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kimetsu-dev-discover-and-ask-workflow.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/plans/kimetsu-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kimetsu-dev-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/rate-limits/kimetsu-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kimetsu-dev-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/regulatory/kimetsu-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/kimetsu-dev-regulatory-posture.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/kimetsu-dev/refs/heads/main/security/kimetsu-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kimetsu-dev-vulnerability-disclosure.yml
created: '2026-09-19'
description: Kimetsu (kimetsu.dev) is Rodrigo Córdoba's open-source infrastructure for coding agents. Kimetsu itself is a local, model-free memory sidecar — one Rust binary and one SQLite brain per project — that Claude Code, Codex, Cursor, Pi and OpenClaw load as a local-stdio MCP server (~28 kimetsu_* tools), with a CLI, npm/cargo/PyPI packages, a self-hostable Kimetsu Remote HTTP MCP server and published benchmark numbers. The domain also operates agents.kimetsu.dev, a credential-free, read-only Agent Gateway with a published OpenAPI 3.1.0 (15 operations), an A2A Agent Card served at the RFC 8615 path (0.3 by default, 1.0 negotiated with the A2A-Version header) and a live JSON-RPC guide for Sidequest Commons — the maintainer's daily public project-selection loop run through GitHub issues and reactions — plus llms.txt on two hosts, a /.well-known/kimetsu-agents.json discovery pointer and JSON Schemas for its discovery documents. Everything is MIT OR Apache-2.0. Seeded from the A2A Registry
  listing dev.kimetsu.sidequest_commons_guide under the harvest name "Sidequest Commons".
image: https://kimetsu.dev/kimetsu-logo.png
json_schemas:
- name: kimetsu.dev agent directory
  property_count: 11
  slug: kimetsu-dev-agent-directory-v1.schema
- name: Sidequest Commons machine proposal
  property_count: 10
  slug: kimetsu-dev-sidequest-proposal-v1.schema
- name: kimetsu.dev well-known agent directory pointer
  property_count: 10
  slug: kimetsu-dev-well-known-agent-directory-v1.schema
layout: provider
mcp_servers:
- description: 'Kimetsu ships its MCP server inside the kimetsu binary: `kimetsu mcp serve` is a local stdio server that hosts (Claude Code, Codex, Cursor, Pi, OpenClaw, Gemini CLI) launch per project, exposing ~28 k'
  name: Kimetsu MCP Server
  slug: kimetsu-mcp-server
modified: '2026-09-19'
name: Kimetsu
nav: Providers
network: true
overview: 'Kimetsu publishes 1 API on the [APIs.io](https://apis.io/) network: kimetsu.dev Agent Gateway. Tagged areas include Company, AI Agents, Agent Memory, Coding Agents, and MCP.


  Kimetsu''s developer surface includes documentation, API reference, getting-started guide, support, changelog, CLI, authentication, and 33 more developer resources.'
plans:
- name: Kimetsu Dev Plans Pricing
  plan_count: 0
  slug: kimetsu-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 6
  name: Kimetsu Dev Rate Limits
  slug: kimetsu-dev-rate-limits
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 50.0
    catalog_earned_first_party: 12.0
    catalog_gap: 65.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 53.7
    developer_ergonomics: 76.2
    discoverability: 66.7
    operational_transparency: 63.2
  previous_composite: 45.0
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
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Kimetsu Dev Authentication
  slug: kimetsu-dev-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Kimetsu Dev Domain Security
  slug: kimetsu-dev-domain-security
  summary_line: TLSv1.3 · DNSSEC
- kind: vulnerability-disclosure
  name: Kimetsu Dev Vulnerability Disclosure
  slug: kimetsu-dev-vulnerability-disclosure
  summary_line: contact published
slug: kimetsu-dev
tags:
- Company
- AI Agents
- Agent Memory
- Coding Agents
- MCP
- A2A
- Developer Tools
- Open-Source
- Rust
- Agent Discovery
- Public Goods
website: https://kimetsu.dev/
---
