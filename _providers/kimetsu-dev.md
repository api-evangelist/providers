---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Kimetsu Dev Agentic Access
  operation_count: 15
  slug: kimetsu-dev-agentic-access
  summary_line: 15 operations · 1 acting
api_count: 1
apis:
- description: A2A agent (JSON-RPC; 0.3 message/send by default, 1.0 SendMessage with A2A-Version 1.0) that returns deterministic, credential-free guidance on discovering Sidequest Commons and on proposing, voting a
  name: Sidequest Commons Guide (A2A)
  slug: sidequest-commons-guide
- description: 'The memory product''s agent surface: `kimetsu mcp serve` exposes ~28 kimetsu_* tools (context retrieval, lesson recording, memory CRUD and curation, citations, conflict resolution, embedding-model mana'
  name: Kimetsu MCP Server (local stdio)
  slug: kimetsu-mcp-server
- baseURL: https://agents.kimetsu.dev
  baseurl_source: declared
  description: Deterministic guidance; no delegated actions or writes.
  name: Kimetsu A2A API
  slug: kimetsu-dev-a2a-api
- baseURL: https://agents.kimetsu.dev
  baseurl_source: declared
  description: Static, anonymous machine-discovery documents.
  name: Kimetsu Discovery API
  slug: kimetsu-dev-discovery-api
- baseURL: https://agents.kimetsu.dev
  baseurl_source: declared
  description: Read-only Sidequest Commons public data.
  name: Kimetsu Sidequest API
  slug: kimetsu-dev-sidequest-api
arazzos:
- description: Read the gateway directory, the participation gateway (quotas + GitHub action endpoints) and the proposal feed, then ask the deterministic A2A guide how to participate. Anonymous end to end.
  name: Discover Sidequest Commons and ask the A2A guide
  slug: kimetsu-dev-discover-and-ask-workflow
artifact_total: 20
common:
- group: auth
  href: https://artifacts.apis.io/kimetsu-dev/security/kimetsu-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/kimetsu-dev-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/agentic-access/kimetsu-dev-agentic-access.yml
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
  href: https://artifacts.apis.io/kimetsu-dev/changelog/kimetsu-dev-changelog.yml
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
  href: https://artifacts.apis.io/kimetsu-dev/llms/kimetsu-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/kimetsu-dev-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://kimetsu.dev/llms.txt
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/well-known/kimetsu-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/kimetsu-dev-well-known.yml
- group: docs
  href: https://artifacts.apis.io/kimetsu-dev/json-schema/kimetsu-dev-well-known-agent-directory-v1.schema.json
  title: ''
  type: JSONSchema
  url: json-schema/kimetsu-dev-well-known-agent-directory-v1.schema.json
- group: other
  href: https://artifacts.apis.io/kimetsu-dev/a2a/kimetsu-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/kimetsu-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/mcp/kimetsu-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/kimetsu-dev-mcp.yml
- group: build
  href: https://artifacts.apis.io/kimetsu-dev/mcp/kimetsu-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/kimetsu-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/skills/kimetsu-dev-kimetsu-brain-SKILL.md
  title: ''
  type: AgentSkill
  url: skills/kimetsu-dev-kimetsu-brain-SKILL.md
- group: agent
  href: https://artifacts.apis.io/kimetsu-dev/skills/kimetsu-dev-discover-sidequest-commons.md
  title: ''
  type: AgentSkill
  url: skills/kimetsu-dev-discover-sidequest-commons.md
- group: build
  href: https://artifacts.apis.io/kimetsu-dev/packages/kimetsu-dev-packages.yml
  title: ''
  type: Packages
  url: packages/kimetsu-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/kimetsu-dev/packages/kimetsu-dev-packages.yml
  title: ''
  type: SDKs
  url: packages/kimetsu-dev-packages.yml
- group: build
  href: https://artifacts.apis.io/kimetsu-dev/cli/kimetsu-dev-cli.yml
  title: ''
  type: CLI
  url: cli/kimetsu-dev-cli.yml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/conformance/kimetsu-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/kimetsu-dev-conformance.yml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/errors/kimetsu-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/kimetsu-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/lifecycle/kimetsu-dev-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/kimetsu-dev-lifecycle.yml
