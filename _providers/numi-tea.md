---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
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
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 25.0
  scored_at: '2026-09-05'
api_count: 1
apis:
- description: Numi Tea's Universal Commerce Protocol shopping service, exposed over MCP at numitea.com/api/ucp/mcp. Thirteen tools cover catalog search and lookup, product detail, cart create/update/cancel, checkou
  name: Numi Tea UCP Shopping MCP
  slug: numi-tea-ucp-shopping-mcp
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://numitea.com/
- group: docs
  title: ''
  type: Documentation
  url: https://numitea.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/numi-tea-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/numi-tea-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/numi-tea-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/numi-tea-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/numi-tea-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/numi-tea-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/numi-tea-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/numi-tea-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/numi-tea-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/numi-tea-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/numi-tea-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/numi-tea-domain-security.yml
- group: operate
  title: ''
  type: Support
  url: https://numitea.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://numitea.com/pages/faq
- group: company
  title: ''
  type: Blog
  url: https://numitea.com/blogs/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://numitea.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://numitea.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://numitea.com/account/login
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/numi-tea-shop-and-checkout.md
- group: agent
  title: ''
  type: AgentSkill
  url: skills/numi-tea-catalog-research.md
created: '2026-08-26'
description: 'Numi Tea (Numi Organic Tea) is an Oakland, California social enterprise founded in 1999 by siblings Ahmed Rahim and Reem Hassani, selling premium organic and Fair Trade certified teas and herbal teasans built from real fruits, flowers, herbs and spices. It is a consumer packaged-goods company with no developer program, no API keys and no developer portal -- but its Shopify storefront at numitea.com serves a genuine, live agent-commerce surface: a Universal Commerce Protocol (UCP) MCP server at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools with full JSON Schema, a UCP discovery document pinned to protocol version 2026-04-08, RFC 8414/9728 OAuth metadata, OpenID Connect discovery on its own account host, and a substantive hand-written llms.txt and agents.md instructing AI shopping agents. Payment completion is explicitly fenced behind contemporaneous human approval.'
image: https://numitea.com/cdn/shop/files/group1200x628.jpg?v=1714413933
layout: provider
mcp_servers:
- description: ''
  name: Numi Tea MCP Server
  slug: numi-tea-mcp-server
modified: '2026-08-26'
name: Numi Tea
nav: Providers
network: true
overview: 'Numi Tea publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Tea, Beverages, Consumer Packaged Goods, Retail, and E-Commerce.


  Numi Tea''s developer surface includes documentation, authentication, support, engineering blog, signup flow, and 18 more developer resources.'
plans:
- name: Numi Tea Plans Pricing
  plan_count: 0
  slug: numi-tea-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Numi Tea Rate Limits
  slug: numi-tea-rate-limits
scopes:
- name: Numi Tea Scopes
  scope_count: 0
  slug: numi-tea-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 15
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
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 22.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/numi-tea/refs/heads/main/screenshots/numi-tea-2026-09-02T150814.png
security:
- kind: authentication
  name: Numi Tea Authentication
  slug: numi-tea-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Numi Tea Domain Security
  slug: numi-tea-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: numi-tea
tags:
- Tea
- Beverages
- Consumer Packaged Goods
- Retail
- E-Commerce
- Organic
- Fair Trade
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://numitea.com/
---
