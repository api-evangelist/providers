---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 44.2
  scored_at: '2026-08-24'
api_count: 5
apis:
- description: 'Read and write the ESG data core of the Measurabl platform: portfolios, buildings, spaces, funds, energy and water meters and their readings and bills, waste meters and readings, green building certif'
  name: Measurabl Core API
  slug: measurabl-core-api
- description: 'Asset-level building intelligence (the Insights surface): submit buildings by coordinates, address or Measurabl building id and receive modeled energy estimates, carbon estimates, green building certi'
  name: Measurabl ESGx Buildings API
  slug: measurabl-esgx-buildings-api
- description: 'Listed real estate ESG datasets for capital markets: list available listed-real-estate reports and retrieve their company-level and building-level data sets, with pre-signed URL downloads for each dat'
  name: Measurabl ESGx Securities API
  slug: measurabl-esgx-securities-api
- description: List and download the compliance files published alongside the ESGx Securities listed real estate datasets, with pre-signed URL redirect downloads.
  name: Measurabl ESGx Securities Compliance Files API
  slug: measurabl-esgx-securities-compliance-files-api
- description: 'Partner-facing surface for integration partners acting on behalf of a Measurabl customer: list portfolios, list the buildings in a portfolio, and read monthly utility data for a building.'
  name: Measurabl Partner API
  slug: measurabl-partner-api
artifact_total: 17
collections:
- collection_type: open
  name: Measurabl Core API
  slug: open-measurabl-core
- collection_type: open
  name: ESGx Buildings API
  slug: open-measurabl-esgx-buildings
- collection_type: open
  name: ESGx Securities Compliance Files API
  slug: open-measurabl-esgx-securities-compliance-files
- collection_type: open
  name: ESGx Securities API
  slug: open-measurabl-esgx-securities
- collection_type: open
  name: Partner API V0
  slug: open-measurabl-partners
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/measurabl-mcp.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/measurabl-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/measurabl-scopes.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/measurabl-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.measurabl.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.measurabl.com/api-docs/
- group: docs
  title: ''
  type: Documentation
  url: https://api.measurabl.com/api-docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.measurabl.com/api-docs/index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://support.measurabl.com/hc/en-us/articles/34695708902541-Measurabl-API-Getting-Started-Guide
- group: operate
  title: ''
  type: Support
  url: https://support.measurabl.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.measurabl.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.measurabl.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Measurabl
- group: start
  title: ''
  type: SignUp
  url: https://app.measurabl.com/users/auth/identities?screen_hint=signup
- group: start
  title: ''
  type: Login
  url: https://app.measurabl.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.measurabl.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.measurabl.com/release_notes
- group: operate
  title: ''
  type: FAQ
  url: https://www.measurabl.com/measurabl-api-faq/
- group: build
  title: ''
  type: CodeSamples
  url: https://github.com/Measurabl/measurabl_api_code_samples
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/measurabl-api/measurabl-core-api/overview
- group: auth
  title: ''
  type: Compliance
  url: https://www.measurabl.com/security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/measurabl-trust-center.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/measurabl-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/measurabl-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/measurabl-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/measurabl-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/measurabl-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/measurabl-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/measurabl-changelog.yml
- group: build
  title: ''
  type: Packages
  url: packages/measurabl-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/measurabl-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-01'
description: 'Measurabl is an ESG (environmental, social and governance) data and sustainability management platform for commercial real estate, used by owners, investors, asset managers and capital-markets participants to measure, manage, report and act on building performance data. The platform covers utility and waste data collection, carbon accounting, green building certifications and ratings, local performance ordinance compliance, CRREM transition-risk analysis, and portfolio and fund-level ESG reporting. Measurabl exposes this through a REST API surface documented in Swagger UI at api.measurabl.com: a Core API for reading and writing portfolios, buildings, spaces, funds, energy/water meters and readings, waste meters, certifications and ratings; an ESGx Buildings (Insights) API for asset-level energy and carbon estimates, certification and ordinance lookups, CRREM lookups and bulk exports; ESGx Securities and ESGx Securities Compliance Files APIs for listed real estate company-level
  and building-level datasets; and a Partner API for partner-side portfolio, building and monthly utility data access. Every API is OpenAPI 3.0.1, secured with OAuth 2.0 client credentials, and returns JSON:API (application/vnd.api+json) documents.'
image: https://www.measurabl.com/wp-content/uploads/2019/06/cropped-measurabl_icon-1-192x192.png
layout: provider
mcp_servers:
- description: ''
  name: Measurabl MCP Server
  slug: measurabl-mcp-server
modified: '2026-08-01'
name: Measurabl
nav: Providers
network: true
overview: 'Measurabl publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Core API, ESGx Buildings API, ESGx Securities API, and 2 more. Tagged areas include ESG, Real-Estate, Sustainability, Carbon Accounting, and Energy Management.


  Measurabl''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 25 more developer resources.'
random_paper: 11
rate_limits:
- limit_count: 3
  name: Measurabl Rate Limits
  slug: measurabl-rate-limits
scopes:
- name: Measurabl Scopes
  scope_count: 0
  slug: measurabl-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 53.0
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 16.7
    contract_quality: 44.3
    developer_ergonomics: 58.9
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 53.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 58.1
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/measurabl/refs/heads/main/screenshots/measurabl-2026-08-07T172304.png
security:
- kind: authentication
  name: Measurabl Authentication
  slug: measurabl-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Measurabl Domain Security
  slug: measurabl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Measurabl Vulnerability Disclosure
  slug: measurabl-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Measurabl Trust Center
  slug: measurabl-trust-center
  summary_line: SOC 2 Type 2, ISO 27001:2013, GDPR, Privacy Shield
slug: measurabl
tags:
- ESG
- Real-Estate
- Sustainability
- Carbon Accounting
- Energy Management
- Building Performance
- Climate Risk
- Benchmarking
- Compliance
- PropTech
- Utility Data
- Capital Markets
website: https://www.measurabl.com/
---
