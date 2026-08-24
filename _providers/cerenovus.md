---
access_model:
  confidence: high
  label: Contact Sales
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - https://www.cerenovus.ai/book-demo
  - https://www.cerenovus.ai/sitemap.xml
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://www.cerenovus.ai/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cerenovus-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cerenovus-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cerenovus-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/cerenovus-security.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/cerenovus-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cerenovus-scopes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cerenovus-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cerenovus-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/cerenovus-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cerenovus-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/cerenovus-plans-pricing.yml
- group: build
  title: ''
  type: Packages
  url: packages/cerenovus-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerenovus-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/cerenovus-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.cerenovus.ai/.well-known/security.txt
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.cerenovus.ai/trust-and-security
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cerenovus.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cerenovus.ai/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Cerenovus
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cerenovus-ai/
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Cerenovusai
- group: other
  title: ''
  type: CompanyProfile
  url: https://www.ycombinator.com/companies/cerenovus
- group: company
  title: ''
  type: Careers
  url: https://www.cerenovus.ai/careers
created: '2026-07-17'
description: Cerenovus Inc. (cerenovus.ai) is a San Francisco AI software company backed by Y Combinator (S26 batch). Cerenovus is both the company and the product — earlier product names have been retired, and Compendium is its internal workspace rather than a public offering. It reads the records an organization already produces (email, contracts, invoices, ledgers, tickets, calendars, meeting notes and documents), resolves the same customer, vendor or person across systems into one entity, runs deterministic scans for countable problems such as duplicate payments, dormant vendors and missed discount windows, then uses models to investigate what the scans surface and returns ranked findings with every claim cited back to the source record. It is sold as eight standalone engagements — operational due diligence, value creation plan, post-merger integration, exit readiness, operational diagnostic, decision intelligence, operational foresight and early warning, and spend and vendor intelligence
  — to enterprises, middle-market companies, private equity firms, consulting and advisory firms, and corporate development teams. Cerenovus publishes no developer portal, API reference or machine-readable specification; the only machine surface found is an undocumented, OAuth-protected remote MCP server at api.cerenovus.ai/mcp. Not affiliated with the similarly named Johnson & Johnson MedTech neurovascular device business.
image: https://www.cerenovus.ai/favicon-48.png
layout: provider
mcp_servers:
- description: ''
  name: Cerenovus MCP Server (remote, OAuth-protected)
  slug: cerenovus-mcp-server-remote-oauth-protected
modified: '2026-08-14'
name: Cerenovus
nav: Providers
network: true
overview: 'Cerenovus is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Enterprise Software, and Decision Intelligence.


  Cerenovus'' developer surface includes authentication and 23 more developer resources.'
plans:
- name: Cerenovus Plans Pricing
  plan_count: 0
  slug: cerenovus-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 0
  name: Cerenovus Rate Limits
  slug: cerenovus-rate-limits
scopes:
- name: Cerenovus Scopes
  scope_count: 9
  slug: cerenovus-scopes
  summary_line: 9 scopes · authorizationCode
score:
  band: emerging
  composite: 19.2
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 19.2
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cerenovus/refs/heads/main/screenshots/cerenovus-2026-07-25T204948.png
security:
- kind: authentication
  name: Cerenovus Authentication
  slug: cerenovus-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cerenovus Domain Security
  slug: cerenovus-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Cerenovus Vulnerability Disclosure
  slug: cerenovus-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Cerenovus Trust Center
  slug: cerenovus-trust-center
  summary_line: trust center published
slug: cerenovus
tags:
- Company
- Artificial Intelligence
- AI Agents
- Enterprise Software
- Decision Intelligence
- Knowledge-Management
- Private Equity
- Due Diligence
- MCP
- Y Combinator
website: https://www.cerenovus.ai/
---
