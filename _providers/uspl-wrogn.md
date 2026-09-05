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
    agent_skills: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.4
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uspl-wrogn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wrogn.com/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uspl-wrogn-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uspl-wrogn-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uspl-wrogn-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uspl-wrogn-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uspl-wrogn-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uspl-wrogn-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uspl-wrogn-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://wrogn.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://wrogn.com/pages/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://wrogn.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://wrogn.com/policies/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://wrogn.com/account/login
created: '2026-07-17'
description: 'USPL (Universal Sportsbiz Pvt. Ltd.) is an Accel-backed Indian celebrity-fashion company whose flagship brand Wrogn — founded in 2014 by Anjana and Vikram Reddy and co-created with cricketer Virat Kohli — sells men''s casual wear, footwear, and accessories at wrogn.com (usplworld.com redirects there). The store runs on Shopify and exposes a genuinely agent-ready commerce surface: a public storefront MCP server at /api/mcp, a Universal Commerce Protocol merchant profile at /.well-known/ucp with a UCP MCP endpoint, published agent instructions at /agents.md and /llms.txt, Shopify Customer Accounts OIDC discovery on its own host, and unauthenticated product JSON endpoints.'
image: https://wrogn.com/cdn/shop/files/WROGN-LOGO-1.jpg?v=1704889508
layout: provider
mcp_servers:
- description: Wrogn (USPL / Universal Sportsbiz) runs its store on Shopify, which exposes the storefront's native MCP server publicly. POST https://wrogn.com/api/mcp answered MCP tools/list unauthenticated at probe
  name: USPL Wrogn MCP Server
  slug: uspl-wrogn-mcp-server
modified: '2026-07-21'
name: USPL Wrogn
nav: Providers
network: true
overview: 'USPL Wrogn is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, Apparel, and E-Commerce.


  USPL Wrogn''s developer surface includes authentication, engineering blog, support, and 12 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 0
  name: Uspl Wrogn Rate Limits
  slug: uspl-wrogn-rate-limits
scopes:
- name: Uspl Wrogn Scopes
  scope_count: 4
  slug: uspl-wrogn-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 18.7
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 18.7
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uspl-wrogn/refs/heads/main/screenshots/uspl-wrogn-2026-09-02T165257.png
security:
- kind: authentication
  name: Uspl Wrogn Authentication
  slug: uspl-wrogn-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Uspl Wrogn Domain Security
  slug: uspl-wrogn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uspl-wrogn
tags:
- Company
- Consumer
- Fashion
- Apparel
- E-Commerce
- Retail
- India
- Agentic Commerce
- MCP
website: https://wrogn.com/
---
