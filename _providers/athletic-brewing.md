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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 16.4
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: The Universal Commerce Protocol shopping service Athletic Brewing's Shopify storefront serves at https://athleticbrewing.com/api/ucp/mcp. An anonymous MCP (JSON-RPC 2.0) endpoint exposing thirteen too
  name: Athletic Brewing UCP Commerce (MCP)
  slug: athletic-brewing-ucp-commerce-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://athleticbrewing.com/
- group: docs
  title: ''
  type: Documentation
  url: https://athleticbrewing.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://help.athleticbrewing.com/en-US
- group: company
  title: ''
  type: Blog
  url: https://athleticbrewing.com/blogs/news
- group: company
  title: ''
  type: BlogRSS
  url: https://athleticbrewing.com/blogs/news.atom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://athleticbrewing.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://athleticbrewing.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://athleticbrewing.com/account/login
- group: agent
  title: ''
  type: MCPServer
  url: mcp/athletic-brewing-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/athletic-brewing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/athletic-brewing-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/athletic-brewing-authentication.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/athletic-brewing-openid-configuration.json
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/athletic-brewing-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/athletic-brewing-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/athletic-brewing-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/athletic-brewing-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/athletic-brewing-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/athletic-brewing-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/athletic-brewing-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/athletic-brewing-domain-security.yml
created: '2026-08-06'
description: 'Athletic Brewing Company is a Milford, Connecticut brewer of craft non-alcoholic beer, founded in 2017 by Bill Shufelt and John Walker, selling direct-to-consumer across the United States alongside national retail distribution. Athletic Brewing is not a software company and publishes no developer program, but its Shopify-hosted storefront at athleticbrewing.com exposes a real, anonymous, machine-readable agent commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live MCP endpoint at /api/ucp/mcp serving thirteen catalog, cart, checkout and order tools with full JSON Schema, an OpenID Connect discovery document for Shopify customer accounts, and a published /llms.txt and /agents.md that document the agent flow and its buyer-approval rules.'
image: https://athleticbrewing.com/cdn/shop/files/Athletic-Brewing-Company-Non-Alcoholic-Beer.png?v=1667574176
layout: provider
mcp_servers:
- description: 'Athletic Brewing''s Shopify storefront serves a live, anonymous Model Context Protocol endpoint implementing the Universal Commerce Protocol (UCP) dev.ucp.shopping service. Discovered from the store''s '
  name: Athletic Brewing UCP Commerce MCP Server
  slug: athletic-brewing-ucp-commerce-mcp-server
modified: '2026-08-06'
name: Athletic Brewing
nav: Providers
network: true
overview: 'Athletic Brewing publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Non-Alcoholic Beer, Beverage, Consumer Packaged Goods, and Direct to Consumer.


  Athletic Brewing''s developer surface includes documentation, support, engineering blog, authentication, and 18 more developer resources.'
random_paper: 3
rate_limits:
- limit_count: 0
  name: Athletic Brewing Rate Limits
  slug: athletic-brewing-rate-limits
scopes:
- name: Athletic Brewing Scopes
  scope_count: 0
  slug: athletic-brewing-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 21.4
  coverage:
    artifact_dirs: 14
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 21.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/athletic-brewing/refs/heads/main/screenshots/athletic-brewing-2026-08-07T161840.png
security:
- kind: authentication
  name: Athletic Brewing Authentication
  slug: athletic-brewing-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Athletic Brewing Domain Security
  slug: athletic-brewing-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: athletic-brewing
tags:
- Company
- Non-Alcoholic Beer
- Beverage
- Consumer Packaged Goods
- Direct to Consumer
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://athleticbrewing.com/
---
