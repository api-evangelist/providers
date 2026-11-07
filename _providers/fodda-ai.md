---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: documented
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 32
  human_in_the_loop: 0
  name: Fodda Ai Agentic Access
  operation_count: 167
  slug: fodda-ai-agentic-access
  summary_line: 167 operations · 32 acting
api_count: 2
apis:
- description: 'Hosted Model Context Protocol server at mcp.fodda.ai exposing 53 tools (tools-manifest.json, v1.46.79) over streamable-http (/mcp), SSE (/sse), a curated 17-tool Microsoft Copilot endpoint (/copilot) '
  name: Fodda MCP Server
  slug: fodda-mcp-server
- description: Agent-to-Agent endpoint at mcp.fodda.ai/a2a (JSONRPC, A2A protocolVersion 0.3.0) discovered from https://www.fodda.ai/.well-known/agent-card.json, declaring seven skills — brand intelligence, trend se
  name: Fodda Research Agent (A2A)
  slug: fodda-research-agent-a2a
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Accounts API from Fodda (PSFK) — 1 operation(s) for accounts.
  name: Fodda (PSFK) Accounts API
  slug: fodda-ai-accounts-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Admin API from Fodda (PSFK) — 1 operation(s) for admin.
  name: Fodda (PSFK) Admin API
  slug: fodda-ai-admin-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Analysts API from Fodda (PSFK) — 3 operation(s) for analysts.
  name: Fodda (PSFK) Analysts API
  slug: fodda-ai-analysts-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Brand Intelligence API from Fodda (PSFK) — 1 operation(s) for brand intelligence.
  name: Fodda (PSFK) Brand Intelligence API
  slug: fodda-ai-brand-intelligence-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Context API from Fodda (PSFK) — 1 operation(s) for context.
  name: Fodda (PSFK) Context API
  slug: fodda-ai-context-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Copilot API from Fodda (PSFK) — 3 operation(s) for copilot.
  name: Fodda (PSFK) Copilot API
  slug: fodda-ai-copilot-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Graph Slice API from Fodda (PSFK) — 2 operation(s) for graph slice.
  name: Fodda (PSFK) Graph Slice API
  slug: fodda-ai-graph-slice-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Graphs API from Fodda (PSFK) — 18 operation(s) for graphs.
  name: Fodda (PSFK) Graphs API
  slug: fodda-ai-graphs-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Health API from Fodda (PSFK) — 1 operation(s) for health.
  name: Fodda (PSFK) Health API
  slug: fodda-ai-health-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Log API from Fodda (PSFK) — 1 operation(s) for log.
  name: Fodda (PSFK) Log API
  slug: fodda-ai-log-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Offerings API from Fodda (PSFK) — 1 operation(s) for offerings.
  name: Fodda (PSFK) Offerings API
  slug: fodda-ai-offerings-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Psfk API from Fodda (PSFK) — 1 operation(s) for psfk.
  name: Fodda (PSFK) Psfk API
  slug: fodda-ai-psfk-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Research API from Fodda (PSFK) — 9 operation(s) for research.
  name: Fodda (PSFK) Research API
  slug: fodda-ai-research-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Search API from Fodda (PSFK) — 5 operation(s) for search.
  name: Fodda (PSFK) Search API
  slug: fodda-ai-search-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Sources API from Fodda (PSFK) — 1 operation(s) for sources.
  name: Fodda (PSFK) Sources API
  slug: fodda-ai-sources-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Spt API from Fodda (PSFK) — 1 operation(s) for spt.
  name: Fodda (PSFK) Spt API
  slug: fodda-ai-spt-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The Supplemental API from Fodda (PSFK) — 110 operation(s) for supplemental.
  name: Fodda (PSFK) Supplemental API
  slug: fodda-ai-supplemental-api
- baseURL: https://api.fodda.ai
  baseurl_source: declared
  description: The User API from Fodda (PSFK) — 5 operation(s) for user.
  name: Fodda (PSFK) User API
  slug: fodda-ai-user-api
artifact_total: 44
asyncapis:
- description: ''
  name: Fodda Ai Event Surface
  slug: fodda-ai-event-surface
