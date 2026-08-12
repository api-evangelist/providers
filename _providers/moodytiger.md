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
    agent_skills: true
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 15.3
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Agent-facing shopping surface for the moodytiger Shopify store implemented with the Universal Commerce Protocol (UCP). Agents discover capabilities at /.well-known/ucp and transact (catalog search, ca
  name: moodytiger UCP Commerce (MCP)
  slug: moodytiger-ucp-commerce-mcp
artifact_total: 3
common:
- group: company
  title: ''
  type: Website
  url: https://moodytiger.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moodytiger-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/moodytiger-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/moodytiger-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moodytiger-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://moodytiger.com/agents.md
- group: company
  title: ''
  type: Blog
  url: https://moodytiger.com/blogs/news
- group: operate
  title: ''
  type: Support
  url: https://moodytiger.com/pages/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://moodytiger.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://moodytiger.com/policies/terms-of-service
created: '2026-07-17'
description: 'moodytiger is a technology-driven, design-led activewear brand for kids, offering leggings, shorts, tees, skirts and outerwear for boys and girls. Surfaced as a portfolio company of Qiming Venture Partners, its direct-to-consumer storefront runs on Shopify at moodytiger.com. The store has no bespoke first-party developer API, but it does expose a modern agent-native commerce surface: a published Universal Commerce Protocol (UCP, ucp.dev) MCP shopping endpoint, an /agents.md agent-instructions document mirrored at /llms.txt, and Shopify Customer Account OIDC discovery under /.well-known/. This profile captures those verifiable agent and well-known surfaces.'
image: http://moodytiger.com/cdn/shop/files/1200_628.jpg?v=1684201715
layout: provider
mcp_servers:
- description: ''
  name: moodytiger-mcp.yml
  slug: moodytiger-mcpyml
modified: '2026-07-20'
name: moodytiger
nav: Providers
network: true
overview: 'moodytiger publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, E-Commerce, Apparel, and Kids Activewear.


  moodytiger''s developer surface includes documentation, engineering blog, support, and 8 more developer resources.'
random_paper: 47
score:
  band: emerging
  composite: 17.9
  delta: -1.1
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 19.0
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/moodytiger/refs/heads/main/screenshots/moodytiger-2026-08-07T184237.png
security:
- kind: domain-security
  name: Moodytiger Domain Security
  slug: moodytiger-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: moodytiger
tags:
- Company
- Retail
- E-Commerce
- Apparel
- Kids Activewear
- Agentic Commerce
- Universal Commerce Protocol
- MCP
- Shopify
website: https://moodytiger.com
---
