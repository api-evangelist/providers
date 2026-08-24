---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.1
  scored_at: '2026-08-24'
api_count: 1
apis:
- description: Green Check Access is Green Check's public REST API suite for service providers — financial institutions, payroll companies, CRMs and other platforms serving the cannabis industry. It exposes 49 opera
  name: Green Check Access
  slug: green-check-access
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/green-check-verified-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/green-check-verified-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://greencheckverified.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.greencheckverified.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.greencheckverified.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://developer.greencheckverified.com/apis/swagger
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.greencheckverified.com/guides/insights-quickstart
- group: operate
  title: ''
  type: Support
  url: https://support.greencheckverified.com/
- group: company
  title: ''
  type: Blog
  url: https://greencheckverified.com/knowledge-center/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/greencheckverified
- group: start
  title: ''
  type: SignUp
  url: https://greencheckverified.com/get-started/
- group: start
  title: ''
  type: Login
  url: https://app.greencheckverified.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://greencheckverified.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://greencheckverified.com/privacy-policy/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/green-check-verified-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/green-check-verified-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/green-check-verified-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/green-check-verified-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/green-check-verified-access-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/green-check-verified-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/green-check-verified-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/green-check-verified-lifecycle.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/green-check-verified-scopes.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/green-check-verified-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/green-check-verified-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/green-check-verified-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/green-check-verified-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/green-check-verified-rate-limits.yml
created: '2026-08-22'
description: Green Check Verified (Green Check) is a New Haven, Connecticut specialty-banking compliance platform founded in 2017 that sits between financial institutions and the cannabis and other cash-intensive businesses they serve. Banks and credit unions use it to onboard cannabis-related businesses (CRBs), collect and review due-diligence documentation, validate that deposits trace to legally licensed sales, monitor licenses and negative news, and produce the BSA/AML oversight reporting examiners require. Its public developer product, Green Check Access, is a REST API suite that normalizes compliance, company and transactional data across more than twenty point-of-sale and seed-to-sale systems — Dutchie, Treez, Flowhub, Biotrack, Metrc, Cova, Canix, Greenbits and others — so service providers such as payroll companies, CRMs, lenders and fintechs can programmatically create and onboard CRBs and read their sales, products, inventory, customer and document data through one contract instead
  of one integration per POS.
image: https://greencheckverified.com/wp-content/uploads/2021/06/Feature-Image.png
layout: provider
mcp_servers:
- description: ''
  name: Green Check Verified MCP Server
  slug: green-check-verified-mcp-server
modified: '2026-08-22'
name: Green Check Verified
nav: Providers
network: true
overview: 'Green Check Verified publishes 1 API on the [APIs.io](https://apis.io/) network: Green Check Access. Tagged areas include Company, Cannabis, Compliance, Banking, and Financial Services.


  Green Check Verified''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 22 more developer resources.'
plans:
- name: Green Check Verified Plans Pricing
  plan_count: 0
  slug: green-check-verified-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Green Check Verified Rate Limits
  slug: green-check-verified-rate-limits
scopes:
- name: Green Check Verified Scopes
  scope_count: 0
  slug: green-check-verified-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 49.7
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 30.3
    contract_quality: 50.5
    developer_ergonomics: 71.4
    discoverability: 87.0
    governance: 30.3
    operational_transparency: 2.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 53.2
  schema_version: 0.12.1
  scored_at: '2026-08-24'
security:
- kind: authentication
  name: Green Check Verified Authentication
  slug: green-check-verified-authentication
  summary_line: oauth2/apiKey · 1 scheme
- kind: domain-security
  name: Green Check Verified Domain Security
  slug: green-check-verified-domain-security
  summary_line: TLSv1.3 · DMARC
slug: green-check-verified
tags:
- Company
- Cannabis
- Compliance
- Banking
- Financial Services
- BSA/AML
- Regulatory Technology
- Point of Sale
- Onboarding
- Due Diligence
- Know Your Customer
- Data Aggregation
website: https://greencheckverified.com/
---
