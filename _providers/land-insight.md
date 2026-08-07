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
    mcp_server: derived
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 46.2
  scored_at: '2026-08-06'
api_count: 12
apis:
- description: Endpoint to get details of sites from Homes England Land Hub
  name: Land Insight Additional Opportunities API
  slug: land-insight-additional-opportunities-api
- description: Endpoint to get details of various development constraints. Includes airport, HS2, rail and building (wharf) safeguarding. Also includes article 4 and national landscape data.
  name: Land Insight Development Constraints API
  slug: land-insight-development-constraints-api
- description: Endpoint to get details of Named Regeneration Areas and Area Action Plans
  name: Land Insight Development Opportunities API
  slug: land-insight-development-opportunities-api
- description: Endpoints to help you understand how to interact with the API.
  name: Land Insight Getting Started API
  slug: land-insight-getting-started-api
- description: Endpoint to get details about Land Availability Assessment sites
  name: Land Insight Land Availability Assessment API
  slug: land-insight-land-availability-assessment-api
- description: Endpoint to get details of local plan policies
  name: Land Insight Local Policy API
  slug: land-insight-local-policy-api
- description: Endpoints to get details about land ownership and property information.
  name: Land Insight Ownership API
  slug: land-insight-ownership-api
- description: Endpoints to search for parcels and associated attributes.
  name: Land Insight Parcels API
  slug: land-insight-parcels-api
- description: Endpoints to search for planning applications and get details on individual applications.
  name: Land Insight Planning Applications API
  slug: land-insight-planning-applications-api
- description: Endpoint to get details of substations, lines, cables and towers
  name: Land Insight Power API
  slug: land-insight-power-api
- description: Endpoint to get details on sites from the Renewable Energy Planning Database
  name: Land Insight Renewable Energy Planning DB API
  slug: land-insight-renewable-energy-planning-db-api
- description: Endpoint for details on strategic industrial location
  name: Land Insight Strategic Industrial Location API
  slug: land-insight-strategic-industrial-location-api
artifact_total: 16
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/land-insight-trust-center.yml
- group: company
  title: ''
  type: Website
  url: https://land.tech
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.land.tech/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.land.tech/openapi
- group: docs
  title: ''
  type: APIReference
  url: https://developers.land.tech/openapi
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.land.tech/openapi/getting-started/getauthstatus
- group: operate
  title: ''
  type: Support
  url: https://support.land.tech/en/
- group: company
  title: ''
  type: Blog
  url: https://land.tech/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/landtechnologies
- group: build
  title: ''
  type: Packages
  url: packages/land-insight-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://land.tech/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.land.tech/landinsight/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://land.tech/legal/website_terms_of_use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://land.tech/legal/privacy
- group: auth
  title: ''
  type: Compliance
  url: https://land.tech/blog/security
- group: auth
  title: ''
  type: Authentication
  url: authentication/land-insight-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/land-insight-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/land-insight-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/land-insight-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/land-insight-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/land-insight-data-model.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/land-insight-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/land-insight-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/land-insight-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/land-insight-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LandTech (land.tech) is a UK property technology company whose LandInsight platform is used by developers, land agents, planners and investors to source and assess development sites. It combines HM Land Registry ownership and title data, planning applications, local plan policy, development constraints (Green Belt, flood zones, Article 4 directions, heritage designations), Land Availability Assessments, brownfield and regeneration opportunities, EPC and property attributes, and electricity network / renewable energy infrastructure into a single map-based product. Alongside LandInsight the company ships LandFund for development finance appraisal and Give My View for community engagement. The LandTech API exposes the same UK land and planning datasets as a paid HTTP product so customers can feed parcel search, ownership, planning application and constraint data into their own internal or customer-facing systems.
image: https://land.tech/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: land-insight-mcp.yml
  slug: land-insight-mcpyml
modified: '2026-07-19'
name: Land Insight
nav: Providers
network: true
overview: 'Land Insight publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Additional Opportunities API, Development Constraints API, Development Opportunities API, and 9 more. Tagged areas include Company, Real Estate, Property, Land, and Planning.


  Land Insight''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 19 more developer resources.'
random_paper: 88
score:
  band: developing
  composite: 50.3
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 62.7
    developer_ergonomics: 56.0
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 50.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/land-insight/refs/heads/main/screenshots/land-insight-2026-07-25T224458.png
security:
- kind: authentication
  name: Land Insight Authentication
  slug: land-insight-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Land Insight Domain Security
  slug: land-insight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Land Insight Trust Center
  slug: land-insight-trust-center
  summary_line: ISO 27001, GDPR
slug: land-insight
tags:
- Company
- Real Estate
- Property
- Land
- Planning
- Geospatial
- Data
- United Kingdom
- PropTech
- Construction
website: https://land.tech
---
