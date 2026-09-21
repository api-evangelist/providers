---
agent_readiness:
  band: agent-ready
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.4
  scored_at: '2026-09-20'
api_count: 1
apis:
- baseURL: https://agentsearch.luthersystems.com
  baseurl_source: declared
  description: Public, no-auth HTTP API for AgentSearch, Luther Systems' daily-scored index of AI agents and MCP servers, at https://agentsearch.luthersystems.com. Six operations described by a provider-published Op
  name: AgentSearch HTTP API
  slug: agentsearch-api
- description: 'Model Context Protocol surface for AgentSearch in two deployments. Hosted: POST https://agentsearch.luthersystems.com/api/mcp, Streamable HTTP, protocol version 2025-06-18, serverInfo agentsearch 0.1.'
  name: AgentSearch MCP Server
  slug: agentsearch-mcp
- description: Agent2Agent surface for AgentSearch — an agent card at https://agentsearch.luthersystems.com/.well-known/agent-card.json (protocolVersion 0.3.0, version 0.1.0, provider Luther Systems, five skills wit
  name: AgentSearch A2A Agent
  slug: agentsearch-a2a-agent
- description: 'Hosted Model Context Protocol server for InsideOut, Luther Systems'' agentic cloud architect: POST https://app.luthersystems.com/v1/insideout-mcp, Streamable HTTP with SSE responses and an Mcp-Session-'
  name: InsideOut (Riley) MCP Server
  slug: insideout-mcp
- description: Agent2Agent surface for InsideOut — an agent card at https://insideout.luthersystems.com/.well-known/agent-card.json (protocolVersion 0.3, version 1.0.0, provider Luther Systems, one skill design-depl
  name: InsideOut A2A Agent
  slug: insideout-a2a-agent
- description: 'Buf-managed Protocol Buffers published at github.com/luthersystems/protos (module buf.build/luthersystems/protos) that define API contracts and shared messages across the Luther Enterprise platform: t'
  name: Luther Platform Protobuf Contracts
  slug: luther-platform-protobuf
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://luthersystems.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.luthersystems.com/
- group: docs
  title: ''
  type: APIReference
  url: https://agentsearch.luthersystems.com/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/luthersystems/docs/blob/main/common-operation-script/quickstart/README.md
- group: operate
  title: ''
  type: Support
  url: https://www.luthersystems.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.luthersystems.com/insights
- group: other
  title: ''
  type: CaseStudies
  url: https://www.luthersystems.com/case-studies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/luthersystems
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/luther-systems
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.luthersystems.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.luthersystems.com/cookie-policy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://www.luthersystems.com/privacy-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/changelog/luthersystems-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/luthersystems-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/luthersystems/docs/blob/main/release-notes.md
- group: auth
  title: ''
  type: Security
  url: https://github.com/luthersystems/insideout-agent-skills/blob/main/SECURITY.md
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/security/luthersystems-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/luthersystems-com-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/security/luthersystems-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/luthersystems-com-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/well-known/luthersystems-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/luthersystems-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/a2a/luthersystems-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/luthersystems-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/mcp/luthersystems-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/luthersystems-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/mcp/luthersystems-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/luthersystems-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/llms/luthersystems-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/luthersystems-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://agentsearch.luthersystems.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://insideout.luthersystems.com/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/luthersystems/insideout-agent-skills/blob/main/SKILL.md
- group: agent
  title: ''
  type: AgentSkill
  url: https://github.com/luthersystems/substrate-agent-skills/blob/main/SKILL.md
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/grpc/luthersystems-protos/pdfserv/v1/service.proto
  title: ''
  type: Protobuf
  url: grpc/luthersystems-protos/pdfserv/v1/service.proto
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/packages/luthersystems-com-packages.yml
  title: ''
  type: Packages
  url: packages/luthersystems-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/packages/luthersystems-com-packages.yml
  title: ''
  type: SDKs
  url: packages/luthersystems-com-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/cli/luthersystems-com-cli.yml
  title: ''
  type: CLI
  url: cli/luthersystems-com-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/authentication/luthersystems-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/luthersystems-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/conventions/luthersystems-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/luthersystems-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/errors/luthersystems-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/luthersystems-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/lifecycle/luthersystems-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/luthersystems-com-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/conformance/luthersystems-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/luthersystems-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/data-model/luthersystems-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/luthersystems-com-data-model.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/plans/luthersystems-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/luthersystems-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/rate-limits/luthersystems-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/luthersystems-com-rate-limits.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/luthersystems-com/refs/heads/main/regulatory/luthersystems-com-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/luthersystems-com-regulatory-posture.yml
