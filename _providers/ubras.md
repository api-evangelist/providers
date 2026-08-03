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
  score: 23.4
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: 'Agent-facing commerce surface of the ubras.com Shopify storefront: a live storefront MCP endpoint (catalog search, cart, product details, policy FAQs), a Universal Commerce Protocol shopping service w'
  name: Ubras Storefront Agent Commerce (UCP + MCP)
  slug: ubras-storefront-agent-commerce-ucp-mcp
artifact_total: 4
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ubras-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ubras.com
- group: company
  title: ''
  type: Website
  url: https://www.ubras.cn
- group: docs
  title: ''
  type: Documentation
  url: https://ubras.com/agents.md
- group: start
  title: ''
  type: Login
  url: https://ubras.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://ubras.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://ubras.com/blogs/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ubras.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ubras.com/policies/terms-of-service
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ubras-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ubras-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ubras-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ubras-authentication.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ubras-conformance.yml
created: '2026-07-17'
description: 'Ubras is a Chinese direct-to-consumer intimate apparel brand best known for popularizing sizeless (one-size) wireless bras and skin-layer basics. It sells through its Chinese official site at www.ubras.cn and an international Shopify storefront at ubras.com. The international store publishes a genuinely agent-ready commerce surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, live MCP endpoints for catalog search, cart, and buyer-approved checkout, llms.txt and agents.md agent instructions, and Shopify customer-accounts OIDC discovery. Ubras is a portfolio company of Hongshan (Sequoia Capital China).'
image: https://ubras.com/cdn/shop/files/20220928-174018.jpg?v=1664358034
layout: provider
mcp_servers:
- description: ''
  name: ubras-mcp.yml
  slug: ubras-mcpyml
modified: '2026-07-21'
name: Ubras
nav: Providers
network: true
overview: 'Ubras publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Retail, eCommerce, and Apparel.


  Ubras'' developer surface includes documentation, support, engineering blog, authentication, and 10 more developer resources.'
random_paper: 66
score:
  band: emerging
  composite: 24.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.0
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Ubras Authentication
  slug: ubras-authentication
  summary_line: openIdConnect · 1 scheme
- kind: domain-security
  name: Ubras Domain Security
  slug: ubras-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ubras
tags:
- Company
- Consumer
- Retail
- eCommerce
- Apparel
- Intimate Apparel
- Direct-to-Consumer
- Agentic Commerce
website: https://ubras.com
---
