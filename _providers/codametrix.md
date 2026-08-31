---
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.2
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Codametrix Agentic Access
  operation_count: 8
  slug: codametrix-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: The component tree for the CodaMetrix platform.
  name: CodaMetrix Components API
  slug: codametrix-components-api
- description: Unplanned incidents and their update timelines.
  name: CodaMetrix Incidents API
  slug: codametrix-incidents-api
- description: Planned maintenance windows and their update timelines.
  name: CodaMetrix Scheduled Maintenances API
  slug: codametrix-scheduled-maintenances-api
- description: Overall page status rollup.
  name: CodaMetrix Status API
  slug: codametrix-status-api
- description: Combined rollup of status, components, unresolved incidents and active/upcoming maintenances.
  name: CodaMetrix Summary API
  slug: codametrix-summary-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: CodaMetrix Status Components API
  slug: open-codametrix-components-api
- collection_type: open
  name: CodaMetrix Status Incidents API
  slug: open-codametrix-incidents-api
- collection_type: open
  name: CodaMetrix Status Scheduled Maintenances API
  slug: open-codametrix-scheduled-maintenances-api
- collection_type: open
  name: CodaMetrix Status API
  slug: open-codametrix-status-api
- collection_type: open
  name: CodaMetrix Status Summary API
  slug: open-codametrix-summary-api
common:
- group: agent
  title: ''
  type: MCPServer
  url: mcp/codametrix-mcp.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/codametrix-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codametrix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codametrix.com/
- group: company
  title: ''
  type: Blog
  url: https://www.codametrix.com/resources
- group: operate
  title: ''
  type: Support
  url: mailto:hello@codametrix.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cdn.prod.website-files.com/684cc6638b0f0abf60033894/69efd0a7e96fba6f9ddd6d69_CodaMetrix_Privacy%20Policy-04-27-26.pdf
- group: operate
  title: ''
  type: StatusPage
  url: https://status.codametrix.com
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.codametrix.com
- group: auth
  title: ''
  type: Compliance
  url: https://trust.codametrix.com
- group: company
  title: ''
  type: Careers
  url: https://www.codametrix.com/careers
- group: other
  title: ''
  type: CaseStudies
  url: https://www.codametrix.com/case-studies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codametrix/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/codametrix_stock/
- group: build
  title: ''
  type: Examples
  url: examples/codametrix-status-api-examples.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/codametrix-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/codametrix-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/codametrix-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/codametrix-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/codametrix-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/codametrix-llms.txt
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/codametrix-status-openapi.yml
- group: docs
  title: ''
  type: Documentation
  url: https://status.codametrix.com/api/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/codametrix-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/codametrix-data-model.yml
- group: docs
  title: ''
  type: OpenAPIOverlay
  url: overlays/codametrix-status-overlay.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  title: ''
  type: StatusHistory
  url: https://status.codametrix.com/history.atom
- group: company
  title: ''
  type: About
  url: https://www.codametrix.com/about
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/CMXCodaMetrix/
created: '2026-08-02'
description: CodaMetrix is a Boston-based healthcare AI company that builds CMX CARE, an autonomous medical coding platform that translates clinical documentation into billing and diagnostic codes without human touch. Spun out of Mass General Brigham's physician billing organization in 2019, the platform combines machine learning, deep learning and natural language processing to produce a patient-centric, longitudinal view of the record and code across radiology, pathology, evaluation and management, endoscopy, emergency medicine and surgery. It is delivered as an AWS-hosted SaaS that integrates directly into the EHR (Epic Toolbox member, plus Cerner, Meditech and GE) rather than as a public developer API; the only publicly callable surface CodaMetrix operates is the unauthenticated Atlassian Statuspage Page API on status.codametrix.com. The company has raised $95M across Series A and Series B and was ranked No. 1 in the inaugural Best in KLAS category for autonomous medical coding.
examples:
- key_count: 2
  name: Codametrix Status Components
  slug: codametrix-status-components
- key_count: 2
  name: Codametrix Status Incidents Unresolved
  slug: codametrix-status-incidents-unresolved
- key_count: 2
  name: Codametrix Status Incidents
  slug: codametrix-status-incidents
- key_count: 2
  name: Codametrix Status Scheduled Maintenances Active
  slug: codametrix-status-scheduled-maintenances-active
- key_count: 2
  name: Codametrix Status Scheduled Maintenances Upcoming
  slug: codametrix-status-scheduled-maintenances-upcoming
- key_count: 2
  name: Codametrix Status Scheduled Maintenances
  slug: codametrix-status-scheduled-maintenances
- key_count: 2
  name: Codametrix Status Status
  slug: codametrix-status-status
- key_count: 5
  name: Codametrix Status Summary
  slug: codametrix-status-summary
image: https://cdn.prod.website-files.com/684cc6638b0f0abf60033894/6858a1d6db0f8dcba0f11337_CodaMetrix-CodeForBetter.png
layout: provider
mcp_servers:
- description: ''
  name: CodaMetrix MCP Server
  slug: codametrix-mcp-server
modified: '2026-08-04'
name: CodaMetrix
nav: Providers
network: true
overview: 'CodaMetrix publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Components API, Incidents API, Scheduled Maintenances API, and 2 more. Tagged areas include Company, healthcare, health-systems, medical-coding, and autonomous-coding.


  CodaMetrix''s developer surface includes engineering blog, support, code examples, authentication, documentation, and 25 more developer resources.'
random_paper: 1
score:
  band: thin
  composite: 39.1
  coverage:
    artifact_dirs: 18
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 71.4
    commercial_clarity: 71.4
    contract_governance: 18.2
    contract_quality: 16.5
    developer_ergonomics: 37.5
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 15.8
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 5
      marker_coverage: 100.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/codametrix/refs/heads/main/screenshots/codametrix-2026-08-07T163535.png
security:
- kind: authentication
  name: Codametrix Authentication
  slug: codametrix-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Codametrix Domain Security
  slug: codametrix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Codametrix Trust Center
  slug: codametrix-trust-center
  summary_line: SOC 2, SOC 2 Type 2, ISO 27001, HIPAA
slug: codametrix
tags:
- Company
- healthcare
- health-systems
- medical-coding
- autonomous-coding
- revenue-cycle-management
- clinical-documentation
- healthcare-ai
- machine-learning
- natural-language-processing
- ehr-integration
- Status
website: https://www.codametrix.com/
---
