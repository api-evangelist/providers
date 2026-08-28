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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 27.3
  scored_at: '2026-08-26'
api_count: 1
apis:
- description: 'OAuth-protected Model Context Protocol (JSON-RPC 2.0) server exposing Fibe''s consumer lending platform to AI agents. Advertised scopes: loan.read (read loan/eligibility information) and loan.apply (su'
  name: Fibe MCP Server
  slug: fibe-mcp-server
artifact_total: 5
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/fibe-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fibe-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/fibe-scopes.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/fibe-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/fibe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fibe.in/about-us/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/fibe-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fibe-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.fibe.in/mcp/
- group: company
  title: ''
  type: Blog
  url: https://www.fibe.in/blogs/
- group: operate
  title: ''
  type: Support
  url: https://www.fibe.in/contact-us/
- group: start
  title: ''
  type: SignUp
  url: https://portal.fibe.in/SignUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.fibe.in/terms-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fibe.in/privacy-policy/
- group: company
  title: ''
  type: Website
  url: https://fibe.in
created: '2026-07-17'
description: Fibe (formerly EarlySalary) is a digital consumer lending platform in India, founded in 2015 and headquartered in Pune. It offers instant personal loans up to Rs 10 lakh, loans against mutual funds, fixed deposits, a co-branded Fibe Axis Bank credit card, insurance, and purpose-driven (BNPL) financing across education, healthcare, travel, e-commerce, and solar. As of March 2026 Fibe reports over Rs 48,000 crore disbursed across 9.8 million loans to 3.3 million customers and 46 million app downloads. Fibe is ISO/IEC 27001, SOC 2, and PCI DSS certified. Notably, Fibe operates a live, OAuth-protected Model Context Protocol (MCP) server that lets AI agents read loan/eligibility information and initiate loan applications (scopes loan.read and loan.apply). Fibe publishes no public REST/OpenAPI developer surface; its machine-facing surface is the MCP server, secured with OAuth 2.0 authorization-code + PKCE and dynamic client registration.
image: https://www.fibe.in/Fibe-og-img.png
layout: provider
mcp_servers:
- description: ''
  name: Fibe MCP Server
  slug: fibe-mcp-server
modified: '2026-07-19'
name: Fibe
nav: Providers
network: true
overview: 'Fibe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Personal Loans, and Consumer Finance.


  Fibe''s developer surface includes authentication, engineering blog, support, signup flow, and 11 more developer resources.'
random_paper: 7
scopes:
- name: Fibe Scopes
  scope_count: 2
  slug: fibe-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: emerging
  composite: 23.1
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 23.1
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fibe/refs/heads/main/screenshots/fibe-2026-07-25T214400.png
security:
- kind: authentication
  name: Fibe Authentication
  slug: fibe-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Fibe Domain Security
  slug: fibe-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: fibe
tags:
- Company
- Fintech
- Lending
- Personal Loans
- Consumer Finance
- India
- Credit
- MCP
- Agents
website: https://fibe.in
---
