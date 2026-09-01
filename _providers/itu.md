---
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
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Itu Agentic Access
  operation_count: 20
  slug: itu-agentic-access
  summary_line: 20 operations · 2 acting
api_count: 2
apis:
- description: Curated DataHub dashboard definitions.
  name: ITU Dashboards API
  slug: itu-dashboards-api
- description: Indicator time series, by indicator, country and region aggregate.
  name: ITU Data API
  slug: itu-data-api
- description: ICT Development Index composite scores.
  name: ITU IDI API
  slug: itu-idi-api
- description: The indicator dictionary — categories, definitions, units and coverage.
  name: ITU Indicators API
  slug: itu-indicators-api
- description: Dataset provenance and the owning ITU divisions.
  name: ITU Methodology API
  slug: itu-methodology-api
- description: Batch proximity scoring of coordinates against the ITU Interactive Transmission Map.
  name: ITU Proximity API
  slug: itu-proximity-api
- description: Country and region reference data.
  name: ITU Reference API
  slug: itu-reference-api
- description: Universal and Meaningful Connectivity targets and scores.
  name: ITU UMC API
  slug: itu-umc-api
artifact_total: 14
collections:
- collection_type: open
  name: ITU DataHub API
  slug: open-itu-datahub
- collection_type: open
  name: ITU Proximity to Fibre Node API
  slug: open-itu-proximity
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/itu-datahub-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/itu-proximity-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/itu-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/itu-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/itu-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/itu-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/itu-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/itu-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/itu-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/itu-data-model.yml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/itu-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/itu-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/itu-llms.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://bbmaps.itu.int/llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.itu.int/
- group: docs
  title: ''
  type: Documentation
  url: https://www.itu.int/en/ITU-T/publications/Pages/recs.aspx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ITUINT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/itu
- group: company
  title: ''
  type: Blog
  url: https://www.itu.int/hub/
- group: operate
  title: ''
  type: Support
  url: https://www.itu.int/home/contact/index.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.itu.int/en/about/Pages/terms-of-use.aspx
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.itu.int/en/about/Pages/privacy-notice.aspx
created: '2026-07-25'
description: 'The International Telecommunication Union (ITU) is the United Nations specialized agency for information and communication technologies, headquartered in Geneva and made up of 194 Member States plus roughly 1,000 sector members. It sits at the top of the global telecom value chain rather than inside it: ITU-R allocates the global radio spectrum and manages the master international frequency register and satellite filings, ITU-T publishes the Recommendations that define interoperable telecom networks, and ITU-D collects and publishes the world''s reference ICT statistics. Its market is Global by treaty. Its API posture is genuinely open but entirely undeclared: ITU operates real, anonymously callable HTTP APIs behind the DataHub statistics portal and behind an ITU-D "Proximity to Fibre Node" demonstration built on the ITU Broadband Maps, and neither requires a key, a login, or a partner agreement — but there is no developer portal, no api.itu.int, no published OpenAPI, no SDK,
  no terms of programmatic use, and the official ITU GitHub organization has zero public repositories. ITU is not a CAMARA participant and not a GSMA Open Gateway operator; network APIs are being standardised outside the UN system, and ITU''s role in that layer is limited to the IMT requirements framework rather than any callable interface.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
mcp_servers:
- description: ''
  name: ITU MCP Server
  slug: itu-mcp-server
modified: '2026-07-26'
name: ITU
nav: Providers
network: true
overview: 'ITU publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Dashboards API, Data API, IDI API, and 5 more. Tagged areas include Telecommunications, Global, Regulator, Standards, and Spectrum.


  ITU''s developer surface includes authentication, code examples, documentation, engineering blog, support, and 19 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 26.2
  coverage:
    artifact_dirs: 19
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 15.8
    developer_ergonomics: 37.5
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 26.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.1
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/itu/refs/heads/main/screenshots/itu-2026-08-07T170931.png
security:
- kind: authentication
  name: Itu Authentication
  slug: itu-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Itu Domain Security
  slug: itu-domain-security
  summary_line: TLSv1.3 · DMARC
slug: itu
tags:
- Telecommunications
- Global
- Regulator
- Standards
- Spectrum
- Satellite
- Broadband
- ICT Statistics
- Open Data
- United Nations
website: https://www.itu.int/
---
