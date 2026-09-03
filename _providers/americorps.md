---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Americorps Agentic Access
  operation_count: 4
  slug: americorps-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: The AmeriCorps Open Data portal provides programmatic access to AmeriCorps research, evaluation, and program datasets via the Socrata Open Data API (SODA). The portal includes datasets on program outc
  name: AmeriCorps Open Data SODA API
  slug: americorps-open-data-soda-api
- baseURL: https://data.americorps.gov/resource
  baseurl_source: declared
  description: Discover datasets published on the AmeriCorps open data portal.
  name: AmeriCorps Catalog API
  slug: americorps-catalog-api
- baseURL: https://data.americorps.gov/resource
  baseurl_source: declared
  description: Retrieve dataset rows via the Socrata SODA resource endpoint.
  name: AmeriCorps Datasets API
  slug: americorps-datasets-api
- baseURL: https://data.americorps.gov/resource
  baseurl_source: declared
  description: Retrieve dataset metadata and schema information.
  name: AmeriCorps Metadata API
  slug: americorps-metadata-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AmeriCorps Open Data Catalog API
  slug: open-americorps-catalog-api
- collection_type: open
  name: AmeriCorps Open Data Catalog Datasets API
  slug: open-americorps-datasets-api
- collection_type: open
  name: AmeriCorps Open Data Catalog Metadata API
  slug: open-americorps-metadata-api
- collection_type: open
  name: AmeriCorps Open Data API
  slug: open-americorps
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/americorps-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/americorps-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/americorps-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/americorps
- group: company
  title: ''
  type: Website
  url: https://americorps.gov
- group: start
  title: ''
  type: Portal
  url: https://data.americorps.gov
- group: other
  title: ''
  type: DataAPI
  url: https://data.americorps.gov/api/views
- group: start
  title: ''
  type: GettingStarted
  url: https://dev.socrata.com/docs/endpoints.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/americorps
- group: other
  title: ''
  type: DataCatalog
  url: https://data.americorps.gov/data.json
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.americorps.gov/about/agency-overview/privacy-policy
- group: build
  title: ''
  type: Packages
  url: packages/americorps-packages.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/americorps-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/americorps-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/americorps-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/americorps-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/americorps-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/americorps-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socrata.com
- group: design
  title: ''
  type: Conventions
  url: conventions/americorps-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/americorps-data-model.yml
- group: auth
  title: ''
  type: Security
  url: security/americorps-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/americorps-vulnerability-disclosure.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/americorps-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/americorps-rate-limits.yml
created: '2024-11-21'
description: AmeriCorps is a federal agency that engages millions of Americans in service to their communities through programs including AmeriCorps State and National, AmeriCorps VISTA, AmeriCorps NCCC, AmeriCorps Seniors, and the Volunteer Generation Fund. Established in 1993 under the Corporation for National and Community Service (CNCS), AmeriCorps addresses critical community needs in education, disaster response, environmental conservation, economic opportunity, and healthy futures. The agency operates the AmeriCorps Open Data portal (data.americorps.gov) providing programmatic access to research, evaluation, and program data via the Socrata Open Data API (SODA).
features:
- description: Program engaging more than 75,000 Americans in intensive service through nonprofits, schools, public agencies, and community organizations addressing critical needs across all 50 states.
  name: AmeriCorps State and National
- description: Volunteers in Service to America (VISTA) program placing members with nonprofits and public agencies to build capacity and fight poverty.
  name: AmeriCorps VISTA
- description: National Civilian Community Corps residential service program for young adults completing team-based service projects on environmental and disaster relief efforts.
  name: AmeriCorps NCCC
- description: Programs engaging adults 55 and older in volunteer service through RSVP, Foster Grandparents, and Senior Companions programs.
  name: AmeriCorps Seniors
- description: Research and evaluation data portal (data.americorps.gov) providing SODA API access to program effectiveness studies, member outcome data, and ROI analyses.
  name: Evidence Exchange Open Data
- description: Grant program supporting organizations that recruit, manage, and support volunteers to meet critical community needs.
  name: Volunteer Generation Fund
finops:
- name: Americorps Finops
  service_category: API
  slug: americorps-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/americorps.png
integrations:
- description: Standard Socrata SODA API integration enabling applications to query, filter, and aggregate AmeriCorps program data programmatically.
  name: Socrata Open Data API
- description: OData V2 and V4 endpoints enabling connection to Microsoft Excel, Tableau, Power BI, and other business intelligence tools.
  name: OData Endpoints
- description: AmeriCorps eGrants system for grantee organizations to submit applications, manage awards, and report on AmeriCorps program activities.
  name: eGrants Grant Management System
layout: provider
mcp_servers:
- description: ''
  name: AmeriCorps MCP Server
  slug: americorps-mcp-server
modified: '2026-09-02'
name: AmeriCorps
nav: Providers
network: true
overview: 'AmeriCorps publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API, Datasets API, and Metadata API. Tagged areas include Federal-Government, National Service, Volunteerism, Community Development, and Civic Engagement.


  AmeriCorps'' developer surface includes authentication, developer portal, getting-started guide, and 23 more developer resources.'
plans:
- name: Americorps Plans Pricing
  plan_count: 0
  slug: americorps-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Americorps Rate Limits
  slug: americorps-rate-limits
score:
  band: developing
  composite: 42.8
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 9.6
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 44.6
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 33.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 50.0
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/americorps/refs/heads/main/screenshots/americorps-2026-06-20T171928.png
security:
- kind: authentication
  name: Americorps Authentication
  slug: americorps-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Americorps Domain Security
  slug: americorps-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Americorps Vulnerability Disclosure
  slug: americorps-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: americorps
tags:
- Federal-Government
- National Service
- Volunteerism
- Community Development
- Civic Engagement
- Education
- Disaster Response
- Environmental Conservation
use_cases:
- description: Accessing AmeriCorps program evaluation reports and impact data via the SODA API to conduct independent research on national service effectiveness.
  name: Program Evaluation Research
- description: Partners and grantees accessing program data and reporting resources to manage AmeriCorps grants and measure member outcomes.
  name: Grant Management and Reporting
- description: Analyzing volunteer engagement patterns, member satisfaction data, and civic participation trends using AmeriCorps open datasets.
  name: Volunteer Engagement Analytics
- description: Accessing return-on-investment studies, evidence snapshots, and program outcome data to support policy development and advocacy for national service.
  name: Policy and Advocacy Research
website: https://americorps.gov
---
