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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 26.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Nittei is MeetsMore's self-hosted calendar and scheduler server, written in Rust (Axum + SQLx + PostgreSQL) and published under the MIT licence. It exposes a multi-tenant REST API under /api/v1 coveri
  name: Nittei Scheduler API
  slug: nittei-scheduler-api
- description: use-ai is MeetsMore's open-source (BUSL-1.1) React client and Node/Bun server for letting an LLM drive a web application's own frontend. The server partially implements the AG-UI protocol over Socket.
  name: use-ai Server
  slug: use-ai-server
artifact_total: 10
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
  href: https://artifacts.apis.io/meetsmore/packages/meetsmore-packages.yml
  title: ''
  type: Packages
  url: packages/meetsmore-packages.yml
- group: build
  href: https://artifacts.apis.io/meetsmore/packages/meetsmore-packages.yml
  title: ''
  type: SDKs
  url: packages/meetsmore-packages.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/components/meetsmore-components.yml
  title: ''
  type: Components
  url: components/meetsmore-components.yml
- group: agent
  href: https://artifacts.apis.io/meetsmore/mcp/meetsmore-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/meetsmore-mcp.yml
- group: agent
  href: https://artifacts.apis.io/meetsmore/llms/meetsmore-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/meetsmore-llms.txt
- group: design
  href: https://artifacts.apis.io/meetsmore/conformance/meetsmore-conformance.yml
  title: ''
  type: Conformance
  url: conformance/meetsmore-conformance.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/lifecycle/meetsmore-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/meetsmore-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/meetsmore/changelog/meetsmore-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/meetsmore-changelog.yml
- group: auth
  href: https://artifacts.apis.io/meetsmore/authentication/meetsmore-authentication.yml
  title: ''
  type: Authentication
  url: authentication/meetsmore-authentication.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/conventions/meetsmore-conventions.yml
  title: ''
  type: Conventions
  url: conventions/meetsmore-conventions.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/errors/meetsmore-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/meetsmore-problem-types.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/data-model/meetsmore-data-model.yml
  title: ''
  type: DataModel
  url: data-model/meetsmore-data-model.yml
- group: design
  href: https://artifacts.apis.io/meetsmore/asyncapi/meetsmore-nittei-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/meetsmore-nittei-webhooks.yml
- group: commercial
  href: https://artifacts.apis.io/meetsmore/plans/meetsmore-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meetsmore-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/meetsmore/rate-limits/meetsmore-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/meetsmore-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/meetsmore/security/meetsmore-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meetsmore-domain-security.yml
created: '2026-08-25'
description: MeetsMore Inc. (株式会社ミツモア) operates Japan's largest local-services marketplace, matching consumers and businesses with vetted professionals across 600+ categories — house cleaning, appliance installation, moving, renovation, pest control, photography, tax accountants and administrative scriveners — alongside ProOne, a cloud operations system for short-term construction contractors, and Hatchoo, an enterprise procurement platform built on the same contractor network. Founded February 2017 and headquartered in Ginza, Tokyo, the company reports 77,000+ registered service providers and passed a cumulative five million service requests in 2024. MeetsMore runs no public developer program for the marketplace itself and its production backend (api.meetsmore.com) is a closed AWS API Gateway; its public API surface is instead two first-party open-source products published from its own GitHub organization — Nittei, a self-hosted Rust calendar/scheduler API server with a utoipa-generated
  OpenAPI document, and use-ai, an AG-UI/MCP React framework distributed as four npm packages.
finops:
- has_sources: true
  method: derived
  name: Meetsmore Finops
  primary_unit: 成約金額
  service_category: ''
  slug: meetsmore-finops
  template: false
image: https://avatars.githubusercontent.com/u/27227297?v=4
layout: provider
mcp_servers:
- description: ''
  name: MeetsMore MCP Server
  slug: meetsmore-mcp-yml
modified: '2026-08-25'
name: MeetsMore
nav: Providers
network: true
overview: 'MeetsMore is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Marketplace, Local Services, Home Services, and Japan.


  The MeetsMore catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  MeetsMore''s developer surface includes engineering blog, pricing, signup flow, support, changelog, authentication, and 19 more developer resources.'
plans:
- name: Meetsmore Plans Pricing
  plan_count: 12
  slug: meetsmore-plans-pricing
- name: Meetsmore Price Estimates
  plan_count: 0
  slug: meetsmore-price-estimates
random_paper: 17
rate_limits:
- limit_count: 0
  name: Meetsmore Rate Limits
  slug: meetsmore-rate-limits
score:
  band: developing
  composite: 49.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.6
  facets:
    access_clarity: 84.2
    contract_governance: 18.2
    contract_quality: 39.0
    developer_ergonomics: 47.6
    discoverability: 65.0
    operational_transparency: 28.9
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - japan
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - japan-korea
  previous_composite: 48.1
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/meetsmore/meetsmore-2026-09-02T150511.png
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
- Field Service Management
- Open Source
- Artificial Intelligence
- Agents
website: https://meetsmore.com/
---
