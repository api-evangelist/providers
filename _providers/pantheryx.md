---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    error_semantics: false
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
  score: 22.2
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The Relesium direct-to-consumer storefront (a PanTheryx consumer brand, named on pantheryx.com/consumer-brands/) exposes a Universal Commerce Protocol shopping service over MCP. An anonymous POST of t
  name: Relesium Agentic Commerce (UCP / MCP)
  slug: relesium-agentic-commerce-ucp-mcp
- description: The Life's First Naturals storefront (a PanTheryx consumer brand; its UCP profile resolves to the Shopify shop handle pantheryxlfn.myshopify.com, which confirms PanTheryx ownership) exposes the same U
  name: Life's First Naturals Agentic Commerce (UCP / MCP)
  slug: lifes-first-naturals-agentic-commerce-ucp-mcp
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://pantheryx.com/
- group: company
  title: ''
  type: Blog
  url: https://pantheryx.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://pantheryx.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pantheryx.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pantheryx.com/terms-and-conditions/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/pantheryx-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/pantheryx-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/pantheryx-relesium-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/pantheryx-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pantheryx-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/pantheryx-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/pantheryx-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/pantheryx-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/pantheryx-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pantheryx-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/pantheryx-scopes.yml
created: '2026-08-26'
description: 'PanTheryx, Inc. is a Boulder, Colorado nutrition and biotechnology company, founded in 2007, that commercializes bovine colostrum-based products for human and animal health. Its proprietary ColostrumOne ingredient underpins DiaResQ, a Food for Special Dietary Use for acute infectious diarrhea, alongside the consumer brands Relesium, Life''s First Naturals and TruBiotics (acquired from Bayer HealthCare). PanTheryx sells physical nutrition products and publishes no developer program, OpenAPI, SDK or API reference of any kind; its corporate site is a WordPress marketing and news property. It does, however, operate two Shopify-hosted direct-to-consumer storefronts that expose a live, anonymous agentic-commerce surface: both relesium.com and lifesfirstnaturals.com serve an llms.txt, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and a working MCP endpoint at /api/ucp/mcp answering tools/list with 13 catalog, cart, checkout and order tools.'
image: https://pantheryx.com/wp-content/uploads/2020/08/logo.svg
layout: provider
mcp_servers:
- description: ''
  name: Relesium Universal Commerce Protocol shopping service (MCP)
  slug: relesium-universal-commerce-protocol-shopping-service-mcp
- description: ''
  name: Life's First Naturals Universal Commerce Protocol shopping service (MCP)
  slug: lifes-first-naturals-universal-commerce-protocol-shopping-service-mcp
modified: '2026-08-26'
name: PanTheryx
nav: Providers
network: true
overview: 'PanTheryx publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Nutrition, Biotechnology, Life Sciences, and Consumer Health.


  PanTheryx''s developer surface includes engineering blog, support, authentication, and 14 more developer resources.'
plans:
- name: Pantheryx Plans Pricing
  plan_count: 0
  slug: pantheryx-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 0
  name: Pantheryx Rate Limits
  slug: pantheryx-rate-limits
scopes:
- name: Pantheryx Scopes
  scope_count: 0
  slug: pantheryx-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 20.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 52.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pantheryx/refs/heads/main/screenshots/pantheryx-2026-09-02T150905.png
security:
- kind: authentication
  name: Pantheryx Authentication
  slug: pantheryx-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Pantheryx Domain Security
  slug: pantheryx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: pantheryx
tags:
- Company
- Nutrition
- Biotechnology
- Life Sciences
- Consumer Health
- Dietary Supplements
- Colostrum
- Animal Health
- E-Commerce
- Agentic Commerce
website: https://pantheryx.com/
---
