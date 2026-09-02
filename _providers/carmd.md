---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.4
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: CarMD's vehicle API (marketed as CarScan) provides access to OBD-II code definitions, vehicle images, repair information and predicted upcoming issues. Registration issues credentials that are sent on
  name: CarMD Vehicle API
  slug: carmd
- description: 'Live Model Context Protocol endpoint on CarMD''s own domain, implementing the Universal Commerce Protocol (version 2026-04-08, with 2026-01-23 still served). Probed anonymously on 2026-08-27: initializ'
  name: CarMD Agentic Commerce API (UCP MCP)
  slug: carmd-agentic-commerce
- description: 'The Shopify-provided Storefront GraphQL API served on carmd.com, version 2026-04. Anonymous introspection on 2026-08-27 returned a 424-type schema (262 objects, 34 query fields, 41 mutations), and an '
  name: CarMD Storefront GraphQL API
  slug: carmd-storefront-graphql
artifact_total: 11
collections:
- collection_type: open
  name: API Collection
  slug: open-carmd
common:
- group: company
  title: ''
  type: Website
  url: https://carmd.com/
- group: company
  title: ''
  type: Blog
  url: https://carmd.com/pages/blog-homepage
- group: operate
  title: ''
  type: Support
  url: https://carmd.com/pages/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://carmd.com/pages/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://carmd.com/pages/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/carmd-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/carmd-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/carmd-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/carmd-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/carmd-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/carmd-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/carmd-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/carmd-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/carmd-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/carmd-packages.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/carmd-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/carmd-rate-limits.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carmd-domain-security.yml
created: '2024-03-30'
description: 'CarMD specializes in automotive diagnostics and insights, selling the CarMD Connect vehicle-health device and publishing the CarMD Vehicle Health Index. Its developer story has two very different halves today. The historic CarMD Vehicle API (CarScan) — code definitions, vehicle images, repair and upcoming-issue prediction — is documented at api.carmd.com and still linked from the carmd.com footer, but that host refused TCP connections on ports 80 and 443 when probed on 2026-08-27, and the old carmd.com/api pricing page now returns 404. Meanwhile the rebuilt carmd.com storefront serves a live, anonymous agent surface: an llms.txt, a Universal Commerce Protocol merchant profile, a working MCP endpoint with thirteen commerce tools, and an anonymously introspectable Storefront GraphQL API.'
finops:
- name: Carmd Finops
  service_category: API
  slug: carmd-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carmd.png
layout: provider
mcp_servers:
- description: 'CarMD serves a live, anonymous Model Context Protocol endpoint on its own domain at https://carmd.com/api/ucp/mcp. It is the Shopify-provided Universal Commerce Protocol (UCP) commerce server for the '
  name: CarMD Universal Commerce (UCP) MCP Server
  slug: carmd-universal-commerce-ucp-mcp-server
modified: '2026-08-27'
name: CarMD
nav: Providers
network: true
overview: 'CarMD publishes 1 API on the [APIs.io](https://apis.io/) network: Vehicle API. Tagged areas include Automobiles, Cars, Diagnostics, Vehicles, and Automotive.


  CarMD''s developer surface includes engineering blog, support, authentication, and 16 more developer resources.'
plans:
- name: Carmd Plans Pricing
  plan_count: 0
  slug: carmd-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Carmd Rate Limits
  slug: carmd-rate-limits
scopes:
- name: Carmd Scopes
  scope_count: 0
  slug: carmd-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 33.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 1.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 41.5
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carmd/refs/heads/main/screenshots/carmd-2026-06-20T174011.png
security:
- kind: authentication
  name: Carmd Authentication
  slug: carmd-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Carmd Domain Security
  slug: carmd-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: carmd
tags:
- Automobiles
- Cars
- Diagnostics
- Vehicles
- Automotive
- OBD-II
- Agentic Commerce
- MCP
- E-Commerce
website: https://carmd.com/
---
