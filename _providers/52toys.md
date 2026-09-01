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
    agentic_commerce: platform
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 21.2
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Agent-driven commerce over the official 52TOYS Shopify storefront via the Universal Commerce Protocol MCP endpoint — catalog search, cart, and buyer-approved checkout. Read-only catalog browsing is un
  name: 52TOYS Agentic Commerce (UCP)
  slug: 52toys-agentic-commerce-ucp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://52toys.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://hi52toys.com/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/52toys-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/52toys-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/52toys-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/52toys-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/52toys-conventions.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/52toys-well-known.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/52toys-domain-security.yml
- group: start
  title: ''
  type: SignUp
  url: https://hi52toys.com/account/register
- group: start
  title: ''
  type: Login
  url: https://hi52toys.com/account/login
- group: operate
  title: ''
  type: Support
  url: https://hi52toys.com/pages/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hi52toys.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hi52toys.com/policies/privacy-policy
created: '2026-07-17'
description: '52TOYS is a leading IP-driven toy and collectibles company founded in Beijing in 2015 on the brand proposition "Play for Fun." It designs and produces blind boxes, articulated figures, mechanical and model kits, plush, keychains, and lifestyle merchandise across 100+ owned and licensed IPs — original hits like BEASTBOX, Panda Roll, Nook, and POUKAPOUKA alongside global licenses such as Crayon Shin-chan, Minions, and Tom and Jerry. Its official global storefront runs on Shopify at hi52toys.com (52toys.com redirects there) and is notably agent-native: it publishes an llms.txt, a Universal Commerce Protocol (UCP) merchant profile, a hosted UCP MCP endpoint for agent-driven commerce, and Shopify customer-account OpenID Connect discovery. Surfaced in the API Evangelist network as a Qiming portfolio company.'
image: https://hi52toys.com/cdn/shop/files/52Toys_Logo.png?v=1763377030&width=2048
layout: provider
mcp_servers:
- description: ''
  name: 52TOYS MCP Server
  slug: 52toys-mcp-server
modified: '2026-07-17'
name: 52TOYS
nav: Providers
network: true
overview: '52TOYS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Collectibles, Toys, and Retail.


  52TOYS''s developer surface includes authentication, signup flow, support, and 12 more developer resources.'
random_paper: 20
scopes:
- name: 52Toys Scopes
  scope_count: 4
  slug: 52toys-scopes
  summary_line: 4 scopes
score:
  band: emerging
  composite: 20.0
  coverage:
    artifact_dirs: 9
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 20.0
  provenance:
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/52toys/refs/heads/main/screenshots/52toys-2026-07-25T181212.png
security:
- kind: authentication
  name: 52Toys Authentication
  slug: 52toys-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: 52Toys Domain Security
  slug: 52toys-domain-security
  summary_line: TLSv1.3
slug: 52toys
tags:
- Company
- Consumer
- Collectibles
- Toys
- Retail
- E-Commerce
- Shopify
- Agentic Commerce
website: https://52toys.com
---
