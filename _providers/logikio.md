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
    agentic_access: derived
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Logikio Agentic Access
  operation_count: 36
  slug: logikio-agentic-access
  summary_line: 36 operations · 16 acting
api_count: 4
apis:
- description: Export Blueprints
  name: Logik.io Blueprint > Export API
  slug: logikio-blueprint-export-api
- description: Import Blueprints
  name: Logik.io Blueprint > Import API
  slug: logikio-blueprint-import-api
- description: APIs to retrieve BOM information
  name: Logik.io BOM API
  slug: logikio-bom-api
- description: APIs to operate on Configuration blueprint to generate BOM
  name: Logik.io Configuration API
  slug: logikio-configuration-api
- description: Creating new configurations, reconfiguring existing configurations, making updates to a configuration and saving changes.
  name: Logik.io Configuration (V2) API
  slug: logikio-configuration-v2-api
- description: Export and Download Tables
  name: Logik.io Managed Tables > Export Tables API
  slug: logikio-managed-tables-export-tables-api
- description: Import and Replace Tables
  name: Logik.io Managed Tables > Import Tables API
  slug: logikio-managed-tables-import-tables-api
- description: Working with Table Metadata
  name: Logik.io Managed Tables > Metadata API
  slug: logikio-managed-tables-metadata-api
- description: Working with individual Table Rows
  name: Logik.io Managed Tables > Table Rows API
  slug: logikio-managed-tables-table-rows-api
- description: Listing all Tables and working with indiviudal Tables
  name: Logik.io Managed Tables > Tables API
  slug: logikio-managed-tables-tables-api
- description: Get Bill of Materials (BOM) information for a given configuration UUID.
  name: Logik.io Runtime - Bill of Materials API
  slug: logikio-runtime-bill-of-materials-api
artifact_total: 30
collections:
- collection_type: postman
  name: Logik Configurator Runtime APIs
  slug: postman-logikio-runtime
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export API
  slug: open-logikio-blueprint-export-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Blueprint > Import API
  slug: open-logikio-blueprint-import-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export BOM API
  slug: open-logikio-bom-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Configuration API
  slug: open-logikio-configuration-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Configuration (V2) API
  slug: open-logikio-configuration-v2-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Managed Tables > Export Tables API
  slug: open-logikio-managed-tables-export-tables-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Managed Tables > Import Tables API
  slug: open-logikio-managed-tables-import-tables-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Managed Tables > Metadata API
  slug: open-logikio-managed-tables-metadata-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Managed Tables > Table Rows API
  slug: open-logikio-managed-tables-table-rows-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Managed Tables > Tables API
  slug: open-logikio-managed-tables-tables-api
- collection_type: open
  name: Logik.io Admin API - Blueprint Import/Export Blueprint > Export Runtime - Bill of Materials API
  slug: open-logikio-runtime-bill-of-materials-api
common:
- group: other
  title: ''
  type: ParentCompany
  url: https://apis.io/providers/servicenow/
- group: other
  title: ''
  type: Overlay
  url: overlays/logikio-admin-blueprint-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://www.logik.io
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.logik.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.logik.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/logikioopensource
- group: build
  title: ''
  type: Postman
  url: postman/logikio-runtime.postman_collection.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/logikio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/logikio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/logikio-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/logikio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/logikio-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/logikio-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/logikio-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/logikio-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/logikio-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/logikio-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/logikio-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/logikio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/logikio-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/logikio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/logikio-rate-limits.yml
- group: operate
  title: ''
  type: Support
  url: https://support.logik.io/
created: '2026-07-17'
description: Logik.io is a headless, composable, API-first CPQ (Configure, Price, Quote) and product-configuration engine. It powers guided configuration, pricing, and quoting for complex products across Salesforce CPQ/Commerce and any headless front end, and computes Sales, Manufacturing, and Custom Bills of Materials. The platform exposes versioned Runtime APIs (start/update/save configurations, access Sets, retrieve BOMs) and Admin APIs (blueprints, fields, rules, managed data tables, jobs), authenticated with HTTP Bearer Runtime and Admin tokens. Logik.io was acquired by ServiceNow and is now also marketed as ServiceNow CPQ / Logik.ai; the developer surface at api-docs.logik.io and github.com/logikioopensource remains live and independent.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/logikio.png
layout: provider
mcp_servers:
- description: ''
  name: Logik.io MCP Server
  slug: logikio-mcp-server
modified: '2026-08-13'
name: Logik.io
nav: Providers
network: true
overview: 'Logik.io publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Blueprint > Export API, Blueprint > Import API, BOM API, and 8 more. Tagged areas include Company, Sales Tech, CPQ, Configure Price Quote, and Product Configuration.


  Logik.io''s developer surface includes documentation, API reference, authentication, sandbox, support, and 19 more developer resources.'
plans:
- name: Logikio Plans Pricing
  plan_count: 0
  slug: logikio-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Logikio Rate Limits
  slug: logikio-rate-limits
score:
  band: thin
  composite: 35.3
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 54.4
    developer_ergonomics: 47.0
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 35.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/logikio/refs/heads/main/screenshots/logikio-2026-07-25T225503.png
security:
- kind: authentication
  name: Logikio Authentication
  slug: logikio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Logikio Domain Security
  slug: logikio-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: logikio
tags:
- Company
- Sales Tech
- CPQ
- Configure Price Quote
- Product Configuration
- Bill of Materials
- E-Commerce
- Salesforce
- API-First
website: https://www.logik.io
---
