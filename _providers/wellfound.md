---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.6
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Remote MCP server exposing a recruiter's inbound job applications to an agent, and letting it accept or reject them. Named "Wellfound recruiter applications" in its own RFC 9728 protected-resource doc
  name: Wellfound Applications MCP
  slug: wellfound-applications-mcp
- description: Remote MCP server for Wellfound Reach, the AI sourcing product. Seven scopes across four resources - projects:read, agents:read, agents:write, candidates:read, candidates:write, company_lists:read, co
  name: Wellfound Reach MCP
  slug: wellfound-reach-mcp
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://wellfound.com/
- group: operate
  title: ''
  type: Support
  url: https://help.wellfound.com/
- group: company
  title: ''
  type: Blog
  url: https://wellfound.com/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://wellfound.com/blog.rss
- group: commercial
  title: ''
  type: Pricing
  url: https://wellfound.com/recruit/pricing
- group: start
  title: ''
  type: SignUp
  url: https://wellfound.com/jobs/signup
- group: start
  title: ''
  type: Login
  url: https://wellfound.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wellfound.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wellfound.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wellfound.com/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.wellfound.ai/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/wellfound-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wellfound-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/wellfound-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/wellfound-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/wellfound-security.txt
- group: auth
  title: ''
  type: Security
  url: security/wellfound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wellfound-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wellfound-domain-security.yml
- group: auth
  title: ''
  type: Compliance
  url: security/wellfound-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wellfound-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wellfound-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/wellfound-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wellfound-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/wellfound-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wellfound-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/wellfound-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wellfound-llms.txt
created: '2026-09-04'
description: Wellfound (formerly AngelList Talent) is a startup hiring marketplace and AI recruiting platform operating wellfound.com, the Wellfound Reach AI sourcing product and the Autopilot managed-recruiting service. Its entire public machine-readable API surface is two OAuth-protected Model Context Protocol servers - https://wellfound.com/api/mcp for recruiter applications and https://reach.wellfound.com/mcp for Reach projects, sourcing agents, candidates and company lists - discovered from a complete RFC 8414 / RFC 9728 / OpenID Connect discovery stack and verified by probe. Wellfound publishes no OpenAPI document, no public GraphQL endpoint, no REST reference and no developer portal, so the discovery documents are the only published description of how to integrate.
image: https://reach.wellfound.com/assets/marketing/og/homepage-2fb80e2936cb06211fa7702e4b089510c772d1b887166b884b4720f73445e875.png
layout: provider
mcp_servers:
- description: ''
  name: Wellfound MCP servers
  slug: wellfound-mcp-servers
modified: '2026-09-04'
name: Wellfound
nav: Providers
network: true
overview: 'Wellfound publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Recruiting, Hiring, Talent, Human Resources, and Applicant Tracking.


  Wellfound''s developer surface includes support, engineering blog, pricing, signup flow, authentication, and 23 more developer resources.'
plans:
- name: Wellfound Plans Pricing
  plan_count: 0
  slug: wellfound-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Wellfound Rate Limits
  slug: wellfound-rate-limits
scopes:
- name: Wellfound Scopes
  scope_count: 0
  slug: wellfound-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 28.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
security:
- kind: authentication
  name: Wellfound Authentication
  slug: wellfound-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Wellfound Domain Security
  slug: wellfound-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wellfound Vulnerability Disclosure
  slug: wellfound-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Wellfound Trust Center
  slug: wellfound-trust-center
  summary_line: SOC 2
slug: wellfound
tags:
- Recruiting
- Hiring
- Talent
- Human Resources
- Applicant Tracking
- Job Board
- Startups
- MCP
- agent-native
- OAuth
- AI Sourcing
website: https://wellfound.com/
---