- group: auth
  href: https://artifacts.apis.io/kimetsu-dev/authentication/kimetsu-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/kimetsu-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/conventions/kimetsu-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/kimetsu-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/data-model/kimetsu-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/kimetsu-dev-data-model.yml
- group: other
  href: https://artifacts.apis.io/kimetsu-dev/overlays/kimetsu-dev-agent-gateway-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/kimetsu-dev-agent-gateway-overlay.yaml
- group: design
  href: https://artifacts.apis.io/kimetsu-dev/arazzo/kimetsu-dev-discover-and-ask-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/kimetsu-dev-discover-and-ask-workflow.yml
- group: commercial
  href: https://artifacts.apis.io/kimetsu-dev/plans/kimetsu-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/kimetsu-dev-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/kimetsu-dev/rate-limits/kimetsu-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/kimetsu-dev-rate-limits.yml
- group: other
  href: https://artifacts.apis.io/kimetsu-dev/regulatory/kimetsu-dev-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/kimetsu-dev-regulatory-posture.yml
- group: auth
  href: https://artifacts.apis.io/kimetsu-dev/security/kimetsu-dev-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/kimetsu-dev-vulnerability-disclosure.yml
created: '2026-09-19'
description: Kimetsu (kimetsu.dev) is Rodrigo Córdoba's open-source infrastructure for coding agents. Kimetsu itself is a local, model-free memory sidecar — one Rust binary and one SQLite brain per project — that Claude Code, Codex, Cursor, Pi and OpenClaw load as a local-stdio MCP server (~28 kimetsu_* tools), with a CLI, npm/cargo/PyPI packages, a self-hostable Kimetsu Remote HTTP MCP server and published benchmark numbers. The domain also operates agents.kimetsu.dev, a credential-free, read-only Agent Gateway with a published OpenAPI 3.1.0 (15 operations), an A2A Agent Card served at the RFC 8615 path (0.3 by default, 1.0 negotiated with the A2A-Version header) and a live JSON-RPC guide for Sidequest Commons — the maintainer's daily public project-selection loop run through GitHub issues and reactions — plus llms.txt on two hosts, a /.well-known/kimetsu-agents.json discovery pointer and JSON Schemas for its discovery documents. Everything is MIT OR Apache-2.0. Seeded from the A2A Registry
  listing dev.kimetsu.sidequest_commons_guide under the harvest name "Sidequest Commons".
finops:
- has_sources: true
  method: derived
  name: Kimetsu Dev Finops
  primary_unit: ''
  service_category: ''
  slug: kimetsu-dev-finops
  template: true
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
  slug: kimetsu
modified: '2026-09-19'
name: Kimetsu
nav: Providers
network: true
overview: 'Kimetsu publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including A2A API, Discovery API, Sidequest API, and 2 more. Tagged areas include Company, AI Agents, Agent Memory, Coding Agents, and MCP.


  The Kimetsu catalog on APIs.io includes 1 Spectral governance ruleset.


  Kimetsu''s developer surface includes documentation, API reference, getting-started guide, support, changelog, CLI, authentication, and 33 more developer resources.'
plans:
- name: Kimetsu Dev Plans Pricing
  plan_count: 0
  slug: kimetsu-dev-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Kimetsu Dev Rate Limits
  slug: kimetsu-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 92
  extends:
  - spectral:oas
  name: Kimetsu API Rules
  rule_count: 51
  severity_counts:
    error: 48
    hint: 0
    info: 1
    warn: 2
  slug: kimetsu-dev-rules
score:
  band: developing
  composite: 41.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 53.9
    catalog_earned_first_party: 12.0
    catalog_gap: 61.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.1
  facets:
    access_clarity: 0.0
    contract_governance: 31.8
    contract_quality: 53.3
    developer_ergonomics: 54.8
    discoverability: 63.3
    operational_transparency: 47.4
  previous_composite: 46.1
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
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/kimetsu-dev/kimetsu-dev-2026-10-11T110127.png
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
skill_count: 2
skills:
- name: discover-sidequest-commons
  slug: kimetsu-dev-discover-sidequest-commons
- name: kimetsu-brain
  slug: kimetsu-dev-kimetsu-brain-SKILL
slug: kimetsu-dev
tags:
- Company
- AI Agents
- Agent Memory
- Coding Agents
- MCP
- A2A
- Developer Tools
- Open Source
- Rust
- Agent Discovery
- Public Goods
website: https://kimetsu.dev/
---
