---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: true
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: verified
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 60.3
  scored_at: '2026-09-23'
agentic_access:
- acting_count: 24
  human_in_the_loop: 1
  name: Postalform Com Agentic Access
  operation_count: 44
  slug: postalform-com-agentic-access
  summary_line: 44 operations · 24 acting · 1 human-in-the-loop
api_count: 4
apis:
- baseURL: https://postalform.com/api/machine
  baseurl_source: declared
  description: 'Machine-oriented print-and-mail REST API for autonomous agents: validate and quote, then create, pay for and poll document mail orders (PDF, server-rendered letter in text/html/markdown/rtf, workflow '
  name: PostalForm Machine Payments API
  slug: postalform-machine-payments-api
- baseURL: https://projects.postalform.com/api/v1
  baseurl_source: declared
  description: 'Developer mail infrastructure for server-side applications: per-workspace bearer API keys with a free simulated test mode (pf_test_) and a live mode on prepaid credits (pf_live_), two-step PDF upload,'
  name: PostalForm Projects Public API
  slug: postalform-projects-public-api
- description: Remote Model Context Protocol server at https://postalform.com/mcp (Streamable HTTP, wire protocol 2025-06-18, serverInfo postalform 0.1.0). initialize, tools/list and resources/list answer anonymousl
  name: PostalForm MCP Server
  slug: postalform-mcp-server
- description: 'Agent2Agent (A2A) surface: an agent card served from https://postalform.com/.well-known/agent-card.json (protocolVersion 1.0, JSONRPC binding, version 0.1.0, a2a-version: 1.0 response header) advertis'
  name: PostalForm A2A Agent
  slug: postalform-a2a-agent
artifact_total: 12
asyncapis:
- description: ''
  name: Postalform Com Projects Webhooks
  slug: postalform-com-projects-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://postalform.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://projects.postalform.com/
- group: docs
  title: ''
  type: Documentation
  url: https://postalform.com/developers
- group: docs
  title: ''
  type: APIReference
  url: https://postalform.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://postalform.com/developers/quickstart
- group: operate
  title: ''
  type: Support
  url: https://postalform.com/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://postalform.com/help
- group: company
  title: ''
  type: Blog
  url: https://blog.postalform.com/
- group: company
  title: ''
  type: BlogRSS
  url: https://blog.postalform.com/rss.xml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postalform
- group: commercial
  title: ''
  type: Pricing
  url: https://postalform.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://projects.postalform.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postalform.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postalform.com/privacy
- group: other
  title: ''
  type: AcceptableUsePolicy
  url: https://postalform.com/acceptable-use
- group: operate
  title: ''
  type: StatusPage
  url: https://postalform.com/api/health
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/changelog/postalform-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/postalform-com-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.postalform.com/
- group: other
  title: ''
  type: APIsJson
  url: https://postalform.com/apis.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/llms/postalform-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postalform-com-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://postalform.com/llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/a2a/postalform-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/postalform-com-a2a.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/mcp/postalform-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/postalform-com-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/mcp/postalform-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/postalform-com-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/well-known/postalform-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postalform-com-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/well-known/postalform-com-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/postalform-com-api-catalog.json
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/well-known/postalform-com-robots.txt
  title: ''
  type: ContentSignal
  url: well-known/postalform-com-robots.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/authentication/postalform-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postalform-com-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/conventions/postalform-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postalform-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/conventions/postalform-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postalform-com-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/errors/postalform-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postalform-com-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/lifecycle/postalform-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/postalform-com-lifecycle.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/sandbox/postalform-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/postalform-com-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/conformance/postalform-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postalform-com-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/data-model/postalform-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postalform-com-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/asyncapi/postalform-com-projects-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/postalform-com-projects-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/plans/postalform-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postalform-com-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/rate-limits/postalform-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/postalform-com-rate-limits.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/packages/postalform-com-packages.yml
  title: ''
  type: Packages
  url: packages/postalform-com-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/agentic-access/postalform-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postalform-com-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/postalform-com/refs/heads/main/security/postalform-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postalform-com-domain-security.yml
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://postalform.com/privacy
created: '2026-09-19'
description: 'PostalForm is an online print-and-mail service operated by MindBike Technologies LLC that turns PDFs, letters, filled government and consumer forms, dispute packets, postcards and CSV bulk campaigns into real postal mail for twelve countries, with address validation, Certified Mail and electronic return receipts. It is built agent-first: a remote MCP server at https://postalform.com/mcp (12 tools, no credential to connect) creates reviewable hosted-checkout drafts; a 17-operation Machine Payments API lets autonomous runtimes validate, pay for and track orders through x402 (USDC on Base) or Stripe''s Machine Payments Protocol under an HTTP 402 challenge; an A2A 1.0 agent card, UCP and ACP checkout endpoints, an RFC 9727 api-catalog, an APIs.json index and an x402 manifest are served from /.well-known/. PostalForm Projects (25 operations) adds API-key workspaces with a free test mode, final-price quotes, Idempotency-Key orders, prepaid credits and signed webhooks.'
image: https://postalform.com/og/default.png
layout: provider
mcp_servers:
- description: ''
  name: PostalForm MCP Server
  slug: postalform-mcp-server
- description: ''
  name: PostalForm MCP endpoint (Streamable HTTP)
  slug: postalform-mcp-endpoint-streamable-http
modified: '2026-09-19'
name: PostalForm
nav: Providers
network: true
overview: 'PostalForm publishes 2 APIs on the [APIs.io](https://apis.io/) network: Machine Payments API and Projects Public API. Tagged areas include Physical Mail, Print & Mail, Postal Mail, Certified Mail, and Documents.


  The PostalForm catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  PostalForm''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 36 more developer resources.'
plans:
- name: Postalform Com Plans Pricing
  plan_count: 3
  slug: postalform-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Postalform Com Rate Limits
  slug: postalform-com-rate-limits
score:
  band: strong
  composite: 59.5
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 54.1
    developer_ergonomics: 71.4
    discoverability: 81.5
    operational_transparency: 44.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 59.5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: true
    score: 0.0
security:
- kind: authentication
  name: Postalform Com Authentication
  slug: postalform-com-authentication
  summary_line: http/none/payment-gated · 3 schemes
- kind: domain-security
  name: Postalform Com Domain Security
  slug: postalform-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postalform-com
tags:
- Physical Mail
- Print & Mail
- Postal Mail
- Certified Mail
- Documents
- Agents
- Agentic Commerce
- MCP
- A2A
- x402
- Machine Payments
- Webhook
- Agent-Native
- United States
website: https://postalform.com/
---
