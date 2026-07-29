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
  score: 24.5
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Universal Commerce Protocol shopping service exposed over MCP by the tnuck.com Shopify storefront - catalog search, cart, checkout, fulfillment, discounts, and orders, with buyer-approved payment. Dis
  name: Storefront Agent Commerce (UCP over MCP)
  slug: storefront-agent-commerce-ucp-over-mcp
artifact_total: 5
common:
- group: company
  title: ''
  type: Website
  url: https://tnuck.com
- group: docs
  title: ''
  type: Documentation
  url: https://tnuck.com/agents.md
- group: agent
  title: ''
  type: MCPServer
  url: mcp/uscoop-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/uscoop-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/uscoop-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/uscoop-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/uscoop-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/uscoop-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uscoop-domain-security.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tnuck.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tnuck.com/policies/terms-of-service
- group: start
  title: ''
  type: Login
  url: https://tnuck.com/account
- group: operate
  title: ''
  type: Support
  url: https://tnuck.com/pages/contact-us
- group: company
  title: ''
  type: Blog
  url: https://tnuck.com/blogs/news
created: '2026-07-17'
description: uScoop appears in the 500 Global portfolio mapped to the website tnuck.com. The original uScoop was a 2010 college-student daily-deals startup (theuscoop.com, later uscoop.com); both domains are now offline or parked for sale, and the recorded website today is the Tuckernuck online retail storefront on Shopify. This profile documents the live API and agent surface of that recorded website, which publishes llms.txt and agents.md agent instructions, a Universal Commerce Protocol (UCP) merchant profile, a live MCP shopping endpoint, and OpenID Connect / OAuth 2.0 discovery documents for customer accounts.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uscoop.png
layout: provider
mcp_servers:
- description: ''
  name: uscoop-mcp.yml
  slug: uscoop-mcpyml
modified: '2026-07-21'
name: uScoop
nav: Providers
network: true
overview: 'uScoop publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Retail, Fashion, eCommerce, and Agentic Commerce.


  uScoop''s developer surface includes documentation, authentication, support, engineering blog, and 11 more developer resources.'
random_paper: 33
scopes:
- name: Uscoop Scopes
  scope_count: 4
  slug: uscoop-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 24.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 36.4
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 24.3
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Uscoop Authentication
  slug: uscoop-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Uscoop Domain Security
  slug: uscoop-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uscoop
tags:
- Company
- Retail
- Fashion
- eCommerce
- Agentic Commerce
- Shopping
website: https://tnuck.com
---
