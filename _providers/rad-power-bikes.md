---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Universal Commerce Protocol (UCP) shopping service for the Rad Power Bikes online store, exposed over MCP. Anonymous tools/list returns 13 tools covering catalog search and lookup, product detail,
  name: Rad Power Bikes UCP Commerce MCP
  slug: rad-power-bikes-ucp-commerce-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.radpowerbikes.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.radpowerbikes.com/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://www.radpowerbikes.com/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://www.radpowerbikes.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://www.radpowerbikes.com/blogs/the-scenic-route
- group: start
  title: ''
  type: SignUp
  url: https://www.radpowerbikes.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.radpowerbikes.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.radpowerbikes.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/rad-power-bikes-well-known.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/rad-power-bikes-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/rad-power-bikes-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rad-power-bikes-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-26'
description: 'Rad Power Bikes is a Seattle-based direct-to-consumer electric bicycle maker, selling cargo, utility, commuter and off-road ebikes plus parts, accessories and service plans through its own online store and a small network of RadRetail locations. The company filed for Chapter 11 in December 2025 and its assets were acquired by Life Electric Vehicles Holdings in March 2026; the store continues to operate at radpowerbikes.com. Rad Power Bikes publishes no developer program, no public REST OpenAPI and no partner API portal. It does, however, expose a real, anonymous, machine-readable agent commerce surface on its own domain: a Universal Commerce Protocol (UCP) discovery document at /.well-known/ucp, agent instructions at /agents.md and /llms.txt, and a live MCP endpoint at /api/ucp/mcp that answers tools/list without credentials with 13 catalog, cart, checkout and order tools. That surface is Shopify platform infrastructure, provisioned per-store and served from the merchant''s
  own hosts.'
image: https://cdn.shopify.com/s/files/1/0799/9645/files/RPB-logo-US_1af3a809-34a2-4783-bb7f-12074e8c0357.png?v=1626972856
layout: provider
mcp_servers:
- description: ''
  name: Rad Power Bikes UCP Commerce MCP
  slug: rad-power-bikes-ucp-commerce-mcp
modified: '2026-08-26'
name: Rad Power Bikes
nav: Providers
network: true
overview: 'Rad Power Bikes publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Electric Bikes, Micromobility, E-Commerce, and Retail.


  Rad Power Bikes'' developer surface includes documentation, getting-started guide, support, engineering blog, signup flow, and 8 more developer resources.'
plans:
- name: Rad Power Bikes Plans Pricing
  plan_count: 0
  slug: rad-power-bikes-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Rad Power Bikes Rate Limits
  slug: rad-power-bikes-rate-limits
scopes:
- name: Rad Power Bikes Scopes
  scope_count: 0
  slug: rad-power-bikes-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 19
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 42.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 25.1
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rad-power-bikes/refs/heads/main/screenshots/rad-power-bikes-2026-09-02T152746.png
security:
- kind: authentication
  name: Rad Power Bikes Authentication
  slug: rad-power-bikes-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rad Power Bikes Domain Security
  slug: rad-power-bikes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rad-power-bikes
tags:
- Company
- Electric Bikes
- Micromobility
- E-Commerce
- Retail
- Consumer Products
- Agentic Commerce
- Shopify
- MCP
- Universal Commerce Protocol
website: https://www.radpowerbikes.com/
---
