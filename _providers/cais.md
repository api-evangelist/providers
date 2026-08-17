---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: CAIS operates a remote Model Context Protocol server at https://mcp.caisgroup.com/mcp, announced 2026-05-19 as the first surface of the company's "Alts Engine" strategy and initially available to a se
  name: CAIS MCP Server
  slug: cais-mcp-server
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cais-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/cais-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/cais-well-known.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cais-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cais-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/cais-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/cais-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/cais-problem-types.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cais-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.caisgroup.com/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cais_stock/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.caisgroup.com/financial-advisor/how-we-partner/integrations
- group: docs
  title: ''
  type: Documentation
  url: https://www.caisgroup.com/financial-advisor/cais-platform/cais-solutions
- group: operate
  title: ''
  type: Support
  url: https://www.caisgroup.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.caisgroup.com/insights
- group: start
  title: ''
  type: SignUp
  url: https://www.caisgroup.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://members.caisgroup.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.caisgroup.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.caisgroup.com/legal/privacy-policy
- group: other
  title: ''
  type: Accessibility
  url: https://www.caisgroup.com/legal/accessibility-commitment
- group: other
  title: ''
  type: BusinessContinuity
  url: https://www.caisgroup.com/legal/business-continuity-plan
- group: company
  title: ''
  type: Press
  url: https://www.caisgroup.com/our-company/press
- group: other
  title: ''
  type: Podcast
  url: https://www.caisgroup.com/podcast
- group: other
  title: ''
  type: CaseStudies
  url: https://www.caisgroup.com/case-studies
- group: company
  title: ''
  type: Careers
  url: https://www.caisgroup.com/our-company/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cais
created: '2026-08-01'
description: CAIS (Capital Integration Systems LLC) is a New York-headquartered fintech company operating the leading alternative investment platform for independent wealth management. Founded in 2009 by Matt Brown, CAIS connects financial advisors with a curated menu of private equity, private credit, hedge fund, real estate, infrastructure, structured note and precious metals strategies from third-party asset managers and bank issuers, and pairs the marketplace with CAIS Solutions (a SaaS trade and post-trade operating layer for RIAs, aggregators and independent broker-dealers), CAIS IQ (advisor education), Compass (portfolio construction) and CAISey (an AI assistant). The platform serves 2,500+ wealth management firms and 65,000+ advisors overseeing roughly $8.5 trillion in end-client assets, with technology integrations into major custodians (Fidelity, BNY Pershing, Schwab Advisor Services, Goldman Sachs Custody Solutions), reporting providers (Addepar, Black Diamond, Envestnet, Orion,
  Tamarac) and 30+ fund administrators, plus DTCC AIP reporting. In May 2026 CAIS launched a remote Model Context Protocol (MCP) server as part of its "Alts Engine" strategy, exposing fund, holdings, education and identity data to AI agents over OAuth 2.1.
image: https://www.caisgroup.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: cais-mcp.yml
  slug: cais-mcpyml
modified: '2026-08-01'
name: CAIS
nav: Providers
network: true
overview: 'CAIS publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Alternative Investments, Wealth Management, Financial Services, and Fintech.


  CAIS''s developer surface includes authentication, documentation, support, engineering blog, signup flow, and 21 more developer resources.'
random_paper: 118
scopes:
- name: Cais Scopes
  scope_count: 12
  slug: cais-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: emerging
  composite: 25.7
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 43.5
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 25.7
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cais/refs/heads/main/screenshots/cais-2026-08-07T162901.png
security:
- kind: authentication
  name: Cais Authentication
  slug: cais-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Cais Domain Security
  slug: cais-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cais
tags:
- Company
- Alternative Investments
- Wealth Management
- Financial Services
- Fintech
- Private Markets
- Asset Management
- Structured Products
- Investment Platform
- Artificial Intelligence
website: https://www.caisgroup.com/
---
