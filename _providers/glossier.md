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
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.8
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: 'Agent-facing commerce surface for the Glossier storefront implementing the Universal Commerce Protocol over MCP: catalog search, cart, checkout, and fulfillment with a buyer-approval invariant on paym'
  name: Glossier Agent Commerce (UCP / MCP)
  slug: glossier-agent-commerce-ucp-mcp
artifact_total: 6
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/glossier-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/glossier-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/glossier-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/glossier-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/glossier-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/glossier-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/glossier-conventions.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/glossier-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.glossier.com/pages/responsible-disclosure
- group: auth
  title: ''
  type: DomainSecurity
  url: security/glossier-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ucp.dev/2026-04-08/specification/overview/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.glossier.com/policies/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.glossier.com/policies/terms-of-service
- group: company
  title: ''
  type: Website
  url: https://www.glossier.com
created: '2026-07-17'
description: 'Glossier is a direct-to-consumer beauty and personal-care brand (skincare, makeup, body, and fragrance) that sells through its own Shopify-powered storefront at glossier.com. It reached the API Evangelist network as a portfolio company of Forerunner Ventures, Index Ventures, IVP, and Thrive Capital. Glossier does not publish a traditional developer program, but its storefront is agent-native: it implements the Universal Commerce Protocol (UCP) with a live MCP endpoint for agent-driven catalog search, cart, and buyer-approved checkout, publishes /llms.txt and /agents.md agent instructions, and exposes Shopify Customer Account OAuth2/OIDC authentication with a discoverable authorization server.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/glossier.png
layout: provider
mcp_servers:
- description: Glossier's Shopify storefront exposes a live agent-commerce MCP endpoint via the Universal Commerce Protocol (UCP). The endpoint enumerates its tool schemas only after an agent supplies a valid UCP ag
  name: Glossier MCP Server
  slug: glossier-mcp-server
modified: '2026-07-19'
name: Glossier
nav: Providers
network: true
overview: 'Glossier publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Beauty, Cosmetics, and E-Commerce.


  Glossier''s developer surface includes authentication, documentation, and 12 more developer resources.'
random_paper: 11
scopes:
- name: Glossier Scopes
  scope_count: 4
  slug: glossier-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: emerging
  composite: 20.7
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 20.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/glossier/refs/heads/main/screenshots/glossier-2026-07-25T215930.png
security:
- kind: authentication
  name: Glossier Authentication
  slug: glossier-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Glossier Domain Security
  slug: glossier-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Glossier Vulnerability Disclosure
  slug: glossier-vulnerability-disclosure
  summary_line: disclosure policy published
slug: glossier
tags:
- Company
- Consumer
- Beauty
- Cosmetics
- E-Commerce
- Retail
- Agent Commerce
- Universal Commerce Protocol
- Shopify
- MCP
website: https://www.glossier.com
---
