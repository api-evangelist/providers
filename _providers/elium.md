---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Elium's single GraphQL endpoint, served per tenant at https://{platform}.elium.com/graphql. 17 queries, 206 mutations and 18 subscriptions over 1128 type definitions, covering stories (content), space
  name: Elium GraphQL API
  slug: elium-graphql-api
- description: A remote Model Context Protocol server, announced 3 June 2026, served per tenant at https://{platform}.elium.com/services/mcp with OAuth 2.0 authorization and optional Dynamic Client Registration. Thr
  name: Elium MCP Server
  slug: elium-mcp-server
artifact_total: 11
asyncapis:
- description: ''
  name: Elium Events
  slug: elium-events
common:
- group: company
  title: ''
  type: Website
  url: https://elium.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.elium.com/en/api/
- group: docs
  title: ''
  type: Documentation
  url: https://learn.elium.com/en/api/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.elium.com/reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.elium.com/en/api/getting_started/quick_start
- group: operate
  title: ''
  type: Support
  url: https://help.elium.com/en/
- group: company
  title: ''
  type: Blog
  url: https://elium.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://elium.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://elium.com/free-trial
- group: start
  title: ''
  type: Login
  url: https://elium.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://elium.com/legal/website-terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elium.com/legal/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.elium.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://elium.com/changelog
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/elium-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://elium.com/trust/controls
- group: auth
  title: ''
  type: Compliance
  url: https://elium.com/trust
- group: agent
  title: ''
  type: MCPServer
  url: mcp/elium-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/elium-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/elium-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/elium-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/elium-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/elium-error-codes.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/elium-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/elium-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/elium-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/elium-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/elium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/elium-rate-limits.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/elium-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/elium-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elium-domain-security.yml
created: '2026-08-17'
description: 'Elium is a European enterprise knowledge-management SaaS platform, founded in 2007 as Knowledge Plaza and renamed Elium in 2017, headquartered in Louvain-la-Neuve, Belgium. Teams capture, validate and govern company knowledge as structured articles - which Elium calls "stories" - inside spaces, using templates, multi-step approval, expiration management, duplicate and gap detection, and in-place multilingual translation. The same governed corpus is then served to people and to AI agents through AI search, smart assistants, external portals and integrations. Programmatically Elium is a GraphQL provider, not a REST one: each customer platform serves its own per-tenant GraphQL endpoint with 17 queries, 206 mutations and 18 subscriptions, documented in a fully published SpectaQL reference, secured with OAuth 2.0 on a single apiv1 scope. In June 2026 Elium added a per-tenant remote Model Context Protocol server exposing three read-only knowledge tools to ChatGPT, Claude and custom
  agents. API and MCP access are Enterprise-plan only. Elium is ISO/IEC 27001:2022 certified and SecNumCloud-qualified, with EU-default and sovereign French hosting options.'
image: https://elium.com/logos/elium-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Elium MCP Server
  slug: elium-mcp-server
modified: '2026-08-17'
name: Elium
nav: Providers
network: true
overview: 'Elium publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Knowledge-Management, Knowledge Base, and Enterprise Search.


  The Elium catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Elium''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Elium Plans Pricing
  plan_count: 3
  slug: elium-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Elium Rate Limits
  slug: elium-rate-limits
scopes:
- name: Elium Scopes
  scope_count: 1
  slug: elium-scopes
  summary_line: 1 scope · authorizationCode/password
score:
  band: developing
  composite: 51.1
  coverage:
    artifact_dirs: 19
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 92.1
    commercial_clarity: 92.1
    contract_governance: 18.2
    contract_quality: 42.7
    developer_ergonomics: 33.9
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 42.1
  previous_composite: 51.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Elium Authentication
  slug: elium-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Elium Domain Security
  slug: elium-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Elium Vulnerability Disclosure
  slug: elium-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Elium Trust Center
  slug: elium-trust-center
  summary_line: ISO/IEC 27001:2022, SecNumCloud, GDPR, EU AI Act, EcoVadis Silver
slug: elium
tags:
- Company
- Software-as-a-Service
- Knowledge-Management
- Knowledge Base
- Enterprise Search
- AI Search
- GraphQL
- MCP
- Collaboration
- Documentation
- RAG
- Europe
website: https://elium.com/
---
