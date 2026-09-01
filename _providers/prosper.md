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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 9.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: RESTful API for Prosper investors and third-party agents to view account information, search active loan listings, place orders to purchase Notes, and retrieve owned Notes, invested loans, and loan pa
  name: Prosper Investor API
  slug: prosper-investor-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.prosper.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.prosper.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.prosper.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developers.prosper.com/docs/investor/
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.prosper.com/docs/investor/
- group: operate
  title: ''
  type: Support
  url: https://developers.prosper.com/support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.prosper.com/
- group: company
  title: ''
  type: Blog
  url: https://www.prosper.com/blog
- group: start
  title: ''
  type: SignUp
  url: https://www.prosper.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.prosper.com/loans/rates-and-fees
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prosper.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.prosper.com/legal/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/prosper-authentication.yml
- group: auth
  title: ''
  type: OAuth
  url: https://www.prosper.com/oauth
- group: start
  title: ''
  type: Sandbox
  url: sandbox/prosper-sandbox.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prosper-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/prosper-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/prosper-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/prosper-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Prosper Marketplace operates one of the largest peer-to-peer (marketplace) lending platforms in the United States, matching individual and institutional investors with consumers seeking personal loans, and also offering a HELOC and a credit-card product. For investors, Prosper publishes a RESTful Investor API that lets individual, institutional, and third-party agents connect directly to the platform to view account balances, search active loan listings, place orders (bids) to purchase Notes, and track owned Notes, loans, and payments. The API uses OAuth 2.0 over SSL with comprehensive filtering and sorting, and offers a sandbox environment for integration testing. This profile was surfaced as a portfolio company of Emergence Capital, IVP, and QED Investors and enriched from Prosper's public developer documentation.
image: https://www.prosper.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: Prosper MCP Server
  slug: prosper-mcp-server
modified: '2026-07-20'
name: Prosper
nav: Providers
network: true
overview: 'Prosper publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Lending, Peer-to-Peer Lending, and Marketplace Lending.


  Prosper''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, pricing, and 13 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 28.7
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 31.6
    commercial_clarity: 31.6
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 7.9
  previous_composite: 28.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Prosper Authentication
  slug: prosper-authentication
  summary_line: oauth2 · 3 schemes
- kind: domain-security
  name: Prosper Domain Security
  slug: prosper-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: prosper
tags:
- Company
- Fintech
- Lending
- Peer-to-Peer Lending
- Marketplace Lending
- Investing
- Personal Loans
- Consumer Credit
- Financial-Services
website: https://www.prosper.com
---
