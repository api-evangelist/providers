---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.6
  scored_at: '2026-09-01'
api_count: 10
apis:
- description: The Buildings API from Measurabl — 6 operation(s) for buildings.
  name: Measurabl Buildings API
  slug: measurabl-buildings-api
- description: The Carbon Estimates API from Measurabl — 7 operation(s) for carbon estimates.
  name: Measurabl Carbon Estimates API
  slug: measurabl-carbon-estimates-api
- description: The Certification Lookups API from Measurabl — 7 operation(s) for certification lookups.
  name: Measurabl Certification Lookups API
  slug: measurabl-certification-lookups-api
- description: The Certification Types API from Measurabl — 1 operation(s) for certification types.
  name: Measurabl Certification Types API
  slug: measurabl-certification-types-api
- description: The Certifications API from Measurabl — 3 operation(s) for certifications.
  name: Measurabl Certifications API
  slug: measurabl-certifications-api
- description: The Energy and Water Meter Bills API from Measurabl — 1 operation(s) for energy and water meter bills.
  name: Measurabl Energy and Water Meter Bills API
  slug: measurabl-energy-and-water-meter-bills-api
- description: The Energy and Water Meter Readings API from Measurabl — 2 operation(s) for energy and water meter readings.
  name: Measurabl Energy and Water Meter Readings API
  slug: measurabl-energy-and-water-meter-readings-api
- description: The Energy and Water Meter Spaces API from Measurabl — 2 operation(s) for energy and water meter spaces.
  name: Measurabl Energy and Water Meter Spaces API
  slug: measurabl-energy-and-water-meter-spaces-api
- description: The Energy and Water Meters API from Measurabl — 3 operation(s) for energy and water meters.
  name: Measurabl Energy and Water Meters API
  slug: measurabl-energy-and-water-meters-api
- description: The Energy Estimates API from Measurabl — 7 operation(s) for energy estimates.
  name: Measurabl Energy Estimates API
  slug: measurabl-energy-estimates-api
- description: The Exports API from Measurabl — 3 operation(s) for exports.
  name: Measurabl Exports API
  slug: measurabl-exports-api
- description: The Funds API from Measurabl — 2 operation(s) for funds.
  name: Measurabl Funds API
  slug: measurabl-funds-api
- description: The Funds Buildings API from Measurabl — 1 operation(s) for funds buildings.
  name: Measurabl Funds Buildings API
  slug: measurabl-funds-buildings-api
- description: The Listed Real Estate Compliance Files API from Measurabl — 3 operation(s) for listed real estate compliance files.
  name: Measurabl Listed Real Estate Compliance Files API
  slug: measurabl-listed-real-estate-compliance-files-api
- description: The Listed Real Estate Reports API from Measurabl — 8 operation(s) for listed real estate reports.
  name: Measurabl Listed Real Estate Reports API
  slug: measurabl-listed-real-estate-reports-api
- description: The Ordinance Lookups API from Measurabl — 7 operation(s) for ordinance lookups.
  name: Measurabl Ordinance Lookups API
  slug: measurabl-ordinance-lookups-api
- description: The Ordinances API from Measurabl — 1 operation(s) for ordinances.
  name: Measurabl Ordinances API
  slug: measurabl-ordinances-api
- description: The Portfolios API from Measurabl — 3 operation(s) for portfolios.
  name: Measurabl Portfolios API
  slug: measurabl-portfolios-api
- description: The Ratings API from Measurabl — 3 operation(s) for ratings.
  name: Measurabl Ratings API
  slug: measurabl-ratings-api
- description: The Space Certifications API from Measurabl — 2 operation(s) for space certifications.
  name: Measurabl Space Certifications API
  slug: measurabl-space-certifications-api
- description: The Space Ratings API from Measurabl — 1 operation(s) for space ratings.
  name: Measurabl Space Ratings API
  slug: measurabl-space-ratings-api
- description: The Spaces API from Measurabl — 2 operation(s) for spaces.
  name: Measurabl Spaces API
  slug: measurabl-spaces-api
- description: The Waste Meter Readings API from Measurabl — 2 operation(s) for waste meter readings.
  name: Measurabl Waste Meter Readings API
  slug: measurabl-waste-meter-readings-api
- description: The Waste Meters API from Measurabl — 3 operation(s) for waste meters.
  name: Measurabl Waste Meters API
  slug: measurabl-waste-meters-api
artifact_total: 36
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/measurabl-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/measurabl-core-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/measurabl-esgx-buildings-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/measurabl-esgx-securities-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/measurabl-esgx-securities-compliance-files-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/measurabl-partners-overlay.yaml
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
overview: 'Measurabl publishes 24 APIs on the [APIs.io](https://apis.io/) network, including Buildings API, Carbon Estimates API, Certification Lookups API, and 21 more. Tagged areas include ESG, Real-Estate, Sustainability, Carbon Accounting, and Energy Management.


  Measurabl''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, signup flow, and 31 more developer resources.'
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
  composite: 50.0
  coverage:
    artifact_dirs: 21
    catalog_gap: 76.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 4.5
    contract_quality: 51.2
    developer_ergonomics: 58.9
    discoverability: 50.0
    governance: 4.5
    operational_transparency: 50.0
  previous_composite: 50.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 64.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
