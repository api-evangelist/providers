---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Checks API from Agent Disco — 1 operation(s) for checks.
  name: Agent Disco Checks API
  slug: agentdisco-io-checks-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Keys API from Agent Disco — 3 operation(s) for keys.
  name: Agent Disco Keys API
  slug: agentdisco-io-keys-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Ops API from Agent Disco — 2 operation(s) for ops.
  name: Agent Disco Ops API
  slug: agentdisco-io-ops-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Scans API from Agent Disco — 3 operation(s) for scans.
  name: Agent Disco Scans API
  slug: agentdisco-io-scans-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Unlist API from Agent Disco — 4 operation(s) for unlist.
  name: Agent Disco Unlist API
  slug: agentdisco-io-unlist-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Webhooks API from Agent Disco — 2 operation(s) for webhooks.
  name: Agent Disco Webhooks API
  slug: agentdisco-io-webhooks-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: The Websites API from Agent Disco — 5 operation(s) for websites.
  name: Agent Disco Websites API
  slug: agentdisco-io-websites-api
- baseURL: https://agentdisco.io/api/v1
  baseurl_source: declared
  description: OpenAPI
  name: Agent Disco Open API
  slug: agentdisco-io-open-api-api
artifact_total: 20
asyncapis:
- description: ''
  name: Agentdisco Io Webhooks
  slug: agentdisco-io-webhooks
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://agentdisco.io/developers
- group: other
  href: https://artifacts.apis.io/agentdisco-io/capabilities/agentdisco-io-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/agentdisco-io-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/agentdisco-io/overlays/agentdisco-io-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/agentdisco-io-openapi-overlay.yaml
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
  href: https://artifacts.apis.io/agentdisco-io/llms/agentdisco-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agentdisco-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/agentdisco-io/well-known/agentdisco-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agentdisco-io-well-known.yml
- group: auth
  href: https://artifacts.apis.io/agentdisco-io/well-known/agentdisco-io-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/agentdisco-io-security.txt
- group: other
  href: https://artifacts.apis.io/agentdisco-io/a2a/agentdisco-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agentdisco-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agentdisco-io/mcp/agentdisco-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agentdisco-io-mcp.yml
- group: build
  href: https://artifacts.apis.io/agentdisco-io/mcp/agentdisco-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/agentdisco-io-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/agentdisco-io/packages/agentdisco-io-packages.yml
  title: ''
  type: Packages
  url: packages/agentdisco-io-packages.yml
- group: build
  href: https://artifacts.apis.io/agentdisco-io/packages/agentdisco-io-packages.yml
  title: ''
  type: SDKs
  url: packages/agentdisco-io-packages.yml
- group: auth
  href: https://artifacts.apis.io/agentdisco-io/authentication/agentdisco-io-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agentdisco-io-authentication.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/conventions/agentdisco-io-conventions.yml
  title: ''
  type: Conventions
  url: conventions/agentdisco-io-conventions.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/errors/agentdisco-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agentdisco-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/data-model/agentdisco-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agentdisco-io-data-model.yml
- group: operate
  href: https://artifacts.apis.io/agentdisco-io/rate-limits/agentdisco-io-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/agentdisco-io-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/agentdisco-io/plans/agentdisco-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/agentdisco-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/asyncapi/agentdisco-io-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/agentdisco-io-webhooks.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/conformance/agentdisco-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agentdisco-io-conformance.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/lifecycle/agentdisco-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/agentdisco-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/agentdisco-io/components/agentdisco-io-components.yml
  title: ''
  type: Components
  url: components/agentdisco-io-components.yml
- group: agent
  href: https://artifacts.apis.io/agentdisco-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/agentdisco-io/security/agentdisco-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agentdisco-io-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/agentdisco-io/security/agentdisco-io-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/agentdisco-io-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/agentdisco-io/security/agentdisco-io-vulnerability-disclosure.yml
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
finops:
- has_sources: true
  method: derived
  name: Agentdisco Io Finops
  primary_unit: ''
  service_category: ''
  slug: agentdisco-io-finops
  template: true
image: https://agentdisco.io/assets/images/favicon-yxiULnz.svg
layout: provider
mcp_servers:
- description: 'Agent Disco publishes an MCP descriptor at /.well-known/mcp.json (protocolVersion 2025-03-26, three tools with inputSchema) but ships NO MCP server: the descriptor''s own note says the tools "are curre'
  name: Agent Disco MCP Server
  slug: agent-disco
modified: '2026-09-19'
name: Agent Disco
nav: Providers
network: true
overview: 'Agent Disco publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checks API, Keys API, Ops API, and 5 more. Tagged areas include AI Agents, Agent Discoverability, Website Auditing, Developer Tools, and Webhook.


  The Agent Disco catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Agent Disco''s developer surface includes pricing, documentation, API reference, getting-started guide, support, signup flow, authentication, and 31 more developer resources.'
plans:
- name: Agentdisco Io Plans Pricing
  plan_count: 3
  slug: agentdisco-io-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 8
  name: Agentdisco Io Rate Limits
  slug: agentdisco-io-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Agent Disco API Rules
  rule_count: 57
  severity_counts:
    error: 45
    hint: 0
    info: 1
    warn: 11
  slug: agentdisco-io-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.5
  facets:
    access_clarity: 53.9
    contract_governance: 31.8
    contract_quality: 59.0
    developer_ergonomics: 42.3
    discoverability: 73.2
    operational_transparency: 52.6
  previous_composite: 62.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 8
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agentdisco-io/agentdisco-io-2026-10-11T093046.png
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
skill_count: 3
skills:
- name: Sign in as a Colony agent for the authenticated tier
  slug: agentdisco-io-colony-agent-sign-in
- name: Grade a site and read the result
  slug: agentdisco-io-grade-a-site
- name: Monitor a host's grade over time with a key and a webhook
  slug: agentdisco-io-monitor-a-host
slug: agentdisco-io
tags:
- AI Agents
- Agent Discoverability
- Website Auditing
- Developer Tools
- Webhook
- Llms.txt
- A2A
- MCP
- Scanning
website: https://agentdisco.io/
---
