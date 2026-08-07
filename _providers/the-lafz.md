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
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Lafz direct-to-consumer storefront on Shopify, with an agent-commerce surface over the Universal Commerce Protocol (UCP) MCP server plus read-only product/collection JSON endpoints and Shopify cus
  name: Lafz Storefront (Shopify UCP)
  slug: lafz-storefront-shopify-ucp
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://thelafz.com
- group: other
  title: ''
  type: Store
  url: https://lafz.com
- group: agent
  title: ''
  type: MCPServer
  url: mcp/the-lafz-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/the-lafz-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/the-lafz-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-lafz-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-lafz-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/the-lafz-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/the-lafz-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://lafz.com/policies/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://lafz.com/pages/contact
- group: company
  title: ''
  type: Blog
  url: https://lafz.com/blogs/news
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-lafz
created: '2026-07-17'
description: 'Lafz is a halal-certified cosmetics and personal-care brand, founded in 2019 and headquartered in Singapore as part of the Believe PTE FMCG group. It sells hair care, skin care, makeup, a caffeine range, deodorants and fragrance made without alcohol, parabens or animal by-products. The direct-to-consumer storefront at lafz.com runs on Shopify and exposes real agent-facing surfaces: a Shopify customer-account OpenID Connect provider, an /llms.txt agent guide, and a Universal Commerce Protocol (UCP) shopping MCP server for buyer-approved agent-driven checkout. thelafz.com is the corporate "halal compliant factories" site. Added to the API Evangelist network as an Accel portfolio-graph lead and enriched from its live public surfaces.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-lafz.png
layout: provider
mcp_servers:
- description: ''
  name: the-lafz-mcp.yml
  slug: the-lafz-mcpyml
modified: '2026-07-21'
name: The Lafz
nav: Providers
network: true
overview: 'The Lafz publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Cosmetics, Personal Care, and E-Commerce.


  The Lafz''s developer surface includes authentication, support, engineering blog, and 11 more developer resources.'
random_paper: 4
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 27.7
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 17.8
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: The Lafz Authentication
  slug: the-lafz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: The Lafz Domain Security
  slug: the-lafz-domain-security
  summary_line: TLSv1.3 · HSTS
slug: the-lafz
tags:
- Company
- Consumer
- Cosmetics
- Personal Care
- E-Commerce
- Halal
- Shopify
- Agent Commerce
website: https://thelafz.com
---
