---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 40.6
  scored_at: '2026-09-02'
api_count: 1
apis:
- baseURL: https://api.bezerocarbonmarkets.com/v3
  baseurl_source: declared
  description: The Projects API from BeZero Carbon — 1 operation(s) for projects.
  name: BeZero Carbon Projects API
  slug: bezero-carbon-projects-api
- baseURL: https://api.bezerocarbonmarkets.com/v3
  baseurl_source: declared
  description: The Ratings API from BeZero Carbon — 3 operation(s) for ratings.
  name: BeZero Carbon Ratings API
  slug: bezero-carbon-ratings-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: BeZero Ratings Projects API
  slug: open-bezero-carbon-projects-api
- collection_type: open
  name: BeZero Ratings API
  slug: open-bezero-carbon-ratings-api
common:
- group: company
  title: ''
  type: Website
  url: https://bezerocarbon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.bezerocarbonmarkets.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.bezerocarbonmarkets.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.bezerocarbonmarkets.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.bezerocarbonmarkets.com/#section/Authentication-and-credential-provision
- group: operate
  title: ''
  type: Support
  url: mailto:engineering@bezerocarbon.com
- group: company
  title: ''
  type: Blog
  url: https://bezerocarbon.com/insights
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BeZeroCarbon
- group: start
  title: ''
  type: SignUp
  url: https://bezerocarbonmarkets.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://legal.bezerocarbon.com/legal-hub/terms-of-use-976d0f8d
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://legal.bezerocarbon.com/legal-hub/privacy-policy-b92ddd45
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/bezero-carbon-ratings-openapi.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/bezero-carbon-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/bezero-carbon-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bezero-carbon-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/bezero-carbon-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/bezero-carbon-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/bezero-carbon-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://legal.bezerocarbon.com/legal-hub/product-specific-terms-ffc0b2c9
- group: design
  title: ''
  type: Conformance
  url: conformance/bezero-carbon-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/bezero-carbon-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/bezero-carbon-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bezero-carbon-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/bezero-carbon-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/bezero-carbon-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/bezero-carbon-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/bezero-carbon-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/bezero-carbon-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/bezero-carbon-ratings-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-07'
description: BeZero Carbon is a global carbon ratings agency for the Voluntary Carbon Market, founded in London in 2020. It publishes an independent, eight-point BeZero Carbon Rating (AAA to D) expressing the likelihood that a given carbon credit achieves a tonne of CO2e avoided or removed, alongside risk factor scores, summary analysis, methodology assessments and reference data across forestry, blue carbon, soil and agriculture, cookstoves, engineered removals and superpollutant projects. The BeZero Ratings API (v3, OAuth 2.0 client credentials) lets exchanges, marketplaces, brokers, data providers and corporate buyers pull ratings, project reference data and premium risk factor scores directly into their own platforms, and its ratings are distributed through Bloomberg, ICE, CUSIP and LSEG.
image: https://bezerocarbon.com/images/metadata-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: BeZero Carbon MCP Server
  slug: bezero-carbon-mcp-server
modified: '2026-08-07'
name: BeZero Carbon
nav: Providers
network: true
overview: 'BeZero Carbon publishes 2 APIs on the [APIs.io](https://apis.io/) network: Projects API and Ratings API. Tagged areas include Company, Carbon Ratings, Carbon Markets, Climate, and Sustainability.


  BeZero Carbon''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 23 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 1
  name: Bezero Carbon Rate Limits
  slug: bezero-carbon-rate-limits
scopes:
- name: Bezero Carbon Scopes
  scope_count: 4
  slug: bezero-carbon-scopes
  summary_line: 4 scopes · clientCredentials
score:
  band: developing
  composite: 41.5
  coverage:
    artifact_dirs: 19
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 60.8
    developer_ergonomics: 53.0
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 31.6
  previous_composite: 41.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bezero-carbon/refs/heads/main/screenshots/bezero-carbon-2026-08-07T162353.png
security:
- kind: authentication
  name: Bezero Carbon Authentication
  slug: bezero-carbon-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Bezero Carbon Domain Security
  slug: bezero-carbon-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: bezero-carbon
tags:
- Company
- Carbon Ratings
- Carbon Markets
- Climate
- Sustainability
- ESG
- Ratings
- Reference Data
- Market Intelligence
- Risk Analysis
website: https://bezerocarbon.com/
---
