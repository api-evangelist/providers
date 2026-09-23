---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.1
  scored_at: '2026-09-23'
api_count: 1
apis:
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: Public HTTP API under /api/v1 - submit a URL for grading, poll the scan, diff it against the previous scan, read a host's latest grade and history, embed an SVG/PNG grade badge, read the check catalog
  name: Agent Disco API
  slug: agent-disco-api
artifact_total: 8
asyncapis:
- description: ''
  name: Agentdisco Io Webhooks
  slug: agentdisco-io-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://agentdisco.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://agentdisco.io/developers
- group: docs
  title: ''
  type: Documentation
  url: https://agentdisco.io/developers
- group: docs
  title: ''
  type: APIReference
  url: https://agentdisco.io/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://agentdisco.io/llms-full.txt
- group: operate
  title: ''
  type: Support
  url: https://agentdisco.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agentdisco.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agentdisco.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://agentdisco.io/register
- group: start
  title: ''
  type: Login
  url: https://agentdisco.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentdisco
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/llms/agentdisco-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdisco-io-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/well-known/agentdisco-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdisco-io-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/well-known/agentdisco-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentdisco-io-security.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/a2a/agentdisco-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentdisco-io-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/mcp/agentdisco-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdisco-io-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/mcp/agentdisco-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentdisco-io-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/packages/agentdisco-io-packages.yml
  title: ''
  type: Packages
  url: packages/agentdisco-io-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/packages/agentdisco-io-packages.yml
  title: ''
  type: SDKs
  url: packages/agentdisco-io-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/authentication/agentdisco-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdisco-io-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/conventions/agentdisco-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentdisco-io-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/errors/agentdisco-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdisco-io-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/data-model/agentdisco-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdisco-io-data-model.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/rate-limits/agentdisco-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentdisco-io-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/plans/agentdisco-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdisco-io-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/asyncapi/agentdisco-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentdisco-io-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/conformance/agentdisco-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdisco-io-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/lifecycle/agentdisco-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentdisco-io-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/components/agentdisco-io-components.yml
  title: ''
  type: Components
  url: components/agentdisco-io-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/security/agentdisco-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdisco-io-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/security/agentdisco-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdisco-io-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/agentdisco-io/refs/heads/main/security/agentdisco-io-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/agentdisco-io-vulnerability-disclosure.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://agentdisco.io/privacy
- group: other
  title: ''
  type: DataResidency
  url: https://agentdisco.io/privacy
created: '2026-09-19'
description: Agent Disco grades any public website for AI-agent discoverability. Operated by Starsol Ltd (Norwich, England), it fetches the handful of URIs agent runtimes actually read - robots.txt rules for GPTBot and ClaudeBot, llms.txt, /.well-known/ai-plugin.json, agent.json and mcp.json, OpenAPI specs, SDK and registry signals, TLS and anti-bot posture - and returns a letter grade A-F with a per-category breakdown, fix hints and an embeddable badge. A public REST API under /api/v1 (OpenAPI 3.1, Swagger UI) submits scans, polls results, diffs scans, manages API keys and signed scan.completed webhooks, and lets autonomous agents sign in with a Colony identity through OAuth 2.0 Token Exchange (RFC 8693).
image: https://agentdisco.io/assets/images/favicon-yxiULnz.svg
layout: provider
mcp_servers:
- description: 'Agent Disco publishes an MCP descriptor at /.well-known/mcp.json (protocolVersion 2025-03-26, three tools with inputSchema) but ships NO MCP server: the descriptor''s own note says the tools "are curre'
  name: Agent Disco MCP Server
  slug: agent-disco-mcp-server
modified: '2026-09-19'
name: Agent Disco
nav: Providers
network: true
overview: 'Agent Disco publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Agent Discoverability, Website Auditing, Developer Tools, and Webhook.


  The Agent Disco catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Agent Disco''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, authentication, and 29 more developer resources.'
plans:
- name: Agentdisco Io Plans Pricing
  plan_count: 3
  slug: agentdisco-io-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 8
  name: Agentdisco Io Rate Limits
  slug: agentdisco-io-rate-limits
score:
  band: strong
  composite: 58.2
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 64.0
    developer_ergonomics: 63.7
    discoverability: 75.9
    operational_transparency: 55.3
  previous_composite: 58.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
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
  name: Agentdisco Io Authentication
  slug: agentdisco-io-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agentdisco Io Domain Security
  slug: agentdisco-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Agentdisco Io Vulnerability Disclosure
  slug: agentdisco-io-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: agentdisco-io
tags:
- AI Agents
- Agent Discoverability
- Website Auditing
- Developer Tools
- Webhook
- llms-txt
- A2A
- MCP
- Scanning
website: https://agentdisco.io/
---
