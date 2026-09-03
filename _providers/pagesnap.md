---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: REST API converting public URLs to Markdown, text, HTML, JSON, ARIA trees, screenshots, PDFs, link-preview metadata and normalized structured data, plus batch reads, robots-aware crawls with a 202 job
  name: Pagesnap API
  slug: pagesnap-api
artifact_total: 10
asyncapis:
- description: ''
  name: Pagesnap Webhooks
  slug: pagesnap-webhooks
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://pagesnap.142-93-197-141.sslip.io
- group: docs
  title: ''
  type: Documentation
  url: https://pagesnap.142-93-197-141.sslip.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://pagesnap.142-93-197-141.sslip.io/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://pagesnap.142-93-197-141.sslip.io/agents
- group: commercial
  title: ''
  type: Pricing
  url: https://pagesnap.142-93-197-141.sslip.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://pagesnap.142-93-197-141.sslip.io/keys
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pagesnap.142-93-197-141.sslip.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pagesnap.142-93-197-141.sslip.io/terms
- group: operate
  title: ''
  type: Support
  url: https://pagesnap.142-93-197-141.sslip.io/support
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/CalibratedGhosts
- group: operate
  title: ''
  type: StatusPage
  url: https://pagesnap.142-93-197-141.sslip.io/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://pagesnap.142-93-197-141.sslip.io/log
- group: start
  title: ''
  type: Sandbox
  url: https://pagesnap.142-93-197-141.sslip.io/playground
- group: build
  title: ''
  type: CLI
  url: cli/pagesnap-cli.yml
- group: build
  title: ''
  type: SDKs
  url: packages/pagesnap-packages.yml
- group: build
  title: ''
  type: Packages
  url: packages/pagesnap-packages.yml
- group: design
  title: ''
  type: Components
  url: components/pagesnap-components.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pagesnap-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/pagesnap-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/pagesnap-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pagesnap-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pagesnap-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pagesnap-conformance.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/pagesnap-sandbox.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pagesnap-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://pagesnap.142-93-197-141.sslip.io/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/pagesnap-security.txt
- group: auth
  title: ''
  type: Security
  url: security/pagesnap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pagesnap-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pagesnap-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pagesnap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pagesnap-authentication.yml
created: '2026-09-02'
description: 'Pagesnap turns any publicly reachable HTTP(S) URL into clean LLM-ready Markdown, a screenshot, a PDF, link-preview metadata, or normalized structured data, and extends the same engine to robots-aware site crawls, llms.txt generation, two-page diffs, and persisted change monitors with signed webhooks. The 66-operation REST API is described by a generated OpenAPI 3.1 contract and is callable anonymously at 30 requests/day with no signup, keyed at higher quota, or keylessly per call via x402 v2 exact USDC payments on Base. The same capabilities are projected through a hosted Streamable HTTP MCP server (11 tools, anonymous), an A2A 1.0 JSON-RPC agent with a JWS-signed agent card, and an Agentic Resource Discovery manifest. Pagesnap is an explicit experiment: it was designed, built, deployed, documented and is operated by AI coding agents within a scope set by a human owner who retains control of the single New York VPS and the self-custodied payment wallet. There is no SLA, no
  failover, and no compliance certification, and the service says so plainly on its own trust page.'
image: https://pagesnap.142-93-197-141.sslip.io/og/5d0796efe9a21e22c0375e43.png
layout: provider
mcp_servers:
- description: ''
  name: Pagesnap MCP Server
  slug: pagesnap-mcp-server
- description: ''
  name: Pagesnap MCP Server
  slug: pagesnap-mcp-server-2
modified: '2026-09-02'
name: Pagesnap
nav: Providers
network: true
overview: 'Pagesnap publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include developer-tools, web-scraping, web-to-markdown, screenshot-api, and pdf-generation.


  The Pagesnap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pagesnap''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, changelog, and 26 more developer resources.'
plans:
- name: Pagesnap Plans Pricing
  plan_count: 5
  slug: pagesnap-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 11
  name: Pagesnap Rate Limits
  slug: pagesnap-rate-limits
score:
  band: exemplar
  composite: 70.7
  coverage:
    artifact_dirs: 22
    catalog_gap: 54.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  facets:
    access_clarity: 84.2
    commercial_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 83.3
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 94.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 56.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
security:
- kind: authentication
  name: Pagesnap Authentication
  slug: pagesnap-authentication
  summary_line: apiKey/http · 4 schemes
- kind: domain-security
  name: Pagesnap Domain Security
  slug: pagesnap-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Pagesnap Vulnerability Disclosure
  slug: pagesnap-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Pagesnap Trust Center
  slug: pagesnap-trust-center
  summary_line: trust center published
slug: pagesnap
tags:
- developer-tools
- web-scraping
- web-to-markdown
- screenshot-api
- pdf-generation
- metadata-extraction
- mcp
- a2a
- x402
- ai-agents
- content-extraction
- structured-data
- web-crawling
- change-monitoring
- llms-txt
- agent-payments
- saas
website: https://pagesnap.142-93-197-141.sslip.io
---
