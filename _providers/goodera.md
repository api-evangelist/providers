---
agent_readiness:
  band: agent-ready
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
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.5
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: REST API for volunteering partners to list Goodera volunteer opportunities inside their own platform, create volunteering events against an opportunity, register and de-register volunteers, and record
  name: Goodera Developer API
  slug: goodera-developer-api
- description: Remote Model Context Protocol server announced as the first from a social impact company, exposing live Goodera volunteering data to AI agents and LLM workflows. Streamable HTTP transport at https://m
  name: Goodera MCP Server
  slug: goodera-mcp
artifact_total: 8
asyncapis:
- description: ''
  name: Goodera Webhooks
  slug: goodera-webhooks
common:
- group: company
  title: ''
  type: Website
  url: https://www.goodera.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.goodera.com/resources/api
- group: docs
  title: ''
  type: Documentation
  url: https://www.goodera.com/resources/api
- group: company
  title: ''
  type: Blog
  url: https://www.goodera.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.goodera.com/pages/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.goodera.com/pages/privacy
- group: operate
  title: ''
  type: Support
  url: https://www.goodera.com/about/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://app.goodera.com/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/goodera-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/goodera-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/goodera-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/goodera-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/goodera-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/goodera-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/goodera-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/goodera-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/goodera-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/goodera-packages.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/goodera-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/goodera-webhooks.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/goodera-domain-security.yml
created: '2026-08-22'
description: Goodera is a B2B SaaS corporate volunteering and social impact platform that curates, hosts and manages employee volunteering programs for enterprises, working with a stated 50,000+ vetted nonprofit partners across 100+ countries in virtual, in-person, outdoor and in-office formats. For integrators it publishes a REST Developer API at developer-api.goodera.com covering volunteering opportunities, event creation, registrations and participation/hours tracking, authenticated with an x-api-key header, and it operates a remote Model Context Protocol server at mcp.goodera.com that exposes 19 anonymous-readable tools over the same events, clients, champions, activities, opportunities and master-data domains.
image: https://cdn.prod.website-files.com/62dadf7d66e2fb7047b69c6d/65709f96a6e543204c638376_Home%20opengraph.webp
layout: provider
mcp_servers:
- description: Remote Model Context Protocol server operated by Goodera. Announced on the Goodera blog as the first MCP server from a social impact company, bringing real-time volunteering data to AI agents and LLM-
  name: Goodera MCP Server
  slug: goodera-mcp-server
modified: '2026-08-22'
name: Goodera
nav: Providers
network: true
overview: 'Goodera publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Corporate Volunteering, Social Impact, CSR, and Employee Engagement.


  The Goodera catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Goodera''s developer surface includes API reference, documentation, engineering blog, support, signup flow, authentication, and 16 more developer resources.'
plans:
- name: Goodera Plans Pricing
  plan_count: 0
  slug: goodera-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Goodera Rate Limits
  slug: goodera-rate-limits
score:
  band: thin
  composite: 34.2
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.3
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 7.9
  previous_composite: 34.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Goodera Authentication
  slug: goodera-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Goodera Domain Security
  slug: goodera-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: goodera
tags:
- Company
- Corporate Volunteering
- Social Impact
- CSR
- Employee Engagement
- Non-Profit
- Event
- Volunteering
- ESG
- MCP
website: https://www.goodera.com/
---
