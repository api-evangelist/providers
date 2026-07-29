---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 14.4
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Agent-native commerce surface for the IM8 Health (Prenetics) Shopify storefront, implemented with the Universal Commerce Protocol (UCP, 2026-04-08) over MCP. Agents discover capabilities at /.well-kno
  name: IM8 Health Agent Commerce (UCP / MCP)
  slug: im8-health-agent-commerce-ucp-mcp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://prenetics.com
- group: other
  title: ''
  type: Portfolio
  url: https://im8health.com
- group: company
  title: ''
  type: InvestorRelations
  url: https://ir.prenetics.com/
- group: company
  title: ''
  type: Blog
  url: https://ir.prenetics.com/news-events/press-releases
- group: company
  title: ''
  type: Careers
  url: https://careers.prenetics.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://im8health.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://im8health.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/prenetics-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prenetics-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prenetics-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/prenetics-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/prenetics-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prenetics-domain-security.yml
created: '2026-07-17'
description: 'Prenetics Global Limited (NASDAQ: PRE) is a consumer healthcare and longevity company whose flagship brand is IM8, a science-backed daily-nutrition and longevity supplement line co-founded with David Beckham that reached roughly $120M in annual recurring revenue within its first year. The company''s IM8 Health direct-to-consumer storefront runs on Shopify and exposes an agent-native commerce surface: it publishes an /llms.txt agent guide and a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp that advertises a hosted Model Context Protocol (MCP) shopping endpoint, letting AI agents search the catalog, build carts, and drive buyer-approved checkout via Shop Pay, Google Pay, and Shopify card handlers. Prenetics itself publishes no separate developer/API program; the agent-commerce surface is the IM8 Health UCP/MCP storefront.'
image: https://cdn.prod.website-files.com/635b81308992081d90756acb/69439a3fcfe67a98dae5dae7_android-chrome-512x512-256x256.png
layout: provider
mcp_servers:
- description: ''
  name: prenetics-mcp.yml
  slug: prenetics-mcpyml
modified: '2026-07-20'
name: Prenetics
nav: Providers
network: true
overview: 'Prenetics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Health, Longevity, Nutrition, and Supplements.


  Prenetics'' developer surface includes engineering blog and 12 more developer resources.'
random_paper: 49
score:
  band: emerging
  composite: 16.6
  delta: 0.9
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 15.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Prenetics Domain Security
  slug: prenetics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prenetics
tags:
- Company
- Consumer Health
- Longevity
- Nutrition
- Supplements
- Ecommerce
- Agent Commerce
- MCP
- UCP
- Shopify
website: https://prenetics.com
---
