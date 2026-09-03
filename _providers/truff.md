---
access_model:
  confidence: medium
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - rate-limits
  - security
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
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: 'The agent-facing commerce surface for TRUFF''s online store. A Model Context Protocol endpoint at https://shop.truff.com/api/ucp/mcp implements the Universal Commerce Protocol dev.ucp.shopping service '
  name: TRUFF Store UCP Shopping API
  slug: truff-ucp-shopping-mcp
artifact_total: 6
common:
- group: company
  title: ''
  type: Website
  url: https://www.truff.com/
- group: company
  title: ''
  type: About
  url: https://www.truff.com/pages/about-us
- group: company
  title: ''
  type: Blog
  url: https://www.truff.com/blogs/the-sauce
- group: operate
  title: ''
  type: Support
  url: https://www.truff.com/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.truff.com/pages/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.truff.com/pages/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.truff.com/pages/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://shop.truff.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/truff-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/truff-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/truff-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/truff-well-known.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: well-known/truff-openid-configuration.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/truff-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/truff-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/truff-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/truff-conformance.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/truff-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/truff-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/truff-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/truff-domain-security.yml
created: '2026-08-30'
description: 'TRUFF is a Los Angeles-based luxury condiments company founded in 2017 by Nick Ajluni and Nick Guillen, known for its black-truffle-infused hot sauce and a pantry line that has grown to include truffle oil, pasta sauce, aioli, mayonnaise and salt. The brand began as a digitally-native direct-to-consumer business selling through its own storefront at truff.com and has since expanded into a multichannel food business carried in more than 20,000 retail stores including Whole Foods, Kroger, Publix and Target, alongside foodservice collaborations with restaurant chains. SKKY Partners took a significant minority stake in the company in November 2023. TRUFF is a consumer packaged goods manufacturer, not a software vendor: it publishes no developer portal, no OpenAPI, no SDKs and issues no API keys. It does, however, expose a live and completely unauthenticated agent commerce surface at shop.truff.com — a Universal Commerce Protocol (UCP) shopping service reachable over MCP, advertised
  in the store''s own llms.txt and /.well-known/ucp, through which an agent can search the catalog, build a cart and complete a purchase. That surface is Shopify''s platform-native UCP implementation running under TRUFF''s merchant identity rather than something TRUFF engineered, and it is recorded here with that provenance.'
image: https://storefront-direct-upload.s3.amazonaws.com/8ee9e03b-afe7-492e-aaba-bee247bf97b3/favicon.png
layout: provider
mcp_servers:
- description: A live, unauthenticated Model Context Protocol endpoint on TRUFF's own storefront host that exposes the store's catalog, cart, checkout and order surface to agents. It is the Shopify platform's native
  name: TRUFF Store — UCP Shopping MCP
  slug: truff-store-ucp-shopping-mcp
modified: '2026-08-30'
name: TRUFF
nav: Providers
network: true
overview: 'TRUFF publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer Packaged Goods, Food and Beverage, Condiments, and Direct to Consumer.


  TRUFF''s developer surface includes engineering blog, support, documentation, authentication, and 17 more developer resources.'
plans:
- name: Truff Plans Pricing
  plan_count: 0
  slug: truff-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Truff Rate Limits
  slug: truff-rate-limits
score:
  band: emerging
  composite: 19.0
  coverage:
    artifact_dirs: 12
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 19.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/truff/refs/heads/main/screenshots/truff-2026-09-02T164357.png
security:
- kind: authentication
  name: Truff Authentication
  slug: truff-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Truff Domain Security
  slug: truff-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: truff
tags:
- Company
- Consumer Packaged Goods
- Food and Beverage
- Condiments
- Direct to Consumer
- Retail
- E-Commerce
- Agentic Commerce
- Universal Commerce Protocol
- Shopify
website: https://www.truff.com/
---
