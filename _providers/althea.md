---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
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
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.3
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the Althea storefront on Shopify: a live Storefront MCP server (search_catalog, get_cart, update_cart, get_product_details, search_shop_policies_and_faqs), a Universa'
  name: Althea Storefront Agent Commerce API
  slug: althea-storefront-agent-commerce-api
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://us.althea.kr
- group: company
  title: ''
  type: Blog
  url: https://us.althea.kr/blogs/beauty-feed
- group: operate
  title: ''
  type: Support
  url: https://support.althea.kr/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://us.althea.kr/account
- group: commercial
  title: ''
  type: TermsOfService
  url: https://us.althea.kr/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://us.althea.kr/policies/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://us.althea.kr/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/althea-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/althea-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/althea-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/althea-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/althea-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/althea-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/althea-conventions.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/althea-domain-security.yml
created: '2026-07-17'
description: 'Althea (Althea Global, us.althea.kr) is a Seoul-founded K-beauty e-commerce company operating an online marketplace that curates and ships authentic Korean skincare, makeup, and hair and body-care products directly from Korea to more than 200 countries, with regional storefronts for the USA, Korea, Malaysia, Singapore, and the Philippines. Founded in 2015 and backed by 500 Global, Tekton Ventures, FirstFloor Capital, InnoVen Capital, and Korea Development Bank, the platform runs on Shopify and exposes a native agent-commerce surface: a live Shopify Storefront MCP server, a Universal Commerce Protocol (UCP) merchant profile and MCP endpoint, Shopify Customer Account OpenID Connect, and published /llms.txt and /agents.md agent instructions for AI shopping assistants.'
image: https://us.althea.kr/cdn/shop/files/althea-logo_a64c523b-c7ea-4aa5-ac1e-19107b425819_grande.png?v=1614805110
layout: provider
mcp_servers:
- description: 'Althea Global runs on Shopify and exposes native agent-commerce endpoints. Two MCP servers are live at the store domain: the Shopify Storefront MCP (/api/mcp) which returns a working tools/list, and t'
  name: Althea MCP Server
  slug: althea-mcp-server
modified: '2026-07-17'
name: Althea
nav: Providers
network: true
overview: 'Althea publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, E-Commerce, Retail, Beauty, and Cosmetics.


  Althea''s developer surface includes engineering blog, support, documentation, authentication, and 11 more developer resources.'
random_paper: 14
scopes:
- name: Althea Scopes
  scope_count: 4
  slug: althea-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 10
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
    developer_ergonomics: 26.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 20.5
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/althea/refs/heads/main/screenshots/althea-2026-08-07T161249.png
security:
- kind: authentication
  name: Althea Authentication
  slug: althea-authentication
  summary_line: openIdConnect/oauth2 · 1 scheme
- kind: domain-security
  name: Althea Domain Security
  slug: althea-domain-security
  summary_line: TLSv1.3 · HSTS
slug: althea
tags:
- Company
- E-Commerce
- Retail
- Beauty
- Cosmetics
- K-Beauty
- Skincare
- Agent Commerce
- Shopify
website: https://us.althea.kr
---
