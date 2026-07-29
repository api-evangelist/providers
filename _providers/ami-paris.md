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
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
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
  score: 27.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Agent-facing commerce surface for the AMI Paris Shopify storefront — a Universal Commerce Protocol (UCP) MCP endpoint for catalog search, cart, checkout, fulfillment, discount, and order operations, p
  name: AMI Paris Agent Commerce (UCP)
  slug: ami-paris-agent-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://amiparis.com
- group: start
  title: ''
  type: Login
  url: https://www.amiparis.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://www.amiparis.com/pages/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amiparis.com/policies/privacy-policy
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ami-paris-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ami-paris-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/ami-paris-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ami-paris-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/ami-paris-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ami-paris-domain-security.yml
created: '2026-07-17'
description: 'AMI Paris is a French contemporary ready-to-wear fashion house founded in 2011 by Alexandre Mattiussi and headquartered in Paris, known for its "Ami de coeur" heart logo. It sells menswear, womenswear, and accessories direct-to-consumer through amiparis.com, an online store built on Shopify. The store exposes a real agent-commerce surface: a Universal Commerce Protocol (UCP, ucp.dev) MCP endpoint advertised in /.well-known/ucp, a published /llms.txt and /agents.md with agent instructions, Shopify Customer Account OIDC/OAuth2 authentication, and read-only product/collection JSON endpoints. It was surfaced as a portfolio company of HongShan (Sequoia China) and profiled by the API Evangelist enrichment pipeline.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ami-paris.png
layout: provider
mcp_servers:
- description: ''
  name: ami-paris-mcp.yml
  slug: ami-paris-mcpyml
modified: '2026-07-17'
name: AMI Paris
nav: Providers
network: true
overview: 'AMI Paris publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Fashion, Retail, and Ecommerce.


  AMI Paris'' developer surface includes support, authentication, and 9 more developer resources.'
random_paper: 52
scopes:
- name: Ami Paris Scopes
  scope_count: 4
  slug: ami-paris-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 19.5
  delta: -0.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 30.4
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.1
  provenance:
    mcp: first-party
    skills: first-party
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Ami Paris Authentication
  slug: ami-paris-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Ami Paris Domain Security
  slug: ami-paris-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ami-paris
tags:
- Company
- Consumer
- Fashion
- Retail
- Ecommerce
- Shopify
- Agent Commerce
- UCP
website: https://amiparis.com
---
