---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 55.7
  scored_at: '2026-09-25'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Fodda Ai Agentic Access
  operation_count: 167
  slug: fodda-ai-agentic-access
  summary_line: 167 operations · 32 acting
api_count: 2
apis:
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: REST interface at api.fodda.ai for expert-curated knowledge graphs (search, node retrieval, neighbor traversal, evidence, statistics, adjacent-trend discovery), autonomous deep research (async job lau
  name: Fodda Context & Research API
  slug: fodda-context-research-api
- description: 'Hosted Model Context Protocol server at mcp.fodda.ai exposing 53 tools (tools-manifest.json, v1.46.79) over streamable-http (/mcp), SSE (/sse), a curated 17-tool Microsoft Copilot endpoint (/copilot) '
  name: Fodda MCP Server
  slug: fodda-mcp-server
- description: Agent-to-Agent endpoint at mcp.fodda.ai/a2a (JSONRPC, A2A protocolVersion 0.3.0) discovered from https://www.fodda.ai/.well-known/agent-card.json, declaring seven skills — brand intelligence, trend se
  name: Fodda Research Agent (A2A)
  slug: fodda-research-agent-a2a
artifact_total: 15
asyncapis:
- description: ''
  name: Fodda Ai Event Surface
  slug: fodda-ai-event-surface
common:
- group: company
  title: ''
  type: Website
  url: https://fodda.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.fodda.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fodda.ai/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.fodda.ai/api
- group: start
  title: ''
  type: GettingStarted
  url: https://www.fodda.ai/connect
- group: operate
  title: ''
  type: Support
  url: https://www.fodda.ai/contact
- group: operate
  title: ''
  type: FAQ
  url: https://www.fodda.ai/faq
- group: company
  title: ''
  type: Blog
  url: https://www.fodda.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fodda-ai
- group: commercial
  title: ''
  type: Pricing
  url: https://www.fodda.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.fodda.ai/sign-up
- group: start
  title: ''
  type: Login
  url: https://app.fodda.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fodda.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fodda.ai/privacy
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/llms/fodda-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fodda-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.fodda.ai/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/well-known/fodda-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fodda-ai-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.fodda.ai/.well-known/api-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/a2a/fodda-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fodda-ai-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/mcp/fodda-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fodda-ai-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/mcp/fodda-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fodda-ai-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/packages/fodda-ai-packages.yml
  title: ''
  type: Packages
  url: packages/fodda-ai-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/cli/fodda-ai-cli.yml
  title: ''
  type: CLI
  url: cli/fodda-ai-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/authentication/fodda-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fodda-ai-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/scopes/fodda-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fodda-ai-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://clerk.fodda.ai/.well-known/openid-configuration
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/conventions/fodda-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fodda-ai-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/errors/fodda-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fodda-ai-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/data-model/fodda-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fodda-ai-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/overlays/fodda-ai-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fodda-ai-tags-overlay.yaml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/examples/fodda-ai-examples.yml
  title: ''
  type: Examples
  url: examples/fodda-ai-examples.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/rate-limits/fodda-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fodda-ai-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/plans/fodda-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fodda-ai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/lifecycle/fodda-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fodda-ai-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/changelog/fodda-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fodda-ai-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/piers-fawkes/fodda-mcp/blob/main/CHANGELOG.md
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/conformance/fodda-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fodda-ai-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/security/fodda-ai-trust-center.yml
  title: ''
  type: Compliance
  url: security/fodda-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/security/fodda-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fodda-ai-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/security/fodda-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fodda-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/security/fodda-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fodda-ai-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/security/fodda-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fodda-ai-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/agentic-access/fodda-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fodda-ai-agentic-access.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/asyncapi/fodda-ai-event-surface.yml
  title: ''
  type: Webhooks
  url: asyncapi/fodda-ai-event-surface.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/fodda-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/fodda-ai-regulatory-posture.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/fodda-ai/refs/heads/main/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: ExitAssistance
  url: regulatory/fodda-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'Fodda is the agent-native research layer built by PSFK, the trend-intelligence publisher, exposing 250+ expert-curated knowledge graphs (retail, beauty, fashion, sport, food and beverage, travel, technology), named-expert "Human Agent" digital twins, earnings-call intelligence across 500+ consumer-sector companies, and 80+ live institutional data sources (FRED, BEA, BLS, Census, ONS, Eurostat, ECB and more) to AI agents. It is reachable three ways from one data core: a REST API at api.fodda.ai (OpenAPI 3.1, 157 operations, per-operation price extensions), a hosted MCP server at mcp.fodda.ai (streamable-http, SSE, a curated Copilot endpoint, OAuth via Clerk with dynamic client registration, plus a stdio package on npm), and an A2A agent at mcp.fodda.ai/a2a discovered from /.well-known/agent-card.json. Access is metered per API call ($0.50) with three rails: an X-API-Key account key with a free monthly tier, enterprise OIDC bearer tokens, and a zero-onboarding Machine Payments
  Protocol flow in which any unauthenticated request answers HTTP 402 with the exact price and a Stripe Shared Payment Token is presented on retry. The catalog itself is published as an Open Knowledge Format bundle, an RFC 9727 api-catalog linkset, llms.txt/agents.txt manifests, and ten MIT-licensed installable Agent Skills.'
image: https://ucarecdn.com/6e7893d7-6b14-426b-83bc-574a3f72d6bc/foddafavicon.png
jsonld:
- class_count: 0
  name: Fodda Ai Retail Graph Slice Context
  property_count: 0
  slug: fodda-ai-retail-graph-slice
layout: provider
mcp_servers:
- description: ''
  name: Fodda
  slug: fodda
- description: ''
  name: Fodda MCP endpoint (Streamable HTTP)
  slug: fodda-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: Fodda (PSFK)
nav: Providers
network: true
overview: 'Fodda (PSFK) publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Fodda Context & Research API, and 2 more. Tagged areas include Market Intelligence, Trend Research, Knowledge Graph, Consumer Insights, and Earnings Intelligence.


  The Fodda (PSFK) catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 JSON-LD context.


  Fodda (PSFK)''s developer surface includes documentation, API reference, getting-started guide, support, FAQ, engineering blog, pricing, and 41 more developer resources.'
plans:
- name: Fodda Ai Plans Pricing
  plan_count: 4
  slug: fodda-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Fodda Ai Rate Limits
  slug: fodda-ai-rate-limits
scopes:
- name: Fodda Ai Scopes
  scope_count: 8
  slug: fodda-ai-scopes
  summary_line: 8 scopes · authorizationCode/deviceCode
score:
  band: strong
  composite: 66.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 54.0
    catalog_earned_first_party: 12.0
    catalog_gap: 61.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.0
  facets:
    access_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 71.4
    discoverability: 85.0
    operational_transparency: 39.5
  previous_composite: 69.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.2
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Fodda Ai Authentication
  slug: fodda-ai-authentication
  summary_line: apiKey/http/openIdConnect/oauth2 · 5 schemes
- kind: domain-security
  name: Fodda Ai Domain Security
  slug: fodda-ai-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Fodda Ai Vulnerability Disclosure
  slug: fodda-ai-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Fodda Ai Trust Center
  slug: fodda-ai-trust-center
  summary_line: trust center published
slug: fodda-ai
tags:
- Market Intelligence
- Trend Research
- Knowledge Graph
- Consumer Insights
- Earnings Intelligence
- Brand Intelligence
- Research
- Institutional Data
- MCP
- A2A
- Agent-Native
- Machine Payments
- Company
website: https://fodda.ai/
---