common:
- group: other
  href: https://artifacts.apis.io/fodda-ai/capabilities/fodda-ai-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/fodda-ai-capability-edges.yml
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
  href: https://artifacts.apis.io/fodda-ai/llms/fodda-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/fodda-ai-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://www.fodda.ai/llms.txt
- group: agent
  href: https://artifacts.apis.io/fodda-ai/well-known/fodda-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/fodda-ai-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.fodda.ai/.well-known/api-catalog.json
- group: other
  href: https://artifacts.apis.io/fodda-ai/a2a/fodda-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/fodda-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/fodda-ai/mcp/fodda-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/fodda-ai-mcp.yml
- group: build
  href: https://artifacts.apis.io/fodda-ai/mcp/fodda-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/fodda-ai-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/fodda-ai/packages/fodda-ai-packages.yml
  title: ''
  type: Packages
  url: packages/fodda-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/fodda-ai/cli/fodda-ai-cli.yml
  title: ''
  type: CLI
  url: cli/fodda-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/authentication/fodda-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/fodda-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/scopes/fodda-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/fodda-ai-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://clerk.fodda.ai/.well-known/openid-configuration
- group: design
  href: https://artifacts.apis.io/fodda-ai/conventions/fodda-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/fodda-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/fodda-ai/errors/fodda-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/fodda-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/fodda-ai/data-model/fodda-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/fodda-ai-data-model.yml
- group: other
  href: https://artifacts.apis.io/fodda-ai/overlays/fodda-ai-tags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/fodda-ai-tags-overlay.yaml
- group: build
  href: https://artifacts.apis.io/fodda-ai/examples/fodda-ai-examples.yml
  title: ''
  type: Examples
  url: examples/fodda-ai-examples.yml
- group: operate
  href: https://artifacts.apis.io/fodda-ai/rate-limits/fodda-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/fodda-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/fodda-ai/plans/fodda-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fodda-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/fodda-ai/lifecycle/fodda-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/fodda-ai-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/fodda-ai/changelog/fodda-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/fodda-ai-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/piers-fawkes/fodda-mcp/blob/main/CHANGELOG.md
- group: design
  href: https://artifacts.apis.io/fodda-ai/conformance/fodda-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/fodda-ai-conformance.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/security/fodda-ai-trust-center.yml
  title: ''
  type: Compliance
  url: security/fodda-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/security/fodda-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/fodda-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/security/fodda-ai-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/fodda-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/security/fodda-ai-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/fodda-ai-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/fodda-ai/security/fodda-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fodda-ai-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/fodda-ai/agentic-access/fodda-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/fodda-ai-agentic-access.yml
- group: agent
  href: https://artifacts.apis.io/fodda-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/fodda-ai/asyncapi/fodda-ai-event-surface.yml
  title: ''
  type: Webhooks
  url: asyncapi/fodda-ai-event-surface.yml
- group: other
  href: https://artifacts.apis.io/fodda-ai/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: AITransparency
  url: regulatory/fodda-ai-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/fodda-ai/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: DataSubjectRequest
  url: regulatory/fodda-ai-regulatory-posture.yml
- group: other
  href: https://artifacts.apis.io/fodda-ai/regulatory/fodda-ai-regulatory-posture.yml
  title: ''
  type: ExitAssistance
  url: regulatory/fodda-ai-regulatory-posture.yml
created: '2026-09-19'
description: 'Fodda is the agent-native research layer built by PSFK, the trend-intelligence publisher, exposing 250+ expert-curated knowledge graphs (retail, beauty, fashion, sport, food and beverage, travel, technology), named-expert "Human Agent" digital twins, earnings-call intelligence across 500+ consumer-sector companies, and 80+ live institutional data sources (FRED, BEA, BLS, Census, ONS, Eurostat, ECB and more) to AI agents. It is reachable three ways from one data core: a REST API at api.fodda.ai (OpenAPI 3.1, 157 operations, per-operation price extensions), a hosted MCP server at mcp.fodda.ai (streamable-http, SSE, a curated Copilot endpoint, OAuth via Clerk with dynamic client registration, plus a stdio package on npm), and an A2A agent at mcp.fodda.ai/a2a discovered from /.well-known/agent-card.json. Access is metered per API call ($0.50) with three rails: an X-API-Key account key with a free monthly tier, enterprise OIDC bearer tokens, and a zero-onboarding Machine Payments
  Protocol flow in which any unauthenticated request answers HTTP 402 with the exact price and a Stripe Shared Payment Token is presented on retry. The catalog itself is published as an Open Knowledge Format bundle, an RFC 9727 api-catalog linkset, llms.txt/agents.txt manifests, and ten MIT-licensed installable Agent Skills.'
