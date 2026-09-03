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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.3
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Eia Agentic Access
  operation_count: 278
  slug: eia-agentic-access
  summary_line: 278 operations
api_count: 1
apis:
- description: EIA's bulk data distribution surface, served from the same api.eia.gov host as APIv2 but requiring no API key whatsoever. A single manifest at /bulk/manifest.txt returns a JSON catalog of every bulk d
  name: EIA Bulk Download Facility
  slug: eia-bulk-download-facility
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Annual Energy Outlook Data
  name: EIA AEO API
  slug: eia-aeo-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Coal Data
  name: EIA COAL API
  slug: eia-coal-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Crude Oil Imports Data
  name: EIA CRUD IMPORTS API
  slug: eia-crud-imports-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Densified Biomass Data
  name: EIA DBF API
  slug: eia-dbf-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Electricity Data
  name: EIA ELEC API
  slug: eia-elec-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to CO2 Emissions Data
  name: EIA EMISS API
  slug: eia-emiss-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to International Energy Outlook Data
  name: EIA IEO API
  slug: eia-ieo-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to International Data
  name: EIA INTL API
  slug: eia-intl-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Natural Gas Data
  name: EIA NG API
  slug: eia-ng-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Nuclear Outages Data
  name: EIA NUC STATUS API
  slug: eia-nuc-status-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Available EIA API Datasets
  name: EIA Root API
  slug: eia-root-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Daily Electricity Data
  name: EIA RTO API
  slug: eia-rto-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to State Energy Data Systems (SEDS) Data
  name: EIA SEDS API
  slug: eia-seds-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to State Electricity Profiles
  name: EIA SEP API
  slug: eia-sep-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Short Term Energy Outlook Data
  name: EIA STEO API
  slug: eia-steo-api
- baseURL: https://api.eia.gov/v2
  baseurl_source: declared
  description: Access to Total Energy Data
  name: EIA TOTAL API
  slug: eia-total-api
artifact_total: 24
collections:
- collection_type: open
  name: EIA APIv2
  slug: open-eia-api-v2
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/eia-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/eia-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/eia-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.eia.gov
- group: start
  title: ''
  type: Portal
  url: https://www.eia.gov/opendata/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/opendata/documentation.php
- group: start
  title: ''
  type: SignUp
  url: https://www.eia.gov/opendata/register.php
- group: start
  title: ''
  type: Console
  url: https://www.eia.gov/opendata/browser/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.eia.gov/about/privacy_security_policy.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/EIAgov
- group: other
  title: ''
  type: DataCatalog
  url: https://www.energy.gov/data.json
- group: build
  title: ''
  type: Tools
  url: https://www.eia.gov/tools/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/opendata/excel/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/electricity/gridmonitor/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/electricity/wholesalemarkets/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/survey/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.eia.gov/opendata/
- group: docs
  title: ''
  type: APIReference
  url: https://www.eia.gov/opendata/browser/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.eia.gov/opendata/documentation.php
- group: operate
  title: ''
  type: Support
  url: https://www.eia.gov/opendata/faqs.php
- group: operate
  title: ''
  type: HelpCenter
  url: https://www.eia.gov/about/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.eia.gov/todayinenergy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.eia.gov/opendata/register.php
- group: other
  title: ''
  type: Copyright
  url: https://www.eia.gov/about/copyrights_reuse.php
- group: build
  title: ''
  type: Packages
  url: packages/eia-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/eia-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/eia-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/eia-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/eia-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/eia-api-v2-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/eia-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/eia-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/eia-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://www.eia.gov/opendata/faqs.php
- group: design
  title: ''
  type: Conventions
  url: conventions/eia-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.eia.gov/opendata/documentation.php
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/eia-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/eia-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/eia-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/eia-api-v2-examples.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/eia-rate-limits.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/eia-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.energy.gov/cio/articles/vulnerability-disclosure-policy
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-27'
description: The U.S. Energy Information Administration (EIA) is the independent statistical and analytical agency within the U.S. Department of Energy, created by the Department of Energy Organization Act of 1977, that collects, analyzes, and disseminates energy information for the United States. EIA sits at the measurement layer of the American energy value chain rather than the operating layer - it does not generate, transmit, distribute, or retail energy, and it does not regulate anyone. Instead it compels the industry to report through mandatory survey forms (EIA-860, EIA-861, EIA-923, EIA-176, EIA-914, EIA-930 and dozens more) and then publishes the result as the reference statistics for electricity, natural gas, petroleum, coal, nuclear, renewables, emissions, and international energy. EIA's API posture is the strongest of any organization in this sector and a genuine benchmark for government data anywhere. The Open Data APIv2 at api.eia.gov/v2 is a fully RESTful, self-documenting,
  hierarchically routed API covering more than two million time series, described by a real downloadable OpenAPI 3.0.0 contract carrying 225 paths and 278 operations, opened by a free API key that is emailed automatically from a public registration form with no review, no accreditation, and no licence to sign. A companion bulk download facility at api.eia.gov/bulk serves the same data as manifest-indexed zip archives and requires no key at all. The split that defines this sector is absolute here. EIA's market, system, and grid data is wide open - hourly balancing-authority demand and interchange, wholesale and spot prices, generator-level capacity and operations - while EIA publishes no consumer energy data API of any kind. There is no Green Button, no ESPI, no Download My Data, no Connect My Data, no consent flow, and no customer usage or billing endpoint, because individual customer data is never collected by EIA in the first place; its surveys arrive already aggregated from utilities
  and are further protected by statutory confidentiality. EIA is therefore the clearest instance of the recurring finding in this series - a federal data agency that publishes a far better documented, far more accessible API than the regulated utilities whose numbers it reports.
image: https://www.eia.gov/global/images/logos/eia_logo_print.png
layout: provider
mcp_servers:
- description: ''
  name: No first-party MCP server; two community stdio servers over APIv2, plus a derived candidate tool set
  slug: no-first-party-mcp-server-two-community-stdio-servers-over-apiv2-plus-a-derived-candidate-tool-set
modified: '2026-07-27'
name: EIA
nav: Providers
network: true
overview: 'EIA publishes 16 APIs on the [APIs.io](https://apis.io/) network, including AEO API, COAL API, CRUD IMPORTS API, and 13 more. Tagged areas include Energy, United States, Energy Markets, Electricity, and Natural Gas.


  EIA''s developer surface includes authentication, developer portal, documentation, signup flow, developer console, tooling, API reference, and 37 more developer resources.'
random_paper: 9
rate_limits:
- limit_count: 2
  name: Eia Rate Limits
  slug: eia-rate-limits
score:
  band: developing
  composite: 50.5
  coverage:
    artifact_dirs: 22
    catalog_gap: 70.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 4.5
    contract_quality: 45.5
    developer_ergonomics: 66.1
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 57.9
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 41.9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/eia/refs/heads/main/screenshots/eia-2026-08-07T164749.png
security:
- kind: authentication
  name: Eia Authentication
  slug: eia-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Eia Domain Security
  slug: eia-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Eia Vulnerability Disclosure
  slug: eia-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: eia
tags:
- Energy
- United States
- Energy Markets
- Electricity
- Natural Gas
- Petroleum
- Coal
- Nuclear
- Renewables
- Grid
- Emissions
- Government
- Open Data
- Energy Statistics
website: https://www.eia.gov
---
