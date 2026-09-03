---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: Nittei is MeetsMore's self-hosted calendar and scheduler server, written in Rust (Axum + SQLx + PostgreSQL) and published under the MIT licence. It exposes a multi-tenant REST API under /api/v1 coveri
  name: Nittei Scheduler API
  slug: nittei-scheduler-api
- description: use-ai is MeetsMore's open-source (BUSL-1.1) React client and Node/Bun server for letting an LLM drive a web application's own frontend. The server partially implements the AG-UI protocol over Socket.
  name: use-ai Server
  slug: use-ai-server
artifact_total: 8
asyncapis:
- description: ''
  name: Meetsmore Nittei Webhooks
  slug: meetsmore-nittei-webhooks
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/meetsmore/nittei/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://meetsmore.com/
- group: company
  title: ''
  type: Blog
  url: https://engineering.meetsmore.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/meetsmore
- group: commercial
  title: ''
  type: Pricing
  url: https://pro.meetsmore.com/guide/pricing
- group: start
  title: ''
  type: SignUp
  url: https://lp.meetsmore.com/lps/pro
- group: operate
  title: ''
  type: Support
  url: https://meetsmore-pro.zendesk.com/hc/ja
- group: commercial
  title: ''
  type: TermsOfService
  url: https://meetsmore.com/policies/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://meetsmore.com/policies/privacy
- group: build
  title: ''
  type: Packages
  url: packages/meetsmore-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/meetsmore-packages.yml
- group: design
  title: ''
  type: Components
  url: components/meetsmore-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/meetsmore-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/meetsmore-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/meetsmore-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/meetsmore-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/meetsmore-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/meetsmore-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/meetsmore-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/meetsmore-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/meetsmore-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/meetsmore-nittei-webhooks.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/meetsmore-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/meetsmore-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/meetsmore-domain-security.yml
created: '2026-08-25'
description: MeetsMore Inc. (株式会社ミツモア) operates Japan's largest local-services marketplace, matching consumers and businesses with vetted professionals across 600+ categories — house cleaning, appliance installation, moving, renovation, pest control, photography, tax accountants and administrative scriveners — alongside ProOne, a cloud operations system for short-term construction contractors, and Hatchoo, an enterprise procurement platform built on the same contractor network. Founded February 2017 and headquartered in Ginza, Tokyo, the company reports 77,000+ registered service providers and passed a cumulative five million service requests in 2024. MeetsMore runs no public developer program for the marketplace itself and its production backend (api.meetsmore.com) is a closed AWS API Gateway; its public API surface is instead two first-party open-source products published from its own GitHub organization — Nittei, a self-hosted Rust calendar/scheduler API server with a utoipa-generated
  OpenAPI document, and use-ai, an AG-UI/MCP React framework distributed as four npm packages.
image: https://avatars.githubusercontent.com/u/27227297?v=4
layout: provider
mcp_servers:
- description: ''
  name: MeetsMore MCP Server
  slug: meetsmore-mcp-server
modified: '2026-08-25'
name: MeetsMore
nav: Providers
network: true
overview: 'MeetsMore publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Local Services, Home Services, and Japan.


  The MeetsMore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MeetsMore''s developer surface includes engineering blog, pricing, signup flow, support, changelog, authentication, and 19 more developer resources.'
plans:
- name: Meetsmore Plans Pricing
  plan_count: 3
  slug: meetsmore-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Meetsmore Rate Limits
  slug: meetsmore-rate-limits
score:
  band: developing
  composite: 47.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 47.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 47.6
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/meetsmore/refs/heads/main/screenshots/meetsmore-2026-09-02T150511.png
security:
- kind: authentication
  name: Meetsmore Authentication
  slug: meetsmore-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Meetsmore Domain Security
  slug: meetsmore-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meetsmore
tags:
- Company
- Marketplace
- Local Services
- Home Services
- Japan
- Scheduling
- Calendar
- Booking
- Field Service
- Open-Source
- Artificial Intelligence
- Agents
website: https://meetsmore.com/
---
