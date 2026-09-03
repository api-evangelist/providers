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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.2
  scored_at: '2026-09-03'
api_count: 1
apis:
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details of sites from Homes England Land Hub
  name: Land Insight Additional Opportunities API
  slug: land-insight-additional-opportunities-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details of various development constraints. Includes airport, HS2, rail and building (wharf) safeguarding. Also includes article 4 and national landscape data.
  name: Land Insight Development Constraints API
  slug: land-insight-development-constraints-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details of Named Regeneration Areas and Area Action Plans
  name: Land Insight Development Opportunities API
  slug: land-insight-development-opportunities-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoints to help you understand how to interact with the API.
  name: Land Insight Getting Started API
  slug: land-insight-getting-started-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details about Land Availability Assessment sites
  name: Land Insight Land Availability Assessment API
  slug: land-insight-land-availability-assessment-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details of local plan policies
  name: Land Insight Local Policy API
  slug: land-insight-local-policy-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoints to get details about land ownership and property information.
  name: Land Insight Ownership API
  slug: land-insight-ownership-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoints to search for parcels and associated attributes.
  name: Land Insight Parcels API
  slug: land-insight-parcels-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoints to search for planning applications and get details on individual applications.
  name: Land Insight Planning Applications API
  slug: land-insight-planning-applications-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details of substations, lines, cables and towers
  name: Land Insight Power API
  slug: land-insight-power-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint to get details on sites from the Renewable Energy Planning Database
  name: Land Insight Renewable Energy Planning DB API
  slug: land-insight-renewable-energy-planning-db-api
- baseURL: https://app.land.tech/api
  baseurl_source: declared
  description: Endpoint for details on strategic industrial location
  name: Land Insight Strategic Industrial Location API
  slug: land-insight-strategic-industrial-location-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: LandTech Additional Opportunities API
  slug: open-land-insight-additional-opportunities-api
- collection_type: open
  name: LandTech Additional Opportunities Development Constraints API
  slug: open-land-insight-development-constraints-api
- collection_type: open
  name: LandTech Additional Opportunities Development Opportunities API
  slug: open-land-insight-development-opportunities-api
- collection_type: open
  name: LandTech Additional Opportunities Getting Started API
  slug: open-land-insight-getting-started-api
- collection_type: open
  name: LandTech Additional Opportunities Land Availability Assessment API
  slug: open-land-insight-land-availability-assessment-api
- collection_type: open
  name: LandTech Additional Opportunities Local Policy API
  slug: open-land-insight-local-policy-api
- collection_type: open
  name: LandTech Additional Opportunities Ownership API
  slug: open-land-insight-ownership-api
- collection_type: open
  name: LandTech Additional Opportunities Parcels API
  slug: open-land-insight-parcels-api
- collection_type: open
  name: LandTech Additional Opportunities Planning Applications API
  slug: open-land-insight-planning-applications-api
- collection_type: open
  name: LandTech Additional Opportunities Power API
  slug: open-land-insight-power-api
- collection_type: open
  name: LandTech Additional Opportunities Renewable Energy Planning DB API
  slug: open-land-insight-renewable-energy-planning-db-api
- collection_type: open
  name: LandTech Additional Opportunities Strategic Industrial Location API
  slug: open-land-insight-strategic-industrial-location-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/land-insight-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/land-insight-api-overlay.yaml
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
  type: X-MCPServerCandidate
  url: mcp/land-insight-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: LandTech (land.tech) is a UK property technology company whose LandInsight platform is used by developers, land agents, planners and investors to source and assess development sites. It combines HM Land Registry ownership and title data, planning applications, local plan policy, development constraints (Green Belt, flood zones, Article 4 directions, heritage designations), Land Availability Assessments, brownfield and regeneration opportunities, EPC and property attributes, and electricity network / renewable energy infrastructure into a single map-based product. Alongside LandInsight the company ships LandFund for development finance appraisal and Give My View for community engagement. The LandTech API exposes the same UK land and planning datasets as a paid HTTP product so customers can feed parcel search, ownership, planning application and constraint data into their own internal or customer-facing systems.
image: https://land.tech/favicon.ico
layout: provider
modified: '2026-07-19'
name: Land Insight
nav: Providers
network: true
overview: 'Land Insight publishes 12 APIs on the [APIs.io](https://apis.io/) network, including Additional Opportunities API, Development Constraints API, Development Opportunities API, and 9 more. Tagged areas include Company, Real-Estate, Property, Land, and Planning.


  Land Insight''s developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, signup flow, and 21 more developer resources.'
random_paper: 0
score:
  band: developing
  composite: 46.6
  coverage:
    artifact_dirs: 18
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 60.5
    commercial_clarity: 60.5
    contract_governance: 4.5
    contract_quality: 56.9
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 46.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: derived
    skills: derived
  schema_version: 0.18.2
  scored_at: '2026-09-03'
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
- Real-Estate
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
