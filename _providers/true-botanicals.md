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
    error_semantics: documented
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
  score: 21.4
  scored_at: '2026-09-03'
api_count: 2
apis:
- description: The Universal Commerce Protocol shopping service True Botanicals serves at its own domain. A POST to /api/ucp/mcp answers an unauthenticated MCP tools/list with 13 tools — search_catalog, lookup_catal
  name: True Botanicals UCP Agent Commerce (MCP)
  slug: true-botanicals-ucp-agent-commerce-mcp
- description: 'The Shopify Storefront GraphQL API as served on True Botanicals'' own domain. Introspection and catalog queries answered keyless on 2026-08-30 (424 types; shop.name returned "True Botanicals"), so the '
  name: True Botanicals Storefront GraphQL (Shopify)
  slug: true-botanicals-storefront-graphql-shopify
artifact_total: 8
common:
- group: company
  title: ''
  type: Website
  url: https://truebotanicals.com/
- group: docs
  title: ''
  type: Documentation
  url: https://truebotanicals.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://truebotanicals.com/pages/contact-us
- group: start
  title: ''
  type: Login
  url: https://truebotanicals.com/account/login
- group: company
  title: ''
  type: Blog
  url: https://truebotanicals.com/blogs/news
- group: commercial
  title: ''
  type: TermsOfService
  url: https://truebotanicals.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://truebotanicals.com/policies/privacy-policy
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/true-botanicals-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/true-botanicals-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/true-botanicals-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/true-botanicals-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/true-botanicals-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/true-botanicals-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/true-botanicals-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/true-botanicals-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/true-botanicals-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/true-botanicals-plans-pricing.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/true-botanicals-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/true-botanicals-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/true-botanicals-domain-security.yml
created: '2026-08-30'
description: True Botanicals is a clean-luxury skincare company selling clinically tested, MADE SAFE certified face and body products direct to consumers from truebotanicals.com. It is not a developer-tools company and publishes no developer portal, API keys or SDKs; its machine-readable surface is the agent-commerce layer its Shopify storefront exposes on its own domain — an llms.txt and agents.md at the site root, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an unauthenticated MCP endpoint at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools, a keyless Shopify Storefront GraphQL endpoint, and OAuth 2.0 / OpenID Connect discovery documents for Shopify customer accounts. Every artifact in this repo was probed live from truebotanicals.com; the schemas behind them are platform-authored by Shopify and shared with every Shopify merchant, and are recorded here as served, not as contracts True Botanicals authored.
image: https://truebotanicals.com/cdn/shop/files/TB_True_Botanicals_f873166b-61da-41ce-8c3d-ea2ab3565a12.png?v=1772667499
layout: provider
mcp_servers:
- description: ''
  name: True Botanicals MCP Server
  slug: true-botanicals-mcp-server
modified: '2026-08-30'
name: True Botanicals
nav: Providers
network: true
overview: 'True Botanicals publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Beauty, and Skincare.


  True Botanicals'' developer surface includes documentation, support, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: True Botanicals Plans Pricing
  plan_count: 0
  slug: true-botanicals-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: True Botanicals Rate Limits
  slug: true-botanicals-rate-limits
scopes:
- name: True Botanicals Scopes
  scope_count: 0
  slug: true-botanicals-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 17
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 21.1
  previous_composite: 23.4
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/true-botanicals/refs/heads/main/screenshots/true-botanicals-2026-09-02T164331.png
security:
- kind: authentication
  name: True Botanicals Authentication
  slug: true-botanicals-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: True Botanicals Domain Security
  slug: true-botanicals-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: true-botanicals
tags:
- Company
- Retail
- E-Commerce
- Beauty
- Skincare
- Consumer Goods
- Direct to Consumer
- Agentic Commerce
- Shopify
- MCP
- Universal Commerce Protocol
website: https://truebotanicals.com/
---
