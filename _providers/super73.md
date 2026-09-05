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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 10.3
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'The agent-facing commerce API for the SUPER73 North American storefront. Implements the Universal Commerce Protocol (UCP) 2026-08-25 over MCP: a merchant profile at /.well-known/ucp declares the suppo'
  name: SUPER73 Agent Commerce (UCP/MCP)
  slug: super73-agent-commerce
- description: The Shopify Storefront GraphQL API served on SUPER73's own host. Anonymous introspection and anonymous read queries against SUPER73 catalog, collection, page, blog and shop data succeed with no access
  name: SUPER73 Storefront GraphQL API
  slug: super73-storefront-graphql
- description: The agent-facing commerce API for the European SUPER73 storefront, operated by SUPER73 BV on the super73europe Shopify store. Identical UCP 2026-08-25 / MCP surface to the North American store — the s
  name: SUPER73 BV Agent Commerce (UCP/MCP)
  slug: super73-eu-agent-commerce
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://super73.com/
- group: docs
  title: ''
  type: Documentation
  url: https://super73.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://super73.com/pages/support
- group: company
  title: ''
  type: Blog
  url: https://super73.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://super73.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://super73.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://super73.com/policies/privacy-policy
- group: agent
  title: ''
  type: WellKnown
  url: well-known/super73-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/super73-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/super73-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/super73-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/super73-plans-pricing.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/super73-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/super73-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/super73-llms.txt
- group: docs
  title: ''
  type: GraphQL
  url: graphql/super73-storefront-graphql.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/super73-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/super73-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/super73-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/super73-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/super73-data-model.yml
created: '2026-08-29'
description: 'SUPER73 (legally SUPER73, Inc., founded 2016 in Orange County, California as Lithium Cycles) is an American electric-bicycle and lifestyle adventure brand best known for its moped-styled Class 2 e-bikes — the S-Series, ZX, RX, R-Series Adventure and the 2026 A-Series with modular dual-battery technology. The company sells direct-to-consumer through Shopify storefronts in North America (super73.com) and Europe (eu.super73.com, operated by SUPER73 BV), and pairs its bikes with a mobile app that adds Bluetooth ride telemetry plus a cellular IoT upgrade for GPS tracking, movement alerts, digital bike passport and remote immobilizer. SUPER73 publishes no traditional developer program, but both storefronts expose a real, anonymous, machine-callable agent surface: an /llms.txt and /agents.md agent instruction document, a Universal Commerce Protocol (UCP 2026-08-25) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp serving 13 commerce tools with full JSON Schema,
  and an anonymously introspectable Shopify Storefront GraphQL API.'
image: https://super73.com/cdn/shop/files/Super73_Logo-Horizontal-Full-Tag_1200x628_ac39ec97-b650-40d2-b3d0-8c573b7fc9e7.jpg?v=1707761079
layout: provider
mcp_servers:
- description: 'SUPER73''s North American storefront exposes a hosted, remote MCP server implementing the Universal Commerce Protocol (UCP) shopping service. tools/list answers anonymously over plain JSON-RPC with 13 '
  name: SUPER73 Agent Commerce MCP Server
  slug: super73-agent-commerce-mcp-server
- description: The European SUPER73 storefront (operated by SUPER73 BV) exposes its own hosted remote MCP server implementing the same Universal Commerce Protocol shopping service as the North American store. tools/
  name: SUPER73 BV Agent Commerce MCP Server
  slug: super73-bv-agent-commerce-mcp-server
modified: '2026-08-29'
name: Super73
nav: Providers
network: true
overview: 'Super73 publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Electric Bikes, Micromobility, E-Commerce, Agentic Commerce, and Consumer Hardware.


  Super73''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Super73 Plans Pricing
  plan_count: 0
  slug: super73-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Super73 Rate Limits
  slug: super73-rate-limits
scopes:
- name: Super73 Scopes
  scope_count: 0
  slug: super73-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.0
    catalog_earned_first_party: 0.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/super73/refs/heads/main/screenshots/super73-2026-09-02T161213.png
security:
- kind: authentication
  name: Super73 Authentication
  slug: super73-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Super73 Domain Security
  slug: super73-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: super73
tags:
- Electric Bikes
- Micromobility
- E-Commerce
- Agentic Commerce
- Consumer Hardware
- MCP
- Universal Commerce Protocol
- Shopify
- Direct to Consumer
- Internet of Things
- Transportation
website: https://super73.com/
---
