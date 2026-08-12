---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-11'
api_count: 3
apis:
- description: RESTful API over HTTPS covering all 1Lookup products (phone/email/IP validation, fraud, enrichment, B2B data, SEO intelligence). API-key Bearer auth, JSON bodies, job-based bulk processing. Roughly 47
  name: 1Lookup REST API
  slug: 1lookup-rest-api
- description: First-party hosted/remote MCP connector with OAuth 2.1 auth (authorization code + PKCE, dynamic client registration, single `lookup` scope) exposing 5 tools (validate_phone, verify_email, ip_lookup, b
  name: 1Lookup MCP Server
  slug: 1lookup-mcp-server
- description: Machine-readable content indexes (llms.txt and llms-full.txt) for AI and answer engines, indexing the free tools, every product page, the comparison pages and the key site sections.
  name: 1Lookup LLMs Index
  slug: 1lookup-llms-index
artifact_total: 12
common:
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.1lookup.io/api
- group: docs
  title: ''
  type: Documentation
  url: https://app.1lookup.io/api
- group: docs
  title: ''
  type: APIReference
  url: https://app.1lookup.io/api#endpoints
- group: start
  title: ''
  type: GettingStarted
  url: https://app.1lookup.io/api#getting-started
- group: company
  title: ''
  type: Website
  url: https://www.1lookup.io
- group: company
  title: ''
  type: Blog
  url: https://www.1lookup.io/blog
- group: operate
  title: ''
  type: Support
  url: https://www.1lookup.io/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://www.1lookup.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.1lookup.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.1lookup.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1lookup.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1lookup.io/privacy
- group: operate
  title: ''
  type: FAQ
  url: https://www.1lookup.io/faq
- group: other
  title: ''
  type: Glossary
  url: https://www.1lookup.io/glossary
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/1lookup
- group: company
  title: ''
  type: Twitter
  url: https://x.com/1LookupApp
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@1LookupApp
- group: auth
  title: ''
  type: Authentication
  url: authentication/1lookup-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1lookup-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1lookup-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1lookup-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1lookup-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/1lookup-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1lookup-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1lookup-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.1lookup.io/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/1lookup-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.1lookup.io/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/1lookup-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1lookup-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1lookup-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/1lookup-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/1lookup-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1lookup-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/1lookup-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1lookup-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-08'
description: 1Lookup is a self-serve data verification and enrichment platform for SMBs, exposing more than forty products through a single REST API and one universal credit balance. It validates phone numbers (line type, carrier, HLR reachability, number portability, DNC status, spam/scam reputation, fraud score), email addresses (syntax, MX, deliverability, disposable and role-based detection) and IP addresses (geolocation, VPN/proxy/Tor and datacenter detection), then extends into B2B company and contact data (firmographics, prospect and account search, contact append, skip trace), SEO and web intelligence (domain authority, backlinks, keyword metrics, audience reports, SERP and website scraping), social and media lookups, property data and audio transcription. The same engine powers a web dashboard with batch CSV validation, roughly twenty-five free rate-limited browser tools, and a first-party hosted MCP connector authorized with OAuth 2.1 that gives AI agents five of the core tools
  without an API key.
image: https://www.1lookup.io/images/featured/pages/homepage.png
layout: provider
mcp_servers:
- description: ''
  name: mcp
  slug: mcp
- description: ''
  name: 1lookup-mcp.yml
  slug: 1lookup-mcpyml
modified: '2026-08-09'
name: 1Lookup
nav: Providers
network: true
overview: '1Lookup publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include phone validation, email validation, IP intelligence, fraud & risk, and data enrichment.


  1Lookup''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 30 more developer resources.'
plans:
- name: 1Lookup Plans Pricing
  plan_count: 5
  slug: 1lookup-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: 1Lookup Rate Limits
  slug: 1lookup-rate-limits
scopes:
- name: 1Lookup Scopes
  scope_count: 1
  slug: 1lookup-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 47.1
  delta: -1.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 92.6
    governance: 12.5
    operational_transparency: 31.6
  previous_composite: 48.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
security:
- kind: authentication
  name: 1Lookup Authentication
  slug: 1lookup-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: 1Lookup Domain Security
  slug: 1lookup-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: 1Lookup Vulnerability Disclosure
  slug: 1lookup-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: 1Lookup Trust Center
  slug: 1lookup-trust-center
  summary_line: trust center published
slug: 1lookup
tags:
- phone validation
- email validation
- IP intelligence
- fraud & risk
- data enrichment
- B2B contact & company data
- SEO / web analytics
- audio transcription
- MCP / agent-native
- REST API
website: https://www.1lookup.io
---
