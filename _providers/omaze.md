---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 26.3
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: The Universal Commerce Protocol Shopping service that Omaze UK exposes over the Model Context Protocol, advertised by Omaze in its own /agents.md and /llms.txt and described by the merchant profile at
  name: Omaze UK UCP Shopping MCP
  slug: omaze-uk-ucp-shopping-mcp
- description: The German-market counterpart of the Omaze UCP Shopping service, exposed over MCP at omaze.de/api/ucp/mcp and described by the merchant profile at omaze.de/.well-known/ucp. Same protocol version (2026
  name: Omaze Germany UCP Shopping MCP
  slug: omaze-de-ucp-shopping-mcp
- description: The anonymous, read-only JSON surface of the Omaze UK storefront, documented by Omaze itself in /agents.md for agents that only need to read store data without transacting. Covers product listings (/p
  name: Omaze UK Storefront JSON
  slug: omaze-uk-storefront-json
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/omaze-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.omaze.com
- group: company
  title: ''
  type: Website
  url: https://omaze.co.uk
- group: company
  title: ''
  type: Website
  url: https://omaze.de
- group: start
  title: ''
  type: DeveloperPortal
  url: https://omaze.co.uk/agents.md
- group: docs
  title: ''
  type: Documentation
  url: https://omaze.co.uk/agents.md
- group: start
  title: ''
  type: GettingStarted
  url: https://omaze.co.uk/llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/omaze-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/omaze-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/omaze-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/omaze-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/omaze-scopes.yml
- group: other
  title: ''
  type: OpenIDConnect
  url: https://omaze.co.uk/.well-known/openid-configuration
- group: design
  title: ''
  type: Conventions
  url: conventions/omaze-conventions.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/omaze-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/omaze-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/omaze-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/omaze-conformance.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: Support
  url: https://omaze.co.uk/pages/contact-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://omaze.co.uk/pages/faqs
- group: company
  title: ''
  type: Blog
  url: https://omaze.co.uk/blogs/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Omaze
- group: start
  title: ''
  type: SignUp
  url: https://omaze.co.uk/account/register
- group: start
  title: ''
  type: Login
  url: https://omaze.co.uk/account/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://omaze.co.uk/pages/legal-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://omaze.co.uk/policies/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://omaze.company/careers.html
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/omaze_stock/
created: '2026-08-02'
description: 'Omaze is a for-profit social-impact entertainment company that runs online prize draws to raise money for charity. Founded in 2012 in Culver City, California by Matthew Pohlson and Ryan Cummins, it lets people enter draws for houses, supercars, cash and once-in-a-lifetime experiences, with a share of every entry going to a partner nonprofit; the company reports raising more than $250 million for over 600 charities and creating 50+ millionaires. Its live consumer operations today are the United Kingdom (omaze.co.uk) and Germany (omaze.de), both built on Shopify, while omaze.com serves as the corporate and brand site. Omaze publishes no developer program, no OpenAPI and no SDKs, but both storefronts do expose a genuine machine-readable agent surface: a Universal Commerce Protocol (UCP) merchant profile at /.well-known/ucp, a UCP Shopping MCP endpoint at /api/ucp/mcp, published agent instructions at /llms.txt and /agents.md, anonymous read-only storefront product JSON, and a standards-compliant
  OpenID Connect authorization server for customer accounts.'
image: https://omaze.co.uk/cdn/shop/files/social_image-2.png?v=1753698911
layout: provider
mcp_servers:
- description: ''
  name: omaze-mcp.yml
  slug: omaze-mcpyml
modified: '2026-08-02'
name: Omaze
nav: Providers
network: true
overview: 'Omaze publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Charity, Fundraising, Nonprofit, and Prize Draws.


  Omaze''s developer surface includes documentation, getting-started guide, authentication, support, engineering blog, signup flow, and 23 more developer resources.'
random_paper: 93
rate_limits:
- limit_count: 0
  name: Omaze Rate Limits
  slug: omaze-rate-limits
scopes:
- name: Omaze Scopes
  scope_count: 0
  slug: omaze-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 29.0
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 51.8
    discoverability: 92.6
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 29.5
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/omaze/refs/heads/main/screenshots/omaze-2026-08-07T190133.png
security:
- kind: authentication
  name: Omaze Authentication
  slug: omaze-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Omaze Domain Security
  slug: omaze-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: omaze
tags:
- Company
- Charity
- Fundraising
- Nonprofit
- Prize Draws
- Sweepstakes
- Ecommerce
- Agentic Commerce
- Universal Commerce Protocol
- Model Context Protocol
- Shopify
- United Kingdom
- Germany
website: https://www.omaze.com
---
