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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 24.7
  scored_at: '2026-09-01'
api_count: 2
apis:
- description: Kizik's Universal Commerce Protocol surface, exposed over MCP at https://kizik.com/api/ucp/mcp. An unauthenticated tools/list returns thirteen tools covering catalog search and lookup, cart create/upd
  name: Kizik Agent Commerce API (UCP / MCP)
  slug: kizik-agent-commerce-api-ucp-mcp
- description: 'The read-only JSON product surface of the Kizik Shopify storefront, documented for agents in https://kizik.com/llms.txt: /products.json, /collections/{handle}/products.json, /products/{handle}.json an'
  name: Kizik Storefront Product Data
  slug: kizik-storefront-product-data
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kizik-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://kizik.com/
- group: docs
  title: ''
  type: Documentation
  url: https://kizik.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/kizik-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/kizik-well-known.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/kizik-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/kizik-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/kizik-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/kizik-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/kizik-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/kizik-plans-pricing.yml
- group: company
  title: ''
  type: Blog
  url: https://kizik.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://kizik.com/pages/contact
- group: operate
  title: ''
  type: HelpCenter
  url: https://kizik.com/pages/faqs
- group: start
  title: ''
  type: SignUp
  url: https://kizik.com/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://kizik.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://kizik.com/policies/privacy-policy
created: '2026-08-23'
description: 'Kizik is the hands-free footwear company founded in Alpine, Utah, built on the patented Cage and Inner Cage step-in technology that lets a wearer put on a shoe without bending down, tying, or using their hands. Kizik sells direct-to-consumer at kizik.com across men''s, women''s and kids'' lines, and licenses its hands-free technology to other footwear brands. Kizik has no traditional developer program, but it operates a real, publicly reachable agent commerce surface: its Shopify storefront serves an agent instruction document at /agents.md and /llms.txt, a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, and an unauthenticated MCP endpoint at /api/ucp/mcp exposing thirteen catalog, cart, checkout and order tools with full JSON Schema inputs. Customer identity is OpenID Connect, discoverable at /.well-known/openid-configuration.'
image: https://kizik.com/cdn/shop/files/social-image-athens-2-soft-chambray.jpg?v=1738684971&width=2048
layout: provider
mcp_servers:
- description: Kizik's Universal Commerce Protocol (UCP) shopping service, exposed over MCP on Kizik's own domain. An unauthenticated JSON-RPC tools/list returns 13 tools with full JSON Schema 2020-12 inputSchemas c
  name: Kizik UCP Commerce MCP Server
  slug: kizik-ucp-commerce-mcp-server
modified: '2026-08-23'
name: Kizik
nav: Providers
network: true
overview: 'Kizik publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Footwear, and Consumer Goods.


  Kizik''s developer surface includes documentation, engineering blog, support, signup flow, and 14 more developer resources.'
plans:
- name: Kizik Plans Pricing
  plan_count: 0
  slug: kizik-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Kizik Rate Limits
  slug: kizik-rate-limits
scopes:
- name: Kizik Scopes
  scope_count: 0
  slug: kizik-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
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
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Kizik Authentication
  slug: kizik-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Kizik Domain Security
  slug: kizik-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: kizik
tags:
- Company
- Retail
- E-Commerce
- Footwear
- Consumer Goods
- Agent Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Direct to Consumer
website: https://kizik.com/
---
