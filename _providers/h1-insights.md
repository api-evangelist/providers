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
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.3
  scored_at: '2026-08-10'
api_count: 11
apis:
- description: The Cost Estimates API from H1 — 4 operation(s) for cost estimates.
  name: H1 Cost Estimates API
  slug: h1-insights-cost-estimates-api
- description: The Filters API from H1 — 4 operation(s) for filters.
  name: H1 Filters API
  slug: h1-insights-filters-api
- description: The Focus Area Endpoints API from H1 — 6 operation(s) for focus area endpoints.
  name: H1 Focus Area Endpoints API
  slug: h1-insights-focus-area-endpoints-api
- description: The Locations API from H1 — 5 operation(s) for locations.
  name: H1 Locations API
  slug: h1-insights-locations-api
- description: The Networks API from H1 — 1 operation(s) for networks.
  name: H1 Networks API
  slug: h1-insights-networks-api
- description: The Organizations API from H1 — 2 operation(s) for organizations.
  name: H1 Organizations API
  slug: h1-insights-organizations-api
- description: The Price Transparency API from H1 — 8 operation(s) for price transparency.
  name: H1 Price Transparency API
  slug: h1-insights-price-transparency-api
- description: The Providers API from H1 — 10 operation(s) for providers.
  name: H1 Providers API
  slug: h1-insights-providers-api
- description: The Reference Endpoints API from H1 — 13 operation(s) for reference endpoints.
  name: H1 Reference Endpoints API
  slug: h1-insights-reference-endpoints-api
- description: The TINs API from H1 — 2 operation(s) for tins.
  name: H1 TI Ns API
  slug: h1-insights-tins-api
- description: The Virtual Care Platforms API from H1 — 2 operation(s) for virtual care platforms.
  name: H1 Virtual Care Platforms API
  slug: h1-insights-virtual-care-platforms-api
artifact_total: 14
common:
- group: company
  title: ''
  type: Website
  url: https://h1.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ribbon.readme.io/
- group: docs
  title: ''
  type: Documentation
  url: https://ribbon.readme.io/
- group: docs
  title: ''
  type: APIReference
  url: https://ribbon.readme.io/reference/getcustomproviders
- group: start
  title: ''
  type: GettingStarted
  url: https://ribbon.readme.io/docs/welcome-to-the-ribbon-health-api
- group: operate
  title: ''
  type: Support
  url: https://h1.com/company/contact-us/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.h1.co/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://h1.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/h1insights
- group: start
  title: ''
  type: SignUp
  url: https://h1.com/request-demo/
- group: start
  title: ''
  type: Login
  url: https://app.h1insights.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://h1.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://h1.com/privacy-policy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.ribbonhealth.com/
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/h1-insights-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/h1-insights-lifecycle.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/h1-insights-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/h1-insights-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/h1-insights-problem-types.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/h1-insights-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/h1-insights-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/h1-insights-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/h1-insights-well-known.yml
- group: build
  title: ''
  type: Packages
  url: packages/h1-insights-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/h1-insights-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/h1-insights-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/h1-insights-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/h1-insights-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-04'
description: H1 is a healthcare data and intelligence company that builds a unified view of the world's healthcare providers — physicians, care locations, organizations, insurance networks, specialties, clinical focus areas, negotiated prices and quality signals — and makes it available to pharmaceutical, life-science, health-plan and digital-health customers through applications and a REST API. Following its acquisition of Ribbon Health (announced January 2025) the provider-data platform is delivered as "H1 for Health Plans and Digital Health", and the developer-facing product is the H1 Provider Data API (still served from the api.ribbonhealth.com host and documented at ribbon.readme.io). The API covers provider directory search by geography, insurance network, specialty, procedure and quality measure; location and organization search; reference data for insurances, specialties, provider types, location types, procedures, languages, conditions and treatments; customer-specific custom directories,
  custom fields and boost/custom ranking filters; price-transparency search over negotiated rates; procedure cost estimates; and real-time member eligibility and benefits checks. H1 states it serves 200+ customers across six continents, including a majority of the top-20 pharmaceutical companies and most major US health plans.
image: https://h1.com/wp-content/uploads/2022/10/Open-Graph-v2-1200x630.png
layout: provider
mcp_servers:
- description: ''
  name: h1-insights-mcp.yml
  slug: h1-insights-mcpyml
modified: '2026-08-04'
name: H1
nav: Providers
network: true
overview: 'H1 publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Cost Estimates API, Filters API, Focus Area Endpoints API, and 8 more. Tagged areas include healthcare, provider-data, provider-directory, health-insurance, and price-transparency.


  H1''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, signup flow, authentication, and 22 more developer resources.'
random_paper: 27
score:
  band: developing
  composite: 45.4
  delta: -0.3
  facets:
    commercial_clarity: 34.2
    contract_quality: 56.5
    developer_ergonomics: 62.5
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 45.7
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/h1-insights/refs/heads/main/screenshots/h1-insights-2026-08-07T165907.png
security:
- kind: authentication
  name: H1 Insights Authentication
  slug: h1-insights-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: H1 Insights Domain Security
  slug: h1-insights-domain-security
  summary_line: TLSv1.3 · DMARC
slug: h1-insights
tags:
- healthcare
- provider-data
- provider-directory
- health-insurance
- price-transparency
- eligibility
- care-navigation
- health-plans
- digital-health
- life-sciences
- clinical-trials
- reference-data
website: https://h1.com/
---
