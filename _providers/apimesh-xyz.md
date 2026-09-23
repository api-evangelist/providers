---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.8
  scored_at: '2026-09-23'
api_count: 2
apis:
- baseURL: https://apimesh.xyz
  baseurl_source: declared
  description: 'The pay-per-call marketplace surface: one API per subdomain (https://{api-name}.apimesh.xyz) with free GET /health, GET / and GET /preview and paid /check, /analyze, /build, /generate, /validate and /'
  name: APIMesh Web Analysis APIs
  slug: apimesh-web-analysis-apis
- description: 'Live, free, unauthenticated endpoint behind the agentsmd wedge: POST /normalize accepts {source_format, content, targets} and returns {files, warnings, detected_formats}, converting between AGENTS.md,'
  name: agentsmd (agentcontext) API
  slug: agentsmd-agentcontext-api
- description: 'Live, free, unauthenticated endpoint behind the stripesig wedge: POST /check accepts {provider (stripe|github|slack|shopify), secret, raw_body, headers, tolerance_seconds?}, recomputes the provider''s '
  name: stripesig Webhook Signature Debugger API
  slug: stripesig-webhook-signature-debugger-api
- description: '@mbeato/apimesh-mcp-server (npm, v1.8.2, 2026-04-26; io.github.mbeato/apimesh in the official MCP registry) — a local stdio MCP server with 76 tools (74 web-analysis tools plus wallet_usage and wallet'
  name: APIMesh MCP Server
  slug: apimesh-mcp-server
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://apimesh.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/mbeato/APIMesh#readme
- group: docs
  title: ''
  type: APIReference
  url: https://apimesh.xyz/.well-known/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://github.com/mbeato/APIMesh#quick-start
- group: operate
  title: ''
  type: Support
  url: https://github.com/mbeato/APIMesh/issues
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mbeato
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/mbeato/APIMesh
- group: operate
  title: ''
  type: Roadmap
  url: https://github.com/mbeato/APIMesh/blob/main/.planning/ROADMAP.md
- group: commercial
  title: ''
  type: Pricing
  url: https://github.com/mbeato/APIMesh#all-apis
- group: start
  title: ''
  type: SignUp
  url: https://apimesh.xyz/signup
- group: start
  title: ''
  type: Login
  url: https://apimesh.xyz/login
- group: start
  title: ''
  type: Console
  url: https://apimesh.xyz/dashboard
- group: other
  title: ''
  type: Playground
  url: https://agentsmd.apimesh.xyz/
- group: other
  title: ''
  type: Playground
  url: https://stripesig.apimesh.xyz/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apimesh.xyz/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apimesh.xyz/legal/privacy
- group: commercial
  title: ''
  type: Legal
  url: https://apimesh.xyz/legal/acceptable-use
- group: commercial
  title: ''
  type: Legal
  url: https://apimesh.xyz/legal/refund
- group: commercial
  title: ''
  type: Legal
  url: https://apimesh.xyz/legal/cookies
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://apimesh.xyz/legal/privacy
- group: other
  title: ''
  type: NoticeAndAction
  url: https://apimesh.xyz/legal/abuse
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/a2a/apimesh-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/apimesh-xyz-a2a.yml
- group: other
  title: ''
  type: AgentCard
  url: https://apimesh.xyz/.well-known/agent-card.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/well-known/apimesh-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apimesh-xyz-well-known.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/llms/apimesh-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apimesh-xyz-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://apimesh.xyz/llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/mcp/apimesh-xyz-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apimesh-xyz-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/mcp/apimesh-xyz-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apimesh-xyz-tool-crosswalk.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/packages/apimesh-xyz-packages.yml
  title: ''
  type: Packages
  url: packages/apimesh-xyz-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/packages/apimesh-xyz-packages.yml
  title: ''
  type: SDKs
  url: packages/apimesh-xyz-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/cli/apimesh-xyz-cli.yml
  title: ''
  type: CLI
  url: cli/apimesh-xyz-cli.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/overlays/apimesh-xyz-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/apimesh-xyz-openapi-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/conformance/apimesh-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apimesh-xyz-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/errors/apimesh-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apimesh-xyz-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/lifecycle/apimesh-xyz-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apimesh-xyz-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/authentication/apimesh-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apimesh-xyz-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/security/apimesh-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apimesh-xyz-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/conventions/apimesh-xyz-conventions.yml
  title: ''
  type: Conventions
  url: conventions/apimesh-xyz-conventions.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/regulatory/apimesh-xyz-regulatory-posture.yml
  title: ''
  type: RegulatoryPosture
  url: regulatory/apimesh-xyz-regulatory-posture.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/changelog/apimesh-xyz-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/apimesh-xyz-changelog.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/plans/apimesh-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/apimesh-xyz-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/apimesh-xyz/refs/heads/main/rate-limits/apimesh-xyz-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/apimesh-xyz-rate-limits.yml
created: '2026-09-19'
description: 'APIMesh (apimesh.xyz) is a solo, MIT-licensed developer-tools project by Maximus Beato that launched in February 2026 as a pay-per-call web-analysis API marketplace — SEO audits, security headers, email verification, tech-stack detection and dozens of autonomously generated endpoints, each on its own subdomain and payable by x402 (USDC on Base), Stripe Machine Payments Protocol or prepaid API-key credits, with a 76-tool MCP server on npm. The marketplace was retired on 2026-05-11 and the domain now hosts two free "wedge" tools: agentsmd (normalize AGENTS.md, CLAUDE.md and other agent rules files via POST /normalize, a CLI and an MCP server) and stripesig (a webhook signature debugger for Stripe, GitHub, Slack and Shopify via POST /check). The A2A agent card, ai-plugin manifest, OpenAPI, llms.txt and x402/MPP discovery documents are still served and describe the retired surface.'
image: https://apimesh.xyz/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: APIMesh MCP Server
  slug: apimesh-mcp-server
- description: ''
  name: npm package (stdio)
  slug: npm-package-stdio
modified: '2026-09-19'
name: APIMesh
nav: Providers
network: true
overview: 'APIMesh publishes 1 API on the [APIs.io](https://apis.io/) network: Web Analysis APIs. Tagged areas include Web Analysis, SEO, Web Security, Email Verification, and Developer Tools.


  APIMesh''s developer surface includes documentation, API reference, getting-started guide, support, GitHub presence, pricing, signup flow, and 35 more developer resources.'
plans:
- name: Apimesh Xyz Plans Pricing
  plan_count: 2
  slug: apimesh-xyz-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 4
  name: Apimesh Xyz Rate Limits
  slug: apimesh-xyz-rate-limits
score:
  band: developing
  composite: 53.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 37.4
    developer_ergonomics: 66.7
    discoverability: 75.9
    operational_transparency: 57.9
  previous_composite: 53.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: authentication
  name: Apimesh Xyz Authentication
  slug: apimesh-xyz-authentication
  summary_line: apiKey/x402/mpp/none · 4 schemes
- kind: domain-security
  name: Apimesh Xyz Domain Security
  slug: apimesh-xyz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apimesh-xyz
tags:
- Web Analysis
- SEO
- Web Security
- Email Verification
- Developer Tools
- Micropayments
- x402
- MCP
- Agent-Native
- Webhook
- AI Coding Agents
- Open-Source
website: https://apimesh.xyz/
---
