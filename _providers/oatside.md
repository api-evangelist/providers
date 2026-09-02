---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: platform
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
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
  score: 15.9
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: 'The agent-facing commerce surface of Oatside''s Singapore direct-to-consumer storefront. Implements the Universal Commerce Protocol (UCP) 2026-04-08 over MCP: an anonymous tools/list returns 13 tools c'
  name: Oatside SG Storefront UCP / MCP
  slug: oatside-sg-storefront-ucp-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://oatside.com/
- group: docs
  title: ''
  type: Documentation
  url: https://shop.oatside.com/agents.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/oatside-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/oatside-well-known.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://oatside.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://oatside.com/privacy-policy/
- group: operate
  title: ''
  type: Support
  url: https://oatside.com/contact-us/
- group: company
  title: ''
  type: Blog
  url: https://oatside.com/the-oatside-of-life/
- group: commercial
  title: ''
  type: Pricing
  url: https://shop.oatside.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/oatside-plans-pricing.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/oatside-domain-security.yml
created: '2026-08-26'
description: 'Oatside is a Southeast Asian oat milk brand founded in Singapore in 2020 by Benedict Lim, operating as one of Asia''s only "full-stack" plant-milk companies — it controls sourcing, R&D and manufacturing from its own facility in Java, Indonesia, using Australian oats. Its barista-oriented range (Barista Blend, Espresso Roast, Caffe Latte, Chocolate, Chocolate Malt, Matcha, Caramel Macchiato) is sold through independent cafes and retail across Singapore, Hong Kong, Indonesia, Vietnam, Thailand, Cambodia, the Philippines, Malaysia, Taiwan, India, the Middle East and Australia. Oatside is a consumer packaged goods company and publishes no developer program, but its direct-to-consumer Shopify storefront exposes a live, anonymous, agent-callable commerce surface: a Universal Commerce Protocol (UCP) merchant profile and an MCP endpoint serving 13 catalog, cart and checkout tools, plus a published agents.md and llms.txt.'
image: https://oatside.com/wp-content/uploads/2026/07/oatside-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: Oatside SG Storefront UCP/MCP Server
  slug: oatside-sg-storefront-ucpmcp-server
modified: '2026-08-26'
name: Oatside
nav: Providers
network: true
overview: 'Oatside publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Food and Beverage, Consumer Packaged Goods, Oat Milk, and Plant-Based.


  Oatside''s developer surface includes documentation, support, engineering blog, pricing, and 7 more developer resources.'
plans:
- name: Oatside Plans Pricing
  plan_count: 0
  slug: oatside-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Oatside Rate Limits
  slug: oatside-rate-limits
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Oatside Authentication
  slug: oatside-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Oatside Domain Security
  slug: oatside-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oatside
tags:
- Company
- Food and Beverage
- Consumer Packaged Goods
- Oat Milk
- Plant-Based
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
- Retail
- Singapore
- Southeast Asia
website: https://oatside.com/
---