created: '2026-09-19'
description: 'Luther Systems is a London- and Campbell, CA-based enterprise software company (Luther Systems Limited and Luther Systems US Incorporated) whose Luther Platform automates end-to-end enterprise processes — "Deep Process Automation" — for customers such as Allianz and DLA Piper''s TOKO, running business logic (ELPS "phyla") on the Substrate runtime over Hyperledger Fabric with ConnectorHub integrations, a shiroclient JSON-RPC gateway, LutherAuth identity and Buf-managed Protobuf contracts. Its public, agent-native surface is two products: AgentSearch (agentsearch.luthersystems.com) — a free, no-auth, daily-scored index of ~4,300 AI agents and MCP servers exposed as an OpenAPI 3.1 HTTP API, a hosted Streamable HTTP MCP server (5 tools) plus an npm stdio package, and an A2A 0.3.0 agent card with a live JSON-RPC endpoint — and InsideOut (Riley) — an agentic cloud architect that designs, prices, generates Terraform for, deploys and inspects AWS/GCP infrastructure through a hosted
  MCP server at app.luthersystems.com (24 tools, session-scoped, no keys for design), an A2A 0.3 card, provider-published Agent Skills, Claude Code / Kiro / Cursor plugins and a Docker image. The enterprise platform ships Go SDKs, the shirotester CLI (with a local MCP server), the mars infrastructure CLI and a public docs repository with dated release notes.'
image: https://avatars.githubusercontent.com/u/20160060?v=4
layout: provider
mcp_servers:
- description: ''
  name: Luther Systems MCP Server
  slug: luther-systems-mcp-server
- description: ''
  name: AgentSearch hosted MCP endpoint (Streamable HTTP)
  slug: agentsearch-hosted-mcp-endpoint-streamable-http
- description: ''
  name: InsideOut hosted MCP endpoint (Streamable HTTP)
  slug: insideout-hosted-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Luther Systems
nav: Providers
network: true
overview: 'Luther Systems publishes 1 API on the [APIs.io](https://apis.io/) network: AgentSearch HTTP API. Tagged areas include Agents, Agent Discovery, MCP, A2A, and agent-native.


  Luther Systems'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, changelog, CLI, and 33 more developer resources.'
plans:
- name: Luthersystems Com Plans Pricing
  plan_count: 1
  slug: luthersystems-com-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 1
  name: Luthersystems Com Rate Limits
  slug: luthersystems-com-rate-limits
score:
  band: developing
  composite: 48.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 48.0
    catalog_earned_first_party: 16.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 45.8
  facets:
    access_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 45.6
    developer_ergonomics: 69.0
    discoverability: 66.7
    operational_transparency: 52.6
  previous_composite: 2.8
  provenance:
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
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 40.9
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: rising
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Luthersystems Com Authentication
  slug: luthersystems-com-authentication
  summary_line: 6 schemes
- kind: domain-security
  name: Luthersystems Com Domain Security
  slug: luthersystems-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Luthersystems Com Vulnerability Disclosure
  slug: luthersystems-com-vulnerability-disclosure
  summary_line: Hackerone · contact published
slug: luthersystems-com
tags:
- Agents
- Agent Discovery
- MCP
- A2A
- agent-native
- Cloud Infrastructure
- Terraform
- Infrastructure as Code
- Process Automation
- Enterprise Automation
- Distributed Ledger
- Hyperledger Fabric
- Insurance
- Financial-Services
- Open-Source
website: https://luthersystems.com/
---
