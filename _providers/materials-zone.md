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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Materials Zone Agentic Access
  operation_count: 35
  slug: materials-zone-agentic-access
  summary_line: 35 operations · 25 acting
api_count: 1
apis:
- description: Files are used to store data not related to specific items.
  name: Materials Zone files API
  slug: materials-zone-files-api
- description: Folders are used to organize other Folders and Tables.
  name: Materials Zone folders API
  slug: materials-zone-folders-api
- description: Items are the rows in tables.
  name: Materials Zone items API
  slug: materials-zone-items-api
- description: Jobs are used to perform long running tasks.
  name: Materials Zone jobs API
  slug: materials-zone-jobs-api
- description: Measurements are the files that are uploaded to the system and can be parsed.
  name: Materials Zone measurements API
  slug: materials-zone-measurements-api
- description: Parameters are used to define the structure of columns in tables.
  name: Materials Zone parameters API
  slug: materials-zone-parameters-api
- description: Parsers are used to convert instrument specific output files to a MaterialsZone common format.
  name: Materials Zone parsers API
  slug: materials-zone-parsers-api
- description: Protocols are used to group parameters in tables.
  name: Materials Zone protocols API
  slug: materials-zone-protocols-api
- description: Tables are organized in folders, and contain Items.
  name: Materials Zone tables API
  slug: materials-zone-tables-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Materials Zone files API
  slug: open-materials-zone-files-api
- collection_type: open
  name: Materials Zone files folders API
  slug: open-materials-zone-folders-api
- collection_type: open
  name: Materials Zone files items API
  slug: open-materials-zone-items-api
- collection_type: open
  name: Materials Zone files jobs API
  slug: open-materials-zone-jobs-api
- collection_type: open
  name: Materials Zone files measurements API
  slug: open-materials-zone-measurements-api
- collection_type: open
  name: Materials Zone files parameters API
  slug: open-materials-zone-parameters-api
- collection_type: open
  name: Materials Zone files parsers API
  slug: open-materials-zone-parsers-api
- collection_type: open
  name: Materials Zone files protocols API
  slug: open-materials-zone-protocols-api
- collection_type: open
  name: Materials Zone files tables API
  slug: open-materials-zone-tables-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/materials-zone-mcp.yml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/materials-zone-openapi.json
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.materials.zone/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.materials.zone/
- group: docs
  title: ''
  type: APIReference
  url: https://api.materials.zone/v2beta1/swagger.json
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.materials.zone/
- group: auth
  title: ''
  type: Authentication
  url: authentication/materials-zone-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/materials-zone-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/materials-zone-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/materials-zone-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/materials-zone-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/materials-zone-conformance.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/materials-zone-openapi-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/materials-zone-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/materials-zone-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/materials-zone-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.materials.zone/blog
- group: start
  title: ''
  type: Login
  url: https://app.materials.zone/signin
- group: operate
  title: ''
  type: Support
  url: mailto:contact@materials.zone
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.materials.zone/legals/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.materials.zone/legals/privacy-policy
- group: company
  title: ''
  type: Website
  url: https://www.materials.zone/
created: '2026-07-17'
description: Materials Zone (MaterialsZone) is a materials-informatics platform that centralizes materials R&D data into a single, structured source of truth. Its RESTful API integrates with lab instruments and supports Python scripts and analytical tools, letting teams automate workflows, connect diverse data sources, and run domain-specific analysis. Data is organized as Folders > Tables > Items, enriched with Parameters, Values, Measurements, Protocols and Parsers, with per-organization data segregation and encryption in transit and at rest. The company is a portfolio company of Insight Partners.
image: https://cdn.prod.website-files.com/66a76467298c454de539f7aa/66cef238e96d8f1502659d8f_WebClip%20%20256x256.png
layout: provider
mcp_servers:
- description: ''
  name: Materials Zone MCP Server
  slug: materials-zone-mcp-server
modified: '2026-07-20'
name: Materials Zone
nav: Providers
network: true
overview: 'Materials Zone publishes 9 APIs on the [APIs.io](https://apis.io/) network, including files API, folders API, items API, and 6 more. Tagged areas include Company, Materials Informatics, Materials Science, Research and Development, and Laboratory Data.


  Materials Zone''s developer surface includes documentation, API reference, getting-started guide, authentication, engineering blog, support, and 17 more developer resources.'
random_paper: 2
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 58.2
    developer_ergonomics: 28.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 0.0
  previous_composite: 36.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 31.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/materials-zone/refs/heads/main/screenshots/materials-zone-2026-07-25T230407.png
security:
- kind: authentication
  name: Materials Zone Authentication
  slug: materials-zone-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Materials Zone Domain Security
  slug: materials-zone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: materials-zone
tags:
- Company
- Materials Informatics
- Materials Science
- Research and Development
- Laboratory Data
- Data Management
- Life Sciences
website: https://www.materials.zone/
---
