---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
  score: 30.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 7
  human_in_the_loop: 1
  name: 1More Agentic Access
  operation_count: 13
  slug: 1more-agentic-access
  summary_line: 13 operations · 7 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: The agent-facing commerce interface 1MORE serves from its own US storefront host. A Universal Commerce Protocol merchant profile at /.well-known/ucp declares the supported UCP versions, services and p
  name: 1MORE Storefront Agent Commerce (UCP/MCP)
  slug: 1more-storefront-agent-commerce
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/1more-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://usa.1more.com/
- group: docs
  title: ''
  type: Documentation
  url: https://usa.1more.com/agents.md
- group: operate
  title: ''
  type: Support
  url: https://usa.1more.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://usa.1more.com/blogs/news
- group: start
  title: ''
  type: SignUp
  url: https://usa.1more.com/account/register
- group: start
  title: ''
  type: Login
  url: https://usa.1more.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usa.1more.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usa.1more.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/1more-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/1more-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/1more-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/1more-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/1more-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/1more-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/1more-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/1more-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/1more-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/1more-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/1more-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/1more-agentic-access.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/1more-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/1more-plans-pricing.yml
created: '2026-09-05'
description: 1MORE (万魔声学 / 1MORE Acoustics Technology Co., Ltd., founded 2013, with operations in China, the United States and the United Kingdom) is a consumer audio brand that designs and sells wired and wireless earbuds, on-ear and over-ear headphones, open-ear sport earbuds and companion mobile apps. 1MORE publishes no developer program or public product API. Its machine-readable surface is its own direct-to-consumer storefront at usa.1more.com, which serves an agent-facing llms.txt/agents.md, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, an anonymous remote MCP endpoint at /api/ucp/mcp exposing 13 catalog, cart, checkout and order tools, OAuth 2.0 / OpenID Connect discovery documents for Shopify customer accounts, and read-only JSON product endpoints. That surface is Shopify's UCP implementation running under 1MORE's own domain and merchant identity.
image: https://usa.1more.com/cdn/shop/files/logo_7d70adc1-01a8-4223-aca7-d56748c230de.png?height=628&pad_color=ffffff&v=1698057387&width=1200
layout: provider
mcp_servers:
- description: ''
  name: 1MORE MCP Server
  slug: 1more-mcp-server
modified: '2026-09-05'
name: 1MORE
nav: Providers
network: true
overview: '1MORE publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Electronics, Audio, Headphones, and Retail.


  1MORE''s developer surface includes documentation, support, engineering blog, signup flow, authentication, and 19 more developer resources.'
plans:
- name: 1More Plans Pricing
  plan_count: 0
  slug: 1more-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: 1More Rate Limits
  slug: 1more-rate-limits
scopes:
- name: 1More Scopes
  scope_count: 4
  slug: 1more-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 1More Authentication
  slug: 1more-authentication
  summary_line: none/oauth2/openIdConnect · 3 schemes
- kind: domain-security
  name: 1More Domain Security
  slug: 1more-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1more
tags:
- Company
- Consumer Electronics
- Audio
- Headphones
- Retail
- E-Commerce
- Agent Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
website: https://usa.1more.com/
---
