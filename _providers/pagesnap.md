---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.0
  scored_at: '2026-09-16'
api_count: 1
apis:
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Keys, usage, referrals
  name: Pagesnap Account API
  slug: pagesnap-account-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: MCP and A2A protocols
  name: Pagesnap Agents API
  slug: pagesnap-agents-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Checkout and receipts
  name: Pagesnap Billing API
  slug: pagesnap-billing-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Reading and rendering
  name: Pagesnap Content API
  slug: pagesnap-content-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Site crawls and asynchronous jobs
  name: Pagesnap Crawl API
  slug: pagesnap-crawl-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Two-page comparison
  name: Pagesnap Diff API
  slug: pagesnap-diff-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Machine-readable discovery resources
  name: Pagesnap Discovery API
  slug: pagesnap-discovery-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Persisted change monitoring
  name: Pagesnap Monitors API
  slug: pagesnap-monitors-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Public health and stats
  name: Pagesnap Status API
  slug: pagesnap-status-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Capability-based support tickets
  name: Pagesnap Support API
  slug: pagesnap-support-api
- baseURL: https://pagesnap.142-93-197-141.sslip.io
  baseurl_source: declared
  description: Keyless USDC per-call payment
  name: Pagesnap X402 API
  slug: pagesnap-x402-api
artifact_total: 20
asyncapis:
- description: ''
  name: Pagesnap Webhooks
  slug: pagesnap-webhooks
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://pagesnap.142-93-197-141.sslip.io/mcp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/mcp/pagesnap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pagesnap-mcp.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/overlays/pagesnap-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/pagesnap-api-overlay.yaml
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
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/cli/pagesnap-cli.yml
  title: ''
  type: CLI
  url: cli/pagesnap-cli.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/packages/pagesnap-packages.yml
  title: ''
  type: SDKs
  url: packages/pagesnap-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/packages/pagesnap-packages.yml
  title: ''
  type: Packages
  url: packages/pagesnap-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/components/pagesnap-components.yml
  title: ''
  type: Components
  url: components/pagesnap-components.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/lifecycle/pagesnap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/pagesnap-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/lifecycle/pagesnap-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/pagesnap-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/changelog/pagesnap-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/pagesnap-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/plans/pagesnap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pagesnap-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/rate-limits/pagesnap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pagesnap-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/conformance/pagesnap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pagesnap-conformance.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/sandbox/pagesnap-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/pagesnap-sandbox.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/well-known/pagesnap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pagesnap-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://pagesnap.142-93-197-141.sslip.io/.well-known/api-catalog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/well-known/pagesnap-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/pagesnap-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/security/pagesnap-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/pagesnap-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/security/pagesnap-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/pagesnap-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/security/pagesnap-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/pagesnap-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/security/pagesnap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pagesnap-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/pagesnap/refs/heads/main/authentication/pagesnap-authentication.yml
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
overview: 'Pagesnap publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account API, Agents API, Billing API, and 8 more. Tagged areas include Developer Tools, Web Scraping, web-to-markdown, screenshot-api, and PDF Generation.


  The Pagesnap catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Pagesnap''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, support, changelog, and 29 more developer resources.'
plans:
- name: Pagesnap Plans Pricing
  plan_count: 5
  slug: pagesnap-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 11
  name: Pagesnap Rate Limits
  slug: pagesnap-rate-limits
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 22
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 4.3
  facets:
    access_clarity: 61.8
    contract_governance: 18.2
    contract_quality: 58.8
    developer_ergonomics: 58.3
    discoverability: 87.0
    operational_transparency: 76.3
  previous_composite: 57.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 50.0
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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
- Developer Tools
- Web Scraping
- web-to-markdown
- screenshot-api
- PDF Generation
- Metadata Extraction
- MCP
- A2A
- x402
- AI Agents
- Content Extraction
- Structured Data
- Web Crawling
- Change Monitoring
- llms-txt
- Agent Payments
- Software-as-a-Service
website: https://pagesnap.142-93-197-141.sslip.io
---
