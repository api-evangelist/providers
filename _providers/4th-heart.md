---
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
- description: The agent-facing commerce surface of the 4th & Heart online store, implemented by Shopify's native Universal Commerce Protocol support on the merchant's own domain. A remote MCP server at https://four
  name: 4th & Heart Agentic Commerce (UCP / MCP)
  slug: 4th-heart-commerce
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://fourthandheart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://fourthandheart.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/4th-heart-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/4th-heart-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/4th-heart-mcp.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/4th-heart-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/4th-heart-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/4th-heart-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/4th-heart-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/4th-heart-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Blog
  url: https://fourthandheart.com/blogs/recipes
- group: operate
  title: ''
  type: Support
  url: https://fourthandheart.com/pages/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://fourthandheart.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fourthandheart.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fourthandheart.com/policies/privacy-policy
created: '2026-09-05'
description: '4th & Heart is a California-based consumer packaged goods company that makes grass-fed, pasture-raised ghee (clarified butter) and ghee-based spreads, sold direct-to-consumer from its own Shopify storefront at fourthandheart.com and through national grocery retail. It is not a software vendor and publishes no developer program, but the storefront exposes a real, unauthenticated agent-commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a live Model Context Protocol server at /api/ucp/mcp serving 13 catalog, cart, checkout and order tools with full JSON Schema, an /llms.txt and /agents.md agent instruction document, and Shopify customer-account OAuth 2.0 / OpenID Connect discovery metadata on its own domain.'
image: https://fourthandheart.com/cdn/shop/files/4thandHeartGhee.png?v=1730292913
layout: provider
mcp_servers:
- description: ''
  name: 4th & Heart MCP Server
  slug: 4th-heart-mcp-server
modified: '2026-09-05'
name: 4th & Heart
nav: Providers
network: true
overview: '4th & Heart publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Retail, and E-Commerce.


  4th & Heart''s developer surface includes documentation, engineering blog, support, signup flow, and 12 more developer resources.'
plans:
- name: 4Th Heart Plans Pricing
  plan_count: 0
  slug: 4th-heart-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: 4Th Heart Rate Limits
  slug: 4th-heart-rate-limits
scopes:
- name: 4Th Heart Scopes
  scope_count: 4
  slug: 4th-heart-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 14
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
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-05'
security:
- kind: authentication
  name: 4Th Heart Authentication
  slug: 4th-heart-authentication
  summary_line: none/oauth2/openIdConnect · 4 schemes
- kind: domain-security
  name: 4Th Heart Domain Security
  slug: 4th-heart-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 4th-heart
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Retail
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
- Direct to Consumer
website: https://fourthandheart.com/
---