finops:
- has_sources: true
  method: derived
  name: Fodda Ai Finops
  primary_unit: api call
  service_category: ''
  slug: fodda-ai-finops
  template: false
image: https://ucarecdn.com/6e7893d7-6b14-426b-83bc-574a3f72d6bc/foddafavicon.png
jsonld:
- class_count: 0
  name: Fodda Ai Retail Graph Slice Context
  property_count: 0
  slug: fodda-ai-retail-graph-slice
layout: provider
mcp_servers:
- description: Fodda ships a hosted, first-party MCP server at mcp.fodda.ai (streamable-http /mcp, SSE /sse, a curated 17-tool Copilot Studio endpoint /copilot, and offering-scoped endpoints such as /grok-brand-cont
  name: Fodda
  slug: fodda
modified: '2026-09-19'
name: Fodda (PSFK)
nav: Providers
network: true
overview: 'Fodda (PSFK) publishes 20 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Admin API, Analysts API, and 17 more. Tagged areas include Market Intelligence, Trend Research, Knowledge Graph, Consumer Insights, and Earnings Intelligence.


  The Fodda (PSFK) catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Fodda (PSFK)''s developer surface includes documentation, API reference, getting-started guide, support, FAQ, engineering blog, pricing, and 42 more developer resources.'
plans:
- name: Fodda Ai Plans Pricing
  plan_count: 4
  slug: fodda-ai-plans-pricing
- name: Fodda Ai Price Estimates
  plan_count: 0
  slug: fodda-ai-price-estimates
random_paper: 13
rate_limits:
- limit_count: 0
  name: Fodda Ai Rate Limits
  slug: fodda-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Fodda (PSFK) API Rules
  rule_count: 52
  severity_counts:
    error: 41
    hint: 0
    info: 5
    warn: 6
  slug: fodda-ai-rules
scopes:
- name: Fodda Ai Scopes
  scope_count: 8
  slug: fodda-ai-scopes
  summary_line: 8 scopes · authorizationCode/deviceCode
score:
  band: strong
  composite: 61.5
  coverage:
    artifact_dirs: 35
    catalog_earned: 61.5
    catalog_earned_first_party: 12.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.9
  facets:
    access_clarity: 77.6
    contract_governance: 31.8
    contract_quality: 64.3
    developer_ergonomics: 48.8
    discoverability: 85.0
    operational_transparency: 36.8
  previous_composite: 70.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 83.3
      total: 18
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 44.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/fodda-ai/fodda-ai-2026-10-11T104547.png
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
skill_count: 10
skills:
- name: fodda-brand-intelligence
  slug: fodda-ai-brand-intelligence
- name: fodda-category-trend-watch
  slug: fodda-ai-category-trend-watch
- name: fodda-commission-expert-deliverable
  slug: fodda-ai-commission-expert-deliverable
- name: fodda-competitive-landscape-brief
  slug: fodda-ai-competitive-landscape-brief
- name: fodda-deep-research
  slug: fodda-ai-deep-research
- name: fodda-earnings-divergence-read
  slug: fodda-ai-earnings-divergence-read
- name: fodda-fit-discovery
  slug: fodda-ai-fodda-fit-discovery
- name: fodda-pitch-prep
  slug: fodda-ai-pitch-prep-pressure-test
- name: fodda-synthetic-consultant
  slug: fodda-ai-synthetic-consultant
- name: fodda-topic-brief
  slug: fodda-ai-topic-brief
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
